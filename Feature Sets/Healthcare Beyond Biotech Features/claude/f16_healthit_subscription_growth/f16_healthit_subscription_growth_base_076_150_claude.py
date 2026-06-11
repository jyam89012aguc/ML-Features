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
def _f16_deferred_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f16_subscription_proxy(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan).abs()


def _f16_subscription_acceleration(deferredrev, w):
    g = deferredrev.pct_change(periods=w)
    return g.diff(periods=w)


# ===== features =====
def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v076_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v077_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v078_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 126).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v079_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 126).rolling(21, min_periods=max(1, 21 // 2)).max() - _f16_deferred_growth(deferredrev, 126).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v080_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 126).rolling(63, min_periods=max(1, 63 // 2)).max() - _f16_deferred_growth(deferredrev, 126).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v081_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 126).rolling(252, min_periods=max(1, 252 // 2)).max() - _f16_deferred_growth(deferredrev, 126).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v082_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v083_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v084_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v085_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v086_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v087_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v088_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v089_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v090_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v091_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v092_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v093_signal(deferredrev, closeadj):
    result = (-_f16_deferred_growth(deferredrev, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v094_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252) * _f16_deferred_growth(deferredrev, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v095_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v096_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v097_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v098_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v099_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v100_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v101_signal(deferredrev, closeadj):
    result = np.log(_f16_deferred_growth(deferredrev, 252).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v102_signal(deferredrev, closeadj):
    result = np.sign(_f16_deferred_growth(deferredrev, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v103_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v104_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v105_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 252).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v106_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 252).rolling(21, min_periods=max(1, 21 // 2)).max() - _f16_deferred_growth(deferredrev, 252).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v107_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 252).rolling(63, min_periods=max(1, 63 // 2)).max() - _f16_deferred_growth(deferredrev, 252).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v108_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 252).rolling(252, min_periods=max(1, 252 // 2)).max() - _f16_deferred_growth(deferredrev, 252).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v109_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v110_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v111_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v112_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v113_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v114_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v115_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v116_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v117_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v118_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v119_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v120_signal(deferredrev, closeadj):
    result = (-_f16_deferred_growth(deferredrev, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v121_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5) * _f16_deferred_growth(deferredrev, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v122_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v123_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v124_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v125_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v126_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v127_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v128_signal(deferredrev, closeadj):
    result = np.log(_f16_deferred_growth(deferredrev, 5).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v129_signal(deferredrev, closeadj):
    result = np.sign(_f16_deferred_growth(deferredrev, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v130_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v131_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v132_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 5).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v133_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 5).rolling(21, min_periods=max(1, 21 // 2)).max() - _f16_deferred_growth(deferredrev, 5).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v134_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 5).rolling(63, min_periods=max(1, 63 // 2)).max() - _f16_deferred_growth(deferredrev, 5).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v135_signal(deferredrev, closeadj):
    result = (_f16_deferred_growth(deferredrev, 5).rolling(252, min_periods=max(1, 252 // 2)).max() - _f16_deferred_growth(deferredrev, 5).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v136_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v137_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v138_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v139_signal(deferredrev, closeadj):
    result = _mean(_f16_deferred_growth(deferredrev, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v140_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v141_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v142_signal(deferredrev, closeadj):
    result = _std(_f16_deferred_growth(deferredrev, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v143_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v144_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v145_signal(deferredrev, closeadj):
    result = _z(_f16_deferred_growth(deferredrev, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v146_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v147_signal(deferredrev, closeadj):
    result = (-_f16_deferred_growth(deferredrev, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v148_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 42) * _f16_deferred_growth(deferredrev, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v149_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 42).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v150_signal(deferredrev, closeadj):
    result = _f16_deferred_growth(deferredrev, 42).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v076_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v077_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v078_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v079_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v080_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_126d_base_v081_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v082_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v083_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v084_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v085_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v086_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v087_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v088_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v089_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v090_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v091_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v092_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v093_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v094_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v095_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v096_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v097_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v098_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v099_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v100_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v101_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v102_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v103_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v104_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v105_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v106_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v107_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_252d_base_v108_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v109_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v110_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v111_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v112_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v113_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v114_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v115_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v116_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v117_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v118_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v119_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v120_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v121_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v122_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v123_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v124_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v125_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v126_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v127_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v128_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v129_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v130_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v131_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v132_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v133_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v134_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_5d_base_v135_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v136_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v137_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v138_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v139_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v140_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v141_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v142_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v143_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v144_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v145_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v146_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v147_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v148_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v149_signal,
    f16hsg_f16_healthit_subscription_growth_deferredgrowth_42d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_HEALTHIT_SUBSCRIPTION_GROWTH_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f16_deferred_growth', '_f16_subscription_proxy', '_f16_subscription_acceleration')
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
    print(f"OK f16_healthit_subscription_growth_base_076_150_claude: {n_features} features pass")
