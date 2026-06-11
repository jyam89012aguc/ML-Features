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
def _f091_payout_signal(payoutratio, dps, w):
    s = payoutratio * dps
    return _mean(s, w)


def _f091_insider_payout_combo(sharesbas, payoutratio, w):
    sd = -sharesbas.pct_change(w).fillna(0)
    return _mean(sd + payoutratio, w)


def _f091_weighted_signal(sharesbas, dps, w):
    sd = -sharesbas.pct_change(w).fillna(0)
    return _mean(sd * dps, w)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_5d_base_v076_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_5d_base_v077_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_5d_base_v078_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_10d_base_v079_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_10d_base_v080_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_10d_base_v081_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_21d_base_v082_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_21d_base_v083_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_21d_base_v084_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_42d_base_v085_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_42d_base_v086_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_42d_base_v087_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_63d_base_v088_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_63d_base_v089_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_63d_base_v090_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_126d_base_v091_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_126d_base_v092_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_126d_base_v093_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_189d_base_v094_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_189d_base_v095_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_189d_base_v096_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_252d_base_v097_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_252d_base_v098_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_252d_base_v099_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_378d_base_v100_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_378d_base_v101_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_378d_base_v102_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_504d_base_v103_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_504d_base_v104_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_504d_base_v105_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_5d_base_v106_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_5d_base_v107_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_5d_base_v108_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_10d_base_v109_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_10d_base_v110_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_10d_base_v111_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_21d_base_v112_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_21d_base_v113_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_21d_base_v114_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_42d_base_v115_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_42d_base_v116_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_42d_base_v117_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_63d_base_v118_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_63d_base_v119_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_63d_base_v120_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_126d_base_v121_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_126d_base_v122_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_126d_base_v123_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_189d_base_v124_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_189d_base_v125_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_189d_base_v126_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_252d_base_v127_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_252d_base_v128_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_252d_base_v129_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_378d_base_v130_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_378d_base_v131_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_378d_base_v132_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_504d_base_v133_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_504d_base_v134_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_504d_base_v135_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_5d_base_v136_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_5d_base_v137_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_5d_base_v138_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_10d_base_v139_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_10d_base_v140_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_10d_base_v141_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_21d_base_v142_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_21d_base_v143_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_21d_base_v144_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_42d_base_v145_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_42d_base_v146_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_42d_base_v147_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_63d_base_v148_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_63d_base_v149_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_63d_base_v150_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_5d_base_v076_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_5d_base_v077_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_5d_base_v078_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_10d_base_v079_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_10d_base_v080_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_10d_base_v081_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_21d_base_v082_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_21d_base_v083_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_21d_base_v084_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_42d_base_v085_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_42d_base_v086_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_42d_base_v087_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_63d_base_v088_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_63d_base_v089_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_63d_base_v090_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_126d_base_v091_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_126d_base_v092_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_126d_base_v093_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_189d_base_v094_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_189d_base_v095_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_189d_base_v096_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_252d_base_v097_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_252d_base_v098_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_252d_base_v099_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_378d_base_v100_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_378d_base_v101_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_378d_base_v102_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_tanh_504d_base_v103_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_tanh_504d_base_v104_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_tanh_504d_base_v105_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_5d_base_v106_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_5d_base_v107_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_5d_base_v108_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_10d_base_v109_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_10d_base_v110_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_10d_base_v111_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_21d_base_v112_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_21d_base_v113_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_21d_base_v114_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_42d_base_v115_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_42d_base_v116_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_42d_base_v117_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_63d_base_v118_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_63d_base_v119_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_63d_base_v120_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_126d_base_v121_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_126d_base_v122_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_126d_base_v123_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_189d_base_v124_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_189d_base_v125_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_189d_base_v126_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_252d_base_v127_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_252d_base_v128_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_252d_base_v129_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_378d_base_v130_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_378d_base_v131_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_378d_base_v132_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_zclip_504d_base_v133_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_zclip_504d_base_v134_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_zclip_504d_base_v135_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_5d_base_v136_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_5d_base_v137_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_5d_base_v138_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_10d_base_v139_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_10d_base_v140_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_10d_base_v141_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_21d_base_v142_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_21d_base_v143_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_21d_base_v144_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_42d_base_v145_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_42d_base_v146_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_42d_base_v147_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_var63_63d_base_v148_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_var63_63d_base_v149_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_var63_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F091_ROLE_WEIGHTED_INSIDER_SIGNAL_PROXY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f091_payout_signal", "_f091_insider_payout_combo", "_f091_weighted_signal")
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
    print(f"OK f091_role_weighted_insider_signal_proxy_base_076_150_claude: {n_features} features pass")
