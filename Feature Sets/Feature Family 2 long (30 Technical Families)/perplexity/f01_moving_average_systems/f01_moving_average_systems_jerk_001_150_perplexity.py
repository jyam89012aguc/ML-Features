import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _ma_sma(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()
def _ma_ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()
def _ma_ratio(closeadj, w):
    ma = _ma_sma(closeadj, w)
    return (closeadj / ma.replace(0, np.nan)) - 1.0

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5_5d_jerk_v001_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21_21d_jerk_v002_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63_63d_jerk_v003_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5_5d_jerk_v004_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21_21d_jerk_v005_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63_63d_jerk_v006_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=5d
def f01mas_moving_average_systems_j63r5_5d_jerk_v007_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=21d
def f01mas_moving_average_systems_j63r21_21d_jerk_v008_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=63d
def f01mas_moving_average_systems_j63r63_63d_jerk_v009_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=5d
def f01mas_moving_average_systems_j126r5_5d_jerk_v010_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=21d
def f01mas_moving_average_systems_j126r21_21d_jerk_v011_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=63d
def f01mas_moving_average_systems_j126r63_63d_jerk_v012_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=5d
def f01mas_moving_average_systems_j252r5_5d_jerk_v013_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=21d
def f01mas_moving_average_systems_j252r21_21d_jerk_v014_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=63d
def f01mas_moving_average_systems_j252r63_63d_jerk_v015_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=5d
def f01mas_moving_average_systems_j504r5_5d_jerk_v016_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=21d
def f01mas_moving_average_systems_j504r21_21d_jerk_v017_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=63d
def f01mas_moving_average_systems_j504r63_63d_jerk_v018_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5v1_5d_jerk_v019_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21v1_21d_jerk_v020_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63v1_63d_jerk_v021_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5v1_5d_jerk_v022_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21v1_21d_jerk_v023_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63v1_63d_jerk_v024_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=5d
def f01mas_moving_average_systems_j63r5v1_5d_jerk_v025_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=21d
def f01mas_moving_average_systems_j63r21v1_21d_jerk_v026_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=63d
def f01mas_moving_average_systems_j63r63v1_63d_jerk_v027_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=5d
def f01mas_moving_average_systems_j126r5v1_5d_jerk_v028_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=21d
def f01mas_moving_average_systems_j126r21v1_21d_jerk_v029_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=63d
def f01mas_moving_average_systems_j126r63v1_63d_jerk_v030_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=5d
def f01mas_moving_average_systems_j252r5v1_5d_jerk_v031_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=21d
def f01mas_moving_average_systems_j252r21v1_21d_jerk_v032_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=63d
def f01mas_moving_average_systems_j252r63v1_63d_jerk_v033_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=5d
def f01mas_moving_average_systems_j504r5v1_5d_jerk_v034_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=21d
def f01mas_moving_average_systems_j504r21v1_21d_jerk_v035_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=63d
def f01mas_moving_average_systems_j504r63v1_63d_jerk_v036_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5v2_5d_jerk_v037_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21v2_21d_jerk_v038_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63v2_63d_jerk_v039_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5v2_5d_jerk_v040_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21v2_21d_jerk_v041_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63v2_63d_jerk_v042_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=5d
def f01mas_moving_average_systems_j63r5v2_5d_jerk_v043_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=21d
def f01mas_moving_average_systems_j63r21v2_21d_jerk_v044_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=63d
def f01mas_moving_average_systems_j63r63v2_63d_jerk_v045_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=5d
def f01mas_moving_average_systems_j126r5v2_5d_jerk_v046_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=21d
def f01mas_moving_average_systems_j126r21v2_21d_jerk_v047_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=63d
def f01mas_moving_average_systems_j126r63v2_63d_jerk_v048_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=5d
def f01mas_moving_average_systems_j252r5v2_5d_jerk_v049_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=21d
def f01mas_moving_average_systems_j252r21v2_21d_jerk_v050_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=63d
def f01mas_moving_average_systems_j252r63v2_63d_jerk_v051_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=5d
def f01mas_moving_average_systems_j504r5v2_5d_jerk_v052_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=21d
def f01mas_moving_average_systems_j504r21v2_21d_jerk_v053_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=63d
def f01mas_moving_average_systems_j504r63v2_63d_jerk_v054_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5v3_5d_jerk_v055_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21v3_21d_jerk_v056_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63v3_63d_jerk_v057_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5v3_5d_jerk_v058_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21v3_21d_jerk_v059_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63v3_63d_jerk_v060_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=5d
def f01mas_moving_average_systems_j63r5v3_5d_jerk_v061_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=21d
def f01mas_moving_average_systems_j63r21v3_21d_jerk_v062_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=63d
def f01mas_moving_average_systems_j63r63v3_63d_jerk_v063_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=5d
def f01mas_moving_average_systems_j126r5v3_5d_jerk_v064_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=21d
def f01mas_moving_average_systems_j126r21v3_21d_jerk_v065_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=63d
def f01mas_moving_average_systems_j126r63v3_63d_jerk_v066_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=5d
def f01mas_moving_average_systems_j252r5v3_5d_jerk_v067_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=21d
def f01mas_moving_average_systems_j252r21v3_21d_jerk_v068_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=63d
def f01mas_moving_average_systems_j252r63v3_63d_jerk_v069_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=5d
def f01mas_moving_average_systems_j504r5v3_5d_jerk_v070_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=21d
def f01mas_moving_average_systems_j504r21v3_21d_jerk_v071_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=63d
def f01mas_moving_average_systems_j504r63v3_63d_jerk_v072_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5v4_5d_jerk_v073_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21v4_21d_jerk_v074_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63v4_63d_jerk_v075_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5v4_5d_jerk_v076_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21v4_21d_jerk_v077_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63v4_63d_jerk_v078_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=5d
def f01mas_moving_average_systems_j63r5v4_5d_jerk_v079_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=21d
def f01mas_moving_average_systems_j63r21v4_21d_jerk_v080_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=63d
def f01mas_moving_average_systems_j63r63v4_63d_jerk_v081_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=5d
def f01mas_moving_average_systems_j126r5v4_5d_jerk_v082_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=21d
def f01mas_moving_average_systems_j126r21v4_21d_jerk_v083_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=63d
def f01mas_moving_average_systems_j126r63v4_63d_jerk_v084_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=5d
def f01mas_moving_average_systems_j252r5v4_5d_jerk_v085_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=21d
def f01mas_moving_average_systems_j252r21v4_21d_jerk_v086_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=63d
def f01mas_moving_average_systems_j252r63v4_63d_jerk_v087_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=5d
def f01mas_moving_average_systems_j504r5v4_5d_jerk_v088_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=21d
def f01mas_moving_average_systems_j504r21v4_21d_jerk_v089_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=63d
def f01mas_moving_average_systems_j504r63v4_63d_jerk_v090_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5v5_5d_jerk_v091_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21v5_21d_jerk_v092_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63v5_63d_jerk_v093_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5v5_5d_jerk_v094_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21v5_21d_jerk_v095_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63v5_63d_jerk_v096_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=5d
def f01mas_moving_average_systems_j63r5v5_5d_jerk_v097_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=21d
def f01mas_moving_average_systems_j63r21v5_21d_jerk_v098_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=63d
def f01mas_moving_average_systems_j63r63v5_63d_jerk_v099_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=5d
def f01mas_moving_average_systems_j126r5v5_5d_jerk_v100_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=21d
def f01mas_moving_average_systems_j126r21v5_21d_jerk_v101_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=63d
def f01mas_moving_average_systems_j126r63v5_63d_jerk_v102_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=5d
def f01mas_moving_average_systems_j252r5v5_5d_jerk_v103_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=21d
def f01mas_moving_average_systems_j252r21v5_21d_jerk_v104_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=63d
def f01mas_moving_average_systems_j252r63v5_63d_jerk_v105_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=5d
def f01mas_moving_average_systems_j504r5v5_5d_jerk_v106_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=21d
def f01mas_moving_average_systems_j504r21v5_21d_jerk_v107_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=63d
def f01mas_moving_average_systems_j504r63v5_63d_jerk_v108_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5v6_5d_jerk_v109_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21v6_21d_jerk_v110_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63v6_63d_jerk_v111_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5v6_5d_jerk_v112_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21v6_21d_jerk_v113_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63v6_63d_jerk_v114_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=5d
def f01mas_moving_average_systems_j63r5v6_5d_jerk_v115_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=21d
def f01mas_moving_average_systems_j63r21v6_21d_jerk_v116_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=63d
def f01mas_moving_average_systems_j63r63v6_63d_jerk_v117_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=5d
def f01mas_moving_average_systems_j126r5v6_5d_jerk_v118_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=21d
def f01mas_moving_average_systems_j126r21v6_21d_jerk_v119_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=63d
def f01mas_moving_average_systems_j126r63v6_63d_jerk_v120_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=5d
def f01mas_moving_average_systems_j252r5v6_5d_jerk_v121_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=21d
def f01mas_moving_average_systems_j252r21v6_21d_jerk_v122_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=63d
def f01mas_moving_average_systems_j252r63v6_63d_jerk_v123_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=5d
def f01mas_moving_average_systems_j504r5v6_5d_jerk_v124_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=21d
def f01mas_moving_average_systems_j504r21v6_21d_jerk_v125_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=63d
def f01mas_moving_average_systems_j504r63v6_63d_jerk_v126_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5v7_5d_jerk_v127_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21v7_21d_jerk_v128_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63v7_63d_jerk_v129_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5v7_5d_jerk_v130_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21v7_21d_jerk_v131_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63v7_63d_jerk_v132_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=5d
def f01mas_moving_average_systems_j63r5v7_5d_jerk_v133_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=21d
def f01mas_moving_average_systems_j63r21v7_21d_jerk_v134_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=63 roc=63d
def f01mas_moving_average_systems_j63r63v7_63d_jerk_v135_signal(closeadj):
    b=_ma_ratio(closeadj, 63)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=5d
def f01mas_moving_average_systems_j126r5v7_5d_jerk_v136_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=21d
def f01mas_moving_average_systems_j126r21v7_21d_jerk_v137_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=126 roc=63d
def f01mas_moving_average_systems_j126r63v7_63d_jerk_v138_signal(closeadj):
    b=_ma_ratio(closeadj, 126)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=5d
def f01mas_moving_average_systems_j252r5v7_5d_jerk_v139_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=21d
def f01mas_moving_average_systems_j252r21v7_21d_jerk_v140_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=252 roc=63d
def f01mas_moving_average_systems_j252r63v7_63d_jerk_v141_signal(closeadj):
    b=_ma_ratio(closeadj, 252)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=5d
def f01mas_moving_average_systems_j504r5v7_5d_jerk_v142_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=21d
def f01mas_moving_average_systems_j504r21v7_21d_jerk_v143_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=504 roc=63d
def f01mas_moving_average_systems_j504r63v7_63d_jerk_v144_signal(closeadj):
    b=_ma_ratio(closeadj, 504)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=5d
def f01mas_moving_average_systems_j5r5v8_5d_jerk_v145_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=21d
def f01mas_moving_average_systems_j5r21v8_21d_jerk_v146_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=5 roc=63d
def f01mas_moving_average_systems_j5r63v8_63d_jerk_v147_signal(closeadj):
    b=_ma_ratio(closeadj, 5)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=5d
def f01mas_moving_average_systems_j21r5v8_5d_jerk_v148_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=21d
def f01mas_moving_average_systems_j21r21v8_21d_jerk_v149_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _ma_ratio w=21 roc=63d
def f01mas_moving_average_systems_j21r63v8_63d_jerk_v150_signal(closeadj):
    b=_ma_ratio(closeadj, 21)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)


REGISTRY = {
    "f01mas_moving_average_systems_j5r5_5d_jerk_v001_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5_5d_jerk_v001_signal},
    "f01mas_moving_average_systems_j5r21_21d_jerk_v002_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21_21d_jerk_v002_signal},
    "f01mas_moving_average_systems_j5r63_63d_jerk_v003_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63_63d_jerk_v003_signal},
    "f01mas_moving_average_systems_j21r5_5d_jerk_v004_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5_5d_jerk_v004_signal},
    "f01mas_moving_average_systems_j21r21_21d_jerk_v005_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21_21d_jerk_v005_signal},
    "f01mas_moving_average_systems_j21r63_63d_jerk_v006_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63_63d_jerk_v006_signal},
    "f01mas_moving_average_systems_j63r5_5d_jerk_v007_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r5_5d_jerk_v007_signal},
    "f01mas_moving_average_systems_j63r21_21d_jerk_v008_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r21_21d_jerk_v008_signal},
    "f01mas_moving_average_systems_j63r63_63d_jerk_v009_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r63_63d_jerk_v009_signal},
    "f01mas_moving_average_systems_j126r5_5d_jerk_v010_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r5_5d_jerk_v010_signal},
    "f01mas_moving_average_systems_j126r21_21d_jerk_v011_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r21_21d_jerk_v011_signal},
    "f01mas_moving_average_systems_j126r63_63d_jerk_v012_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r63_63d_jerk_v012_signal},
    "f01mas_moving_average_systems_j252r5_5d_jerk_v013_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r5_5d_jerk_v013_signal},
    "f01mas_moving_average_systems_j252r21_21d_jerk_v014_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r21_21d_jerk_v014_signal},
    "f01mas_moving_average_systems_j252r63_63d_jerk_v015_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r63_63d_jerk_v015_signal},
    "f01mas_moving_average_systems_j504r5_5d_jerk_v016_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r5_5d_jerk_v016_signal},
    "f01mas_moving_average_systems_j504r21_21d_jerk_v017_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r21_21d_jerk_v017_signal},
    "f01mas_moving_average_systems_j504r63_63d_jerk_v018_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r63_63d_jerk_v018_signal},
    "f01mas_moving_average_systems_j5r5v1_5d_jerk_v019_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5v1_5d_jerk_v019_signal},
    "f01mas_moving_average_systems_j5r21v1_21d_jerk_v020_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21v1_21d_jerk_v020_signal},
    "f01mas_moving_average_systems_j5r63v1_63d_jerk_v021_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63v1_63d_jerk_v021_signal},
    "f01mas_moving_average_systems_j21r5v1_5d_jerk_v022_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5v1_5d_jerk_v022_signal},
    "f01mas_moving_average_systems_j21r21v1_21d_jerk_v023_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21v1_21d_jerk_v023_signal},
    "f01mas_moving_average_systems_j21r63v1_63d_jerk_v024_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63v1_63d_jerk_v024_signal},
    "f01mas_moving_average_systems_j63r5v1_5d_jerk_v025_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r5v1_5d_jerk_v025_signal},
    "f01mas_moving_average_systems_j63r21v1_21d_jerk_v026_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r21v1_21d_jerk_v026_signal},
    "f01mas_moving_average_systems_j63r63v1_63d_jerk_v027_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r63v1_63d_jerk_v027_signal},
    "f01mas_moving_average_systems_j126r5v1_5d_jerk_v028_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r5v1_5d_jerk_v028_signal},
    "f01mas_moving_average_systems_j126r21v1_21d_jerk_v029_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r21v1_21d_jerk_v029_signal},
    "f01mas_moving_average_systems_j126r63v1_63d_jerk_v030_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r63v1_63d_jerk_v030_signal},
    "f01mas_moving_average_systems_j252r5v1_5d_jerk_v031_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r5v1_5d_jerk_v031_signal},
    "f01mas_moving_average_systems_j252r21v1_21d_jerk_v032_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r21v1_21d_jerk_v032_signal},
    "f01mas_moving_average_systems_j252r63v1_63d_jerk_v033_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r63v1_63d_jerk_v033_signal},
    "f01mas_moving_average_systems_j504r5v1_5d_jerk_v034_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r5v1_5d_jerk_v034_signal},
    "f01mas_moving_average_systems_j504r21v1_21d_jerk_v035_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r21v1_21d_jerk_v035_signal},
    "f01mas_moving_average_systems_j504r63v1_63d_jerk_v036_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r63v1_63d_jerk_v036_signal},
    "f01mas_moving_average_systems_j5r5v2_5d_jerk_v037_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5v2_5d_jerk_v037_signal},
    "f01mas_moving_average_systems_j5r21v2_21d_jerk_v038_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21v2_21d_jerk_v038_signal},
    "f01mas_moving_average_systems_j5r63v2_63d_jerk_v039_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63v2_63d_jerk_v039_signal},
    "f01mas_moving_average_systems_j21r5v2_5d_jerk_v040_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5v2_5d_jerk_v040_signal},
    "f01mas_moving_average_systems_j21r21v2_21d_jerk_v041_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21v2_21d_jerk_v041_signal},
    "f01mas_moving_average_systems_j21r63v2_63d_jerk_v042_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63v2_63d_jerk_v042_signal},
    "f01mas_moving_average_systems_j63r5v2_5d_jerk_v043_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r5v2_5d_jerk_v043_signal},
    "f01mas_moving_average_systems_j63r21v2_21d_jerk_v044_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r21v2_21d_jerk_v044_signal},
    "f01mas_moving_average_systems_j63r63v2_63d_jerk_v045_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r63v2_63d_jerk_v045_signal},
    "f01mas_moving_average_systems_j126r5v2_5d_jerk_v046_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r5v2_5d_jerk_v046_signal},
    "f01mas_moving_average_systems_j126r21v2_21d_jerk_v047_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r21v2_21d_jerk_v047_signal},
    "f01mas_moving_average_systems_j126r63v2_63d_jerk_v048_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r63v2_63d_jerk_v048_signal},
    "f01mas_moving_average_systems_j252r5v2_5d_jerk_v049_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r5v2_5d_jerk_v049_signal},
    "f01mas_moving_average_systems_j252r21v2_21d_jerk_v050_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r21v2_21d_jerk_v050_signal},
    "f01mas_moving_average_systems_j252r63v2_63d_jerk_v051_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r63v2_63d_jerk_v051_signal},
    "f01mas_moving_average_systems_j504r5v2_5d_jerk_v052_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r5v2_5d_jerk_v052_signal},
    "f01mas_moving_average_systems_j504r21v2_21d_jerk_v053_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r21v2_21d_jerk_v053_signal},
    "f01mas_moving_average_systems_j504r63v2_63d_jerk_v054_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r63v2_63d_jerk_v054_signal},
    "f01mas_moving_average_systems_j5r5v3_5d_jerk_v055_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5v3_5d_jerk_v055_signal},
    "f01mas_moving_average_systems_j5r21v3_21d_jerk_v056_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21v3_21d_jerk_v056_signal},
    "f01mas_moving_average_systems_j5r63v3_63d_jerk_v057_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63v3_63d_jerk_v057_signal},
    "f01mas_moving_average_systems_j21r5v3_5d_jerk_v058_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5v3_5d_jerk_v058_signal},
    "f01mas_moving_average_systems_j21r21v3_21d_jerk_v059_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21v3_21d_jerk_v059_signal},
    "f01mas_moving_average_systems_j21r63v3_63d_jerk_v060_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63v3_63d_jerk_v060_signal},
    "f01mas_moving_average_systems_j63r5v3_5d_jerk_v061_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r5v3_5d_jerk_v061_signal},
    "f01mas_moving_average_systems_j63r21v3_21d_jerk_v062_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r21v3_21d_jerk_v062_signal},
    "f01mas_moving_average_systems_j63r63v3_63d_jerk_v063_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r63v3_63d_jerk_v063_signal},
    "f01mas_moving_average_systems_j126r5v3_5d_jerk_v064_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r5v3_5d_jerk_v064_signal},
    "f01mas_moving_average_systems_j126r21v3_21d_jerk_v065_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r21v3_21d_jerk_v065_signal},
    "f01mas_moving_average_systems_j126r63v3_63d_jerk_v066_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r63v3_63d_jerk_v066_signal},
    "f01mas_moving_average_systems_j252r5v3_5d_jerk_v067_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r5v3_5d_jerk_v067_signal},
    "f01mas_moving_average_systems_j252r21v3_21d_jerk_v068_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r21v3_21d_jerk_v068_signal},
    "f01mas_moving_average_systems_j252r63v3_63d_jerk_v069_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r63v3_63d_jerk_v069_signal},
    "f01mas_moving_average_systems_j504r5v3_5d_jerk_v070_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r5v3_5d_jerk_v070_signal},
    "f01mas_moving_average_systems_j504r21v3_21d_jerk_v071_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r21v3_21d_jerk_v071_signal},
    "f01mas_moving_average_systems_j504r63v3_63d_jerk_v072_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r63v3_63d_jerk_v072_signal},
    "f01mas_moving_average_systems_j5r5v4_5d_jerk_v073_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5v4_5d_jerk_v073_signal},
    "f01mas_moving_average_systems_j5r21v4_21d_jerk_v074_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21v4_21d_jerk_v074_signal},
    "f01mas_moving_average_systems_j5r63v4_63d_jerk_v075_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63v4_63d_jerk_v075_signal},
    "f01mas_moving_average_systems_j21r5v4_5d_jerk_v076_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5v4_5d_jerk_v076_signal},
    "f01mas_moving_average_systems_j21r21v4_21d_jerk_v077_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21v4_21d_jerk_v077_signal},
    "f01mas_moving_average_systems_j21r63v4_63d_jerk_v078_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63v4_63d_jerk_v078_signal},
    "f01mas_moving_average_systems_j63r5v4_5d_jerk_v079_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r5v4_5d_jerk_v079_signal},
    "f01mas_moving_average_systems_j63r21v4_21d_jerk_v080_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r21v4_21d_jerk_v080_signal},
    "f01mas_moving_average_systems_j63r63v4_63d_jerk_v081_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r63v4_63d_jerk_v081_signal},
    "f01mas_moving_average_systems_j126r5v4_5d_jerk_v082_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r5v4_5d_jerk_v082_signal},
    "f01mas_moving_average_systems_j126r21v4_21d_jerk_v083_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r21v4_21d_jerk_v083_signal},
    "f01mas_moving_average_systems_j126r63v4_63d_jerk_v084_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r63v4_63d_jerk_v084_signal},
    "f01mas_moving_average_systems_j252r5v4_5d_jerk_v085_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r5v4_5d_jerk_v085_signal},
    "f01mas_moving_average_systems_j252r21v4_21d_jerk_v086_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r21v4_21d_jerk_v086_signal},
    "f01mas_moving_average_systems_j252r63v4_63d_jerk_v087_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r63v4_63d_jerk_v087_signal},
    "f01mas_moving_average_systems_j504r5v4_5d_jerk_v088_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r5v4_5d_jerk_v088_signal},
    "f01mas_moving_average_systems_j504r21v4_21d_jerk_v089_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r21v4_21d_jerk_v089_signal},
    "f01mas_moving_average_systems_j504r63v4_63d_jerk_v090_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r63v4_63d_jerk_v090_signal},
    "f01mas_moving_average_systems_j5r5v5_5d_jerk_v091_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5v5_5d_jerk_v091_signal},
    "f01mas_moving_average_systems_j5r21v5_21d_jerk_v092_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21v5_21d_jerk_v092_signal},
    "f01mas_moving_average_systems_j5r63v5_63d_jerk_v093_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63v5_63d_jerk_v093_signal},
    "f01mas_moving_average_systems_j21r5v5_5d_jerk_v094_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5v5_5d_jerk_v094_signal},
    "f01mas_moving_average_systems_j21r21v5_21d_jerk_v095_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21v5_21d_jerk_v095_signal},
    "f01mas_moving_average_systems_j21r63v5_63d_jerk_v096_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63v5_63d_jerk_v096_signal},
    "f01mas_moving_average_systems_j63r5v5_5d_jerk_v097_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r5v5_5d_jerk_v097_signal},
    "f01mas_moving_average_systems_j63r21v5_21d_jerk_v098_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r21v5_21d_jerk_v098_signal},
    "f01mas_moving_average_systems_j63r63v5_63d_jerk_v099_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r63v5_63d_jerk_v099_signal},
    "f01mas_moving_average_systems_j126r5v5_5d_jerk_v100_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r5v5_5d_jerk_v100_signal},
    "f01mas_moving_average_systems_j126r21v5_21d_jerk_v101_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r21v5_21d_jerk_v101_signal},
    "f01mas_moving_average_systems_j126r63v5_63d_jerk_v102_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r63v5_63d_jerk_v102_signal},
    "f01mas_moving_average_systems_j252r5v5_5d_jerk_v103_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r5v5_5d_jerk_v103_signal},
    "f01mas_moving_average_systems_j252r21v5_21d_jerk_v104_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r21v5_21d_jerk_v104_signal},
    "f01mas_moving_average_systems_j252r63v5_63d_jerk_v105_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r63v5_63d_jerk_v105_signal},
    "f01mas_moving_average_systems_j504r5v5_5d_jerk_v106_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r5v5_5d_jerk_v106_signal},
    "f01mas_moving_average_systems_j504r21v5_21d_jerk_v107_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r21v5_21d_jerk_v107_signal},
    "f01mas_moving_average_systems_j504r63v5_63d_jerk_v108_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r63v5_63d_jerk_v108_signal},
    "f01mas_moving_average_systems_j5r5v6_5d_jerk_v109_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5v6_5d_jerk_v109_signal},
    "f01mas_moving_average_systems_j5r21v6_21d_jerk_v110_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21v6_21d_jerk_v110_signal},
    "f01mas_moving_average_systems_j5r63v6_63d_jerk_v111_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63v6_63d_jerk_v111_signal},
    "f01mas_moving_average_systems_j21r5v6_5d_jerk_v112_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5v6_5d_jerk_v112_signal},
    "f01mas_moving_average_systems_j21r21v6_21d_jerk_v113_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21v6_21d_jerk_v113_signal},
    "f01mas_moving_average_systems_j21r63v6_63d_jerk_v114_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63v6_63d_jerk_v114_signal},
    "f01mas_moving_average_systems_j63r5v6_5d_jerk_v115_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r5v6_5d_jerk_v115_signal},
    "f01mas_moving_average_systems_j63r21v6_21d_jerk_v116_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r21v6_21d_jerk_v116_signal},
    "f01mas_moving_average_systems_j63r63v6_63d_jerk_v117_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r63v6_63d_jerk_v117_signal},
    "f01mas_moving_average_systems_j126r5v6_5d_jerk_v118_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r5v6_5d_jerk_v118_signal},
    "f01mas_moving_average_systems_j126r21v6_21d_jerk_v119_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r21v6_21d_jerk_v119_signal},
    "f01mas_moving_average_systems_j126r63v6_63d_jerk_v120_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r63v6_63d_jerk_v120_signal},
    "f01mas_moving_average_systems_j252r5v6_5d_jerk_v121_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r5v6_5d_jerk_v121_signal},
    "f01mas_moving_average_systems_j252r21v6_21d_jerk_v122_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r21v6_21d_jerk_v122_signal},
    "f01mas_moving_average_systems_j252r63v6_63d_jerk_v123_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r63v6_63d_jerk_v123_signal},
    "f01mas_moving_average_systems_j504r5v6_5d_jerk_v124_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r5v6_5d_jerk_v124_signal},
    "f01mas_moving_average_systems_j504r21v6_21d_jerk_v125_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r21v6_21d_jerk_v125_signal},
    "f01mas_moving_average_systems_j504r63v6_63d_jerk_v126_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r63v6_63d_jerk_v126_signal},
    "f01mas_moving_average_systems_j5r5v7_5d_jerk_v127_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5v7_5d_jerk_v127_signal},
    "f01mas_moving_average_systems_j5r21v7_21d_jerk_v128_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21v7_21d_jerk_v128_signal},
    "f01mas_moving_average_systems_j5r63v7_63d_jerk_v129_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63v7_63d_jerk_v129_signal},
    "f01mas_moving_average_systems_j21r5v7_5d_jerk_v130_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5v7_5d_jerk_v130_signal},
    "f01mas_moving_average_systems_j21r21v7_21d_jerk_v131_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21v7_21d_jerk_v131_signal},
    "f01mas_moving_average_systems_j21r63v7_63d_jerk_v132_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63v7_63d_jerk_v132_signal},
    "f01mas_moving_average_systems_j63r5v7_5d_jerk_v133_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r5v7_5d_jerk_v133_signal},
    "f01mas_moving_average_systems_j63r21v7_21d_jerk_v134_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r21v7_21d_jerk_v134_signal},
    "f01mas_moving_average_systems_j63r63v7_63d_jerk_v135_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j63r63v7_63d_jerk_v135_signal},
    "f01mas_moving_average_systems_j126r5v7_5d_jerk_v136_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r5v7_5d_jerk_v136_signal},
    "f01mas_moving_average_systems_j126r21v7_21d_jerk_v137_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r21v7_21d_jerk_v137_signal},
    "f01mas_moving_average_systems_j126r63v7_63d_jerk_v138_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j126r63v7_63d_jerk_v138_signal},
    "f01mas_moving_average_systems_j252r5v7_5d_jerk_v139_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r5v7_5d_jerk_v139_signal},
    "f01mas_moving_average_systems_j252r21v7_21d_jerk_v140_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r21v7_21d_jerk_v140_signal},
    "f01mas_moving_average_systems_j252r63v7_63d_jerk_v141_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j252r63v7_63d_jerk_v141_signal},
    "f01mas_moving_average_systems_j504r5v7_5d_jerk_v142_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r5v7_5d_jerk_v142_signal},
    "f01mas_moving_average_systems_j504r21v7_21d_jerk_v143_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r21v7_21d_jerk_v143_signal},
    "f01mas_moving_average_systems_j504r63v7_63d_jerk_v144_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j504r63v7_63d_jerk_v144_signal},
    "f01mas_moving_average_systems_j5r5v8_5d_jerk_v145_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r5v8_5d_jerk_v145_signal},
    "f01mas_moving_average_systems_j5r21v8_21d_jerk_v146_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r21v8_21d_jerk_v146_signal},
    "f01mas_moving_average_systems_j5r63v8_63d_jerk_v147_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j5r63v8_63d_jerk_v147_signal},
    "f01mas_moving_average_systems_j21r5v8_5d_jerk_v148_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r5v8_5d_jerk_v148_signal},
    "f01mas_moving_average_systems_j21r21v8_21d_jerk_v149_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r21v8_21d_jerk_v149_signal},
    "f01mas_moving_average_systems_j21r63v8_63d_jerk_v150_signal": {"inputs": ["closeadj"], "func": f01mas_moving_average_systems_j21r63v8_63d_jerk_v150_signal}
}
F01_MOVING_AVERAGE_SYSTEMS_REGISTRY_JERK = REGISTRY

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
        assert "_ma_sma" in src or "_ma_ema" in src or "_ma_ratio" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F01_MOVING_AVERAGE_SYSTEMS_REGISTRY_JERK")
