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

def _cr_burn(cash, fcf): return cash / fcf.clip(upper=-1).abs().replace(0, np.nan)

def f48_cash_runway_fcf_slope_w22_s6_v001_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 1. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w23_s7_v002_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 2. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w24_s8_v003_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 3. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w25_s9_v004_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 4. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w26_s10_v005_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 5. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w27_s11_v006_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 6. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w28_s12_v007_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 7. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w29_s13_v008_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 8. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w30_s14_v009_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 9. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w31_s5_v010_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 10. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w32_s6_v011_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 11. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w33_s7_v012_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 12. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w34_s8_v013_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 13. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w35_s9_v014_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 14. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w36_s10_v015_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 15. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w37_s11_v016_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 16. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w38_s12_v017_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 17. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w39_s13_v018_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 18. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w40_s14_v019_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 19. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w41_s5_v020_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 20. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w21_s6_v021_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 21. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w22_s7_v022_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 22. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w23_s8_v023_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 23. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w24_s9_v024_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 24. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w25_s10_v025_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 25. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w26_s11_v026_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 26. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w27_s12_v027_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 27. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w28_s13_v028_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 28. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w29_s14_v029_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 29. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w30_s5_v030_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 30. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w31_s6_v031_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 31. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w32_s7_v032_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 32. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w33_s8_v033_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 33. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w34_s9_v034_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 34. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w35_s10_v035_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 35. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w36_s11_v036_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 36. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w37_s12_v037_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 37. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w38_s13_v038_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 38. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w39_s14_v039_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 39. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w40_s5_v040_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 40. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w41_s6_v041_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 41. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w21_s7_v042_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 42. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w22_s8_v043_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 43. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w23_s9_v044_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 44. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w24_s10_v045_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 45. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w25_s11_v046_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 46. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w26_s12_v047_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 47. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w27_s13_v048_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 48. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w28_s14_v049_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 49. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w29_s5_v050_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 50. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w30_s6_v051_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 51. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w31_s7_v052_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 52. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w32_s8_v053_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 53. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w33_s9_v054_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 54. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w34_s10_v055_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 55. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w35_s11_v056_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 56. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w36_s12_v057_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 57. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w37_s13_v058_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 58. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w38_s14_v059_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 59. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w39_s5_v060_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 60. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w40_s6_v061_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 61. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w41_s7_v062_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 62. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w21_s8_v063_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 63. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w22_s9_v064_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 64. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w23_s10_v065_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 65. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w24_s11_v066_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 66. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w25_s12_v067_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 67. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w26_s13_v068_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 68. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w27_s14_v069_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 69. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w28_s5_v070_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 70. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w29_s6_v071_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 71. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w30_s7_v072_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 72. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w31_s8_v073_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 73. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w32_s9_v074_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 74. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w33_s10_v075_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 75. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w34_s11_v076_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 76. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w35_s12_v077_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 77. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w36_s13_v078_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 78. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w37_s14_v079_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 79. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w38_s5_v080_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 80. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w39_s6_v081_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 81. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w40_s7_v082_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 82. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w41_s8_v083_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 83. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w21_s9_v084_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 84. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w22_s10_v085_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 85. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w23_s11_v086_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 86. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w24_s12_v087_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 87. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w25_s13_v088_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 88. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w26_s14_v089_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 89. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w27_s5_v090_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 90. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w28_s6_v091_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 91. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w29_s7_v092_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 92. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w30_s8_v093_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 93. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w31_s9_v094_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 94. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w32_s10_v095_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 95. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w33_s11_v096_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 96. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w34_s12_v097_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 97. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w35_s13_v098_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 98. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w36_s14_v099_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 99. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w37_s5_v100_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 100. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w38_s6_v101_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 101. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w39_s7_v102_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 102. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w40_s8_v103_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 103. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w41_s9_v104_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 104. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w21_s10_v105_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 105. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w22_s11_v106_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 106. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w23_s12_v107_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 107. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w24_s13_v108_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 108. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w25_s14_v109_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 109. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w26_s5_v110_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 110. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w27_s6_v111_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 111. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w28_s7_v112_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 112. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w29_s8_v113_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 113. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w30_s9_v114_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 114. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w31_s10_v115_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 115. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w32_s11_v116_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 116. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w33_s12_v117_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 117. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w34_s13_v118_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 118. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w35_s14_v119_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 119. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w36_s5_v120_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 120. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w37_s6_v121_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 121. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w38_s7_v122_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 122. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w39_s8_v123_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 123. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w40_s9_v124_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 124. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w41_s10_v125_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 125. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w21_s11_v126_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 126. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w22_s12_v127_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 127. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w23_s13_v128_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 128. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w24_s14_v129_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 129. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w25_s5_v130_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 130. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w26_s6_v131_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 131. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w27_s7_v132_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 132. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w28_s8_v133_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 133. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w29_s9_v134_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 134. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w30_s10_v135_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 135. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w31_s11_v136_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 136. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w32_s12_v137_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 137. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w33_s13_v138_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 138. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w34_s14_v139_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 139. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w35_s5_v140_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 140. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w36_s6_v141_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 141. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(6)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w37_s7_v142_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 142. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(7)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w38_s8_v143_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 143. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(8)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w39_s9_v144_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 144. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(9)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w40_s10_v145_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 145. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w41_s11_v146_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 146. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(11)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w21_s12_v147_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 147. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(12)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w22_s13_v148_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 148. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(13)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_slope_w23_s14_v149_signal(fcf) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: fcf, Variation: 149. Captures rate of change."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    res = base.diff(14)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_slope_w24_s5_v150_signal(cash) -> pd.Series:
    """Slope feature for f48_cash_runway. Input: cash, Variation: 150. Captures rate of change."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "cash": np.random.normal(1000, 100, n).cumsum() + 1000,
        "fcf": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f48_cash_runway_"))]
    
    print(f"Testing {len(funcs)} functions for f48_cash_runway...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f48_cash_runway_"))]}
F48_CASH_RUNWAY_REGISTRY_SLOPE_001_150 = REGISTRY
