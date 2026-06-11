"""Family f106 - Institutional security-type mix from silver DB sf3a | base 001-012."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


# Put value share of total institutional value
def ism_f106_institutional_security_mix_put_value_share_base_v001_signal(putvalue, totalvalue):
    result = _safe_div(putvalue, totalvalue.abs())
    return _clean(result)


# Call value share of total institutional value
def ism_f106_institutional_security_mix_call_value_share_base_v002_signal(cllvalue, totalvalue):
    result = _safe_div(cllvalue, totalvalue.abs())
    return _clean(result)


# Put/call value skew
def ism_f106_institutional_security_mix_put_call_value_skew_base_v003_signal(putvalue, cllvalue):
    result = _safe_div(putvalue - cllvalue, (putvalue.abs() + cllvalue.abs()))
    return _clean(result)


# Put/call holder skew
def ism_f106_institutional_security_mix_put_call_holder_skew_base_v004_signal(putholders, cllholders):
    result = _safe_div(putholders - cllholders, (putholders.abs() + cllholders.abs()))
    return _clean(result)


# Warrant value share
def ism_f106_institutional_security_mix_warrant_value_share_base_v005_signal(wntvalue, totalvalue):
    result = _safe_div(wntvalue, totalvalue.abs())
    return _clean(result)


# Debt security value share
def ism_f106_institutional_security_mix_debt_value_share_base_v006_signal(dbtvalue, totalvalue):
    result = _safe_div(dbtvalue, totalvalue.abs())
    return _clean(result)


# Preferred security value share
def ism_f106_institutional_security_mix_preferred_value_share_base_v007_signal(prfvalue, totalvalue):
    result = _safe_div(prfvalue, totalvalue.abs())
    return _clean(result)


# Non-common institutional value share
def ism_f106_institutional_security_mix_noncommon_value_share_base_v008_signal(putvalue, cllvalue, wntvalue, dbtvalue, prfvalue, fndvalue, totalvalue):
    noncommon = putvalue.abs() + cllvalue.abs() + wntvalue.abs() + dbtvalue.abs() + prfvalue.abs() + fndvalue.abs()
    result = _safe_div(noncommon, totalvalue.abs())
    return _clean(result)


# Common share value concentration
def ism_f106_institutional_security_mix_common_value_share_base_v009_signal(shrvalue, totalvalue):
    result = _safe_div(shrvalue, totalvalue.abs())
    return _clean(result)


# 4-quarter smoothed put/call value skew
def ism_f106_institutional_security_mix_put_call_value_skew_4q_base_v010_signal(putvalue, cllvalue):
    skew = _safe_div(putvalue - cllvalue, (putvalue.abs() + cllvalue.abs()))
    result = _mean(skew, 4)
    return _clean(result)


# Holder breadth outside common stock
def ism_f106_institutional_security_mix_noncommon_holder_breadth_base_v011_signal(putholders, cllholders, wntholders, dbtholders, prfholders, fndholders, shrholders):
    noncommon = putholders.abs() + cllholders.abs() + wntholders.abs() + dbtholders.abs() + prfholders.abs() + fndholders.abs()
    result = _safe_div(noncommon, shrholders.abs() + noncommon.abs())
    return _clean(result)


# Institutional option intensity
def ism_f106_institutional_security_mix_option_value_intensity_base_v012_signal(putvalue, cllvalue, shrvalue):
    result = _safe_div(putvalue.abs() + cllvalue.abs(), shrvalue.abs())
    return _clean(result)
