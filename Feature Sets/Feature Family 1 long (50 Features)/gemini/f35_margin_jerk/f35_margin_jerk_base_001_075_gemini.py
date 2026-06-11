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

def f35_margin_jerk_opinc_margin_jerk_5d_21d_5d_v001_signal(opinc, revenue) -> pd.Series:
    """Margin Jerk for opinc over 5d, 21d, 5d. This captures the second order change in margin momentum. Variation 1."""
    margin = _mj_margin(opinc, revenue)
    res = _mj_jerk(margin, 5, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_5d_21d_5d_v002_signal(ebitda, revenue) -> pd.Series:
    """Margin Jerk for ebitda over 5d, 21d, 5d. This captures the second order change in margin momentum. Variation 2."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_jerk(margin, 5, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_10d_21d_10d_v003_signal(opinc, revenue) -> pd.Series:
    """Margin Jerk for opinc over 10d, 21d, 10d. This captures the second order change in margin momentum. Variation 3."""
    margin = _mj_margin(opinc, revenue)
    res = _mj_jerk(margin, 10, 21, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_10d_21d_10d_v004_signal(ebitda, revenue) -> pd.Series:
    """Margin Jerk for ebitda over 10d, 21d, 10d. This captures the second order change in margin momentum. Variation 4."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_jerk(margin, 10, 21, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_21d_42d_21d_v005_signal(opinc, revenue) -> pd.Series:
    """Margin Jerk for opinc over 21d, 42d, 21d. This captures the second order change in margin momentum. Variation 5."""
    margin = _mj_margin(opinc, revenue)
    res = _mj_jerk(margin, 21, 42, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_21d_42d_21d_v006_signal(ebitda, revenue) -> pd.Series:
    """Margin Jerk for ebitda over 21d, 42d, 21d. This captures the second order change in margin momentum. Variation 6."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_jerk(margin, 21, 42, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_63d_126d_63d_v007_signal(opinc, revenue) -> pd.Series:
    """Margin Jerk for opinc over 63d, 126d, 63d. This captures the second order change in margin momentum. Variation 7."""
    margin = _mj_margin(opinc, revenue)
    res = _mj_jerk(margin, 63, 126, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_63d_126d_63d_v008_signal(ebitda, revenue) -> pd.Series:
    """Margin Jerk for ebitda over 63d, 126d, 63d. This captures the second order change in margin momentum. Variation 8."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_jerk(margin, 63, 126, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v009_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 9. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v010_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 10. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v011_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 11. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v012_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 12. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v013_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 13. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v014_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 14. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v015_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 15. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v016_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 16. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v017_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 17. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v018_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 18. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v019_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 19. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v020_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 20. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v021_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 21. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v022_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 22. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v023_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 23. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v024_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 24. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v025_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 25. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v026_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 26. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v027_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 27. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v028_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 28. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v029_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 29. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v030_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 30. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v031_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 31. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v032_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 32. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v033_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 33. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v034_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 34. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v035_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 35. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v036_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 36. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v037_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 37. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v038_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 38. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v039_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 39. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v040_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 40. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v041_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 41. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v042_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 42. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v043_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 43. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v044_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 44. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v045_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 45. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v046_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 46. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v047_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 47. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v048_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 48. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v049_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 49. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v050_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 50. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v051_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 51. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v052_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 52. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v053_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 53. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v054_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 54. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v055_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 55. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v056_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 56. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v057_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 57. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v058_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 58. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v059_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 59. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v060_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 60. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v061_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 61. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v062_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 62. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v063_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 63. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 84)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v064_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 64. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v065_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 65. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 86)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v066_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 66. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 87)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v067_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 67. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 88)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v068_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 68. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 89)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v069_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 69. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 90)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v070_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 70. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 91)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v071_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 71. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 92)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v072_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 72. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 93)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v073_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 73. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 94)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v074_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 74. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_zscore_v075_signal(opinc, revenue) -> pd.Series:
    """Z-score of margin jerk variation 75. Captures statistical significance of margin momentum changes."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 21, 21)
    res = _mj_zscore(jerk, 96)
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
F35_MARGIN_JERK_REGISTRY_BASE_001_075 = REGISTRY
