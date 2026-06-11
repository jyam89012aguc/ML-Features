"""Family f109 - Valuation normalization and invalid-multiple flags | third derivatives 001-012."""
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


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _bool(s):
    if s.dtype == bool:
        return s.astype(float)
    return s.fillna("").astype(str).str.upper().isin({"TRUE", "1", "Y"}).astype(float)


def vnf_f109_valuation_normalization_flags_negative_pe_accel_v001_signal(has_negative_pe):
    return _clean(_bool(has_negative_pe).diff(1).diff(1))


def vnf_f109_valuation_normalization_flags_negative_pb_accel_v002_signal(has_negative_pb):
    return _clean(_bool(has_negative_pb).diff(1).diff(1))


def vnf_f109_valuation_normalization_flags_negative_earnings_accel_v003_signal(has_negative_earnings):
    return _clean(_bool(has_negative_earnings).diff(1).diff(1))


def vnf_f109_valuation_normalization_flags_negative_equity_accel_v004_signal(has_negative_equity):
    return _clean(_bool(has_negative_equity).diff(1).diff(1))


def vnf_f109_valuation_normalization_flags_alternative_valuation_needed_accel_v005_signal(alternative_valuation_needed):
    return _clean(_bool(alternative_valuation_needed).diff(1).diff(1))


def vnf_f109_valuation_normalization_flags_invalid_multiple_count_accel_v006_signal(has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity, alternative_valuation_needed):
    base = _bool(has_negative_pe) + _bool(has_negative_pb) + _bool(has_negative_earnings) + _bool(has_negative_equity) + _bool(alternative_valuation_needed)
    return _clean(base.diff(1).diff(1))


def vnf_f109_valuation_normalization_flags_pb_normalized_gap_accel_v007_signal(pb, pb_normalized):
    return _clean(_accel(pb_normalized - pb, 63))


def vnf_f109_valuation_normalization_flags_pe_normalized_gap_accel_v008_signal(pe, pe_normalized):
    return _clean(_accel(pe_normalized - pe, 63))


def vnf_f109_valuation_normalization_flags_pb_validity_adjusted_accel_v009_signal(pb, pb_normalized, has_negative_pb, has_negative_equity):
    base = pb_normalized.where((_bool(has_negative_pb) + _bool(has_negative_equity)).gt(0), pb)
    return _clean(_accel(base, 63))


def vnf_f109_valuation_normalization_flags_pe_validity_adjusted_accel_v010_signal(pe, pe_normalized, has_negative_pe, has_negative_earnings):
    base = pe_normalized.where((_bool(has_negative_pe) + _bool(has_negative_earnings)).gt(0), pe)
    return _clean(_accel(base, 63))


def vnf_f109_valuation_normalization_flags_ps_vs_pe_normalized_accel_v011_signal(ps, pe_normalized):
    return _clean(_accel(_safe_div(ps, pe_normalized.abs()), 63))


def vnf_f109_valuation_normalization_flags_252d_invalid_flag_rate_accel_v012_signal(has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity):
    flags = ((_bool(has_negative_pe) + _bool(has_negative_pb) + _bool(has_negative_earnings) + _bool(has_negative_equity)) > 0).astype(float)
    return _clean(_accel(_mean(flags, 252), 63))
