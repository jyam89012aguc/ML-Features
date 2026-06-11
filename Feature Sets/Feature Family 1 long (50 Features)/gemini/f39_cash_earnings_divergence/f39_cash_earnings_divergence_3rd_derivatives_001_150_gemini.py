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

def _ce_div(s1, s2, w): return (s1 - s2).rolling(w).mean()

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j4_v001_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 1. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j5_v002_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 2. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j3_v003_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 3. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j4_v004_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 4. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j5_v005_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 5. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j3_v006_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 6. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j4_v007_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 7. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j5_v008_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 8. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j3_v009_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 9. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j4_v010_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 10. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j5_v011_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 11. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j3_v012_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 12. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j4_v013_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 13. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j5_v014_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 14. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j3_v015_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 15. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j4_v016_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 16. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j5_v017_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 17. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j3_v018_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 18. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j4_v019_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 19. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j5_v020_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 20. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j3_v021_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 21. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j4_v022_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 22. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j5_v023_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 23. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j3_v024_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 24. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j4_v025_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 25. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j5_v026_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 26. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j3_v027_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 27. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j4_v028_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 28. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j5_v029_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 29. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j3_v030_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 30. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j4_v031_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 31. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j5_v032_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 32. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j3_v033_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 33. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j4_v034_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 34. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j5_v035_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 35. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j3_v036_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 36. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j4_v037_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 37. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j5_v038_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 38. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j3_v039_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 39. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j4_v040_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 40. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j5_v041_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 41. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j3_v042_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 42. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j4_v043_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 43. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j5_v044_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 44. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j3_v045_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 45. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j4_v046_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 46. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j5_v047_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 47. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j3_v048_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 48. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j4_v049_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 49. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j5_v050_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 50. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j3_v051_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 51. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j4_v052_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 52. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j5_v053_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 53. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j3_v054_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 54. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j4_v055_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 55. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j5_v056_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 56. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j3_v057_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 57. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j4_v058_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 58. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j5_v059_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 59. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j3_v060_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 60. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j4_v061_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 61. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j5_v062_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 62. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j3_v063_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 63. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j4_v064_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 64. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j5_v065_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 65. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j3_v066_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 66. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j4_v067_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 67. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j5_v068_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 68. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j3_v069_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 69. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j4_v070_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 70. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j5_v071_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 71. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j3_v072_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 72. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j4_v073_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 73. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j5_v074_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 74. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j3_v075_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 75. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j4_v076_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 76. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j5_v077_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 77. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j3_v078_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 78. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j4_v079_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 79. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j5_v080_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 80. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j3_v081_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 81. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j4_v082_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 82. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j5_v083_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 83. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j3_v084_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 84. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j4_v085_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 85. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j5_v086_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 86. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j3_v087_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 87. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j4_v088_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 88. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j5_v089_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 89. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j3_v090_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 90. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j4_v091_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 91. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j5_v092_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 92. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j3_v093_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 93. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j4_v094_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 94. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j5_v095_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 95. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j3_v096_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 96. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j4_v097_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 97. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j5_v098_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 98. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j3_v099_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 99. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j4_v100_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 100. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j5_v101_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 101. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j3_v102_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 102. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j4_v103_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 103. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j5_v104_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 104. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j3_v105_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 105. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j4_v106_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 106. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j5_v107_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 107. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j3_v108_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 108. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j4_v109_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 109. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j5_v110_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 110. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j3_v111_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 111. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j4_v112_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 112. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j5_v113_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 113. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j3_v114_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 114. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j4_v115_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 115. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j5_v116_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 116. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j3_v117_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 117. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j4_v118_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 118. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j5_v119_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 119. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j3_v120_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 120. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j4_v121_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 121. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j5_v122_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 122. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j3_v123_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 123. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j4_v124_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 124. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j5_v125_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 125. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j3_v126_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 126. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j4_v127_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 127. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j5_v128_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 128. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j3_v129_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 129. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j4_v130_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 130. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j5_v131_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 131. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j3_v132_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 132. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j4_v133_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 133. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j5_v134_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 134. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j3_v135_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 135. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j4_v136_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 136. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j5_v137_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 137. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j3_v138_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 138. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j4_v139_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 139. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j5_v140_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 140. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w22_a6_j3_v141_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 141. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w23_a7_j4_v142_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 142. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w24_a8_j5_v143_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 143. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w25_a9_j3_v144_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 144. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w26_a5_j4_v145_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 145. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w27_a6_j5_v146_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 146. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w28_a7_j3_v147_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 147. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w29_a8_j4_v148_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 148. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_jerk_w30_a9_j5_v149_signal(ncfo) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 149. Captures higher-order dynamics."""
    base = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_jerk_w21_a5_j3_v150_signal(ni) -> pd.Series:
    """Jerk feature for f39_cash_earnings_divergence. Input: ni, Variation: 150. Captures higher-order dynamics."""
    base = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "ni": np.random.normal(1000, 100, n).cumsum() + 1000,
        "ncfo": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f39_cash_earnings_divergence_"))]
    
    print(f"Testing {len(funcs)} functions for f39_cash_earnings_divergence...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f39_cash_earnings_divergence_"))]}
F39_CASH_EARNINGS_DIVERGENCE_REGISTRY_JERK_001_150 = REGISTRY
