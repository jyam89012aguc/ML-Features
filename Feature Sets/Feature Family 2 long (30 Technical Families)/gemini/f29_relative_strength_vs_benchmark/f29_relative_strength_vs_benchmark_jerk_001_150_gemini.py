# f29_relative_strength_vs_benchmark_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 5)).std()
def _rs_pct(c, market_c, w):
    p_roc = (c - c.shift(w)) / c.shift(w).abs().replace(0, np.nan)
    m_roc = (market_c - market_c.shift(w)) / market_c.shift(w).abs().replace(0, np.nan)
    return p_roc - m_roc
def _rs_ratio_val(c, market_c):
    return c / market_c.abs().replace(0, np.nan)
def _rs_zscore_val(c, market_c, w):
    ratio = c / market_c.abs().replace(0, np.nan)
    return (ratio - ratio.rolling(w).mean()) / ratio.rolling(w).std().replace(0, np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_jerk_v001_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_10d_jerk_v002_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 10-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_jerk_v003_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 21-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_jerk_v004_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 63-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_jerk_v005_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 126-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 126).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_jerk_v006_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 252-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_504d_jerk_v007_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 504-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_jerk_v008_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of the RS ratio."""
    res = _rs_ratio_val(close, market_close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_5d_jerk_v009_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 5-day RS Z-score."""
    res = _rs_zscore_val(close, market_close, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_10d_jerk_v010_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 10-day RS Z-score."""
    res = _rs_zscore_val(close, market_close, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_21d_jerk_v011_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 21-day RS Z-score."""
    res = _rs_zscore_val(close, market_close, 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_jerk_v012_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 63-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_126d_jerk_v013_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 126-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 126).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_252d_jerk_v014_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 252-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_504d_jerk_v015_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 504-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 504).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_5d_jerk_v016_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 5-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 5), 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_21d_jerk_v017_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 21-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 21), 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_sma_63d_jerk_v018_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 63-day SMA of 63-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 63), 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_252d_jerk_v019_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 252-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(closeadj, market_closeadj), 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_vol_21d_jerk_v020_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 21-day volatility of 5-day RS Percent Difference."""
    res = _std(_rs_pct(close, market_close, 5), 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_vol_63d_jerk_v021_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 63-day volatility of 63-day RS Percent Difference."""
    res = _std(_rs_pct(closeadj, market_closeadj, 63), 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_pos_persistence_21d_jerk_v022_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 21-day persistence of 5-day RS Percent Difference."""
    rs = _rs_pct(close, market_close, 5)
    res = (rs > 0).rolling(21, min_periods=5).mean().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_pos_persistence_63d_jerk_v023_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 63-day persistence of 63-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 63)
    res = (rs > 0).rolling(63, min_periods=21).mean().pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_max_21d_jerk_v024_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 21-day max of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).rolling(21, min_periods=5).max().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_max_63d_jerk_v025_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 63-day max of 63-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 63).rolling(63, min_periods=21).max().pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_min_21d_jerk_v026_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 21-day min of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).rolling(21, min_periods=5).min().pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_min_63d_jerk_v027_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 63-day min of 63-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 63).rolling(63, min_periods=21).min().pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_zscore_21d_jerk_v028_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 21-day Z-score of 5-day RS Percent Difference."""
    rs = _rs_pct(close, market_close, 5)
    z = (rs - rs.rolling(21, min_periods=5).mean()) / rs.rolling(21, min_periods=5).std().replace(0, np.nan)
    res = z.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_zscore_63d_jerk_v029_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 63-day Z-score of 63-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 63)
    z = (rs - rs.rolling(63, min_periods=21).mean()) / rs.rolling(63, min_periods=21).std().replace(0, np.nan)
    res = z.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_acceleration_5d_jerk_v030_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Jerk of 5-day acceleration of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).diff(5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_acceleration_21d_jerk_v031_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Jerk of 21-day acceleration of 63-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 63).diff(21).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Expanded functions
def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v032_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v032"""
    res = _rs_pct(closeadj, market_closeadj, 53).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v033_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v033"""
    res = _rs_pct(closeadj, market_closeadj, 54).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v034_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v034"""
    res = _rs_pct(closeadj, market_closeadj, 55).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v035_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v035"""
    res = _rs_pct(closeadj, market_closeadj, 56).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v036_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v036"""
    res = _rs_pct(closeadj, market_closeadj, 57).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v037_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v037"""
    res = _rs_pct(closeadj, market_closeadj, 58).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v038_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v038"""
    res = _rs_pct(closeadj, market_closeadj, 59).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v039_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v039"""
    res = _rs_pct(closeadj, market_closeadj, 60).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v040_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v040"""
    res = _rs_pct(closeadj, market_closeadj, 61).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v041_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v041"""
    res = _rs_pct(closeadj, market_closeadj, 62).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v043_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v043"""
    res = _rs_pct(closeadj, market_closeadj, 64).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v044_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v044"""
    res = _rs_pct(closeadj, market_closeadj, 65).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v045_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v045"""
    res = _rs_pct(closeadj, market_closeadj, 66).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v046_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v046"""
    res = _rs_pct(closeadj, market_closeadj, 67).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v047_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v047"""
    res = _rs_pct(closeadj, market_closeadj, 68).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v048_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v048"""
    res = _rs_pct(closeadj, market_closeadj, 69).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v049_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v049"""
    res = _rs_pct(closeadj, market_closeadj, 70).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v050_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v050"""
    res = _rs_pct(closeadj, market_closeadj, 71).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v051_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v051"""
    res = _rs_pct(closeadj, market_closeadj, 72).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v052_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v052"""
    res = _rs_pct(closeadj, market_closeadj, 73).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v053_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v053"""
    res = _rs_pct(closeadj, market_closeadj, 74).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v054_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v054"""
    res = _rs_pct(closeadj, market_closeadj, 75).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v055_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v055"""
    res = _rs_pct(closeadj, market_closeadj, 76).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v056_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v056"""
    res = _rs_pct(closeadj, market_closeadj, 77).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v057_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v057"""
    res = _rs_pct(closeadj, market_closeadj, 78).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v058_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v058"""
    res = _rs_pct(closeadj, market_closeadj, 79).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v059_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v059"""
    res = _rs_pct(closeadj, market_closeadj, 80).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v060_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v060"""
    res = _rs_pct(closeadj, market_closeadj, 81).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v061_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v061"""
    res = _rs_pct(closeadj, market_closeadj, 82).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v062_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v062"""
    res = _rs_pct(closeadj, market_closeadj, 83).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v063_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v063"""
    res = _rs_pct(closeadj, market_closeadj, 84).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v064_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v064"""
    res = _rs_pct(closeadj, market_closeadj, 85).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v065_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v065"""
    res = _rs_pct(closeadj, market_closeadj, 86).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v066_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v066"""
    res = _rs_pct(closeadj, market_closeadj, 87).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v067_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v067"""
    res = _rs_pct(closeadj, market_closeadj, 88).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v068_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v068"""
    res = _rs_pct(closeadj, market_closeadj, 89).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v069_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v069"""
    res = _rs_pct(closeadj, market_closeadj, 90).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v070_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v070"""
    res = _rs_pct(closeadj, market_closeadj, 91).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v071_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v071"""
    res = _rs_pct(closeadj, market_closeadj, 92).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v072_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v072"""
    res = _rs_pct(closeadj, market_closeadj, 93).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v073_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v073"""
    res = _rs_pct(closeadj, market_closeadj, 94).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v074_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v074"""
    res = _rs_pct(closeadj, market_closeadj, 95).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v075_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v075"""
    res = _rs_pct(closeadj, market_closeadj, 96).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v076_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v076"""
    res = _rs_pct(closeadj, market_closeadj, 97).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v077_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v077"""
    res = _rs_pct(closeadj, market_closeadj, 98).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v078_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v078"""
    res = _rs_pct(closeadj, market_closeadj, 99).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v079_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v079"""
    res = _rs_pct(closeadj, market_closeadj, 100).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v080_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v080"""
    res = _rs_pct(closeadj, market_closeadj, 101).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v081_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v081"""
    res = _rs_pct(closeadj, market_closeadj, 102).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v082_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v082"""
    res = _rs_pct(closeadj, market_closeadj, 103).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v083_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v083"""
    res = _rs_pct(closeadj, market_closeadj, 104).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v084_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v084"""
    res = _rs_pct(closeadj, market_closeadj, 105).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v085_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v085"""
    res = _rs_pct(closeadj, market_closeadj, 106).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v086_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v086"""
    res = _rs_pct(closeadj, market_closeadj, 107).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v087_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v087"""
    res = _rs_pct(closeadj, market_closeadj, 108).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v088_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v088"""
    res = _rs_pct(closeadj, market_closeadj, 109).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v089_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v089"""
    res = _rs_pct(closeadj, market_closeadj, 110).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v090_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v090"""
    res = _rs_pct(closeadj, market_closeadj, 111).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v091_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v091"""
    res = _rs_pct(closeadj, market_closeadj, 112).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v092_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v092"""
    res = _rs_pct(closeadj, market_closeadj, 113).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v093_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v093"""
    res = _rs_pct(closeadj, market_closeadj, 114).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v094_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v094"""
    res = _rs_pct(closeadj, market_closeadj, 115).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v095_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v095"""
    res = _rs_pct(closeadj, market_closeadj, 116).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v096_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v096"""
    res = _rs_pct(closeadj, market_closeadj, 117).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v097_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v097"""
    res = _rs_pct(closeadj, market_closeadj, 118).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v098_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v098"""
    res = _rs_pct(closeadj, market_closeadj, 119).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v099_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v099"""
    res = _rs_pct(closeadj, market_closeadj, 120).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v100_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v100"""
    res = _rs_pct(closeadj, market_closeadj, 121).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v101_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v101"""
    res = _rs_pct(closeadj, market_closeadj, 122).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v102_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v102"""
    res = _rs_pct(closeadj, market_closeadj, 123).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v103_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v103"""
    res = _rs_pct(closeadj, market_closeadj, 124).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v104_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v104"""
    res = _rs_pct(closeadj, market_closeadj, 125).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v106_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v106"""
    res = _rs_pct(closeadj, market_closeadj, 127).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v107_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v107"""
    res = _rs_pct(closeadj, market_closeadj, 128).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v108_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v108"""
    res = _rs_pct(closeadj, market_closeadj, 129).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v109_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v109"""
    res = _rs_pct(closeadj, market_closeadj, 130).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v110_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v110"""
    res = _rs_pct(closeadj, market_closeadj, 131).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v111_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v111"""
    res = _rs_pct(closeadj, market_closeadj, 132).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v112_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v112"""
    res = _rs_pct(closeadj, market_closeadj, 133).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v113_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v113"""
    res = _rs_pct(closeadj, market_closeadj, 134).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v114_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v114"""
    res = _rs_pct(closeadj, market_closeadj, 135).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v115_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v115"""
    res = _rs_pct(closeadj, market_closeadj, 136).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v116_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v116"""
    res = _rs_pct(closeadj, market_closeadj, 137).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v117_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v117"""
    res = _rs_pct(closeadj, market_closeadj, 138).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v118_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v118"""
    res = _rs_pct(closeadj, market_closeadj, 139).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v119_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v119"""
    res = _rs_pct(closeadj, market_closeadj, 140).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v120_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v120"""
    res = _rs_pct(closeadj, market_closeadj, 141).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v121_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v121"""
    res = _rs_pct(closeadj, market_closeadj, 142).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v122_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v122"""
    res = _rs_pct(closeadj, market_closeadj, 143).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v123_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v123"""
    res = _rs_pct(closeadj, market_closeadj, 144).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v124_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v124"""
    res = _rs_pct(closeadj, market_closeadj, 145).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v125_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v125"""
    res = _rs_pct(closeadj, market_closeadj, 146).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v126_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v126"""
    res = _rs_pct(closeadj, market_closeadj, 147).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v127_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v127"""
    res = _rs_pct(closeadj, market_closeadj, 148).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v128_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v128"""
    res = _rs_pct(closeadj, market_closeadj, 149).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v129_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v129"""
    res = _rs_pct(closeadj, market_closeadj, 150).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v130_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v130"""
    res = _rs_pct(closeadj, market_closeadj, 151).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v131_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v131"""
    res = _rs_pct(closeadj, market_closeadj, 152).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v132_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v132"""
    res = _rs_pct(closeadj, market_closeadj, 153).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v133_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v133"""
    res = _rs_pct(closeadj, market_closeadj, 154).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v134_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v134"""
    res = _rs_pct(closeadj, market_closeadj, 155).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v135_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v135"""
    res = _rs_pct(closeadj, market_closeadj, 156).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v136_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v136"""
    res = _rs_pct(closeadj, market_closeadj, 157).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v137_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v137"""
    res = _rs_pct(closeadj, market_closeadj, 158).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v138_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v138"""
    res = _rs_pct(closeadj, market_closeadj, 159).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v139_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v139"""
    res = _rs_pct(closeadj, market_closeadj, 160).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v140_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v140"""
    res = _rs_pct(closeadj, market_closeadj, 161).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v141_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v141"""
    res = _rs_pct(closeadj, market_closeadj, 162).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v142_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v142"""
    res = _rs_pct(closeadj, market_closeadj, 163).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v143_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v143"""
    res = _rs_pct(closeadj, market_closeadj, 164).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v144_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v144"""
    res = _rs_pct(closeadj, market_closeadj, 165).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v145_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v145"""
    res = _rs_pct(closeadj, market_closeadj, 166).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v146_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v146"""
    res = _rs_pct(closeadj, market_closeadj, 167).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v147_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v147"""
    res = _rs_pct(closeadj, market_closeadj, 168).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v148_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v148"""
    res = _rs_pct(closeadj, market_closeadj, 169).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v149_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v149"""
    res = _rs_pct(closeadj, market_closeadj, 170).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_gen_jerk_v150_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Generated jerk feature v150"""
    res = _rs_pct(closeadj, market_closeadj, 171).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "market_close", "market_closeadj"]}

JERK_NAMES = [f for f in globals() if f.startswith("f29rs_") and f.endswith("_signal")]

F29_RELATIVE_STRENGTH_VS_BENCHMARK_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 600; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "market_close": np.random.randn(sz).cumsum()+100, "market_closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F29_RELATIVE_STRENGTH_VS_BENCHMARK_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001_150 OK")
