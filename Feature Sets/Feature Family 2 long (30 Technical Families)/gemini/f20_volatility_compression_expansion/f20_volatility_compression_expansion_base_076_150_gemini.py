# f20_volatility_compression_expansion_base_076_150_gemini.py
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

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)

def _atr(h, l, c, w):
    return _sma(_tr(h, l, c), w)

def _ema_std(s, w):
    # Approximated EMA volatility
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).std()

# Volatility ratio (EMA) 5d vs 21d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_5d_21d_v076_signal(close: pd.Series) -> pd.Series:
    vol_s = _ema_std(close, 5)
    vol_l = _ema_std(close, 21)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 5d vs 63d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_5d_63d_v077_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 5)
    vol_l = _ema_std(closeadj, 63)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 10d vs 21d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_10d_21d_v078_signal(close: pd.Series) -> pd.Series:
    vol_s = _ema_std(close, 10)
    vol_l = _ema_std(close, 21)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 10d vs 63d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_10d_63d_v079_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 10)
    vol_l = _ema_std(closeadj, 63)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 21d vs 63d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_21d_63d_v080_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 21)
    vol_l = _ema_std(closeadj, 63)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 21d vs 126d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_21d_126d_v081_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 21)
    vol_l = _ema_std(closeadj, 126)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 63d vs 126d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_63d_126d_v082_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 63)
    vol_l = _ema_std(closeadj, 126)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 63d vs 252d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_63d_252d_v083_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 63)
    vol_l = _ema_std(closeadj, 252)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 126d vs 252d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_126d_252d_v084_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 126)
    vol_l = _ema_std(closeadj, 252)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 126d vs 504d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_126d_504d_v085_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 126)
    vol_l = _ema_std(closeadj, 504)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 5d vs 252d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_5d_252d_v086_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 5)
    vol_l = _ema_std(closeadj, 252)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 10d vs 126d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_10d_126d_v087_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 10)
    vol_l = _ema_std(closeadj, 126)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 21d vs 252d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_21d_252d_v088_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 21)
    vol_l = _ema_std(closeadj, 252)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 42d vs 126d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_42d_126d_v089_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 42)
    vol_l = _ema_std(closeadj, 126)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility ratio (EMA) 126d vs 756d
def f20vce_f20_volatility_compression_expansion_vol_ratio_ema_126d_756d_v090_signal(closeadj: pd.Series) -> pd.Series:
    vol_s = _ema_std(closeadj, 126)
    vol_l = _ema_std(closeadj, 756)
    res = _vol_comp_ratio(vol_s, vol_l)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 5 and std dev 0.5
def f20vce_f20_volatility_compression_expansion_bb_width_5d_k0_5_v091_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 5, 0.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 10 and std dev 0.5
def f20vce_f20_volatility_compression_expansion_bb_width_10d_k0_5_v092_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 10, 0.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 21 and std dev 1.25
def f20vce_f20_volatility_compression_expansion_bb_width_21d_k1_25_v093_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 21, 1.25)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 42 and std dev 1.25
def f20vce_f20_volatility_compression_expansion_bb_width_42d_k1_25_v094_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 42, 1.25)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 63 and std dev 1.75
def f20vce_f20_volatility_compression_expansion_bb_width_63d_k1_75_v095_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 63, 1.75)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 126 and std dev 1.75
def f20vce_f20_volatility_compression_expansion_bb_width_126d_k1_75_v096_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 126, 1.75)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 252 and std dev 2.25
def f20vce_f20_volatility_compression_expansion_bb_width_252d_k2_25_v097_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 252, 2.25)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 504 and std dev 2.25
def f20vce_f20_volatility_compression_expansion_bb_width_504d_k2_25_v098_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 504, 2.25)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 21 and std dev 2.5
def f20vce_f20_volatility_compression_expansion_bb_width_21d_k2_5_v099_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 21, 2.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 63 and std dev 2.0
def f20vce_f20_volatility_compression_expansion_bb_width_63d_k2_0_v100_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 63, 2.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 126 and std dev 2.0
def f20vce_f20_volatility_compression_expansion_bb_width_126d_k2_0_v101_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 126, 2.0)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 252 and std dev 2.5
def f20vce_f20_volatility_compression_expansion_bb_width_252d_k2_5_v102_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 252, 2.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 5 and std dev 1.5
def f20vce_f20_volatility_compression_expansion_bb_width_5d_k1_5_v103_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 5, 1.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 10 and std dev 1.5
def f20vce_f20_volatility_compression_expansion_bb_width_10d_k1_5_v104_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 10, 1.5)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width with window 21 and std dev 1.75
def f20vce_f20_volatility_compression_expansion_bb_width_21d_k1_75_v105_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 21, 1.75)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 5 lookback 21
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_5d_21d_v106_signal(close: pd.Series) -> pd.Series:
    vol = _ema_std(close, 5)
    res = _vol_expand_signal(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 10 lookback 21
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_10d_21d_v107_signal(close: pd.Series) -> pd.Series:
    vol = _ema_std(close, 10)
    res = _vol_expand_signal(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 21 lookback 42
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_21d_42d_v108_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 21)
    res = _vol_expand_signal(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 42 lookback 63
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_42d_63d_v109_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 42)
    res = _vol_expand_signal(vol, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 63 lookback 126
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_63d_126d_v110_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 63)
    res = _vol_expand_signal(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 126 lookback 252
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_126d_252d_v111_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 126)
    res = _vol_expand_signal(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 5 lookback 63
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_5d_63d_v112_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 5)
    res = _vol_expand_signal(vol, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 10 lookback 126
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_10d_126d_v113_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 10)
    res = _vol_expand_signal(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 21 lookback 126
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_21d_126d_v114_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 21)
    res = _vol_expand_signal(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 42 lookback 252
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_42d_252d_v115_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 42)
    res = _vol_expand_signal(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 63 lookback 252
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_63d_252d_v116_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 63)
    res = _vol_expand_signal(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 126 lookback 504
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_126d_504d_v117_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 126)
    res = _vol_expand_signal(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 5 lookback 42
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_5d_42d_v118_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 5)
    res = _vol_expand_signal(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 10 lookback 63
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_10d_63d_v119_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 10)
    res = _vol_expand_signal(vol, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion signal (EMA vol) window 21 lookback 252
def f20vce_f20_volatility_compression_expansion_vol_expand_ema_21d_252d_v120_signal(closeadj: pd.Series) -> pd.Series:
    vol = _ema_std(closeadj, 21)
    res = _vol_expand_signal(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 5
def f20vce_f20_volatility_compression_expansion_donchian_atr_squeeze_5d_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    width = high.rolling(5).max() - low.rolling(5).min()
    atr = _atr(high, low, close, 5)
    res = _vol_comp_ratio(width, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 10
def f20vce_f20_volatility_compression_expansion_donchian_atr_squeeze_10d_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    width = high.rolling(10).max() - low.rolling(10).min()
    atr = _atr(high, low, close, 10)
    res = _vol_comp_ratio(width, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 21
def f20vce_f20_volatility_compression_expansion_donchian_atr_squeeze_21d_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    width = high.rolling(21).max() - low.rolling(21).min()
    atr = _atr(high, low, close, 21)
    res = _vol_comp_ratio(width, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 42
def f20vce_f20_volatility_compression_expansion_donchian_atr_squeeze_42d_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    width = h_adj.rolling(42).max() - l_adj.rolling(42).min()
    atr = _atr(h_adj, l_adj, closeadj, 42)
    res = _vol_comp_ratio(width, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 63
def f20vce_f20_volatility_compression_expansion_donchian_atr_squeeze_63d_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    width = h_adj.rolling(63).max() - l_adj.rolling(63).min()
    atr = _atr(h_adj, l_adj, closeadj, 63)
    res = _vol_comp_ratio(width, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 126
def f20vce_f20_volatility_compression_expansion_donchian_atr_squeeze_126d_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    width = h_adj.rolling(126).max() - l_adj.rolling(126).min()
    atr = _atr(h_adj, l_adj, closeadj, 126)
    res = _vol_comp_ratio(width, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 252
def f20vce_f20_volatility_compression_expansion_donchian_atr_squeeze_252d_v127_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    width = h_adj.rolling(252).max() - l_adj.rolling(252).min()
    atr = _atr(h_adj, l_adj, closeadj, 252)
    res = _vol_comp_ratio(width, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 504
def f20vce_f20_volatility_compression_expansion_donchian_atr_squeeze_504d_v128_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    width = h_adj.rolling(504).max() - l_adj.rolling(504).min()
    atr = _atr(h_adj, l_adj, closeadj, 504)
    res = _vol_comp_ratio(width, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Donchian Width / ATR Squeeze window 21 (alt)

# Donchian Width / ATR Squeeze window 63 (alt)

# BB Width relative to its SMA window 5 avg 21
def f20vce_f20_volatility_compression_expansion_bb_width_rel_5d_21d_v131_signal(close: pd.Series) -> pd.Series:
    bbw = _bb_width_val(close, 5, 2.0)
    bbw_avg = _sma(bbw, 21)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its SMA window 10 avg 42
def f20vce_f20_volatility_compression_expansion_bb_width_rel_10d_42d_v132_signal(closeadj: pd.Series) -> pd.Series:
    bbw = _bb_width_val(closeadj, 10, 2.0)
    bbw_avg = _sma(bbw, 42)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its SMA window 21 avg 63
def f20vce_f20_volatility_compression_expansion_bb_width_rel_21d_63d_v133_signal(closeadj: pd.Series) -> pd.Series:
    bbw = _bb_width_val(closeadj, 21, 2.0)
    bbw_avg = _sma(bbw, 63)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its SMA window 42 avg 126
def f20vce_f20_volatility_compression_expansion_bb_width_rel_42d_126d_v134_signal(closeadj: pd.Series) -> pd.Series:
    bbw = _bb_width_val(closeadj, 42, 2.0)
    bbw_avg = _sma(bbw, 126)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its SMA window 63 avg 252
def f20vce_f20_volatility_compression_expansion_bb_width_rel_63d_252d_v135_signal(closeadj: pd.Series) -> pd.Series:
    bbw = _bb_width_val(closeadj, 63, 2.0)
    bbw_avg = _sma(bbw, 252)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its EMA window 5 avg 21
def f20vce_f20_volatility_compression_expansion_bb_width_rel_ema_5d_21d_v136_signal(close: pd.Series) -> pd.Series:
    bbw = _bb_width_val(close, 5, 2.0)
    bbw_avg = _ema(bbw, 21)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its EMA window 10 avg 42
def f20vce_f20_volatility_compression_expansion_bb_width_rel_ema_10d_42d_v137_signal(closeadj: pd.Series) -> pd.Series:
    bbw = _bb_width_val(closeadj, 10, 2.0)
    bbw_avg = _ema(bbw, 42)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its EMA window 21 avg 63
def f20vce_f20_volatility_compression_expansion_bb_width_rel_ema_21d_63d_v138_signal(closeadj: pd.Series) -> pd.Series:
    bbw = _bb_width_val(closeadj, 21, 2.0)
    bbw_avg = _ema(bbw, 63)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its EMA window 42 avg 126
def f20vce_f20_volatility_compression_expansion_bb_width_rel_ema_42d_126d_v139_signal(closeadj: pd.Series) -> pd.Series:
    bbw = _bb_width_val(closeadj, 42, 2.0)
    bbw_avg = _ema(bbw, 126)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width relative to its EMA window 63 avg 252
def f20vce_f20_volatility_compression_expansion_bb_width_rel_ema_63d_252d_v140_signal(closeadj: pd.Series) -> pd.Series:
    bbw = _bb_width_val(closeadj, 63, 2.0)
    bbw_avg = _ema(bbw, 252)
    res = _vol_comp_ratio(bbw, bbw_avg)
    return res.replace([np.inf, -np.inf], np.nan)

# Std Dev relative to ATR window 5
def f20vce_f20_volatility_compression_expansion_std_atr_ratio_5d_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    std = _std(close, 5)
    atr = _atr(high, low, close, 5)
    res = _vol_comp_ratio(std, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Std Dev relative to ATR window 21
def f20vce_f20_volatility_compression_expansion_std_atr_ratio_21d_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    std = _std(close, 21)
    atr = _atr(high, low, close, 21)
    res = _vol_comp_ratio(std, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Std Dev relative to ATR window 63
def f20vce_f20_volatility_compression_expansion_std_atr_ratio_63d_v143_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = _std(closeadj, 63)
    atr = _atr(h_adj, l_adj, closeadj, 63)
    res = _vol_comp_ratio(std, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# ATR expansion window 5 lookback 21
def f20vce_f20_volatility_compression_expansion_atr_expand_5d_21d_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 5)
    res = _vol_expand_signal(atr, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# ATR expansion window 21 lookback 63
def f20vce_f20_volatility_compression_expansion_atr_expand_21d_63d_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 21)
    res = _vol_expand_signal(atr, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# High-Low Range / ATR ratio window 5
def f20vce_f20_volatility_compression_expansion_hl_atr_ratio_5d_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hl = high - low
    atr = _atr(high, low, close, 5)
    res = _vol_comp_ratio(hl, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# High-Low Range / ATR ratio window 21
def f20vce_f20_volatility_compression_expansion_hl_atr_ratio_21d_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hl = high - low
    atr = _atr(high, low, close, 21)
    res = _vol_comp_ratio(hl, atr)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width at 1.0 std dev / 2.0 std dev ratio window 21
def f20vce_f20_volatility_compression_expansion_bbw_ratio_1_2_21d_v148_signal(close: pd.Series) -> pd.Series:
    bbw1 = _bb_width_val(close, 21, 1.0)
    bbw2 = _bb_width_val(close, 21, 2.0)
    res = _vol_comp_ratio(bbw1, bbw2)
    return res.replace([np.inf, -np.inf], np.nan)

# BB Width at 1.5 std dev / 2.5 std dev ratio window 63
def f20vce_f20_volatility_compression_expansion_bbw_ratio_15_25_63d_v149_signal(closeadj: pd.Series) -> pd.Series:
    bbw1 = _bb_width_val(closeadj, 63, 1.5)
    bbw2 = _bb_width_val(closeadj, 63, 2.5)
    res = _vol_comp_ratio(bbw1, bbw2)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility expansion window 252 lookback 504
def f20vce_f20_volatility_compression_expansion_vol_expand_252d_504d_v150_signal(closeadj: pd.Series) -> pd.Series:
    vol = _std(closeadj, 252)
    res = _vol_expand_signal(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f20vce_") and f.endswith("_signal")]

F20_VOLATILITY_COMPRESSION_EXPANSION_BASE_REGISTRY_076_150 = {
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
    for n, c in F20_VOLATILITY_COMPRESSION_EXPANSION_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076_150 OK")
