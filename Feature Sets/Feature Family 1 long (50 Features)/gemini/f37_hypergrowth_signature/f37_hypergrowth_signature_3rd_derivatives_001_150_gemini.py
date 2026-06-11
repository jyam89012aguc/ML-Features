import pandas as pd
import numpy as np

def _sma(s, w):
    """Simple Moving Average with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()

def _std(s, w):
    """Standard Deviation with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _z(s, w):
    """Z-score calculation."""
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _hs_growth(s, w):
    """Domain Primitive: Growth over a window."""
    return s.pct_change(w)

def _hs_consistency(s, w):
    """Domain Primitive: Consistency of growth over a window."""
    growth = s.pct_change(21)
    return _sma(growth, w) / _std(growth, w).replace(0, np.nan)

def _hs_zscore(s, w):
    """Domain Primitive: Z-score of a series."""
    return _z(s, w)

def _hs_acceleration(s, w1, w2):
    """Domain Primitive: Acceleration of growth."""
    return s.pct_change(w1).diff(w2)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j4_v001_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 1."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j5_v002_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 2."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j3_v003_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 3."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j4_v004_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 4."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j5_v005_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 5."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j3_v006_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 6."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j4_v007_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 7."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j5_v008_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 8."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j3_v009_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 9."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j4_v010_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 10."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j5_v011_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 11."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j3_v012_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 12."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j4_v013_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 13."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j5_v014_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 14."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j3_v015_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 15."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j4_v016_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 16."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j5_v017_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 17."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j3_v018_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 18."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j4_v019_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 19."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j5_v020_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 20."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j3_v021_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 21."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j4_v022_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 22."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j5_v023_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 23."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j3_v024_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 24."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j4_v025_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 25."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j5_v026_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 26."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j3_v027_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 27."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j4_v028_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 28."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j5_v029_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 29."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j3_v030_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 30."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j4_v031_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 31."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j5_v032_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 32."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j3_v033_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 33."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j4_v034_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 34."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j5_v035_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 35."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j3_v036_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 36."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j4_v037_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 37."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j5_v038_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 38."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j3_v039_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 39."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j4_v040_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 40."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j5_v041_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 41."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j3_v042_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 42."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j4_v043_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 43."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j5_v044_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 44."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j3_v045_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 45."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j4_v046_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 46."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j5_v047_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 47."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j3_v048_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 48."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j4_v049_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 49."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j5_v050_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 50."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j3_v051_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 51."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j4_v052_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 52."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j5_v053_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 53."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j3_v054_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 54."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j4_v055_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 55."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j5_v056_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 56."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j3_v057_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 57."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j4_v058_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 58."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j5_v059_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 59."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j3_v060_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 60."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j4_v061_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 61."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j5_v062_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 62."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j3_v063_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 63."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j4_v064_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 64."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j5_v065_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 65."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j3_v066_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 66."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j4_v067_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 67."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j5_v068_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 68."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j3_v069_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 69."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j4_v070_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 70."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j5_v071_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 71."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j3_v072_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 72."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j4_v073_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 73."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j5_v074_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 74."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j3_v075_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 75."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j4_v076_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 76."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j5_v077_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 77."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j3_v078_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 78."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j4_v079_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 79."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j5_v080_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 80."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j3_v081_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 81."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j4_v082_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 82."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j5_v083_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 83."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j3_v084_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 84."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j4_v085_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 85."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j5_v086_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 86."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j3_v087_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 87."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j4_v088_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 88."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j5_v089_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 89."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j3_v090_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 90."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j4_v091_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 91."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j5_v092_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 92."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j3_v093_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 93."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j4_v094_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 94."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j5_v095_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 95."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j3_v096_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 96."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j4_v097_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 97."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j5_v098_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 98."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j3_v099_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 99."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j4_v100_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 100."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j5_v101_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 101."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j3_v102_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 102."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j4_v103_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 103."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j5_v104_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 104."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j3_v105_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 105."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j4_v106_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 106."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j5_v107_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 107."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j3_v108_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 108."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j4_v109_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 109."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j5_v110_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 110."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j3_v111_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 111."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j4_v112_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 112."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j5_v113_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 113."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j3_v114_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 114."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j4_v115_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 115."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j5_v116_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 116."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j3_v117_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 117."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j4_v118_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 118."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j5_v119_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 119."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j3_v120_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 120."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j4_v121_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 121."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j5_v122_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 122."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j3_v123_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 123."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j4_v124_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 124."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j5_v125_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 125."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j3_v126_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 126."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j4_v127_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 127."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j5_v128_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 128."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j3_v129_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 129."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j4_v130_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 130."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j5_v131_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 131."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j3_v132_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 132."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j4_v133_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 133."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j5_v134_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 134."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j3_v135_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 135."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j4_v136_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 136."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j5_v137_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 137."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j3_v138_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 138."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j4_v139_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 139."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j5_v140_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 140."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w22_a6_j3_v141_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 141."""
    accel = _hs_acceleration(opinc, 22, 6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w23_a7_j4_v142_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 142."""
    accel = _hs_acceleration(revenue, 23, 7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w24_a8_j5_v143_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 143."""
    accel = _hs_acceleration(opinc, 24, 8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w25_a9_j3_v144_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 144."""
    accel = _hs_acceleration(revenue, 25, 9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w26_a5_j4_v145_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 145."""
    accel = _hs_acceleration(opinc, 26, 5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w27_a6_j5_v146_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 146."""
    accel = _hs_acceleration(revenue, 27, 6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w28_a7_j3_v147_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 147."""
    accel = _hs_acceleration(opinc, 28, 7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w29_a8_j4_v148_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 148."""
    accel = _hs_acceleration(revenue, 29, 8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_opinc_jerk_w30_a9_j5_v149_signal(opinc) -> pd.Series:
    """Jerk of hypergrowth signature. Input: opinc, Variation: 149."""
    accel = _hs_acceleration(opinc, 30, 9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_hypergrowth_signature_revenue_jerk_w21_a5_j3_v150_signal(revenue) -> pd.Series:
    """Jerk of hypergrowth signature. Input: revenue, Variation: 150."""
    accel = _hs_acceleration(revenue, 21, 5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum(),
        "opinc": np.random.normal(100, 20, n).cumsum(),
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f37_hypergrowth_signature_"))]
    
    print(f"Testing {len(funcs)} functions for f37_hypergrowth_signature...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        if len(q) == 0:
            print(f"Warning: {func.__name__} produced all NaNs in test range.")
            continue
        assert q.nunique() > 10, f"{func.__name__} has too few unique values: {q.nunique()}"

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f37_hypergrowth_signature_"))]}
F37_HYPERGROWTH_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY
