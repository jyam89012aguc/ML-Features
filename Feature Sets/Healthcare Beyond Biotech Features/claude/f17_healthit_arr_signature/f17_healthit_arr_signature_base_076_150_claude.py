import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f17_arr_proxy(revenue, deferredrev, w):
    smooth_rev = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (smooth_rev + deferredrev) / revenue.replace(0, np.nan).abs()


def _f17_revenue_recurring_share(deferredrev, revenue, w):
    rev_w = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return deferredrev / rev_w.replace(0, np.nan).abs()


def _f17_arr_quality(revenue, deferredrev, w):
    rev_std = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    rev_mean = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    cv = rev_std / rev_mean.replace(0, np.nan).abs()
    return deferredrev / revenue.replace(0, np.nan).abs() / cv.replace(0, np.nan)


# ===== features =====
def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v076_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v077_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v078_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 126).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v079_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 126).rolling(21, min_periods=max(1, 21 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 126).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v080_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 126).rolling(63, min_periods=max(1, 63 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 126).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_126d_base_v081_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 126).rolling(252, min_periods=max(1, 252 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 126).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v082_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v083_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v084_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v085_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v086_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v087_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v088_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v089_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v090_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v091_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v092_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v093_signal(revenue, deferredrev, closeadj):
    result = (-_f17_arr_proxy(revenue, deferredrev, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v094_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252) * _f17_arr_proxy(revenue, deferredrev, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v095_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v096_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v097_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v098_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v099_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v100_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v101_signal(revenue, deferredrev, closeadj):
    result = np.log(_f17_arr_proxy(revenue, deferredrev, 252).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v102_signal(revenue, deferredrev, closeadj):
    result = np.sign(_f17_arr_proxy(revenue, deferredrev, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v103_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v104_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v105_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 252).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v106_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 252).rolling(21, min_periods=max(1, 21 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 252).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v107_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 252).rolling(63, min_periods=max(1, 63 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 252).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_252d_base_v108_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 252).rolling(252, min_periods=max(1, 252 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 252).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v109_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v110_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v111_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v112_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v113_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v114_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v115_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v116_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v117_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v118_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v119_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v120_signal(revenue, deferredrev, closeadj):
    result = (-_f17_arr_proxy(revenue, deferredrev, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v121_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5) * _f17_arr_proxy(revenue, deferredrev, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v122_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v123_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v124_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v125_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v126_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v127_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v128_signal(revenue, deferredrev, closeadj):
    result = np.log(_f17_arr_proxy(revenue, deferredrev, 5).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v129_signal(revenue, deferredrev, closeadj):
    result = np.sign(_f17_arr_proxy(revenue, deferredrev, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v130_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v131_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v132_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 5).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v133_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 5).rolling(21, min_periods=max(1, 21 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 5).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v134_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 5).rolling(63, min_periods=max(1, 63 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 5).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_5d_base_v135_signal(revenue, deferredrev, closeadj):
    result = (_f17_arr_proxy(revenue, deferredrev, 5).rolling(252, min_periods=max(1, 252 // 2)).max() - _f17_arr_proxy(revenue, deferredrev, 5).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v136_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v137_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v138_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v139_signal(revenue, deferredrev, closeadj):
    result = _mean(_f17_arr_proxy(revenue, deferredrev, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v140_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v141_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v142_signal(revenue, deferredrev, closeadj):
    result = _std(_f17_arr_proxy(revenue, deferredrev, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v143_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v144_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v145_signal(revenue, deferredrev, closeadj):
    result = _z(_f17_arr_proxy(revenue, deferredrev, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v146_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v147_signal(revenue, deferredrev, closeadj):
    result = (-_f17_arr_proxy(revenue, deferredrev, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v148_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 42) * _f17_arr_proxy(revenue, deferredrev, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v149_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 42).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17has_f17_healthit_arr_signature_arrproxy_42d_base_v150_signal(revenue, deferredrev, closeadj):
    result = _f17_arr_proxy(revenue, deferredrev, 42).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v076_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v077_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v078_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v079_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v080_signal,
    f17has_f17_healthit_arr_signature_arrproxy_126d_base_v081_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v082_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v083_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v084_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v085_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v086_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v087_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v088_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v089_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v090_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v091_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v092_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v093_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v094_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v095_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v096_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v097_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v098_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v099_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v100_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v101_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v102_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v103_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v104_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v105_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v106_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v107_signal,
    f17has_f17_healthit_arr_signature_arrproxy_252d_base_v108_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v109_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v110_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v111_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v112_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v113_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v114_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v115_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v116_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v117_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v118_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v119_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v120_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v121_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v122_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v123_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v124_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v125_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v126_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v127_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v128_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v129_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v130_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v131_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v132_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v133_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v134_signal,
    f17has_f17_healthit_arr_signature_arrproxy_5d_base_v135_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v136_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v137_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v138_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v139_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v140_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v141_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v142_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v143_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v144_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v145_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v146_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v147_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v148_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v149_signal,
    f17has_f17_healthit_arr_signature_arrproxy_42d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_HEALTHIT_ARR_SIGNATURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "sgna": sgna,
        "opex": opex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f17_arr_proxy', '_f17_revenue_recurring_share', '_f17_arr_quality')
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_healthit_arr_signature_base_076_150_claude: {n_features} features pass")
