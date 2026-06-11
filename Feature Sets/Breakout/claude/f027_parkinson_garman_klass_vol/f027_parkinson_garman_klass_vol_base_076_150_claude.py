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


def _f027_parkinson(high, low, w):
    hi = high.replace(0, np.nan).abs()
    lo = low.replace(0, np.nan).abs()
    lr = np.log(hi / lo)
    sq = (lr * lr) / (4.0 * np.log(2.0))
    return sq.rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)


def _f027_garman_klass(high, low, closeadj, w):
    hi = high.replace(0, np.nan).abs()
    lo = low.replace(0, np.nan).abs()
    cl = closeadj.replace(0, np.nan).abs()
    op = cl.shift(1).replace(0, np.nan)
    lr_hl = np.log(hi / lo)
    lr_co = np.log(cl / op)
    val = 0.5 * lr_hl * lr_hl - (2.0 * np.log(2.0) - 1.0) * lr_co * lr_co
    return val.rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=0).pow(0.5)


def _f027_hl_vol_compress(high, low, w):
    rng = (high - low).abs()
    short_std = rng.rolling(max(2, w // 4), min_periods=1).std()
    long_std = rng.rolling(w, min_periods=max(1, w // 2)).std()
    return short_std / long_std.replace(0, np.nan)


def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_5d_base_v076_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_5d_base_v077_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_5d_base_v078_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_10d_base_v079_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_10d_base_v080_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_10d_base_v081_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_21d_base_v082_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_21d_base_v083_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_21d_base_v084_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_42d_base_v085_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_42d_base_v086_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_42d_base_v087_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_63d_base_v088_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_63d_base_v089_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_63d_base_v090_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_126d_base_v091_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_126d_base_v092_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_126d_base_v093_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_189d_base_v094_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_189d_base_v095_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_189d_base_v096_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_252d_base_v097_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_252d_base_v098_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_252d_base_v099_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_378d_base_v100_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_378d_base_v101_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_378d_base_v102_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_504d_base_v103_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_504d_base_v104_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_504d_base_v105_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_5d_base_v106_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_5d_base_v107_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_5d_base_v108_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_10d_base_v109_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_10d_base_v110_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_10d_base_v111_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_21d_base_v112_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_21d_base_v113_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_21d_base_v114_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_42d_base_v115_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_42d_base_v116_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_42d_base_v117_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_63d_base_v118_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_63d_base_v119_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_63d_base_v120_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_126d_base_v121_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_126d_base_v122_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_126d_base_v123_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_189d_base_v124_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_189d_base_v125_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_189d_base_v126_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_252d_base_v127_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_252d_base_v128_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_252d_base_v129_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_378d_base_v130_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_378d_base_v131_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_378d_base_v132_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_504d_base_v133_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_504d_base_v134_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_504d_base_v135_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_5d_base_v136_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_5d_base_v137_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_5d_base_v138_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_10d_base_v139_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_10d_base_v140_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_10d_base_v141_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_21d_base_v142_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_21d_base_v143_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_21d_base_v144_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_42d_base_v145_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_42d_base_v146_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_42d_base_v147_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_63d_base_v148_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_63d_base_v149_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_63d_base_v150_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_5d_base_v076_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_5d_base_v077_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_5d_base_v078_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_10d_base_v079_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_10d_base_v080_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_10d_base_v081_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_21d_base_v082_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_21d_base_v083_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_21d_base_v084_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_42d_base_v085_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_42d_base_v086_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_42d_base_v087_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_63d_base_v088_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_63d_base_v089_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_63d_base_v090_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_126d_base_v091_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_126d_base_v092_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_126d_base_v093_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_189d_base_v094_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_189d_base_v095_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_189d_base_v096_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_252d_base_v097_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_252d_base_v098_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_252d_base_v099_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_378d_base_v100_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_378d_base_v101_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_378d_base_v102_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsontanh_504d_base_v103_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasstanh_504d_base_v104_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresstanh_504d_base_v105_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_5d_base_v106_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_5d_base_v107_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_5d_base_v108_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_10d_base_v109_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_10d_base_v110_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_10d_base_v111_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_21d_base_v112_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_21d_base_v113_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_21d_base_v114_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_42d_base_v115_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_42d_base_v116_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_42d_base_v117_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_63d_base_v118_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_63d_base_v119_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_63d_base_v120_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_126d_base_v121_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_126d_base_v122_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_126d_base_v123_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_189d_base_v124_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_189d_base_v125_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_189d_base_v126_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_252d_base_v127_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_252d_base_v128_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_252d_base_v129_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_378d_base_v130_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_378d_base_v131_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_378d_base_v132_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonzclip_504d_base_v133_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasszclip_504d_base_v134_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresszclip_504d_base_v135_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_5d_base_v136_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_5d_base_v137_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_5d_base_v138_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_10d_base_v139_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_10d_base_v140_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_10d_base_v141_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_21d_base_v142_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_21d_base_v143_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_21d_base_v144_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_42d_base_v145_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_42d_base_v146_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_42d_base_v147_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonvar63_63d_base_v148_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassvar63_63d_base_v149_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressvar63_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F027_PARKINSON_GARMAN_KLASS_VOL_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f027_parkinson', '_f027_garman_klass', '_f027_hl_vol_compress')
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
    print(f"OK f027_parkinson_garman_klass_vol_base_076_150_claude: {n_features} features pass")
