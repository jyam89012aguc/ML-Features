"""Family f104 - Event-code intensity from silver DB events | base 001-012."""
import numpy as np
import pandas as pd


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _has_code(eventcodes, code):
    parts = eventcodes.fillna("").astype(str)
    return parts.str.split("|").apply(lambda xs: code in xs).astype(float)


def _code_count(eventcodes):
    text = eventcodes.fillna("").astype(str)
    return text.where(text.ne(""), np.nan).str.count(r"\|").add(1).fillna(0.0)


def _entropy_component(flag, w):
    p = _mean(flag, w).clip(1e-12, 1 - 1e-12)
    return -(p * np.log(p) + (1 - p) * np.log(1 - p))


def eci_f104_event_code_intensity_any_event_63d_base_v001_signal(eventcodes):
    result = _sum(eventcodes.fillna("").astype(str).ne("").astype(float), 63)
    return _clean(result)


def eci_f104_event_code_intensity_any_event_252d_base_v002_signal(eventcodes):
    result = _sum(eventcodes.fillna("").astype(str).ne("").astype(float), 252)
    return _clean(result)


def eci_f104_event_code_intensity_multicode_252d_base_v003_signal(eventcodes):
    result = _sum((_code_count(eventcodes) > 1).astype(float), 252)
    return _clean(result)


def eci_f104_event_code_intensity_code_81_252d_base_v004_signal(eventcodes):
    result = _sum(_has_code(eventcodes, "81"), 252)
    return _clean(result)


def eci_f104_event_code_intensity_code_34_252d_base_v005_signal(eventcodes):
    result = _sum(_has_code(eventcodes, "34"), 252)
    return _clean(result)


def eci_f104_event_code_intensity_code_91_252d_base_v006_signal(eventcodes):
    result = _sum(_has_code(eventcodes, "91"), 252)
    return _clean(result)


def eci_f104_event_code_intensity_code_22_252d_base_v007_signal(eventcodes):
    result = _sum(_has_code(eventcodes, "22"), 252)
    return _clean(result)


def eci_f104_event_code_intensity_code_71_252d_base_v008_signal(eventcodes):
    result = _sum(_has_code(eventcodes, "71"), 252)
    return _clean(result)


def eci_f104_event_code_intensity_code_52_252d_base_v009_signal(eventcodes):
    result = _sum(_has_code(eventcodes, "52"), 252)
    return _clean(result)


def eci_f104_event_code_intensity_code_breadth_252d_base_v010_signal(eventcodes):
    result = _mean(_code_count(eventcodes), 252)
    return _clean(result)


def eci_f104_event_code_intensity_common_code_entropy_252d_base_v011_signal(eventcodes):
    flags = [_has_code(eventcodes, c) for c in ("81", "34", "91", "22", "71", "52")]
    result = sum(_entropy_component(flag, 252) for flag in flags)
    return _clean(result)


def eci_f104_event_code_intensity_event_mix_shift_63d_252d_base_v012_signal(eventcodes):
    multicode = (_code_count(eventcodes) > 1).astype(float)
    result = _mean(multicode, 63) - _mean(multicode, 252)
    return _clean(result)
