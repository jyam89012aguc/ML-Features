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

def f48_cash_runway_fcf_jerk_w22_a6_j4_v001_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 1. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j5_v002_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 2. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j3_v003_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 3. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j4_v004_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 4. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j5_v005_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 5. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j3_v006_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 6. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j4_v007_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 7. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j5_v008_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 8. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j3_v009_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 9. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j4_v010_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 10. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j5_v011_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 11. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j3_v012_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 12. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j4_v013_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 13. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j5_v014_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 14. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j3_v015_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 15. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j4_v016_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 16. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j5_v017_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 17. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j3_v018_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 18. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j4_v019_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 19. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j5_v020_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 20. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j3_v021_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 21. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j4_v022_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 22. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j5_v023_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 23. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j3_v024_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 24. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j4_v025_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 25. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j5_v026_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 26. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j3_v027_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 27. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j4_v028_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 28. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j5_v029_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 29. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j3_v030_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 30. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j4_v031_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 31. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j5_v032_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 32. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j3_v033_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 33. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j4_v034_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 34. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j5_v035_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 35. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j3_v036_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 36. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j4_v037_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 37. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j5_v038_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 38. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j3_v039_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 39. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j4_v040_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 40. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j5_v041_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 41. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j3_v042_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 42. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j4_v043_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 43. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j5_v044_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 44. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j3_v045_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 45. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j4_v046_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 46. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j5_v047_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 47. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j3_v048_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 48. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j4_v049_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 49. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j5_v050_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 50. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j3_v051_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 51. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j4_v052_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 52. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j5_v053_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 53. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j3_v054_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 54. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j4_v055_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 55. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j5_v056_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 56. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j3_v057_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 57. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j4_v058_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 58. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j5_v059_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 59. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j3_v060_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 60. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j4_v061_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 61. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j5_v062_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 62. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j3_v063_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 63. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j4_v064_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 64. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j5_v065_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 65. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j3_v066_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 66. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j4_v067_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 67. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j5_v068_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 68. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j3_v069_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 69. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j4_v070_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 70. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j5_v071_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 71. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j3_v072_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 72. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j4_v073_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 73. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j5_v074_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 74. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j3_v075_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 75. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j4_v076_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 76. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j5_v077_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 77. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j3_v078_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 78. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j4_v079_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 79. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j5_v080_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 80. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j3_v081_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 81. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j4_v082_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 82. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j5_v083_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 83. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j3_v084_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 84. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j4_v085_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 85. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j5_v086_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 86. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j3_v087_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 87. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j4_v088_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 88. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j5_v089_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 89. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j3_v090_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 90. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j4_v091_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 91. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j5_v092_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 92. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j3_v093_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 93. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j4_v094_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 94. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j5_v095_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 95. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j3_v096_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 96. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j4_v097_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 97. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j5_v098_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 98. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j3_v099_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 99. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j4_v100_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 100. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j5_v101_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 101. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j3_v102_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 102. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j4_v103_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 103. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j5_v104_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 104. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j3_v105_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 105. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j4_v106_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 106. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j5_v107_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 107. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j3_v108_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 108. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j4_v109_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 109. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j5_v110_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 110. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j3_v111_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 111. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j4_v112_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 112. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j5_v113_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 113. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j3_v114_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 114. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j4_v115_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 115. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j5_v116_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 116. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j3_v117_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 117. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j4_v118_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 118. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j5_v119_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 119. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j3_v120_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 120. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j4_v121_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 121. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j5_v122_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 122. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j3_v123_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 123. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j4_v124_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 124. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j5_v125_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 125. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j3_v126_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 126. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j4_v127_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 127. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j5_v128_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 128. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j3_v129_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 129. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j4_v130_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 130. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j5_v131_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 131. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j3_v132_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 132. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j4_v133_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 133. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j5_v134_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 134. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j3_v135_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 135. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j4_v136_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 136. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j5_v137_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 137. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j3_v138_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 138. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j4_v139_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 139. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j5_v140_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 140. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w22_a6_j3_v141_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 141. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w23_a7_j4_v142_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 142. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w24_a8_j5_v143_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 143. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w25_a9_j3_v144_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 144. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w26_a5_j4_v145_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 145. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w27_a6_j5_v146_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 146. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(6)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w28_a7_j3_v147_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 147. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(7)
    res = accel.diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w29_a8_j4_v148_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 148. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(8)
    res = accel.diff(4)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_fcf_jerk_w30_a9_j5_v149_signal(fcf) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: fcf, Variation: 149. Captures higher-order dynamics."""
    base = _cr_burn(fcf, fcf if 'fcf' == 'cash' else cash)
    accel = base.diff(9)
    res = accel.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_cash_runway_cash_jerk_w21_a5_j3_v150_signal(cash) -> pd.Series:
    """Jerk feature for f48_cash_runway. Input: cash, Variation: 150. Captures higher-order dynamics."""
    base = _cr_burn(cash, fcf if 'cash' == 'cash' else cash)
    accel = base.diff(5)
    res = accel.diff(3)
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
F48_CASH_RUNWAY_REGISTRY_JERK_001_150 = REGISTRY
