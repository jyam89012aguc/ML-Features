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

def f47_roic_compounder_fin_roic_slope_pct_5d_v001_signal(roic):
    """Percentage slope for Raw level of roic over 5d window."""
    res = _slope_pct(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_5d_v002_signal(invcap):
    """Percentage slope for Raw level of invcap over 5d window."""
    res = _slope_pct(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_5d_v003_signal(netinc):
    """Percentage slope for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_5d_v004_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 5d window."""
    res = _slope_pct(_std(roic, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_10d_v005_signal(roic):
    """Percentage slope for Raw level of roic over 10d window."""
    res = _slope_pct(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_10d_v006_signal(invcap):
    """Percentage slope for Raw level of invcap over 10d window."""
    res = _slope_pct(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_10d_v007_signal(netinc):
    """Percentage slope for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_10d_v008_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 10d window."""
    res = _slope_pct(_std(roic, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_21d_v009_signal(roic):
    """Percentage slope for Raw level of roic over 21d window."""
    res = _slope_pct(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_21d_v010_signal(invcap):
    """Percentage slope for Raw level of invcap over 21d window."""
    res = _slope_pct(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_21d_v011_signal(netinc):
    """Percentage slope for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_21d_v012_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 21d window."""
    res = _slope_pct(_std(roic, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_42d_v013_signal(roic):
    """Percentage slope for Raw level of roic over 42d window."""
    res = _slope_pct(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_42d_v014_signal(invcap):
    """Percentage slope for Raw level of invcap over 42d window."""
    res = _slope_pct(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_42d_v015_signal(netinc):
    """Percentage slope for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_42d_v016_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 42d window."""
    res = _slope_pct(_std(roic, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_63d_v017_signal(roic):
    """Percentage slope for Raw level of roic over 63d window."""
    res = _slope_pct(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_63d_v018_signal(invcap):
    """Percentage slope for Raw level of invcap over 63d window."""
    res = _slope_pct(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_63d_v019_signal(netinc):
    """Percentage slope for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_63d_v020_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 63d window."""
    res = _slope_pct(_std(roic, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_126d_v021_signal(roic):
    """Percentage slope for Raw level of roic over 126d window."""
    res = _slope_pct(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_126d_v022_signal(invcap):
    """Percentage slope for Raw level of invcap over 126d window."""
    res = _slope_pct(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_126d_v023_signal(netinc):
    """Percentage slope for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_126d_v024_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 126d window."""
    res = _slope_pct(_std(roic, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_252d_v025_signal(roic):
    """Percentage slope for Raw level of roic over 252d window."""
    res = _slope_pct(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_252d_v026_signal(invcap):
    """Percentage slope for Raw level of invcap over 252d window."""
    res = _slope_pct(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_252d_v027_signal(netinc):
    """Percentage slope for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_252d_v028_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 252d window."""
    res = _slope_pct(_std(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_504d_v029_signal(roic):
    """Percentage slope for Raw level of roic over 504d window."""
    res = _slope_pct(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_504d_v030_signal(invcap):
    """Percentage slope for Raw level of invcap over 504d window."""
    res = _slope_pct(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_504d_v031_signal(netinc):
    """Percentage slope for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_504d_v032_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 504d window."""
    res = _slope_pct(_std(roic, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_756d_v033_signal(roic):
    """Percentage slope for Raw level of roic over 756d window."""
    res = _slope_pct(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_756d_v034_signal(invcap):
    """Percentage slope for Raw level of invcap over 756d window."""
    res = _slope_pct(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_756d_v035_signal(netinc):
    """Percentage slope for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_756d_v036_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 756d window."""
    res = _slope_pct(_std(roic, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_1008d_v037_signal(roic):
    """Percentage slope for Raw level of roic over 1008d window."""
    res = _slope_pct(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_1008d_v038_signal(invcap):
    """Percentage slope for Raw level of invcap over 1008d window."""
    res = _slope_pct(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_1008d_v039_signal(netinc):
    """Percentage slope for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_1008d_v040_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 1008d window."""
    res = _slope_pct(_std(roic, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_pct_1260d_v041_signal(roic):
    """Percentage slope for Raw level of roic over 1260d window."""
    res = _slope_pct(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_pct_1260d_v042_signal(invcap):
    """Percentage slope for Raw level of invcap over 1260d window."""
    res = _slope_pct(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_pct_1260d_v043_signal(netinc):
    """Percentage slope for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_pct_1260d_v044_signal(roic):
    """Percentage slope for ROIC stability (standard deviation) over 1260d window."""
    res = _slope_pct(_std(roic, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_5d_v045_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 5d window."""
    res = _jerk(roic, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_5d_v046_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 5d window."""
    res = _jerk(invcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_5d_v047_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_5d_v048_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 5d window."""
    res = _jerk(_std(roic, 252), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_10d_v049_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 10d window."""
    res = _jerk(roic, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_10d_v050_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 10d window."""
    res = _jerk(invcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_10d_v051_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_10d_v052_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 10d window."""
    res = _jerk(_std(roic, 252), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_21d_v053_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 21d window."""
    res = _jerk(roic, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_21d_v054_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 21d window."""
    res = _jerk(invcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_21d_v055_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_21d_v056_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 21d window."""
    res = _jerk(_std(roic, 252), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_42d_v057_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 42d window."""
    res = _jerk(roic, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_42d_v058_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 42d window."""
    res = _jerk(invcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_42d_v059_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_42d_v060_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 42d window."""
    res = _jerk(_std(roic, 252), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_63d_v061_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 63d window."""
    res = _jerk(roic, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_63d_v062_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 63d window."""
    res = _jerk(invcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_63d_v063_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_63d_v064_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 63d window."""
    res = _jerk(_std(roic, 252), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_126d_v065_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 126d window."""
    res = _jerk(roic, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_126d_v066_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 126d window."""
    res = _jerk(invcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_126d_v067_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_126d_v068_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 126d window."""
    res = _jerk(_std(roic, 252), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_252d_v069_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 252d window."""
    res = _jerk(roic, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_252d_v070_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 252d window."""
    res = _jerk(invcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_252d_v071_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_252d_v072_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 252d window."""
    res = _jerk(_std(roic, 252), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_504d_v073_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 504d window."""
    res = _jerk(roic, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_504d_v074_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 504d window."""
    res = _jerk(invcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_504d_v075_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_504d_v076_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 504d window."""
    res = _jerk(_std(roic, 252), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_756d_v077_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 756d window."""
    res = _jerk(roic, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_756d_v078_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 756d window."""
    res = _jerk(invcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_756d_v079_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_756d_v080_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 756d window."""
    res = _jerk(_std(roic, 252), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_1008d_v081_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 1008d window."""
    res = _jerk(roic, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_1008d_v082_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 1008d window."""
    res = _jerk(invcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_1008d_v083_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_1008d_v084_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 1008d window."""
    res = _jerk(_std(roic, 252), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_jerk_1260d_v085_signal(roic):
    """Acceleration/Jerk for Raw level of roic over 1260d window."""
    res = _jerk(roic, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_jerk_1260d_v086_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 1260d window."""
    res = _jerk(invcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_jerk_1260d_v087_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_jerk_1260d_v088_signal(roic):
    """Acceleration/Jerk for ROIC stability (standard deviation) over 1260d window."""
    res = _jerk(_std(roic, 252), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_5d_v089_signal(roic):
    """Normalized slope change for Raw level of roic over 5d window."""
    res = (_slope_pct(roic, 5).diff(5) / _sma(roic.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_5d_v090_signal(invcap):
    """Normalized slope change for Raw level of invcap over 5d window."""
    res = (_slope_pct(invcap, 5).diff(5) / _sma(invcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_5d_v091_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_5d_v092_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 5d window."""
    res = (_slope_pct(_std(roic, 252), 5).diff(5) / _sma(_std(roic, 252).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_10d_v093_signal(roic):
    """Normalized slope change for Raw level of roic over 10d window."""
    res = (_slope_pct(roic, 10).diff(10) / _sma(roic.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_10d_v094_signal(invcap):
    """Normalized slope change for Raw level of invcap over 10d window."""
    res = (_slope_pct(invcap, 10).diff(10) / _sma(invcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_10d_v095_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_10d_v096_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 10d window."""
    res = (_slope_pct(_std(roic, 252), 10).diff(10) / _sma(_std(roic, 252).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_21d_v097_signal(roic):
    """Normalized slope change for Raw level of roic over 21d window."""
    res = (_slope_pct(roic, 21).diff(21) / _sma(roic.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_21d_v098_signal(invcap):
    """Normalized slope change for Raw level of invcap over 21d window."""
    res = (_slope_pct(invcap, 21).diff(21) / _sma(invcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_21d_v099_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_21d_v100_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 21d window."""
    res = (_slope_pct(_std(roic, 252), 21).diff(21) / _sma(_std(roic, 252).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_42d_v101_signal(roic):
    """Normalized slope change for Raw level of roic over 42d window."""
    res = (_slope_pct(roic, 42).diff(42) / _sma(roic.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_42d_v102_signal(invcap):
    """Normalized slope change for Raw level of invcap over 42d window."""
    res = (_slope_pct(invcap, 42).diff(42) / _sma(invcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_42d_v103_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_42d_v104_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 42d window."""
    res = (_slope_pct(_std(roic, 252), 42).diff(42) / _sma(_std(roic, 252).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_63d_v105_signal(roic):
    """Normalized slope change for Raw level of roic over 63d window."""
    res = (_slope_pct(roic, 63).diff(63) / _sma(roic.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_63d_v106_signal(invcap):
    """Normalized slope change for Raw level of invcap over 63d window."""
    res = (_slope_pct(invcap, 63).diff(63) / _sma(invcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_63d_v107_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_63d_v108_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 63d window."""
    res = (_slope_pct(_std(roic, 252), 63).diff(63) / _sma(_std(roic, 252).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_126d_v109_signal(roic):
    """Normalized slope change for Raw level of roic over 126d window."""
    res = (_slope_pct(roic, 126).diff(126) / _sma(roic.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_126d_v110_signal(invcap):
    """Normalized slope change for Raw level of invcap over 126d window."""
    res = (_slope_pct(invcap, 126).diff(126) / _sma(invcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_126d_v111_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_126d_v112_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 126d window."""
    res = (_slope_pct(_std(roic, 252), 126).diff(126) / _sma(_std(roic, 252).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_252d_v113_signal(roic):
    """Normalized slope change for Raw level of roic over 252d window."""
    res = (_slope_pct(roic, 252).diff(252) / _sma(roic.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_252d_v114_signal(invcap):
    """Normalized slope change for Raw level of invcap over 252d window."""
    res = (_slope_pct(invcap, 252).diff(252) / _sma(invcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_252d_v115_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_252d_v116_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 252d window."""
    res = (_slope_pct(_std(roic, 252), 252).diff(252) / _sma(_std(roic, 252).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_504d_v117_signal(roic):
    """Normalized slope change for Raw level of roic over 504d window."""
    res = (_slope_pct(roic, 504).diff(504) / _sma(roic.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_504d_v118_signal(invcap):
    """Normalized slope change for Raw level of invcap over 504d window."""
    res = (_slope_pct(invcap, 504).diff(504) / _sma(invcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_504d_v119_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_504d_v120_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 504d window."""
    res = (_slope_pct(_std(roic, 252), 504).diff(504) / _sma(_std(roic, 252).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_756d_v121_signal(roic):
    """Normalized slope change for Raw level of roic over 756d window."""
    res = (_slope_pct(roic, 756).diff(756) / _sma(roic.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_756d_v122_signal(invcap):
    """Normalized slope change for Raw level of invcap over 756d window."""
    res = (_slope_pct(invcap, 756).diff(756) / _sma(invcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_756d_v123_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_756d_v124_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 756d window."""
    res = (_slope_pct(_std(roic, 252), 756).diff(756) / _sma(_std(roic, 252).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_1008d_v125_signal(roic):
    """Normalized slope change for Raw level of roic over 1008d window."""
    res = (_slope_pct(roic, 1008).diff(1008) / _sma(roic.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_1008d_v126_signal(invcap):
    """Normalized slope change for Raw level of invcap over 1008d window."""
    res = (_slope_pct(invcap, 1008).diff(1008) / _sma(invcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_1008d_v127_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_1008d_v128_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 1008d window."""
    res = (_slope_pct(_std(roic, 252), 1008).diff(1008) / _sma(_std(roic, 252).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_slope_diff_norm_1260d_v129_signal(roic):
    """Normalized slope change for Raw level of roic over 1260d window."""
    res = (_slope_pct(roic, 1260).diff(1260) / _sma(roic.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_slope_diff_norm_1260d_v130_signal(invcap):
    """Normalized slope change for Raw level of invcap over 1260d window."""
    res = (_slope_pct(invcap, 1260).diff(1260) / _sma(invcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_slope_diff_norm_1260d_v131_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_diff_norm_1260d_v132_signal(roic):
    """Normalized slope change for ROIC stability (standard deviation) over 1260d window."""
    res = (_slope_pct(_std(roic, 252), 1260).diff(1260) / _sma(_std(roic, 252).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_5d_v133_signal(roic):
    """Relative momentum strength for Raw level of roic over 5d window."""
    res = _z(_slope_pct(roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_5d_v134_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 5d window."""
    res = _z(_slope_pct(invcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_5d_v135_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_5d_v136_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 5d window."""
    res = _z(_slope_pct(_std(roic, 252), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_10d_v137_signal(roic):
    """Relative momentum strength for Raw level of roic over 10d window."""
    res = _z(_slope_pct(roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_10d_v138_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 10d window."""
    res = _z(_slope_pct(invcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_10d_v139_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_10d_v140_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 10d window."""
    res = _z(_slope_pct(_std(roic, 252), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_21d_v141_signal(roic):
    """Relative momentum strength for Raw level of roic over 21d window."""
    res = _z(_slope_pct(roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_21d_v142_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 21d window."""
    res = _z(_slope_pct(invcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_21d_v143_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_21d_v144_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 21d window."""
    res = _z(_slope_pct(_std(roic, 252), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_42d_v145_signal(roic):
    """Relative momentum strength for Raw level of roic over 42d window."""
    res = _z(_slope_pct(roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_42d_v146_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 42d window."""
    res = _z(_slope_pct(invcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_42d_v147_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_42d_v148_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 42d window."""
    res = _z(_slope_pct(_std(roic, 252), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_63d_v149_signal(roic):
    """Relative momentum strength for Raw level of roic over 63d window."""
    res = _z(_slope_pct(roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_63d_v150_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 63d window."""
    res = _z(_slope_pct(invcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f47_roic_compounder_fin_roic_slope_pct_5d_v001_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_5d_v001_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_5d_v002_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_5d_v002_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_5d_v003_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_5d_v003_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_5d_v004_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_5d_v004_signal},
    "f47_roic_compounder_fin_roic_slope_pct_10d_v005_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_10d_v005_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_10d_v006_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_10d_v006_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_10d_v007_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_10d_v007_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_10d_v008_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_10d_v008_signal},
    "f47_roic_compounder_fin_roic_slope_pct_21d_v009_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_21d_v009_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_21d_v010_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_21d_v010_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_21d_v011_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_21d_v011_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_21d_v012_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_21d_v012_signal},
    "f47_roic_compounder_fin_roic_slope_pct_42d_v013_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_42d_v013_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_42d_v014_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_42d_v014_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_42d_v015_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_42d_v015_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_42d_v016_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_42d_v016_signal},
    "f47_roic_compounder_fin_roic_slope_pct_63d_v017_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_63d_v017_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_63d_v018_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_63d_v018_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_63d_v019_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_63d_v019_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_63d_v020_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_63d_v020_signal},
    "f47_roic_compounder_fin_roic_slope_pct_126d_v021_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_126d_v021_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_126d_v022_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_126d_v022_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_126d_v023_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_126d_v023_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_126d_v024_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_126d_v024_signal},
    "f47_roic_compounder_fin_roic_slope_pct_252d_v025_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_252d_v025_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_252d_v026_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_252d_v026_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_252d_v027_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_252d_v027_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_252d_v028_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_252d_v028_signal},
    "f47_roic_compounder_fin_roic_slope_pct_504d_v029_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_504d_v029_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_504d_v030_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_504d_v030_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_504d_v031_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_504d_v031_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_504d_v032_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_504d_v032_signal},
    "f47_roic_compounder_fin_roic_slope_pct_756d_v033_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_756d_v033_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_756d_v034_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_756d_v034_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_756d_v035_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_756d_v035_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_756d_v036_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_756d_v036_signal},
    "f47_roic_compounder_fin_roic_slope_pct_1008d_v037_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_1008d_v037_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_1008d_v038_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_1008d_v038_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_1008d_v039_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_1008d_v039_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_1008d_v040_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_1008d_v040_signal},
    "f47_roic_compounder_fin_roic_slope_pct_1260d_v041_signal": {"func": f47_roic_compounder_fin_roic_slope_pct_1260d_v041_signal},
    "f47_roic_compounder_fin_invcap_slope_pct_1260d_v042_signal": {"func": f47_roic_compounder_fin_invcap_slope_pct_1260d_v042_signal},
    "f47_roic_compounder_fin_netinc_slope_pct_1260d_v043_signal": {"func": f47_roic_compounder_fin_netinc_slope_pct_1260d_v043_signal},
    "f47_roic_compounder_fin_roic_vol_slope_pct_1260d_v044_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_pct_1260d_v044_signal},
    "f47_roic_compounder_fin_roic_jerk_5d_v045_signal": {"func": f47_roic_compounder_fin_roic_jerk_5d_v045_signal},
    "f47_roic_compounder_fin_invcap_jerk_5d_v046_signal": {"func": f47_roic_compounder_fin_invcap_jerk_5d_v046_signal},
    "f47_roic_compounder_fin_netinc_jerk_5d_v047_signal": {"func": f47_roic_compounder_fin_netinc_jerk_5d_v047_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_5d_v048_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_5d_v048_signal},
    "f47_roic_compounder_fin_roic_jerk_10d_v049_signal": {"func": f47_roic_compounder_fin_roic_jerk_10d_v049_signal},
    "f47_roic_compounder_fin_invcap_jerk_10d_v050_signal": {"func": f47_roic_compounder_fin_invcap_jerk_10d_v050_signal},
    "f47_roic_compounder_fin_netinc_jerk_10d_v051_signal": {"func": f47_roic_compounder_fin_netinc_jerk_10d_v051_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_10d_v052_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_10d_v052_signal},
    "f47_roic_compounder_fin_roic_jerk_21d_v053_signal": {"func": f47_roic_compounder_fin_roic_jerk_21d_v053_signal},
    "f47_roic_compounder_fin_invcap_jerk_21d_v054_signal": {"func": f47_roic_compounder_fin_invcap_jerk_21d_v054_signal},
    "f47_roic_compounder_fin_netinc_jerk_21d_v055_signal": {"func": f47_roic_compounder_fin_netinc_jerk_21d_v055_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_21d_v056_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_21d_v056_signal},
    "f47_roic_compounder_fin_roic_jerk_42d_v057_signal": {"func": f47_roic_compounder_fin_roic_jerk_42d_v057_signal},
    "f47_roic_compounder_fin_invcap_jerk_42d_v058_signal": {"func": f47_roic_compounder_fin_invcap_jerk_42d_v058_signal},
    "f47_roic_compounder_fin_netinc_jerk_42d_v059_signal": {"func": f47_roic_compounder_fin_netinc_jerk_42d_v059_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_42d_v060_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_42d_v060_signal},
    "f47_roic_compounder_fin_roic_jerk_63d_v061_signal": {"func": f47_roic_compounder_fin_roic_jerk_63d_v061_signal},
    "f47_roic_compounder_fin_invcap_jerk_63d_v062_signal": {"func": f47_roic_compounder_fin_invcap_jerk_63d_v062_signal},
    "f47_roic_compounder_fin_netinc_jerk_63d_v063_signal": {"func": f47_roic_compounder_fin_netinc_jerk_63d_v063_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_63d_v064_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_63d_v064_signal},
    "f47_roic_compounder_fin_roic_jerk_126d_v065_signal": {"func": f47_roic_compounder_fin_roic_jerk_126d_v065_signal},
    "f47_roic_compounder_fin_invcap_jerk_126d_v066_signal": {"func": f47_roic_compounder_fin_invcap_jerk_126d_v066_signal},
    "f47_roic_compounder_fin_netinc_jerk_126d_v067_signal": {"func": f47_roic_compounder_fin_netinc_jerk_126d_v067_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_126d_v068_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_126d_v068_signal},
    "f47_roic_compounder_fin_roic_jerk_252d_v069_signal": {"func": f47_roic_compounder_fin_roic_jerk_252d_v069_signal},
    "f47_roic_compounder_fin_invcap_jerk_252d_v070_signal": {"func": f47_roic_compounder_fin_invcap_jerk_252d_v070_signal},
    "f47_roic_compounder_fin_netinc_jerk_252d_v071_signal": {"func": f47_roic_compounder_fin_netinc_jerk_252d_v071_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_252d_v072_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_252d_v072_signal},
    "f47_roic_compounder_fin_roic_jerk_504d_v073_signal": {"func": f47_roic_compounder_fin_roic_jerk_504d_v073_signal},
    "f47_roic_compounder_fin_invcap_jerk_504d_v074_signal": {"func": f47_roic_compounder_fin_invcap_jerk_504d_v074_signal},
    "f47_roic_compounder_fin_netinc_jerk_504d_v075_signal": {"func": f47_roic_compounder_fin_netinc_jerk_504d_v075_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_504d_v076_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_504d_v076_signal},
    "f47_roic_compounder_fin_roic_jerk_756d_v077_signal": {"func": f47_roic_compounder_fin_roic_jerk_756d_v077_signal},
    "f47_roic_compounder_fin_invcap_jerk_756d_v078_signal": {"func": f47_roic_compounder_fin_invcap_jerk_756d_v078_signal},
    "f47_roic_compounder_fin_netinc_jerk_756d_v079_signal": {"func": f47_roic_compounder_fin_netinc_jerk_756d_v079_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_756d_v080_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_756d_v080_signal},
    "f47_roic_compounder_fin_roic_jerk_1008d_v081_signal": {"func": f47_roic_compounder_fin_roic_jerk_1008d_v081_signal},
    "f47_roic_compounder_fin_invcap_jerk_1008d_v082_signal": {"func": f47_roic_compounder_fin_invcap_jerk_1008d_v082_signal},
    "f47_roic_compounder_fin_netinc_jerk_1008d_v083_signal": {"func": f47_roic_compounder_fin_netinc_jerk_1008d_v083_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_1008d_v084_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_1008d_v084_signal},
    "f47_roic_compounder_fin_roic_jerk_1260d_v085_signal": {"func": f47_roic_compounder_fin_roic_jerk_1260d_v085_signal},
    "f47_roic_compounder_fin_invcap_jerk_1260d_v086_signal": {"func": f47_roic_compounder_fin_invcap_jerk_1260d_v086_signal},
    "f47_roic_compounder_fin_netinc_jerk_1260d_v087_signal": {"func": f47_roic_compounder_fin_netinc_jerk_1260d_v087_signal},
    "f47_roic_compounder_fin_roic_vol_jerk_1260d_v088_signal": {"func": f47_roic_compounder_fin_roic_vol_jerk_1260d_v088_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_5d_v089_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_5d_v089_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_5d_v090_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_5d_v090_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_5d_v091_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_5d_v091_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_5d_v092_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_5d_v092_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_10d_v093_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_10d_v093_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_10d_v094_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_10d_v094_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_10d_v095_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_10d_v095_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_10d_v096_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_10d_v096_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_21d_v097_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_21d_v097_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_21d_v098_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_21d_v098_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_21d_v099_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_21d_v099_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_21d_v100_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_21d_v100_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_42d_v101_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_42d_v101_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_42d_v102_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_42d_v102_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_42d_v103_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_42d_v103_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_42d_v104_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_42d_v104_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_63d_v105_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_63d_v105_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_63d_v106_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_63d_v106_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_63d_v107_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_63d_v107_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_63d_v108_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_63d_v108_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_126d_v109_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_126d_v109_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_126d_v110_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_126d_v110_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_126d_v111_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_126d_v111_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_126d_v112_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_126d_v112_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_252d_v113_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_252d_v113_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_252d_v114_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_252d_v114_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_252d_v115_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_252d_v115_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_252d_v116_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_252d_v116_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_504d_v117_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_504d_v117_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_504d_v118_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_504d_v118_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_504d_v119_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_504d_v119_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_504d_v120_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_504d_v120_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_756d_v121_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_756d_v121_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_756d_v122_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_756d_v122_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_756d_v123_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_756d_v123_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_756d_v124_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_756d_v124_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_1008d_v125_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_1008d_v125_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_1008d_v126_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_1008d_v126_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_1008d_v127_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_1008d_v127_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_1008d_v128_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_1008d_v128_signal},
    "f47_roic_compounder_fin_roic_slope_diff_norm_1260d_v129_signal": {"func": f47_roic_compounder_fin_roic_slope_diff_norm_1260d_v129_signal},
    "f47_roic_compounder_fin_invcap_slope_diff_norm_1260d_v130_signal": {"func": f47_roic_compounder_fin_invcap_slope_diff_norm_1260d_v130_signal},
    "f47_roic_compounder_fin_netinc_slope_diff_norm_1260d_v131_signal": {"func": f47_roic_compounder_fin_netinc_slope_diff_norm_1260d_v131_signal},
    "f47_roic_compounder_fin_roic_vol_slope_diff_norm_1260d_v132_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_diff_norm_1260d_v132_signal},
    "f47_roic_compounder_fin_roic_mom_z_5d_v133_signal": {"func": f47_roic_compounder_fin_roic_mom_z_5d_v133_signal},
    "f47_roic_compounder_fin_invcap_mom_z_5d_v134_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_5d_v134_signal},
    "f47_roic_compounder_fin_netinc_mom_z_5d_v135_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_5d_v135_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_5d_v136_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_5d_v136_signal},
    "f47_roic_compounder_fin_roic_mom_z_10d_v137_signal": {"func": f47_roic_compounder_fin_roic_mom_z_10d_v137_signal},
    "f47_roic_compounder_fin_invcap_mom_z_10d_v138_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_10d_v138_signal},
    "f47_roic_compounder_fin_netinc_mom_z_10d_v139_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_10d_v139_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_10d_v140_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_10d_v140_signal},
    "f47_roic_compounder_fin_roic_mom_z_21d_v141_signal": {"func": f47_roic_compounder_fin_roic_mom_z_21d_v141_signal},
    "f47_roic_compounder_fin_invcap_mom_z_21d_v142_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_21d_v142_signal},
    "f47_roic_compounder_fin_netinc_mom_z_21d_v143_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_21d_v143_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_21d_v144_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_21d_v144_signal},
    "f47_roic_compounder_fin_roic_mom_z_42d_v145_signal": {"func": f47_roic_compounder_fin_roic_mom_z_42d_v145_signal},
    "f47_roic_compounder_fin_invcap_mom_z_42d_v146_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_42d_v146_signal},
    "f47_roic_compounder_fin_netinc_mom_z_42d_v147_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_42d_v147_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_42d_v148_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_42d_v148_signal},
    "f47_roic_compounder_fin_roic_mom_z_63d_v149_signal": {"func": f47_roic_compounder_fin_roic_mom_z_63d_v149_signal},
    "f47_roic_compounder_fin_invcap_mom_z_63d_v150_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 47...")
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
