"""Display helpers for notebook tables and other rich outputs."""

from __future__ import annotations

from typing import Any

import pandas as pd
from IPython.display import display

try:
    from pandas.io.formats.style import Styler
except Exception:  # pragma: no cover - defensive import for pandas variants
    Styler = ()


def _max_text_length(value: pd.DataFrame | pd.Series) -> int:
    if isinstance(value, pd.Series):
        if value.empty:
            return 0
        text = value.astype("string").fillna("")
        return int(text.str.len().max())

    object_like = value.select_dtypes(include=["object", "string"])
    if object_like.empty:
        return 0

    text = object_like.astype("string").fillna("")
    return int(text.apply(lambda col: col.str.len().max()).max())


def _max_label_length(value: pd.DataFrame | pd.Series) -> int:
    if isinstance(value, pd.Series):
        labels = [value.name] if value.name is not None else []
    else:
        labels = list(value.columns)
    return max((len(str(label)) for label in labels), default=0)


def _needs_wrapping(
    value: pd.DataFrame | pd.Series,
    *,
    wrap_threshold: int = 28,
) -> bool:
    return max(_max_text_length(value), _max_label_length(value)) > wrap_threshold


def display_wrapped(value: pd.DataFrame | pd.Series, max_width: str = "360px") -> Any:
    """Render a pandas object with wrapped cell text for long narrative tables."""

    if isinstance(value, pd.Series):
        name = value.name if value.name is not None else "value"
        value = value.to_frame(name=name)

    styler = value.style.set_properties(
        **{
            "white-space": "normal",
            "max-width": max_width,
            "text-align": "left",
            "vertical-align": "top",
        }
    ).set_table_styles(
        [
            {
                "selector": "th",
                "props": [("white-space", "normal"), ("text-align", "left")],
            }
        ]
    )
    return display(styler)


def smart_display(
    value: Any,
    *,
    max_width: str = "360px",
    wrap_threshold: int = 28,
) -> Any:
    """Display notebook output while automatically wrapping long pandas tables."""

    if Styler and isinstance(value, Styler):
        return display(value)

    if isinstance(value, (pd.DataFrame, pd.Series)):
        if _needs_wrapping(value, wrap_threshold=wrap_threshold):
            return display_wrapped(value, max_width=max_width)
        return display(value)

    return display(value)
