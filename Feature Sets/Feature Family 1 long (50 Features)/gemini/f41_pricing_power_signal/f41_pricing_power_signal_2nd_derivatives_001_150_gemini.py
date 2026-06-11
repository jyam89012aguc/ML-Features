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

def _pp_margin(gp, rev): return gp / rev.replace(0, np.nan)

def f41_pricing_power_signal_gp_slope_w22_s6_v001_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 1. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w23_s7_v002_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 2. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w24_s8_v003_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 3. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w25_s9_v004_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 4. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w26_s10_v005_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 5. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w27_s11_v006_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 6. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w28_s12_v007_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 7. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w29_s13_v008_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 8. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w30_s14_v009_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 9. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w31_s5_v010_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 10. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w32_s6_v011_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 11. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w33_s7_v012_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 12. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w34_s8_v013_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 13. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w35_s9_v014_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 14. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w36_s10_v015_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 15. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w37_s11_v016_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 16. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w38_s12_v017_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 17. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w39_s13_v018_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 18. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w40_s14_v019_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 19. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w41_s5_v020_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 20. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w21_s6_v021_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 21. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w22_s7_v022_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 22. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w23_s8_v023_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 23. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w24_s9_v024_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 24. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w25_s10_v025_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 25. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w26_s11_v026_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 26. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w27_s12_v027_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 27. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w28_s13_v028_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 28. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w29_s14_v029_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 29. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w30_s5_v030_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 30. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w31_s6_v031_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 31. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w32_s7_v032_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 32. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w33_s8_v033_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 33. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w34_s9_v034_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 34. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w35_s10_v035_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 35. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w36_s11_v036_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 36. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w37_s12_v037_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 37. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w38_s13_v038_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 38. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w39_s14_v039_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 39. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w40_s5_v040_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 40. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w41_s6_v041_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 41. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w21_s7_v042_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 42. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w22_s8_v043_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 43. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w23_s9_v044_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 44. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w24_s10_v045_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 45. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w25_s11_v046_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 46. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w26_s12_v047_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 47. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w27_s13_v048_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 48. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w28_s14_v049_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 49. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w29_s5_v050_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 50. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w30_s6_v051_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 51. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w31_s7_v052_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 52. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w32_s8_v053_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 53. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w33_s9_v054_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 54. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w34_s10_v055_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 55. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w35_s11_v056_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 56. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w36_s12_v057_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 57. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w37_s13_v058_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 58. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w38_s14_v059_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 59. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w39_s5_v060_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 60. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w40_s6_v061_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 61. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w41_s7_v062_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 62. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w21_s8_v063_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 63. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w22_s9_v064_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 64. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w23_s10_v065_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 65. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w24_s11_v066_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 66. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w25_s12_v067_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 67. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w26_s13_v068_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 68. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w27_s14_v069_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 69. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w28_s5_v070_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 70. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w29_s6_v071_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 71. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w30_s7_v072_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 72. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w31_s8_v073_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 73. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w32_s9_v074_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 74. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w33_s10_v075_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 75. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w34_s11_v076_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 76. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w35_s12_v077_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 77. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w36_s13_v078_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 78. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w37_s14_v079_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 79. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w38_s5_v080_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 80. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w39_s6_v081_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 81. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w40_s7_v082_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 82. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w41_s8_v083_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 83. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w21_s9_v084_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 84. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w22_s10_v085_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 85. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w23_s11_v086_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 86. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w24_s12_v087_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 87. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w25_s13_v088_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 88. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w26_s14_v089_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 89. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w27_s5_v090_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 90. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w28_s6_v091_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 91. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w29_s7_v092_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 92. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w30_s8_v093_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 93. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w31_s9_v094_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 94. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w32_s10_v095_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 95. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w33_s11_v096_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 96. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w34_s12_v097_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 97. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w35_s13_v098_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 98. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w36_s14_v099_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 99. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w37_s5_v100_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 100. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w38_s6_v101_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 101. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w39_s7_v102_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 102. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w40_s8_v103_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 103. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w41_s9_v104_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 104. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w21_s10_v105_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 105. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w22_s11_v106_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 106. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w23_s12_v107_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 107. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w24_s13_v108_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 108. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w25_s14_v109_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 109. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w26_s5_v110_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 110. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w27_s6_v111_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 111. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w28_s7_v112_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 112. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w29_s8_v113_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 113. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w30_s9_v114_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 114. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w31_s10_v115_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 115. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w32_s11_v116_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 116. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w33_s12_v117_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 117. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w34_s13_v118_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 118. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w35_s14_v119_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 119. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w36_s5_v120_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 120. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w37_s6_v121_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 121. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w38_s7_v122_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 122. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w39_s8_v123_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 123. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w40_s9_v124_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 124. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w41_s10_v125_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 125. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w21_s11_v126_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 126. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w22_s12_v127_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 127. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w23_s13_v128_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 128. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w24_s14_v129_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 129. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w25_s5_v130_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 130. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w26_s6_v131_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 131. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w27_s7_v132_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 132. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w28_s8_v133_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 133. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w29_s9_v134_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 134. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w30_s10_v135_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 135. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w31_s11_v136_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 136. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w32_s12_v137_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 137. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w33_s13_v138_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 138. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w34_s14_v139_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 139. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w35_s5_v140_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 140. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w36_s6_v141_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 141. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w37_s7_v142_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 142. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w38_s8_v143_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 143. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w39_s9_v144_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 144. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w40_s10_v145_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 145. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w41_s11_v146_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 146. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w21_s12_v147_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 147. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w22_s13_v148_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 148. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_gp_slope_w23_s14_v149_signal(gp) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: gp, Variation: 149. Captures rate of change."""
    base = _pp_margin(gp, revenue if 'gp' == 'gp' else gp)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_pricing_power_signal_revenue_slope_w24_s5_v150_signal(revenue) -> pd.Series:
    """Slope feature for f41_pricing_power_signal. Input: revenue, Variation: 150. Captures rate of change."""
    base = _pp_margin(revenue, revenue if 'revenue' == 'gp' else gp)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000,
        "gp": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f41_pricing_power_signal_"))]
    
    print(f"Testing {len(funcs)} functions for f41_pricing_power_signal...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f41_pricing_power_signal_"))]}
F41_PRICING_POWER_SIGNAL_REGISTRY_SLOPE_001_150 = REGISTRY
