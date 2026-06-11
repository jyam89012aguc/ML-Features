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
def _f095_quality_signal(roic, w):
    return _mean(roic, w)


def _f095_low_share_growth(sharesbas, w):
    return -sharesbas.pct_change(w).fillna(0)


def _f095_skilled_proxy(roic, sharesbas, w):
    q = _mean(roic, w)
    low_g = -sharesbas.pct_change(w).fillna(0)
    return q + low_g


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_5d_base_v076_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_5d_base_v077_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_5d_base_v078_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_10d_base_v079_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_10d_base_v080_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_10d_base_v081_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_21d_base_v082_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_21d_base_v083_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_21d_base_v084_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_42d_base_v085_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_42d_base_v086_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_42d_base_v087_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_63d_base_v088_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_63d_base_v089_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_63d_base_v090_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_126d_base_v091_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_126d_base_v092_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_126d_base_v093_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_189d_base_v094_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_189d_base_v095_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_189d_base_v096_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_252d_base_v097_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_252d_base_v098_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_252d_base_v099_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_378d_base_v100_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_378d_base_v101_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_378d_base_v102_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualstnh_504d_base_v103_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrtnh_504d_base_v104_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxytnh_504d_base_v105_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_5d_base_v106_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_5d_base_v107_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_5d_base_v108_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_10d_base_v109_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_10d_base_v110_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_10d_base_v111_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_21d_base_v112_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_21d_base_v113_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_21d_base_v114_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_42d_base_v115_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_42d_base_v116_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_42d_base_v117_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_63d_base_v118_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_63d_base_v119_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_63d_base_v120_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_126d_base_v121_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_126d_base_v122_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_126d_base_v123_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_189d_base_v124_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_189d_base_v125_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_189d_base_v126_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_252d_base_v127_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_252d_base_v128_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_252d_base_v129_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_378d_base_v130_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_378d_base_v131_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_378d_base_v132_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualszcl_504d_base_v133_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrzcl_504d_base_v134_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_504d_base_v135_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsrvr_5d_base_v136_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrrvr_5d_base_v137_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_5d_base_v138_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsrvr_10d_base_v139_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrrvr_10d_base_v140_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_10d_base_v141_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsrvr_21d_base_v142_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrrvr_21d_base_v143_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_21d_base_v144_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsrvr_42d_base_v145_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrrvr_42d_base_v146_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_42d_base_v147_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsrvr_63d_base_v148_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrrvr_63d_base_v149_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_63d_base_v150_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_5d_base_v076_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_5d_base_v077_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_5d_base_v078_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_10d_base_v079_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_10d_base_v080_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_10d_base_v081_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_21d_base_v082_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_21d_base_v083_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_21d_base_v084_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_42d_base_v085_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_42d_base_v086_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_42d_base_v087_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_63d_base_v088_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_63d_base_v089_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_63d_base_v090_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_126d_base_v091_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_126d_base_v092_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_126d_base_v093_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_189d_base_v094_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_189d_base_v095_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_189d_base_v096_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_252d_base_v097_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_252d_base_v098_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_252d_base_v099_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_378d_base_v100_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_378d_base_v101_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_378d_base_v102_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualstnh_504d_base_v103_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrtnh_504d_base_v104_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxytnh_504d_base_v105_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_5d_base_v106_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_5d_base_v107_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_5d_base_v108_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_10d_base_v109_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_10d_base_v110_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_10d_base_v111_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_21d_base_v112_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_21d_base_v113_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_21d_base_v114_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_42d_base_v115_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_42d_base_v116_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_42d_base_v117_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_63d_base_v118_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_63d_base_v119_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_63d_base_v120_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_126d_base_v121_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_126d_base_v122_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_126d_base_v123_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_189d_base_v124_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_189d_base_v125_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_189d_base_v126_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_252d_base_v127_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_252d_base_v128_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_252d_base_v129_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_378d_base_v130_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_378d_base_v131_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_378d_base_v132_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualszcl_504d_base_v133_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrzcl_504d_base_v134_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyzcl_504d_base_v135_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsrvr_5d_base_v136_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrrvr_5d_base_v137_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_5d_base_v138_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsrvr_10d_base_v139_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrrvr_10d_base_v140_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_10d_base_v141_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsrvr_21d_base_v142_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrrvr_21d_base_v143_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_21d_base_v144_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsrvr_42d_base_v145_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrrvr_42d_base_v146_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_42d_base_v147_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsrvr_63d_base_v148_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrrvr_63d_base_v149_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyrvr_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F095_SKILLED_MANAGER_ADDS_PROXY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f095_quality_signal", "_f095_low_share_growth", "_f095_skilled_proxy")
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
    print(f"OK f095_skilled_manager_adds_proxy_base_076_150_claude: {n_features} features pass")
