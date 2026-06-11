"""Family f109 - Valuation normalization and invalid-multiple flags | base 001-012."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _bool(s):
    if s.dtype == bool:
        return s.astype(float)
    return s.fillna("").astype(str).str.upper().isin({"TRUE", "1", "Y"}).astype(float)


def vnf_f109_valuation_normalization_flags_negative_pe_base_v001_signal(has_negative_pe):
    return _clean(_bool(has_negative_pe))


def vnf_f109_valuation_normalization_flags_negative_pb_base_v002_signal(has_negative_pb):
    return _clean(_bool(has_negative_pb))


def vnf_f109_valuation_normalization_flags_negative_earnings_base_v003_signal(has_negative_earnings):
    return _clean(_bool(has_negative_earnings))


def vnf_f109_valuation_normalization_flags_negative_equity_base_v004_signal(has_negative_equity):
    return _clean(_bool(has_negative_equity))


def vnf_f109_valuation_normalization_flags_alternative_valuation_needed_base_v005_signal(alternative_valuation_needed):
    return _clean(_bool(alternative_valuation_needed))


def vnf_f109_valuation_normalization_flags_invalid_multiple_count_base_v006_signal(has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity, alternative_valuation_needed):
    result = _bool(has_negative_pe) + _bool(has_negative_pb) + _bool(has_negative_earnings) + _bool(has_negative_equity) + _bool(alternative_valuation_needed)
    return _clean(result)


def vnf_f109_valuation_normalization_flags_pb_normalized_gap_base_v007_signal(pb, pb_normalized):
    result = pb_normalized - pb
    return _clean(result)


def vnf_f109_valuation_normalization_flags_pe_normalized_gap_base_v008_signal(pe, pe_normalized):
    result = pe_normalized - pe
    return _clean(result)


def vnf_f109_valuation_normalization_flags_pb_validity_adjusted_base_v009_signal(pb, pb_normalized, has_negative_pb, has_negative_equity):
    result = pb_normalized.where((_bool(has_negative_pb) + _bool(has_negative_equity)).gt(0), pb)
    return _clean(result)


def vnf_f109_valuation_normalization_flags_pe_validity_adjusted_base_v010_signal(pe, pe_normalized, has_negative_pe, has_negative_earnings):
    result = pe_normalized.where((_bool(has_negative_pe) + _bool(has_negative_earnings)).gt(0), pe)
    return _clean(result)


def vnf_f109_valuation_normalization_flags_ps_vs_pe_normalized_base_v011_signal(ps, pe_normalized):
    result = _safe_div(ps, pe_normalized.abs())
    return _clean(result)


def vnf_f109_valuation_normalization_flags_252d_invalid_flag_rate_base_v012_signal(has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity):
    flags = ((_bool(has_negative_pe) + _bool(has_negative_pb) + _bool(has_negative_earnings) + _bool(has_negative_equity)) > 0).astype(float)
    result = _mean(flags, 252)
    return _clean(result)
