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
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _f029_vol_regime(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    long_vol = ret.rolling(max(w * 2, 21), min_periods=max(1, w // 2)).std()
    return vol / long_vol.replace(0, np.nan)


def _f029_regime_transition(closeadj, w):
    ret = closeadj.pct_change()
    vol_now = ret.rolling(w, min_periods=max(1, w // 2)).std()
    vol_prev = vol_now.shift(w)
    return (vol_now - vol_prev) / vol_prev.replace(0, np.nan).abs()


def _f029_transition_strength(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    m = vol.rolling(max(w * 2, 21), min_periods=max(1, w // 2)).mean()
    sd = vol.rolling(max(w * 2, 21), min_periods=max(1, w // 2)).std()
    return (vol - m) / sd.replace(0, np.nan)


def f029vrt_f029_vol_regime_transition_flag_volregimetanh_5d_base_v076_signal(closeadj):
    base = _f029_vol_regime(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_5d_base_v077_signal(closeadj):
    base = _f029_regime_transition(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_5d_base_v078_signal(closeadj):
    base = _f029_transition_strength(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_10d_base_v079_signal(closeadj):
    base = _f029_vol_regime(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_10d_base_v080_signal(closeadj):
    base = _f029_regime_transition(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_10d_base_v081_signal(closeadj):
    base = _f029_transition_strength(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_21d_base_v082_signal(closeadj):
    base = _f029_vol_regime(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_21d_base_v083_signal(closeadj):
    base = _f029_regime_transition(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_21d_base_v084_signal(closeadj):
    base = _f029_transition_strength(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_42d_base_v085_signal(closeadj):
    base = _f029_vol_regime(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_42d_base_v086_signal(closeadj):
    base = _f029_regime_transition(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_42d_base_v087_signal(closeadj):
    base = _f029_transition_strength(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_63d_base_v088_signal(closeadj):
    base = _f029_vol_regime(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_63d_base_v089_signal(closeadj):
    base = _f029_regime_transition(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_63d_base_v090_signal(closeadj):
    base = _f029_transition_strength(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_126d_base_v091_signal(closeadj):
    base = _f029_vol_regime(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_126d_base_v092_signal(closeadj):
    base = _f029_regime_transition(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_126d_base_v093_signal(closeadj):
    base = _f029_transition_strength(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_189d_base_v094_signal(closeadj):
    base = _f029_vol_regime(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_189d_base_v095_signal(closeadj):
    base = _f029_regime_transition(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_189d_base_v096_signal(closeadj):
    base = _f029_transition_strength(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_252d_base_v097_signal(closeadj):
    base = _f029_vol_regime(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_252d_base_v098_signal(closeadj):
    base = _f029_regime_transition(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_252d_base_v099_signal(closeadj):
    base = _f029_transition_strength(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_378d_base_v100_signal(closeadj):
    base = _f029_vol_regime(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_378d_base_v101_signal(closeadj):
    base = _f029_regime_transition(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_378d_base_v102_signal(closeadj):
    base = _f029_transition_strength(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimetanh_504d_base_v103_signal(closeadj):
    base = _f029_vol_regime(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranstanh_504d_base_v104_signal(closeadj):
    base = _f029_regime_transition(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrtanh_504d_base_v105_signal(closeadj):
    base = _f029_transition_strength(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_5d_base_v106_signal(closeadj):
    base = _f029_vol_regime(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_5d_base_v107_signal(closeadj):
    base = _f029_regime_transition(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_5d_base_v108_signal(closeadj):
    base = _f029_transition_strength(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_10d_base_v109_signal(closeadj):
    base = _f029_vol_regime(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_10d_base_v110_signal(closeadj):
    base = _f029_regime_transition(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_10d_base_v111_signal(closeadj):
    base = _f029_transition_strength(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_21d_base_v112_signal(closeadj):
    base = _f029_vol_regime(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_21d_base_v113_signal(closeadj):
    base = _f029_regime_transition(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_21d_base_v114_signal(closeadj):
    base = _f029_transition_strength(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_42d_base_v115_signal(closeadj):
    base = _f029_vol_regime(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_42d_base_v116_signal(closeadj):
    base = _f029_regime_transition(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_42d_base_v117_signal(closeadj):
    base = _f029_transition_strength(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_63d_base_v118_signal(closeadj):
    base = _f029_vol_regime(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_63d_base_v119_signal(closeadj):
    base = _f029_regime_transition(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_63d_base_v120_signal(closeadj):
    base = _f029_transition_strength(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_126d_base_v121_signal(closeadj):
    base = _f029_vol_regime(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_126d_base_v122_signal(closeadj):
    base = _f029_regime_transition(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_126d_base_v123_signal(closeadj):
    base = _f029_transition_strength(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_189d_base_v124_signal(closeadj):
    base = _f029_vol_regime(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_189d_base_v125_signal(closeadj):
    base = _f029_regime_transition(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_189d_base_v126_signal(closeadj):
    base = _f029_transition_strength(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_252d_base_v127_signal(closeadj):
    base = _f029_vol_regime(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_252d_base_v128_signal(closeadj):
    base = _f029_regime_transition(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_252d_base_v129_signal(closeadj):
    base = _f029_transition_strength(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_378d_base_v130_signal(closeadj):
    base = _f029_vol_regime(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_378d_base_v131_signal(closeadj):
    base = _f029_regime_transition(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_378d_base_v132_signal(closeadj):
    base = _f029_transition_strength(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimezclip_504d_base_v133_signal(closeadj):
    base = _f029_vol_regime(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetranszclip_504d_base_v134_signal(closeadj):
    base = _f029_regime_transition(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrzclip_504d_base_v135_signal(closeadj):
    base = _f029_transition_strength(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimevar63_5d_base_v136_signal(closeadj):
    base = _f029_vol_regime(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetransvar63_5d_base_v137_signal(closeadj):
    base = _f029_regime_transition(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrvar63_5d_base_v138_signal(closeadj):
    base = _f029_transition_strength(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimevar63_10d_base_v139_signal(closeadj):
    base = _f029_vol_regime(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetransvar63_10d_base_v140_signal(closeadj):
    base = _f029_regime_transition(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrvar63_10d_base_v141_signal(closeadj):
    base = _f029_transition_strength(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimevar63_21d_base_v142_signal(closeadj):
    base = _f029_vol_regime(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetransvar63_21d_base_v143_signal(closeadj):
    base = _f029_regime_transition(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrvar63_21d_base_v144_signal(closeadj):
    base = _f029_transition_strength(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimevar63_42d_base_v145_signal(closeadj):
    base = _f029_vol_regime(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetransvar63_42d_base_v146_signal(closeadj):
    base = _f029_regime_transition(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrvar63_42d_base_v147_signal(closeadj):
    base = _f029_transition_strength(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_volregimevar63_63d_base_v148_signal(closeadj):
    base = _f029_vol_regime(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_regimetransvar63_63d_base_v149_signal(closeadj):
    base = _f029_regime_transition(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f029vrt_f029_vol_regime_transition_flag_transstrvar63_63d_base_v150_signal(closeadj):
    base = _f029_transition_strength(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_5d_base_v076_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_5d_base_v077_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_5d_base_v078_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_10d_base_v079_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_10d_base_v080_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_10d_base_v081_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_21d_base_v082_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_21d_base_v083_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_21d_base_v084_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_42d_base_v085_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_42d_base_v086_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_42d_base_v087_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_63d_base_v088_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_63d_base_v089_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_63d_base_v090_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_126d_base_v091_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_126d_base_v092_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_126d_base_v093_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_189d_base_v094_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_189d_base_v095_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_189d_base_v096_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_252d_base_v097_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_252d_base_v098_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_252d_base_v099_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_378d_base_v100_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_378d_base_v101_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_378d_base_v102_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimetanh_504d_base_v103_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranstanh_504d_base_v104_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrtanh_504d_base_v105_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_5d_base_v106_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_5d_base_v107_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_5d_base_v108_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_10d_base_v109_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_10d_base_v110_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_10d_base_v111_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_21d_base_v112_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_21d_base_v113_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_21d_base_v114_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_42d_base_v115_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_42d_base_v116_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_42d_base_v117_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_63d_base_v118_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_63d_base_v119_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_63d_base_v120_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_126d_base_v121_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_126d_base_v122_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_126d_base_v123_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_189d_base_v124_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_189d_base_v125_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_189d_base_v126_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_252d_base_v127_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_252d_base_v128_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_252d_base_v129_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_378d_base_v130_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_378d_base_v131_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_378d_base_v132_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimezclip_504d_base_v133_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetranszclip_504d_base_v134_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrzclip_504d_base_v135_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimevar63_5d_base_v136_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetransvar63_5d_base_v137_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrvar63_5d_base_v138_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimevar63_10d_base_v139_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetransvar63_10d_base_v140_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrvar63_10d_base_v141_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimevar63_21d_base_v142_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetransvar63_21d_base_v143_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrvar63_21d_base_v144_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimevar63_42d_base_v145_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetransvar63_42d_base_v146_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrvar63_42d_base_v147_signal,
    f029vrt_f029_vol_regime_transition_flag_volregimevar63_63d_base_v148_signal,
    f029vrt_f029_vol_regime_transition_flag_regimetransvar63_63d_base_v149_signal,
    f029vrt_f029_vol_regime_transition_flag_transstrvar63_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F029_VOL_REGIME_TRANSITION_FLAG_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f029_vol_regime', '_f029_regime_transition', '_f029_transition_strength')
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
    print(f"OK f029_vol_regime_transition_flag_base_076_150_claude: {n_features} features pass")
