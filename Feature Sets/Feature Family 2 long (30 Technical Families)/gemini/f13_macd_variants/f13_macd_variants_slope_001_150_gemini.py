# f13_macd_variants_slope_001_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _macd_val(c, f, s):
    return (_ema(c, f) - _ema(c, s)) / _ema(c, s).abs().replace(0, np.nan)
def _macd_sig(macd, sig):
    return _ema(macd, sig)
def _macd_h(macd, signal):
    return macd - signal

# MACD val (12, 26) slope 5d
def f13mv_macd_val_12_26_slope_5_v001_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 10d
def f13mv_macd_val_12_26_slope_10_v002_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 21d
def f13mv_macd_val_12_26_slope_21_v003_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) adj slope 21d
def f13mv_macd_val_adj_12_26_slope_21_v004_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) adj slope 63d
def f13mv_macd_val_adj_12_26_slope_63_v005_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) slope 5d
def f13mv_macd_sig_12_26_9_slope_5_v006_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _macd_sig(val, 9).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) slope 10d
def f13mv_macd_sig_12_26_9_slope_10_v007_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _macd_sig(val, 9).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) slope 21d
def f13mv_macd_sig_12_26_9_slope_21_v008_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _macd_sig(val, 9).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) adj slope 21d
def f13mv_macd_sig_adj_12_26_9_slope_21_v009_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    res = _macd_sig(val, 9).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) adj slope 63d
def f13mv_macd_sig_adj_12_26_9_slope_63_v010_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    res = _macd_sig(val, 9).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 5d
def f13mv_macd_h_12_26_9_slope_5_v011_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 10d
def f13mv_macd_h_12_26_9_slope_10_v012_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 21d
def f13mv_macd_h_12_26_9_slope_21_v013_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) adj slope 21d
def f13mv_macd_h_adj_12_26_9_slope_21_v014_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) adj slope 63d
def f13mv_macd_h_adj_12_26_9_slope_63_v015_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term MACD val (5, 13) slope 5d
def f13mv_macd_val_5_13_slope_5_v016_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 13).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term MACD val (5, 13) slope 10d
def f13mv_macd_val_5_13_slope_10_v017_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 13).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term MACD val (5, 13) slope 21d
def f13mv_macd_val_5_13_slope_21_v018_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 13).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term MACD sig (5, 13, 5) slope 5d
def f13mv_macd_sig_5_13_5_slope_5_v019_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    res = _macd_sig(val, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term MACD sig (5, 13, 5) slope 10d
def f13mv_macd_sig_5_13_5_slope_10_v020_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    res = _macd_sig(val, 5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term MACD h (5, 13, 5) slope 5d
def f13mv_macd_h_5_13_5_slope_5_v021_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term MACD h (5, 13, 5) slope 10d
def f13mv_macd_h_5_13_5_slope_10_v022_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term MACD val (21, 50) slope 21d
def f13mv_macd_val_21_50_slope_21_v023_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term MACD val (21, 50) slope 63d
def f13mv_macd_val_21_50_slope_63_v024_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term MACD val (21, 50) slope 126d
def f13mv_macd_val_21_50_slope_126_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term MACD sig (21, 50, 15) slope 21d
def f13mv_macd_sig_21_50_15_slope_21_v026_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    res = _macd_sig(val, 15).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term MACD sig (21, 50, 15) slope 63d
def f13mv_macd_sig_21_50_15_slope_63_v027_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    res = _macd_sig(val, 15).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term MACD h (21, 50, 15) slope 21d
def f13mv_macd_h_21_50_15_slope_21_v028_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term MACD h (21, 50, 15) slope 63d
def f13mv_macd_h_21_50_15_slope_63_v029_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD typical (12, 26) slope 5d
def f13mv_macd_val_typ_12_26_slope_5_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 12, 26).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD typical (12, 26) slope 21d
def f13mv_macd_val_typ_12_26_slope_21_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 12, 26).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD typical adj (12, 26) slope 21d
def f13mv_macd_val_typ_adj_12_26_slope_21_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 12, 26).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD median (12, 26) slope 5d
def f13mv_macd_val_med_12_26_slope_5_v033_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 12, 26).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD median (12, 26) slope 21d
def f13mv_macd_val_med_12_26_slope_21_v034_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 12, 26).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 20) slope 5d
def f13mv_macd_val_10_20_slope_5_v035_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 20).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 20) slope 10d
def f13mv_macd_val_10_20_slope_10_v036_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 20).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (10, 20, 7) slope 5d
def f13mv_macd_sig_10_20_7_slope_5_v037_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 20)
    res = _macd_sig(val, 7).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (10, 20, 7) slope 5d
def f13mv_macd_h_10_20_7_slope_5_v038_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 20)
    sig = _macd_sig(val, 7)
    res = _macd_h(val, sig).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 40) adj slope 21d
def f13mv_macd_val_20_40_adj_slope_21_v039_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 40).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 40) adj slope 63d
def f13mv_macd_val_20_40_adj_slope_63_v040_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 40).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (20, 40, 9) adj slope 21d
def f13mv_macd_sig_20_40_9_adj_slope_21_v041_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 20, 40)
    res = _macd_sig(val, 9).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (20, 40, 9) adj slope 21d
def f13mv_macd_h_20_40_9_adj_slope_21_v042_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 20, 40)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 100) adj slope 63d
def f13mv_macd_val_50_100_adj_slope_63_v043_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 100).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 100) adj slope 126d
def f13mv_macd_val_50_100_adj_slope_126_v044_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 100).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (50, 100, 20) adj slope 63d
def f13mv_macd_sig_50_100_20_adj_slope_63_v045_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 50, 100)
    res = _macd_sig(val, 20).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (50, 100, 20) adj slope 63d
def f13mv_macd_h_50_100_20_adj_slope_63_v046_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 50, 100)
    sig = _macd_sig(val, 20)
    res = _macd_h(val, sig).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (3, 10) slope 5d
def f13mv_macd_val_3_10_slope_5_v047_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 3, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (3, 10) slope 10d
def f13mv_macd_val_3_10_slope_10_v048_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 3, 10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (3, 10, 16) slope 10d
def f13mv_macd_sig_3_10_16_slope_10_v049_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 3, 10)
    res = _macd_sig(val, 16).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (3, 10, 16) slope 10d
def f13mv_macd_h_3_10_16_slope_10_v050_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 3, 10)
    sig = _macd_sig(val, 16)
    res = _macd_h(val, sig).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val high (12, 26) slope 5d
def f13mv_macd_val_high_12_26_slope_5_v051_signal(high: pd.Series) -> pd.Series:
    res = _macd_val(high, 12, 26).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val low (12, 26) slope 5d
def f13mv_macd_val_low_12_26_slope_5_v052_signal(low: pd.Series) -> pd.Series:
    res = _macd_val(low, 12, 26).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 17) slope 5d
def f13mv_macd_val_8_17_slope_5_v053_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 17).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (8, 17, 9) slope 5d
def f13mv_macd_sig_8_17_9_slope_5_v054_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 8, 17)
    res = _macd_sig(val, 9).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (24, 52) adj slope 21d
def f13mv_macd_val_24_52_adj_slope_21_v055_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 24, 52).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (24, 52, 18) adj slope 21d
def f13mv_macd_sig_24_52_18_adj_slope_21_v056_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 24, 52)
    res = _macd_sig(val, 18).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (24, 52, 18) adj slope 21d
def f13mv_macd_h_24_52_18_adj_slope_21_v057_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 24, 52)
    sig = _macd_sig(val, 18)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 35) slope 5d
def f13mv_macd_val_5_35_slope_5_v058_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 35).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (5, 35, 5) slope 5d
def f13mv_macd_sig_5_35_5_slope_5_v059_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 35)
    res = _macd_sig(val, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (5, 35, 5) slope 5d
def f13mv_macd_h_5_35_5_slope_5_v060_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 35)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 100) adj slope 63d
def f13mv_macd_val_10_100_adj_slope_63_v061_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 100).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (10, 100, 10) adj slope 63d
def f13mv_macd_sig_10_100_10_adj_slope_63_v062_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 100)
    res = _macd_sig(val, 10).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (10, 100, 10) adj slope 63d
def f13mv_macd_h_10_100_10_adj_slope_63_v063_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 100)
    sig = _macd_sig(val, 10)
    res = _macd_h(val, sig).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (19, 39) adj slope 21d
def f13mv_macd_val_19_39_adj_slope_21_v064_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 19, 39).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (19, 39, 9) adj slope 21d
def f13mv_macd_sig_19_39_9_adj_slope_21_v065_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 19, 39)
    res = _macd_sig(val, 9).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (19, 39, 9) adj slope 21d
def f13mv_macd_h_19_39_9_adj_slope_21_v066_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 19, 39)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD typical (6, 13) slope 5d
def f13mv_macd_val_typ_6_13_slope_5_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 6, 13).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD median (6, 13) slope 5d
def f13mv_macd_val_med_6_13_slope_5_v068_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 6, 13).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (13, 26) slope 5d
def f13mv_macd_val_13_26_slope_5_v069_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 13, 26).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (13, 26, 9) slope 5d
def f13mv_macd_sig_13_26_9_slope_5_v070_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 13, 26)
    res = _macd_sig(val, 9).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (2, 5) slope 5d
def f13mv_macd_val_2_5_slope_5_v071_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 2, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (2, 5, 2) slope 5d
def f13mv_macd_sig_2_5_2_slope_5_v072_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 2, 5)
    res = _macd_sig(val, 2).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 80) adj slope 63d
def f13mv_macd_val_40_80_adj_slope_63_v073_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 80).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (40, 80, 20) adj slope 63d
def f13mv_macd_sig_40_80_20_adj_slope_63_v074_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 40, 80)
    res = _macd_sig(val, 20).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (100, 200) adj slope 126d
def f13mv_macd_val_100_200_adj_slope_126_v075_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 100, 200).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (100, 200, 50) adj slope 126d
def f13mv_macd_sig_100_200_50_adj_slope_126_v076_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 100, 200)
    res = _macd_sig(val, 50).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 35) slope 10d
def f13mv_macd_val_15_35_slope_10_v077_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 15, 35).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (15, 35, 9) slope 10d
def f13mv_macd_sig_15_35_9_slope_10_v078_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 15, 35)
    res = _macd_sig(val, 9).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 30) slope 10d
def f13mv_macd_val_10_30_slope_10_v079_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 30).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (10, 30, 10) slope 10d
def f13mv_macd_sig_10_30_10_slope_10_v080_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 30)
    res = _macd_sig(val, 10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 100) adj slope 63d
def f13mv_macd_val_40_100_adj_slope_63_v081_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 100).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (40, 100, 20) adj slope 63d
def f13mv_macd_sig_40_100_20_adj_slope_63_v082_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 40, 100)
    res = _macd_sig(val, 20).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 60) adj slope 63d
def f13mv_macd_val_20_60_adj_slope_63_v083_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 60).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (20, 60, 15) adj slope 63d
def f13mv_macd_sig_20_60_15_adj_slope_63_v084_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 20, 60)
    res = _macd_sig(val, 15).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 63d

# MACD sig (12, 26, 9) slope 63d

# MACD h (12, 26, 9) slope 63d

# MACD typical (5, 13) slope 5d
def f13mv_macd_val_typ_5_13_slope_5_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 5, 13).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD median (5, 13) slope 5d
def f13mv_macd_val_med_5_13_slope_5_v089_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 5, 13).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 20) slope 5d
def f13mv_macd_val_8_20_slope_5_v090_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 20).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 20) adj slope 21d
def f13mv_macd_val_8_20_adj_slope_21_v091_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 8, 20).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (8, 20, 7) slope 5d
def f13mv_macd_sig_8_20_7_slope_5_v092_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 8, 20)
    res = _macd_sig(val, 7).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (8, 20, 7) slope 5d
def f13mv_macd_h_8_20_7_slope_5_v093_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 8, 20)
    sig = _macd_sig(val, 7)
    res = _macd_h(val, sig).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 25) slope 5d
def f13mv_macd_val_10_25_slope_5_v094_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 25).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 25) adj slope 21d
def f13mv_macd_val_10_25_adj_slope_21_v095_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 25).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (10, 25, 8) slope 5d
def f13mv_macd_sig_10_25_8_slope_5_v096_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 25)
    res = _macd_sig(val, 8).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (10, 25, 8) slope 5d
def f13mv_macd_h_10_25_8_slope_5_v097_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 25)
    sig = _macd_sig(val, 8)
    res = _macd_h(val, sig).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (25, 50) adj slope 21d
def f13mv_macd_val_25_50_adj_slope_21_v098_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 25, 50).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (25, 50) adj slope 63d
def f13mv_macd_val_25_50_adj_slope_63_v099_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 25, 50).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (25, 50, 10) adj slope 21d
def f13mv_macd_sig_25_50_10_adj_slope_21_v100_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 25, 50)
    res = _macd_sig(val, 10).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (25, 50, 10) adj slope 21d
def f13mv_macd_h_25_50_10_adj_slope_21_v101_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 25, 50)
    sig = _macd_sig(val, 10)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 60) adj slope 21d
def f13mv_macd_val_15_60_adj_slope_21_v102_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 60).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (15, 60, 15) adj slope 21d
def f13mv_macd_sig_15_60_15_adj_slope_21_v103_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 15, 60)
    res = _macd_sig(val, 15).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (15, 60, 15) adj slope 21d
def f13mv_macd_h_15_60_15_adj_slope_21_v104_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 15, 60)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (30, 90) adj slope 63d
def f13mv_macd_val_30_90_adj_slope_63_v105_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 30, 90).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (30, 90, 20) adj slope 63d
def f13mv_macd_sig_30_90_20_adj_slope_63_v106_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 30, 90)
    res = _macd_sig(val, 20).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 150) adj slope 63d
def f13mv_macd_val_50_150_adj_slope_63_v107_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 150).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (50, 150, 30) adj slope 63d
def f13mv_macd_sig_50_150_30_adj_slope_63_v108_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 50, 150)
    res = _macd_sig(val, 30).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 50) adj slope 21d
def f13mv_macd_val_10_50_adj_slope_21_v109_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 50).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (10, 50, 10) adj slope 21d
def f13mv_macd_sig_10_50_10_adj_slope_21_v110_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 50)
    res = _macd_sig(val, 10).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 20) slope 5d
def f13mv_macd_val_5_20_slope_5_v111_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 20).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 126d
def f13mv_macd_val_12_26_slope_126_v112_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) slope 126d
def f13mv_macd_sig_12_26_9_slope_126_v113_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    res = _macd_sig(val, 9).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 126d
def f13mv_macd_h_12_26_9_slope_126_v114_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 252d
def f13mv_macd_val_12_26_slope_252_v115_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 252d
def f13mv_macd_h_12_26_9_slope_252_v116_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 13) slope 63d
def f13mv_macd_val_5_13_slope_63_v117_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 5, 13).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (5, 13, 5) slope 63d
def f13mv_macd_h_5_13_5_slope_63_v118_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 5, 13)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (21, 50) slope 252d
def f13mv_macd_val_21_50_slope_252_v119_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (21, 50, 15) slope 252d
def f13mv_macd_h_21_50_15_slope_252_v120_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typ (12, 26) slope 63d
def f13mv_macd_val_typ_12_26_slope_63_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 12, 26).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (12, 26) slope 63d
def f13mv_macd_val_med_12_26_slope_63_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    med_adj = (high * adj + low * adj) / 2
    res = _macd_val(med_adj, 12, 26).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 35) slope 21d
def f13mv_macd_val_15_35_slope_21_v123_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 35).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 30) slope 21d
def f13mv_macd_val_10_30_slope_21_v124_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 30).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 100) slope 126d
def f13mv_macd_val_40_100_slope_126_v125_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 100).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 60) slope 126d
def f13mv_macd_val_20_60_slope_126_v126_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 60).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typ (5, 13) slope 21d
def f13mv_macd_val_typ_5_13_slope_21_v127_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 5, 13).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (5, 13) slope 21d
def f13mv_macd_val_med_5_13_slope_21_v128_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 5, 13).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 20) slope 10d
def f13mv_macd_val_8_20_slope_10_v129_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 20).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 25) slope 10d
def f13mv_macd_val_10_25_slope_10_v130_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 25).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (25, 50) slope 126d
def f13mv_macd_val_25_50_slope_126_v131_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 25, 50).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 60) slope 63d
def f13mv_macd_val_15_60_slope_63_v132_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 60).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (30, 90) slope 126d
def f13mv_macd_val_30_90_slope_126_v133_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 30, 90).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 150) slope 126d
def f13mv_macd_val_50_150_slope_126_v134_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 150).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 50) slope 63d
def f13mv_macd_val_10_50_slope_63_v135_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 50).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 20) slope 10d
def f13mv_macd_val_5_20_slope_10_v136_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 20).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 5d on (H+L+C)/3
def f13mv_macd_val_hlc3_12_26_slope_5_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hlc3 = (high + low + close) / 3
    res = _macd_val(hlc3, 12, 26).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) slope 5d on (H+L+C)/3
def f13mv_macd_sig_hlc3_12_26_9_slope_5_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hlc3 = (high + low + close) / 3
    val = _macd_val(hlc3, 12, 26)
    res = _macd_sig(val, 9).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 5d on (H+L+C)/3
def f13mv_macd_h_hlc3_12_26_9_slope_5_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hlc3 = (high + low + close) / 3
    val = _macd_val(hlc3, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 21d on (H+L+C)/3
def f13mv_macd_val_hlc3_12_26_slope_21_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hlc3 = (high + low + close) / 3
    res = _macd_val(hlc3, 12, 26).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 21d on (H+L+C)/3
def f13mv_macd_h_hlc3_12_26_9_slope_21_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hlc3 = (high + low + close) / 3
    val = _macd_val(hlc3, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 63d on hlc3 adj
def f13mv_macd_val_hlc3_adj_12_26_slope_63_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    hlc3_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(hlc3_adj, 12, 26).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 63d on hlc3 adj
def f13mv_macd_h_hlc3_adj_12_26_9_slope_63_v143_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    hlc3_adj = (high * adj + low * adj + closeadj) / 3
    val = _macd_val(hlc3_adj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 13) slope 21d on typical price

# MACD val (5, 13) slope 21d on median price

# MACD val (21, 50) slope 63d on typical price adj
def f13mv_macd_val_typ_adj_21_50_slope_63_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 21, 50).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (21, 50, 15) slope 63d on typical price adj
def f13mv_macd_h_typ_adj_21_50_15_slope_63_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    val = _macd_val(typ_adj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) slope 126d on median price adj
def f13mv_macd_val_med_adj_12_26_slope_126_v148_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    med_adj = (high * adj + low * adj) / 2
    res = _macd_val(med_adj, 12, 26).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) slope 126d on median price adj
def f13mv_macd_h_med_adj_12_26_9_slope_126_v149_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    med_adj = (high * adj + low * adj) / 2
    val = _macd_val(med_adj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 20) slope 21d

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

SLOPE_NAMES = [f for f in globals() if f.startswith("f13mv_") and f.endswith("_signal")]

F13_MACD_VARIANTS_SLOPE_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(SLOPE_NAMES)
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
    for n, c in F13_MACD_VARIANTS_SLOPE_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("slope 001_150 OK")
