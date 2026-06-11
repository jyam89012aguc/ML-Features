import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _hlrd_daily_range(high, low, close):
    return (high - low) / close.abs().replace(0, np.nan)
def _hlrd_range_expansion(high, low, close, w):
    r = _hlrd_daily_range(high, low, close)
    return r / r.rolling(w, min_periods=max(1, w//2)).mean().replace(0, np.nan)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v001_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v002_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v003_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v004_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v005_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v006_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v007_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v008_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v009_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v010_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v011_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v012_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v013_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v014_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v015_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v016_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v017_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v018_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v019_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v020_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v021_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v022_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v023_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v024_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v025_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v026_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v027_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v028_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v029_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v030_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v031_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v032_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v033_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v034_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v035_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v036_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v037_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v038_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v039_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v040_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v041_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v042_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v043_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v044_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v045_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v046_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v047_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v048_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v049_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v050_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v051_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v052_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v053_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v054_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v055_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v056_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v057_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v058_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v059_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v060_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v061_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v062_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v063_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v064_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v065_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v066_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v067_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v068_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v069_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v070_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v071_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v072_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v073_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v074_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v075_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v076_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v077_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v078_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v079_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v080_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v081_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v082_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v083_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v084_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v085_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v086_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v087_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v088_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v089_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v090_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v091_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v092_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v093_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v094_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v095_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v096_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v097_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v098_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v099_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v100_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v101_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v102_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v103_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v104_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v105_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v106_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v107_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v108_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v109_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v110_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v111_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v112_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v113_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v114_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v115_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v116_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v117_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v118_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v119_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v120_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v121_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v122_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v123_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v124_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v125_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v126_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v127_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v128_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v129_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v130_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v131_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v132_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v133_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v134_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v135_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v136_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v137_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v138_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v139_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v140_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v141_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v142_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v143_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=21d
def f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v144_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v145_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v146_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v147_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v148_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v149_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# jerk of _hlrd_daily_range roc=5d
def f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v150_signal(close, high, low):
    b=_hlrd_daily_range(high, low, close)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)


REGISTRY = {
    "f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v001_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v001_signal},
    "f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v002_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v002_signal},
    "f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v003_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v003_signal},
    "f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v004_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v004_signal},
    "f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v005_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v005_signal},
    "f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v006_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5_5d_jerk_v006_signal},
    "f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v007_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v007_signal},
    "f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v008_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v008_signal},
    "f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v009_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v009_signal},
    "f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v010_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v010_signal},
    "f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v011_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v011_signal},
    "f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v012_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21_21d_jerk_v012_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v013_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v013_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v014_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v014_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v015_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v015_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v016_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v016_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v017_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v017_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v018_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v1_5d_jerk_v018_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v019_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v019_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v020_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v020_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v021_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v021_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v022_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v022_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v023_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v023_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v024_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v1_21d_jerk_v024_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v025_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v025_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v026_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v026_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v027_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v027_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v028_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v028_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v029_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v029_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v030_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v2_5d_jerk_v030_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v031_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v031_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v032_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v032_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v033_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v033_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v034_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v034_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v035_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v035_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v036_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v2_21d_jerk_v036_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v037_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v037_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v038_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v038_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v039_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v039_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v040_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v040_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v041_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v041_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v042_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v3_5d_jerk_v042_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v043_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v043_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v044_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v044_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v045_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v045_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v046_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v046_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v047_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v047_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v048_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v3_21d_jerk_v048_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v049_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v049_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v050_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v050_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v051_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v051_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v052_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v052_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v053_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v053_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v054_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v4_5d_jerk_v054_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v055_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v055_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v056_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v056_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v057_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v057_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v058_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v058_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v059_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v059_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v060_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v4_21d_jerk_v060_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v061_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v061_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v062_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v062_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v063_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v063_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v064_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v064_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v065_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v065_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v066_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v5_5d_jerk_v066_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v067_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v067_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v068_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v068_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v069_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v069_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v070_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v070_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v071_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v071_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v072_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v5_21d_jerk_v072_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v073_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v073_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v074_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v074_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v075_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v075_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v076_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v076_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v077_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v077_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v078_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v6_5d_jerk_v078_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v079_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v079_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v080_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v080_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v081_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v081_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v082_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v082_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v083_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v083_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v084_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v6_21d_jerk_v084_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v085_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v085_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v086_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v086_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v087_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v087_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v088_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v088_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v089_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v089_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v090_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v7_5d_jerk_v090_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v091_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v091_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v092_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v092_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v093_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v093_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v094_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v094_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v095_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v095_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v096_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v7_21d_jerk_v096_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v097_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v097_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v098_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v098_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v099_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v099_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v100_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v100_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v101_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v101_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v102_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v8_5d_jerk_v102_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v103_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v103_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v104_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v104_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v105_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v105_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v106_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v106_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v107_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v107_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v108_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v8_21d_jerk_v108_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v109_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v109_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v110_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v110_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v111_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v111_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v112_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v112_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v113_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v113_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v114_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v9_5d_jerk_v114_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v115_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v115_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v116_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v116_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v117_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v117_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v118_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v118_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v119_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v119_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v120_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v9_21d_jerk_v120_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v121_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v121_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v122_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v122_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v123_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v123_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v124_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v124_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v125_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v125_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v126_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v10_5d_jerk_v126_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v127_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v127_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v128_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v128_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v129_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v129_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v130_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v130_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v131_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v131_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v132_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v10_21d_jerk_v132_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v133_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v133_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v134_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v134_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v135_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v135_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v136_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v136_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v137_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v137_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v138_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v11_5d_jerk_v138_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v139_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v139_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v140_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v140_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v141_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v141_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v142_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v142_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v143_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v143_signal},
    "f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v144_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r21v11_21d_jerk_v144_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v145_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v145_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v146_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v146_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v147_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v147_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v148_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v148_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v149_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v149_signal},
    "f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v150_signal": {"inputs": ["close", "high", "low"], "func": f08hlrd_high_low_range_dynamics_j_r5v12_5d_jerk_v150_signal}
}
F08_HIGH_LOW_RANGE_DYNAMICS_REGISTRY_JERK = REGISTRY

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
        assert "_hlrd_daily_range" in src or "_hlrd_range_expansion" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F08_HIGH_LOW_RANGE_DYNAMICS_REGISTRY_JERK")
