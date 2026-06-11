import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _cfj_growth(s, w):
    return s.pct_change(w)

def _cfj_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _cfj_jerk(s, w1, w2, w3):
    accel = s.pct_change(w1).pct_change(w2)
    return accel.diff(w3)

def _cfj_slope(s, w):
    return s.pct_change(w)

def _cfj_jerk_deriv(s, w):
    return s.diff(w)

def _cfj_zscore(s, w):
    return _z(s, w)

def f36_cash_flow_jerk_fcf_jerk_5d_21d_5d_v001_signal(fcf) -> pd.Series:
    """Cash Flow Jerk for fcf over 5d, 21d, 5d. Captures high-order changes in cash flow generation. Variation 1."""
    res = _cfj_jerk(fcf, 5, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_jerk_5d_21d_5d_v002_signal(ncfo) -> pd.Series:
    """Cash Flow Jerk for ncfo over 5d, 21d, 5d. Captures high-order changes in cash flow generation. Variation 2."""
    res = _cfj_jerk(ncfo, 5, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_jerk_10d_21d_10d_v003_signal(fcf) -> pd.Series:
    """Cash Flow Jerk for fcf over 10d, 21d, 10d. Captures high-order changes in cash flow generation. Variation 3."""
    res = _cfj_jerk(fcf, 10, 21, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_jerk_10d_21d_10d_v004_signal(ncfo) -> pd.Series:
    """Cash Flow Jerk for ncfo over 10d, 21d, 10d. Captures high-order changes in cash flow generation. Variation 4."""
    res = _cfj_jerk(ncfo, 10, 21, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_jerk_21d_42d_21d_v005_signal(fcf) -> pd.Series:
    """Cash Flow Jerk for fcf over 21d, 42d, 21d. Captures high-order changes in cash flow generation. Variation 5."""
    res = _cfj_jerk(fcf, 21, 42, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_jerk_21d_42d_21d_v006_signal(ncfo) -> pd.Series:
    """Cash Flow Jerk for ncfo over 21d, 42d, 21d. Captures high-order changes in cash flow generation. Variation 6."""
    res = _cfj_jerk(ncfo, 21, 42, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_jerk_63d_126d_63d_v007_signal(fcf) -> pd.Series:
    """Cash Flow Jerk for fcf over 63d, 126d, 63d. Captures high-order changes in cash flow generation. Variation 7."""
    res = _cfj_jerk(fcf, 63, 126, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_jerk_63d_126d_63d_v008_signal(ncfo) -> pd.Series:
    """Cash Flow Jerk for ncfo over 63d, 126d, 63d. Captures high-order changes in cash flow generation. Variation 8."""
    res = _cfj_jerk(ncfo, 63, 126, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v009_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 9. Normalizes cash flow volatility. Variation 9."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v010_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 10. Normalizes cash flow volatility. Variation 10."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v011_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 11. Normalizes cash flow volatility. Variation 11."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v012_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 12. Normalizes cash flow volatility. Variation 12."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v013_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 13. Normalizes cash flow volatility. Variation 13."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v014_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 14. Normalizes cash flow volatility. Variation 14."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v015_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 15. Normalizes cash flow volatility. Variation 15."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v016_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 16. Normalizes cash flow volatility. Variation 16."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v017_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 17. Normalizes cash flow volatility. Variation 17."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v018_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 18. Normalizes cash flow volatility. Variation 18."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v019_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 19. Normalizes cash flow volatility. Variation 19."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v020_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 20. Normalizes cash flow volatility. Variation 20."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v021_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 21. Normalizes cash flow volatility. Variation 21."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v022_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 22. Normalizes cash flow volatility. Variation 22."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v023_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 23. Normalizes cash flow volatility. Variation 23."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v024_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 24. Normalizes cash flow volatility. Variation 24."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v025_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 25. Normalizes cash flow volatility. Variation 25."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v026_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 26. Normalizes cash flow volatility. Variation 26."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v027_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 27. Normalizes cash flow volatility. Variation 27."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v028_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 28. Normalizes cash flow volatility. Variation 28."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v029_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 29. Normalizes cash flow volatility. Variation 29."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v030_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 30. Normalizes cash flow volatility. Variation 30."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v031_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 31. Normalizes cash flow volatility. Variation 31."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v032_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 32. Normalizes cash flow volatility. Variation 32."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v033_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 33. Normalizes cash flow volatility. Variation 33."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v034_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 34. Normalizes cash flow volatility. Variation 34."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v035_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 35. Normalizes cash flow volatility. Variation 35."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v036_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 36. Normalizes cash flow volatility. Variation 36."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v037_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 37. Normalizes cash flow volatility. Variation 37."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v038_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 38. Normalizes cash flow volatility. Variation 38."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v039_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 39. Normalizes cash flow volatility. Variation 39."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v040_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 40. Normalizes cash flow volatility. Variation 40."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v041_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 41. Normalizes cash flow volatility. Variation 41."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v042_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 42. Normalizes cash flow volatility. Variation 42."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v043_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 43. Normalizes cash flow volatility. Variation 43."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v044_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 44. Normalizes cash flow volatility. Variation 44."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v045_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 45. Normalizes cash flow volatility. Variation 45."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v046_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 46. Normalizes cash flow volatility. Variation 46."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v047_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 47. Normalizes cash flow volatility. Variation 47."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v048_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 48. Normalizes cash flow volatility. Variation 48."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v049_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 49. Normalizes cash flow volatility. Variation 49."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v050_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 50. Normalizes cash flow volatility. Variation 50."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v051_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 51. Normalizes cash flow volatility. Variation 51."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v052_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 52. Normalizes cash flow volatility. Variation 52."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v053_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 53. Normalizes cash flow volatility. Variation 53."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v054_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 54. Normalizes cash flow volatility. Variation 54."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v055_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 55. Normalizes cash flow volatility. Variation 55."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v056_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 56. Normalizes cash flow volatility. Variation 56."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v057_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 57. Normalizes cash flow volatility. Variation 57."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v058_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 58. Normalizes cash flow volatility. Variation 58."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v059_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 59. Normalizes cash flow volatility. Variation 59."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v060_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 60. Normalizes cash flow volatility. Variation 60."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v061_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 61. Normalizes cash flow volatility. Variation 61."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v062_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 62. Normalizes cash flow volatility. Variation 62."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v063_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 63. Normalizes cash flow volatility. Variation 63."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 84)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v064_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 64. Normalizes cash flow volatility. Variation 64."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v065_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 65. Normalizes cash flow volatility. Variation 65."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 86)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v066_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 66. Normalizes cash flow volatility. Variation 66."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 87)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v067_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 67. Normalizes cash flow volatility. Variation 67."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 88)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v068_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 68. Normalizes cash flow volatility. Variation 68."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 89)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v069_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 69. Normalizes cash flow volatility. Variation 69."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 90)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v070_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 70. Normalizes cash flow volatility. Variation 70."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 91)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v071_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 71. Normalizes cash flow volatility. Variation 71."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 92)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v072_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 72. Normalizes cash flow volatility. Variation 72."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 93)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v073_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 73. Normalizes cash flow volatility. Variation 73."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 94)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v074_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 74. Normalizes cash flow volatility. Variation 74."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_zscore_v075_signal(fcf) -> pd.Series:
    """Z-score of cash flow jerk variation 75. Normalizes cash flow volatility. Variation 75."""
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, 96)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "fcf": np.random.normal(10, 2, n).cumsum() + 1000,
        "ncfo": np.random.normal(15, 3, n).cumsum() + 1500,
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f36_cash_flow_jerk_"))]
    
    print(f"Testing {len(funcs)} functions...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 10

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f36_cash_flow_jerk_"))]}
F36_CASH_FLOW_JERK_REGISTRY_BASE_001_075 = REGISTRY
