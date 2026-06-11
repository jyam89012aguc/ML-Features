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


def _f028_semi_vol_up(closeadj, w):
    ret = closeadj.pct_change()
    up = ret.where(ret > 0, 0.0)
    sq = up * up
    return sq.rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)


def _f028_semi_vol_down(closeadj, w):
    ret = closeadj.pct_change()
    dn = ret.where(ret < 0, 0.0)
    sq = dn * dn
    return sq.rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)


def _f028_vol_skew(closeadj, w):
    ret = closeadj.pct_change()
    up = ret.where(ret > 0, 0.0)
    dn = ret.where(ret < 0, 0.0)
    su = (up * up).rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)
    sd = (dn * dn).rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)
    return (sd - su) / (sd + su).replace(0, np.nan)


def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_5d_base_v076_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_5d_base_v077_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_5d_base_v078_signal(closeadj):
    base = _f028_vol_skew(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_10d_base_v079_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_10d_base_v080_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_10d_base_v081_signal(closeadj):
    base = _f028_vol_skew(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_21d_base_v082_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_21d_base_v083_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_21d_base_v084_signal(closeadj):
    base = _f028_vol_skew(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_42d_base_v085_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_42d_base_v086_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_42d_base_v087_signal(closeadj):
    base = _f028_vol_skew(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_63d_base_v088_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_63d_base_v089_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_63d_base_v090_signal(closeadj):
    base = _f028_vol_skew(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_126d_base_v091_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_126d_base_v092_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_126d_base_v093_signal(closeadj):
    base = _f028_vol_skew(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_189d_base_v094_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_189d_base_v095_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_189d_base_v096_signal(closeadj):
    base = _f028_vol_skew(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_252d_base_v097_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_252d_base_v098_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_252d_base_v099_signal(closeadj):
    base = _f028_vol_skew(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_378d_base_v100_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_378d_base_v101_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_378d_base_v102_signal(closeadj):
    base = _f028_vol_skew(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_504d_base_v103_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_504d_base_v104_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_504d_base_v105_signal(closeadj):
    base = _f028_vol_skew(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_5d_base_v106_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_5d_base_v107_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_5d_base_v108_signal(closeadj):
    base = _f028_vol_skew(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_10d_base_v109_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_10d_base_v110_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_10d_base_v111_signal(closeadj):
    base = _f028_vol_skew(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_21d_base_v112_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_21d_base_v113_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_21d_base_v114_signal(closeadj):
    base = _f028_vol_skew(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_42d_base_v115_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_42d_base_v116_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_42d_base_v117_signal(closeadj):
    base = _f028_vol_skew(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_63d_base_v118_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_63d_base_v119_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_63d_base_v120_signal(closeadj):
    base = _f028_vol_skew(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_126d_base_v121_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_126d_base_v122_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_126d_base_v123_signal(closeadj):
    base = _f028_vol_skew(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_189d_base_v124_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_189d_base_v125_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_189d_base_v126_signal(closeadj):
    base = _f028_vol_skew(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_252d_base_v127_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_252d_base_v128_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_252d_base_v129_signal(closeadj):
    base = _f028_vol_skew(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_378d_base_v130_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_378d_base_v131_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_378d_base_v132_signal(closeadj):
    base = _f028_vol_skew(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_504d_base_v133_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_504d_base_v134_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_504d_base_v135_signal(closeadj):
    base = _f028_vol_skew(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_5d_base_v136_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_5d_base_v137_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_5d_base_v138_signal(closeadj):
    base = _f028_vol_skew(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_10d_base_v139_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_10d_base_v140_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_10d_base_v141_signal(closeadj):
    base = _f028_vol_skew(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_21d_base_v142_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_21d_base_v143_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_21d_base_v144_signal(closeadj):
    base = _f028_vol_skew(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_42d_base_v145_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_42d_base_v146_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_42d_base_v147_signal(closeadj):
    base = _f028_vol_skew(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_63d_base_v148_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_63d_base_v149_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_63d_base_v150_signal(closeadj):
    base = _f028_vol_skew(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_5d_base_v076_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_5d_base_v077_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_5d_base_v078_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_10d_base_v079_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_10d_base_v080_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_10d_base_v081_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_21d_base_v082_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_21d_base_v083_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_21d_base_v084_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_42d_base_v085_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_42d_base_v086_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_42d_base_v087_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_63d_base_v088_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_63d_base_v089_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_63d_base_v090_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_126d_base_v091_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_126d_base_v092_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_126d_base_v093_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_189d_base_v094_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_189d_base_v095_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_189d_base_v096_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_252d_base_v097_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_252d_base_v098_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_252d_base_v099_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_378d_base_v100_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_378d_base_v101_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_378d_base_v102_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoluptanh_504d_base_v103_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldntanh_504d_base_v104_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewtanh_504d_base_v105_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_5d_base_v106_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_5d_base_v107_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_5d_base_v108_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_10d_base_v109_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_10d_base_v110_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_10d_base_v111_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_21d_base_v112_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_21d_base_v113_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_21d_base_v114_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_42d_base_v115_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_42d_base_v116_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_42d_base_v117_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_63d_base_v118_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_63d_base_v119_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_63d_base_v120_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_126d_base_v121_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_126d_base_v122_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_126d_base_v123_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_189d_base_v124_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_189d_base_v125_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_189d_base_v126_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_252d_base_v127_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_252d_base_v128_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_252d_base_v129_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_378d_base_v130_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_378d_base_v131_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_378d_base_v132_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupzclip_504d_base_v133_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnzclip_504d_base_v134_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewzclip_504d_base_v135_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_5d_base_v136_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_5d_base_v137_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_5d_base_v138_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_10d_base_v139_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_10d_base_v140_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_10d_base_v141_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_21d_base_v142_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_21d_base_v143_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_21d_base_v144_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_42d_base_v145_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_42d_base_v146_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_42d_base_v147_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupvar63_63d_base_v148_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnvar63_63d_base_v149_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewvar63_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F028_DOWNSIDE_VS_UPSIDE_VOL_SKEW_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f028_semi_vol_up', '_f028_semi_vol_down', '_f028_vol_skew')
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
    print(f"OK f028_downside_vs_upside_vol_skew_base_076_150_claude: {n_features} features pass")
