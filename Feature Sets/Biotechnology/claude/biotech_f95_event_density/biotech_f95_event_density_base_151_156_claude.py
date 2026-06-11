"""Family f95 - Event density | silver DB event-code additions base 151-156."""
import numpy as np
import pandas as pd


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _has_code(eventcodes, code):
    return eventcodes.fillna("").astype(str).str.split("|").apply(lambda xs: code in xs).astype(float)


def _code_count(eventcodes):
    text = eventcodes.fillna("").astype(str)
    return text.where(text.ne(""), np.nan).str.count(r"\|").add(1).fillna(0.0)


def ed_f95_event_density_code_81_density_252d_base_v151_signal(eventcodes):
    return _clean(_sum(_has_code(eventcodes, "81"), 252))


def ed_f95_event_density_code_34_density_252d_base_v152_signal(eventcodes):
    return _clean(_sum(_has_code(eventcodes, "34"), 252))


def ed_f95_event_density_code_91_density_252d_base_v153_signal(eventcodes):
    return _clean(_sum(_has_code(eventcodes, "91"), 252))


def ed_f95_event_density_multicode_density_252d_base_v154_signal(eventcodes):
    return _clean(_sum((_code_count(eventcodes) > 1).astype(float), 252))


def ed_f95_event_density_code_breadth_252d_base_v155_signal(eventcodes):
    return _clean(_mean(_code_count(eventcodes), 252))


def ed_f95_event_density_recent_vs_long_multicode_mix_base_v156_signal(eventcodes):
    multicode = (_code_count(eventcodes) > 1).astype(float)
    return _clean(_mean(multicode, 63) - _mean(multicode, 252))
