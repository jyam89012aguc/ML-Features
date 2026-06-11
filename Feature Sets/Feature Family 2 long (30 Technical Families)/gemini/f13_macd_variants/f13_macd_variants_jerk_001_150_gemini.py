# f13_macd_variants_jerk_001_150_gemini.py
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

# MACD val (12, 26) jerk 5-5
def f13mv_macd_val_12_26_jerk_5_5_v001_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) jerk 5-10
def f13mv_macd_val_12_26_jerk_5_10_v002_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) jerk 10-5
def f13mv_macd_val_12_26_jerk_10_5_v003_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) jerk 21-5
def f13mv_macd_val_12_26_jerk_21_5_v004_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) adj jerk 21-21
def f13mv_macd_val_adj_12_26_jerk_21_21_v005_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) jerk 5-5
def f13mv_macd_sig_12_26_9_jerk_5_5_v006_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _macd_sig(val, 9).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) jerk 10-5
def f13mv_macd_sig_12_26_9_jerk_10_5_v007_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _macd_sig(val, 9).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) adj jerk 21-10
def f13mv_macd_sig_adj_12_26_9_jerk_21_10_v008_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    res = _macd_sig(val, 9).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) jerk 5-5
def f13mv_macd_h_12_26_9_jerk_5_5_v009_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) jerk 10-5
def f13mv_macd_h_12_26_9_jerk_10_5_v010_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) adj jerk 21-21
def f13mv_macd_h_adj_12_26_9_jerk_21_21_v011_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Short MACD val (5, 13) jerk 5-5
def f13mv_macd_val_5_13_jerk_5_5_v012_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 13).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Short MACD val (5, 13) jerk 10-5
def f13mv_macd_val_5_13_jerk_10_5_v013_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 13).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Short MACD sig (5, 13, 5) jerk 5-5
def f13mv_macd_sig_5_13_5_jerk_5_5_v014_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    res = _macd_sig(val, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Short MACD h (5, 13, 5) jerk 5-5
def f13mv_macd_h_5_13_5_jerk_5_5_v015_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Long MACD val (21, 50) jerk 21-21
def f13mv_macd_val_21_50_jerk_21_21_v016_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Long MACD val (21, 50) jerk 63-21
def f13mv_macd_val_21_50_jerk_63_21_v017_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Long MACD sig (21, 50, 15) jerk 21-21
def f13mv_macd_sig_21_50_15_jerk_21_21_v018_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    res = _macd_sig(val, 15).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Long MACD h (21, 50, 15) jerk 21-21
def f13mv_macd_h_21_50_15_jerk_21_21_v019_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD typ (12, 26) jerk 5-5
def f13mv_macd_val_typ_12_26_jerk_5_5_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 12, 26).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD typ adj (12, 26) jerk 21-10
def f13mv_macd_val_typ_adj_12_26_jerk_21_10_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 12, 26).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD med (12, 26) jerk 5-5
def f13mv_macd_val_med_12_26_jerk_5_5_v022_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 12, 26).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 20) jerk 5-5
def f13mv_macd_val_10_20_jerk_5_5_v023_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 20).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 40) adj jerk 21-10
def f13mv_macd_val_20_40_adj_jerk_21_10_v024_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 40).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 100) adj jerk 63-21
def f13mv_macd_val_50_100_adj_jerk_63_21_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 100).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (3, 10) jerk 5-5
def f13mv_macd_val_3_10_jerk_5_5_v026_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 3, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val high (12, 26) jerk 5-5
def f13mv_macd_val_high_12_26_jerk_5_5_v027_signal(high: pd.Series) -> pd.Series:
    res = _macd_val(high, 12, 26).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val low (12, 26) jerk 5-5
def f13mv_macd_val_low_12_26_jerk_5_5_v028_signal(low: pd.Series) -> pd.Series:
    res = _macd_val(low, 12, 26).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 17) jerk 5-5
def f13mv_macd_val_8_17_jerk_5_5_v029_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 17).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (24, 52) adj jerk 21-10
def f13mv_macd_val_24_52_adj_jerk_21_10_v030_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 24, 52).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 35) jerk 5-5
def f13mv_macd_val_5_35_jerk_5_5_v031_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 35).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 100) adj jerk 63-21
def f13mv_macd_val_10_100_adj_jerk_63_21_v032_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 100).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (19, 39) adj jerk 21-10
def f13mv_macd_val_19_39_adj_jerk_21_10_v033_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 19, 39).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (13, 26) jerk 5-5
def f13mv_macd_val_13_26_jerk_5_5_v034_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 13, 26).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (2, 5) jerk 5-5
def f13mv_macd_val_2_5_jerk_5_5_v035_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 2, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 80) adj jerk 63-21
def f13mv_macd_val_40_80_adj_jerk_63_21_v036_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 80).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (100, 200) adj jerk 126-63
def f13mv_macd_val_100_200_adj_jerk_126_63_v037_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 100, 200).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 35) jerk 10-5
def f13mv_macd_val_15_35_jerk_10_5_v038_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 15, 35).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 30) jerk 10-5
def f13mv_macd_val_10_30_jerk_10_5_v039_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 30).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 100) adj jerk 63-21
def f13mv_macd_val_40_100_adj_jerk_63_21_v040_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 100).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 60) adj jerk 63-21
def f13mv_macd_val_20_60_adj_jerk_63_21_v041_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 60).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) jerk 63-21
def f13mv_macd_val_12_26_jerk_63_21_v042_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typ (5, 13) jerk 5-5
def f13mv_macd_val_typ_5_13_jerk_5_5_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 5, 13).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (5, 13) jerk 5-5
def f13mv_macd_val_med_5_13_jerk_5_5_v044_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 5, 13).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 20) jerk 5-5
def f13mv_macd_val_8_20_jerk_5_5_v045_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 20).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 25) jerk 5-5
def f13mv_macd_val_10_25_jerk_5_5_v046_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 25).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (25, 50) adj jerk 21-10
def f13mv_macd_val_25_50_adj_jerk_21_10_v047_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 25, 50).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 60) adj jerk 21-10
def f13mv_macd_val_15_60_adj_jerk_21_10_v048_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 60).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (30, 90) adj jerk 63-21
def f13mv_macd_val_30_90_adj_jerk_63_21_v049_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 30, 90).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 150) adj jerk 63-21
def f13mv_macd_val_50_150_adj_jerk_63_21_v050_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 150).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 50) adj jerk 21-10
def f13mv_macd_val_10_50_adj_jerk_21_10_v051_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 50).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 20) jerk 5-5
def f13mv_macd_val_5_20_jerk_5_5_v052_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 20).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) jerk 126-63
def f13mv_macd_val_12_26_jerk_126_63_v053_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) jerk 252-63
def f13mv_macd_val_12_26_jerk_252_63_v054_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(252).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 13) jerk 63-21
def f13mv_macd_val_5_13_jerk_63_21_v055_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 5, 13).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (21, 50) jerk 252-63
def f13mv_macd_val_21_50_jerk_252_63_v056_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(252).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typ (12, 26) jerk 63-21
def f13mv_macd_val_typ_12_26_jerk_63_21_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 12, 26).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (12, 26) jerk 63-21
def f13mv_macd_val_med_12_26_jerk_63_21_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    med_adj = (high * adj + low * adj) / 2
    res = _macd_val(med_adj, 12, 26).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 35) jerk 21-10
def f13mv_macd_val_15_35_jerk_21_10_v059_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 35).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 30) jerk 21-10
def f13mv_macd_val_10_30_jerk_21_10_v060_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 30).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 100) jerk 126-63
def f13mv_macd_val_40_100_jerk_126_63_v061_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 100).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 60) jerk 126-63
def f13mv_macd_val_20_60_jerk_126_63_v062_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 60).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typ (5, 13) jerk 21-10
def f13mv_macd_val_typ_5_13_jerk_21_10_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 5, 13).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (5, 13) jerk 21-10
def f13mv_macd_val_med_5_13_jerk_21_10_v064_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 5, 13).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 20) jerk 10-5
def f13mv_macd_val_8_20_jerk_10_5_v065_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 20).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 25) jerk 10-5
def f13mv_macd_val_10_25_jerk_10_5_v066_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 25).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (25, 50) jerk 126-63
def f13mv_macd_val_25_50_jerk_126_63_v067_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 25, 50).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 60) jerk 63-21
def f13mv_macd_val_15_60_jerk_63_21_v068_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 60).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (30, 90) jerk 126-63
def f13mv_macd_val_30_90_jerk_126_63_v069_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 30, 90).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 150) jerk 126-63
def f13mv_macd_val_50_150_jerk_126_63_v070_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 150).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 50) jerk 63-21
def f13mv_macd_val_10_50_jerk_63_21_v071_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 50).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 20) jerk 10-5
def f13mv_macd_val_5_20_jerk_10_5_v072_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 20).pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val hlc3 (12, 26) jerk 5-5
def f13mv_macd_val_hlc3_12_26_jerk_5_5_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hlc3 = (high + low + close) / 3
    res = _macd_val(hlc3, 12, 26).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med adj (12, 26) jerk 21-10
def f13mv_macd_val_med_adj_12_26_jerk_21_10_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    med_adj = (high * adj + low * adj) / 2
    res = _macd_val(med_adj, 12, 26).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typical adj (12, 26) jerk 21-10

# MACD val (12, 26) jerk 10-10
def f13mv_macd_val_12_26_jerk_10_10_v076_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) jerk 10-10
def f13mv_macd_sig_12_26_9_jerk_10_10_v077_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _macd_sig(val, 9).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) jerk 10-10
def f13mv_macd_h_12_26_9_jerk_10_10_v078_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 13) jerk 10-10
def f13mv_macd_val_5_13_jerk_10_10_v079_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 13).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (21, 50) jerk 63-63
def f13mv_macd_val_21_50_jerk_63_63_v080_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (21, 50, 15) jerk 63-63
def f13mv_macd_sig_21_50_15_jerk_63_63_v081_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    res = _macd_sig(val, 15).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (21, 50, 15) jerk 63-63
def f13mv_macd_h_21_50_15_jerk_63_63_v082_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typ (12, 26) jerk 10-10
def f13mv_macd_val_typ_12_26_jerk_10_10_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 12, 26).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (12, 26) jerk 10-10
def f13mv_macd_val_med_12_26_jerk_10_10_v084_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 12, 26).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 20) jerk 10-10
def f13mv_macd_val_10_20_jerk_10_10_v085_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 20).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 40) adj jerk 21-21
def f13mv_macd_val_20_40_adj_jerk_21_21_v086_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 40).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 100) adj jerk 126-63
def f13mv_macd_val_50_100_adj_jerk_126_63_v087_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 100).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (3, 10) jerk 10-10
def f13mv_macd_val_3_10_jerk_10_10_v088_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 3, 10).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val high (12, 26) jerk 10-10
def f13mv_macd_val_high_12_26_jerk_10_10_v089_signal(high: pd.Series) -> pd.Series:
    res = _macd_val(high, 12, 26).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val low (12, 26) jerk 10-10
def f13mv_macd_val_low_12_26_jerk_10_10_v090_signal(low: pd.Series) -> pd.Series:
    res = _macd_val(low, 12, 26).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 17) jerk 10-10
def f13mv_macd_val_8_17_jerk_10_10_v091_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 17).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (24, 52) adj jerk 63-21
def f13mv_macd_val_24_52_adj_jerk_63_21_v092_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 24, 52).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 35) jerk 10-10
def f13mv_macd_val_5_35_jerk_10_10_v093_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 35).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 100) adj jerk 126-63
def f13mv_macd_val_10_100_adj_jerk_126_63_v094_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 100).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (19, 39) adj jerk 63-21
def f13mv_macd_val_19_39_adj_jerk_63_21_v095_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 19, 39).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (13, 26) jerk 10-10
def f13mv_macd_val_13_26_jerk_10_10_v096_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 13, 26).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (2, 5) jerk 10-10
def f13mv_macd_val_2_5_jerk_10_10_v097_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 2, 5).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 80) adj jerk 126-63
def f13mv_macd_val_40_80_adj_jerk_126_63_v098_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 80).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (100, 200) adj jerk 252-126
def f13mv_macd_val_100_200_adj_jerk_252_126_v099_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 100, 200).pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 35) jerk 21-10

# MACD val (10, 30) jerk 21-10

# MACD val (40, 100) adj jerk 126-63

# MACD val (20, 60) adj jerk 126-63

# MACD val (12, 26) jerk 126-63

# MACD val typ (5, 13) jerk 10-10
def f13mv_macd_val_typ_5_13_jerk_10_10_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 5, 13).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (5, 13) jerk 10-10
def f13mv_macd_val_med_5_13_jerk_10_10_v106_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 5, 13).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 20) jerk 10-10
def f13mv_macd_val_8_20_jerk_10_10_v107_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 20).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 25) jerk 10-10
def f13mv_macd_val_10_25_jerk_10_10_v108_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 25).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (25, 50) adj jerk 63-63
def f13mv_macd_val_25_50_adj_jerk_63_63_v109_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 25, 50).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 60) adj jerk 63-63
def f13mv_macd_val_15_60_adj_jerk_63_63_v110_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 60).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (30, 90) adj jerk 126-126
def f13mv_macd_val_30_90_adj_jerk_126_126_v111_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 30, 90).pct_change(126).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 150) adj jerk 126-126
def f13mv_macd_val_50_150_adj_jerk_126_126_v112_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 150).pct_change(126).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 50) adj jerk 63-63
def f13mv_macd_val_10_50_adj_jerk_63_63_v113_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 50).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 20) jerk 10-10
def f13mv_macd_val_5_20_jerk_10_10_v114_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 20).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val hlc3 (12, 26) jerk 10-10
def f13mv_macd_val_hlc3_12_26_jerk_10_10_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hlc3 = (high + low + close) / 3
    res = _macd_val(hlc3, 12, 26).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med adj (12, 26) jerk 63-63
def f13mv_macd_val_med_adj_12_26_jerk_63_63_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    med_adj = (high * adj + low * adj) / 2
    res = _macd_val(med_adj, 12, 26).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typical adj (12, 26) jerk 63-63
def f13mv_macd_val_typ_adj_12_26_jerk_63_63_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 12, 26).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) jerk 21-10
def f13mv_macd_val_12_26_jerk_21_10_v118_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (12, 26, 9) jerk 21-10
def f13mv_macd_sig_12_26_9_jerk_21_10_v119_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _macd_sig(val, 9).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (12, 26, 9) jerk 21-10
def f13mv_macd_h_12_26_9_jerk_21_10_v120_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 13) jerk 21-10
def f13mv_macd_val_5_13_jerk_21_10_v121_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 13).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (21, 50) jerk 126-63
def f13mv_macd_val_21_50_jerk_126_63_v122_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD sig (21, 50, 15) jerk 126-63
def f13mv_macd_sig_21_50_15_jerk_126_63_v123_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    res = _macd_sig(val, 15).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD h (21, 50, 15) jerk 126-63
def f13mv_macd_h_21_50_15_jerk_126_63_v124_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typ (12, 26) jerk 21-10
def f13mv_macd_val_typ_12_26_jerk_21_10_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typ = (high + low + close) / 3
    res = _macd_val(typ, 12, 26).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (12, 26) jerk 21-10
def f13mv_macd_val_med_12_26_jerk_21_10_v126_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    med = (high + low) / 2
    res = _macd_val(med, 12, 26).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 20) jerk 21-10
def f13mv_macd_val_10_20_jerk_21_10_v127_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 20).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 40) adj jerk 63-21
def f13mv_macd_val_20_40_adj_jerk_63_21_v128_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 40).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (50, 100) adj jerk 252-126
def f13mv_macd_val_50_100_adj_jerk_252_126_v129_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 100).pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (3, 10) jerk 21-10
def f13mv_macd_val_3_10_jerk_21_10_v130_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 3, 10).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val high (12, 26) jerk 21-10
def f13mv_macd_val_high_12_26_jerk_21_10_v131_signal(high: pd.Series) -> pd.Series:
    res = _macd_val(high, 12, 26).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val low (12, 26) jerk 21-10
def f13mv_macd_val_low_12_26_jerk_21_10_v132_signal(low: pd.Series) -> pd.Series:
    res = _macd_val(low, 12, 26).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 17) jerk 21-10
def f13mv_macd_val_8_17_jerk_21_10_v133_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 17).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (24, 52) adj jerk 126-63
def f13mv_macd_val_24_52_adj_jerk_126_63_v134_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 24, 52).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (5, 35) jerk 21-10
def f13mv_macd_val_5_35_jerk_21_10_v135_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 35).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 100) adj jerk 252-126
def f13mv_macd_val_10_100_adj_jerk_252_126_v136_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 100).pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (19, 39) adj jerk 126-63
def f13mv_macd_val_19_39_adj_jerk_126_63_v137_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 19, 39).pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (13, 26) jerk 21-10
def f13mv_macd_val_13_26_jerk_21_10_v138_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 13, 26).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (2, 5) jerk 21-10
def f13mv_macd_val_2_5_jerk_21_10_v139_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 2, 5).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 80) adj jerk 252-126
def f13mv_macd_val_40_80_adj_jerk_252_126_v140_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 80).pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (100, 200) adj jerk 504-252
def f13mv_macd_val_100_200_adj_jerk_504_252_v141_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 100, 200).pct_change(504).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (15, 35) jerk 63-21
def f13mv_macd_val_15_35_jerk_63_21_v142_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 15, 35).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 30) jerk 63-21
def f13mv_macd_val_10_30_jerk_63_21_v143_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 30).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (40, 100) adj jerk 252-126
def f13mv_macd_val_40_100_adj_jerk_252_126_v144_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 100).pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (20, 60) adj jerk 252-126
def f13mv_macd_val_20_60_adj_jerk_252_126_v145_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 60).pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (12, 26) jerk 252-126
def f13mv_macd_val_12_26_jerk_252_126_v146_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26).pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val typ (5, 13) jerk 63-21
def f13mv_macd_val_typ_5_13_jerk_63_21_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    typ_adj = (high * adj + low * adj + closeadj) / 3
    res = _macd_val(typ_adj, 5, 13).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val med (5, 13) jerk 63-21
def f13mv_macd_val_med_5_13_jerk_63_21_v148_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    med_adj = (high * adj + low * adj) / 2
    res = _macd_val(med_adj, 5, 13).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (8, 20) jerk 63-21
def f13mv_macd_val_8_20_jerk_63_21_v149_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 8, 20).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD val (10, 25) jerk 63-21
def f13mv_macd_val_10_25_jerk_63_21_v150_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 25).pct_change(63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

JERK_NAMES = [f for f in globals() if f.startswith("f13mv_") and f.endswith("_signal")]

F13_MACD_VARIANTS_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
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
    for n, c in F13_MACD_VARIANTS_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001_150 OK")
