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

def f36_cash_flow_jerk_jerk_deriv_v001_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 1. High frequency momentum indicator. Variation 1."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v002_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 2. High frequency momentum indicator. Variation 2."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v003_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 3. High frequency momentum indicator. Variation 3."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v004_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 4. High frequency momentum indicator. Variation 4."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v005_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 5. High frequency momentum indicator. Variation 5."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v006_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 6. High frequency momentum indicator. Variation 6."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v007_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 7. High frequency momentum indicator. Variation 7."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v008_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 8. High frequency momentum indicator. Variation 8."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v009_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 9. High frequency momentum indicator. Variation 9."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v010_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 10. High frequency momentum indicator. Variation 10."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v011_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 11. High frequency momentum indicator. Variation 11."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v012_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 12. High frequency momentum indicator. Variation 12."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v013_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 13. High frequency momentum indicator. Variation 13."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v014_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 14. High frequency momentum indicator. Variation 14."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v015_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 15. High frequency momentum indicator. Variation 15."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v016_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 16. High frequency momentum indicator. Variation 16."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v017_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 17. High frequency momentum indicator. Variation 17."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v018_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 18. High frequency momentum indicator. Variation 18."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v019_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 19. High frequency momentum indicator. Variation 19."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v020_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 20. High frequency momentum indicator. Variation 20."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v021_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 21. High frequency momentum indicator. Variation 21."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v022_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 22. High frequency momentum indicator. Variation 22."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v023_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 23. High frequency momentum indicator. Variation 23."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v024_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 24. High frequency momentum indicator. Variation 24."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v025_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 25. High frequency momentum indicator. Variation 25."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v026_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 26. High frequency momentum indicator. Variation 26."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v027_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 27. High frequency momentum indicator. Variation 27."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v028_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 28. High frequency momentum indicator. Variation 28."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v029_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 29. High frequency momentum indicator. Variation 29."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v030_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 30. High frequency momentum indicator. Variation 30."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v031_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 31. High frequency momentum indicator. Variation 31."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v032_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 32. High frequency momentum indicator. Variation 32."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v033_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 33. High frequency momentum indicator. Variation 33."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v034_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 34. High frequency momentum indicator. Variation 34."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v035_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 35. High frequency momentum indicator. Variation 35."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v036_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 36. High frequency momentum indicator. Variation 36."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v037_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 37. High frequency momentum indicator. Variation 37."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v038_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 38. High frequency momentum indicator. Variation 38."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v039_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 39. High frequency momentum indicator. Variation 39."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v040_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 40. High frequency momentum indicator. Variation 40."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v041_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 41. High frequency momentum indicator. Variation 41."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v042_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 42. High frequency momentum indicator. Variation 42."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v043_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 43. High frequency momentum indicator. Variation 43."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v044_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 44. High frequency momentum indicator. Variation 44."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v045_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 45. High frequency momentum indicator. Variation 45."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v046_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 46. High frequency momentum indicator. Variation 46."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v047_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 47. High frequency momentum indicator. Variation 47."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v048_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 48. High frequency momentum indicator. Variation 48."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v049_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 49. High frequency momentum indicator. Variation 49."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v050_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 50. High frequency momentum indicator. Variation 50."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v051_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 51. High frequency momentum indicator. Variation 51."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v052_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 52. High frequency momentum indicator. Variation 52."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v053_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 53. High frequency momentum indicator. Variation 53."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v054_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 54. High frequency momentum indicator. Variation 54."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v055_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 55. High frequency momentum indicator. Variation 55."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v056_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 56. High frequency momentum indicator. Variation 56."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v057_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 57. High frequency momentum indicator. Variation 57."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v058_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 58. High frequency momentum indicator. Variation 58."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v059_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 59. High frequency momentum indicator. Variation 59."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v060_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 60. High frequency momentum indicator. Variation 60."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v061_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 61. High frequency momentum indicator. Variation 61."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v062_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 62. High frequency momentum indicator. Variation 62."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v063_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 63. High frequency momentum indicator. Variation 63."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v064_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 64. High frequency momentum indicator. Variation 64."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v065_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 65. High frequency momentum indicator. Variation 65."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v066_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 66. High frequency momentum indicator. Variation 66."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v067_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 67. High frequency momentum indicator. Variation 67."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v068_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 68. High frequency momentum indicator. Variation 68."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v069_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 69. High frequency momentum indicator. Variation 69."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v070_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 70. High frequency momentum indicator. Variation 70."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v071_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 71. High frequency momentum indicator. Variation 71."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v072_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 72. High frequency momentum indicator. Variation 72."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v073_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 73. High frequency momentum indicator. Variation 73."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v074_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 74. High frequency momentum indicator. Variation 74."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v075_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 75. High frequency momentum indicator. Variation 75."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v076_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 76. High frequency momentum indicator. Variation 76."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v077_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 77. High frequency momentum indicator. Variation 77."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v078_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 78. High frequency momentum indicator. Variation 78."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v079_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 79. High frequency momentum indicator. Variation 79."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v080_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 80. High frequency momentum indicator. Variation 80."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v081_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 81. High frequency momentum indicator. Variation 81."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v082_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 82. High frequency momentum indicator. Variation 82."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v083_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 83. High frequency momentum indicator. Variation 83."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v084_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 84. High frequency momentum indicator. Variation 84."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v085_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 85. High frequency momentum indicator. Variation 85."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v086_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 86. High frequency momentum indicator. Variation 86."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v087_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 87. High frequency momentum indicator. Variation 87."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v088_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 88. High frequency momentum indicator. Variation 88."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v089_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 89. High frequency momentum indicator. Variation 89."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v090_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 90. High frequency momentum indicator. Variation 90."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v091_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 91. High frequency momentum indicator. Variation 91."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v092_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 92. High frequency momentum indicator. Variation 92."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v093_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 93. High frequency momentum indicator. Variation 93."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v094_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 94. High frequency momentum indicator. Variation 94."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v095_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 95. High frequency momentum indicator. Variation 95."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v096_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 96. High frequency momentum indicator. Variation 96."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v097_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 97. High frequency momentum indicator. Variation 97."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v098_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 98. High frequency momentum indicator. Variation 98."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v099_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 99. High frequency momentum indicator. Variation 99."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v100_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 100. High frequency momentum indicator. Variation 100."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v101_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 101. High frequency momentum indicator. Variation 101."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v102_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 102. High frequency momentum indicator. Variation 102."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v103_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 103. High frequency momentum indicator. Variation 103."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v104_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 104. High frequency momentum indicator. Variation 104."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v105_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 105. High frequency momentum indicator. Variation 105."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v106_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 106. High frequency momentum indicator. Variation 106."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v107_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 107. High frequency momentum indicator. Variation 107."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v108_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 108. High frequency momentum indicator. Variation 108."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v109_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 109. High frequency momentum indicator. Variation 109."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v110_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 110. High frequency momentum indicator. Variation 110."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v111_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 111. High frequency momentum indicator. Variation 111."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v112_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 112. High frequency momentum indicator. Variation 112."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v113_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 113. High frequency momentum indicator. Variation 113."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v114_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 114. High frequency momentum indicator. Variation 114."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v115_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 115. High frequency momentum indicator. Variation 115."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v116_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 116. High frequency momentum indicator. Variation 116."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v117_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 117. High frequency momentum indicator. Variation 117."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v118_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 118. High frequency momentum indicator. Variation 118."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v119_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 119. High frequency momentum indicator. Variation 119."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v120_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 120. High frequency momentum indicator. Variation 120."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v121_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 121. High frequency momentum indicator. Variation 121."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v122_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 122. High frequency momentum indicator. Variation 122."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v123_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 123. High frequency momentum indicator. Variation 123."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v124_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 124. High frequency momentum indicator. Variation 124."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v125_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 125. High frequency momentum indicator. Variation 125."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v126_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 126. High frequency momentum indicator. Variation 126."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v127_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 127. High frequency momentum indicator. Variation 127."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v128_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 128. High frequency momentum indicator. Variation 128."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v129_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 129. High frequency momentum indicator. Variation 129."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v130_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 130. High frequency momentum indicator. Variation 130."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v131_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 131. High frequency momentum indicator. Variation 131."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v132_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 132. High frequency momentum indicator. Variation 132."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v133_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 133. High frequency momentum indicator. Variation 133."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v134_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 134. High frequency momentum indicator. Variation 134."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v135_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 135. High frequency momentum indicator. Variation 135."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v136_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 136. High frequency momentum indicator. Variation 136."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v137_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 137. High frequency momentum indicator. Variation 137."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v138_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 138. High frequency momentum indicator. Variation 138."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v139_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 139. High frequency momentum indicator. Variation 139."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v140_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 140. High frequency momentum indicator. Variation 140."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v141_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 141. High frequency momentum indicator. Variation 141."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v142_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 142. High frequency momentum indicator. Variation 142."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v143_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 143. High frequency momentum indicator. Variation 143."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v144_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 144. High frequency momentum indicator. Variation 144."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v145_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 145. High frequency momentum indicator. Variation 145."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v146_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 146. High frequency momentum indicator. Variation 146."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v147_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 147. High frequency momentum indicator. Variation 147."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v148_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 148. High frequency momentum indicator. Variation 148."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v149_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 149. High frequency momentum indicator. Variation 149."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_cash_flow_jerk_jerk_deriv_v150_signal(ncfo) -> pd.Series:
    """Derivative of cash flow jerk variation 150. High frequency momentum indicator. Variation 150."""
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, 6)
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
F36_CASH_FLOW_JERK_REGISTRY_JERK_001_150 = REGISTRY
