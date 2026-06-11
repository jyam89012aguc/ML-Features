import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _pgk_parkinson(high, low, w):
    lhl = np.log(high / low.replace(0, np.nan))
    return np.sqrt(lhl.pow(2).rolling(w, min_periods=max(1, w//2)).mean() / (4 * np.log(2))) * np.sqrt(252)
def _pgk_garman_klass(open_, high, low, close, w):
    lhl = np.log(high / low.replace(0, np.nan))
    lco = np.log(close / open_.replace(0, np.nan))
    gk = 0.5 * lhl.pow(2) - (2 * np.log(2) - 1) * lco.pow(2)
    return np.sqrt(gk.rolling(w, min_periods=max(1, w//2)).mean() * 252)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5_5d_slope_v001_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21_21d_slope_v002_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63_63d_slope_v003_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5_5d_slope_v004_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21_21d_slope_v005_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63_63d_slope_v006_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5_5d_slope_v007_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21_21d_slope_v008_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63_63d_slope_v009_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5_5d_slope_v010_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21_21d_slope_v011_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63_63d_slope_v012_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v1_5d_slope_v013_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v1_21d_slope_v014_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v1_63d_slope_v015_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v1_5d_slope_v016_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v1_21d_slope_v017_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v1_63d_slope_v018_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v1_5d_slope_v019_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v1_21d_slope_v020_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v1_63d_slope_v021_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v1_5d_slope_v022_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v1_21d_slope_v023_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v1_63d_slope_v024_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v2_5d_slope_v025_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v2_21d_slope_v026_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v2_63d_slope_v027_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v2_5d_slope_v028_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v2_21d_slope_v029_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v2_63d_slope_v030_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v2_5d_slope_v031_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v2_21d_slope_v032_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v2_63d_slope_v033_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v2_5d_slope_v034_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v2_21d_slope_v035_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v2_63d_slope_v036_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v3_5d_slope_v037_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v3_21d_slope_v038_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v3_63d_slope_v039_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v3_5d_slope_v040_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v3_21d_slope_v041_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v3_63d_slope_v042_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v3_5d_slope_v043_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v3_21d_slope_v044_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v3_63d_slope_v045_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v3_5d_slope_v046_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v3_21d_slope_v047_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v3_63d_slope_v048_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v4_5d_slope_v049_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v4_21d_slope_v050_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v4_63d_slope_v051_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v4_5d_slope_v052_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v4_21d_slope_v053_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v4_63d_slope_v054_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v4_5d_slope_v055_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v4_21d_slope_v056_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v4_63d_slope_v057_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v4_5d_slope_v058_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v4_21d_slope_v059_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v4_63d_slope_v060_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v5_5d_slope_v061_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v5_21d_slope_v062_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v5_63d_slope_v063_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v5_5d_slope_v064_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v5_21d_slope_v065_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v5_63d_slope_v066_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v5_5d_slope_v067_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v5_21d_slope_v068_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v5_63d_slope_v069_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v5_5d_slope_v070_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v5_21d_slope_v071_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v5_63d_slope_v072_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v6_5d_slope_v073_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v6_21d_slope_v074_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v6_63d_slope_v075_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v6_5d_slope_v076_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v6_21d_slope_v077_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v6_63d_slope_v078_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v6_5d_slope_v079_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v6_21d_slope_v080_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v6_63d_slope_v081_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v6_5d_slope_v082_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v6_21d_slope_v083_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v6_63d_slope_v084_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v7_5d_slope_v085_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v7_21d_slope_v086_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v7_63d_slope_v087_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v7_5d_slope_v088_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v7_21d_slope_v089_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v7_63d_slope_v090_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v7_5d_slope_v091_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v7_21d_slope_v092_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v7_63d_slope_v093_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v7_5d_slope_v094_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v7_21d_slope_v095_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v7_63d_slope_v096_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v8_5d_slope_v097_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v8_21d_slope_v098_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v8_63d_slope_v099_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v8_5d_slope_v100_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v8_21d_slope_v101_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v8_63d_slope_v102_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v8_5d_slope_v103_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v8_21d_slope_v104_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v8_63d_slope_v105_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v8_5d_slope_v106_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v8_21d_slope_v107_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v8_63d_slope_v108_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v9_5d_slope_v109_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v9_21d_slope_v110_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v9_63d_slope_v111_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v9_5d_slope_v112_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v9_21d_slope_v113_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v9_63d_slope_v114_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v9_5d_slope_v115_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v9_21d_slope_v116_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v9_63d_slope_v117_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v9_5d_slope_v118_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v9_21d_slope_v119_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v9_63d_slope_v120_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v10_5d_slope_v121_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v10_21d_slope_v122_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v10_63d_slope_v123_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v10_5d_slope_v124_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v10_21d_slope_v125_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v10_63d_slope_v126_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v10_5d_slope_v127_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v10_21d_slope_v128_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v10_63d_slope_v129_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v10_5d_slope_v130_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v10_21d_slope_v131_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v10_63d_slope_v132_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v11_5d_slope_v133_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v11_21d_slope_v134_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v11_63d_slope_v135_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v11_5d_slope_v136_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v11_21d_slope_v137_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v11_63d_slope_v138_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s63r5v11_5d_slope_v139_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s63r21v11_21d_slope_v140_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s63r63v11_63d_slope_v141_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 63)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s126r5v11_5d_slope_v142_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s126r21v11_21d_slope_v143_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s126r63v11_63d_slope_v144_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 126)
    result=_z(b.pct_change(63),252)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s5r5v12_5d_slope_v145_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s5r21v12_21d_slope_v146_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s5r63v12_63d_slope_v147_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 5)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_s21r5v12_5d_slope_v148_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_s21r21v12_21d_slope_v149_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_s21r63v12_63d_slope_v150_signal(open_, high, low, close):
    b=_pgk_parkinson(high, low, 21)
    result=b.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)


REGISTRY = {
    "f18pgk_parkinson_garman_klass_estimators_s5r5_5d_slope_v001_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5_5d_slope_v001_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21_21d_slope_v002_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21_21d_slope_v002_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63_63d_slope_v003_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63_63d_slope_v003_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5_5d_slope_v004_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5_5d_slope_v004_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21_21d_slope_v005_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21_21d_slope_v005_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63_63d_slope_v006_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63_63d_slope_v006_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5_5d_slope_v007_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5_5d_slope_v007_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21_21d_slope_v008_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21_21d_slope_v008_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63_63d_slope_v009_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63_63d_slope_v009_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5_5d_slope_v010_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5_5d_slope_v010_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21_21d_slope_v011_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21_21d_slope_v011_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63_63d_slope_v012_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63_63d_slope_v012_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v1_5d_slope_v013_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v1_5d_slope_v013_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v1_21d_slope_v014_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v1_21d_slope_v014_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v1_63d_slope_v015_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v1_63d_slope_v015_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v1_5d_slope_v016_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v1_5d_slope_v016_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v1_21d_slope_v017_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v1_21d_slope_v017_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v1_63d_slope_v018_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v1_63d_slope_v018_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v1_5d_slope_v019_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v1_5d_slope_v019_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v1_21d_slope_v020_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v1_21d_slope_v020_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v1_63d_slope_v021_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v1_63d_slope_v021_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v1_5d_slope_v022_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v1_5d_slope_v022_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v1_21d_slope_v023_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v1_21d_slope_v023_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v1_63d_slope_v024_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v1_63d_slope_v024_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v2_5d_slope_v025_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v2_5d_slope_v025_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v2_21d_slope_v026_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v2_21d_slope_v026_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v2_63d_slope_v027_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v2_63d_slope_v027_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v2_5d_slope_v028_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v2_5d_slope_v028_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v2_21d_slope_v029_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v2_21d_slope_v029_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v2_63d_slope_v030_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v2_63d_slope_v030_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v2_5d_slope_v031_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v2_5d_slope_v031_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v2_21d_slope_v032_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v2_21d_slope_v032_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v2_63d_slope_v033_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v2_63d_slope_v033_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v2_5d_slope_v034_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v2_5d_slope_v034_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v2_21d_slope_v035_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v2_21d_slope_v035_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v2_63d_slope_v036_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v2_63d_slope_v036_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v3_5d_slope_v037_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v3_5d_slope_v037_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v3_21d_slope_v038_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v3_21d_slope_v038_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v3_63d_slope_v039_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v3_63d_slope_v039_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v3_5d_slope_v040_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v3_5d_slope_v040_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v3_21d_slope_v041_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v3_21d_slope_v041_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v3_63d_slope_v042_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v3_63d_slope_v042_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v3_5d_slope_v043_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v3_5d_slope_v043_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v3_21d_slope_v044_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v3_21d_slope_v044_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v3_63d_slope_v045_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v3_63d_slope_v045_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v3_5d_slope_v046_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v3_5d_slope_v046_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v3_21d_slope_v047_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v3_21d_slope_v047_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v3_63d_slope_v048_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v3_63d_slope_v048_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v4_5d_slope_v049_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v4_5d_slope_v049_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v4_21d_slope_v050_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v4_21d_slope_v050_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v4_63d_slope_v051_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v4_63d_slope_v051_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v4_5d_slope_v052_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v4_5d_slope_v052_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v4_21d_slope_v053_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v4_21d_slope_v053_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v4_63d_slope_v054_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v4_63d_slope_v054_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v4_5d_slope_v055_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v4_5d_slope_v055_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v4_21d_slope_v056_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v4_21d_slope_v056_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v4_63d_slope_v057_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v4_63d_slope_v057_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v4_5d_slope_v058_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v4_5d_slope_v058_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v4_21d_slope_v059_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v4_21d_slope_v059_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v4_63d_slope_v060_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v4_63d_slope_v060_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v5_5d_slope_v061_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v5_5d_slope_v061_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v5_21d_slope_v062_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v5_21d_slope_v062_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v5_63d_slope_v063_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v5_63d_slope_v063_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v5_5d_slope_v064_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v5_5d_slope_v064_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v5_21d_slope_v065_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v5_21d_slope_v065_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v5_63d_slope_v066_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v5_63d_slope_v066_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v5_5d_slope_v067_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v5_5d_slope_v067_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v5_21d_slope_v068_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v5_21d_slope_v068_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v5_63d_slope_v069_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v5_63d_slope_v069_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v5_5d_slope_v070_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v5_5d_slope_v070_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v5_21d_slope_v071_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v5_21d_slope_v071_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v5_63d_slope_v072_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v5_63d_slope_v072_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v6_5d_slope_v073_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v6_5d_slope_v073_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v6_21d_slope_v074_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v6_21d_slope_v074_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v6_63d_slope_v075_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v6_63d_slope_v075_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v6_5d_slope_v076_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v6_5d_slope_v076_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v6_21d_slope_v077_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v6_21d_slope_v077_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v6_63d_slope_v078_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v6_63d_slope_v078_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v6_5d_slope_v079_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v6_5d_slope_v079_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v6_21d_slope_v080_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v6_21d_slope_v080_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v6_63d_slope_v081_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v6_63d_slope_v081_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v6_5d_slope_v082_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v6_5d_slope_v082_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v6_21d_slope_v083_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v6_21d_slope_v083_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v6_63d_slope_v084_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v6_63d_slope_v084_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v7_5d_slope_v085_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v7_5d_slope_v085_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v7_21d_slope_v086_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v7_21d_slope_v086_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v7_63d_slope_v087_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v7_63d_slope_v087_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v7_5d_slope_v088_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v7_5d_slope_v088_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v7_21d_slope_v089_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v7_21d_slope_v089_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v7_63d_slope_v090_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v7_63d_slope_v090_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v7_5d_slope_v091_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v7_5d_slope_v091_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v7_21d_slope_v092_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v7_21d_slope_v092_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v7_63d_slope_v093_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v7_63d_slope_v093_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v7_5d_slope_v094_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v7_5d_slope_v094_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v7_21d_slope_v095_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v7_21d_slope_v095_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v7_63d_slope_v096_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v7_63d_slope_v096_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v8_5d_slope_v097_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v8_5d_slope_v097_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v8_21d_slope_v098_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v8_21d_slope_v098_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v8_63d_slope_v099_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v8_63d_slope_v099_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v8_5d_slope_v100_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v8_5d_slope_v100_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v8_21d_slope_v101_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v8_21d_slope_v101_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v8_63d_slope_v102_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v8_63d_slope_v102_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v8_5d_slope_v103_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v8_5d_slope_v103_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v8_21d_slope_v104_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v8_21d_slope_v104_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v8_63d_slope_v105_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v8_63d_slope_v105_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v8_5d_slope_v106_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v8_5d_slope_v106_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v8_21d_slope_v107_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v8_21d_slope_v107_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v8_63d_slope_v108_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v8_63d_slope_v108_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v9_5d_slope_v109_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v9_5d_slope_v109_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v9_21d_slope_v110_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v9_21d_slope_v110_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v9_63d_slope_v111_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v9_63d_slope_v111_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v9_5d_slope_v112_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v9_5d_slope_v112_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v9_21d_slope_v113_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v9_21d_slope_v113_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v9_63d_slope_v114_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v9_63d_slope_v114_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v9_5d_slope_v115_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v9_5d_slope_v115_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v9_21d_slope_v116_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v9_21d_slope_v116_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v9_63d_slope_v117_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v9_63d_slope_v117_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v9_5d_slope_v118_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v9_5d_slope_v118_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v9_21d_slope_v119_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v9_21d_slope_v119_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v9_63d_slope_v120_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v9_63d_slope_v120_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v10_5d_slope_v121_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v10_5d_slope_v121_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v10_21d_slope_v122_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v10_21d_slope_v122_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v10_63d_slope_v123_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v10_63d_slope_v123_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v10_5d_slope_v124_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v10_5d_slope_v124_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v10_21d_slope_v125_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v10_21d_slope_v125_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v10_63d_slope_v126_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v10_63d_slope_v126_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v10_5d_slope_v127_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v10_5d_slope_v127_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v10_21d_slope_v128_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v10_21d_slope_v128_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v10_63d_slope_v129_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v10_63d_slope_v129_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v10_5d_slope_v130_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v10_5d_slope_v130_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v10_21d_slope_v131_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v10_21d_slope_v131_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v10_63d_slope_v132_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v10_63d_slope_v132_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v11_5d_slope_v133_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v11_5d_slope_v133_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v11_21d_slope_v134_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v11_21d_slope_v134_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v11_63d_slope_v135_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v11_63d_slope_v135_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v11_5d_slope_v136_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v11_5d_slope_v136_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v11_21d_slope_v137_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v11_21d_slope_v137_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v11_63d_slope_v138_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v11_63d_slope_v138_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r5v11_5d_slope_v139_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r5v11_5d_slope_v139_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r21v11_21d_slope_v140_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r21v11_21d_slope_v140_signal},
    "f18pgk_parkinson_garman_klass_estimators_s63r63v11_63d_slope_v141_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s63r63v11_63d_slope_v141_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r5v11_5d_slope_v142_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r5v11_5d_slope_v142_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r21v11_21d_slope_v143_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r21v11_21d_slope_v143_signal},
    "f18pgk_parkinson_garman_klass_estimators_s126r63v11_63d_slope_v144_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s126r63v11_63d_slope_v144_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r5v12_5d_slope_v145_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r5v12_5d_slope_v145_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r21v12_21d_slope_v146_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r21v12_21d_slope_v146_signal},
    "f18pgk_parkinson_garman_klass_estimators_s5r63v12_63d_slope_v147_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s5r63v12_63d_slope_v147_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r5v12_5d_slope_v148_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r5v12_5d_slope_v148_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r21v12_21d_slope_v149_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r21v12_21d_slope_v149_signal},
    "f18pgk_parkinson_garman_klass_estimators_s21r63v12_63d_slope_v150_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_s21r63v12_63d_slope_v150_signal}
}
F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_SLOPE = REGISTRY

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    idx = pd.date_range("2020-01-01", periods=n, freq="B")
    closeadj = pd.Series(100 * np.exp(np.random.normal(0, 0.01, n).cumsum()), index=idx)
    close = closeadj * (1 + np.random.normal(0, 0.001, n))
    high = close * (1 + np.abs(np.random.normal(0, 0.005, n)))
    low = close * (1 - np.abs(np.random.normal(0, 0.005, n)))
    open_ = close.shift(1).fillna(close.iloc[0])
    volume = pd.Series(np.random.lognormal(15, 0.5, n), index=idx)
    bench = pd.Series(100 * np.exp(np.random.normal(0, 0.009, n).cumsum()), index=idx)
    args_pool = dict(closeadj=closeadj, close=close, high=high, low=low,
                     open_=open_, volume=volume, bench=bench)
    nan_fracs = []
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [args_pool.get(c, closeadj) for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2, check_names=False)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, f"{name}: empty after warm-up"
        assert q.std() > 0, f"{name}: constant output"
        src = inspect.getsource(fn)
        assert "_pgk_parkinson" in src or "_pgk_garman_klass" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_SLOPE")
