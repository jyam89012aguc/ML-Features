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

def _mt_trend(s, w): return s / _sma(s, w)

def f43_moat_trajectory_opinc_jerk_w22_a6_j4_v001_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 1. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w23_a7_j5_v002_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 2. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w24_a8_j3_v003_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 3. Captures higher-order dynamics."""
    base = _mt_trend(gp, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w25_a9_j4_v004_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 4. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w26_a5_j5_v005_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 5. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w27_a6_j3_v006_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 6. Captures higher-order dynamics."""
    base = _mt_trend(gp, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w28_a7_j4_v007_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 7. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w29_a8_j5_v008_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 8. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w30_a9_j3_v009_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 9. Captures higher-order dynamics."""
    base = _mt_trend(gp, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w21_a5_j4_v010_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 10. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w22_a6_j5_v011_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 11. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w23_a7_j3_v012_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 12. Captures higher-order dynamics."""
    base = _mt_trend(gp, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w24_a8_j4_v013_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 13. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w25_a9_j5_v014_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 14. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w26_a5_j3_v015_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 15. Captures higher-order dynamics."""
    base = _mt_trend(gp, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w27_a6_j4_v016_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 16. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w28_a7_j5_v017_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 17. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w29_a8_j3_v018_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 18. Captures higher-order dynamics."""
    base = _mt_trend(gp, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w30_a9_j4_v019_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 19. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w21_a5_j5_v020_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 20. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w22_a6_j3_v021_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 21. Captures higher-order dynamics."""
    base = _mt_trend(gp, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w23_a7_j4_v022_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 22. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w24_a8_j5_v023_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 23. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w25_a9_j3_v024_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 24. Captures higher-order dynamics."""
    base = _mt_trend(gp, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w26_a5_j4_v025_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 25. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w27_a6_j5_v026_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 26. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w28_a7_j3_v027_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 27. Captures higher-order dynamics."""
    base = _mt_trend(gp, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w29_a8_j4_v028_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 28. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w30_a9_j5_v029_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 29. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w21_a5_j3_v030_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 30. Captures higher-order dynamics."""
    base = _mt_trend(gp, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w22_a6_j4_v031_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 31. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w23_a7_j5_v032_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 32. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w24_a8_j3_v033_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 33. Captures higher-order dynamics."""
    base = _mt_trend(gp, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w25_a9_j4_v034_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 34. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w26_a5_j5_v035_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 35. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w27_a6_j3_v036_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 36. Captures higher-order dynamics."""
    base = _mt_trend(gp, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w28_a7_j4_v037_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 37. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w29_a8_j5_v038_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 38. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w30_a9_j3_v039_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 39. Captures higher-order dynamics."""
    base = _mt_trend(gp, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w21_a5_j4_v040_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 40. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w22_a6_j5_v041_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 41. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w23_a7_j3_v042_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 42. Captures higher-order dynamics."""
    base = _mt_trend(gp, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w24_a8_j4_v043_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 43. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w25_a9_j5_v044_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 44. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w26_a5_j3_v045_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 45. Captures higher-order dynamics."""
    base = _mt_trend(gp, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w27_a6_j4_v046_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 46. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w28_a7_j5_v047_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 47. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w29_a8_j3_v048_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 48. Captures higher-order dynamics."""
    base = _mt_trend(gp, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w30_a9_j4_v049_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 49. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w21_a5_j5_v050_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 50. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w22_a6_j3_v051_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 51. Captures higher-order dynamics."""
    base = _mt_trend(gp, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w23_a7_j4_v052_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 52. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w24_a8_j5_v053_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 53. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w25_a9_j3_v054_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 54. Captures higher-order dynamics."""
    base = _mt_trend(gp, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w26_a5_j4_v055_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 55. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w27_a6_j5_v056_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 56. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w28_a7_j3_v057_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 57. Captures higher-order dynamics."""
    base = _mt_trend(gp, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w29_a8_j4_v058_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 58. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w30_a9_j5_v059_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 59. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w21_a5_j3_v060_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 60. Captures higher-order dynamics."""
    base = _mt_trend(gp, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w22_a6_j4_v061_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 61. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w23_a7_j5_v062_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 62. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w24_a8_j3_v063_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 63. Captures higher-order dynamics."""
    base = _mt_trend(gp, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w25_a9_j4_v064_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 64. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w26_a5_j5_v065_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 65. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w27_a6_j3_v066_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 66. Captures higher-order dynamics."""
    base = _mt_trend(gp, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w28_a7_j4_v067_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 67. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w29_a8_j5_v068_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 68. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w30_a9_j3_v069_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 69. Captures higher-order dynamics."""
    base = _mt_trend(gp, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w21_a5_j4_v070_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 70. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w22_a6_j5_v071_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 71. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w23_a7_j3_v072_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 72. Captures higher-order dynamics."""
    base = _mt_trend(gp, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w24_a8_j4_v073_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 73. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w25_a9_j5_v074_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 74. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w26_a5_j3_v075_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 75. Captures higher-order dynamics."""
    base = _mt_trend(gp, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w27_a6_j4_v076_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 76. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w28_a7_j5_v077_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 77. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w29_a8_j3_v078_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 78. Captures higher-order dynamics."""
    base = _mt_trend(gp, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w30_a9_j4_v079_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 79. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w21_a5_j5_v080_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 80. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w22_a6_j3_v081_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 81. Captures higher-order dynamics."""
    base = _mt_trend(gp, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w23_a7_j4_v082_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 82. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w24_a8_j5_v083_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 83. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w25_a9_j3_v084_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 84. Captures higher-order dynamics."""
    base = _mt_trend(gp, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w26_a5_j4_v085_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 85. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w27_a6_j5_v086_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 86. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w28_a7_j3_v087_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 87. Captures higher-order dynamics."""
    base = _mt_trend(gp, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w29_a8_j4_v088_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 88. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w30_a9_j5_v089_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 89. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w21_a5_j3_v090_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 90. Captures higher-order dynamics."""
    base = _mt_trend(gp, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w22_a6_j4_v091_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 91. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w23_a7_j5_v092_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 92. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w24_a8_j3_v093_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 93. Captures higher-order dynamics."""
    base = _mt_trend(gp, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w25_a9_j4_v094_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 94. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w26_a5_j5_v095_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 95. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w27_a6_j3_v096_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 96. Captures higher-order dynamics."""
    base = _mt_trend(gp, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w28_a7_j4_v097_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 97. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w29_a8_j5_v098_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 98. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w30_a9_j3_v099_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 99. Captures higher-order dynamics."""
    base = _mt_trend(gp, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w21_a5_j4_v100_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 100. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w22_a6_j5_v101_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 101. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w23_a7_j3_v102_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 102. Captures higher-order dynamics."""
    base = _mt_trend(gp, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w24_a8_j4_v103_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 103. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w25_a9_j5_v104_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 104. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w26_a5_j3_v105_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 105. Captures higher-order dynamics."""
    base = _mt_trend(gp, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w27_a6_j4_v106_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 106. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w28_a7_j5_v107_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 107. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w29_a8_j3_v108_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 108. Captures higher-order dynamics."""
    base = _mt_trend(gp, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w30_a9_j4_v109_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 109. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w21_a5_j5_v110_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 110. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w22_a6_j3_v111_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 111. Captures higher-order dynamics."""
    base = _mt_trend(gp, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w23_a7_j4_v112_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 112. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w24_a8_j5_v113_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 113. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w25_a9_j3_v114_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 114. Captures higher-order dynamics."""
    base = _mt_trend(gp, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w26_a5_j4_v115_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 115. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w27_a6_j5_v116_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 116. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w28_a7_j3_v117_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 117. Captures higher-order dynamics."""
    base = _mt_trend(gp, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w29_a8_j4_v118_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 118. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w30_a9_j5_v119_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 119. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w21_a5_j3_v120_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 120. Captures higher-order dynamics."""
    base = _mt_trend(gp, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w22_a6_j4_v121_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 121. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w23_a7_j5_v122_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 122. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w24_a8_j3_v123_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 123. Captures higher-order dynamics."""
    base = _mt_trend(gp, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w25_a9_j4_v124_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 124. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w26_a5_j5_v125_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 125. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w27_a6_j3_v126_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 126. Captures higher-order dynamics."""
    base = _mt_trend(gp, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w28_a7_j4_v127_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 127. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w29_a8_j5_v128_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 128. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w30_a9_j3_v129_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 129. Captures higher-order dynamics."""
    base = _mt_trend(gp, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w21_a5_j4_v130_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 130. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w22_a6_j5_v131_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 131. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w23_a7_j3_v132_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 132. Captures higher-order dynamics."""
    base = _mt_trend(gp, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w24_a8_j4_v133_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 133. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w25_a9_j5_v134_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 134. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w26_a5_j3_v135_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 135. Captures higher-order dynamics."""
    base = _mt_trend(gp, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w27_a6_j4_v136_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 136. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w28_a7_j5_v137_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 137. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w29_a8_j3_v138_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 138. Captures higher-order dynamics."""
    base = _mt_trend(gp, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w30_a9_j4_v139_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 139. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w21_a5_j5_v140_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 140. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w22_a6_j3_v141_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 141. Captures higher-order dynamics."""
    base = _mt_trend(gp, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w23_a7_j4_v142_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 142. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w24_a8_j5_v143_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 143. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w25_a9_j3_v144_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 144. Captures higher-order dynamics."""
    base = _mt_trend(gp, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w26_a5_j4_v145_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 145. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w27_a6_j5_v146_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 146. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w28_a7_j3_v147_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 147. Captures higher-order dynamics."""
    base = _mt_trend(gp, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_opinc_jerk_w29_a8_j4_v148_signal(opinc) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: opinc, Variation: 148. Captures higher-order dynamics."""
    base = _mt_trend(opinc, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_revenue_jerk_w30_a9_j5_v149_signal(revenue) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: revenue, Variation: 149. Captures higher-order dynamics."""
    base = _mt_trend(revenue, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_moat_trajectory_gp_jerk_w21_a5_j3_v150_signal(gp) -> pd.Series:
    """Jerk feature for f43_moat_trajectory. Input: gp, Variation: 150. Captures higher-order dynamics."""
    base = _mt_trend(gp, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "gp": np.random.normal(1000, 100, n).cumsum() + 1000,
        "opinc": np.random.normal(1000, 100, n).cumsum() + 1000,
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f43_moat_trajectory_"))]
    
    print(f"Testing {len(funcs)} functions for f43_moat_trajectory...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f43_moat_trajectory_"))]}
F43_MOAT_TRAJECTORY_REGISTRY_JERK_001_150 = REGISTRY
