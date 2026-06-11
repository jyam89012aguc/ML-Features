import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return _slope_pct(s, w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()

def f30_market_sentiment_beta_revenue_slope_pct_5d_v001_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_5d_v002_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 5d window."""
    res = _slope_pct(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_5d_v003_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 5d window."""
    res = _slope_pct(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_5d_v004_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 5d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_10d_v005_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_10d_v006_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 10d window."""
    res = _slope_pct(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_10d_v007_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 10d window."""
    res = _slope_pct(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_10d_v008_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 10d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_21d_v009_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_21d_v010_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 21d window."""
    res = _slope_pct(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_21d_v011_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 21d window."""
    res = _slope_pct(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_21d_v012_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 21d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_42d_v013_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_42d_v014_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 42d window."""
    res = _slope_pct(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_42d_v015_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 42d window."""
    res = _slope_pct(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_42d_v016_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 42d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_63d_v017_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_63d_v018_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 63d window."""
    res = _slope_pct(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_63d_v019_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 63d window."""
    res = _slope_pct(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_63d_v020_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 63d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_126d_v021_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_126d_v022_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 126d window."""
    res = _slope_pct(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_126d_v023_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 126d window."""
    res = _slope_pct(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_126d_v024_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 126d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_252d_v025_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_252d_v026_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 252d window."""
    res = _slope_pct(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_252d_v027_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 252d window."""
    res = _slope_pct(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_252d_v028_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 252d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_504d_v029_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_504d_v030_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 504d window."""
    res = _slope_pct(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_504d_v031_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 504d window."""
    res = _slope_pct(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_504d_v032_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 504d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_756d_v033_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_756d_v034_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 756d window."""
    res = _slope_pct(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_756d_v035_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 756d window."""
    res = _slope_pct(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_756d_v036_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 756d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_1008d_v037_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_1008d_v038_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 1008d window."""
    res = _slope_pct(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_1008d_v039_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 1008d window."""
    res = _slope_pct(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_1008d_v040_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 1008d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_pct_1260d_v041_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_pct_1260d_v042_signal(marketcap):
    """Percentage slope for momentum for Raw level of marketcap over 1260d window."""
    res = _slope_pct(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_pct_1260d_v043_signal(closeadj):
    """Percentage slope for momentum for Raw level of closeadj over 1260d window."""
    res = _slope_pct(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_pct_1260d_v044_signal(closeadj):
    """Percentage slope for momentum for Price relative to long-term trend over 1260d window."""
    res = _slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_5d_v045_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_5d_v046_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 5d window."""
    res = _jerk(marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_5d_v047_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 5d window."""
    res = _jerk(closeadj, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_5d_v048_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 5d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_10d_v049_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_10d_v050_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 10d window."""
    res = _jerk(marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_10d_v051_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 10d window."""
    res = _jerk(closeadj, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_10d_v052_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 10d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_21d_v053_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_21d_v054_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 21d window."""
    res = _jerk(marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_21d_v055_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 21d window."""
    res = _jerk(closeadj, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_21d_v056_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 21d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_42d_v057_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_42d_v058_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 42d window."""
    res = _jerk(marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_42d_v059_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 42d window."""
    res = _jerk(closeadj, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_42d_v060_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 42d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_63d_v061_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_63d_v062_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 63d window."""
    res = _jerk(marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_63d_v063_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 63d window."""
    res = _jerk(closeadj, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_63d_v064_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 63d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_126d_v065_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_126d_v066_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 126d window."""
    res = _jerk(marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_126d_v067_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 126d window."""
    res = _jerk(closeadj, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_126d_v068_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 126d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_252d_v069_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_252d_v070_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 252d window."""
    res = _jerk(marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_252d_v071_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 252d window."""
    res = _jerk(closeadj, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_252d_v072_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 252d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_504d_v073_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_504d_v074_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 504d window."""
    res = _jerk(marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_504d_v075_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 504d window."""
    res = _jerk(closeadj, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_504d_v076_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 504d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_756d_v077_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_756d_v078_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 756d window."""
    res = _jerk(marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_756d_v079_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 756d window."""
    res = _jerk(closeadj, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_756d_v080_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 756d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_1008d_v081_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_1008d_v082_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 1008d window."""
    res = _jerk(marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_1008d_v083_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 1008d window."""
    res = _jerk(closeadj, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_1008d_v084_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 1008d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_jerk_1260d_v085_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_jerk_1260d_v086_signal(marketcap):
    """Acceleration/Jerk for structural shifts for Raw level of marketcap over 1260d window."""
    res = _jerk(marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_jerk_1260d_v087_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Raw level of closeadj over 1260d window."""
    res = _jerk(closeadj, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_jerk_1260d_v088_signal(closeadj):
    """Acceleration/Jerk for structural shifts for Price relative to long-term trend over 1260d window."""
    res = _jerk(_ratio(closeadj, _sma(closeadj, 252)), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_5d_v089_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_5d_v090_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 5d window."""
    res = (_slope_pct(marketcap, 5).diff(5) / _sma(marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_5d_v091_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 5d window."""
    res = (_slope_pct(closeadj, 5).diff(5) / _sma(closeadj.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_5d_v092_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 5d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 5).diff(5) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_10d_v093_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_10d_v094_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 10d window."""
    res = (_slope_pct(marketcap, 10).diff(10) / _sma(marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_10d_v095_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 10d window."""
    res = (_slope_pct(closeadj, 10).diff(10) / _sma(closeadj.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_10d_v096_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 10d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 10).diff(10) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_21d_v097_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_21d_v098_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 21d window."""
    res = (_slope_pct(marketcap, 21).diff(21) / _sma(marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_21d_v099_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 21d window."""
    res = (_slope_pct(closeadj, 21).diff(21) / _sma(closeadj.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_21d_v100_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 21d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 21).diff(21) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_42d_v101_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_42d_v102_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 42d window."""
    res = (_slope_pct(marketcap, 42).diff(42) / _sma(marketcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_42d_v103_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 42d window."""
    res = (_slope_pct(closeadj, 42).diff(42) / _sma(closeadj.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_42d_v104_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 42d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 42).diff(42) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_63d_v105_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_63d_v106_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 63d window."""
    res = (_slope_pct(marketcap, 63).diff(63) / _sma(marketcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_63d_v107_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 63d window."""
    res = (_slope_pct(closeadj, 63).diff(63) / _sma(closeadj.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_63d_v108_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 63d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 63).diff(63) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_126d_v109_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_126d_v110_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 126d window."""
    res = (_slope_pct(marketcap, 126).diff(126) / _sma(marketcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_126d_v111_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 126d window."""
    res = (_slope_pct(closeadj, 126).diff(126) / _sma(closeadj.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_126d_v112_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 126d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 126).diff(126) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_252d_v113_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_252d_v114_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 252d window."""
    res = (_slope_pct(marketcap, 252).diff(252) / _sma(marketcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_252d_v115_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 252d window."""
    res = (_slope_pct(closeadj, 252).diff(252) / _sma(closeadj.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_252d_v116_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 252d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 252).diff(252) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_504d_v117_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_504d_v118_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 504d window."""
    res = (_slope_pct(marketcap, 504).diff(504) / _sma(marketcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_504d_v119_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 504d window."""
    res = (_slope_pct(closeadj, 504).diff(504) / _sma(closeadj.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_504d_v120_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 504d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 504).diff(504) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_756d_v121_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_756d_v122_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 756d window."""
    res = (_slope_pct(marketcap, 756).diff(756) / _sma(marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_756d_v123_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 756d window."""
    res = (_slope_pct(closeadj, 756).diff(756) / _sma(closeadj.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_756d_v124_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 756d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 756).diff(756) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_1008d_v125_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_1008d_v126_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1008d window."""
    res = (_slope_pct(marketcap, 1008).diff(1008) / _sma(marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_1008d_v127_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 1008d window."""
    res = (_slope_pct(closeadj, 1008).diff(1008) / _sma(closeadj.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_1008d_v128_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 1008d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 1008).diff(1008) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_slope_diff_norm_1260d_v129_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_slope_diff_norm_1260d_v130_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1260d window."""
    res = (_slope_pct(marketcap, 1260).diff(1260) / _sma(marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_slope_diff_norm_1260d_v131_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 1260d window."""
    res = (_slope_pct(closeadj, 1260).diff(1260) / _sma(closeadj.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_1260d_v132_signal(closeadj):
    """Normalized slope change for Price relative to long-term trend over 1260d window."""
    res = (_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 1260).diff(1260) / _sma(_ratio(closeadj, _sma(closeadj, 252)).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_mom_z_5d_v133_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_mom_z_5d_v134_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 5d window."""
    res = _z(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_mom_z_5d_v135_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 5d window."""
    res = _z(_slope_pct(closeadj, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_mom_z_5d_v136_signal(closeadj):
    """Relative momentum strength for Price relative to long-term trend over 5d window."""
    res = _z(_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_mom_z_10d_v137_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_mom_z_10d_v138_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 10d window."""
    res = _z(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_mom_z_10d_v139_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 10d window."""
    res = _z(_slope_pct(closeadj, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_mom_z_10d_v140_signal(closeadj):
    """Relative momentum strength for Price relative to long-term trend over 10d window."""
    res = _z(_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_mom_z_21d_v141_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_mom_z_21d_v142_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 21d window."""
    res = _z(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_mom_z_21d_v143_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 21d window."""
    res = _z(_slope_pct(closeadj, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_mom_z_21d_v144_signal(closeadj):
    """Relative momentum strength for Price relative to long-term trend over 21d window."""
    res = _z(_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_mom_z_42d_v145_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_mom_z_42d_v146_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 42d window."""
    res = _z(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_closeadj_mom_z_42d_v147_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 42d window."""
    res = _z(_slope_pct(closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_sentiment_momentum_mom_z_42d_v148_signal(closeadj):
    """Relative momentum strength for Price relative to long-term trend over 42d window."""
    res = _z(_slope_pct(_ratio(closeadj, _sma(closeadj, 252)), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_revenue_mom_z_63d_v149_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_market_sentiment_beta_marketcap_mom_z_63d_v150_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 63d window."""
    res = _z(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f30_market_sentiment_beta_revenue_slope_pct_5d_v001_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_5d_v001_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_5d_v002_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_5d_v002_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_5d_v003_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_5d_v003_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_5d_v004_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_5d_v004_signal},    "f30_market_sentiment_beta_revenue_slope_pct_10d_v005_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_10d_v005_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_10d_v006_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_10d_v006_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_10d_v007_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_10d_v007_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_10d_v008_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_10d_v008_signal},    "f30_market_sentiment_beta_revenue_slope_pct_21d_v009_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_21d_v009_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_21d_v010_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_21d_v010_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_21d_v011_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_21d_v011_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_21d_v012_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_21d_v012_signal},    "f30_market_sentiment_beta_revenue_slope_pct_42d_v013_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_42d_v013_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_42d_v014_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_42d_v014_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_42d_v015_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_42d_v015_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_42d_v016_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_42d_v016_signal},    "f30_market_sentiment_beta_revenue_slope_pct_63d_v017_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_63d_v017_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_63d_v018_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_63d_v018_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_63d_v019_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_63d_v019_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_63d_v020_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_63d_v020_signal},    "f30_market_sentiment_beta_revenue_slope_pct_126d_v021_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_126d_v021_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_126d_v022_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_126d_v022_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_126d_v023_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_126d_v023_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_126d_v024_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_126d_v024_signal},    "f30_market_sentiment_beta_revenue_slope_pct_252d_v025_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_252d_v025_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_252d_v026_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_252d_v026_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_252d_v027_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_252d_v027_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_252d_v028_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_252d_v028_signal},    "f30_market_sentiment_beta_revenue_slope_pct_504d_v029_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_504d_v029_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_504d_v030_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_504d_v030_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_504d_v031_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_504d_v031_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_504d_v032_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_504d_v032_signal},    "f30_market_sentiment_beta_revenue_slope_pct_756d_v033_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_756d_v033_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_756d_v034_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_756d_v034_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_756d_v035_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_756d_v035_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_756d_v036_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_756d_v036_signal},    "f30_market_sentiment_beta_revenue_slope_pct_1008d_v037_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_1008d_v037_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_1008d_v038_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_1008d_v038_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_1008d_v039_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_1008d_v039_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_1008d_v040_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_1008d_v040_signal},    "f30_market_sentiment_beta_revenue_slope_pct_1260d_v041_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_pct_1260d_v041_signal},    "f30_market_sentiment_beta_marketcap_slope_pct_1260d_v042_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_pct_1260d_v042_signal},    "f30_market_sentiment_beta_closeadj_slope_pct_1260d_v043_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_pct_1260d_v043_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_pct_1260d_v044_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_pct_1260d_v044_signal},    "f30_market_sentiment_beta_revenue_jerk_5d_v045_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_5d_v045_signal},    "f30_market_sentiment_beta_marketcap_jerk_5d_v046_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_5d_v046_signal},    "f30_market_sentiment_beta_closeadj_jerk_5d_v047_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_5d_v047_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_5d_v048_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_5d_v048_signal},    "f30_market_sentiment_beta_revenue_jerk_10d_v049_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_10d_v049_signal},    "f30_market_sentiment_beta_marketcap_jerk_10d_v050_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_10d_v050_signal},    "f30_market_sentiment_beta_closeadj_jerk_10d_v051_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_10d_v051_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_10d_v052_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_10d_v052_signal},    "f30_market_sentiment_beta_revenue_jerk_21d_v053_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_21d_v053_signal},    "f30_market_sentiment_beta_marketcap_jerk_21d_v054_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_21d_v054_signal},    "f30_market_sentiment_beta_closeadj_jerk_21d_v055_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_21d_v055_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_21d_v056_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_21d_v056_signal},    "f30_market_sentiment_beta_revenue_jerk_42d_v057_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_42d_v057_signal},    "f30_market_sentiment_beta_marketcap_jerk_42d_v058_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_42d_v058_signal},    "f30_market_sentiment_beta_closeadj_jerk_42d_v059_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_42d_v059_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_42d_v060_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_42d_v060_signal},    "f30_market_sentiment_beta_revenue_jerk_63d_v061_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_63d_v061_signal},    "f30_market_sentiment_beta_marketcap_jerk_63d_v062_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_63d_v062_signal},    "f30_market_sentiment_beta_closeadj_jerk_63d_v063_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_63d_v063_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_63d_v064_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_63d_v064_signal},    "f30_market_sentiment_beta_revenue_jerk_126d_v065_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_126d_v065_signal},    "f30_market_sentiment_beta_marketcap_jerk_126d_v066_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_126d_v066_signal},    "f30_market_sentiment_beta_closeadj_jerk_126d_v067_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_126d_v067_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_126d_v068_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_126d_v068_signal},    "f30_market_sentiment_beta_revenue_jerk_252d_v069_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_252d_v069_signal},    "f30_market_sentiment_beta_marketcap_jerk_252d_v070_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_252d_v070_signal},    "f30_market_sentiment_beta_closeadj_jerk_252d_v071_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_252d_v071_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_252d_v072_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_252d_v072_signal},    "f30_market_sentiment_beta_revenue_jerk_504d_v073_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_504d_v073_signal},    "f30_market_sentiment_beta_marketcap_jerk_504d_v074_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_504d_v074_signal},    "f30_market_sentiment_beta_closeadj_jerk_504d_v075_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_504d_v075_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_504d_v076_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_504d_v076_signal},    "f30_market_sentiment_beta_revenue_jerk_756d_v077_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_756d_v077_signal},    "f30_market_sentiment_beta_marketcap_jerk_756d_v078_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_756d_v078_signal},    "f30_market_sentiment_beta_closeadj_jerk_756d_v079_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_756d_v079_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_756d_v080_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_756d_v080_signal},    "f30_market_sentiment_beta_revenue_jerk_1008d_v081_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_1008d_v081_signal},    "f30_market_sentiment_beta_marketcap_jerk_1008d_v082_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_1008d_v082_signal},    "f30_market_sentiment_beta_closeadj_jerk_1008d_v083_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_1008d_v083_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_1008d_v084_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_1008d_v084_signal},    "f30_market_sentiment_beta_revenue_jerk_1260d_v085_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_jerk_1260d_v085_signal},    "f30_market_sentiment_beta_marketcap_jerk_1260d_v086_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_jerk_1260d_v086_signal},    "f30_market_sentiment_beta_closeadj_jerk_1260d_v087_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_jerk_1260d_v087_signal},    "f30_market_sentiment_beta_sentiment_momentum_jerk_1260d_v088_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_jerk_1260d_v088_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_5d_v089_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_5d_v090_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_5d_v091_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_5d_v092_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_10d_v093_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_10d_v094_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_10d_v095_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_10d_v096_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_21d_v097_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_21d_v098_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_21d_v099_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_21d_v100_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_42d_v101_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_42d_v102_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_42d_v103_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_42d_v104_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_63d_v105_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_63d_v106_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_63d_v107_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_63d_v108_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_126d_v109_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_126d_v110_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_126d_v111_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_126d_v112_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_252d_v113_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_252d_v114_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_252d_v115_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_252d_v116_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_504d_v117_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_504d_v118_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_504d_v119_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_504d_v120_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_756d_v121_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_756d_v122_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_756d_v123_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_756d_v124_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_1008d_v125_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_1008d_v126_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_1008d_v127_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_1008d_v128_signal},    "f30_market_sentiment_beta_revenue_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_slope_diff_norm_1260d_v129_signal},    "f30_market_sentiment_beta_marketcap_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_slope_diff_norm_1260d_v130_signal},    "f30_market_sentiment_beta_closeadj_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_slope_diff_norm_1260d_v131_signal},    "f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_slope_diff_norm_1260d_v132_signal},    "f30_market_sentiment_beta_revenue_mom_z_5d_v133_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_mom_z_5d_v133_signal},    "f30_market_sentiment_beta_marketcap_mom_z_5d_v134_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_mom_z_5d_v134_signal},    "f30_market_sentiment_beta_closeadj_mom_z_5d_v135_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_mom_z_5d_v135_signal},    "f30_market_sentiment_beta_sentiment_momentum_mom_z_5d_v136_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_mom_z_5d_v136_signal},    "f30_market_sentiment_beta_revenue_mom_z_10d_v137_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_mom_z_10d_v137_signal},    "f30_market_sentiment_beta_marketcap_mom_z_10d_v138_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_mom_z_10d_v138_signal},    "f30_market_sentiment_beta_closeadj_mom_z_10d_v139_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_mom_z_10d_v139_signal},    "f30_market_sentiment_beta_sentiment_momentum_mom_z_10d_v140_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_mom_z_10d_v140_signal},    "f30_market_sentiment_beta_revenue_mom_z_21d_v141_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_mom_z_21d_v141_signal},    "f30_market_sentiment_beta_marketcap_mom_z_21d_v142_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_mom_z_21d_v142_signal},    "f30_market_sentiment_beta_closeadj_mom_z_21d_v143_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_mom_z_21d_v143_signal},    "f30_market_sentiment_beta_sentiment_momentum_mom_z_21d_v144_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_mom_z_21d_v144_signal},    "f30_market_sentiment_beta_revenue_mom_z_42d_v145_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_mom_z_42d_v145_signal},    "f30_market_sentiment_beta_marketcap_mom_z_42d_v146_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_mom_z_42d_v146_signal},    "f30_market_sentiment_beta_closeadj_mom_z_42d_v147_signal": {"inputs": [], "func": f30_market_sentiment_beta_closeadj_mom_z_42d_v147_signal},    "f30_market_sentiment_beta_sentiment_momentum_mom_z_42d_v148_signal": {"inputs": [], "func": f30_market_sentiment_beta_sentiment_momentum_mom_z_42d_v148_signal},    "f30_market_sentiment_beta_revenue_mom_z_63d_v149_signal": {"inputs": [], "func": f30_market_sentiment_beta_revenue_mom_z_63d_v149_signal},    "f30_market_sentiment_beta_marketcap_mom_z_63d_v150_signal": {"inputs": [], "func": f30_market_sentiment_beta_marketcap_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 30...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
