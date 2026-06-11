# f04_basing_pattern_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _base_range(c, w):
    return (c.rolling(w, min_periods=1).max() / c.rolling(w, min_periods=1).min().replace(0, np.nan) - 1)

def _base_tightness(c, w):
    return c.pct_change().rolling(w, min_periods=1).std()

def _base_range_ohlc(h, l, w):
    return (h.rolling(w, min_periods=1).max() / l.rolling(w, min_periods=1).min().replace(0, np.nan) - 1)

def _z_score(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

# Feature 001: Base range 3d
def f04_basing_pattern_range_3d_base_v001_signal(arg_high, arg_low):
    res = _base_range_ohlc(arg_high, arg_low, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 002: Base range 5d
def f04_basing_pattern_range_5d_base_v002_signal(arg_high, arg_low):
    res = _base_range_ohlc(arg_high, arg_low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 003: Base range 8d
def f04_basing_pattern_range_8d_base_v003_signal(arg_close):
    res = _base_range(arg_close, 8)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 004: Base range 10d
def f04_basing_pattern_range_10d_base_v004_signal(arg_close):
    res = _base_range(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 005: Base range 12d
def f04_basing_pattern_range_12d_base_v005_signal(arg_close):
    res = _base_range(arg_close, 12)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 006: Base range 15d
def f04_basing_pattern_range_15d_base_v006_signal(arg_close):
    res = _base_range(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 007: Base range 21d
def f04_basing_pattern_range_21d_base_v007_signal(arg_close):
    res = _base_range(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 008: Base range 30d
def f04_basing_pattern_range_30d_base_v008_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 009: Base range 40d
def f04_basing_pattern_range_40d_base_v009_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 40)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 010: Base range 50d
def f04_basing_pattern_range_50d_base_v010_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 011: Base range 63d
def f04_basing_pattern_range_63d_base_v011_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 012: Base range 90d
def f04_basing_pattern_range_90d_base_v012_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 90)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 013: Base range 126d
def f04_basing_pattern_range_126d_base_v013_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 014: Base range 252d
def f04_basing_pattern_range_252d_base_v014_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 015: Base range 504d
def f04_basing_pattern_range_504d_base_v015_signal(arg_closeadj):
    res = _base_range(arg_closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 016: Base tightness 3d
def f04_basing_pattern_tightness_3d_base_v016_signal(arg_close):
    res = _base_tightness(arg_close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 017: Base tightness 5d
def f04_basing_pattern_tightness_5d_base_v017_signal(arg_close):
    res = _base_tightness(arg_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 018: Base tightness 8d
def f04_basing_pattern_tightness_8d_base_v018_signal(arg_close):
    res = _base_tightness(arg_close, 8)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 019: Base tightness 10d
def f04_basing_pattern_tightness_10d_base_v019_signal(arg_close):
    res = _base_tightness(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 020: Base tightness 12d
def f04_basing_pattern_tightness_12d_base_v020_signal(arg_close):
    res = _base_tightness(arg_close, 12)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 021: Base tightness 15d
def f04_basing_pattern_tightness_15d_base_v021_signal(arg_close):
    res = _base_tightness(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 022: Base tightness 21d
def f04_basing_pattern_tightness_21d_base_v022_signal(arg_close):
    res = _base_tightness(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 023: Base tightness 30d
def f04_basing_pattern_tightness_30d_base_v023_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 024: Base tightness 40d
def f04_basing_pattern_tightness_40d_base_v024_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 40)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 025: Base tightness 50d
def f04_basing_pattern_tightness_50d_base_v025_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 026: Base tightness 63d
def f04_basing_pattern_tightness_63d_base_v026_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 027: Base tightness 90d
def f04_basing_pattern_tightness_90d_base_v027_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 90)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 028: Base tightness 126d
def f04_basing_pattern_tightness_126d_base_v028_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 029: Base tightness 252d
def f04_basing_pattern_tightness_252d_base_v029_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 030: Base tightness 504d
def f04_basing_pattern_tightness_504d_base_v030_signal(arg_closeadj):
    res = _base_tightness(arg_closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 031: Z-score range 3d (252d window)
def f04_basing_pattern_range_z_3d_base_v031_signal(arg_high, arg_low):
    rng = _base_range_ohlc(arg_high, arg_low, 3)
    res = _z_score(rng, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 032: Z-score range 5d (252d window)
def f04_basing_pattern_range_z_5d_base_v032_signal(arg_high, arg_low):
    rng = _base_range_ohlc(arg_high, arg_low, 5)
    res = _z_score(rng, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 033: Z-score range 10d (252d window)
def f04_basing_pattern_range_z_10d_base_v033_signal(arg_close):
    rng = _base_range(arg_close, 10)
    res = _z_score(rng, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 034: Z-score range 21d (252d window)
def f04_basing_pattern_range_z_21d_base_v034_signal(arg_close):
    rng = _base_range(arg_close, 21)
    res = _z_score(rng, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 035: Z-score range 63d (252d window)
def f04_basing_pattern_range_z_63d_base_v035_signal(arg_closeadj):
    rng = _base_range(arg_closeadj, 63)
    res = _z_score(rng, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 036: Z-score tightness 3d (252d window)
def f04_basing_pattern_tightness_z_3d_base_v036_signal(arg_close):
    t = _base_tightness(arg_close, 3)
    res = _z_score(t, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 037: Z-score tightness 5d (252d window)
def f04_basing_pattern_tightness_z_5d_base_v037_signal(arg_close):
    t = _base_tightness(arg_close, 5)
    res = _z_score(t, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 038: Z-score tightness 10d (252d window)
def f04_basing_pattern_tightness_z_10d_base_v038_signal(arg_close):
    t = _base_tightness(arg_close, 10)
    res = _z_score(t, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 039: Z-score tightness 21d (252d window)
def f04_basing_pattern_tightness_z_21d_base_v039_signal(arg_close):
    t = _base_tightness(arg_close, 21)
    res = _z_score(t, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 040: Z-score tightness 63d (252d window)
def f04_basing_pattern_tightness_z_63d_base_v040_signal(arg_closeadj):
    t = _base_tightness(arg_closeadj, 63)
    res = _z_score(t, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 041: Relative range 3d / 252d
def f04_basing_pattern_range_rel_3d_252d_base_v041_signal(arg_high, arg_low, arg_closeadj):
    r3 = _base_range_ohlc(arg_high, arg_low, 3)
    r252 = _base_range(arg_closeadj, 252)
    res = r3 / r252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 042: Relative range 5d / 252d
def f04_basing_pattern_range_rel_5d_252d_base_v042_signal(arg_high, arg_low, arg_closeadj):
    r5 = _base_range_ohlc(arg_high, arg_low, 5)
    r252 = _base_range(arg_closeadj, 252)
    res = r5 / r252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 043: Relative range 10d / 252d
def f04_basing_pattern_range_rel_10d_252d_base_v043_signal(arg_close, arg_closeadj):
    r10 = _base_range(arg_close, 10)
    r252 = _base_range(arg_closeadj, 252)
    res = r10 / r252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 044: Relative range 21d / 252d
def f04_basing_pattern_range_rel_21d_252d_base_v044_signal(arg_close, arg_closeadj):
    r21 = _base_range(arg_close, 21)
    r252 = _base_range(arg_closeadj, 252)
    res = r21 / r252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 045: Relative range 63d / 252d
def f04_basing_pattern_range_rel_63d_252d_base_v045_signal(arg_closeadj):
    r63 = _base_range(arg_closeadj, 63)
    r252 = _base_range(arg_closeadj, 252)
    res = r63 / r252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 046: Relative tightness 3d / 252d
def f04_basing_pattern_tightness_rel_3d_252d_base_v046_signal(arg_close, arg_closeadj):
    t3 = _base_tightness(arg_close, 3)
    t252 = _base_tightness(arg_closeadj, 252)
    res = t3 / t252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 047: Relative tightness 5d / 252d
def f04_basing_pattern_tightness_rel_5d_252d_base_v047_signal(arg_close, arg_closeadj):
    t5 = _base_tightness(arg_close, 5)
    t252 = _base_tightness(arg_closeadj, 252)
    res = t5 / t252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 048: Relative tightness 10d / 252d
def f04_basing_pattern_tightness_rel_10d_252d_base_v048_signal(arg_close, arg_closeadj):
    t10 = _base_tightness(arg_close, 10)
    t252 = _base_tightness(arg_closeadj, 252)
    res = t10 / t252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 049: Relative tightness 21d / 252d
def f04_basing_pattern_tightness_rel_21d_252d_base_v049_signal(arg_close, arg_closeadj):
    t21 = _base_tightness(arg_close, 21)
    t252 = _base_tightness(arg_closeadj, 252)
    res = t21 / t252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 050: Relative tightness 63d / 252d
def f04_basing_pattern_tightness_rel_63d_252d_base_v050_signal(arg_closeadj):
    t63 = _base_tightness(arg_closeadj, 63)
    t252 = _base_tightness(arg_closeadj, 252)
    res = t63 / t252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 051: Days range < 5% over 10d
def f04_basing_pattern_days_tight_5pct_10d_base_v051_signal(arg_close):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.05).rolling(10, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 052: Days range < 5% over 21d
def f04_basing_pattern_days_tight_5pct_21d_base_v052_signal(arg_close):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.05).rolling(21, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 053: Days range < 5% over 63d
def f04_basing_pattern_days_tight_5pct_63d_base_v053_signal(arg_close, arg_closeadj):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.05).rolling(63, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 054: Days range < 2% over 10d
def f04_basing_pattern_days_tight_2pct_10d_base_v054_signal(arg_close):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.02).rolling(10, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 055: Days range < 2% over 21d
def f04_basing_pattern_days_tight_2pct_21d_base_v055_signal(arg_close):
    rng = _base_range(arg_close, 5)
    res = (rng < 0.02).rolling(21, min_periods=1).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 056: High to Close relative dist 5d
def f04_basing_pattern_high_to_close_rel_5d_base_v056_signal(arg_high, arg_low, arg_close):
    h = arg_high.rolling(5, min_periods=1).max()
    l = arg_low.rolling(5, min_periods=1).min()
    res = (h - arg_close) / (h - l).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 057: High to Close relative dist 10d
def f04_basing_pattern_high_to_close_rel_10d_base_v057_signal(arg_close):
    h = arg_close.rolling(10, min_periods=1).max()
    l = arg_close.rolling(10, min_periods=1).min()
    res = (h - arg_close) / (h - l).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 058: High to Close relative dist 21d
def f04_basing_pattern_high_to_close_rel_21d_base_v058_signal(arg_close):
    h = arg_close.rolling(21, min_periods=1).max()
    l = arg_close.rolling(21, min_periods=1).min()
    res = (h - arg_close) / (h - l).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 059: High to Close relative dist 63d
def f04_basing_pattern_high_to_close_rel_63d_base_v059_signal(arg_closeadj):
    h = arg_closeadj.rolling(63, min_periods=1).max()
    l = arg_closeadj.rolling(63, min_periods=1).min()
    res = (h - arg_closeadj) / (h - l).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 060: High to Close relative dist 126d
def f04_basing_pattern_high_to_close_rel_126d_base_v060_signal(arg_closeadj):
    h = arg_closeadj.rolling(126, min_periods=1).max()
    l = arg_closeadj.rolling(126, min_periods=1).min()
    res = (h - arg_closeadj) / (h - l).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 061: Volume volatility 5d
def f04_basing_pattern_vol_volatility_5d_base_v061_signal(arg_volume):
    res = arg_volume.pct_change().rolling(5, min_periods=1).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 062: Volume volatility 10d
def f04_basing_pattern_vol_volatility_10d_base_v062_signal(arg_volume):
    res = arg_volume.pct_change().rolling(10, min_periods=1).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 063: Volume volatility 21d
def f04_basing_pattern_vol_volatility_21d_base_v063_signal(arg_volume):
    res = arg_volume.pct_change().rolling(21, min_periods=1).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 064: Volume volatility 63d
def f04_basing_pattern_vol_volatility_63d_base_v064_signal(arg_volume):
    res = arg_volume.pct_change().rolling(63, min_periods=1).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 065: Breakout strength 5d
def f04_basing_pattern_breakout_strength_5d_base_v065_signal(arg_close, arg_high):
    h = arg_high.rolling(5, min_periods=1).max()
    res = arg_close / h.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 066: Breakout strength 10d
def f04_basing_pattern_breakout_strength_10d_base_v066_signal(arg_close):
    h = arg_close.rolling(10, min_periods=1).max()
    res = arg_close / h.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 067: Breakout strength 21d
def f04_basing_pattern_breakout_strength_21d_base_v067_signal(arg_close):
    h = arg_close.rolling(21, min_periods=1).max()
    res = arg_close / h.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 068: Breakout strength 63d
def f04_basing_pattern_breakout_strength_63d_base_v068_signal(arg_closeadj):
    h = arg_closeadj.rolling(63, min_periods=1).max()
    res = arg_closeadj / h.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 069: Breakout strength 126d
def f04_basing_pattern_breakout_strength_126d_base_v069_signal(arg_closeadj):
    h = arg_closeadj.rolling(126, min_periods=1).max()
    res = arg_closeadj / h.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 070: Rolling mean range 5d (over 21d)
def f04_basing_pattern_range_mean_5d_21d_base_v070_signal(arg_high, arg_low):
    rng = _base_range_ohlc(arg_high, arg_low, 5)
    res = _sma(rng, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 071: Rolling mean range 10d (over 21d)
def f04_basing_pattern_range_mean_10d_21d_base_v071_signal(arg_close):
    rng = _base_range(arg_close, 10)
    res = _sma(rng, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 072: Rolling mean range 21d (over 63d)
def f04_basing_pattern_range_mean_21d_63d_base_v072_signal(arg_close):
    rng = _base_range(arg_close, 21)
    res = _sma(rng, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 073: Rolling mean tightness 5d (over 21d)
def f04_basing_pattern_tightness_mean_5d_21d_base_v073_signal(arg_close):
    t = _base_tightness(arg_close, 5)
    res = _sma(t, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 074: Rolling mean tightness 10d (over 21d)
def f04_basing_pattern_tightness_mean_10d_21d_base_v074_signal(arg_close):
    t = _base_tightness(arg_close, 10)
    res = _sma(t, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 075: Rolling mean tightness 21d (over 63d)
def f04_basing_pattern_tightness_mean_21d_63d_base_v075_signal(arg_close):
    t = _base_tightness(arg_close, 21)
    res = _sma(t, 63)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f04_basing_pattern_range_3d_base_v001_signal": {"inputs": ["arg_high", "arg_low"], "func": f04_basing_pattern_range_3d_base_v001_signal},
    "f04_basing_pattern_range_5d_base_v002_signal": {"inputs": ["arg_high", "arg_low"], "func": f04_basing_pattern_range_5d_base_v002_signal},
    "f04_basing_pattern_range_8d_base_v003_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_8d_base_v003_signal},
    "f04_basing_pattern_range_10d_base_v004_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_10d_base_v004_signal},
    "f04_basing_pattern_range_12d_base_v005_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_12d_base_v005_signal},
    "f04_basing_pattern_range_15d_base_v006_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_15d_base_v006_signal},
    "f04_basing_pattern_range_21d_base_v007_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_21d_base_v007_signal},
    "f04_basing_pattern_range_30d_base_v008_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_30d_base_v008_signal},
    "f04_basing_pattern_range_40d_base_v009_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_40d_base_v009_signal},
    "f04_basing_pattern_range_50d_base_v010_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_50d_base_v010_signal},
    "f04_basing_pattern_range_63d_base_v011_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_63d_base_v011_signal},
    "f04_basing_pattern_range_90d_base_v012_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_90d_base_v012_signal},
    "f04_basing_pattern_range_126d_base_v013_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_126d_base_v013_signal},
    "f04_basing_pattern_range_252d_base_v014_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_252d_base_v014_signal},
    "f04_basing_pattern_range_504d_base_v015_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_504d_base_v015_signal},
    "f04_basing_pattern_tightness_3d_base_v016_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_3d_base_v016_signal},
    "f04_basing_pattern_tightness_5d_base_v017_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_5d_base_v017_signal},
    "f04_basing_pattern_tightness_8d_base_v018_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_8d_base_v018_signal},
    "f04_basing_pattern_tightness_10d_base_v019_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_10d_base_v019_signal},
    "f04_basing_pattern_tightness_12d_base_v020_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_12d_base_v020_signal},
    "f04_basing_pattern_tightness_15d_base_v021_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_15d_base_v021_signal},
    "f04_basing_pattern_tightness_21d_base_v022_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_21d_base_v022_signal},
    "f04_basing_pattern_tightness_30d_base_v023_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_30d_base_v023_signal},
    "f04_basing_pattern_tightness_40d_base_v024_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_40d_base_v024_signal},
    "f04_basing_pattern_tightness_50d_base_v025_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_50d_base_v025_signal},
    "f04_basing_pattern_tightness_63d_base_v026_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_63d_base_v026_signal},
    "f04_basing_pattern_tightness_90d_base_v027_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_90d_base_v027_signal},
    "f04_basing_pattern_tightness_126d_base_v028_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_126d_base_v028_signal},
    "f04_basing_pattern_tightness_252d_base_v029_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_252d_base_v029_signal},
    "f04_basing_pattern_tightness_504d_base_v030_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_504d_base_v030_signal},
    "f04_basing_pattern_range_z_3d_base_v031_signal": {"inputs": ["arg_high", "arg_low"], "func": f04_basing_pattern_range_z_3d_base_v031_signal},
    "f04_basing_pattern_range_z_5d_base_v032_signal": {"inputs": ["arg_high", "arg_low"], "func": f04_basing_pattern_range_z_5d_base_v032_signal},
    "f04_basing_pattern_range_z_10d_base_v033_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_z_10d_base_v033_signal},
    "f04_basing_pattern_range_z_21d_base_v034_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_z_21d_base_v034_signal},
    "f04_basing_pattern_range_z_63d_base_v035_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_z_63d_base_v035_signal},
    "f04_basing_pattern_tightness_z_3d_base_v036_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_z_3d_base_v036_signal},
    "f04_basing_pattern_tightness_z_5d_base_v037_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_z_5d_base_v037_signal},
    "f04_basing_pattern_tightness_z_10d_base_v038_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_z_10d_base_v038_signal},
    "f04_basing_pattern_tightness_z_21d_base_v039_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_z_21d_base_v039_signal},
    "f04_basing_pattern_tightness_z_63d_base_v040_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_z_63d_base_v040_signal},
    "f04_basing_pattern_range_rel_3d_252d_base_v041_signal": {"inputs": ["arg_high", "arg_low", "arg_closeadj"], "func": f04_basing_pattern_range_rel_3d_252d_base_v041_signal},
    "f04_basing_pattern_range_rel_5d_252d_base_v042_signal": {"inputs": ["arg_high", "arg_low", "arg_closeadj"], "func": f04_basing_pattern_range_rel_5d_252d_base_v042_signal},
    "f04_basing_pattern_range_rel_10d_252d_base_v043_signal": {"inputs": ["arg_close", "arg_closeadj"], "func": f04_basing_pattern_range_rel_10d_252d_base_v043_signal},
    "f04_basing_pattern_range_rel_21d_252d_base_v044_signal": {"inputs": ["arg_close", "arg_closeadj"], "func": f04_basing_pattern_range_rel_21d_252d_base_v044_signal},
    "f04_basing_pattern_range_rel_63d_252d_base_v045_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_range_rel_63d_252d_base_v045_signal},
    "f04_basing_pattern_tightness_rel_3d_252d_base_v046_signal": {"inputs": ["arg_close", "arg_closeadj"], "func": f04_basing_pattern_tightness_rel_3d_252d_base_v046_signal},
    "f04_basing_pattern_tightness_rel_5d_252d_base_v047_signal": {"inputs": ["arg_close", "arg_closeadj"], "func": f04_basing_pattern_tightness_rel_5d_252d_base_v047_signal},
    "f04_basing_pattern_tightness_rel_10d_252d_base_v048_signal": {"inputs": ["arg_close", "arg_closeadj"], "func": f04_basing_pattern_tightness_rel_10d_252d_base_v048_signal},
    "f04_basing_pattern_tightness_rel_21d_252d_base_v049_signal": {"inputs": ["arg_close", "arg_closeadj"], "func": f04_basing_pattern_tightness_rel_21d_252d_base_v049_signal},
    "f04_basing_pattern_tightness_rel_63d_252d_base_v050_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_tightness_rel_63d_252d_base_v050_signal},
    "f04_basing_pattern_days_tight_5pct_10d_base_v051_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_days_tight_5pct_10d_base_v051_signal},
    "f04_basing_pattern_days_tight_5pct_21d_base_v052_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_days_tight_5pct_21d_base_v052_signal},
    "f04_basing_pattern_days_tight_5pct_63d_base_v053_signal": {"inputs": ["arg_close", "arg_closeadj"], "func": f04_basing_pattern_days_tight_5pct_63d_base_v053_signal},
    "f04_basing_pattern_days_tight_2pct_10d_base_v054_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_days_tight_2pct_10d_base_v054_signal},
    "f04_basing_pattern_days_tight_2pct_21d_base_v055_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_days_tight_2pct_21d_base_v055_signal},
    "f04_basing_pattern_high_to_close_rel_5d_base_v056_signal": {"inputs": ["arg_high", "arg_low", "arg_close"], "func": f04_basing_pattern_high_to_close_rel_5d_base_v056_signal},
    "f04_basing_pattern_high_to_close_rel_10d_base_v057_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_high_to_close_rel_10d_base_v057_signal},
    "f04_basing_pattern_high_to_close_rel_21d_base_v058_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_high_to_close_rel_21d_base_v058_signal},
    "f04_basing_pattern_high_to_close_rel_63d_base_v059_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_high_to_close_rel_63d_base_v059_signal},
    "f04_basing_pattern_high_to_close_rel_126d_base_v060_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_high_to_close_rel_126d_base_v060_signal},
    "f04_basing_pattern_vol_volatility_5d_base_v061_signal": {"inputs": ["arg_volume"], "func": f04_basing_pattern_vol_volatility_5d_base_v061_signal},
    "f04_basing_pattern_vol_volatility_10d_base_v062_signal": {"inputs": ["arg_volume"], "func": f04_basing_pattern_vol_volatility_10d_base_v062_signal},
    "f04_basing_pattern_vol_volatility_21d_base_v063_signal": {"inputs": ["arg_volume"], "func": f04_basing_pattern_vol_volatility_21d_base_v063_signal},
    "f04_basing_pattern_vol_volatility_63d_base_v064_signal": {"inputs": ["arg_volume"], "func": f04_basing_pattern_vol_volatility_63d_base_v064_signal},
    "f04_basing_pattern_breakout_strength_5d_base_v065_signal": {"inputs": ["arg_close", "arg_high"], "func": f04_basing_pattern_breakout_strength_5d_base_v065_signal},
    "f04_basing_pattern_breakout_strength_10d_base_v066_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_breakout_strength_10d_base_v066_signal},
    "f04_basing_pattern_breakout_strength_21d_base_v067_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_breakout_strength_21d_base_v067_signal},
    "f04_basing_pattern_breakout_strength_63d_base_v068_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_breakout_strength_63d_base_v068_signal},
    "f04_basing_pattern_breakout_strength_126d_base_v069_signal": {"inputs": ["arg_closeadj"], "func": f04_basing_pattern_breakout_strength_126d_base_v069_signal},
    "f04_basing_pattern_range_mean_5d_21d_base_v070_signal": {"inputs": ["arg_high", "arg_low"], "func": f04_basing_pattern_range_mean_5d_21d_base_v070_signal},
    "f04_basing_pattern_range_mean_10d_21d_base_v071_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_mean_10d_21d_base_v071_signal},
    "f04_basing_pattern_range_mean_21d_63d_base_v072_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_range_mean_21d_63d_base_v072_signal},
    "f04_basing_pattern_tightness_mean_5d_21d_base_v073_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_mean_5d_21d_base_v073_signal},
    "f04_basing_pattern_tightness_mean_10d_21d_base_v074_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_mean_10d_21d_base_v074_signal},
    "f04_basing_pattern_tightness_mean_21d_63d_base_v075_signal": {"inputs": ["arg_close"], "func": f04_basing_pattern_tightness_mean_21d_63d_base_v075_signal},
}

F04_BASING_PATTERN_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    import inspect
    pd.set_option('display.max_columns', None)
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        "arg_open": np.exp(np.random.normal(0, 0.01, n).cumsum()) * 100,
    })
    df["arg_high"] = df["arg_open"] * (1 + np.abs(np.random.normal(0, 0.01, n)))
    df["arg_low"] = df["arg_open"] * (1 - np.abs(np.random.normal(0, 0.01, n)))
    df["arg_close"] = (df["arg_high"] + df["arg_low"]) / 2 + np.random.normal(0, 0.005, n)
    df["arg_closeadj"] = df["arg_close"] * 0.98
    df["arg_volume"] = np.random.exponential(1000, n)
    
    for name, info in REGISTRY.items():
        inputs = [df[col] for col in info["inputs"]]
        y1 = info["func"](*inputs)
        y2 = info["func"](*inputs)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 2
        assert q.std() > 0
        assert not q.isna().all()
    print("All tests passed!")
