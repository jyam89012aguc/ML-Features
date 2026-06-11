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

def f28_synergy_potential_ebitda_slope_pct_5d_v001_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 5d window."""
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_5d_v002_signal(sgna):
    """Percentage slope for Raw level of sgna over 5d window."""
    res = _slope_pct(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_5d_v003_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 5d window."""
    res = _slope_pct(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_5d_v004_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 5d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_10d_v005_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 10d window."""
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_10d_v006_signal(sgna):
    """Percentage slope for Raw level of sgna over 10d window."""
    res = _slope_pct(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_10d_v007_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 10d window."""
    res = _slope_pct(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_10d_v008_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 10d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_21d_v009_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 21d window."""
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_21d_v010_signal(sgna):
    """Percentage slope for Raw level of sgna over 21d window."""
    res = _slope_pct(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_21d_v011_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 21d window."""
    res = _slope_pct(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_21d_v012_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 21d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_42d_v013_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 42d window."""
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_42d_v014_signal(sgna):
    """Percentage slope for Raw level of sgna over 42d window."""
    res = _slope_pct(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_42d_v015_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 42d window."""
    res = _slope_pct(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_42d_v016_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 42d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_63d_v017_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 63d window."""
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_63d_v018_signal(sgna):
    """Percentage slope for Raw level of sgna over 63d window."""
    res = _slope_pct(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_63d_v019_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 63d window."""
    res = _slope_pct(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_63d_v020_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 63d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_126d_v021_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 126d window."""
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_126d_v022_signal(sgna):
    """Percentage slope for Raw level of sgna over 126d window."""
    res = _slope_pct(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_126d_v023_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 126d window."""
    res = _slope_pct(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_126d_v024_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 126d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_252d_v025_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 252d window."""
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_252d_v026_signal(sgna):
    """Percentage slope for Raw level of sgna over 252d window."""
    res = _slope_pct(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_252d_v027_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 252d window."""
    res = _slope_pct(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_252d_v028_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 252d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_504d_v029_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 504d window."""
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_504d_v030_signal(sgna):
    """Percentage slope for Raw level of sgna over 504d window."""
    res = _slope_pct(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_504d_v031_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 504d window."""
    res = _slope_pct(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_504d_v032_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 504d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_756d_v033_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 756d window."""
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_756d_v034_signal(sgna):
    """Percentage slope for Raw level of sgna over 756d window."""
    res = _slope_pct(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_756d_v035_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 756d window."""
    res = _slope_pct(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_756d_v036_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 756d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_1008d_v037_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1008d window."""
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_1008d_v038_signal(sgna):
    """Percentage slope for Raw level of sgna over 1008d window."""
    res = _slope_pct(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_1008d_v039_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1008d window."""
    res = _slope_pct(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_1008d_v040_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 1008d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_pct_1260d_v041_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1260d window."""
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_pct_1260d_v042_signal(sgna):
    """Percentage slope for Raw level of sgna over 1260d window."""
    res = _slope_pct(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_pct_1260d_v043_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1260d window."""
    res = _slope_pct(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_pct_1260d_v044_signal(ebitda, sgna):
    """Percentage slope for Operating income per overhead dollar over 1260d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_5d_v045_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 5d window."""
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_5d_v046_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 5d window."""
    res = _jerk(sgna, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_5d_v047_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 5d window."""
    res = _jerk(marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_5d_v048_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 5d window."""
    res = _jerk(_ratio(ebitda, sgna), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_10d_v049_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 10d window."""
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_10d_v050_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 10d window."""
    res = _jerk(sgna, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_10d_v051_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 10d window."""
    res = _jerk(marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_10d_v052_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 10d window."""
    res = _jerk(_ratio(ebitda, sgna), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_21d_v053_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 21d window."""
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_21d_v054_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 21d window."""
    res = _jerk(sgna, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_21d_v055_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 21d window."""
    res = _jerk(marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_21d_v056_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 21d window."""
    res = _jerk(_ratio(ebitda, sgna), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_42d_v057_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 42d window."""
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_42d_v058_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 42d window."""
    res = _jerk(sgna, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_42d_v059_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 42d window."""
    res = _jerk(marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_42d_v060_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 42d window."""
    res = _jerk(_ratio(ebitda, sgna), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_63d_v061_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 63d window."""
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_63d_v062_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 63d window."""
    res = _jerk(sgna, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_63d_v063_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 63d window."""
    res = _jerk(marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_63d_v064_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 63d window."""
    res = _jerk(_ratio(ebitda, sgna), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_126d_v065_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 126d window."""
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_126d_v066_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 126d window."""
    res = _jerk(sgna, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_126d_v067_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 126d window."""
    res = _jerk(marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_126d_v068_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 126d window."""
    res = _jerk(_ratio(ebitda, sgna), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_252d_v069_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 252d window."""
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_252d_v070_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 252d window."""
    res = _jerk(sgna, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_252d_v071_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 252d window."""
    res = _jerk(marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_252d_v072_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 252d window."""
    res = _jerk(_ratio(ebitda, sgna), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_504d_v073_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 504d window."""
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_504d_v074_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 504d window."""
    res = _jerk(sgna, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_504d_v075_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 504d window."""
    res = _jerk(marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_504d_v076_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 504d window."""
    res = _jerk(_ratio(ebitda, sgna), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_756d_v077_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 756d window."""
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_756d_v078_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 756d window."""
    res = _jerk(sgna, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_756d_v079_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 756d window."""
    res = _jerk(marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_756d_v080_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 756d window."""
    res = _jerk(_ratio(ebitda, sgna), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_1008d_v081_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1008d window."""
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_1008d_v082_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 1008d window."""
    res = _jerk(sgna, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_1008d_v083_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1008d window."""
    res = _jerk(marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_1008d_v084_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 1008d window."""
    res = _jerk(_ratio(ebitda, sgna), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_jerk_1260d_v085_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1260d window."""
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_jerk_1260d_v086_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 1260d window."""
    res = _jerk(sgna, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_jerk_1260d_v087_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1260d window."""
    res = _jerk(marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_jerk_1260d_v088_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per overhead dollar over 1260d window."""
    res = _jerk(_ratio(ebitda, sgna), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_5d_v089_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 5d window."""
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_5d_v090_signal(sgna):
    """Normalized slope change for Raw level of sgna over 5d window."""
    res = (_slope_pct(sgna, 5).diff(5) / _sma(sgna.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_5d_v091_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 5d window."""
    res = (_slope_pct(marketcap, 5).diff(5) / _sma(marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_5d_v092_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 5d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 5).diff(5) / _sma(_ratio(ebitda, sgna).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_10d_v093_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 10d window."""
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_10d_v094_signal(sgna):
    """Normalized slope change for Raw level of sgna over 10d window."""
    res = (_slope_pct(sgna, 10).diff(10) / _sma(sgna.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_10d_v095_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 10d window."""
    res = (_slope_pct(marketcap, 10).diff(10) / _sma(marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_10d_v096_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 10d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 10).diff(10) / _sma(_ratio(ebitda, sgna).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_21d_v097_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 21d window."""
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_21d_v098_signal(sgna):
    """Normalized slope change for Raw level of sgna over 21d window."""
    res = (_slope_pct(sgna, 21).diff(21) / _sma(sgna.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_21d_v099_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 21d window."""
    res = (_slope_pct(marketcap, 21).diff(21) / _sma(marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_21d_v100_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 21d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 21).diff(21) / _sma(_ratio(ebitda, sgna).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_42d_v101_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 42d window."""
    res = (_slope_pct(ebitda, 42).diff(42) / _sma(ebitda.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_42d_v102_signal(sgna):
    """Normalized slope change for Raw level of sgna over 42d window."""
    res = (_slope_pct(sgna, 42).diff(42) / _sma(sgna.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_42d_v103_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 42d window."""
    res = (_slope_pct(marketcap, 42).diff(42) / _sma(marketcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_42d_v104_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 42d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 42).diff(42) / _sma(_ratio(ebitda, sgna).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_63d_v105_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 63d window."""
    res = (_slope_pct(ebitda, 63).diff(63) / _sma(ebitda.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_63d_v106_signal(sgna):
    """Normalized slope change for Raw level of sgna over 63d window."""
    res = (_slope_pct(sgna, 63).diff(63) / _sma(sgna.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_63d_v107_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 63d window."""
    res = (_slope_pct(marketcap, 63).diff(63) / _sma(marketcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_63d_v108_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 63d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 63).diff(63) / _sma(_ratio(ebitda, sgna).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_126d_v109_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 126d window."""
    res = (_slope_pct(ebitda, 126).diff(126) / _sma(ebitda.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_126d_v110_signal(sgna):
    """Normalized slope change for Raw level of sgna over 126d window."""
    res = (_slope_pct(sgna, 126).diff(126) / _sma(sgna.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_126d_v111_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 126d window."""
    res = (_slope_pct(marketcap, 126).diff(126) / _sma(marketcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_126d_v112_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 126d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 126).diff(126) / _sma(_ratio(ebitda, sgna).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_252d_v113_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 252d window."""
    res = (_slope_pct(ebitda, 252).diff(252) / _sma(ebitda.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_252d_v114_signal(sgna):
    """Normalized slope change for Raw level of sgna over 252d window."""
    res = (_slope_pct(sgna, 252).diff(252) / _sma(sgna.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_252d_v115_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 252d window."""
    res = (_slope_pct(marketcap, 252).diff(252) / _sma(marketcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_252d_v116_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 252d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 252).diff(252) / _sma(_ratio(ebitda, sgna).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_504d_v117_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 504d window."""
    res = (_slope_pct(ebitda, 504).diff(504) / _sma(ebitda.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_504d_v118_signal(sgna):
    """Normalized slope change for Raw level of sgna over 504d window."""
    res = (_slope_pct(sgna, 504).diff(504) / _sma(sgna.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_504d_v119_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 504d window."""
    res = (_slope_pct(marketcap, 504).diff(504) / _sma(marketcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_504d_v120_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 504d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 504).diff(504) / _sma(_ratio(ebitda, sgna).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_756d_v121_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 756d window."""
    res = (_slope_pct(ebitda, 756).diff(756) / _sma(ebitda.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_756d_v122_signal(sgna):
    """Normalized slope change for Raw level of sgna over 756d window."""
    res = (_slope_pct(sgna, 756).diff(756) / _sma(sgna.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_756d_v123_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 756d window."""
    res = (_slope_pct(marketcap, 756).diff(756) / _sma(marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_756d_v124_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 756d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 756).diff(756) / _sma(_ratio(ebitda, sgna).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_1008d_v125_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 1008d window."""
    res = (_slope_pct(ebitda, 1008).diff(1008) / _sma(ebitda.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_1008d_v126_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1008d window."""
    res = (_slope_pct(sgna, 1008).diff(1008) / _sma(sgna.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_1008d_v127_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1008d window."""
    res = (_slope_pct(marketcap, 1008).diff(1008) / _sma(marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_1008d_v128_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 1008d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 1008).diff(1008) / _sma(_ratio(ebitda, sgna).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_slope_diff_norm_1260d_v129_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 1260d window."""
    res = (_slope_pct(ebitda, 1260).diff(1260) / _sma(ebitda.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_slope_diff_norm_1260d_v130_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1260d window."""
    res = (_slope_pct(sgna, 1260).diff(1260) / _sma(sgna.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_slope_diff_norm_1260d_v131_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1260d window."""
    res = (_slope_pct(marketcap, 1260).diff(1260) / _sma(marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_slope_diff_norm_1260d_v132_signal(ebitda, sgna):
    """Normalized slope change for Operating income per overhead dollar over 1260d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 1260).diff(1260) / _sma(_ratio(ebitda, sgna).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_mom_z_5d_v133_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 5d window."""
    res = _z(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_mom_z_5d_v134_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 5d window."""
    res = _z(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_mom_z_5d_v135_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 5d window."""
    res = _z(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_mom_z_5d_v136_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per overhead dollar over 5d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_mom_z_10d_v137_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 10d window."""
    res = _z(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_mom_z_10d_v138_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 10d window."""
    res = _z(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_mom_z_10d_v139_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 10d window."""
    res = _z(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_mom_z_10d_v140_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per overhead dollar over 10d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_mom_z_21d_v141_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 21d window."""
    res = _z(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_mom_z_21d_v142_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 21d window."""
    res = _z(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_mom_z_21d_v143_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 21d window."""
    res = _z(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_mom_z_21d_v144_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per overhead dollar over 21d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_mom_z_42d_v145_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 42d window."""
    res = _z(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_mom_z_42d_v146_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 42d window."""
    res = _z(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_marketcap_mom_z_42d_v147_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 42d window."""
    res = _z(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_cost_moat_mom_z_42d_v148_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per overhead dollar over 42d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_ebitda_mom_z_63d_v149_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 63d window."""
    res = _z(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_synergy_potential_sgna_mom_z_63d_v150_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 63d window."""
    res = _z(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f28_synergy_potential_ebitda_slope_pct_5d_v001_signal": {"func": f28_synergy_potential_ebitda_slope_pct_5d_v001_signal},
    "f28_synergy_potential_sgna_slope_pct_5d_v002_signal": {"func": f28_synergy_potential_sgna_slope_pct_5d_v002_signal},
    "f28_synergy_potential_marketcap_slope_pct_5d_v003_signal": {"func": f28_synergy_potential_marketcap_slope_pct_5d_v003_signal},
    "f28_synergy_potential_cost_moat_slope_pct_5d_v004_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_5d_v004_signal},
    "f28_synergy_potential_ebitda_slope_pct_10d_v005_signal": {"func": f28_synergy_potential_ebitda_slope_pct_10d_v005_signal},
    "f28_synergy_potential_sgna_slope_pct_10d_v006_signal": {"func": f28_synergy_potential_sgna_slope_pct_10d_v006_signal},
    "f28_synergy_potential_marketcap_slope_pct_10d_v007_signal": {"func": f28_synergy_potential_marketcap_slope_pct_10d_v007_signal},
    "f28_synergy_potential_cost_moat_slope_pct_10d_v008_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_10d_v008_signal},
    "f28_synergy_potential_ebitda_slope_pct_21d_v009_signal": {"func": f28_synergy_potential_ebitda_slope_pct_21d_v009_signal},
    "f28_synergy_potential_sgna_slope_pct_21d_v010_signal": {"func": f28_synergy_potential_sgna_slope_pct_21d_v010_signal},
    "f28_synergy_potential_marketcap_slope_pct_21d_v011_signal": {"func": f28_synergy_potential_marketcap_slope_pct_21d_v011_signal},
    "f28_synergy_potential_cost_moat_slope_pct_21d_v012_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_21d_v012_signal},
    "f28_synergy_potential_ebitda_slope_pct_42d_v013_signal": {"func": f28_synergy_potential_ebitda_slope_pct_42d_v013_signal},
    "f28_synergy_potential_sgna_slope_pct_42d_v014_signal": {"func": f28_synergy_potential_sgna_slope_pct_42d_v014_signal},
    "f28_synergy_potential_marketcap_slope_pct_42d_v015_signal": {"func": f28_synergy_potential_marketcap_slope_pct_42d_v015_signal},
    "f28_synergy_potential_cost_moat_slope_pct_42d_v016_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_42d_v016_signal},
    "f28_synergy_potential_ebitda_slope_pct_63d_v017_signal": {"func": f28_synergy_potential_ebitda_slope_pct_63d_v017_signal},
    "f28_synergy_potential_sgna_slope_pct_63d_v018_signal": {"func": f28_synergy_potential_sgna_slope_pct_63d_v018_signal},
    "f28_synergy_potential_marketcap_slope_pct_63d_v019_signal": {"func": f28_synergy_potential_marketcap_slope_pct_63d_v019_signal},
    "f28_synergy_potential_cost_moat_slope_pct_63d_v020_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_63d_v020_signal},
    "f28_synergy_potential_ebitda_slope_pct_126d_v021_signal": {"func": f28_synergy_potential_ebitda_slope_pct_126d_v021_signal},
    "f28_synergy_potential_sgna_slope_pct_126d_v022_signal": {"func": f28_synergy_potential_sgna_slope_pct_126d_v022_signal},
    "f28_synergy_potential_marketcap_slope_pct_126d_v023_signal": {"func": f28_synergy_potential_marketcap_slope_pct_126d_v023_signal},
    "f28_synergy_potential_cost_moat_slope_pct_126d_v024_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_126d_v024_signal},
    "f28_synergy_potential_ebitda_slope_pct_252d_v025_signal": {"func": f28_synergy_potential_ebitda_slope_pct_252d_v025_signal},
    "f28_synergy_potential_sgna_slope_pct_252d_v026_signal": {"func": f28_synergy_potential_sgna_slope_pct_252d_v026_signal},
    "f28_synergy_potential_marketcap_slope_pct_252d_v027_signal": {"func": f28_synergy_potential_marketcap_slope_pct_252d_v027_signal},
    "f28_synergy_potential_cost_moat_slope_pct_252d_v028_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_252d_v028_signal},
    "f28_synergy_potential_ebitda_slope_pct_504d_v029_signal": {"func": f28_synergy_potential_ebitda_slope_pct_504d_v029_signal},
    "f28_synergy_potential_sgna_slope_pct_504d_v030_signal": {"func": f28_synergy_potential_sgna_slope_pct_504d_v030_signal},
    "f28_synergy_potential_marketcap_slope_pct_504d_v031_signal": {"func": f28_synergy_potential_marketcap_slope_pct_504d_v031_signal},
    "f28_synergy_potential_cost_moat_slope_pct_504d_v032_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_504d_v032_signal},
    "f28_synergy_potential_ebitda_slope_pct_756d_v033_signal": {"func": f28_synergy_potential_ebitda_slope_pct_756d_v033_signal},
    "f28_synergy_potential_sgna_slope_pct_756d_v034_signal": {"func": f28_synergy_potential_sgna_slope_pct_756d_v034_signal},
    "f28_synergy_potential_marketcap_slope_pct_756d_v035_signal": {"func": f28_synergy_potential_marketcap_slope_pct_756d_v035_signal},
    "f28_synergy_potential_cost_moat_slope_pct_756d_v036_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_756d_v036_signal},
    "f28_synergy_potential_ebitda_slope_pct_1008d_v037_signal": {"func": f28_synergy_potential_ebitda_slope_pct_1008d_v037_signal},
    "f28_synergy_potential_sgna_slope_pct_1008d_v038_signal": {"func": f28_synergy_potential_sgna_slope_pct_1008d_v038_signal},
    "f28_synergy_potential_marketcap_slope_pct_1008d_v039_signal": {"func": f28_synergy_potential_marketcap_slope_pct_1008d_v039_signal},
    "f28_synergy_potential_cost_moat_slope_pct_1008d_v040_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_1008d_v040_signal},
    "f28_synergy_potential_ebitda_slope_pct_1260d_v041_signal": {"func": f28_synergy_potential_ebitda_slope_pct_1260d_v041_signal},
    "f28_synergy_potential_sgna_slope_pct_1260d_v042_signal": {"func": f28_synergy_potential_sgna_slope_pct_1260d_v042_signal},
    "f28_synergy_potential_marketcap_slope_pct_1260d_v043_signal": {"func": f28_synergy_potential_marketcap_slope_pct_1260d_v043_signal},
    "f28_synergy_potential_cost_moat_slope_pct_1260d_v044_signal": {"func": f28_synergy_potential_cost_moat_slope_pct_1260d_v044_signal},
    "f28_synergy_potential_ebitda_jerk_5d_v045_signal": {"func": f28_synergy_potential_ebitda_jerk_5d_v045_signal},
    "f28_synergy_potential_sgna_jerk_5d_v046_signal": {"func": f28_synergy_potential_sgna_jerk_5d_v046_signal},
    "f28_synergy_potential_marketcap_jerk_5d_v047_signal": {"func": f28_synergy_potential_marketcap_jerk_5d_v047_signal},
    "f28_synergy_potential_cost_moat_jerk_5d_v048_signal": {"func": f28_synergy_potential_cost_moat_jerk_5d_v048_signal},
    "f28_synergy_potential_ebitda_jerk_10d_v049_signal": {"func": f28_synergy_potential_ebitda_jerk_10d_v049_signal},
    "f28_synergy_potential_sgna_jerk_10d_v050_signal": {"func": f28_synergy_potential_sgna_jerk_10d_v050_signal},
    "f28_synergy_potential_marketcap_jerk_10d_v051_signal": {"func": f28_synergy_potential_marketcap_jerk_10d_v051_signal},
    "f28_synergy_potential_cost_moat_jerk_10d_v052_signal": {"func": f28_synergy_potential_cost_moat_jerk_10d_v052_signal},
    "f28_synergy_potential_ebitda_jerk_21d_v053_signal": {"func": f28_synergy_potential_ebitda_jerk_21d_v053_signal},
    "f28_synergy_potential_sgna_jerk_21d_v054_signal": {"func": f28_synergy_potential_sgna_jerk_21d_v054_signal},
    "f28_synergy_potential_marketcap_jerk_21d_v055_signal": {"func": f28_synergy_potential_marketcap_jerk_21d_v055_signal},
    "f28_synergy_potential_cost_moat_jerk_21d_v056_signal": {"func": f28_synergy_potential_cost_moat_jerk_21d_v056_signal},
    "f28_synergy_potential_ebitda_jerk_42d_v057_signal": {"func": f28_synergy_potential_ebitda_jerk_42d_v057_signal},
    "f28_synergy_potential_sgna_jerk_42d_v058_signal": {"func": f28_synergy_potential_sgna_jerk_42d_v058_signal},
    "f28_synergy_potential_marketcap_jerk_42d_v059_signal": {"func": f28_synergy_potential_marketcap_jerk_42d_v059_signal},
    "f28_synergy_potential_cost_moat_jerk_42d_v060_signal": {"func": f28_synergy_potential_cost_moat_jerk_42d_v060_signal},
    "f28_synergy_potential_ebitda_jerk_63d_v061_signal": {"func": f28_synergy_potential_ebitda_jerk_63d_v061_signal},
    "f28_synergy_potential_sgna_jerk_63d_v062_signal": {"func": f28_synergy_potential_sgna_jerk_63d_v062_signal},
    "f28_synergy_potential_marketcap_jerk_63d_v063_signal": {"func": f28_synergy_potential_marketcap_jerk_63d_v063_signal},
    "f28_synergy_potential_cost_moat_jerk_63d_v064_signal": {"func": f28_synergy_potential_cost_moat_jerk_63d_v064_signal},
    "f28_synergy_potential_ebitda_jerk_126d_v065_signal": {"func": f28_synergy_potential_ebitda_jerk_126d_v065_signal},
    "f28_synergy_potential_sgna_jerk_126d_v066_signal": {"func": f28_synergy_potential_sgna_jerk_126d_v066_signal},
    "f28_synergy_potential_marketcap_jerk_126d_v067_signal": {"func": f28_synergy_potential_marketcap_jerk_126d_v067_signal},
    "f28_synergy_potential_cost_moat_jerk_126d_v068_signal": {"func": f28_synergy_potential_cost_moat_jerk_126d_v068_signal},
    "f28_synergy_potential_ebitda_jerk_252d_v069_signal": {"func": f28_synergy_potential_ebitda_jerk_252d_v069_signal},
    "f28_synergy_potential_sgna_jerk_252d_v070_signal": {"func": f28_synergy_potential_sgna_jerk_252d_v070_signal},
    "f28_synergy_potential_marketcap_jerk_252d_v071_signal": {"func": f28_synergy_potential_marketcap_jerk_252d_v071_signal},
    "f28_synergy_potential_cost_moat_jerk_252d_v072_signal": {"func": f28_synergy_potential_cost_moat_jerk_252d_v072_signal},
    "f28_synergy_potential_ebitda_jerk_504d_v073_signal": {"func": f28_synergy_potential_ebitda_jerk_504d_v073_signal},
    "f28_synergy_potential_sgna_jerk_504d_v074_signal": {"func": f28_synergy_potential_sgna_jerk_504d_v074_signal},
    "f28_synergy_potential_marketcap_jerk_504d_v075_signal": {"func": f28_synergy_potential_marketcap_jerk_504d_v075_signal},
    "f28_synergy_potential_cost_moat_jerk_504d_v076_signal": {"func": f28_synergy_potential_cost_moat_jerk_504d_v076_signal},
    "f28_synergy_potential_ebitda_jerk_756d_v077_signal": {"func": f28_synergy_potential_ebitda_jerk_756d_v077_signal},
    "f28_synergy_potential_sgna_jerk_756d_v078_signal": {"func": f28_synergy_potential_sgna_jerk_756d_v078_signal},
    "f28_synergy_potential_marketcap_jerk_756d_v079_signal": {"func": f28_synergy_potential_marketcap_jerk_756d_v079_signal},
    "f28_synergy_potential_cost_moat_jerk_756d_v080_signal": {"func": f28_synergy_potential_cost_moat_jerk_756d_v080_signal},
    "f28_synergy_potential_ebitda_jerk_1008d_v081_signal": {"func": f28_synergy_potential_ebitda_jerk_1008d_v081_signal},
    "f28_synergy_potential_sgna_jerk_1008d_v082_signal": {"func": f28_synergy_potential_sgna_jerk_1008d_v082_signal},
    "f28_synergy_potential_marketcap_jerk_1008d_v083_signal": {"func": f28_synergy_potential_marketcap_jerk_1008d_v083_signal},
    "f28_synergy_potential_cost_moat_jerk_1008d_v084_signal": {"func": f28_synergy_potential_cost_moat_jerk_1008d_v084_signal},
    "f28_synergy_potential_ebitda_jerk_1260d_v085_signal": {"func": f28_synergy_potential_ebitda_jerk_1260d_v085_signal},
    "f28_synergy_potential_sgna_jerk_1260d_v086_signal": {"func": f28_synergy_potential_sgna_jerk_1260d_v086_signal},
    "f28_synergy_potential_marketcap_jerk_1260d_v087_signal": {"func": f28_synergy_potential_marketcap_jerk_1260d_v087_signal},
    "f28_synergy_potential_cost_moat_jerk_1260d_v088_signal": {"func": f28_synergy_potential_cost_moat_jerk_1260d_v088_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_5d_v089_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_5d_v089_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_5d_v090_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_5d_v090_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_5d_v091_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_5d_v091_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_5d_v092_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_5d_v092_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_10d_v093_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_10d_v093_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_10d_v094_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_10d_v094_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_10d_v095_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_10d_v095_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_10d_v096_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_10d_v096_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_21d_v097_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_21d_v097_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_21d_v098_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_21d_v098_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_21d_v099_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_21d_v099_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_21d_v100_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_21d_v100_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_42d_v101_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_42d_v101_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_42d_v102_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_42d_v102_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_42d_v103_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_42d_v103_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_42d_v104_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_42d_v104_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_63d_v105_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_63d_v105_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_63d_v106_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_63d_v106_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_63d_v107_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_63d_v107_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_63d_v108_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_63d_v108_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_126d_v109_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_126d_v109_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_126d_v110_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_126d_v110_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_126d_v111_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_126d_v111_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_126d_v112_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_126d_v112_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_252d_v113_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_252d_v113_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_252d_v114_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_252d_v114_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_252d_v115_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_252d_v115_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_252d_v116_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_252d_v116_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_504d_v117_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_504d_v117_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_504d_v118_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_504d_v118_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_504d_v119_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_504d_v119_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_504d_v120_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_504d_v120_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_756d_v121_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_756d_v121_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_756d_v122_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_756d_v122_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_756d_v123_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_756d_v123_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_756d_v124_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_756d_v124_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_1008d_v125_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_1008d_v125_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_1008d_v126_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_1008d_v126_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_1008d_v127_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_1008d_v127_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_1008d_v128_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_1008d_v128_signal},
    "f28_synergy_potential_ebitda_slope_diff_norm_1260d_v129_signal": {"func": f28_synergy_potential_ebitda_slope_diff_norm_1260d_v129_signal},
    "f28_synergy_potential_sgna_slope_diff_norm_1260d_v130_signal": {"func": f28_synergy_potential_sgna_slope_diff_norm_1260d_v130_signal},
    "f28_synergy_potential_marketcap_slope_diff_norm_1260d_v131_signal": {"func": f28_synergy_potential_marketcap_slope_diff_norm_1260d_v131_signal},
    "f28_synergy_potential_cost_moat_slope_diff_norm_1260d_v132_signal": {"func": f28_synergy_potential_cost_moat_slope_diff_norm_1260d_v132_signal},
    "f28_synergy_potential_ebitda_mom_z_5d_v133_signal": {"func": f28_synergy_potential_ebitda_mom_z_5d_v133_signal},
    "f28_synergy_potential_sgna_mom_z_5d_v134_signal": {"func": f28_synergy_potential_sgna_mom_z_5d_v134_signal},
    "f28_synergy_potential_marketcap_mom_z_5d_v135_signal": {"func": f28_synergy_potential_marketcap_mom_z_5d_v135_signal},
    "f28_synergy_potential_cost_moat_mom_z_5d_v136_signal": {"func": f28_synergy_potential_cost_moat_mom_z_5d_v136_signal},
    "f28_synergy_potential_ebitda_mom_z_10d_v137_signal": {"func": f28_synergy_potential_ebitda_mom_z_10d_v137_signal},
    "f28_synergy_potential_sgna_mom_z_10d_v138_signal": {"func": f28_synergy_potential_sgna_mom_z_10d_v138_signal},
    "f28_synergy_potential_marketcap_mom_z_10d_v139_signal": {"func": f28_synergy_potential_marketcap_mom_z_10d_v139_signal},
    "f28_synergy_potential_cost_moat_mom_z_10d_v140_signal": {"func": f28_synergy_potential_cost_moat_mom_z_10d_v140_signal},
    "f28_synergy_potential_ebitda_mom_z_21d_v141_signal": {"func": f28_synergy_potential_ebitda_mom_z_21d_v141_signal},
    "f28_synergy_potential_sgna_mom_z_21d_v142_signal": {"func": f28_synergy_potential_sgna_mom_z_21d_v142_signal},
    "f28_synergy_potential_marketcap_mom_z_21d_v143_signal": {"func": f28_synergy_potential_marketcap_mom_z_21d_v143_signal},
    "f28_synergy_potential_cost_moat_mom_z_21d_v144_signal": {"func": f28_synergy_potential_cost_moat_mom_z_21d_v144_signal},
    "f28_synergy_potential_ebitda_mom_z_42d_v145_signal": {"func": f28_synergy_potential_ebitda_mom_z_42d_v145_signal},
    "f28_synergy_potential_sgna_mom_z_42d_v146_signal": {"func": f28_synergy_potential_sgna_mom_z_42d_v146_signal},
    "f28_synergy_potential_marketcap_mom_z_42d_v147_signal": {"func": f28_synergy_potential_marketcap_mom_z_42d_v147_signal},
    "f28_synergy_potential_cost_moat_mom_z_42d_v148_signal": {"func": f28_synergy_potential_cost_moat_mom_z_42d_v148_signal},
    "f28_synergy_potential_ebitda_mom_z_63d_v149_signal": {"func": f28_synergy_potential_ebitda_mom_z_63d_v149_signal},
    "f28_synergy_potential_sgna_mom_z_63d_v150_signal": {"func": f28_synergy_potential_sgna_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 28...")
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
