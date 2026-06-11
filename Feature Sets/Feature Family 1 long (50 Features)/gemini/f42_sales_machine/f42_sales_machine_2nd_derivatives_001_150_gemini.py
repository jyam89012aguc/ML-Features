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

def _sm_efficiency(rev, sga, w): return rev.pct_change(w) / sga.pct_change(w).replace(0, np.nan)

def f42_sales_machine_revenue_slope_w22_s6_v001_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 1. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 22)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w23_s7_v002_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 2. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 23)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w24_s8_v003_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 3. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 24)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w25_s9_v004_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 4. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 25)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w26_s10_v005_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 5. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 26)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w27_s11_v006_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 6. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 27)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w28_s12_v007_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 7. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 28)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w29_s13_v008_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 8. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 29)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w30_s14_v009_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 9. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 30)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w31_s5_v010_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 10. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 31)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w32_s6_v011_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 11. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 32)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w33_s7_v012_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 12. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 33)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w34_s8_v013_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 13. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 34)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w35_s9_v014_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 14. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 35)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w36_s10_v015_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 15. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 36)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w37_s11_v016_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 16. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 37)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w38_s12_v017_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 17. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 38)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w39_s13_v018_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 18. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 39)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w40_s14_v019_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 19. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 40)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w41_s5_v020_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 20. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 41)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w21_s6_v021_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 21. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 21)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w22_s7_v022_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 22. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 22)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w23_s8_v023_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 23. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 23)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w24_s9_v024_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 24. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 24)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w25_s10_v025_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 25. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 25)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w26_s11_v026_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 26. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 26)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w27_s12_v027_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 27. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 27)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w28_s13_v028_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 28. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 28)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w29_s14_v029_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 29. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 29)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w30_s5_v030_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 30. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 30)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w31_s6_v031_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 31. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 31)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w32_s7_v032_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 32. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 32)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w33_s8_v033_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 33. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 33)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w34_s9_v034_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 34. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 34)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w35_s10_v035_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 35. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 35)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w36_s11_v036_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 36. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 36)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w37_s12_v037_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 37. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 37)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w38_s13_v038_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 38. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 38)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w39_s14_v039_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 39. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 39)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w40_s5_v040_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 40. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 40)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w41_s6_v041_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 41. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 41)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w21_s7_v042_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 42. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 21)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w22_s8_v043_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 43. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 22)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w23_s9_v044_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 44. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 23)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w24_s10_v045_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 45. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 24)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w25_s11_v046_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 46. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 25)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w26_s12_v047_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 47. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 26)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w27_s13_v048_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 48. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 27)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w28_s14_v049_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 49. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 28)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w29_s5_v050_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 50. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 29)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w30_s6_v051_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 51. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 30)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w31_s7_v052_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 52. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 31)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w32_s8_v053_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 53. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 32)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w33_s9_v054_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 54. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 33)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w34_s10_v055_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 55. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 34)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w35_s11_v056_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 56. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 35)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w36_s12_v057_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 57. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 36)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w37_s13_v058_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 58. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 37)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w38_s14_v059_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 59. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 38)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w39_s5_v060_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 60. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 39)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w40_s6_v061_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 61. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 40)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w41_s7_v062_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 62. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 41)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w21_s8_v063_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 63. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 21)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w22_s9_v064_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 64. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 22)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w23_s10_v065_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 65. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 23)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w24_s11_v066_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 66. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 24)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w25_s12_v067_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 67. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 25)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w26_s13_v068_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 68. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 26)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w27_s14_v069_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 69. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 27)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w28_s5_v070_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 70. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 28)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w29_s6_v071_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 71. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 29)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w30_s7_v072_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 72. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 30)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w31_s8_v073_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 73. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 31)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w32_s9_v074_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 74. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 32)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w33_s10_v075_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 75. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 33)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w34_s11_v076_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 76. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 34)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w35_s12_v077_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 77. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 35)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w36_s13_v078_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 78. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 36)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w37_s14_v079_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 79. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 37)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w38_s5_v080_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 80. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 38)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w39_s6_v081_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 81. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 39)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w40_s7_v082_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 82. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 40)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w41_s8_v083_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 83. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 41)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w21_s9_v084_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 84. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 21)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w22_s10_v085_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 85. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 22)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w23_s11_v086_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 86. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 23)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w24_s12_v087_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 87. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 24)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w25_s13_v088_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 88. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 25)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w26_s14_v089_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 89. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 26)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w27_s5_v090_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 90. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 27)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w28_s6_v091_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 91. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 28)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w29_s7_v092_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 92. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 29)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w30_s8_v093_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 93. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 30)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w31_s9_v094_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 94. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 31)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w32_s10_v095_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 95. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 32)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w33_s11_v096_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 96. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 33)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w34_s12_v097_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 97. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 34)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w35_s13_v098_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 98. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 35)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w36_s14_v099_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 99. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 36)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w37_s5_v100_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 100. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 37)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w38_s6_v101_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 101. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 38)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w39_s7_v102_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 102. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 39)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w40_s8_v103_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 103. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 40)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w41_s9_v104_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 104. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 41)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w21_s10_v105_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 105. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 21)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w22_s11_v106_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 106. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 22)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w23_s12_v107_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 107. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 23)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w24_s13_v108_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 108. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 24)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w25_s14_v109_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 109. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 25)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w26_s5_v110_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 110. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 26)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w27_s6_v111_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 111. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 27)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w28_s7_v112_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 112. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 28)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w29_s8_v113_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 113. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 29)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w30_s9_v114_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 114. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 30)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w31_s10_v115_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 115. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 31)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w32_s11_v116_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 116. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 32)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w33_s12_v117_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 117. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 33)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w34_s13_v118_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 118. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 34)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w35_s14_v119_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 119. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 35)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w36_s5_v120_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 120. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 36)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w37_s6_v121_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 121. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 37)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w38_s7_v122_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 122. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 38)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w39_s8_v123_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 123. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 39)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w40_s9_v124_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 124. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 40)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w41_s10_v125_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 125. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 41)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w21_s11_v126_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 126. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 21)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w22_s12_v127_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 127. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 22)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w23_s13_v128_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 128. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 23)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w24_s14_v129_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 129. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 24)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w25_s5_v130_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 130. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 25)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w26_s6_v131_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 131. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 26)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w27_s7_v132_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 132. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 27)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w28_s8_v133_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 133. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 28)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w29_s9_v134_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 134. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 29)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w30_s10_v135_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 135. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 30)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w31_s11_v136_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 136. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 31)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w32_s12_v137_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 137. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 32)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w33_s13_v138_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 138. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 33)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w34_s14_v139_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 139. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 34)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w35_s5_v140_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 140. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 35)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w36_s6_v141_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 141. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 36)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w37_s7_v142_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 142. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 37)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w38_s8_v143_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 143. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 38)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w39_s9_v144_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 144. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 39)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w40_s10_v145_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 145. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 40)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w41_s11_v146_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 146. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 41)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w21_s12_v147_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 147. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 21)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w22_s13_v148_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 148. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 22)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_slope_w23_s14_v149_signal(revenue) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: revenue, Variation: 149. Captures rate of change."""
    base = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 23)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_slope_w24_s5_v150_signal(sga) -> pd.Series:
    """Slope feature for f42_sales_machine. Input: sga, Variation: 150. Captures rate of change."""
    base = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 24)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "sga": np.random.normal(1000, 100, n).cumsum() + 1000,
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f42_sales_machine_"))]
    
    print(f"Testing {len(funcs)} functions for f42_sales_machine...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f42_sales_machine_"))]}
F42_SALES_MACHINE_REGISTRY_SLOPE_001_150 = REGISTRY
