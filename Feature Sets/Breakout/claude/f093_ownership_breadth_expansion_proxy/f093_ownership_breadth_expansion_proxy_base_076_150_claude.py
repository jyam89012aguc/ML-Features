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
def _f093_volume_breadth(volume, w):
    return _mean(volume, w) / _mean(volume, w * 2).replace(0, np.nan)


def _f093_share_count_stable(sharesbas, w):
    return 1.0 - _std(sharesbas.pct_change(), w).fillna(0)


def _f093_breadth_proxy(volume, sharesbas, w):
    turnover = volume / sharesbas.replace(0, np.nan)
    return _mean(turnover, w)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_5d_base_v076_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_5d_base_v077_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_5d_base_v078_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_10d_base_v079_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_10d_base_v080_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_10d_base_v081_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_21d_base_v082_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_21d_base_v083_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_21d_base_v084_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_42d_base_v085_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_42d_base_v086_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_42d_base_v087_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_63d_base_v088_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_63d_base_v089_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_63d_base_v090_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_126d_base_v091_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_126d_base_v092_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_126d_base_v093_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_189d_base_v094_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_189d_base_v095_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_189d_base_v096_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_252d_base_v097_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_252d_base_v098_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_252d_base_v099_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_378d_base_v100_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_378d_base_v101_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_378d_base_v102_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_504d_base_v103_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_504d_base_v104_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_504d_base_v105_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_5d_base_v106_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_5d_base_v107_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_5d_base_v108_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_10d_base_v109_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_10d_base_v110_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_10d_base_v111_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_21d_base_v112_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_21d_base_v113_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_21d_base_v114_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_42d_base_v115_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_42d_base_v116_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_42d_base_v117_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_63d_base_v118_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_63d_base_v119_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_63d_base_v120_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_126d_base_v121_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_126d_base_v122_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_126d_base_v123_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_189d_base_v124_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_189d_base_v125_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_189d_base_v126_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_252d_base_v127_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_252d_base_v128_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_252d_base_v129_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_378d_base_v130_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_378d_base_v131_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_378d_base_v132_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_504d_base_v133_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_504d_base_v134_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_504d_base_v135_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_5d_base_v136_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_5d_base_v137_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_5d_base_v138_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_10d_base_v139_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_10d_base_v140_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_10d_base_v141_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_21d_base_v142_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_21d_base_v143_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_21d_base_v144_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_42d_base_v145_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_42d_base_v146_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_42d_base_v147_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_63d_base_v148_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_63d_base_v149_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_63d_base_v150_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_5d_base_v076_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_5d_base_v077_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_5d_base_v078_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_10d_base_v079_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_10d_base_v080_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_10d_base_v081_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_21d_base_v082_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_21d_base_v083_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_21d_base_v084_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_42d_base_v085_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_42d_base_v086_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_42d_base_v087_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_63d_base_v088_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_63d_base_v089_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_63d_base_v090_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_126d_base_v091_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_126d_base_v092_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_126d_base_v093_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_189d_base_v094_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_189d_base_v095_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_189d_base_v096_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_252d_base_v097_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_252d_base_v098_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_252d_base_v099_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_378d_base_v100_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_378d_base_v101_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_378d_base_v102_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrtnh_504d_base_v103_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcsttnh_504d_base_v104_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxytnh_504d_base_v105_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_5d_base_v106_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_5d_base_v107_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_5d_base_v108_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_10d_base_v109_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_10d_base_v110_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_10d_base_v111_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_21d_base_v112_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_21d_base_v113_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_21d_base_v114_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_42d_base_v115_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_42d_base_v116_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_42d_base_v117_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_63d_base_v118_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_63d_base_v119_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_63d_base_v120_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_126d_base_v121_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_126d_base_v122_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_126d_base_v123_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_189d_base_v124_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_189d_base_v125_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_189d_base_v126_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_252d_base_v127_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_252d_base_v128_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_252d_base_v129_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_378d_base_v130_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_378d_base_v131_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_378d_base_v132_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrzcl_504d_base_v133_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstzcl_504d_base_v134_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyzcl_504d_base_v135_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_5d_base_v136_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_5d_base_v137_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_5d_base_v138_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_10d_base_v139_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_10d_base_v140_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_10d_base_v141_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_21d_base_v142_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_21d_base_v143_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_21d_base_v144_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_42d_base_v145_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_42d_base_v146_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_42d_base_v147_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrrvr_63d_base_v148_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstrvr_63d_base_v149_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyrvr_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F093_OWNERSHIP_BREADTH_EXPANSION_PROXY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {
        "closeadj": closeadj, "volume": volume, "sharesbas": sharesbas,
        "marketcap": marketcap, "dps": dps, "payoutratio": payoutratio,
        "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f093_volume_breadth", "_f093_share_count_stable", "_f093_breadth_proxy")
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
    print(f"OK f093_ownership_breadth_expansion_proxy_base_076_150_claude: {n_features} features pass")
