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
def _f004_donchian_break(close, w):
    hi = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    return (close - hi) / hi.replace(0, np.nan).abs()


def _f004_breakout_strength(close, w):
    hi = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    excess = (close - hi).clip(lower=0.0)
    return excess / hi.replace(0, np.nan).abs()


def _f004_break_score(close, w):
    hi = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (close - hi) / (hi - lo).replace(0, np.nan).abs()


def f004nwh_f004_n_week_high_breakout_flag_dbkth_5d_base_v076_signal(closeadj):
    base = _f004_donchian_break(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_5d_base_v077_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_5d_base_v078_signal(closeadj):
    base = _f004_break_score(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_10d_base_v079_signal(closeadj):
    base = _f004_donchian_break(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_10d_base_v080_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_10d_base_v081_signal(closeadj):
    base = _f004_break_score(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_21d_base_v082_signal(closeadj):
    base = _f004_donchian_break(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_21d_base_v083_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_21d_base_v084_signal(closeadj):
    base = _f004_break_score(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_42d_base_v085_signal(closeadj):
    base = _f004_donchian_break(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_42d_base_v086_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_42d_base_v087_signal(closeadj):
    base = _f004_break_score(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_63d_base_v088_signal(closeadj):
    base = _f004_donchian_break(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_63d_base_v089_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_63d_base_v090_signal(closeadj):
    base = _f004_break_score(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_126d_base_v091_signal(closeadj):
    base = _f004_donchian_break(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_126d_base_v092_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_126d_base_v093_signal(closeadj):
    base = _f004_break_score(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_189d_base_v094_signal(closeadj):
    base = _f004_donchian_break(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_189d_base_v095_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_189d_base_v096_signal(closeadj):
    base = _f004_break_score(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_252d_base_v097_signal(closeadj):
    base = _f004_donchian_break(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_252d_base_v098_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_252d_base_v099_signal(closeadj):
    base = _f004_break_score(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_378d_base_v100_signal(closeadj):
    base = _f004_donchian_break(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_378d_base_v101_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_378d_base_v102_signal(closeadj):
    base = _f004_break_score(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkth_504d_base_v103_signal(closeadj):
    base = _f004_donchian_break(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstth_504d_base_v104_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscth_504d_base_v105_signal(closeadj):
    base = _f004_break_score(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_5d_base_v106_signal(closeadj):
    base = _f004_donchian_break(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_5d_base_v107_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_5d_base_v108_signal(closeadj):
    base = _f004_break_score(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_10d_base_v109_signal(closeadj):
    base = _f004_donchian_break(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_10d_base_v110_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_10d_base_v111_signal(closeadj):
    base = _f004_break_score(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_21d_base_v112_signal(closeadj):
    base = _f004_donchian_break(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_21d_base_v113_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_21d_base_v114_signal(closeadj):
    base = _f004_break_score(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_42d_base_v115_signal(closeadj):
    base = _f004_donchian_break(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_42d_base_v116_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_42d_base_v117_signal(closeadj):
    base = _f004_break_score(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_63d_base_v118_signal(closeadj):
    base = _f004_donchian_break(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_63d_base_v119_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_63d_base_v120_signal(closeadj):
    base = _f004_break_score(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_126d_base_v121_signal(closeadj):
    base = _f004_donchian_break(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_126d_base_v122_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_126d_base_v123_signal(closeadj):
    base = _f004_break_score(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_189d_base_v124_signal(closeadj):
    base = _f004_donchian_break(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_189d_base_v125_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_189d_base_v126_signal(closeadj):
    base = _f004_break_score(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_252d_base_v127_signal(closeadj):
    base = _f004_donchian_break(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_252d_base_v128_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_252d_base_v129_signal(closeadj):
    base = _f004_break_score(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_378d_base_v130_signal(closeadj):
    base = _f004_donchian_break(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_378d_base_v131_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_378d_base_v132_signal(closeadj):
    base = _f004_break_score(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkcl_504d_base_v133_signal(closeadj):
    base = _f004_donchian_break(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstcl_504d_base_v134_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bsccl_504d_base_v135_signal(closeadj):
    base = _f004_break_score(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkvr_5d_base_v136_signal(closeadj):
    base = _f004_donchian_break(closeadj, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstvr_5d_base_v137_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscvr_5d_base_v138_signal(closeadj):
    base = _f004_break_score(closeadj, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkvr_10d_base_v139_signal(closeadj):
    base = _f004_donchian_break(closeadj, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstvr_10d_base_v140_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscvr_10d_base_v141_signal(closeadj):
    base = _f004_break_score(closeadj, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkvr_21d_base_v142_signal(closeadj):
    base = _f004_donchian_break(closeadj, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstvr_21d_base_v143_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscvr_21d_base_v144_signal(closeadj):
    base = _f004_break_score(closeadj, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkvr_42d_base_v145_signal(closeadj):
    base = _f004_donchian_break(closeadj, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstvr_42d_base_v146_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscvr_42d_base_v147_signal(closeadj):
    base = _f004_break_score(closeadj, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_dbkvr_63d_base_v148_signal(closeadj):
    base = _f004_donchian_break(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bstvr_63d_base_v149_signal(closeadj):
    base = _f004_breakout_strength(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f004nwh_f004_n_week_high_breakout_flag_bscvr_63d_base_v150_signal(closeadj):
    base = _f004_break_score(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f004nwh_f004_n_week_high_breakout_flag_dbkth_5d_base_v076_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_5d_base_v077_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_5d_base_v078_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_10d_base_v079_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_10d_base_v080_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_10d_base_v081_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_21d_base_v082_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_21d_base_v083_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_21d_base_v084_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_42d_base_v085_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_42d_base_v086_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_42d_base_v087_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_63d_base_v088_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_63d_base_v089_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_63d_base_v090_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_126d_base_v091_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_126d_base_v092_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_126d_base_v093_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_189d_base_v094_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_189d_base_v095_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_189d_base_v096_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_252d_base_v097_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_252d_base_v098_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_252d_base_v099_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_378d_base_v100_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_378d_base_v101_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_378d_base_v102_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkth_504d_base_v103_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstth_504d_base_v104_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscth_504d_base_v105_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_5d_base_v106_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_5d_base_v107_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_5d_base_v108_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_10d_base_v109_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_10d_base_v110_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_10d_base_v111_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_21d_base_v112_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_21d_base_v113_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_21d_base_v114_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_42d_base_v115_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_42d_base_v116_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_42d_base_v117_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_63d_base_v118_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_63d_base_v119_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_63d_base_v120_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_126d_base_v121_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_126d_base_v122_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_126d_base_v123_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_189d_base_v124_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_189d_base_v125_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_189d_base_v126_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_252d_base_v127_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_252d_base_v128_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_252d_base_v129_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_378d_base_v130_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_378d_base_v131_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_378d_base_v132_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkcl_504d_base_v133_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstcl_504d_base_v134_signal,
    f004nwh_f004_n_week_high_breakout_flag_bsccl_504d_base_v135_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkvr_5d_base_v136_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstvr_5d_base_v137_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscvr_5d_base_v138_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkvr_10d_base_v139_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstvr_10d_base_v140_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscvr_10d_base_v141_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkvr_21d_base_v142_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstvr_21d_base_v143_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscvr_21d_base_v144_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkvr_42d_base_v145_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstvr_42d_base_v146_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscvr_42d_base_v147_signal,
    f004nwh_f004_n_week_high_breakout_flag_dbkvr_63d_base_v148_signal,
    f004nwh_f004_n_week_high_breakout_flag_bstvr_63d_base_v149_signal,
    f004nwh_f004_n_week_high_breakout_flag_bscvr_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F004_N_WEEK_HIGH_BREAKOUT_FLAG_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f004_donchian_break", "_f004_breakout_strength", "_f004_break_score")
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
    print(f"OK f004_n_week_high_breakout_flag_base_076_150_claude: {n_features} features pass")
