# f26_accumulation_distribution_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _mf_mult(h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    return ((c - l) - (h - c)) / (h - l).abs().replace(0, np.nan)

def _mf_vol(mult: pd.Series, v: pd.Series) -> pd.Series:
    return mult * v

def _ad_osc(mfv: pd.Series, w: int) -> pd.Series:
    return mfv.rolling(w).sum() / mfv.rolling(w).std().abs().replace(0, np.nan)

def _sma(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _zscore(s: pd.Series, w: int) -> pd.Series:
    return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

# Accumulation Distribution Oscillator 5d using raw close
def f26ad_accumulation_distribution_osc_5d_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 5)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 10d using raw close
def f26ad_accumulation_distribution_osc_10d_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 10)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 21d using raw close
def f26ad_accumulation_distribution_osc_21d_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 21)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 42d using raw close
def f26ad_accumulation_distribution_osc_42d_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 42)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 63d using raw close
def f26ad_accumulation_distribution_osc_63d_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 63)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 84d using raw close
def f26ad_accumulation_distribution_osc_84d_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 84)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 126d using raw close
def f26ad_accumulation_distribution_osc_126d_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 126)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 168d using raw close
def f26ad_accumulation_distribution_osc_168d_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 168)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 252d using raw close
def f26ad_accumulation_distribution_osc_252d_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 252)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 336d using raw close
def f26ad_accumulation_distribution_osc_336d_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 336)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 504d using raw close
def f26ad_accumulation_distribution_osc_504d_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 504)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 756d using raw close
def f26ad_accumulation_distribution_osc_756d_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 756)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 5d using raw close
# Accumulation Distribution Oscillator 10d using raw close
# Accumulation Distribution Oscillator 21d using raw close
# Accumulation Distribution Oscillator 42d using raw close
# Accumulation Distribution Oscillator 63d using raw close
# Accumulation Distribution Oscillator 84d using raw close
# Accumulation Distribution Oscillator 126d using raw close
# Accumulation Distribution Oscillator 168d using raw close
# Accumulation Distribution Oscillator 42d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_42d_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 42)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 63d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_63d_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 63)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 84d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_84d_v023_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 84)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 126d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_126d_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 126)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 168d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_168d_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 168)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 252d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_252d_v026_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 252)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 336d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_336d_v027_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 336)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 504d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_504d_v028_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 504)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 756d using adjusted prices
def f26ad_accumulation_distribution_osc_adj_756d_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    mult = _mf_mult(h_adj, l_adj, closeadj)
    mfv = _mf_vol(mult, volume)
    res = _ad_osc(mfv, 756)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator 42d using adjusted prices
# Accumulation Distribution Oscillator 63d using adjusted prices
# Accumulation Distribution Oscillator 84d using adjusted prices
# Accumulation Distribution Oscillator 126d using adjusted prices
# Accumulation Distribution Oscillator 168d using adjusted prices
# Accumulation Distribution Oscillator 252d using adjusted prices
# Accumulation Distribution Oscillator 336d using adjusted prices
# Accumulation Distribution Oscillator 504d using adjusted prices
# Accumulation Distribution Oscillator 756d using adjusted prices
# Accumulation Distribution Oscillator 42d using adjusted prices
# Accumulation Distribution Oscillator 63d using adjusted prices
# Chaikin-style AD Oscillator Difference 3d and 10d
def f26ad_accumulation_distribution_chaikin_diff_3_10_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 3) - _ema(mfv, 10)
    res = res / _ema(volume, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 5d and 21d
def f26ad_accumulation_distribution_chaikin_diff_5_21_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 5) - _ema(mfv, 21)
    res = res / _ema(volume, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 10d and 42d
def f26ad_accumulation_distribution_chaikin_diff_10_42_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 10) - _ema(mfv, 42)
    res = res / _ema(volume, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 21d and 63d
def f26ad_accumulation_distribution_chaikin_diff_21_63_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 21) - _ema(mfv, 63)
    res = res / _ema(volume, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 42d and 126d
def f26ad_accumulation_distribution_chaikin_diff_42_126_v045_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 42) - _ema(mfv, 126)
    res = res / _ema(volume, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 63d and 252d
def f26ad_accumulation_distribution_chaikin_diff_63_252_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 63) - _ema(mfv, 252)
    res = res / _ema(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 126d and 504d
def f26ad_accumulation_distribution_chaikin_diff_126_504_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 126) - _ema(mfv, 504)
    res = res / _ema(volume, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 5d and 42d
def f26ad_accumulation_distribution_chaikin_diff_5_42_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 5) - _ema(mfv, 42)
    res = res / _ema(volume, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 10d and 63d
def f26ad_accumulation_distribution_chaikin_diff_10_63_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 10) - _ema(mfv, 63)
    res = res / _ema(volume, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 21d and 126d
def f26ad_accumulation_distribution_chaikin_diff_21_126_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 21) - _ema(mfv, 126)
    res = res / _ema(volume, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 42d and 252d
def f26ad_accumulation_distribution_chaikin_diff_42_252_v051_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 42) - _ema(mfv, 252)
    res = res / _ema(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 63d and 504d
def f26ad_accumulation_distribution_chaikin_diff_63_504_v052_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 63) - _ema(mfv, 504)
    res = res / _ema(volume, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 21d and 252d
def f26ad_accumulation_distribution_chaikin_diff_21_252_v053_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 21) - _ema(mfv, 252)
    res = res / _ema(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 10d and 252d
def f26ad_accumulation_distribution_chaikin_diff_10_252_v054_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 10) - _ema(mfv, 252)
    res = res / _ema(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Chaikin-style AD Oscillator Difference 5d and 63d
def f26ad_accumulation_distribution_chaikin_diff_5_63_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = _ema(mfv, 5) - _ema(mfv, 63)
    res = res / _ema(volume, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 5d
def f26ad_accumulation_distribution_rel_vol_5d_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(5).sum() / volume.rolling(5).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 10d
def f26ad_accumulation_distribution_rel_vol_10d_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(10).sum() / volume.rolling(10).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 21d
def f26ad_accumulation_distribution_rel_vol_21d_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(21).sum() / volume.rolling(21).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 42d
def f26ad_accumulation_distribution_rel_vol_42d_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(42).sum() / volume.rolling(42).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 63d
def f26ad_accumulation_distribution_rel_vol_63d_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(63).sum() / volume.rolling(63).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 84d
def f26ad_accumulation_distribution_rel_vol_84d_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(84).sum() / volume.rolling(84).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 126d
def f26ad_accumulation_distribution_rel_vol_126d_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(126).sum() / volume.rolling(126).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 168d
def f26ad_accumulation_distribution_rel_vol_168d_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(168).sum() / volume.rolling(168).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 252d
def f26ad_accumulation_distribution_rel_vol_252d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(252).sum() / volume.rolling(252).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution relative to Total Volume 336d
def f26ad_accumulation_distribution_rel_vol_336d_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    res = mfv.rolling(336).sum() / volume.rolling(336).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 5d
def f26ad_accumulation_distribution_osc_zscore_5d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 5)
    res = _zscore(osc, 5*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 10d
def f26ad_accumulation_distribution_osc_zscore_10d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 10)
    res = _zscore(osc, 10*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 21d
def f26ad_accumulation_distribution_osc_zscore_21d_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 21)
    res = _zscore(osc, 21*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 42d
def f26ad_accumulation_distribution_osc_zscore_42d_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 42)
    res = _zscore(osc, 42*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 63d
def f26ad_accumulation_distribution_osc_zscore_63d_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 63)
    res = _zscore(osc, 63*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 84d
def f26ad_accumulation_distribution_osc_zscore_84d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 84)
    res = _zscore(osc, 84*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 126d
def f26ad_accumulation_distribution_osc_zscore_126d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 126)
    res = _zscore(osc, 126*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 168d
def f26ad_accumulation_distribution_osc_zscore_168d_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 168)
    res = _zscore(osc, 168*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 252d
def f26ad_accumulation_distribution_osc_zscore_252d_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 252)
    res = _zscore(osc, 252*2)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Oscillator Z-Score 336d
def f26ad_accumulation_distribution_osc_zscore_336d_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 336)
    res = _zscore(osc, 336*2)
    return res.replace([np.inf, -np.inf], np.nan)
SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f26ad_") and f.endswith("_signal")]

F26_ACCUMULATION_DISTRIBUTION_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "volume": np.random.randint(100, 1000, sz).astype(float), "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F26_ACCUMULATION_DISTRIBUTION_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
