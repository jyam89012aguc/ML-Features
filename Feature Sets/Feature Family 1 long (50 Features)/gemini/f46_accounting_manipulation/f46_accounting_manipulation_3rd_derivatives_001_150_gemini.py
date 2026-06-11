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

def _am_accrual(ncfo, rev, w): return (rev - ncfo).rolling(w).mean()

def f46_accounting_manipulation_revenue_jerk_w22_a6_j4_v001_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 1. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w23_a7_j5_v002_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 2. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w24_a8_j3_v003_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 3. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w25_a9_j4_v004_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 4. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w26_a5_j5_v005_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 5. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w27_a6_j3_v006_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 6. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w28_a7_j4_v007_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 7. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w29_a8_j5_v008_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 8. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w30_a9_j3_v009_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 9. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w21_a5_j4_v010_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 10. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w22_a6_j5_v011_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 11. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w23_a7_j3_v012_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 12. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w24_a8_j4_v013_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 13. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w25_a9_j5_v014_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 14. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w26_a5_j3_v015_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 15. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w27_a6_j4_v016_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 16. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w28_a7_j5_v017_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 17. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w29_a8_j3_v018_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 18. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w30_a9_j4_v019_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 19. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w21_a5_j5_v020_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 20. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w22_a6_j3_v021_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 21. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w23_a7_j4_v022_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 22. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w24_a8_j5_v023_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 23. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w25_a9_j3_v024_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 24. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w26_a5_j4_v025_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 25. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w27_a6_j5_v026_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 26. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w28_a7_j3_v027_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 27. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w29_a8_j4_v028_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 28. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w30_a9_j5_v029_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 29. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w21_a5_j3_v030_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 30. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w22_a6_j4_v031_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 31. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w23_a7_j5_v032_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 32. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w24_a8_j3_v033_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 33. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w25_a9_j4_v034_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 34. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w26_a5_j5_v035_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 35. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w27_a6_j3_v036_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 36. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w28_a7_j4_v037_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 37. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w29_a8_j5_v038_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 38. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w30_a9_j3_v039_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 39. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w21_a5_j4_v040_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 40. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w22_a6_j5_v041_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 41. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w23_a7_j3_v042_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 42. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w24_a8_j4_v043_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 43. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w25_a9_j5_v044_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 44. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w26_a5_j3_v045_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 45. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w27_a6_j4_v046_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 46. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w28_a7_j5_v047_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 47. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w29_a8_j3_v048_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 48. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w30_a9_j4_v049_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 49. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w21_a5_j5_v050_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 50. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w22_a6_j3_v051_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 51. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w23_a7_j4_v052_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 52. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w24_a8_j5_v053_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 53. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w25_a9_j3_v054_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 54. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w26_a5_j4_v055_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 55. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w27_a6_j5_v056_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 56. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w28_a7_j3_v057_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 57. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w29_a8_j4_v058_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 58. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w30_a9_j5_v059_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 59. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w21_a5_j3_v060_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 60. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w22_a6_j4_v061_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 61. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w23_a7_j5_v062_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 62. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w24_a8_j3_v063_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 63. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w25_a9_j4_v064_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 64. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w26_a5_j5_v065_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 65. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w27_a6_j3_v066_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 66. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w28_a7_j4_v067_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 67. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w29_a8_j5_v068_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 68. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w30_a9_j3_v069_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 69. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w21_a5_j4_v070_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 70. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w22_a6_j5_v071_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 71. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w23_a7_j3_v072_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 72. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w24_a8_j4_v073_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 73. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w25_a9_j5_v074_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 74. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w26_a5_j3_v075_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 75. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w27_a6_j4_v076_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 76. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w28_a7_j5_v077_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 77. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w29_a8_j3_v078_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 78. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w30_a9_j4_v079_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 79. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w21_a5_j5_v080_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 80. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w22_a6_j3_v081_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 81. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w23_a7_j4_v082_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 82. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w24_a8_j5_v083_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 83. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w25_a9_j3_v084_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 84. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w26_a5_j4_v085_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 85. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w27_a6_j5_v086_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 86. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w28_a7_j3_v087_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 87. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w29_a8_j4_v088_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 88. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w30_a9_j5_v089_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 89. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w21_a5_j3_v090_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 90. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w22_a6_j4_v091_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 91. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w23_a7_j5_v092_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 92. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w24_a8_j3_v093_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 93. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w25_a9_j4_v094_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 94. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w26_a5_j5_v095_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 95. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w27_a6_j3_v096_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 96. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w28_a7_j4_v097_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 97. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w29_a8_j5_v098_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 98. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w30_a9_j3_v099_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 99. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w21_a5_j4_v100_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 100. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w22_a6_j5_v101_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 101. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w23_a7_j3_v102_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 102. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w24_a8_j4_v103_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 103. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w25_a9_j5_v104_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 104. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w26_a5_j3_v105_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 105. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w27_a6_j4_v106_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 106. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w28_a7_j5_v107_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 107. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w29_a8_j3_v108_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 108. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w30_a9_j4_v109_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 109. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w21_a5_j5_v110_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 110. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w22_a6_j3_v111_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 111. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w23_a7_j4_v112_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 112. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w24_a8_j5_v113_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 113. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w25_a9_j3_v114_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 114. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w26_a5_j4_v115_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 115. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w27_a6_j5_v116_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 116. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w28_a7_j3_v117_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 117. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w29_a8_j4_v118_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 118. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w30_a9_j5_v119_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 119. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w21_a5_j3_v120_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 120. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w22_a6_j4_v121_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 121. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 22)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w23_a7_j5_v122_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 122. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 23)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w24_a8_j3_v123_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 123. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 24)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w25_a9_j4_v124_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 124. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 25)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w26_a5_j5_v125_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 125. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 26)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w27_a6_j3_v126_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 126. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 27)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w28_a7_j4_v127_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 127. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 28)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w29_a8_j5_v128_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 128. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 29)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w30_a9_j3_v129_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 129. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 30)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w21_a5_j4_v130_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 130. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 21)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w22_a6_j5_v131_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 131. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 22)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w23_a7_j3_v132_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 132. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 23)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w24_a8_j4_v133_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 133. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 24)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w25_a9_j5_v134_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 134. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 25)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w26_a5_j3_v135_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 135. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 26)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w27_a6_j4_v136_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 136. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 27)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w28_a7_j5_v137_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 137. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 28)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w29_a8_j3_v138_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 138. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 29)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w30_a9_j4_v139_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 139. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 30)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w21_a5_j5_v140_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 140. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 21)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w22_a6_j3_v141_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 141. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 22)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w23_a7_j4_v142_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 142. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 23)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w24_a8_j5_v143_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 143. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 24)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w25_a9_j3_v144_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 144. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 25)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w26_a5_j4_v145_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 145. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 26)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w27_a6_j5_v146_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 146. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 27)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w28_a7_j3_v147_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 147. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 28)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_jerk_w29_a8_j4_v148_signal(revenue) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: revenue, Variation: 148. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 29)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_jerk_w30_a9_j5_v149_signal(ncfo) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: ncfo, Variation: 149. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 30)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_jerk_w21_a5_j3_v150_signal(assets) -> pd.Series:
    """Jerk feature for f46_accounting_manipulation. Input: assets, Variation: 150. Captures higher-order dynamics."""
    base = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 21)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "assets": np.random.normal(1000, 100, n).cumsum() + 1000,
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000,
        "ncfo": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f46_accounting_manipulation_"))]
    
    print(f"Testing {len(funcs)} functions for f46_accounting_manipulation...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f46_accounting_manipulation_"))]}
F46_ACCOUNTING_MANIPULATION_REGISTRY_JERK_001_150 = REGISTRY
