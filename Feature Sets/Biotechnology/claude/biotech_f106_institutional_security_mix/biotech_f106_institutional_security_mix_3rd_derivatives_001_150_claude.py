"""Family f106 - Institutional security-type mix from silver DB sf3a | third derivatives 001-012."""
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


def ism_f106_institutional_security_mix_put_value_share_accel_v001_signal(putvalue, totalvalue):
    result = _accel(_safe_div(putvalue, totalvalue.abs()), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_call_value_share_accel_v002_signal(cllvalue, totalvalue):
    result = _accel(_safe_div(cllvalue, totalvalue.abs()), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_put_call_value_skew_accel_v003_signal(putvalue, cllvalue):
    base = _safe_div(putvalue - cllvalue, putvalue.abs() + cllvalue.abs())
    result = _accel(base, 4)
    return _clean(result)


def ism_f106_institutional_security_mix_put_call_holder_skew_accel_v004_signal(putholders, cllholders):
    base = _safe_div(putholders - cllholders, putholders.abs() + cllholders.abs())
    result = _accel(base, 4)
    return _clean(result)


def ism_f106_institutional_security_mix_warrant_value_share_accel_v005_signal(wntvalue, totalvalue):
    result = _accel(_safe_div(wntvalue, totalvalue.abs()), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_debt_value_share_accel_v006_signal(dbtvalue, totalvalue):
    result = _accel(_safe_div(dbtvalue, totalvalue.abs()), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_preferred_value_share_accel_v007_signal(prfvalue, totalvalue):
    result = _accel(_safe_div(prfvalue, totalvalue.abs()), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_noncommon_value_share_accel_v008_signal(putvalue, cllvalue, wntvalue, dbtvalue, prfvalue, fndvalue, totalvalue):
    noncommon = putvalue.abs() + cllvalue.abs() + wntvalue.abs() + dbtvalue.abs() + prfvalue.abs() + fndvalue.abs()
    result = _accel(_safe_div(noncommon, totalvalue.abs()), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_common_value_share_accel_v009_signal(shrvalue, totalvalue):
    result = _accel(_safe_div(shrvalue, totalvalue.abs()), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_put_call_value_skew_4q_accel_v010_signal(putvalue, cllvalue):
    skew = _safe_div(putvalue - cllvalue, putvalue.abs() + cllvalue.abs())
    result = _accel(_mean(skew, 4), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_noncommon_holder_breadth_accel_v011_signal(putholders, cllholders, wntholders, dbtholders, prfholders, fndholders, shrholders):
    noncommon = putholders.abs() + cllholders.abs() + wntholders.abs() + dbtholders.abs() + prfholders.abs() + fndholders.abs()
    result = _accel(_safe_div(noncommon, shrholders.abs() + noncommon.abs()), 4)
    return _clean(result)


def ism_f106_institutional_security_mix_option_value_intensity_accel_v012_signal(putvalue, cllvalue, shrvalue):
    result = _accel(_safe_div(putvalue.abs() + cllvalue.abs(), shrvalue.abs()), 4)
    return _clean(result)
