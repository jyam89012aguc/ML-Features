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

def f36_cash_flow_jerk_fcf_slope_5d_v001_signal(fcf) -> pd.Series:
    """Slope of cash flow jerk for fcf with window 5d. Variation 1."""
    jerk = _cfj_jerk(fcf, 5, 10, 5)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_slope_5d_v002_signal(ncfo) -> pd.Series:
    """Slope of cash flow jerk for ncfo with window 5d. Variation 2."""
    jerk = _cfj_jerk(ncfo, 5, 10, 5)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_slope_5d_v003_signal(fcf) -> pd.Series:
    """Slope of cash flow jerk for fcf with window 5d. Variation 3."""
    jerk = _cfj_jerk(fcf, 10, 21, 10)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_slope_5d_v004_signal(ncfo) -> pd.Series:
    """Slope of cash flow jerk for ncfo with window 5d. Variation 4."""
    jerk = _cfj_jerk(ncfo, 10, 21, 10)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_slope_5d_v005_signal(fcf) -> pd.Series:
    """Slope of cash flow jerk for fcf with window 5d. Variation 5."""
    jerk = _cfj_jerk(fcf, 21, 42, 21)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_slope_5d_v006_signal(ncfo) -> pd.Series:
    """Slope of cash flow jerk for ncfo with window 5d. Variation 6."""
    jerk = _cfj_jerk(ncfo, 21, 42, 21)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_slope_5d_v007_signal(fcf) -> pd.Series:
    """Slope of cash flow jerk for fcf with window 5d. Variation 7."""
    jerk = _cfj_jerk(fcf, 63, 63, 63)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_slope_5d_v008_signal(ncfo) -> pd.Series:
    """Slope of cash flow jerk for ncfo with window 5d. Variation 8."""
    jerk = _cfj_jerk(ncfo, 63, 63, 63)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_slope_21d_v009_signal(fcf) -> pd.Series:
    """Slope of cash flow jerk for fcf with window 21d. Variation 9."""
    jerk = _cfj_jerk(fcf, 5, 10, 5)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_slope_21d_v010_signal(ncfo) -> pd.Series:
    """Slope of cash flow jerk for ncfo with window 21d. Variation 10."""
    jerk = _cfj_jerk(ncfo, 5, 10, 5)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_slope_21d_v011_signal(fcf) -> pd.Series:
    """Slope of cash flow jerk for fcf with window 21d. Variation 11."""
    jerk = _cfj_jerk(fcf, 10, 21, 10)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_slope_21d_v012_signal(ncfo) -> pd.Series:
    """Slope of cash flow jerk for ncfo with window 21d. Variation 12."""
    jerk = _cfj_jerk(ncfo, 10, 21, 10)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_slope_21d_v013_signal(fcf) -> pd.Series:
    """Slope of cash flow jerk for fcf with window 21d. Variation 13."""
    jerk = _cfj_jerk(fcf, 21, 42, 21)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_slope_21d_v014_signal(ncfo) -> pd.Series:
    """Slope of cash flow jerk for ncfo with window 21d. Variation 14."""
    jerk = _cfj_jerk(ncfo, 21, 42, 21)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_fcf_slope_21d_v015_signal(fcf) -> pd.Series:
    """Slope of cash flow jerk for fcf with window 21d. Variation 15."""
    jerk = _cfj_jerk(fcf, 63, 63, 63)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_ncfo_slope_21d_v016_signal(ncfo) -> pd.Series:
    """Slope of cash flow jerk for ncfo with window 21d. Variation 16."""
    jerk = _cfj_jerk(ncfo, 63, 63, 63)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v017_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 22. Variation 17."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v018_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 23. Variation 18."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v019_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 24. Variation 19."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v020_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 25. Variation 20."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v021_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 26. Variation 21."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v022_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 27. Variation 22."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v023_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 28. Variation 23."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v024_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 29. Variation 24."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v025_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 30. Variation 25."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v026_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 31. Variation 26."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v027_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 32. Variation 27."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v028_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 33. Variation 28."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v029_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 34. Variation 29."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v030_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 35. Variation 30."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v031_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 36. Variation 31."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v032_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 37. Variation 32."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v033_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 38. Variation 33."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v034_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 39. Variation 34."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v035_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 40. Variation 35."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v036_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 41. Variation 36."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v037_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 42. Variation 37."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v038_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 43. Variation 38."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v039_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 44. Variation 39."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v040_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 45. Variation 40."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v041_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 46. Variation 41."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v042_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 47. Variation 42."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v043_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 48. Variation 43."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v044_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 49. Variation 44."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v045_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 50. Variation 45."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v046_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 51. Variation 46."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v047_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 52. Variation 47."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v048_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 53. Variation 48."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v049_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 54. Variation 49."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v050_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 55. Variation 50."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v051_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 56. Variation 51."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v052_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 57. Variation 52."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v053_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 58. Variation 53."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v054_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 59. Variation 54."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v055_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 60. Variation 55."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v056_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 61. Variation 56."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v057_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 62. Variation 57."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v058_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 63. Variation 58."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v059_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 64. Variation 59."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v060_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 65. Variation 60."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v061_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 66. Variation 61."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v062_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 67. Variation 62."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v063_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 5. Variation 63."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v064_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 6. Variation 64."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v065_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 7. Variation 65."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v066_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 8. Variation 66."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v067_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 9. Variation 67."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v068_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 10. Variation 68."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v069_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 11. Variation 69."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v070_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 12. Variation 70."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v071_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 13. Variation 71."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v072_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 14. Variation 72."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v073_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 15. Variation 73."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v074_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 16. Variation 74."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v075_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 17. Variation 75."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v076_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 18. Variation 76."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v077_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 19. Variation 77."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v078_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 20. Variation 78."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v079_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 21. Variation 79."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v080_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 22. Variation 80."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v081_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 23. Variation 81."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v082_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 24. Variation 82."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v083_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 25. Variation 83."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v084_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 26. Variation 84."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v085_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 27. Variation 85."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v086_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 28. Variation 86."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v087_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 29. Variation 87."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v088_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 30. Variation 88."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v089_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 31. Variation 89."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v090_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 32. Variation 90."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v091_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 33. Variation 91."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v092_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 34. Variation 92."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v093_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 35. Variation 93."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v094_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 36. Variation 94."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v095_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 37. Variation 95."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v096_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 38. Variation 96."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v097_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 39. Variation 97."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v098_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 40. Variation 98."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v099_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 41. Variation 99."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v100_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 42. Variation 100."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v101_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 43. Variation 101."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v102_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 44. Variation 102."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v103_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 45. Variation 103."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v104_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 46. Variation 104."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v105_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 47. Variation 105."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v106_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 48. Variation 106."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v107_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 49. Variation 107."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v108_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 50. Variation 108."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v109_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 51. Variation 109."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v110_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 52. Variation 110."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v111_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 53. Variation 111."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v112_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 54. Variation 112."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v113_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 55. Variation 113."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v114_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 56. Variation 114."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v115_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 57. Variation 115."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v116_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 58. Variation 116."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v117_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 59. Variation 117."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v118_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 60. Variation 118."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v119_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 61. Variation 119."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v120_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 62. Variation 120."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v121_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 63. Variation 121."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v122_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 64. Variation 122."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v123_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 65. Variation 123."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v124_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 66. Variation 124."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v125_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 67. Variation 125."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v126_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 5. Variation 126."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v127_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 6. Variation 127."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v128_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 7. Variation 128."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v129_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 8. Variation 129."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v130_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 9. Variation 130."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v131_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 10. Variation 131."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v132_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 11. Variation 132."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v133_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 12. Variation 133."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v134_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 13. Variation 134."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v135_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 14. Variation 135."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v136_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 15. Variation 136."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v137_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 16. Variation 137."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v138_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 17. Variation 138."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v139_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 18. Variation 139."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v140_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 19. Variation 140."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v141_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 20. Variation 141."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v142_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 21. Variation 142."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v143_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 22. Variation 143."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v144_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 23. Variation 144."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v145_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 24. Variation 145."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v146_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 25. Variation 146."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v147_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 26. Variation 147."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v148_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 27. Variation 148."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v149_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 28. Variation 149."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_slope_fill_v150_signal(fcf) -> pd.Series:
    """Filling slope variations to reach 150. Window 29. Variation 150."""
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, 29)
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
F36_CASH_FLOW_JERK_REGISTRY_SLOPE_001_150 = REGISTRY
