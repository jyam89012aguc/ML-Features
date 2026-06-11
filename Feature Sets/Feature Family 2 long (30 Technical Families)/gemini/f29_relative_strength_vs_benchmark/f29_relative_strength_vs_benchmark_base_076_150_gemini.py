# f29_relative_strength_vs_benchmark_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
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

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_vol_21d_v076_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day volatility of 5-day RS Percent Difference."""
    res = _std(_rs_pct(close, market_close, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_10d_vol_21d_v077_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day volatility of 10-day RS Percent Difference."""
    res = _std(_rs_pct(close, market_close, 10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_vol_21d_v078_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day volatility of 21-day RS Percent Difference."""
    res = _std(_rs_pct(close, market_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_vol_63d_v079_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day volatility of 63-day RS Percent Difference."""
    res = _std(_rs_pct(closeadj, market_closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_vol_63d_v080_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day volatility of 126-day RS Percent Difference."""
    res = _std(_rs_pct(closeadj, market_closeadj, 126), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_vol_63d_v081_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day volatility of 252-day RS Percent Difference."""
    res = _std(_rs_pct(closeadj, market_closeadj, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_vol_252d_v082_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day volatility of the RS ratio."""
    res = _std(_rs_ratio_val(closeadj, market_closeadj), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sharpe_21d_v083_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Sharpe-like ratio of 5-day RS Percent Difference over 21 days."""
    rs = _rs_pct(close, market_close, 5)
    res = _sma(rs, 21) / _std(rs, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sharpe_21d_v084_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Sharpe-like ratio of 21-day RS Percent Difference over 21 days."""
    rs = _rs_pct(close, market_close, 21)
    res = _sma(rs, 21) / _std(rs, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_sharpe_63d_v085_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Sharpe-like ratio of 63-day RS Percent Difference over 63 days."""
    rs = _rs_pct(closeadj, market_closeadj, 63)
    res = _sma(rs, 63) / _std(rs, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_sharpe_63d_v086_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Sharpe-like ratio of 126-day RS Percent Difference over 63 days."""
    rs = _rs_pct(closeadj, market_closeadj, 126)
    res = _sma(rs, 63) / _std(rs, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_sharpe_63d_v087_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Sharpe-like ratio of 252-day RS Percent Difference over 63 days."""
    rs = _rs_pct(closeadj, market_closeadj, 252)
    res = _sma(rs, 63) / _std(rs, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sharpe_252d_v088_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Sharpe-like ratio of the RS ratio over 252 days."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    res = _sma(ratio, 252) / _std(ratio, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_sharpe_21d_v089_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Sharpe-like ratio of 63-day RS Z-score over 21 days."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 63)
    res = _sma(rsz, 21) / _std(rsz, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_dd_21d_v090_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day drawdown of 5-day RS Percent Difference."""
    rs = _rs_pct(close, market_close, 5)
    res = rs - rs.rolling(21, min_periods=5).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_dd_21d_v091_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day drawdown of 21-day RS Percent Difference."""
    rs = _rs_pct(close, market_close, 21)
    res = rs - rs.rolling(21, min_periods=5).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_dd_63d_v092_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day drawdown of 63-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 63)
    res = rs - rs.rolling(63, min_periods=21).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_dd_63d_v093_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day drawdown of 126-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 126)
    res = rs - rs.rolling(63, min_periods=21).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_dd_63d_v094_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day drawdown of 252-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 252)
    res = rs - rs.rolling(63, min_periods=21).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_dd_252d_v095_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day drawdown of the RS ratio."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    res = ratio - ratio.rolling(252, min_periods=63).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_252d_dd_21d_v096_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day drawdown of 252-day RS Z-score."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 252)
    res = rsz - rsz.rolling(21, min_periods=5).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_channel_pos_21d_v097_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Position of 5-day RS Percent Difference within its 21-day range."""
    rs = _rs_pct(close, market_close, 5)
    mn, mx = rs.rolling(21, min_periods=5).min(), rs.rolling(21, min_periods=5).max()
    res = (rs - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_channel_pos_21d_v098_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Position of 21-day RS Percent Difference within its 21-day range."""
    rs = _rs_pct(close, market_close, 21)
    mn, mx = rs.rolling(21, min_periods=5).min(), rs.rolling(21, min_periods=5).max()
    res = (rs - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_channel_pos_63d_v099_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Position of 63-day RS Percent Difference within its 63-day range."""
    rs = _rs_pct(closeadj, market_closeadj, 63)
    mn, mx = rs.rolling(63, min_periods=21).min(), rs.rolling(63, min_periods=21).max()
    res = (rs - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_channel_pos_63d_v100_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Position of 126-day RS Percent Difference within its 63-day range."""
    rs = _rs_pct(closeadj, market_closeadj, 126)
    mn, mx = rs.rolling(63, min_periods=21).min(), rs.rolling(63, min_periods=21).max()
    res = (rs - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_channel_pos_63d_v101_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Position of 252-day RS Percent Difference within its 63-day range."""
    rs = _rs_pct(closeadj, market_closeadj, 252)
    mn, mx = rs.rolling(63, min_periods=21).min(), rs.rolling(63, min_periods=21).max()
    res = (rs - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_channel_pos_252d_v102_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Position of the RS ratio within its 252-day range."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    mn, mx = ratio.rolling(252, min_periods=63).min(), ratio.rolling(252, min_periods=63).max()
    res = (ratio - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_252d_channel_pos_21d_v103_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Position of 252-day RS Z-score within its 21-day range."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 252)
    mn, mx = rsz.rolling(21, min_periods=5).min(), rsz.rolling(21, min_periods=5).max()
    res = (rsz - mn) / (mx - mn).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_ema_5d_v104_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """5-day EMA of 5-day RS Percent Difference."""
    res = _ema(_rs_pct(close, market_close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_10d_ema_10d_v105_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """10-day EMA of 10-day RS Percent Difference."""
    res = _ema(_rs_pct(close, market_close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_ema_21d_v106_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day EMA of 21-day RS Percent Difference."""
    res = _ema(_rs_pct(close, market_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_ema_21d_v107_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day EMA of 63-day RS Percent Difference."""
    res = _ema(_rs_pct(closeadj, market_closeadj, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_126d_ema_21d_v108_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day EMA of 126-day RS Percent Difference."""
    res = _ema(_rs_pct(closeadj, market_closeadj, 126), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_252d_ema_63d_v109_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day EMA of 252-day RS Percent Difference."""
    res = _ema(_rs_pct(closeadj, market_closeadj, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_ema_252d_v110_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day EMA of the RS ratio."""
    res = _ema(_rs_ratio_val(closeadj, market_closeadj), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_vs_ema_21d_v111_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """5-day RS Percent Difference relative to its 21-day EMA."""
    rs = _rs_pct(close, market_close, 5)
    res = rs - _ema(rs, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_vs_ema_63d_v112_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """21-day RS Percent Difference relative to its 63-day EMA."""
    rs = _rs_pct(closeadj, market_closeadj, 21)
    res = rs - _ema(rs, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_vs_ema_252d_v113_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """RS ratio relative to its 252-day EMA."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    res = ratio - _ema(ratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_vs_ema_21d_v114_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day RS Z-score relative to its 21-day EMA."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 63)
    res = rsz - _ema(rsz, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_skew_63d_v115_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """63-day skewness of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).rolling(63, min_periods=21).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_skew_126d_v116_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """126-day skewness of 21-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 21).rolling(126, min_periods=63).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_skew_252d_v117_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day skewness of the RS ratio."""
    res = _rs_ratio_val(closeadj, market_closeadj).rolling(252, min_periods=63).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_kurt_63d_v118_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """63-day kurtosis of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).rolling(63, min_periods=21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_kurt_126d_v119_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """126-day kurtosis of 21-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 21).rolling(126, min_periods=63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_kurt_252d_v120_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day kurtosis of the RS ratio."""
    res = _rs_ratio_val(closeadj, market_closeadj).rolling(252, min_periods=63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_rolling_rank_63d_v121_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """63-day rolling percentile rank of 5-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5).rolling(63, min_periods=21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_rolling_rank_126d_v122_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """126-day rolling percentile rank of 21-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 21).rolling(126, min_periods=63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_rolling_rank_252d_v123_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of the RS ratio."""
    res = _rs_ratio_val(closeadj, market_closeadj).rolling(252, min_periods=63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_rolling_rank_63d_v124_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day rolling percentile rank of 63-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 63).rolling(63, min_periods=21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_trend_21d_v125_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Trend (21-day slope) of 5-day RS Percent Difference."""
    rs = _rs_pct(close, market_close, 5)
    res = rs.diff(21) / 21
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_trend_63d_v126_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Trend (63-day slope) of 21-day RS Percent Difference."""
    rs = _rs_pct(closeadj, market_closeadj, 21)
    res = rs.diff(63) / 63
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_trend_126d_v127_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Trend (126-day slope) of the RS ratio."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    res = ratio.diff(126) / 126
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sma_5d_diff_21d_v128_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day difference of 5-day SMA of 5-day RS Percent Difference."""
    res = _sma(_rs_pct(close, market_close, 5), 5).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sma_10d_diff_63d_v129_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day difference of 10-day SMA of 21-day RS Percent Difference."""
    res = _sma(_rs_pct(closeadj, market_closeadj, 21), 10).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sma_21d_diff_126d_v130_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """126-day difference of 21-day SMA of the RS ratio."""
    res = _sma(_rs_ratio_val(closeadj, market_closeadj), 21).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_weighted_v131_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """5-day RS Percent Difference weighted by its 21-day persistence."""
    rs = _rs_pct(close, market_close, 5)
    persistence = (rs > 0).rolling(21, min_periods=5).mean()
    res = rs * persistence
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_weighted_v132_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """21-day RS Percent Difference weighted by its 21-day persistence."""
    rs = _rs_pct(close, market_close, 21)
    persistence = (rs > 0).rolling(21, min_periods=5).mean()
    res = rs * persistence
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_weighted_v133_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """RS ratio weighted by its 63-day persistence."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    persistence = (ratio > ratio.rolling(63, min_periods=21).mean()).rolling(63, min_periods=21).mean()
    res = ratio * persistence
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_weighted_v134_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """63-day RS Z-score weighted by its 21-day persistence."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 63)
    persistence = (rsz > 0).rolling(21, min_periods=5).mean()
    res = rsz * persistence
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_minus_21d_v135_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Difference between 5-day and 21-day RS Percent Difference."""
    res = _rs_pct(close, market_close, 5) - _rs_pct(close, market_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_minus_63d_v136_signal(close: pd.Series, market_close: pd.Series, closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Difference between 21-day and 63-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 21) - _rs_pct(closeadj, market_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_minus_252d_v137_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Difference between 63-day and 252-day RS Percent Difference."""
    res = _rs_pct(closeadj, market_closeadj, 63) - _rs_pct(closeadj, market_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_div_sma_252d_v138_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """RS ratio divided by its 252-day SMA."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    res = ratio / _sma(ratio, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_63d_abs_v139_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Absolute value of 63-day RS Z-score."""
    res = _rs_zscore_val(closeadj, market_closeadj, 63).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sq_v140_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Square of 5-day RS Percent Difference (preserving sign)."""
    rs = _rs_pct(close, market_close, 5)
    res = rs.abs() * rs
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sq_v141_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Square of 21-day RS Percent Difference (preserving sign)."""
    rs = _rs_pct(close, market_close, 21)
    res = rs.abs() * rs
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_sq_v142_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Square of 63-day RS Percent Difference (preserving sign)."""
    rs = _rs_pct(closeadj, market_closeadj, 63)
    res = rs.abs() * rs
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sq_v143_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Square of the RS ratio."""
    ratio = _rs_ratio_val(closeadj, market_closeadj)
    res = ratio * ratio
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_252d_sq_v144_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Square of 252-day RS Z-score (preserving sign)."""
    rsz = _rs_zscore_val(closeadj, market_closeadj, 252)
    res = rsz.abs() * rsz
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_sig_v145_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Sign of 5-day RS Percent Difference."""
    res = np.sign(_rs_pct(close, market_close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_21d_sig_v146_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Sign of 21-day RS Percent Difference."""
    res = np.sign(_rs_pct(close, market_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_63d_sig_v147_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Sign of 63-day RS Percent Difference."""
    res = np.sign(_rs_pct(closeadj, market_closeadj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_ratio_sig_v148_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Sign of RS ratio (always 1 if positive prices)."""
    res = np.sign(_rs_ratio_val(closeadj, market_closeadj))
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_252d_sig_v149_signal(closeadj: pd.Series, market_closeadj: pd.Series) -> pd.Series:
    """Sign of 252-day RS Z-score."""
    res = np.sign(_rs_zscore_val(closeadj, market_closeadj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f29rs_f29_relative_strength_vs_benchmark_rs_pct_5d_combined_v150_signal(close: pd.Series, market_close: pd.Series) -> pd.Series:
    """Product of 5-day RS Percent Difference and its 5-day SMA."""
    rs = _rs_pct(close, market_close, 5)
    res = rs * _sma(rs, 5)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "market_close", "market_closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f29rs_") and f.endswith("_signal")]

F29_RELATIVE_STRENGTH_VS_BENCHMARK_BASE_REGISTRY_076_150 = {
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
    for n, c in F29_RELATIVE_STRENGTH_VS_BENCHMARK_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076_150 OK")
