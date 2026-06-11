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
def _f20_revenue_per_cost(revenue, opex):
    return revenue / opex.replace(0, np.nan).abs()


def _f20_platform_efficiency(revenue, opex, w):
    ratio = revenue / opex.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


def _f20_platform_scaling_score(revenue, sgna, opex, w):
    rev_growth = revenue.pct_change(periods=w)
    cost_growth = (sgna + opex).pct_change(periods=w)
    return rev_growth - cost_growth


# ===== features =====
def f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v076_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 63).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v077_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 63).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v078_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 63).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v079_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 63).rolling(21, min_periods=max(1, 21 // 2)).max() - _f20_platform_efficiency(revenue, opex, 63).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v080_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 63).rolling(63, min_periods=max(1, 63 // 2)).max() - _f20_platform_efficiency(revenue, opex, 63).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v081_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 63).rolling(252, min_periods=max(1, 252 // 2)).max() - _f20_platform_efficiency(revenue, opex, 63).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v082_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v083_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v084_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v085_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v086_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v087_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v088_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v089_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v090_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v091_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v092_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v093_signal(revenue, opex, closeadj):
    result = (-_f20_platform_efficiency(revenue, opex, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v094_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126) * _f20_platform_efficiency(revenue, opex, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v095_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v096_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v097_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v098_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v099_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v100_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v101_signal(revenue, opex, closeadj):
    result = np.log(_f20_platform_efficiency(revenue, opex, 126).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v102_signal(revenue, opex, closeadj):
    result = np.sign(_f20_platform_efficiency(revenue, opex, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v103_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v104_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v105_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 126).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v106_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 126).rolling(21, min_periods=max(1, 21 // 2)).max() - _f20_platform_efficiency(revenue, opex, 126).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v107_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 126).rolling(63, min_periods=max(1, 63 // 2)).max() - _f20_platform_efficiency(revenue, opex, 126).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v108_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 126).rolling(252, min_periods=max(1, 252 // 2)).max() - _f20_platform_efficiency(revenue, opex, 126).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v109_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v110_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v111_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v112_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v113_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v114_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v115_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v116_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v117_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v118_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v119_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v120_signal(revenue, opex, closeadj):
    result = (-_f20_platform_efficiency(revenue, opex, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v121_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252) * _f20_platform_efficiency(revenue, opex, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v122_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v123_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v124_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v125_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v126_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v127_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v128_signal(revenue, opex, closeadj):
    result = np.log(_f20_platform_efficiency(revenue, opex, 252).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v129_signal(revenue, opex, closeadj):
    result = np.sign(_f20_platform_efficiency(revenue, opex, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v130_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v131_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v132_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 252).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v133_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 252).rolling(21, min_periods=max(1, 21 // 2)).max() - _f20_platform_efficiency(revenue, opex, 252).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v134_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 252).rolling(63, min_periods=max(1, 63 // 2)).max() - _f20_platform_efficiency(revenue, opex, 252).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v135_signal(revenue, opex, closeadj):
    result = (_f20_platform_efficiency(revenue, opex, 252).rolling(252, min_periods=max(1, 252 // 2)).max() - _f20_platform_efficiency(revenue, opex, 252).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v136_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v137_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v138_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v139_signal(revenue, opex, closeadj):
    result = _mean(_f20_platform_efficiency(revenue, opex, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v140_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v141_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v142_signal(revenue, opex, closeadj):
    result = _std(_f20_platform_efficiency(revenue, opex, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v143_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v144_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v145_signal(revenue, opex, closeadj):
    result = _z(_f20_platform_efficiency(revenue, opex, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v146_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v147_signal(revenue, opex, closeadj):
    result = (-_f20_platform_efficiency(revenue, opex, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v148_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 5) * _f20_platform_efficiency(revenue, opex, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v149_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 5).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v150_signal(revenue, opex, closeadj):
    result = _f20_platform_efficiency(revenue, opex, 5).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v076_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v077_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v078_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v079_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v080_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_63d_base_v081_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v082_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v083_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v084_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v085_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v086_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v087_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v088_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v089_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v090_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v091_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v092_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v093_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v094_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v095_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v096_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v097_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v098_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v099_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v100_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v101_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v102_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v103_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v104_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v105_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v106_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v107_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_126d_base_v108_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v109_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v110_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v111_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v112_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v113_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v114_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v115_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v116_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v117_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v118_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v119_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v120_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v121_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v122_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v123_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v124_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v125_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v126_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v127_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v128_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v129_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v130_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v131_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v132_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v133_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v134_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_252d_base_v135_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v136_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v137_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v138_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v139_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v140_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v141_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v142_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v143_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v144_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v145_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v146_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v147_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v148_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v149_signal,
    f20hps_f20_healthit_platform_scaling_platformefficiency_5d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_HEALTHIT_PLATFORM_SCALING_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f20_revenue_per_cost', '_f20_platform_efficiency', '_f20_platform_scaling_score')
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
    print(f"OK f20_healthit_platform_scaling_base_076_150_claude: {n_features} features pass")
