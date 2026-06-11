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

def _wt_dominance(s, w): return s.pct_change(w) / _std(s, w)

def f44_winner_take_all_signal_opinc_slope_w22_s6_v001_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 1. Captures rate of change."""
    base = _wt_dominance(opinc, 22)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w23_s7_v002_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 2. Captures rate of change."""
    base = _wt_dominance(revenue, 23)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w24_s8_v003_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 3. Captures rate of change."""
    base = _wt_dominance(opinc, 24)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w25_s9_v004_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 4. Captures rate of change."""
    base = _wt_dominance(revenue, 25)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w26_s10_v005_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 5. Captures rate of change."""
    base = _wt_dominance(opinc, 26)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w27_s11_v006_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 6. Captures rate of change."""
    base = _wt_dominance(revenue, 27)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w28_s12_v007_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 7. Captures rate of change."""
    base = _wt_dominance(opinc, 28)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w29_s13_v008_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 8. Captures rate of change."""
    base = _wt_dominance(revenue, 29)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w30_s14_v009_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 9. Captures rate of change."""
    base = _wt_dominance(opinc, 30)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w31_s5_v010_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 10. Captures rate of change."""
    base = _wt_dominance(revenue, 31)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w32_s6_v011_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 11. Captures rate of change."""
    base = _wt_dominance(opinc, 32)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w33_s7_v012_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 12. Captures rate of change."""
    base = _wt_dominance(revenue, 33)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w34_s8_v013_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 13. Captures rate of change."""
    base = _wt_dominance(opinc, 34)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w35_s9_v014_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 14. Captures rate of change."""
    base = _wt_dominance(revenue, 35)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w36_s10_v015_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 15. Captures rate of change."""
    base = _wt_dominance(opinc, 36)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w37_s11_v016_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 16. Captures rate of change."""
    base = _wt_dominance(revenue, 37)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w38_s12_v017_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 17. Captures rate of change."""
    base = _wt_dominance(opinc, 38)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w39_s13_v018_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 18. Captures rate of change."""
    base = _wt_dominance(revenue, 39)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w40_s14_v019_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 19. Captures rate of change."""
    base = _wt_dominance(opinc, 40)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w41_s5_v020_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 20. Captures rate of change."""
    base = _wt_dominance(revenue, 41)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w21_s6_v021_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 21. Captures rate of change."""
    base = _wt_dominance(opinc, 21)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w22_s7_v022_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 22. Captures rate of change."""
    base = _wt_dominance(revenue, 22)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w23_s8_v023_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 23. Captures rate of change."""
    base = _wt_dominance(opinc, 23)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w24_s9_v024_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 24. Captures rate of change."""
    base = _wt_dominance(revenue, 24)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w25_s10_v025_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 25. Captures rate of change."""
    base = _wt_dominance(opinc, 25)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w26_s11_v026_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 26. Captures rate of change."""
    base = _wt_dominance(revenue, 26)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w27_s12_v027_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 27. Captures rate of change."""
    base = _wt_dominance(opinc, 27)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w28_s13_v028_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 28. Captures rate of change."""
    base = _wt_dominance(revenue, 28)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w29_s14_v029_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 29. Captures rate of change."""
    base = _wt_dominance(opinc, 29)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w30_s5_v030_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 30. Captures rate of change."""
    base = _wt_dominance(revenue, 30)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w31_s6_v031_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 31. Captures rate of change."""
    base = _wt_dominance(opinc, 31)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w32_s7_v032_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 32. Captures rate of change."""
    base = _wt_dominance(revenue, 32)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w33_s8_v033_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 33. Captures rate of change."""
    base = _wt_dominance(opinc, 33)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w34_s9_v034_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 34. Captures rate of change."""
    base = _wt_dominance(revenue, 34)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w35_s10_v035_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 35. Captures rate of change."""
    base = _wt_dominance(opinc, 35)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w36_s11_v036_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 36. Captures rate of change."""
    base = _wt_dominance(revenue, 36)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w37_s12_v037_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 37. Captures rate of change."""
    base = _wt_dominance(opinc, 37)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w38_s13_v038_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 38. Captures rate of change."""
    base = _wt_dominance(revenue, 38)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w39_s14_v039_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 39. Captures rate of change."""
    base = _wt_dominance(opinc, 39)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w40_s5_v040_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 40. Captures rate of change."""
    base = _wt_dominance(revenue, 40)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w41_s6_v041_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 41. Captures rate of change."""
    base = _wt_dominance(opinc, 41)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w21_s7_v042_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 42. Captures rate of change."""
    base = _wt_dominance(revenue, 21)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w22_s8_v043_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 43. Captures rate of change."""
    base = _wt_dominance(opinc, 22)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w23_s9_v044_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 44. Captures rate of change."""
    base = _wt_dominance(revenue, 23)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w24_s10_v045_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 45. Captures rate of change."""
    base = _wt_dominance(opinc, 24)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w25_s11_v046_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 46. Captures rate of change."""
    base = _wt_dominance(revenue, 25)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w26_s12_v047_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 47. Captures rate of change."""
    base = _wt_dominance(opinc, 26)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w27_s13_v048_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 48. Captures rate of change."""
    base = _wt_dominance(revenue, 27)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w28_s14_v049_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 49. Captures rate of change."""
    base = _wt_dominance(opinc, 28)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w29_s5_v050_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 50. Captures rate of change."""
    base = _wt_dominance(revenue, 29)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w30_s6_v051_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 51. Captures rate of change."""
    base = _wt_dominance(opinc, 30)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w31_s7_v052_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 52. Captures rate of change."""
    base = _wt_dominance(revenue, 31)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w32_s8_v053_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 53. Captures rate of change."""
    base = _wt_dominance(opinc, 32)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w33_s9_v054_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 54. Captures rate of change."""
    base = _wt_dominance(revenue, 33)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w34_s10_v055_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 55. Captures rate of change."""
    base = _wt_dominance(opinc, 34)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w35_s11_v056_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 56. Captures rate of change."""
    base = _wt_dominance(revenue, 35)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w36_s12_v057_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 57. Captures rate of change."""
    base = _wt_dominance(opinc, 36)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w37_s13_v058_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 58. Captures rate of change."""
    base = _wt_dominance(revenue, 37)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w38_s14_v059_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 59. Captures rate of change."""
    base = _wt_dominance(opinc, 38)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w39_s5_v060_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 60. Captures rate of change."""
    base = _wt_dominance(revenue, 39)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w40_s6_v061_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 61. Captures rate of change."""
    base = _wt_dominance(opinc, 40)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w41_s7_v062_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 62. Captures rate of change."""
    base = _wt_dominance(revenue, 41)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w21_s8_v063_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 63. Captures rate of change."""
    base = _wt_dominance(opinc, 21)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w22_s9_v064_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 64. Captures rate of change."""
    base = _wt_dominance(revenue, 22)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w23_s10_v065_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 65. Captures rate of change."""
    base = _wt_dominance(opinc, 23)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w24_s11_v066_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 66. Captures rate of change."""
    base = _wt_dominance(revenue, 24)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w25_s12_v067_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 67. Captures rate of change."""
    base = _wt_dominance(opinc, 25)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w26_s13_v068_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 68. Captures rate of change."""
    base = _wt_dominance(revenue, 26)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w27_s14_v069_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 69. Captures rate of change."""
    base = _wt_dominance(opinc, 27)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w28_s5_v070_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 70. Captures rate of change."""
    base = _wt_dominance(revenue, 28)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w29_s6_v071_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 71. Captures rate of change."""
    base = _wt_dominance(opinc, 29)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w30_s7_v072_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 72. Captures rate of change."""
    base = _wt_dominance(revenue, 30)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w31_s8_v073_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 73. Captures rate of change."""
    base = _wt_dominance(opinc, 31)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w32_s9_v074_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 74. Captures rate of change."""
    base = _wt_dominance(revenue, 32)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w33_s10_v075_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 75. Captures rate of change."""
    base = _wt_dominance(opinc, 33)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w34_s11_v076_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 76. Captures rate of change."""
    base = _wt_dominance(revenue, 34)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w35_s12_v077_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 77. Captures rate of change."""
    base = _wt_dominance(opinc, 35)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w36_s13_v078_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 78. Captures rate of change."""
    base = _wt_dominance(revenue, 36)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w37_s14_v079_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 79. Captures rate of change."""
    base = _wt_dominance(opinc, 37)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w38_s5_v080_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 80. Captures rate of change."""
    base = _wt_dominance(revenue, 38)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w39_s6_v081_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 81. Captures rate of change."""
    base = _wt_dominance(opinc, 39)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w40_s7_v082_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 82. Captures rate of change."""
    base = _wt_dominance(revenue, 40)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w41_s8_v083_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 83. Captures rate of change."""
    base = _wt_dominance(opinc, 41)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w21_s9_v084_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 84. Captures rate of change."""
    base = _wt_dominance(revenue, 21)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w22_s10_v085_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 85. Captures rate of change."""
    base = _wt_dominance(opinc, 22)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w23_s11_v086_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 86. Captures rate of change."""
    base = _wt_dominance(revenue, 23)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w24_s12_v087_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 87. Captures rate of change."""
    base = _wt_dominance(opinc, 24)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w25_s13_v088_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 88. Captures rate of change."""
    base = _wt_dominance(revenue, 25)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w26_s14_v089_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 89. Captures rate of change."""
    base = _wt_dominance(opinc, 26)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w27_s5_v090_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 90. Captures rate of change."""
    base = _wt_dominance(revenue, 27)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w28_s6_v091_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 91. Captures rate of change."""
    base = _wt_dominance(opinc, 28)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w29_s7_v092_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 92. Captures rate of change."""
    base = _wt_dominance(revenue, 29)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w30_s8_v093_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 93. Captures rate of change."""
    base = _wt_dominance(opinc, 30)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w31_s9_v094_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 94. Captures rate of change."""
    base = _wt_dominance(revenue, 31)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w32_s10_v095_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 95. Captures rate of change."""
    base = _wt_dominance(opinc, 32)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w33_s11_v096_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 96. Captures rate of change."""
    base = _wt_dominance(revenue, 33)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w34_s12_v097_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 97. Captures rate of change."""
    base = _wt_dominance(opinc, 34)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w35_s13_v098_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 98. Captures rate of change."""
    base = _wt_dominance(revenue, 35)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w36_s14_v099_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 99. Captures rate of change."""
    base = _wt_dominance(opinc, 36)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w37_s5_v100_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 100. Captures rate of change."""
    base = _wt_dominance(revenue, 37)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w38_s6_v101_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 101. Captures rate of change."""
    base = _wt_dominance(opinc, 38)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w39_s7_v102_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 102. Captures rate of change."""
    base = _wt_dominance(revenue, 39)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w40_s8_v103_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 103. Captures rate of change."""
    base = _wt_dominance(opinc, 40)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w41_s9_v104_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 104. Captures rate of change."""
    base = _wt_dominance(revenue, 41)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w21_s10_v105_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 105. Captures rate of change."""
    base = _wt_dominance(opinc, 21)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w22_s11_v106_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 106. Captures rate of change."""
    base = _wt_dominance(revenue, 22)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w23_s12_v107_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 107. Captures rate of change."""
    base = _wt_dominance(opinc, 23)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w24_s13_v108_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 108. Captures rate of change."""
    base = _wt_dominance(revenue, 24)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w25_s14_v109_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 109. Captures rate of change."""
    base = _wt_dominance(opinc, 25)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w26_s5_v110_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 110. Captures rate of change."""
    base = _wt_dominance(revenue, 26)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w27_s6_v111_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 111. Captures rate of change."""
    base = _wt_dominance(opinc, 27)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w28_s7_v112_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 112. Captures rate of change."""
    base = _wt_dominance(revenue, 28)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w29_s8_v113_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 113. Captures rate of change."""
    base = _wt_dominance(opinc, 29)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w30_s9_v114_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 114. Captures rate of change."""
    base = _wt_dominance(revenue, 30)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w31_s10_v115_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 115. Captures rate of change."""
    base = _wt_dominance(opinc, 31)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w32_s11_v116_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 116. Captures rate of change."""
    base = _wt_dominance(revenue, 32)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w33_s12_v117_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 117. Captures rate of change."""
    base = _wt_dominance(opinc, 33)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w34_s13_v118_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 118. Captures rate of change."""
    base = _wt_dominance(revenue, 34)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w35_s14_v119_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 119. Captures rate of change."""
    base = _wt_dominance(opinc, 35)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w36_s5_v120_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 120. Captures rate of change."""
    base = _wt_dominance(revenue, 36)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w37_s6_v121_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 121. Captures rate of change."""
    base = _wt_dominance(opinc, 37)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w38_s7_v122_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 122. Captures rate of change."""
    base = _wt_dominance(revenue, 38)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w39_s8_v123_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 123. Captures rate of change."""
    base = _wt_dominance(opinc, 39)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w40_s9_v124_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 124. Captures rate of change."""
    base = _wt_dominance(revenue, 40)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w41_s10_v125_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 125. Captures rate of change."""
    base = _wt_dominance(opinc, 41)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w21_s11_v126_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 126. Captures rate of change."""
    base = _wt_dominance(revenue, 21)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w22_s12_v127_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 127. Captures rate of change."""
    base = _wt_dominance(opinc, 22)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w23_s13_v128_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 128. Captures rate of change."""
    base = _wt_dominance(revenue, 23)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w24_s14_v129_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 129. Captures rate of change."""
    base = _wt_dominance(opinc, 24)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w25_s5_v130_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 130. Captures rate of change."""
    base = _wt_dominance(revenue, 25)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w26_s6_v131_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 131. Captures rate of change."""
    base = _wt_dominance(opinc, 26)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w27_s7_v132_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 132. Captures rate of change."""
    base = _wt_dominance(revenue, 27)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w28_s8_v133_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 133. Captures rate of change."""
    base = _wt_dominance(opinc, 28)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w29_s9_v134_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 134. Captures rate of change."""
    base = _wt_dominance(revenue, 29)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w30_s10_v135_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 135. Captures rate of change."""
    base = _wt_dominance(opinc, 30)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w31_s11_v136_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 136. Captures rate of change."""
    base = _wt_dominance(revenue, 31)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w32_s12_v137_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 137. Captures rate of change."""
    base = _wt_dominance(opinc, 32)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w33_s13_v138_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 138. Captures rate of change."""
    base = _wt_dominance(revenue, 33)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w34_s14_v139_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 139. Captures rate of change."""
    base = _wt_dominance(opinc, 34)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w35_s5_v140_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 140. Captures rate of change."""
    base = _wt_dominance(revenue, 35)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w36_s6_v141_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 141. Captures rate of change."""
    base = _wt_dominance(opinc, 36)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w37_s7_v142_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 142. Captures rate of change."""
    base = _wt_dominance(revenue, 37)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w38_s8_v143_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 143. Captures rate of change."""
    base = _wt_dominance(opinc, 38)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w39_s9_v144_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 144. Captures rate of change."""
    base = _wt_dominance(revenue, 39)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w40_s10_v145_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 145. Captures rate of change."""
    base = _wt_dominance(opinc, 40)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w41_s11_v146_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 146. Captures rate of change."""
    base = _wt_dominance(revenue, 41)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w21_s12_v147_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 147. Captures rate of change."""
    base = _wt_dominance(opinc, 21)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w22_s13_v148_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 148. Captures rate of change."""
    base = _wt_dominance(revenue, 22)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_opinc_slope_w23_s14_v149_signal(opinc) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: opinc, Variation: 149. Captures rate of change."""
    base = _wt_dominance(opinc, 23)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_winner_take_all_signal_revenue_slope_w24_s5_v150_signal(revenue) -> pd.Series:
    """Slope feature for f44_winner_take_all_signal. Input: revenue, Variation: 150. Captures rate of change."""
    base = _wt_dominance(revenue, 24)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000,
        "opinc": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f44_winner_take_all_signal_"))]
    
    print(f"Testing {len(funcs)} functions for f44_winner_take_all_signal...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f44_winner_take_all_signal_"))]}
F44_WINNER_TAKE_ALL_SIGNAL_REGISTRY_SLOPE_001_150 = REGISTRY
