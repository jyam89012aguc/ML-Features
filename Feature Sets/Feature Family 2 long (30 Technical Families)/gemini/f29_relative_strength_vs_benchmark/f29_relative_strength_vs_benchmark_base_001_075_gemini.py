# f29_relative_strength_vs_benchmark_base_001_075_gemini.py
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

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_v001_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """RS Percent Difference over 5 days."""
    res = _rs_pct(close, market_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_10d_v002_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """RS Percent Difference over 10 days."""
    res = _rs_pct(close, market_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_v003_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """RS Percent Difference over 21 days."""
    res = _rs_pct(close, market_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_v004_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """RS Percent Difference over 63 days using adjusted prices."""
    res = _rs_pct(closeadj, market_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_v005_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """RS Percent Difference over 126 days using adjusted prices."""
    res = _rs_pct(closeadj, market_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_v006_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """RS Percent Difference over 252 days using adjusted prices."""
    res = _rs_pct(closeadj, market_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_504d_v007_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """RS Percent Difference over 504 days using adjusted prices."""
    res = _rs_pct(closeadj, market_closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_v008_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Ratio of price to benchmark price."""
    res = _rs_ratio_val(close, market_close)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_5d_v009_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Z-score of the RS ratio over 5 days."""
    res = _rs_zscore_val(close, market_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_10d_v010_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Z-score of the RS ratio over 10 days."""
    res = _rs_zscore_val(close, market_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_21d_v011_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Z-score of the RS ratio over 21 days."""
    res = _rs_zscore_val(close, market_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_v012_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Z-score of the RS ratio over 63 days using adjusted prices."""
    res = _rs_zscore_val(closeadj, market_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_126d_v013_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Z-score of the RS ratio over 126 days using adjusted prices."""
    res = _rs_zscore_val(closeadj, market_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_252d_v014_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Z-score of the RS ratio over 252 days using adjusted prices."""
    res = _rs_zscore_val(closeadj, market_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_504d_v015_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Z-score of the RS ratio over 504 days using adjusted prices."""
    res = _rs_zscore_val(closeadj, market_closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_5d_v016_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """5-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_10d_v017_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """10-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 5), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_21d_v018_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_63d_v019_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_126d_v020_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """126-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 5), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_252d_v021_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 5), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_504d_v022_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """504-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 5), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_5d_v023_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """5-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 21), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_10d_v024_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """10-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 21), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_21d_v025_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_63d_v026_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_126d_v027_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """126-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 21), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_252d_v028_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 21), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_504d_v029_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """504-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 21), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_5d_v030_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """5-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(close, market_close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_10d_v031_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """10-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(close, market_close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_21d_v032_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(close, market_close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_63d_v033_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(closeadj, market_closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_126d_v034_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """126-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(closeadj, market_closeadj), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_252d_v035_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(closeadj, market_closeadj), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_504d_v036_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """504-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(closeadj, market_closeadj), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_max_21d_v037_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day max of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).rolling(21, min_periods=5).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_max_21d_v038_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day max of 21-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 21).rolling(21, min_periods=5).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_max_63d_v039_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day max of 63-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 63).rolling(63, min_periods=21).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_max_63d_v040_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day max of 126-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 126).rolling(63, min_periods=21).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_max_63d_v041_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day max of 252-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 252).rolling(63, min_periods=21).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_max_252d_v042_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day max of the RS ratio."""
    res = _rs_ratio_val(closeadj, market_closeadj).rolling(252, min_periods=63).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_252d_max_21d_v043_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day max of 252-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 252).rolling(21, min_periods=5).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_min_21d_v044_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day min of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).rolling(21, min_periods=5).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_min_21d_v045_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day min of 21-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 21).rolling(21, min_periods=5).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_min_63d_v046_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day min of 63-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 63).rolling(63, min_periods=21).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_min_63d_v047_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day min of 126-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 126).rolling(63, min_periods=21).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_min_63d_v048_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day min of 252-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 252).rolling(63, min_periods=21).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_min_252d_v049_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day min of the RS ratio."""
    res = _rs_ratio_val(closeadj, market_closeadj).rolling(252, min_periods=63).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_252d_min_21d_v050_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day min of 252-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 252).rolling(21, min_periods=5).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_zscore_21d_v051_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day Z-score of 5-day RS Percent Difference."""
    rs = _rs_pct(close, market_close, 5)
    res = (rs - rs.rolling(21, min_periods=5).mean()) / rs.rolling(21, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_zscore_21d_v052_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day Z-score of 21-day RS Percent Difference."""
    rs = _rs_pct(close, market_close, 21)
    res = (rs - rs.rolling(21, min_periods=5).mean()) / rs.rolling(21, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_zscore_63d_v053_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 63-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 63)
    res = (rs - rs.rolling(63, min_periods=21).mean()) / rs.rolling(63, min_periods=21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_zscore_63d_v054_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 126-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 126)
    res = (rs - rs.rolling(63, min_periods=21).mean()) / rs.rolling(63, min_periods=21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_zscore_63d_v055_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 252-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 252)
    res = (rs - rs.rolling(63, min_periods=21).mean()) / rs.rolling(63, min_periods=21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_zscore_21d_v057_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day Z-score of 63-day RS Z-score."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 63)
    res = (rsz - rsz.rolling(21, min_periods=5).mean()) / rsz.rolling(21, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_pos_persistence_21d_v058_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Percentage of days where 5-day RS Percent Difference was positive over the last 21 days."""
    rs = _rs_pct(close, market_close, 5)
    res = (rs > 0).rolling(21, min_periods=5).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_pos_persistence_21d_v059_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Percentage of days where 21-day RS Percent Difference was positive over the last 21 days."""
    rs = _rs_pct(close, market_close, 21)
    res = (rs > 0).rolling(21, min_periods=5).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_pos_persistence_63d_v060_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Percentage of days where 63-day RS Percent Difference was positive over the last 63 days."""
    rs = _rs_pct(closeadj, market_closeadj, 63)
    res = (rs > 0).rolling(63, min_periods=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_pos_persistence_63d_v061_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Percentage of days where 126-day RS Percent Difference was positive over the last 63 days."""
    rs = _rs_pct(closeadj, market_closeadj, 126)
    res = (rs > 0).rolling(63, min_periods=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_pos_persistence_63d_v062_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Percentage of days where 252-day RS Percent Difference was positive over the last 63 days."""
    rs = _rs_pct(closeadj, market_closeadj, 252)
    res = (rs > 0).rolling(63, min_periods=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_pos_persistence_252d_v063_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Percentage of days where the RS ratio was above its 252-day mean."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    res = (ratio > ratio.rolling(252, min_periods=63).mean()).rolling(252, min_periods=63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_pos_persistence_21d_v064_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Percentage of days where 63-day RS Z-score was positive over the last 21 days."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 63)
    res = (rsz > 0).rolling(21, min_periods=5).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_acceleration_5d_v065_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """5-day difference of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_acceleration_10d_v066_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """10-day difference of 21-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 21).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_acceleration_21d_v067_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day difference of 63-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_acceleration_21d_v068_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day difference of 126-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_acceleration_63d_v069_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day difference of 252-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 252).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_acceleration_21d_v070_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day difference of the RS ratio."""
    res = _rs_ratio_val(closeadj, market_closeadj).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_acceleration_10d_v071_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """10-day difference of 63-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 63).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_vs_sma_21d_v072_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """5-day RS Percent Difference relative to its 21-day SMA."""
    rs = _rs_pct(close, market_close, 5)
    res = rs - _sma(rs, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_vs_sma_63d_v073_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day RS Percent Difference relative to its 63-day SMA."""
    rs = _rs_pct(closeadj, market_closeadj, 21)
    res = rs - _sma(rs, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_vs_sma_252d_v074_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """RS ratio relative to its 252-day SMA."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    res = ratio - _sma(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_vs_sma_21d_v075_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day RS Z-score relative to its 21-day SMA."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 63)
    res = rsz - _sma(rsz, 21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "market_close", "market_closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f29rs_") and f.endswith("_signal")]

F29_RELATIVE_STRENGTH_VS_BENCHMARK_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 600; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "market_close": np.random.randn(sz).cumsum()+100, "market_closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F29_RELATIVE_STRENGTH_VS_BENCHMARK_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001_075 OK")
