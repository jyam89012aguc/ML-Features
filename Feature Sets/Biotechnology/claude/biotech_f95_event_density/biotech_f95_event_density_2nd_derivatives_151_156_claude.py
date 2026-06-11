"""Family f95 - Event density | silver DB event-code additions second derivatives 151-156."""
import numpy as np
import pandas as pd


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _has_code(eventcodes, code):
    return eventcodes.fillna("").astype(str).str.split("|").apply(lambda xs: code in xs).astype(float)


def _code_count(eventcodes):
    text = eventcodes.fillna("").astype(str)
    return text.where(text.ne(""), np.nan).str.count(r"\|").add(1).fillna(0.0)


def ed_f95_event_density_code_81_density_252d_slope_v151_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "81"), 252), 63))


def ed_f95_event_density_code_34_density_252d_slope_v152_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "34"), 252), 63))


def ed_f95_event_density_code_91_density_252d_slope_v153_signal(eventcodes):
    return _clean(_slope(_sum(_has_code(eventcodes, "91"), 252), 63))


def ed_f95_event_density_multicode_density_252d_slope_v154_signal(eventcodes):
    return _clean(_slope(_sum((_code_count(eventcodes) > 1).astype(float), 252), 63))


def ed_f95_event_density_code_breadth_252d_slope_v155_signal(eventcodes):
    return _clean(_slope(_mean(_code_count(eventcodes), 252), 63))


def ed_f95_event_density_recent_vs_long_multicode_mix_slope_v156_signal(eventcodes):
    multicode = (_code_count(eventcodes) > 1).astype(float)
    return _clean(_slope(_mean(multicode, 63) - _mean(multicode, 252), 63))
