import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _mj_margin(num, den):
    return num / den.replace(0, np.nan)

def _mj_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _mj_jerk(s, w1, w2, w3):
    accel = s.pct_change(w1).pct_change(w2)
    return accel.diff(w3)

def _mj_slope(s, w):
    return s.pct_change(w)

def _mj_jerk_deriv(s, w):
    return s.diff(w)

def _mj_zscore(s, w):
    return _z(s, w)

def f35_margin_jerk_jerk_deriv_v001_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 1. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v002_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 2. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v003_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 3. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v004_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 4. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v005_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 5. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v006_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 6. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v007_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 7. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v008_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 8. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v009_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 9. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v010_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 10. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v011_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 11. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v012_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 12. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v013_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 13. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v014_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 14. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v015_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 15. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v016_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 16. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v017_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 17. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v018_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 18. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v019_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 19. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v020_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 20. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v021_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 21. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v022_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 22. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v023_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 23. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v024_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 24. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v025_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 25. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v026_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 26. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v027_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 27. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v028_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 28. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v029_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 29. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v030_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 30. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v031_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 31. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v032_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 32. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v033_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 33. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v034_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 34. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v035_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 35. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v036_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 36. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v037_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 37. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v038_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 38. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v039_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 39. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v040_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 40. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v041_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 41. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v042_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 42. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v043_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 43. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v044_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 44. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v045_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 45. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v046_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 46. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v047_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 47. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v048_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 48. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v049_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 49. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v050_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 50. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v051_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 51. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v052_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 52. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v053_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 53. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v054_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 54. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v055_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 55. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v056_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 56. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v057_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 57. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v058_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 58. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v059_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 59. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v060_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 60. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v061_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 61. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v062_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 62. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v063_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 63. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v064_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 64. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v065_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 65. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v066_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 66. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v067_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 67. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v068_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 68. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v069_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 69. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v070_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 70. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v071_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 71. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v072_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 72. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v073_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 73. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v074_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 74. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v075_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 75. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v076_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 76. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v077_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 77. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v078_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 78. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v079_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 79. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v080_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 80. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v081_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 81. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v082_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 82. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v083_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 83. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v084_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 84. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v085_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 85. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v086_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 86. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v087_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 87. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v088_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 88. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v089_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 89. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v090_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 90. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v091_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 91. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v092_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 92. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v093_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 93. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v094_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 94. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v095_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 95. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v096_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 96. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v097_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 97. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v098_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 98. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v099_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 99. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v100_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 100. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v101_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 101. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v102_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 102. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v103_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 103. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v104_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 104. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v105_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 105. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v106_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 106. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v107_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 107. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v108_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 108. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v109_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 109. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v110_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 110. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v111_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 111. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v112_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 112. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v113_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 113. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v114_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 114. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v115_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 115. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v116_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 116. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v117_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 117. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v118_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 118. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v119_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 119. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v120_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 120. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v121_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 121. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v122_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 122. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v123_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 123. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v124_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 124. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v125_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 125. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v126_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 126. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v127_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 127. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v128_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 128. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v129_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 129. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v130_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 130. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v131_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 131. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v132_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 132. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v133_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 133. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v134_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 134. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v135_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 135. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v136_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 136. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v137_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 137. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v138_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 138. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v139_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 139. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v140_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 140. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v141_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 141. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v142_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 142. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v143_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 143. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v144_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 144. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v145_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 145. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v146_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 146. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v147_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 147. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v148_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 148. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 4)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v149_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 149. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_jerk_deriv_v150_signal(opinc, revenue) -> pd.Series:
    """Derivative of margin jerk variation 150. Higher order momentum indicator."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_jerk_deriv(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum() + 10000,
        "opinc": np.random.normal(100, 20, n).cumsum() + 1000,
        "ebitda": np.random.normal(150, 30, n).cumsum() + 1500,
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f35_margin_jerk_"))]
    
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f35_margin_jerk_"))]}
F35_MARGIN_JERK_REGISTRY_JERK_001_150 = REGISTRY
