"""Shared structured-output parsing utilities for notebook LLM workflows."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any

from pydantic import ValidationError

from .local_llm import clean_generated_text


DEFAULT_NESTED_KEYS = [
    "draft",
    "response",
    "answer",
    "result",
    "translation",
    "causal_question",
    "causal_question_draft",
    "causal_design",
]


@dataclass
class ParseResult:
    parsed: Any
    json_text: str
    notes: list[str]


def extract_json_object(text: Any) -> str | None:
    cleaned = clean_generated_text(text)
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned.strip())
    cleaned = re.sub(r"\s*```$", "", cleaned.strip())
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    return cleaned[start : end + 1]


def normalize_field_name(name: Any, aliases: dict[str, str] | None = None) -> str:
    aliases = aliases or {}
    key = re.sub(r"[^a-zA-Z0-9]+", "_", str(name).strip().lower()).strip("_")
    compact = key.replace("_", "")
    return aliases.get(key) or aliases.get(compact) or key


def normalize_scalar_value(value: Any, aliases: dict[str, str] | None = None) -> tuple[str, str | None]:
    aliases = aliases or {}
    text = scalar_to_text(value)
    key = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    compact = key.replace("_", "")
    canonical = aliases.get(key) or aliases.get(compact)
    if canonical is not None:
        return canonical, f"normalized scalar value {text!r} to {canonical!r}"
    for alias_key, alias_value in sorted(aliases.items(), key=lambda item: len(item[0].replace("_", "")), reverse=True):
        normalized_alias = re.sub(r"[^a-zA-Z0-9]+", "_", str(alias_key).strip().lower()).strip("_")
        compact_alias = normalized_alias.replace("_", "")
        if not compact_alias:
            continue
        if (
            key.startswith(normalized_alias)
            or normalized_alias in key
            or compact.startswith(compact_alias)
            or compact_alias in compact
        ):
            return alias_value, f"fuzzy-normalized scalar value {text!r} to {alias_value!r}"
    return text, None


def scalar_to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return clean_generated_text(value)
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, list):
        return "; ".join(scalar_to_text(item) for item in value if scalar_to_text(item))
    if isinstance(value, dict):
        if len(value) == 1:
            return scalar_to_text(next(iter(value.values())))
        pieces = []
        for key, item in value.items():
            text = scalar_to_text(item)
            if text:
                pieces.append(f"{key}: {text}")
        return "; ".join(pieces)
    return clean_generated_text(str(value))


def split_list_like_string(value: Any) -> list[str]:
    value = clean_generated_text(value)
    if not value:
        return []
    if ";" in value or "\n" in value:
        pieces = re.split(r";|\n", value)
    elif re.search(r",\s+(?:and\s+)?[a-zA-Z]", value):
        pieces = re.split(r",\s*", value)
    else:
        pieces = [value]
    cleaned = [piece.strip(" .-") for piece in pieces if piece.strip(" .-")]
    return cleaned or [value]


def coerce_to_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [scalar_to_text(item).strip() for item in value if scalar_to_text(item).strip()]
    if isinstance(value, str):
        return split_list_like_string(value)
    if value is None:
        return []
    return [scalar_to_text(value)]


def unwrap_container(data: Any, nested_keys: list[str] | None = None) -> tuple[Any, list[str]]:
    nested_keys = nested_keys or DEFAULT_NESTED_KEYS
    if isinstance(data, list) and len(data) == 1 and isinstance(data[0], dict):
        return data[0], ["unwrapped single-item list"]
    if not isinstance(data, dict):
        return data, []

    for key in nested_keys:
        value = data.get(key)
        if isinstance(value, dict):
            return value, [f"unwrapped nested {key}"]
    return data, []


def normalize_schema_candidate(
    candidate: str,
    *,
    scalar_fields: list[str] | None = None,
    list_fields: list[str] | None = None,
    field_aliases: dict[str, str] | None = None,
    value_aliases: dict[str, dict[str, str]] | None = None,
    nested_keys: list[str] | None = None,
    defaults: dict[str, Any] | None = None,
) -> tuple[str, list[str]]:
    scalar_fields = scalar_fields or []
    list_fields = list_fields or []
    field_aliases = field_aliases or {}
    value_aliases = value_aliases or {}
    defaults = defaults or {}

    data = json.loads(candidate)
    data, notes = unwrap_container(data, nested_keys=nested_keys)
    if not isinstance(data, dict):
        raise TypeError(f"expected JSON object, got {type(data).__name__}")

    normalized: dict[str, Any] = {}
    allowed = set(scalar_fields) | set(list_fields)
    for key, value in data.items():
        normalized_key = normalize_field_name(key, field_aliases)
        if normalized_key in allowed:
            normalized[normalized_key] = value
        else:
            normalized[key] = value

    for key, value in defaults.items():
        if key not in normalized:
            normalized[key] = value
            notes.append(f"defaulted missing {key}")

    for field in scalar_fields:
        if field in normalized:
            original_type = type(normalized[field]).__name__
            normalized[field], value_note = normalize_scalar_value(normalized[field], value_aliases.get(field))
            if original_type != "str":
                notes.append(f"coerced {field} from {original_type} to string")
            if value_note:
                notes.append(f"{field}: {value_note}")

    for field in list_fields:
        value = normalized.get(field, [])
        if not isinstance(value, list):
            notes.append(f"coerced {field} from {type(value).__name__} to list")
        elif any(not isinstance(item, str) for item in value):
            notes.append(f"coerced non-string items in {field} to strings")
        normalized[field] = coerce_to_list(value)

    return json.dumps(normalized), notes


def parse_pydantic_output(
    raw_output: Any,
    model_class: type[Any],
    *,
    scalar_fields: list[str] | None = None,
    list_fields: list[str] | None = None,
    field_aliases: dict[str, str] | None = None,
    value_aliases: dict[str, dict[str, str]] | None = None,
    nested_keys: list[str] | None = None,
    defaults: dict[str, Any] | None = None,
) -> ParseResult:
    candidates = [clean_generated_text(raw_output)]
    extracted = extract_json_object(raw_output)
    if extracted is not None and extracted not in candidates:
        candidates.append(extracted)

    errors: list[str] = []
    for candidate in candidates:
        try:
            return ParseResult(model_class.model_validate_json(candidate), candidate, errors)
        except ValidationError as error:
            errors.append(error.errors()[0]["msg"])

        try:
            repaired_candidate, notes = normalize_schema_candidate(
                candidate,
                scalar_fields=scalar_fields,
                list_fields=list_fields,
                field_aliases=field_aliases,
                value_aliases=value_aliases,
                nested_keys=nested_keys,
                defaults=defaults,
            )
            return ParseResult(model_class.model_validate_json(repaired_candidate), repaired_candidate, errors + notes)
        except (TypeError, json.JSONDecodeError, ValidationError) as error:
            errors.append(str(error).splitlines()[0])

    raise ValueError(f"No valid {model_class.__name__} found. Parser errors: {errors}")
