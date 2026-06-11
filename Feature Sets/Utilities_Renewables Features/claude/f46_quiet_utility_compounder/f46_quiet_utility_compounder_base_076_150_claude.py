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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====
def _f46_low_vol_signal(closeadj, w):
    r = closeadj.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std()
    return -vol * closeadj


def _f46_steady_growth(netinc, w):
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = netinc.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f46_compounder_composite(closeadj, netinc, w):
    r = closeadj.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    return (m / vol) * np.sign(closeadj)


# ===== features =====
def f46quc_f46_quiet_utility_compounder_lv_close_10d_s01_base_v076_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 10)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_10d_s01_base_v077_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_10d_s01_base_v078_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 10)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_10d_s01_base_v079_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v080_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v081_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v082_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v083_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v084_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v085_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v086_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v087_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v088_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v089_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v090_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v091_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v092_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v093_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v094_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v095_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v096_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v097_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v098_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v099_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v100_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v101_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v102_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v103_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v104_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v105_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v106_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v107_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v108_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v109_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v110_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v111_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v112_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v113_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v114_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v115_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v116_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v117_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v118_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v119_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v120_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v121_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v122_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v123_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v124_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v125_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v126_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v127_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v128_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v129_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v130_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v131_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v132_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v133_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v134_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v135_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v136_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v137_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v138_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v139_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v140_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v141_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v142_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v143_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v144_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v145_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v146_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v147_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v148_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v149_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v150_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46quc_f46_quiet_utility_compounder_lv_close_10d_s01_base_v076_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_10d_s01_base_v077_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_10d_s01_base_v078_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_10d_s01_base_v079_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v080_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v081_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v082_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v083_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v084_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v085_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v086_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s01_base_v087_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v088_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v089_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v090_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v091_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v092_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v093_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v094_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s01_base_v095_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v096_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v097_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v098_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v099_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v100_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v101_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v102_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s01_base_v103_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v104_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v105_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v106_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v107_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v108_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v109_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v110_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s01_base_v111_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v112_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v113_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v114_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v115_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v116_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v117_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v118_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s01_base_v119_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v120_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v121_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v122_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v123_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v124_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v125_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v126_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s01_base_v127_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v128_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v129_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v130_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v131_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v132_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v133_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v134_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s01_base_v135_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v136_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v137_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v138_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v139_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v140_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v141_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v142_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s01_base_v143_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v144_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v145_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v146_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v147_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v148_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v149_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s01_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_QUIET_UTILITY_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")
    cols = {"closeadj": closeadj, "ebitda": ebitda, "eps": eps, "netinc": netinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f46_low_vol_signal", "_f46_steady_growth", "_f46_compounder_composite",)
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
    print(f"OK f46_quiet_utility_compounder_base_076_150_claude: {n_features} features pass")
