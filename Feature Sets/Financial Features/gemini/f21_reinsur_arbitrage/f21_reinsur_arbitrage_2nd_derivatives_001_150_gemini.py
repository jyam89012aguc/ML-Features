import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
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

def f21_reinsur_arbitrage_cor_slope_pct_5d_v001_signal(cor):
    """Percentage slope for Raw level of cor over 5d window."""
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_5d_v002_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 5d window."""
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_5d_v003_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_5d_v004_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 5d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_10d_v005_signal(cor):
    """Percentage slope for Raw level of cor over 10d window."""
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_10d_v006_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 10d window."""
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_10d_v007_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_10d_v008_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 10d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_21d_v009_signal(cor):
    """Percentage slope for Raw level of cor over 21d window."""
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_21d_v010_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 21d window."""
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_21d_v011_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_21d_v012_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 21d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_42d_v013_signal(cor):
    """Percentage slope for Raw level of cor over 42d window."""
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_42d_v014_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 42d window."""
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_42d_v015_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_42d_v016_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 42d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_63d_v017_signal(cor):
    """Percentage slope for Raw level of cor over 63d window."""
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_63d_v018_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 63d window."""
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_63d_v019_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_63d_v020_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 63d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_126d_v021_signal(cor):
    """Percentage slope for Raw level of cor over 126d window."""
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_126d_v022_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 126d window."""
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_126d_v023_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_126d_v024_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 126d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_252d_v025_signal(cor):
    """Percentage slope for Raw level of cor over 252d window."""
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_252d_v026_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 252d window."""
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_252d_v027_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_252d_v028_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 252d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_504d_v029_signal(cor):
    """Percentage slope for Raw level of cor over 504d window."""
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_504d_v030_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 504d window."""
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_504d_v031_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_504d_v032_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 504d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_756d_v033_signal(cor):
    """Percentage slope for Raw level of cor over 756d window."""
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_756d_v034_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 756d window."""
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_756d_v035_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_756d_v036_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 756d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_1008d_v037_signal(cor):
    """Percentage slope for Raw level of cor over 1008d window."""
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_1008d_v038_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 1008d window."""
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_1008d_v039_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_1008d_v040_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 1008d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_pct_1260d_v041_signal(cor):
    """Percentage slope for Raw level of cor over 1260d window."""
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_pct_1260d_v042_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 1260d window."""
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_pct_1260d_v043_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_pct_1260d_v044_signal(grossmargin, cor, revenue):
    """Percentage slope for Net underwriting spread over 1260d window."""
    res = _slope_pct(grossmargin - (cor / revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_5d_v045_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 5d window."""
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_5d_v046_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 5d window."""
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_5d_v047_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_5d_v048_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 5d window."""
    res = _jerk(grossmargin - (cor / revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_10d_v049_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 10d window."""
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_10d_v050_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 10d window."""
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_10d_v051_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_10d_v052_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 10d window."""
    res = _jerk(grossmargin - (cor / revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_21d_v053_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 21d window."""
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_21d_v054_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 21d window."""
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_21d_v055_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_21d_v056_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 21d window."""
    res = _jerk(grossmargin - (cor / revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_42d_v057_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 42d window."""
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_42d_v058_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 42d window."""
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_42d_v059_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_42d_v060_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 42d window."""
    res = _jerk(grossmargin - (cor / revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_63d_v061_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 63d window."""
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_63d_v062_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 63d window."""
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_63d_v063_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_63d_v064_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 63d window."""
    res = _jerk(grossmargin - (cor / revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_126d_v065_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 126d window."""
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_126d_v066_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 126d window."""
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_126d_v067_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_126d_v068_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 126d window."""
    res = _jerk(grossmargin - (cor / revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_252d_v069_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 252d window."""
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_252d_v070_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 252d window."""
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_252d_v071_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_252d_v072_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 252d window."""
    res = _jerk(grossmargin - (cor / revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_504d_v073_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 504d window."""
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_504d_v074_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 504d window."""
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_504d_v075_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_504d_v076_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 504d window."""
    res = _jerk(grossmargin - (cor / revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_756d_v077_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 756d window."""
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_756d_v078_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 756d window."""
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_756d_v079_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_756d_v080_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 756d window."""
    res = _jerk(grossmargin - (cor / revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_1008d_v081_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1008d window."""
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_1008d_v082_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 1008d window."""
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_1008d_v083_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_1008d_v084_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 1008d window."""
    res = _jerk(grossmargin - (cor / revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_jerk_1260d_v085_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1260d window."""
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_jerk_1260d_v086_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 1260d window."""
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_jerk_1260d_v087_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_jerk_1260d_v088_signal(grossmargin, cor, revenue):
    """Acceleration/Jerk for Net underwriting spread over 1260d window."""
    res = _jerk(grossmargin - (cor / revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_5d_v089_signal(cor):
    """Normalized slope change for Raw level of cor over 5d window."""
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_5d_v090_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 5d window."""
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_5d_v091_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_5d_v092_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 5d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 5).diff(5) / _sma(grossmargin - (cor / revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_10d_v093_signal(cor):
    """Normalized slope change for Raw level of cor over 10d window."""
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_10d_v094_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 10d window."""
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_10d_v095_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_10d_v096_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 10d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 10).diff(10) / _sma(grossmargin - (cor / revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_21d_v097_signal(cor):
    """Normalized slope change for Raw level of cor over 21d window."""
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_21d_v098_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 21d window."""
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_21d_v099_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_21d_v100_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 21d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 21).diff(21) / _sma(grossmargin - (cor / revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_42d_v101_signal(cor):
    """Normalized slope change for Raw level of cor over 42d window."""
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_42d_v102_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 42d window."""
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_42d_v103_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_42d_v104_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 42d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 42).diff(42) / _sma(grossmargin - (cor / revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_63d_v105_signal(cor):
    """Normalized slope change for Raw level of cor over 63d window."""
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_63d_v106_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 63d window."""
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_63d_v107_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_63d_v108_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 63d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 63).diff(63) / _sma(grossmargin - (cor / revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_126d_v109_signal(cor):
    """Normalized slope change for Raw level of cor over 126d window."""
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_126d_v110_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 126d window."""
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_126d_v111_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_126d_v112_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 126d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 126).diff(126) / _sma(grossmargin - (cor / revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_252d_v113_signal(cor):
    """Normalized slope change for Raw level of cor over 252d window."""
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_252d_v114_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 252d window."""
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_252d_v115_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_252d_v116_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 252d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 252).diff(252) / _sma(grossmargin - (cor / revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_504d_v117_signal(cor):
    """Normalized slope change for Raw level of cor over 504d window."""
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_504d_v118_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 504d window."""
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_504d_v119_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_504d_v120_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 504d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 504).diff(504) / _sma(grossmargin - (cor / revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_756d_v121_signal(cor):
    """Normalized slope change for Raw level of cor over 756d window."""
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_756d_v122_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 756d window."""
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_756d_v123_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_756d_v124_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 756d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 756).diff(756) / _sma(grossmargin - (cor / revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_1008d_v125_signal(cor):
    """Normalized slope change for Raw level of cor over 1008d window."""
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_1008d_v126_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1008d window."""
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_1008d_v127_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_1008d_v128_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 1008d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 1008).diff(1008) / _sma(grossmargin - (cor / revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_slope_diff_norm_1260d_v129_signal(cor):
    """Normalized slope change for Raw level of cor over 1260d window."""
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_slope_diff_norm_1260d_v130_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1260d window."""
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_slope_diff_norm_1260d_v131_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_slope_diff_norm_1260d_v132_signal(grossmargin, cor, revenue):
    """Normalized slope change for Net underwriting spread over 1260d window."""
    res = (_slope_pct(grossmargin - (cor / revenue), 1260).diff(1260) / _sma(grossmargin - (cor / revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_mom_z_5d_v133_signal(cor):
    """Relative momentum strength for Raw level of cor over 5d window."""
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_mom_z_5d_v134_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 5d window."""
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_mom_z_5d_v135_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_mom_z_5d_v136_signal(grossmargin, cor, revenue):
    """Relative momentum strength for Net underwriting spread over 5d window."""
    res = _z(_slope_pct(grossmargin - (cor / revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_mom_z_10d_v137_signal(cor):
    """Relative momentum strength for Raw level of cor over 10d window."""
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_mom_z_10d_v138_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 10d window."""
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_mom_z_10d_v139_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_mom_z_10d_v140_signal(grossmargin, cor, revenue):
    """Relative momentum strength for Net underwriting spread over 10d window."""
    res = _z(_slope_pct(grossmargin - (cor / revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_mom_z_21d_v141_signal(cor):
    """Relative momentum strength for Raw level of cor over 21d window."""
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_mom_z_21d_v142_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 21d window."""
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_mom_z_21d_v143_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_mom_z_21d_v144_signal(grossmargin, cor, revenue):
    """Relative momentum strength for Net underwriting spread over 21d window."""
    res = _z(_slope_pct(grossmargin - (cor / revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_mom_z_42d_v145_signal(cor):
    """Relative momentum strength for Raw level of cor over 42d window."""
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_mom_z_42d_v146_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 42d window."""
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_revenue_mom_z_42d_v147_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_uw_spread_mom_z_42d_v148_signal(grossmargin, cor, revenue):
    """Relative momentum strength for Net underwriting spread over 42d window."""
    res = _z(_slope_pct(grossmargin - (cor / revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_cor_mom_z_63d_v149_signal(cor):
    """Relative momentum strength for Raw level of cor over 63d window."""
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_reinsur_arbitrage_grossmargin_mom_z_63d_v150_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 63d window."""
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f21_reinsur_arbitrage_cor_slope_pct_5d_v001_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_5d_v001_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_5d_v002_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_5d_v002_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_5d_v003_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_5d_v003_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_5d_v004_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_5d_v004_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_10d_v005_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_10d_v005_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_10d_v006_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_10d_v006_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_10d_v007_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_10d_v007_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_10d_v008_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_10d_v008_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_21d_v009_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_21d_v009_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_21d_v010_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_21d_v010_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_21d_v011_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_21d_v011_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_21d_v012_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_21d_v012_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_42d_v013_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_42d_v013_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_42d_v014_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_42d_v014_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_42d_v015_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_42d_v015_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_42d_v016_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_42d_v016_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_63d_v017_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_63d_v017_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_63d_v018_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_63d_v018_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_63d_v019_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_63d_v019_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_63d_v020_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_63d_v020_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_126d_v021_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_126d_v021_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_126d_v022_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_126d_v022_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_126d_v023_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_126d_v023_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_126d_v024_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_126d_v024_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_252d_v025_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_252d_v025_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_252d_v026_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_252d_v026_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_252d_v027_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_252d_v027_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_252d_v028_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_252d_v028_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_504d_v029_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_504d_v029_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_504d_v030_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_504d_v030_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_504d_v031_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_504d_v031_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_504d_v032_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_504d_v032_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_756d_v033_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_756d_v033_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_756d_v034_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_756d_v034_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_756d_v035_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_756d_v035_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_756d_v036_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_756d_v036_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_1008d_v037_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_1008d_v037_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_1008d_v038_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_1008d_v038_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_1008d_v039_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_1008d_v039_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_1008d_v040_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_1008d_v040_signal},
    "f21_reinsur_arbitrage_cor_slope_pct_1260d_v041_signal": {"func": f21_reinsur_arbitrage_cor_slope_pct_1260d_v041_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_pct_1260d_v042_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_pct_1260d_v042_signal},
    "f21_reinsur_arbitrage_revenue_slope_pct_1260d_v043_signal": {"func": f21_reinsur_arbitrage_revenue_slope_pct_1260d_v043_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_pct_1260d_v044_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_pct_1260d_v044_signal},
    "f21_reinsur_arbitrage_cor_jerk_5d_v045_signal": {"func": f21_reinsur_arbitrage_cor_jerk_5d_v045_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_5d_v046_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_5d_v046_signal},
    "f21_reinsur_arbitrage_revenue_jerk_5d_v047_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_5d_v047_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_5d_v048_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_5d_v048_signal},
    "f21_reinsur_arbitrage_cor_jerk_10d_v049_signal": {"func": f21_reinsur_arbitrage_cor_jerk_10d_v049_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_10d_v050_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_10d_v050_signal},
    "f21_reinsur_arbitrage_revenue_jerk_10d_v051_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_10d_v051_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_10d_v052_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_10d_v052_signal},
    "f21_reinsur_arbitrage_cor_jerk_21d_v053_signal": {"func": f21_reinsur_arbitrage_cor_jerk_21d_v053_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_21d_v054_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_21d_v054_signal},
    "f21_reinsur_arbitrage_revenue_jerk_21d_v055_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_21d_v055_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_21d_v056_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_21d_v056_signal},
    "f21_reinsur_arbitrage_cor_jerk_42d_v057_signal": {"func": f21_reinsur_arbitrage_cor_jerk_42d_v057_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_42d_v058_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_42d_v058_signal},
    "f21_reinsur_arbitrage_revenue_jerk_42d_v059_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_42d_v059_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_42d_v060_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_42d_v060_signal},
    "f21_reinsur_arbitrage_cor_jerk_63d_v061_signal": {"func": f21_reinsur_arbitrage_cor_jerk_63d_v061_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_63d_v062_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_63d_v062_signal},
    "f21_reinsur_arbitrage_revenue_jerk_63d_v063_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_63d_v063_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_63d_v064_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_63d_v064_signal},
    "f21_reinsur_arbitrage_cor_jerk_126d_v065_signal": {"func": f21_reinsur_arbitrage_cor_jerk_126d_v065_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_126d_v066_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_126d_v066_signal},
    "f21_reinsur_arbitrage_revenue_jerk_126d_v067_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_126d_v067_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_126d_v068_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_126d_v068_signal},
    "f21_reinsur_arbitrage_cor_jerk_252d_v069_signal": {"func": f21_reinsur_arbitrage_cor_jerk_252d_v069_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_252d_v070_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_252d_v070_signal},
    "f21_reinsur_arbitrage_revenue_jerk_252d_v071_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_252d_v071_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_252d_v072_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_252d_v072_signal},
    "f21_reinsur_arbitrage_cor_jerk_504d_v073_signal": {"func": f21_reinsur_arbitrage_cor_jerk_504d_v073_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_504d_v074_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_504d_v074_signal},
    "f21_reinsur_arbitrage_revenue_jerk_504d_v075_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_504d_v075_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_504d_v076_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_504d_v076_signal},
    "f21_reinsur_arbitrage_cor_jerk_756d_v077_signal": {"func": f21_reinsur_arbitrage_cor_jerk_756d_v077_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_756d_v078_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_756d_v078_signal},
    "f21_reinsur_arbitrage_revenue_jerk_756d_v079_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_756d_v079_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_756d_v080_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_756d_v080_signal},
    "f21_reinsur_arbitrage_cor_jerk_1008d_v081_signal": {"func": f21_reinsur_arbitrage_cor_jerk_1008d_v081_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_1008d_v082_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_1008d_v082_signal},
    "f21_reinsur_arbitrage_revenue_jerk_1008d_v083_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_1008d_v083_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_1008d_v084_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_1008d_v084_signal},
    "f21_reinsur_arbitrage_cor_jerk_1260d_v085_signal": {"func": f21_reinsur_arbitrage_cor_jerk_1260d_v085_signal},
    "f21_reinsur_arbitrage_grossmargin_jerk_1260d_v086_signal": {"func": f21_reinsur_arbitrage_grossmargin_jerk_1260d_v086_signal},
    "f21_reinsur_arbitrage_revenue_jerk_1260d_v087_signal": {"func": f21_reinsur_arbitrage_revenue_jerk_1260d_v087_signal},
    "f21_reinsur_arbitrage_uw_spread_jerk_1260d_v088_signal": {"func": f21_reinsur_arbitrage_uw_spread_jerk_1260d_v088_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_5d_v089_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_5d_v089_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_5d_v090_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_5d_v090_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_5d_v091_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_5d_v091_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_5d_v092_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_5d_v092_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_10d_v093_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_10d_v093_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_10d_v094_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_10d_v094_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_10d_v095_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_10d_v095_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_10d_v096_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_10d_v096_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_21d_v097_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_21d_v097_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_21d_v098_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_21d_v098_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_21d_v099_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_21d_v099_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_21d_v100_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_21d_v100_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_42d_v101_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_42d_v101_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_42d_v102_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_42d_v102_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_42d_v103_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_42d_v103_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_42d_v104_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_42d_v104_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_63d_v105_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_63d_v105_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_63d_v106_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_63d_v106_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_63d_v107_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_63d_v107_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_63d_v108_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_63d_v108_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_126d_v109_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_126d_v109_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_126d_v110_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_126d_v110_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_126d_v111_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_126d_v111_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_126d_v112_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_126d_v112_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_252d_v113_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_252d_v113_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_252d_v114_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_252d_v114_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_252d_v115_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_252d_v115_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_252d_v116_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_252d_v116_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_504d_v117_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_504d_v117_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_504d_v118_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_504d_v118_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_504d_v119_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_504d_v119_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_504d_v120_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_504d_v120_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_756d_v121_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_756d_v121_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_756d_v122_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_756d_v122_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_756d_v123_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_756d_v123_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_756d_v124_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_756d_v124_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_1008d_v125_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_1008d_v125_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_1008d_v126_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_1008d_v126_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_1008d_v127_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_1008d_v127_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_1008d_v128_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_1008d_v128_signal},
    "f21_reinsur_arbitrage_cor_slope_diff_norm_1260d_v129_signal": {"func": f21_reinsur_arbitrage_cor_slope_diff_norm_1260d_v129_signal},
    "f21_reinsur_arbitrage_grossmargin_slope_diff_norm_1260d_v130_signal": {"func": f21_reinsur_arbitrage_grossmargin_slope_diff_norm_1260d_v130_signal},
    "f21_reinsur_arbitrage_revenue_slope_diff_norm_1260d_v131_signal": {"func": f21_reinsur_arbitrage_revenue_slope_diff_norm_1260d_v131_signal},
    "f21_reinsur_arbitrage_uw_spread_slope_diff_norm_1260d_v132_signal": {"func": f21_reinsur_arbitrage_uw_spread_slope_diff_norm_1260d_v132_signal},
    "f21_reinsur_arbitrage_cor_mom_z_5d_v133_signal": {"func": f21_reinsur_arbitrage_cor_mom_z_5d_v133_signal},
    "f21_reinsur_arbitrage_grossmargin_mom_z_5d_v134_signal": {"func": f21_reinsur_arbitrage_grossmargin_mom_z_5d_v134_signal},
    "f21_reinsur_arbitrage_revenue_mom_z_5d_v135_signal": {"func": f21_reinsur_arbitrage_revenue_mom_z_5d_v135_signal},
    "f21_reinsur_arbitrage_uw_spread_mom_z_5d_v136_signal": {"func": f21_reinsur_arbitrage_uw_spread_mom_z_5d_v136_signal},
    "f21_reinsur_arbitrage_cor_mom_z_10d_v137_signal": {"func": f21_reinsur_arbitrage_cor_mom_z_10d_v137_signal},
    "f21_reinsur_arbitrage_grossmargin_mom_z_10d_v138_signal": {"func": f21_reinsur_arbitrage_grossmargin_mom_z_10d_v138_signal},
    "f21_reinsur_arbitrage_revenue_mom_z_10d_v139_signal": {"func": f21_reinsur_arbitrage_revenue_mom_z_10d_v139_signal},
    "f21_reinsur_arbitrage_uw_spread_mom_z_10d_v140_signal": {"func": f21_reinsur_arbitrage_uw_spread_mom_z_10d_v140_signal},
    "f21_reinsur_arbitrage_cor_mom_z_21d_v141_signal": {"func": f21_reinsur_arbitrage_cor_mom_z_21d_v141_signal},
    "f21_reinsur_arbitrage_grossmargin_mom_z_21d_v142_signal": {"func": f21_reinsur_arbitrage_grossmargin_mom_z_21d_v142_signal},
    "f21_reinsur_arbitrage_revenue_mom_z_21d_v143_signal": {"func": f21_reinsur_arbitrage_revenue_mom_z_21d_v143_signal},
    "f21_reinsur_arbitrage_uw_spread_mom_z_21d_v144_signal": {"func": f21_reinsur_arbitrage_uw_spread_mom_z_21d_v144_signal},
    "f21_reinsur_arbitrage_cor_mom_z_42d_v145_signal": {"func": f21_reinsur_arbitrage_cor_mom_z_42d_v145_signal},
    "f21_reinsur_arbitrage_grossmargin_mom_z_42d_v146_signal": {"func": f21_reinsur_arbitrage_grossmargin_mom_z_42d_v146_signal},
    "f21_reinsur_arbitrage_revenue_mom_z_42d_v147_signal": {"func": f21_reinsur_arbitrage_revenue_mom_z_42d_v147_signal},
    "f21_reinsur_arbitrage_uw_spread_mom_z_42d_v148_signal": {"func": f21_reinsur_arbitrage_uw_spread_mom_z_42d_v148_signal},
    "f21_reinsur_arbitrage_cor_mom_z_63d_v149_signal": {"func": f21_reinsur_arbitrage_cor_mom_z_63d_v149_signal},
    "f21_reinsur_arbitrage_grossmargin_mom_z_63d_v150_signal": {"func": f21_reinsur_arbitrage_grossmargin_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 21...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
