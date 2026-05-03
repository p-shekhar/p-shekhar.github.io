"""Robust local LLM utilities for the AI and causal inference notebooks.

The notebooks intentionally compare several model families. Those families do
not all share the same tokenizer, processor, chat template, or Transformers
model class. Centralizing those quirks here keeps notebook examples focused on
causal analysis rather than repeated model plumbing.
"""

from __future__ import annotations

import gc
import importlib.util
import os
import re
from dataclasses import dataclass
from functools import lru_cache
from typing import Any

import numpy as np
import torch

os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("TRANSFORMERS_NO_ADVISORY_WARNINGS", "1")


@dataclass(frozen=True)
class ModelSpec:
    label: str
    model_id: str
    role: str


LOCAL_SMOKE_TEST_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"
LOCAL_FAST_MODEL = "Qwen/Qwen2.5-7B-Instruct"
LOCAL_STRONG_MODEL = "Qwen/Qwen2.5-14B-Instruct"
LOCAL_SCALE_MODEL = "Qwen/Qwen2.5-32B-Instruct"
LOCAL_ALT_REASONING_MODEL = "microsoft/Phi-3.5-mini-instruct"
LOCAL_ALT_OPEN_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"
LOCAL_MISTRAL_SMALL_MODEL = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
LOCAL_GEMMA_MODEL = "google/gemma-3-27b-it"
LOCAL_LLAMA_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct"

DEFAULT_MODELS_TO_COMPARE: list[tuple[str, str, str]] = [
    ("Qwen 0.5B", LOCAL_SMOKE_TEST_MODEL, "pipeline smoke test"),
    ("Qwen 7B", LOCAL_FAST_MODEL, "fast default"),
    ("Qwen 14B", LOCAL_STRONG_MODEL, "strong local analysis"),
    ("Qwen 32B", LOCAL_SCALE_MODEL, "scale comparison"),
    ("Phi mini", LOCAL_ALT_REASONING_MODEL, "compact non-Qwen comparison"),
    ("Mistral 7B", LOCAL_ALT_OPEN_MODEL, "7B model-family comparison"),
    ("Mistral Small 24B", LOCAL_MISTRAL_SMALL_MODEL, "strong non-Qwen comparison"),
    ("Gemma 3 27B", LOCAL_GEMMA_MODEL, "large non-Qwen comparison"),
    ("Llama 3.1 8B", LOCAL_LLAMA_MODEL, "industry-standard instruct baseline"),
]


def has_package(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def get_device() -> str:
    return "cuda" if torch.cuda.is_available() else "cpu"


def set_generation_seed(seed: int = 123) -> None:
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def clean_generated_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    replacements = {
        "Ċ": "\n",
        "Ġ": " ",
        "ĉ": "\t",
        "<0x0A>": "\n",
        "<|im_end|>": "",
        "<|endoftext|>": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clear_gpu_memory() -> None:
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def disable_model_progress_bars() -> None:
    """Avoid Jupyter widget progress outputs that break static HTML rendering."""

    os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
    try:
        from huggingface_hub.utils import disable_progress_bars

        disable_progress_bars()
    except Exception:
        pass

    try:
        from transformers.utils import logging as transformers_logging

        transformers_logging.disable_progress_bar()
    except Exception:
        pass


def _dtype_for_model(model_id: str) -> torch.dtype:
    if not torch.cuda.is_available():
        return torch.float32
    if model_id.startswith("google/gemma-3"):
        return torch.bfloat16
    return torch.float16


def _load_kwargs(model_id: str, *, local_files_only: bool = True) -> dict[str, Any]:
    kwargs: dict[str, Any] = {
        "local_files_only": local_files_only,
        "trust_remote_code": True,
    }
    if model_id.startswith("mistralai/Mistral-Small"):
        kwargs["fix_mistral_regex"] = True
    return kwargs


@lru_cache(maxsize=2)
def load_local_model(model_id: str, *, local_files_only: bool = True) -> tuple[Any, Any]:
    """Load a local Hugging Face model with model-family-specific fallbacks."""

    disable_model_progress_bars()

    from transformers import AutoModelForCausalLM, AutoProcessor, AutoTokenizer

    clear_gpu_memory()
    dtype = _dtype_for_model(model_id)

    if model_id.startswith("google/gemma-3"):
        from transformers import Gemma3ForConditionalGeneration

        processor = AutoProcessor.from_pretrained(model_id, local_files_only=local_files_only)
        model = Gemma3ForConditionalGeneration.from_pretrained(
            model_id,
            device_map="auto" if torch.cuda.is_available() and has_package("accelerate") else None,
            dtype=dtype,
            low_cpu_mem_usage=torch.cuda.is_available() and has_package("accelerate"),
            local_files_only=local_files_only,
        )
        if not (torch.cuda.is_available() and has_package("accelerate")):
            model.to(get_device())
        model.eval()
        return processor, model

    if model_id.startswith("mistralai/Mistral-Small"):
        from transformers import Mistral3ForConditionalGeneration

        tokenizer = AutoTokenizer.from_pretrained(model_id, **_load_kwargs(model_id, local_files_only=local_files_only))
        model = Mistral3ForConditionalGeneration.from_pretrained(
            model_id,
            device_map="auto" if torch.cuda.is_available() and has_package("accelerate") else None,
            dtype=dtype,
            low_cpu_mem_usage=torch.cuda.is_available() and has_package("accelerate"),
            local_files_only=local_files_only,
            trust_remote_code=True,
        )
        if not (torch.cuda.is_available() and has_package("accelerate")):
            model.to(get_device())
        model.eval()
        return tokenizer, model

    if model_id.startswith("microsoft/Phi-3.5"):
        from transformers import LlamaTokenizerFast, Phi3Config, Phi3ForCausalLM

        tokenizer = LlamaTokenizerFast.from_pretrained(model_id, local_files_only=local_files_only)
        config = Phi3Config.from_pretrained(model_id, local_files_only=local_files_only)
        model = Phi3ForCausalLM.from_pretrained(
            model_id,
            config=config,
            device_map="auto" if torch.cuda.is_available() and has_package("accelerate") else None,
            dtype=dtype,
            low_cpu_mem_usage=torch.cuda.is_available() and has_package("accelerate"),
            local_files_only=local_files_only,
            trust_remote_code=True,
        )
        if not (torch.cuda.is_available() and has_package("accelerate")):
            model.to(get_device())
        model.eval()
        return tokenizer, model

    tokenizer = AutoTokenizer.from_pretrained(model_id, **_load_kwargs(model_id, local_files_only=local_files_only))
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto" if torch.cuda.is_available() and has_package("accelerate") else None,
        dtype=dtype,
        low_cpu_mem_usage=torch.cuda.is_available() and has_package("accelerate"),
        local_files_only=local_files_only,
        trust_remote_code=True,
    )
    if not (torch.cuda.is_available() and has_package("accelerate")):
        model.to(get_device())
    model.eval()
    return tokenizer, model


def clear_loaded_model_cache() -> None:
    load_local_model.cache_clear()
    clear_gpu_memory()


def build_chat_messages(system_message: str, user_message: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]


def build_text_only_messages(system_message: str, user_message: str) -> list[dict[str, Any]]:
    combined = f"{system_message}\n\n{user_message}".strip()
    return [{"role": "user", "content": [{"type": "text", "text": combined}]}]


def build_gemma_messages(system_message: str, user_message: str) -> list[dict[str, Any]]:
    return build_text_only_messages(system_message, user_message)


def build_mistral_small_prompt(system_message: str, user_message: str) -> str:
    return f"<s>[INST] {system_message.strip()}\n\n{user_message.strip()} [/INST]"


def build_phi_prompt(system_message: str, user_message: str) -> str:
    return f"<|system|>\n{system_message.strip()}<|end|>\n<|user|>\n{user_message.strip()}<|end|>\n<|assistant|>\n"


def format_chat_prompt(tokenizer: Any, system_message: str, user_message: str, model_id: str | None = None) -> str:
    if model_id and model_id.startswith("mistralai/Mistral-Small"):
        return build_mistral_small_prompt(system_message, user_message)
    if model_id and model_id.startswith("microsoft/Phi-3.5"):
        return build_phi_prompt(system_message, user_message)

    base_tokenizer = getattr(tokenizer, "tokenizer", tokenizer)
    chat_template = getattr(tokenizer, "chat_template", None) or getattr(base_tokenizer, "chat_template", None)
    if hasattr(tokenizer, "apply_chat_template") and chat_template is not None:
        return tokenizer.apply_chat_template(build_chat_messages(system_message, user_message), tokenize=False, add_generation_prompt=True)
    return f"System: {system_message}\n\nUser: {user_message}\n\nAssistant:"


def prepare_chat_inputs(tokenizer: Any, system_message: str, user_message: str, model_id: str) -> Any:
    if model_id.startswith("google/gemma-3"):
        return tokenizer.apply_chat_template(
            build_gemma_messages(system_message, user_message),
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
            return_dict=True,
        )

    if model_id.startswith("mistralai/Mistral-Small"):
        return tokenizer(build_mistral_small_prompt(system_message, user_message), return_tensors="pt", return_dict=True)

    base_tokenizer = getattr(tokenizer, "tokenizer", tokenizer)
    chat_template = getattr(tokenizer, "chat_template", None) or getattr(base_tokenizer, "chat_template", None)
    if hasattr(tokenizer, "apply_chat_template") and chat_template is not None:
        return tokenizer.apply_chat_template(
            build_chat_messages(system_message, user_message),
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
            return_dict=True,
        )

    if model_id.startswith("microsoft/Phi-3.5"):
        return tokenizer(build_phi_prompt(system_message, user_message), return_tensors="pt", return_dict=True)

    prompt = format_chat_prompt(tokenizer, system_message, user_message, model_id=model_id)
    return tokenizer(prompt, return_tensors="pt", return_dict=True)


def build_chat_inputs(tokenizer: Any, system_message: str, user_message: str, model_id: str) -> Any:
    return prepare_chat_inputs(tokenizer, system_message, user_message, model_id)


def move_inputs_to_model_device(inputs: Any, model: Any) -> Any:
    if hasattr(model, "hf_device_map"):
        for device in model.hf_device_map.values():
            if isinstance(device, str) and device not in {"cpu", "disk", "meta"}:
                return inputs.to(device)
            if isinstance(device, int):
                return inputs.to(f"cuda:{device}")
        return inputs
    return inputs.to(getattr(model, "device", get_device()))


def decode_generated_response(tokenizer: Any, output_ids: Any, input_length: int, model_id: str | None = None) -> str:
    decoder = getattr(tokenizer, "tokenizer", tokenizer)
    generated_ids = output_ids[0, input_length:]
    return clean_generated_text(decoder.decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False))


def generate_local_response(
    user_message: str,
    *,
    system_message: str | None = None,
    model_id: str,
    max_new_tokens: int = 600,
    temperature: float = 0.0,
    seed: int = 123,
    enabled: bool = True,
    local_files_only: bool = True,
) -> str:
    if not enabled:
        raise RuntimeError("Local LLM execution is disabled for this notebook run.")

    set_generation_seed(seed)
    system_message = system_message or (
        "You are a careful causal inference assistant. Give final answers only; do not include scratch work."
    )
    tokenizer, model = load_local_model(model_id, local_files_only=local_files_only)
    inputs = prepare_chat_inputs(tokenizer, system_message, user_message, model_id=model_id)
    inputs = move_inputs_to_model_device(inputs, model)
    prompt_token_count = inputs["input_ids"].shape[-1]

    decoder = getattr(tokenizer, "tokenizer", tokenizer)
    pad_token_id = getattr(decoder, "pad_token_id", None) or getattr(decoder, "eos_token_id", None)
    if pad_token_id is None and getattr(model, "generation_config", None) is not None:
        pad_token_id = getattr(model.generation_config, "eos_token_id", None)

    generation_kwargs: dict[str, Any] = {
        "max_new_tokens": max_new_tokens,
        "do_sample": temperature > 0,
        "pad_token_id": pad_token_id,
    }
    if temperature > 0:
        generation_kwargs["temperature"] = temperature
    generation_kwargs = {key: value for key, value in generation_kwargs.items() if value is not None}

    with torch.inference_mode():
        output_ids = model.generate(**inputs, **generation_kwargs)

    return decode_generated_response(tokenizer, output_ids, prompt_token_count, model_id=model_id)


def local_chat(
    user_message: str,
    system_message: str | None = None,
    *,
    model_id: str,
    max_new_tokens: int = 600,
    temperature: float = 0.0,
    seed: int = 123,
    enabled: bool = True,
    local_files_only: bool = True,
) -> str:
    return generate_local_response(
        user_message,
        system_message=system_message,
        model_id=model_id,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        seed=seed,
        enabled=enabled,
        local_files_only=local_files_only,
    )
