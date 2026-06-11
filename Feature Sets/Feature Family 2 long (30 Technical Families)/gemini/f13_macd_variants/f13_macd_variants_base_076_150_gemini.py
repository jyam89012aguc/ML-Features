# f13_macd_variants_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)
def _macd_val(c, f, s):
    return (_ema(c, f) - _ema(c, s)) / _ema(c, s).abs().replace(0, np.nan)
def _macd_sig(macd, sig):
    return _ema(macd, sig)
def _macd_h(macd, signal):
    return macd - signal

# MACD value using (12, 26) on closeadj, z-scored over 126 days
def f13mv_macd_val_adj_zscore_126_v076_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    res = _z(val, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (12, 26, 9) on closeadj, z-scored over 126 days
def f13mv_macd_h_adj_zscore_126_v077_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    sig = _macd_sig(val, 9)
    h = _macd_h(val, sig)
    res = _z(h, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (21, 50) on closeadj, z-scored over 252 days
def f13mv_macd_val_adj_21_50_zscore_252_v078_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    res = _z(val, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (21, 50, 15) on closeadj, z-scored over 252 days
def f13mv_macd_h_adj_21_50_15_zscore_252_v079_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    h = _macd_h(val, sig)
    res = _z(h, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (12, 26) on close price, z-scored over 252 days
def f13mv_macd_val_zscore_252_v080_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _z(val, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (12, 26, 9) on close price, z-scored over 252 days
def f13mv_macd_h_zscore_252_v081_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    h = _macd_h(val, sig)
    res = _z(h, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (5, 13) on close price, z-scored over 252 days
def f13mv_macd_val_5_13_zscore_252_v082_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    res = _z(val, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (5, 13, 5) on close price, z-scored over 252 days
def f13mv_macd_h_5_13_5_zscore_252_v083_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    sig = _macd_sig(val, 5)
    h = _macd_h(val, sig)
    res = _z(h, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (12, 26) on high/low average (median) on closeadj
def f13mv_macd_val_hl2_adj_12_26_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    hl2_adj = (high * adj + low * adj) / 2
    res = _macd_val(hl2_adj, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (12, 26, 9) on high/low average (median) on closeadj
def f13mv_macd_sig_hl2_adj_12_26_9_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    hl2_adj = (high * adj + low * adj) / 2
    val = _macd_val(hl2_adj, 12, 26)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (12, 26, 9) on high/low average (median) on closeadj
def f13mv_macd_h_hl2_adj_12_26_9_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    hl2_adj = (high * adj + low * adj) / 2
    val = _macd_val(hl2_adj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (12, 26) on typical price on closeadj
def f13mv_macd_val_typ_adj_12_26_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (12, 26, 9) on typical price on closeadj
def f13mv_macd_sig_typ_adj_12_26_9_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    val = _macd_val(typ_adj, 12, 26)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (12, 26, 9) on typical price on closeadj
def f13mv_macd_h_typ_adj_12_26_9_v089_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    val = _macd_val(typ_adj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (15, 35)
def f13mv_macd_val_15_35_v090_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 15, 35)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (15, 35, 9)
def f13mv_macd_sig_15_35_9_v091_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 15, 35)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (15, 35, 9)
def f13mv_macd_h_15_35_9_v092_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 15, 35)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (15, 35) on closeadj
def f13mv_macd_val_adj_15_35_v093_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 35)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (15, 35, 9) on closeadj
def f13mv_macd_sig_adj_15_35_9_v094_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 15, 35)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (15, 35, 9) on closeadj
def f13mv_macd_h_adj_15_35_9_v095_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 15, 35)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (10, 30)
def f13mv_macd_val_10_30_v096_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (10, 30, 10)
def f13mv_macd_sig_10_30_10_v097_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 30)
    res = _macd_sig(val, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (10, 30, 10)
def f13mv_macd_h_10_30_10_v098_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 30)
    sig = _macd_sig(val, 10)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (10, 30) on closeadj
def f13mv_macd_val_adj_10_30_v099_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (10, 30, 10) on closeadj
def f13mv_macd_sig_adj_10_30_10_v100_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 30)
    res = _macd_sig(val, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (10, 30, 10) on closeadj
def f13mv_macd_h_adj_10_30_10_v101_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 30)
    sig = _macd_sig(val, 10)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (40, 100) on closeadj
def f13mv_macd_val_adj_40_100_v102_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 100)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (40, 100, 20) on closeadj
def f13mv_macd_sig_adj_40_100_20_v103_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 40, 100)
    res = _macd_sig(val, 20)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (40, 100, 20) on closeadj
def f13mv_macd_h_adj_40_100_20_v104_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 40, 100)
    sig = _macd_sig(val, 20)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (20, 60) on closeadj
def f13mv_macd_val_adj_20_60_v105_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 60)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (20, 60, 15) on closeadj
def f13mv_macd_sig_adj_20_60_15_v106_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 20, 60)
    res = _macd_sig(val, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (20, 60, 15) on closeadj
def f13mv_macd_h_adj_20_60_15_v107_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 20, 60)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (12, 26) on close price, z-scored over 63 days
def f13mv_macd_val_zscore_63_v108_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _z(val, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (12, 26, 9) on close price, z-scored over 63 days
def f13mv_macd_h_zscore_63_v109_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    h = _macd_h(val, sig)
    res = _z(h, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (5, 13) on close price, z-scored over 63 days
def f13mv_macd_val_5_13_zscore_63_v110_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    res = _z(val, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (5, 13, 5) on close price, z-scored over 63 days
def f13mv_macd_h_5_13_5_zscore_63_v111_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    sig = _macd_sig(val, 5)
    h = _macd_h(val, sig)
    res = _z(h, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (21, 50) on closeadj, z-scored over 63 days
def f13mv_macd_val_adj_21_50_zscore_63_v112_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    res = _z(val, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (21, 50, 15) on closeadj, z-scored over 63 days
def f13mv_macd_h_adj_21_50_15_zscore_63_v113_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    h = _macd_h(val, sig)
    res = _z(h, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (12, 26) on high/low average (median)

# MACD signal using (12, 26, 9) on high/low average (median)

# MACD histogram using (12, 26, 9) on high/low average (median)

# MACD value using (5, 13) on typical price
def f13mv_macd_val_typ_5_13_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 5, 13)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (5, 13, 5) on typical price
def f13mv_macd_sig_typ_5_13_5_v118_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    val = _macd_val(typ, 5, 13)
    res = _macd_sig(val, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (5, 13, 5) on typical price
def f13mv_macd_h_typ_5_13_5_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    val = _macd_val(typ, 5, 13)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (21, 50) on typical price on closeadj
def f13mv_macd_val_typ_adj_21_50_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 21, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (21, 50, 15) on typical price on closeadj
def f13mv_macd_sig_typ_adj_21_50_15_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    val = _macd_val(typ_adj, 21, 50)
    res = _macd_sig(val, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (21, 50, 15) on typical price on closeadj
def f13mv_macd_h_typ_adj_21_50_15_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    val = _macd_val(typ_adj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (8, 20)
def f13mv_macd_val_8_20_v123_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 20)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (8, 20, 7)
def f13mv_macd_sig_8_20_7_v124_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 8, 20)
    res = _macd_sig(val, 7)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (8, 20, 7)
def f13mv_macd_h_8_20_7_v125_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 8, 20)
    sig = _macd_sig(val, 7)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (8, 20) on closeadj
def f13mv_macd_val_adj_8_20_v126_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 8, 20)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (8, 20, 7) on closeadj
def f13mv_macd_sig_adj_8_20_7_v127_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 8, 20)
    res = _macd_sig(val, 7)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (8, 20, 7) on closeadj
def f13mv_macd_h_adj_8_20_7_v128_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 8, 20)
    sig = _macd_sig(val, 7)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (10, 25)
def f13mv_macd_val_10_25_v129_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 25)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (10, 25, 8)
def f13mv_macd_sig_10_25_8_v130_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 25)
    res = _macd_sig(val, 8)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (10, 25, 8)
def f13mv_macd_h_10_25_8_v131_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 25)
    sig = _macd_sig(val, 8)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (10, 25) on closeadj
def f13mv_macd_val_adj_10_25_v132_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 25)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (10, 25, 8) on closeadj
def f13mv_macd_sig_adj_10_25_8_v133_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 25)
    res = _macd_sig(val, 8)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (10, 25, 8) on closeadj
def f13mv_macd_h_adj_10_25_8_v134_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 25)
    sig = _macd_sig(val, 8)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (25, 50) on closeadj
def f13mv_macd_val_adj_25_50_v135_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 25, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (25, 50, 10) on closeadj
def f13mv_macd_sig_adj_25_50_10_v136_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 25, 50)
    res = _macd_sig(val, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (25, 50, 10) on closeadj
def f13mv_macd_h_adj_25_50_10_v137_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 25, 50)
    sig = _macd_sig(val, 10)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (15, 60) on closeadj
def f13mv_macd_val_adj_15_60_v138_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 60)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (15, 60, 15) on closeadj
def f13mv_macd_sig_adj_15_60_15_v139_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 15, 60)
    res = _macd_sig(val, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (15, 60, 15) on closeadj
def f13mv_macd_h_adj_15_60_15_v140_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 15, 60)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (30, 90) on closeadj
def f13mv_macd_val_adj_30_90_v141_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 30, 90)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (30, 90, 20) on closeadj
def f13mv_macd_sig_adj_30_90_20_v142_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 30, 90)
    res = _macd_sig(val, 20)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (30, 90, 20) on closeadj
def f13mv_macd_h_adj_30_90_20_v143_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 30, 90)
    sig = _macd_sig(val, 20)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (50, 150) on closeadj
def f13mv_macd_val_adj_50_150_v144_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 150)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (50, 150, 30) on closeadj
def f13mv_macd_sig_adj_50_150_30_v145_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 50, 150)
    res = _macd_sig(val, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (50, 150, 30) on closeadj
def f13mv_macd_h_adj_50_150_30_v146_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 50, 150)
    sig = _macd_sig(val, 30)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (10, 50) on closeadj
def f13mv_macd_val_adj_10_50_v147_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal using (10, 50, 10) on closeadj
def f13mv_macd_sig_adj_10_50_10_v148_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 50)
    res = _macd_sig(val, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using (10, 50, 10) on closeadj
def f13mv_macd_h_adj_10_50_10_v149_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 50)
    sig = _macd_sig(val, 10)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (5, 20)
def f13mv_macd_val_5_20_v150_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 20)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f13mv_") and f.endswith("_signal")]

F13_MACD_VARIANTS_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 500
    d = pd.DataFrame({
        "close": np.random.randn(sz).cumsum() + 100,
        "closeadj": np.random.randn(sz).cumsum() + 100,
        "high": np.random.randn(sz).cumsum() + 110,
        "low": np.random.randn(sz).cumsum() + 90,
        "ticker": ["T"] * sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F13_MACD_VARIANTS_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076_150 OK")
