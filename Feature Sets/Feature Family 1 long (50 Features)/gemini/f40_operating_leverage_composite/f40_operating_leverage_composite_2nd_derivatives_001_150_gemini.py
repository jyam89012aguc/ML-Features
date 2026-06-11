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

def f40_operating_leverage_composite_opinc_slope_w22_s6_v001_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 1. Captures rate of change."""
    base = _ol_leverage(opinc, 22)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w23_s7_v002_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 2. Captures rate of change."""
    base = _ol_leverage(sga, 23)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w24_s8_v003_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 3. Captures rate of change."""
    base = _ol_leverage(revenue, 24)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w25_s9_v004_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 4. Captures rate of change."""
    base = _ol_leverage(opinc, 25)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w26_s10_v005_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 5. Captures rate of change."""
    base = _ol_leverage(sga, 26)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w27_s11_v006_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 6. Captures rate of change."""
    base = _ol_leverage(revenue, 27)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w28_s12_v007_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 7. Captures rate of change."""
    base = _ol_leverage(opinc, 28)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w29_s13_v008_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 8. Captures rate of change."""
    base = _ol_leverage(sga, 29)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w30_s14_v009_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 9. Captures rate of change."""
    base = _ol_leverage(revenue, 30)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w31_s5_v010_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 10. Captures rate of change."""
    base = _ol_leverage(opinc, 31)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w32_s6_v011_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 11. Captures rate of change."""
    base = _ol_leverage(sga, 32)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w33_s7_v012_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 12. Captures rate of change."""
    base = _ol_leverage(revenue, 33)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w34_s8_v013_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 13. Captures rate of change."""
    base = _ol_leverage(opinc, 34)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w35_s9_v014_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 14. Captures rate of change."""
    base = _ol_leverage(sga, 35)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w36_s10_v015_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 15. Captures rate of change."""
    base = _ol_leverage(revenue, 36)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w37_s11_v016_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 16. Captures rate of change."""
    base = _ol_leverage(opinc, 37)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w38_s12_v017_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 17. Captures rate of change."""
    base = _ol_leverage(sga, 38)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w39_s13_v018_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 18. Captures rate of change."""
    base = _ol_leverage(revenue, 39)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w40_s14_v019_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 19. Captures rate of change."""
    base = _ol_leverage(opinc, 40)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w41_s5_v020_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 20. Captures rate of change."""
    base = _ol_leverage(sga, 41)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w21_s6_v021_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 21. Captures rate of change."""
    base = _ol_leverage(revenue, 21)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w22_s7_v022_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 22. Captures rate of change."""
    base = _ol_leverage(opinc, 22)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w23_s8_v023_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 23. Captures rate of change."""
    base = _ol_leverage(sga, 23)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w24_s9_v024_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 24. Captures rate of change."""
    base = _ol_leverage(revenue, 24)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w25_s10_v025_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 25. Captures rate of change."""
    base = _ol_leverage(opinc, 25)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w26_s11_v026_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 26. Captures rate of change."""
    base = _ol_leverage(sga, 26)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w27_s12_v027_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 27. Captures rate of change."""
    base = _ol_leverage(revenue, 27)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w28_s13_v028_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 28. Captures rate of change."""
    base = _ol_leverage(opinc, 28)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w29_s14_v029_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 29. Captures rate of change."""
    base = _ol_leverage(sga, 29)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w30_s5_v030_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 30. Captures rate of change."""
    base = _ol_leverage(revenue, 30)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w31_s6_v031_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 31. Captures rate of change."""
    base = _ol_leverage(opinc, 31)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w32_s7_v032_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 32. Captures rate of change."""
    base = _ol_leverage(sga, 32)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w33_s8_v033_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 33. Captures rate of change."""
    base = _ol_leverage(revenue, 33)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w34_s9_v034_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 34. Captures rate of change."""
    base = _ol_leverage(opinc, 34)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w35_s10_v035_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 35. Captures rate of change."""
    base = _ol_leverage(sga, 35)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w36_s11_v036_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 36. Captures rate of change."""
    base = _ol_leverage(revenue, 36)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w37_s12_v037_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 37. Captures rate of change."""
    base = _ol_leverage(opinc, 37)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w38_s13_v038_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 38. Captures rate of change."""
    base = _ol_leverage(sga, 38)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w39_s14_v039_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 39. Captures rate of change."""
    base = _ol_leverage(revenue, 39)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w40_s5_v040_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 40. Captures rate of change."""
    base = _ol_leverage(opinc, 40)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w41_s6_v041_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 41. Captures rate of change."""
    base = _ol_leverage(sga, 41)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w21_s7_v042_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 42. Captures rate of change."""
    base = _ol_leverage(revenue, 21)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w22_s8_v043_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 43. Captures rate of change."""
    base = _ol_leverage(opinc, 22)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w23_s9_v044_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 44. Captures rate of change."""
    base = _ol_leverage(sga, 23)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w24_s10_v045_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 45. Captures rate of change."""
    base = _ol_leverage(revenue, 24)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w25_s11_v046_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 46. Captures rate of change."""
    base = _ol_leverage(opinc, 25)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w26_s12_v047_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 47. Captures rate of change."""
    base = _ol_leverage(sga, 26)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w27_s13_v048_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 48. Captures rate of change."""
    base = _ol_leverage(revenue, 27)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w28_s14_v049_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 49. Captures rate of change."""
    base = _ol_leverage(opinc, 28)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w29_s5_v050_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 50. Captures rate of change."""
    base = _ol_leverage(sga, 29)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w30_s6_v051_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 51. Captures rate of change."""
    base = _ol_leverage(revenue, 30)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w31_s7_v052_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 52. Captures rate of change."""
    base = _ol_leverage(opinc, 31)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w32_s8_v053_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 53. Captures rate of change."""
    base = _ol_leverage(sga, 32)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w33_s9_v054_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 54. Captures rate of change."""
    base = _ol_leverage(revenue, 33)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w34_s10_v055_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 55. Captures rate of change."""
    base = _ol_leverage(opinc, 34)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w35_s11_v056_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 56. Captures rate of change."""
    base = _ol_leverage(sga, 35)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w36_s12_v057_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 57. Captures rate of change."""
    base = _ol_leverage(revenue, 36)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w37_s13_v058_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 58. Captures rate of change."""
    base = _ol_leverage(opinc, 37)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w38_s14_v059_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 59. Captures rate of change."""
    base = _ol_leverage(sga, 38)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w39_s5_v060_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 60. Captures rate of change."""
    base = _ol_leverage(revenue, 39)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w40_s6_v061_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 61. Captures rate of change."""
    base = _ol_leverage(opinc, 40)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w41_s7_v062_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 62. Captures rate of change."""
    base = _ol_leverage(sga, 41)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w21_s8_v063_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 63. Captures rate of change."""
    base = _ol_leverage(revenue, 21)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w22_s9_v064_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 64. Captures rate of change."""
    base = _ol_leverage(opinc, 22)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w23_s10_v065_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 65. Captures rate of change."""
    base = _ol_leverage(sga, 23)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w24_s11_v066_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 66. Captures rate of change."""
    base = _ol_leverage(revenue, 24)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w25_s12_v067_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 67. Captures rate of change."""
    base = _ol_leverage(opinc, 25)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w26_s13_v068_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 68. Captures rate of change."""
    base = _ol_leverage(sga, 26)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w27_s14_v069_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 69. Captures rate of change."""
    base = _ol_leverage(revenue, 27)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w28_s5_v070_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 70. Captures rate of change."""
    base = _ol_leverage(opinc, 28)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w29_s6_v071_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 71. Captures rate of change."""
    base = _ol_leverage(sga, 29)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w30_s7_v072_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 72. Captures rate of change."""
    base = _ol_leverage(revenue, 30)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w31_s8_v073_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 73. Captures rate of change."""
    base = _ol_leverage(opinc, 31)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w32_s9_v074_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 74. Captures rate of change."""
    base = _ol_leverage(sga, 32)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w33_s10_v075_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 75. Captures rate of change."""
    base = _ol_leverage(revenue, 33)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w34_s11_v076_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 76. Captures rate of change."""
    base = _ol_leverage(opinc, 34)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w35_s12_v077_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 77. Captures rate of change."""
    base = _ol_leverage(sga, 35)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w36_s13_v078_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 78. Captures rate of change."""
    base = _ol_leverage(revenue, 36)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w37_s14_v079_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 79. Captures rate of change."""
    base = _ol_leverage(opinc, 37)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w38_s5_v080_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 80. Captures rate of change."""
    base = _ol_leverage(sga, 38)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w39_s6_v081_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 81. Captures rate of change."""
    base = _ol_leverage(revenue, 39)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w40_s7_v082_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 82. Captures rate of change."""
    base = _ol_leverage(opinc, 40)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w41_s8_v083_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 83. Captures rate of change."""
    base = _ol_leverage(sga, 41)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w21_s9_v084_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 84. Captures rate of change."""
    base = _ol_leverage(revenue, 21)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w22_s10_v085_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 85. Captures rate of change."""
    base = _ol_leverage(opinc, 22)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w23_s11_v086_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 86. Captures rate of change."""
    base = _ol_leverage(sga, 23)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w24_s12_v087_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 87. Captures rate of change."""
    base = _ol_leverage(revenue, 24)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w25_s13_v088_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 88. Captures rate of change."""
    base = _ol_leverage(opinc, 25)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w26_s14_v089_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 89. Captures rate of change."""
    base = _ol_leverage(sga, 26)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w27_s5_v090_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 90. Captures rate of change."""
    base = _ol_leverage(revenue, 27)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w28_s6_v091_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 91. Captures rate of change."""
    base = _ol_leverage(opinc, 28)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w29_s7_v092_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 92. Captures rate of change."""
    base = _ol_leverage(sga, 29)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w30_s8_v093_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 93. Captures rate of change."""
    base = _ol_leverage(revenue, 30)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w31_s9_v094_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 94. Captures rate of change."""
    base = _ol_leverage(opinc, 31)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w32_s10_v095_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 95. Captures rate of change."""
    base = _ol_leverage(sga, 32)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w33_s11_v096_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 96. Captures rate of change."""
    base = _ol_leverage(revenue, 33)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w34_s12_v097_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 97. Captures rate of change."""
    base = _ol_leverage(opinc, 34)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w35_s13_v098_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 98. Captures rate of change."""
    base = _ol_leverage(sga, 35)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w36_s14_v099_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 99. Captures rate of change."""
    base = _ol_leverage(revenue, 36)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w37_s5_v100_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 100. Captures rate of change."""
    base = _ol_leverage(opinc, 37)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w38_s6_v101_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 101. Captures rate of change."""
    base = _ol_leverage(sga, 38)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w39_s7_v102_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 102. Captures rate of change."""
    base = _ol_leverage(revenue, 39)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w40_s8_v103_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 103. Captures rate of change."""
    base = _ol_leverage(opinc, 40)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w41_s9_v104_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 104. Captures rate of change."""
    base = _ol_leverage(sga, 41)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w21_s10_v105_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 105. Captures rate of change."""
    base = _ol_leverage(revenue, 21)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w22_s11_v106_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 106. Captures rate of change."""
    base = _ol_leverage(opinc, 22)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w23_s12_v107_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 107. Captures rate of change."""
    base = _ol_leverage(sga, 23)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w24_s13_v108_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 108. Captures rate of change."""
    base = _ol_leverage(revenue, 24)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w25_s14_v109_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 109. Captures rate of change."""
    base = _ol_leverage(opinc, 25)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w26_s5_v110_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 110. Captures rate of change."""
    base = _ol_leverage(sga, 26)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w27_s6_v111_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 111. Captures rate of change."""
    base = _ol_leverage(revenue, 27)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w28_s7_v112_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 112. Captures rate of change."""
    base = _ol_leverage(opinc, 28)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w29_s8_v113_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 113. Captures rate of change."""
    base = _ol_leverage(sga, 29)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w30_s9_v114_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 114. Captures rate of change."""
    base = _ol_leverage(revenue, 30)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w31_s10_v115_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 115. Captures rate of change."""
    base = _ol_leverage(opinc, 31)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w32_s11_v116_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 116. Captures rate of change."""
    base = _ol_leverage(sga, 32)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w33_s12_v117_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 117. Captures rate of change."""
    base = _ol_leverage(revenue, 33)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w34_s13_v118_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 118. Captures rate of change."""
    base = _ol_leverage(opinc, 34)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w35_s14_v119_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 119. Captures rate of change."""
    base = _ol_leverage(sga, 35)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w36_s5_v120_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 120. Captures rate of change."""
    base = _ol_leverage(revenue, 36)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w37_s6_v121_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 121. Captures rate of change."""
    base = _ol_leverage(opinc, 37)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w38_s7_v122_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 122. Captures rate of change."""
    base = _ol_leverage(sga, 38)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w39_s8_v123_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 123. Captures rate of change."""
    base = _ol_leverage(revenue, 39)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w40_s9_v124_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 124. Captures rate of change."""
    base = _ol_leverage(opinc, 40)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w41_s10_v125_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 125. Captures rate of change."""
    base = _ol_leverage(sga, 41)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w21_s11_v126_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 126. Captures rate of change."""
    base = _ol_leverage(revenue, 21)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w22_s12_v127_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 127. Captures rate of change."""
    base = _ol_leverage(opinc, 22)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w23_s13_v128_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 128. Captures rate of change."""
    base = _ol_leverage(sga, 23)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w24_s14_v129_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 129. Captures rate of change."""
    base = _ol_leverage(revenue, 24)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w25_s5_v130_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 130. Captures rate of change."""
    base = _ol_leverage(opinc, 25)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w26_s6_v131_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 131. Captures rate of change."""
    base = _ol_leverage(sga, 26)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w27_s7_v132_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 132. Captures rate of change."""
    base = _ol_leverage(revenue, 27)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w28_s8_v133_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 133. Captures rate of change."""
    base = _ol_leverage(opinc, 28)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w29_s9_v134_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 134. Captures rate of change."""
    base = _ol_leverage(sga, 29)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w30_s10_v135_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 135. Captures rate of change."""
    base = _ol_leverage(revenue, 30)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w31_s11_v136_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 136. Captures rate of change."""
    base = _ol_leverage(opinc, 31)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w32_s12_v137_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 137. Captures rate of change."""
    base = _ol_leverage(sga, 32)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w33_s13_v138_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 138. Captures rate of change."""
    base = _ol_leverage(revenue, 33)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w34_s14_v139_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 139. Captures rate of change."""
    base = _ol_leverage(opinc, 34)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w35_s5_v140_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 140. Captures rate of change."""
    base = _ol_leverage(sga, 35)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w36_s6_v141_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 141. Captures rate of change."""
    base = _ol_leverage(revenue, 36)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w37_s7_v142_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 142. Captures rate of change."""
    base = _ol_leverage(opinc, 37)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w38_s8_v143_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 143. Captures rate of change."""
    base = _ol_leverage(sga, 38)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w39_s9_v144_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 144. Captures rate of change."""
    base = _ol_leverage(revenue, 39)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w40_s10_v145_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 145. Captures rate of change."""
    base = _ol_leverage(opinc, 40)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w41_s11_v146_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 146. Captures rate of change."""
    base = _ol_leverage(sga, 41)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w21_s12_v147_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 147. Captures rate of change."""
    base = _ol_leverage(revenue, 21)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_slope_w22_s13_v148_signal(opinc) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: opinc, Variation: 148. Captures rate of change."""
    base = _ol_leverage(opinc, 22)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_slope_w23_s14_v149_signal(sga) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: sga, Variation: 149. Captures rate of change."""
    base = _ol_leverage(sga, 23)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_slope_w24_s5_v150_signal(revenue) -> pd.Series:
    """Slope feature for f40_operating_leverage_composite. Input: revenue, Variation: 150. Captures rate of change."""
    base = _ol_leverage(revenue, 24)
    res = base.diff(5)
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
F40_OPERATING_LEVERAGE_COMPOSITE_REGISTRY_SLOPE_001_150 = REGISTRY
