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
def _f094_small_mc(marketcap, w):
    return 1.0 / (1.0 + _mean(marketcap, w) / 1e9)


def _f094_low_share_growth(sharesbas, w):
    g = sharesbas.pct_change(w)
    return -g.fillna(0)


def _f094_low_float_setup(marketcap, sharesbas, w):
    small = 1.0 / (1.0 + _mean(marketcap, w) / 1e9)
    low_g = -sharesbas.pct_change(w).fillna(0)
    return small + low_g


def f094lfl_f094_low_float_low_inst_setup_smamctnh_5d_base_v076_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_5d_base_v077_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_5d_base_v078_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_10d_base_v079_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_10d_base_v080_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_10d_base_v081_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_21d_base_v082_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_21d_base_v083_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_21d_base_v084_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_42d_base_v085_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_42d_base_v086_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_42d_base_v087_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_63d_base_v088_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_63d_base_v089_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_63d_base_v090_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_126d_base_v091_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_126d_base_v092_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_126d_base_v093_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_189d_base_v094_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_189d_base_v095_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_189d_base_v096_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_252d_base_v097_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_252d_base_v098_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_252d_base_v099_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_378d_base_v100_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_378d_base_v101_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_378d_base_v102_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamctnh_504d_base_v103_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrtnh_504d_base_v104_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflsttnh_504d_base_v105_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_5d_base_v106_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_5d_base_v107_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_5d_base_v108_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_10d_base_v109_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_10d_base_v110_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_10d_base_v111_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_21d_base_v112_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_21d_base_v113_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_21d_base_v114_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_42d_base_v115_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_42d_base_v116_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_42d_base_v117_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_63d_base_v118_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_63d_base_v119_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_63d_base_v120_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_126d_base_v121_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_126d_base_v122_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_126d_base_v123_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_189d_base_v124_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_189d_base_v125_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_189d_base_v126_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_252d_base_v127_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_252d_base_v128_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_252d_base_v129_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_378d_base_v130_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_378d_base_v131_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_378d_base_v132_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamczcl_504d_base_v133_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrzcl_504d_base_v134_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstzcl_504d_base_v135_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcrvr_5d_base_v136_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrrvr_5d_base_v137_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstrvr_5d_base_v138_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcrvr_10d_base_v139_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrrvr_10d_base_v140_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstrvr_10d_base_v141_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcrvr_21d_base_v142_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrrvr_21d_base_v143_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstrvr_21d_base_v144_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcrvr_42d_base_v145_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrrvr_42d_base_v146_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstrvr_42d_base_v147_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_smamcrvr_63d_base_v148_signal(marketcap, sharesbas, closeadj):
    base = _f094_small_mc(marketcap, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_losgrrvr_63d_base_v149_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_share_growth(sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f094lfl_f094_low_float_low_inst_setup_lflstrvr_63d_base_v150_signal(marketcap, sharesbas, closeadj):
    base = _f094_low_float_setup(marketcap, sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f094lfl_f094_low_float_low_inst_setup_smamctnh_5d_base_v076_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_5d_base_v077_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_5d_base_v078_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_10d_base_v079_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_10d_base_v080_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_10d_base_v081_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_21d_base_v082_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_21d_base_v083_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_21d_base_v084_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_42d_base_v085_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_42d_base_v086_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_42d_base_v087_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_63d_base_v088_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_63d_base_v089_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_63d_base_v090_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_126d_base_v091_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_126d_base_v092_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_126d_base_v093_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_189d_base_v094_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_189d_base_v095_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_189d_base_v096_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_252d_base_v097_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_252d_base_v098_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_252d_base_v099_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_378d_base_v100_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_378d_base_v101_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_378d_base_v102_signal,
    f094lfl_f094_low_float_low_inst_setup_smamctnh_504d_base_v103_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrtnh_504d_base_v104_signal,
    f094lfl_f094_low_float_low_inst_setup_lflsttnh_504d_base_v105_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_5d_base_v106_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_5d_base_v107_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_5d_base_v108_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_10d_base_v109_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_10d_base_v110_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_10d_base_v111_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_21d_base_v112_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_21d_base_v113_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_21d_base_v114_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_42d_base_v115_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_42d_base_v116_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_42d_base_v117_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_63d_base_v118_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_63d_base_v119_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_63d_base_v120_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_126d_base_v121_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_126d_base_v122_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_126d_base_v123_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_189d_base_v124_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_189d_base_v125_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_189d_base_v126_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_252d_base_v127_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_252d_base_v128_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_252d_base_v129_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_378d_base_v130_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_378d_base_v131_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_378d_base_v132_signal,
    f094lfl_f094_low_float_low_inst_setup_smamczcl_504d_base_v133_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrzcl_504d_base_v134_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstzcl_504d_base_v135_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcrvr_5d_base_v136_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrrvr_5d_base_v137_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstrvr_5d_base_v138_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcrvr_10d_base_v139_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrrvr_10d_base_v140_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstrvr_10d_base_v141_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcrvr_21d_base_v142_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrrvr_21d_base_v143_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstrvr_21d_base_v144_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcrvr_42d_base_v145_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrrvr_42d_base_v146_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstrvr_42d_base_v147_signal,
    f094lfl_f094_low_float_low_inst_setup_smamcrvr_63d_base_v148_signal,
    f094lfl_f094_low_float_low_inst_setup_losgrrvr_63d_base_v149_signal,
    f094lfl_f094_low_float_low_inst_setup_lflstrvr_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F094_LOW_FLOAT_LOW_INST_SETUP_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f094_small_mc", "_f094_low_share_growth", "_f094_low_float_setup")
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
    print(f"OK f094_low_float_low_inst_setup_base_076_150_claude: {n_features} features pass")
