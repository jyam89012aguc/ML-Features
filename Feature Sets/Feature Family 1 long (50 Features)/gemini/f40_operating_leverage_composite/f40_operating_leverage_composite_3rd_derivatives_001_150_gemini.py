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

def _ol_leverage(s, w): return s.pct_change(w)

def f40_operating_leverage_composite_opinc_jerk_w22_a6_j4_v001_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 1. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w23_a7_j5_v002_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 2. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w24_a8_j3_v003_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 3. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w25_a9_j4_v004_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 4. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w26_a5_j5_v005_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 5. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w27_a6_j3_v006_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 6. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w28_a7_j4_v007_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 7. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w29_a8_j5_v008_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 8. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w30_a9_j3_v009_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 9. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w21_a5_j4_v010_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 10. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w22_a6_j5_v011_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 11. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w23_a7_j3_v012_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 12. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w24_a8_j4_v013_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 13. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w25_a9_j5_v014_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 14. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w26_a5_j3_v015_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 15. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w27_a6_j4_v016_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 16. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w28_a7_j5_v017_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 17. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w29_a8_j3_v018_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 18. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w30_a9_j4_v019_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 19. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w21_a5_j5_v020_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 20. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w22_a6_j3_v021_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 21. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w23_a7_j4_v022_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 22. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w24_a8_j5_v023_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 23. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w25_a9_j3_v024_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 24. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w26_a5_j4_v025_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 25. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w27_a6_j5_v026_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 26. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w28_a7_j3_v027_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 27. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w29_a8_j4_v028_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 28. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w30_a9_j5_v029_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 29. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w21_a5_j3_v030_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 30. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w22_a6_j4_v031_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 31. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w23_a7_j5_v032_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 32. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w24_a8_j3_v033_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 33. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w25_a9_j4_v034_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 34. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w26_a5_j5_v035_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 35. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w27_a6_j3_v036_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 36. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w28_a7_j4_v037_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 37. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w29_a8_j5_v038_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 38. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w30_a9_j3_v039_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 39. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w21_a5_j4_v040_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 40. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w22_a6_j5_v041_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 41. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w23_a7_j3_v042_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 42. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w24_a8_j4_v043_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 43. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w25_a9_j5_v044_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 44. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w26_a5_j3_v045_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 45. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w27_a6_j4_v046_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 46. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w28_a7_j5_v047_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 47. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w29_a8_j3_v048_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 48. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w30_a9_j4_v049_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 49. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w21_a5_j5_v050_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 50. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w22_a6_j3_v051_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 51. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w23_a7_j4_v052_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 52. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w24_a8_j5_v053_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 53. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w25_a9_j3_v054_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 54. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w26_a5_j4_v055_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 55. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w27_a6_j5_v056_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 56. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w28_a7_j3_v057_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 57. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w29_a8_j4_v058_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 58. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w30_a9_j5_v059_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 59. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w21_a5_j3_v060_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 60. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w22_a6_j4_v061_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 61. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w23_a7_j5_v062_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 62. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w24_a8_j3_v063_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 63. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w25_a9_j4_v064_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 64. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w26_a5_j5_v065_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 65. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w27_a6_j3_v066_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 66. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w28_a7_j4_v067_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 67. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w29_a8_j5_v068_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 68. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w30_a9_j3_v069_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 69. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w21_a5_j4_v070_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 70. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w22_a6_j5_v071_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 71. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w23_a7_j3_v072_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 72. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w24_a8_j4_v073_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 73. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w25_a9_j5_v074_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 74. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w26_a5_j3_v075_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 75. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w27_a6_j4_v076_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 76. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w28_a7_j5_v077_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 77. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w29_a8_j3_v078_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 78. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w30_a9_j4_v079_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 79. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w21_a5_j5_v080_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 80. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w22_a6_j3_v081_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 81. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w23_a7_j4_v082_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 82. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w24_a8_j5_v083_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 83. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w25_a9_j3_v084_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 84. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w26_a5_j4_v085_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 85. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w27_a6_j5_v086_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 86. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w28_a7_j3_v087_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 87. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w29_a8_j4_v088_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 88. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w30_a9_j5_v089_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 89. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w21_a5_j3_v090_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 90. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w22_a6_j4_v091_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 91. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w23_a7_j5_v092_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 92. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w24_a8_j3_v093_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 93. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w25_a9_j4_v094_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 94. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w26_a5_j5_v095_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 95. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w27_a6_j3_v096_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 96. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w28_a7_j4_v097_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 97. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w29_a8_j5_v098_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 98. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w30_a9_j3_v099_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 99. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w21_a5_j4_v100_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 100. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w22_a6_j5_v101_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 101. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w23_a7_j3_v102_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 102. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w24_a8_j4_v103_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 103. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w25_a9_j5_v104_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 104. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w26_a5_j3_v105_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 105. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w27_a6_j4_v106_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 106. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w28_a7_j5_v107_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 107. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w29_a8_j3_v108_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 108. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w30_a9_j4_v109_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 109. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w21_a5_j5_v110_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 110. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w22_a6_j3_v111_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 111. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w23_a7_j4_v112_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 112. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w24_a8_j5_v113_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 113. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w25_a9_j3_v114_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 114. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w26_a5_j4_v115_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 115. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w27_a6_j5_v116_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 116. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w28_a7_j3_v117_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 117. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w29_a8_j4_v118_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 118. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w30_a9_j5_v119_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 119. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w21_a5_j3_v120_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 120. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w22_a6_j4_v121_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 121. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w23_a7_j5_v122_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 122. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w24_a8_j3_v123_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 123. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w25_a9_j4_v124_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 124. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w26_a5_j5_v125_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 125. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w27_a6_j3_v126_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 126. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w28_a7_j4_v127_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 127. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w29_a8_j5_v128_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 128. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w30_a9_j3_v129_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 129. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w21_a5_j4_v130_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 130. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w22_a6_j5_v131_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 131. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w23_a7_j3_v132_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 132. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w24_a8_j4_v133_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 133. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w25_a9_j5_v134_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 134. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w26_a5_j3_v135_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 135. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w27_a6_j4_v136_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 136. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w28_a7_j5_v137_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 137. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w29_a8_j3_v138_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 138. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w30_a9_j4_v139_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 139. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w21_a5_j5_v140_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 140. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w22_a6_j3_v141_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 141. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w23_a7_j4_v142_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 142. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w24_a8_j5_v143_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 143. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w25_a9_j3_v144_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 144. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w26_a5_j4_v145_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 145. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w27_a6_j5_v146_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 146. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w28_a7_j3_v147_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 147. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_jerk_w29_a8_j4_v148_signal(opinc) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: opinc, Variation: 148. Captures higher-order dynamics."""
    base = _ol_leverage(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_jerk_w30_a9_j5_v149_signal(sga) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: sga, Variation: 149. Captures higher-order dynamics."""
    base = _ol_leverage(sga, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_jerk_w21_a5_j3_v150_signal(revenue) -> pd.Series:
    """Jerk feature for f40_operating_leverage_composite. Input: revenue, Variation: 150. Captures higher-order dynamics."""
    base = _ol_leverage(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000,
        "opinc": np.random.normal(1000, 100, n).cumsum() + 1000,
        "sga": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f40_operating_leverage_composite_"))]
    
    print(f"Testing {len(funcs)} functions for f40_operating_leverage_composite...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        if len(q) == 0:
            continue
        assert q.nunique() > 10, f"{func.__name__} has too few unique values: {q.nunique()}"

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f40_operating_leverage_composite_"))]}
F40_OPERATING_LEVERAGE_COMPOSITE_REGISTRY_JERK_001_150 = REGISTRY
