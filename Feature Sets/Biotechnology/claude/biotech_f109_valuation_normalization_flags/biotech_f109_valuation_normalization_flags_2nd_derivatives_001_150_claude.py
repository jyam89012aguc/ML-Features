"""Family f109 - Valuation normalization and invalid-multiple flags | second derivatives 001-012."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _bool(s):
    if s.dtype == bool:
        return s.astype(float)
    return s.fillna("").astype(str).str.upper().isin({"TRUE", "1", "Y"}).astype(float)


def vnf_f109_valuation_normalization_flags_negative_pe_slope_v001_signal(has_negative_pe):
    return _clean(_bool(has_negative_pe).diff(1))


def vnf_f109_valuation_normalization_flags_negative_pb_slope_v002_signal(has_negative_pb):
    return _clean(_bool(has_negative_pb).diff(1))


def vnf_f109_valuation_normalization_flags_negative_earnings_slope_v003_signal(has_negative_earnings):
    return _clean(_bool(has_negative_earnings).diff(1))


def vnf_f109_valuation_normalization_flags_negative_equity_slope_v004_signal(has_negative_equity):
    return _clean(_bool(has_negative_equity).diff(1))


def vnf_f109_valuation_normalization_flags_alternative_valuation_needed_slope_v005_signal(alternative_valuation_needed):
    return _clean(_bool(alternative_valuation_needed).diff(1))


def vnf_f109_valuation_normalization_flags_invalid_multiple_count_slope_v006_signal(has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity, alternative_valuation_needed):
    base = _bool(has_negative_pe) + _bool(has_negative_pb) + _bool(has_negative_earnings) + _bool(has_negative_equity) + _bool(alternative_valuation_needed)
    return _clean(base.diff(1))


def vnf_f109_valuation_normalization_flags_pb_normalized_gap_slope_v007_signal(pb, pb_normalized):
    return _clean(_slope(pb_normalized - pb, 63))


def vnf_f109_valuation_normalization_flags_pe_normalized_gap_slope_v008_signal(pe, pe_normalized):
    return _clean(_slope(pe_normalized - pe, 63))


def vnf_f109_valuation_normalization_flags_pb_validity_adjusted_slope_v009_signal(pb, pb_normalized, has_negative_pb, has_negative_equity):
    base = pb_normalized.where((_bool(has_negative_pb) + _bool(has_negative_equity)).gt(0), pb)
    return _clean(_slope(base, 63))


def vnf_f109_valuation_normalization_flags_pe_validity_adjusted_slope_v010_signal(pe, pe_normalized, has_negative_pe, has_negative_earnings):
    base = pe_normalized.where((_bool(has_negative_pe) + _bool(has_negative_earnings)).gt(0), pe)
    return _clean(_slope(base, 63))


def vnf_f109_valuation_normalization_flags_ps_vs_pe_normalized_slope_v011_signal(ps, pe_normalized):
    return _clean(_slope(_safe_div(ps, pe_normalized.abs()), 63))


def vnf_f109_valuation_normalization_flags_252d_invalid_flag_rate_slope_v012_signal(has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity):
    flags = ((_bool(has_negative_pe) + _bool(has_negative_pb) + _bool(has_negative_earnings) + _bool(has_negative_equity)) > 0).astype(float)
    return _clean(_slope(_mean(flags, 252), 63))
