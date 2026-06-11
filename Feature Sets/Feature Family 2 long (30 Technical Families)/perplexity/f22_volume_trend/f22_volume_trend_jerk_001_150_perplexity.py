import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _vt_vol_ema(volume, w):
    return volume.ewm(span=w, min_periods=max(1, w//2), adjust=False).mean()
def _vt_vol_trend_ratio(volume, fast, slow):
    return _vt_vol_ema(volume, fast) / _vt_vol_ema(volume, slow).replace(0, np.nan) - 1.0
def _vt_vol_slope(volume, w):
    sma = volume.rolling(w, min_periods=max(1, w//2)).mean()
    return sma.diff(w) / sma.shift(w).abs().replace(0, np.nan)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5_5d_jerk_v001_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21_21d_jerk_v002_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63_63d_jerk_v003_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5_5d_jerk_v004_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21_21d_jerk_v005_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63_63d_jerk_v006_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5_5d_jerk_v007_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21_21d_jerk_v008_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63_63d_jerk_v009_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5_5d_jerk_v010_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21_21d_jerk_v011_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63_63d_jerk_v012_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v1_5d_jerk_v013_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v1_21d_jerk_v014_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v1_63d_jerk_v015_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v1_5d_jerk_v016_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v1_21d_jerk_v017_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v1_63d_jerk_v018_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v1_5d_jerk_v019_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v1_21d_jerk_v020_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v1_63d_jerk_v021_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v1_5d_jerk_v022_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v1_21d_jerk_v023_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v1_63d_jerk_v024_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v2_5d_jerk_v025_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v2_21d_jerk_v026_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v2_63d_jerk_v027_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v2_5d_jerk_v028_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v2_21d_jerk_v029_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v2_63d_jerk_v030_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v2_5d_jerk_v031_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v2_21d_jerk_v032_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v2_63d_jerk_v033_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v2_5d_jerk_v034_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v2_21d_jerk_v035_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v2_63d_jerk_v036_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v3_5d_jerk_v037_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v3_21d_jerk_v038_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v3_63d_jerk_v039_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v3_5d_jerk_v040_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v3_21d_jerk_v041_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v3_63d_jerk_v042_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v3_5d_jerk_v043_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v3_21d_jerk_v044_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v3_63d_jerk_v045_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v3_5d_jerk_v046_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v3_21d_jerk_v047_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v3_63d_jerk_v048_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v4_5d_jerk_v049_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v4_21d_jerk_v050_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v4_63d_jerk_v051_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v4_5d_jerk_v052_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v4_21d_jerk_v053_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v4_63d_jerk_v054_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v4_5d_jerk_v055_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v4_21d_jerk_v056_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v4_63d_jerk_v057_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v4_5d_jerk_v058_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v4_21d_jerk_v059_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v4_63d_jerk_v060_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v5_5d_jerk_v061_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v5_21d_jerk_v062_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v5_63d_jerk_v063_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v5_5d_jerk_v064_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v5_21d_jerk_v065_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v5_63d_jerk_v066_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v5_5d_jerk_v067_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v5_21d_jerk_v068_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v5_63d_jerk_v069_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v5_5d_jerk_v070_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v5_21d_jerk_v071_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v5_63d_jerk_v072_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v6_5d_jerk_v073_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v6_21d_jerk_v074_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v6_63d_jerk_v075_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v6_5d_jerk_v076_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v6_21d_jerk_v077_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v6_63d_jerk_v078_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v6_5d_jerk_v079_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v6_21d_jerk_v080_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v6_63d_jerk_v081_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v6_5d_jerk_v082_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v6_21d_jerk_v083_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v6_63d_jerk_v084_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v7_5d_jerk_v085_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v7_21d_jerk_v086_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v7_63d_jerk_v087_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v7_5d_jerk_v088_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v7_21d_jerk_v089_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v7_63d_jerk_v090_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v7_5d_jerk_v091_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v7_21d_jerk_v092_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v7_63d_jerk_v093_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v7_5d_jerk_v094_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v7_21d_jerk_v095_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v7_63d_jerk_v096_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v8_5d_jerk_v097_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v8_21d_jerk_v098_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v8_63d_jerk_v099_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v8_5d_jerk_v100_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v8_21d_jerk_v101_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v8_63d_jerk_v102_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v8_5d_jerk_v103_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v8_21d_jerk_v104_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v8_63d_jerk_v105_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v8_5d_jerk_v106_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v8_21d_jerk_v107_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v8_63d_jerk_v108_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v9_5d_jerk_v109_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v9_21d_jerk_v110_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v9_63d_jerk_v111_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v9_5d_jerk_v112_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v9_21d_jerk_v113_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v9_63d_jerk_v114_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v9_5d_jerk_v115_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v9_21d_jerk_v116_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v9_63d_jerk_v117_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v9_5d_jerk_v118_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v9_21d_jerk_v119_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v9_63d_jerk_v120_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v10_5d_jerk_v121_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v10_21d_jerk_v122_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v10_63d_jerk_v123_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v10_5d_jerk_v124_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v10_21d_jerk_v125_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v10_63d_jerk_v126_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v10_5d_jerk_v127_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v10_21d_jerk_v128_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v10_63d_jerk_v129_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v10_5d_jerk_v130_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v10_21d_jerk_v131_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v10_63d_jerk_v132_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.diff(63)/b.shift(63).abs().replace(0,np.nan)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v11_5d_jerk_v133_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v11_21d_jerk_v134_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v11_63d_jerk_v135_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v11_5d_jerk_v136_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v11_21d_jerk_v137_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v11_63d_jerk_v138_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=5d
def f22vt_volume_trend_j63r5v11_5d_jerk_v139_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=21d
def f22vt_volume_trend_j63r21v11_21d_jerk_v140_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=63 roc=63d
def f22vt_volume_trend_j63r63v11_63d_jerk_v141_signal(volume):
    b=_vt_vol_ema(volume, 63)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=5d
def f22vt_volume_trend_j126r5v11_5d_jerk_v142_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=21d
def f22vt_volume_trend_j126r21v11_21d_jerk_v143_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=126 roc=63d
def f22vt_volume_trend_j126r63v11_63d_jerk_v144_signal(volume):
    b=_vt_vol_ema(volume, 126)
    s=b.pct_change(63)
    result=s.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=5d
def f22vt_volume_trend_j5r5v12_5d_jerk_v145_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=21d
def f22vt_volume_trend_j5r21v12_21d_jerk_v146_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=5 roc=63d
def f22vt_volume_trend_j5r63v12_63d_jerk_v147_signal(volume):
    b=_vt_vol_ema(volume, 5)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=5d
def f22vt_volume_trend_j21r5v12_5d_jerk_v148_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=21d
def f22vt_volume_trend_j21r21v12_21d_jerk_v149_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _vt_vol_ema w=21 roc=63d
def f22vt_volume_trend_j21r63v12_63d_jerk_v150_signal(volume):
    b=_vt_vol_ema(volume, 21)
    s=b.pct_change(63)
    result=s.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)


REGISTRY = {
    "f22vt_volume_trend_j5r5_5d_jerk_v001_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5_5d_jerk_v001_signal},
    "f22vt_volume_trend_j5r21_21d_jerk_v002_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21_21d_jerk_v002_signal},
    "f22vt_volume_trend_j5r63_63d_jerk_v003_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63_63d_jerk_v003_signal},
    "f22vt_volume_trend_j21r5_5d_jerk_v004_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5_5d_jerk_v004_signal},
    "f22vt_volume_trend_j21r21_21d_jerk_v005_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21_21d_jerk_v005_signal},
    "f22vt_volume_trend_j21r63_63d_jerk_v006_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63_63d_jerk_v006_signal},
    "f22vt_volume_trend_j63r5_5d_jerk_v007_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5_5d_jerk_v007_signal},
    "f22vt_volume_trend_j63r21_21d_jerk_v008_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21_21d_jerk_v008_signal},
    "f22vt_volume_trend_j63r63_63d_jerk_v009_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63_63d_jerk_v009_signal},
    "f22vt_volume_trend_j126r5_5d_jerk_v010_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5_5d_jerk_v010_signal},
    "f22vt_volume_trend_j126r21_21d_jerk_v011_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21_21d_jerk_v011_signal},
    "f22vt_volume_trend_j126r63_63d_jerk_v012_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63_63d_jerk_v012_signal},
    "f22vt_volume_trend_j5r5v1_5d_jerk_v013_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v1_5d_jerk_v013_signal},
    "f22vt_volume_trend_j5r21v1_21d_jerk_v014_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v1_21d_jerk_v014_signal},
    "f22vt_volume_trend_j5r63v1_63d_jerk_v015_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v1_63d_jerk_v015_signal},
    "f22vt_volume_trend_j21r5v1_5d_jerk_v016_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v1_5d_jerk_v016_signal},
    "f22vt_volume_trend_j21r21v1_21d_jerk_v017_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v1_21d_jerk_v017_signal},
    "f22vt_volume_trend_j21r63v1_63d_jerk_v018_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v1_63d_jerk_v018_signal},
    "f22vt_volume_trend_j63r5v1_5d_jerk_v019_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v1_5d_jerk_v019_signal},
    "f22vt_volume_trend_j63r21v1_21d_jerk_v020_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v1_21d_jerk_v020_signal},
    "f22vt_volume_trend_j63r63v1_63d_jerk_v021_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v1_63d_jerk_v021_signal},
    "f22vt_volume_trend_j126r5v1_5d_jerk_v022_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v1_5d_jerk_v022_signal},
    "f22vt_volume_trend_j126r21v1_21d_jerk_v023_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v1_21d_jerk_v023_signal},
    "f22vt_volume_trend_j126r63v1_63d_jerk_v024_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v1_63d_jerk_v024_signal},
    "f22vt_volume_trend_j5r5v2_5d_jerk_v025_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v2_5d_jerk_v025_signal},
    "f22vt_volume_trend_j5r21v2_21d_jerk_v026_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v2_21d_jerk_v026_signal},
    "f22vt_volume_trend_j5r63v2_63d_jerk_v027_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v2_63d_jerk_v027_signal},
    "f22vt_volume_trend_j21r5v2_5d_jerk_v028_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v2_5d_jerk_v028_signal},
    "f22vt_volume_trend_j21r21v2_21d_jerk_v029_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v2_21d_jerk_v029_signal},
    "f22vt_volume_trend_j21r63v2_63d_jerk_v030_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v2_63d_jerk_v030_signal},
    "f22vt_volume_trend_j63r5v2_5d_jerk_v031_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v2_5d_jerk_v031_signal},
    "f22vt_volume_trend_j63r21v2_21d_jerk_v032_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v2_21d_jerk_v032_signal},
    "f22vt_volume_trend_j63r63v2_63d_jerk_v033_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v2_63d_jerk_v033_signal},
    "f22vt_volume_trend_j126r5v2_5d_jerk_v034_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v2_5d_jerk_v034_signal},
    "f22vt_volume_trend_j126r21v2_21d_jerk_v035_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v2_21d_jerk_v035_signal},
    "f22vt_volume_trend_j126r63v2_63d_jerk_v036_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v2_63d_jerk_v036_signal},
    "f22vt_volume_trend_j5r5v3_5d_jerk_v037_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v3_5d_jerk_v037_signal},
    "f22vt_volume_trend_j5r21v3_21d_jerk_v038_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v3_21d_jerk_v038_signal},
    "f22vt_volume_trend_j5r63v3_63d_jerk_v039_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v3_63d_jerk_v039_signal},
    "f22vt_volume_trend_j21r5v3_5d_jerk_v040_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v3_5d_jerk_v040_signal},
    "f22vt_volume_trend_j21r21v3_21d_jerk_v041_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v3_21d_jerk_v041_signal},
    "f22vt_volume_trend_j21r63v3_63d_jerk_v042_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v3_63d_jerk_v042_signal},
    "f22vt_volume_trend_j63r5v3_5d_jerk_v043_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v3_5d_jerk_v043_signal},
    "f22vt_volume_trend_j63r21v3_21d_jerk_v044_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v3_21d_jerk_v044_signal},
    "f22vt_volume_trend_j63r63v3_63d_jerk_v045_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v3_63d_jerk_v045_signal},
    "f22vt_volume_trend_j126r5v3_5d_jerk_v046_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v3_5d_jerk_v046_signal},
    "f22vt_volume_trend_j126r21v3_21d_jerk_v047_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v3_21d_jerk_v047_signal},
    "f22vt_volume_trend_j126r63v3_63d_jerk_v048_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v3_63d_jerk_v048_signal},
    "f22vt_volume_trend_j5r5v4_5d_jerk_v049_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v4_5d_jerk_v049_signal},
    "f22vt_volume_trend_j5r21v4_21d_jerk_v050_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v4_21d_jerk_v050_signal},
    "f22vt_volume_trend_j5r63v4_63d_jerk_v051_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v4_63d_jerk_v051_signal},
    "f22vt_volume_trend_j21r5v4_5d_jerk_v052_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v4_5d_jerk_v052_signal},
    "f22vt_volume_trend_j21r21v4_21d_jerk_v053_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v4_21d_jerk_v053_signal},
    "f22vt_volume_trend_j21r63v4_63d_jerk_v054_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v4_63d_jerk_v054_signal},
    "f22vt_volume_trend_j63r5v4_5d_jerk_v055_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v4_5d_jerk_v055_signal},
    "f22vt_volume_trend_j63r21v4_21d_jerk_v056_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v4_21d_jerk_v056_signal},
    "f22vt_volume_trend_j63r63v4_63d_jerk_v057_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v4_63d_jerk_v057_signal},
    "f22vt_volume_trend_j126r5v4_5d_jerk_v058_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v4_5d_jerk_v058_signal},
    "f22vt_volume_trend_j126r21v4_21d_jerk_v059_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v4_21d_jerk_v059_signal},
    "f22vt_volume_trend_j126r63v4_63d_jerk_v060_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v4_63d_jerk_v060_signal},
    "f22vt_volume_trend_j5r5v5_5d_jerk_v061_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v5_5d_jerk_v061_signal},
    "f22vt_volume_trend_j5r21v5_21d_jerk_v062_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v5_21d_jerk_v062_signal},
    "f22vt_volume_trend_j5r63v5_63d_jerk_v063_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v5_63d_jerk_v063_signal},
    "f22vt_volume_trend_j21r5v5_5d_jerk_v064_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v5_5d_jerk_v064_signal},
    "f22vt_volume_trend_j21r21v5_21d_jerk_v065_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v5_21d_jerk_v065_signal},
    "f22vt_volume_trend_j21r63v5_63d_jerk_v066_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v5_63d_jerk_v066_signal},
    "f22vt_volume_trend_j63r5v5_5d_jerk_v067_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v5_5d_jerk_v067_signal},
    "f22vt_volume_trend_j63r21v5_21d_jerk_v068_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v5_21d_jerk_v068_signal},
    "f22vt_volume_trend_j63r63v5_63d_jerk_v069_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v5_63d_jerk_v069_signal},
    "f22vt_volume_trend_j126r5v5_5d_jerk_v070_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v5_5d_jerk_v070_signal},
    "f22vt_volume_trend_j126r21v5_21d_jerk_v071_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v5_21d_jerk_v071_signal},
    "f22vt_volume_trend_j126r63v5_63d_jerk_v072_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v5_63d_jerk_v072_signal},
    "f22vt_volume_trend_j5r5v6_5d_jerk_v073_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v6_5d_jerk_v073_signal},
    "f22vt_volume_trend_j5r21v6_21d_jerk_v074_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v6_21d_jerk_v074_signal},
    "f22vt_volume_trend_j5r63v6_63d_jerk_v075_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v6_63d_jerk_v075_signal},
    "f22vt_volume_trend_j21r5v6_5d_jerk_v076_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v6_5d_jerk_v076_signal},
    "f22vt_volume_trend_j21r21v6_21d_jerk_v077_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v6_21d_jerk_v077_signal},
    "f22vt_volume_trend_j21r63v6_63d_jerk_v078_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v6_63d_jerk_v078_signal},
    "f22vt_volume_trend_j63r5v6_5d_jerk_v079_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v6_5d_jerk_v079_signal},
    "f22vt_volume_trend_j63r21v6_21d_jerk_v080_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v6_21d_jerk_v080_signal},
    "f22vt_volume_trend_j63r63v6_63d_jerk_v081_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v6_63d_jerk_v081_signal},
    "f22vt_volume_trend_j126r5v6_5d_jerk_v082_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v6_5d_jerk_v082_signal},
    "f22vt_volume_trend_j126r21v6_21d_jerk_v083_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v6_21d_jerk_v083_signal},
    "f22vt_volume_trend_j126r63v6_63d_jerk_v084_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v6_63d_jerk_v084_signal},
    "f22vt_volume_trend_j5r5v7_5d_jerk_v085_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v7_5d_jerk_v085_signal},
    "f22vt_volume_trend_j5r21v7_21d_jerk_v086_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v7_21d_jerk_v086_signal},
    "f22vt_volume_trend_j5r63v7_63d_jerk_v087_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v7_63d_jerk_v087_signal},
    "f22vt_volume_trend_j21r5v7_5d_jerk_v088_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v7_5d_jerk_v088_signal},
    "f22vt_volume_trend_j21r21v7_21d_jerk_v089_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v7_21d_jerk_v089_signal},
    "f22vt_volume_trend_j21r63v7_63d_jerk_v090_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v7_63d_jerk_v090_signal},
    "f22vt_volume_trend_j63r5v7_5d_jerk_v091_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v7_5d_jerk_v091_signal},
    "f22vt_volume_trend_j63r21v7_21d_jerk_v092_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v7_21d_jerk_v092_signal},
    "f22vt_volume_trend_j63r63v7_63d_jerk_v093_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v7_63d_jerk_v093_signal},
    "f22vt_volume_trend_j126r5v7_5d_jerk_v094_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v7_5d_jerk_v094_signal},
    "f22vt_volume_trend_j126r21v7_21d_jerk_v095_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v7_21d_jerk_v095_signal},
    "f22vt_volume_trend_j126r63v7_63d_jerk_v096_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v7_63d_jerk_v096_signal},
    "f22vt_volume_trend_j5r5v8_5d_jerk_v097_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v8_5d_jerk_v097_signal},
    "f22vt_volume_trend_j5r21v8_21d_jerk_v098_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v8_21d_jerk_v098_signal},
    "f22vt_volume_trend_j5r63v8_63d_jerk_v099_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v8_63d_jerk_v099_signal},
    "f22vt_volume_trend_j21r5v8_5d_jerk_v100_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v8_5d_jerk_v100_signal},
    "f22vt_volume_trend_j21r21v8_21d_jerk_v101_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v8_21d_jerk_v101_signal},
    "f22vt_volume_trend_j21r63v8_63d_jerk_v102_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v8_63d_jerk_v102_signal},
    "f22vt_volume_trend_j63r5v8_5d_jerk_v103_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v8_5d_jerk_v103_signal},
    "f22vt_volume_trend_j63r21v8_21d_jerk_v104_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v8_21d_jerk_v104_signal},
    "f22vt_volume_trend_j63r63v8_63d_jerk_v105_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v8_63d_jerk_v105_signal},
    "f22vt_volume_trend_j126r5v8_5d_jerk_v106_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v8_5d_jerk_v106_signal},
    "f22vt_volume_trend_j126r21v8_21d_jerk_v107_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v8_21d_jerk_v107_signal},
    "f22vt_volume_trend_j126r63v8_63d_jerk_v108_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v8_63d_jerk_v108_signal},
    "f22vt_volume_trend_j5r5v9_5d_jerk_v109_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v9_5d_jerk_v109_signal},
    "f22vt_volume_trend_j5r21v9_21d_jerk_v110_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v9_21d_jerk_v110_signal},
    "f22vt_volume_trend_j5r63v9_63d_jerk_v111_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v9_63d_jerk_v111_signal},
    "f22vt_volume_trend_j21r5v9_5d_jerk_v112_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v9_5d_jerk_v112_signal},
    "f22vt_volume_trend_j21r21v9_21d_jerk_v113_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v9_21d_jerk_v113_signal},
    "f22vt_volume_trend_j21r63v9_63d_jerk_v114_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v9_63d_jerk_v114_signal},
    "f22vt_volume_trend_j63r5v9_5d_jerk_v115_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v9_5d_jerk_v115_signal},
    "f22vt_volume_trend_j63r21v9_21d_jerk_v116_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v9_21d_jerk_v116_signal},
    "f22vt_volume_trend_j63r63v9_63d_jerk_v117_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v9_63d_jerk_v117_signal},
    "f22vt_volume_trend_j126r5v9_5d_jerk_v118_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v9_5d_jerk_v118_signal},
    "f22vt_volume_trend_j126r21v9_21d_jerk_v119_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v9_21d_jerk_v119_signal},
    "f22vt_volume_trend_j126r63v9_63d_jerk_v120_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v9_63d_jerk_v120_signal},
    "f22vt_volume_trend_j5r5v10_5d_jerk_v121_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v10_5d_jerk_v121_signal},
    "f22vt_volume_trend_j5r21v10_21d_jerk_v122_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v10_21d_jerk_v122_signal},
    "f22vt_volume_trend_j5r63v10_63d_jerk_v123_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v10_63d_jerk_v123_signal},
    "f22vt_volume_trend_j21r5v10_5d_jerk_v124_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v10_5d_jerk_v124_signal},
    "f22vt_volume_trend_j21r21v10_21d_jerk_v125_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v10_21d_jerk_v125_signal},
    "f22vt_volume_trend_j21r63v10_63d_jerk_v126_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v10_63d_jerk_v126_signal},
    "f22vt_volume_trend_j63r5v10_5d_jerk_v127_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v10_5d_jerk_v127_signal},
    "f22vt_volume_trend_j63r21v10_21d_jerk_v128_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v10_21d_jerk_v128_signal},
    "f22vt_volume_trend_j63r63v10_63d_jerk_v129_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v10_63d_jerk_v129_signal},
    "f22vt_volume_trend_j126r5v10_5d_jerk_v130_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v10_5d_jerk_v130_signal},
    "f22vt_volume_trend_j126r21v10_21d_jerk_v131_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v10_21d_jerk_v131_signal},
    "f22vt_volume_trend_j126r63v10_63d_jerk_v132_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v10_63d_jerk_v132_signal},
    "f22vt_volume_trend_j5r5v11_5d_jerk_v133_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v11_5d_jerk_v133_signal},
    "f22vt_volume_trend_j5r21v11_21d_jerk_v134_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v11_21d_jerk_v134_signal},
    "f22vt_volume_trend_j5r63v11_63d_jerk_v135_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v11_63d_jerk_v135_signal},
    "f22vt_volume_trend_j21r5v11_5d_jerk_v136_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v11_5d_jerk_v136_signal},
    "f22vt_volume_trend_j21r21v11_21d_jerk_v137_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v11_21d_jerk_v137_signal},
    "f22vt_volume_trend_j21r63v11_63d_jerk_v138_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v11_63d_jerk_v138_signal},
    "f22vt_volume_trend_j63r5v11_5d_jerk_v139_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r5v11_5d_jerk_v139_signal},
    "f22vt_volume_trend_j63r21v11_21d_jerk_v140_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r21v11_21d_jerk_v140_signal},
    "f22vt_volume_trend_j63r63v11_63d_jerk_v141_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j63r63v11_63d_jerk_v141_signal},
    "f22vt_volume_trend_j126r5v11_5d_jerk_v142_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r5v11_5d_jerk_v142_signal},
    "f22vt_volume_trend_j126r21v11_21d_jerk_v143_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r21v11_21d_jerk_v143_signal},
    "f22vt_volume_trend_j126r63v11_63d_jerk_v144_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j126r63v11_63d_jerk_v144_signal},
    "f22vt_volume_trend_j5r5v12_5d_jerk_v145_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r5v12_5d_jerk_v145_signal},
    "f22vt_volume_trend_j5r21v12_21d_jerk_v146_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r21v12_21d_jerk_v146_signal},
    "f22vt_volume_trend_j5r63v12_63d_jerk_v147_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j5r63v12_63d_jerk_v147_signal},
    "f22vt_volume_trend_j21r5v12_5d_jerk_v148_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r5v12_5d_jerk_v148_signal},
    "f22vt_volume_trend_j21r21v12_21d_jerk_v149_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r21v12_21d_jerk_v149_signal},
    "f22vt_volume_trend_j21r63v12_63d_jerk_v150_signal": {"inputs": ["volume"], "func": f22vt_volume_trend_j21r63v12_63d_jerk_v150_signal}
}
F22_VOLUME_TREND_REGISTRY_JERK = REGISTRY

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
        assert "_vt_vol_ema" in src or "_vt_vol_trend_ratio" in src or "_vt_vol_slope" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F22_VOLUME_TREND_REGISTRY_JERK")
