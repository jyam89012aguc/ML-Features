"""Family f104 - Event-code intensity from silver DB events | second derivatives 001-012."""
import numpy as np
import pandas as pd


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _has_code(eventcodes, code):
    return eventcodes.fillna("").astype(str).str.split("|").apply(lambda xs: code in xs).astype(float)


def _code_count(eventcodes):
    text = eventcodes.fillna("").astype(str)
    return text.where(text.ne(""), np.nan).str.count(r"\|").add(1).fillna(0.0)


def _entropy_component(flag, w):
    p = _mean(flag, w).clip(1e-12, 1 - 1e-12)
    return -(p * np.log(p) + (1 - p) * np.log(1 - p))


def eci_f104_event_code_intensity_any_event_63d_slope_v001_signal(eventcodes):
    return _clean(_slope(_sum(eventcodes.fillna("").astype(str).ne("").astype(float), 63), 21))


def eci_f104_event_code_intensity_any_event_252d_slope_v002_signal(eventcodes):
    return _clean(_slope(_sum(eventcodes.fillna("").astype(str).ne("").astype(float), 252), 63))


def eci_f104_event_code_intensity_multicode_252d_slope_v003_signal(eventcodes):
    return _clean(_slope(_sum((_code_count(eventcodes) > 1).astype(float), 252), 63))


def eci_f104_event_code_intensity_code_81_252d_slope_v004_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "81"), 252), 63))


def eci_f104_event_code_intensity_code_34_252d_slope_v005_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "34"), 252), 63))


def eci_f104_event_code_intensity_code_91_252d_slope_v006_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "91"), 252), 63))


def eci_f104_event_code_intensity_code_22_252d_slope_v007_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "22"), 252), 63))


def eci_f104_event_code_intensity_code_71_252d_slope_v008_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "71"), 252), 63))


def eci_f104_event_code_intensity_code_52_252d_slope_v009_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "52"), 252), 63))


def eci_f104_event_code_intensity_code_breadth_252d_slope_v010_signal(eventcodes):
    return _clean(_slope(_mean(_code_count(eventcodes), 252), 63))


def eci_f104_event_code_intensity_common_code_entropy_252d_slope_v011_signal(eventcodes):
    flags = [_has_code(eventcodes, c) for c in ("81", "34", "91", "22", "71", "52")]
    base = sum(_entropy_component(flag, 252) for flag in flags)
    return _clean(_slope(base, 63))


def eci_f104_event_code_intensity_event_mix_shift_63d_252d_slope_v012_signal(eventcodes):
    multicode = (_code_count(eventcodes) > 1).astype(float)
    base = _mean(multicode, 63) - _mean(multicode, 252)
    return _clean(_slope(base, 63))
