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

def f35_margin_jerk_opinc_margin_jerk_slope_5d_v001_signal(opinc, revenue) -> pd.Series:
    """Slope of margin jerk for opinc with window 5d. Variation 1."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 5, 10, 5)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_slope_5d_v002_signal(ebitda, revenue) -> pd.Series:
    """Slope of margin jerk for ebitda with window 5d. Variation 2."""
    margin = _mj_margin(ebitda, revenue)
    jerk = _mj_jerk(margin, 5, 10, 5)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_slope_5d_v003_signal(opinc, revenue) -> pd.Series:
    """Slope of margin jerk for opinc with window 5d. Variation 3."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 21, 10)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_slope_5d_v004_signal(ebitda, revenue) -> pd.Series:
    """Slope of margin jerk for ebitda with window 5d. Variation 4."""
    margin = _mj_margin(ebitda, revenue)
    jerk = _mj_jerk(margin, 10, 21, 10)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_slope_5d_v005_signal(opinc, revenue) -> pd.Series:
    """Slope of margin jerk for opinc with window 5d. Variation 5."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 42, 21)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_slope_5d_v006_signal(ebitda, revenue) -> pd.Series:
    """Slope of margin jerk for ebitda with window 5d. Variation 6."""
    margin = _mj_margin(ebitda, revenue)
    jerk = _mj_jerk(margin, 21, 42, 21)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_slope_5d_v007_signal(opinc, revenue) -> pd.Series:
    """Slope of margin jerk for opinc with window 5d. Variation 7."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 63, 63, 63)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_slope_5d_v008_signal(ebitda, revenue) -> pd.Series:
    """Slope of margin jerk for ebitda with window 5d. Variation 8."""
    margin = _mj_margin(ebitda, revenue)
    jerk = _mj_jerk(margin, 63, 63, 63)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_slope_21d_v009_signal(opinc, revenue) -> pd.Series:
    """Slope of margin jerk for opinc with window 21d. Variation 9."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 5, 10, 5)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_slope_21d_v010_signal(ebitda, revenue) -> pd.Series:
    """Slope of margin jerk for ebitda with window 21d. Variation 10."""
    margin = _mj_margin(ebitda, revenue)
    jerk = _mj_jerk(margin, 5, 10, 5)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_slope_21d_v011_signal(opinc, revenue) -> pd.Series:
    """Slope of margin jerk for opinc with window 21d. Variation 11."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 21, 10)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_slope_21d_v012_signal(ebitda, revenue) -> pd.Series:
    """Slope of margin jerk for ebitda with window 21d. Variation 12."""
    margin = _mj_margin(ebitda, revenue)
    jerk = _mj_jerk(margin, 10, 21, 10)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_slope_21d_v013_signal(opinc, revenue) -> pd.Series:
    """Slope of margin jerk for opinc with window 21d. Variation 13."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 21, 42, 21)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_slope_21d_v014_signal(ebitda, revenue) -> pd.Series:
    """Slope of margin jerk for ebitda with window 21d. Variation 14."""
    margin = _mj_margin(ebitda, revenue)
    jerk = _mj_jerk(margin, 21, 42, 21)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_opinc_margin_jerk_slope_21d_v015_signal(opinc, revenue) -> pd.Series:
    """Slope of margin jerk for opinc with window 21d. Variation 15."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 63, 63, 63)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_ebitda_margin_jerk_slope_21d_v016_signal(ebitda, revenue) -> pd.Series:
    """Slope of margin jerk for ebitda with window 21d. Variation 16."""
    margin = _mj_margin(ebitda, revenue)
    jerk = _mj_jerk(margin, 63, 63, 63)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v017_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 22."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v018_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 23."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v019_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 24."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v020_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 25."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v021_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 26."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v022_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 27."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v023_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 28."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v024_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 29."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v025_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 30."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v026_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 31."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v027_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 32."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v028_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 33."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v029_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 34."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v030_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 35."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v031_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 36."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v032_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 37."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v033_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 38."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v034_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 39."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v035_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 40."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v036_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 41."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v037_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 42."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v038_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 43."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v039_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 44."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v040_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 45."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v041_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 46."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v042_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 47."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v043_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 48."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v044_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 49."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v045_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 50."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v046_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 51."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v047_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 52."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v048_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 53."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v049_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 54."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v050_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 55."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v051_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 56."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v052_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 57."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v053_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 58."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v054_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 59."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v055_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 60."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v056_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 61."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v057_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 62."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v058_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 63."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v059_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 64."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v060_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 65."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v061_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 66."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v062_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 67."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v063_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 5."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v064_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 6."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v065_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 7."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v066_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 8."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v067_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 9."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v068_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 10."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v069_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 11."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v070_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 12."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v071_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 13."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v072_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 14."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v073_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 15."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v074_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 16."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v075_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 17."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v076_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 18."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v077_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 19."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v078_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 20."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v079_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 21."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v080_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 22."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v081_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 23."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v082_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 24."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v083_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 25."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v084_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 26."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v085_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 27."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v086_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 28."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v087_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 29."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v088_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 30."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v089_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 31."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v090_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 32."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v091_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 33."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v092_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 34."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v093_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 35."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v094_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 36."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v095_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 37."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v096_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 38."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v097_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 39."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v098_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 40."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v099_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 41."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v100_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 42."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v101_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 43."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v102_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 44."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v103_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 45."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v104_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 46."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v105_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 47."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v106_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 48."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v107_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 49."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v108_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 50."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v109_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 51."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v110_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 52."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v111_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 53."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v112_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 54."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v113_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 55."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v114_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 56."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v115_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 57."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v116_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 58."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v117_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 59."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v118_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 60."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v119_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 61."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v120_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 62."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v121_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 63."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v122_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 64."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v123_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 65."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v124_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 66."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v125_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 67."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v126_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 5."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v127_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 6."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v128_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 7."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v129_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 8."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v130_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 9."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 9)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v131_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 10."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v132_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 11."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v133_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 12."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v134_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 13."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v135_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 14."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v136_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 15."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v137_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 16."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v138_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 17."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 17)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v139_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 18."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v140_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 19."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v141_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 20."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 20)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v142_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 21."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v143_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 22."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v144_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 23."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v145_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 24."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v146_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 25."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v147_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 26."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v148_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 27."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v149_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 28."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_slope_fill_v150_signal(opinc, revenue) -> pd.Series:
    """Filling slope variations to reach 150. Window 29."""
    margin = _mj_margin(opinc, revenue)
    jerk = _mj_jerk(margin, 10, 10, 10)
    res = _mj_slope(jerk, 29)
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
F35_MARGIN_JERK_REGISTRY_SLOPE_001_150 = REGISTRY
