# f20_volatility_compression_expansion_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _vol_comp_ratio(vol_s, vol_l):
    return vol_s / vol_l.abs().replace(0, np.nan)

def _bb_width_val(c, w, k=2):
    ma = c.rolling(w).mean()
    std = c.rolling(w).std()
    return (2 * k * std) / ma.abs().replace(0, np.nan)

def _vol_expand_signal(vol, w):
    return (vol - vol.rolling(w).min()) / (vol.rolling(w).max() - vol.rolling(w).min()).replace(0, np.nan)

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)

def _atr(h, l, c, w):
    return _sma(_tr(h, l, c), w)

# Volatility ratio 5d vs 21d
def f20vce_f20_volatility_compression_expansion_vol_ratio_5d_21d_v001_signal(close: pd.Series) -> pd.Series:
    vol_s = _std(close, 5)
    vol_l = _std(close, 21)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 5d vs 63d
def f20vce_f20_volatility_compression_expansion_vol_ratio_5d_63d_v002_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 5)
    vol_l = _std(closeadj, 63)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 5d vs 126d
def f20vce_f20_volatility_compression_expansion_vol_ratio_5d_126d_v003_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 5)
    vol_l = _std(closeadj, 126)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 10d vs 21d
def f20vce_f20_volatility_compression_expansion_vol_ratio_10d_21d_v004_signal(close: pd.Series) -> pd.Series:
    vol_s = _std(close, 10)
    vol_l = _std(close, 21)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 10d vs 63d
def f20vce_f20_volatility_compression_expansion_vol_ratio_10d_63d_v005_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 10)
    vol_l = _std(closeadj, 63)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 10d vs 126d
def f20vce_f20_volatility_compression_expansion_vol_ratio_10d_126d_v006_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 10)
    vol_l = _std(closeadj, 126)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 21d vs 42d
def f20vce_f20_volatility_compression_expansion_vol_ratio_21d_42d_v007_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 21)
    vol_l = _std(closeadj, 42)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 21d vs 63d
def f20vce_f20_volatility_compression_expansion_vol_ratio_21d_63d_v008_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 21)
    vol_l = _std(closeadj, 63)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 21d vs 126d
def f20vce_f20_volatility_compression_expansion_vol_ratio_21d_126d_v009_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 21)
    vol_l = _std(closeadj, 126)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 63d vs 126d
def f20vce_f20_volatility_compression_expansion_vol_ratio_63d_126d_v010_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 63)
    vol_l = _std(closeadj, 126)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 63d vs 252d
def f20vce_f20_volatility_compression_expansion_vol_ratio_63d_252d_v011_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 63)
    vol_l = _std(closeadj, 252)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 63d vs 504d
def f20vce_f20_volatility_compression_expansion_vol_ratio_63d_504d_v012_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 63)
    vol_l = _std(closeadj, 504)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 126d vs 252d
def f20vce_f20_volatility_compression_expansion_vol_ratio_126d_252d_v013_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 126)
    vol_l = _std(closeadj, 252)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 126d vs 504d
def f20vce_f20_volatility_compression_expansion_vol_ratio_126d_504d_v014_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 126)
    vol_l = _std(closeadj, 504)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio 126d vs 756d
def f20vce_f20_volatility_compression_expansion_vol_ratio_126d_756d_v015_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _std(closeadj, 126)
    vol_l = _std(closeadj, 756)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 5 and std dev 1.0
def f20vce_f20_volatility_compression_expansion_bb_width_5d_k1_0_v016_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 5, 1.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 10 and std dev 1.0
def f20vce_f20_volatility_compression_expansion_bb_width_10d_k1_0_v017_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 10, 1.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 21 and std dev 1.0
def f20vce_f20_volatility_compression_expansion_bb_width_21d_k1_0_v018_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 21, 1.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 42 and std dev 1.0
def f20vce_f20_volatility_compression_expansion_bb_width_42d_k1_0_v019_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 42, 1.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 63 and std dev 1.0
def f20vce_f20_volatility_compression_expansion_bb_width_63d_k1_0_v020_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 63, 1.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 126 and std dev 1.5
def f20vce_f20_volatility_compression_expansion_bb_width_126d_k1_5_v021_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 126, 1.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 252 and std dev 1.5
def f20vce_f20_volatility_compression_expansion_bb_width_252d_k1_5_v022_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 252, 1.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 5 and std dev 2.0
def f20vce_f20_volatility_compression_expansion_bb_width_5d_k2_0_v023_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 5, 2.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 10 and std dev 2.0
def f20vce_f20_volatility_compression_expansion_bb_width_10d_k2_0_v024_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 10, 2.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 21 and std dev 2.0
def f20vce_f20_volatility_compression_expansion_bb_width_21d_k2_0_v025_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 21, 2.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 42 and std dev 2.0
def f20vce_f20_volatility_compression_expansion_bb_width_42d_k2_0_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 42, 2.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 63 and std dev 2.5
def f20vce_f20_volatility_compression_expansion_bb_width_63d_k2_5_v027_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 63, 2.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 126 and std dev 2.5
def f20vce_f20_volatility_compression_expansion_bb_width_126d_k2_5_v028_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 126, 2.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 252 and std dev 3.0
def f20vce_f20_volatility_compression_expansion_bb_width_252d_k3_0_v029_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 252, 3.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 504 and std dev 3.0
def f20vce_f20_volatility_compression_expansion_bb_width_504d_k3_0_v030_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 504, 3.0)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 5
def f20vce_f20_volatility_compression_expansion_squeeze_ratio_5d_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 5)
    std = _std(close, 5)
    res = _vol_comp_ratio(atr, std)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 10
def f20vce_f20_volatility_compression_expansion_squeeze_ratio_10d_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 10)
    std = _std(close, 10)
    res = _vol_comp_ratio(atr, std)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 21
def f20vce_f20_volatility_compression_expansion_squeeze_ratio_21d_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 21)
    std = _std(close, 21)
    res = _vol_comp_ratio(atr, std)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 42
def f20vce_f20_volatility_compression_expansion_squeeze_ratio_42d_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 42)
    std = _std(closeadj, 42)
    res = _vol_comp_ratio(atr, std)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 63
def f20vce_f20_volatility_compression_expansion_squeeze_ratio_63d_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    std = _std(closeadj, 63)
    res = _vol_comp_ratio(atr, std)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 126
def f20vce_f20_volatility_compression_expansion_squeeze_ratio_126d_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    std = _std(closeadj, 126)
    res = _vol_comp_ratio(atr, std)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 252
def f20vce_f20_volatility_compression_expansion_squeeze_ratio_252d_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    std = _std(closeadj, 252)
    res = _vol_comp_ratio(atr, std)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 504
def f20vce_f20_volatility_compression_expansion_squeeze_ratio_504d_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    std = _std(closeadj, 504)
    res = _vol_comp_ratio(atr, std)
    return res.replace([np.inf, -np.inf], np.nan)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 10 (repeat/alt)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 21 (repeat/alt)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 42 (repeat/alt)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 63 (repeat/alt)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 126 (repeat/alt)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 252 (repeat/alt)

# Keltner vs Bollinger squeeze ratio (ATR/Std) window 504 (repeat/alt)

# Volatility expansion signal (Donchian-style for vol) window 5 lookback 21
def f20vce_f20_volatility_compression_expansion_vol_expand_5d_21d_v046_signal(close: pd.Series) -> pd.Series:
    vol = _std(close, 5)
    res = _vol_expand_signal(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 10 lookback 21
def f20vce_f20_volatility_compression_expansion_vol_expand_10d_21d_v047_signal(close: pd.Series) -> pd.Series:
    vol = _std(close, 10)
    res = _vol_expand_signal(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 21 lookback 42
def f20vce_f20_volatility_compression_expansion_vol_expand_21d_42d_v048_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 21)
    res = _vol_expand_signal(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 42 lookback 63
def f20vce_f20_volatility_compression_expansion_vol_expand_42d_63d_v049_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 42)
    res = _vol_expand_signal(vol, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 63 lookback 126
def f20vce_f20_volatility_compression_expansion_vol_expand_63d_126d_v050_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 63)
    res = _vol_expand_signal(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 126 lookback 252
def f20vce_f20_volatility_compression_expansion_vol_expand_126d_252d_v051_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 126)
    res = _vol_expand_signal(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 5 lookback 63
def f20vce_f20_volatility_compression_expansion_vol_expand_5d_63d_v052_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 5)
    res = _vol_expand_signal(vol, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 10 lookback 126
def f20vce_f20_volatility_compression_expansion_vol_expand_10d_126d_v053_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 10)
    res = _vol_expand_signal(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 21 lookback 126
def f20vce_f20_volatility_compression_expansion_vol_expand_21d_126d_v054_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 21)
    res = _vol_expand_signal(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 42 lookback 252
def f20vce_f20_volatility_compression_expansion_vol_expand_42d_252d_v055_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 42)
    res = _vol_expand_signal(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 63 lookback 252
def f20vce_f20_volatility_compression_expansion_vol_expand_63d_252d_v056_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 63)
    res = _vol_expand_signal(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 126 lookback 504
def f20vce_f20_volatility_compression_expansion_vol_expand_126d_504d_v057_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 126)
    res = _vol_expand_signal(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 5 lookback 10
def f20vce_f20_volatility_compression_expansion_vol_expand_5d_10d_v058_signal(close: pd.Series) -> pd.Series:
    vol = _std(close, 5)
    res = _vol_expand_signal(vol, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (Donchian-style for vol) window 10 lookback 21

# Volatility expansion signal (Donchian-style for vol) window 21 lookback 42

# Volatility spike (ATR / SMA(ATR)) window 5 avg 21
def f20vce_f20_volatility_compression_expansion_vol_spike_5d_21d_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 5)
    atr_avg = _sma(atr, 21)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 10 avg 42
def f20vce_f20_volatility_compression_expansion_vol_spike_10d_42d_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 10)
    atr_avg = _sma(atr, 42)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 21 avg 63
def f20vce_f20_volatility_compression_expansion_vol_spike_21d_63d_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 21)
    atr_avg = _sma(atr, 63)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 42 avg 126
def f20vce_f20_volatility_compression_expansion_vol_spike_42d_126d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 42)
    atr_avg = _sma(atr, 126)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 63 avg 252
def f20vce_f20_volatility_compression_expansion_vol_spike_63d_252d_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    atr_avg = _sma(atr, 252)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 126 avg 504
def f20vce_f20_volatility_compression_expansion_vol_spike_126d_504d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    atr_avg = _sma(atr, 504)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 252 avg 756
def f20vce_f20_volatility_compression_expansion_vol_spike_252d_756d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    atr_avg = _sma(atr, 756)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 5 avg 10
def f20vce_f20_volatility_compression_expansion_vol_spike_5d_10d_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 5)
    atr_avg = _sma(atr, 10)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 10 avg 21
def f20vce_f20_volatility_compression_expansion_vol_spike_10d_21d_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 10)
    atr_avg = _sma(atr, 21)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 21 avg 42
def f20vce_f20_volatility_compression_expansion_vol_spike_21d_42d_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 21)
    atr_avg = _sma(atr, 42)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 42 avg 63
def f20vce_f20_volatility_compression_expansion_vol_spike_42d_63d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 42)
    atr_avg = _sma(atr, 63)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 63 avg 126
def f20vce_f20_volatility_compression_expansion_vol_spike_63d_126d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    atr_avg = _sma(atr, 126)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 126 avg 252
def f20vce_f20_volatility_compression_expansion_vol_spike_126d_252d_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    atr_avg = _sma(atr, 252)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 252 avg 504
def f20vce_f20_volatility_compression_expansion_vol_spike_252d_504d_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    atr_avg = _sma(atr, 504)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility spike (ATR / SMA(ATR)) window 504 avg 756
def f20vce_f20_volatility_compression_expansion_vol_spike_504d_756d_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    atr_avg = _sma(atr, 756)
    res = _vol_comp_ratio(atr, atr_avg)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f20vce_") and f.endswith("_signal")]

F20_VOLATILITY_COMPRESSION_EXPANSION_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 1000
    d = pd.DataFrame({
        "close": np.random.randn(sz).cumsum() + 100,
        "closeadj": np.random.randn(sz).cumsum() + 100,
        "high": np.random.randn(sz).cumsum() + 110,
        "low": np.random.randn(sz).cumsum() + 90,
        "ticker": ["T"] * sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F20_VOLATILITY_COMPRESSION_EXPANSION_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001_075 OK")
