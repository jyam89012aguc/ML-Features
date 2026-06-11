import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _pvd_price_trend(closeadj, w):
    return closeadj.pct_change(w)
def _pvd_vol_trend(volume, w):
    sma = volume.rolling(w, min_periods=max(1, w//2)).mean()
    return sma.pct_change(w)
def _pvd_divergence(closeadj, volume, w):
    return _pvd_price_trend(closeadj, w) - _pvd_vol_trend(volume, w)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5_5d_slope_v001_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21_21d_slope_v002_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5_5d_slope_v003_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21_21d_slope_v004_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5_5d_slope_v005_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21_21d_slope_v006_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v1_5d_slope_v007_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v1_21d_slope_v008_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v1_5d_slope_v009_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v1_21d_slope_v010_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v1_5d_slope_v011_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v1_21d_slope_v012_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v2_5d_slope_v013_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v2_21d_slope_v014_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v2_5d_slope_v015_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v2_21d_slope_v016_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v2_5d_slope_v017_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v2_21d_slope_v018_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v3_5d_slope_v019_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v3_21d_slope_v020_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v3_5d_slope_v021_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v3_21d_slope_v022_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v3_5d_slope_v023_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v3_21d_slope_v024_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v4_5d_slope_v025_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v4_21d_slope_v026_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v4_5d_slope_v027_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v4_21d_slope_v028_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v4_5d_slope_v029_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v4_21d_slope_v030_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v5_5d_slope_v031_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v5_21d_slope_v032_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v5_5d_slope_v033_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v5_21d_slope_v034_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v5_5d_slope_v035_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v5_21d_slope_v036_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v6_5d_slope_v037_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v6_21d_slope_v038_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v6_5d_slope_v039_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v6_21d_slope_v040_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v6_5d_slope_v041_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v6_21d_slope_v042_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v7_5d_slope_v043_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v7_21d_slope_v044_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v7_5d_slope_v045_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v7_21d_slope_v046_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v7_5d_slope_v047_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v7_21d_slope_v048_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v8_5d_slope_v049_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v8_21d_slope_v050_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v8_5d_slope_v051_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v8_21d_slope_v052_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v8_5d_slope_v053_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v8_21d_slope_v054_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v9_5d_slope_v055_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v9_21d_slope_v056_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v9_5d_slope_v057_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v9_21d_slope_v058_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v9_5d_slope_v059_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v9_21d_slope_v060_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v10_5d_slope_v061_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v10_21d_slope_v062_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v10_5d_slope_v063_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v10_21d_slope_v064_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v10_5d_slope_v065_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v10_21d_slope_v066_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v11_5d_slope_v067_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v11_21d_slope_v068_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v11_5d_slope_v069_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v11_21d_slope_v070_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v11_5d_slope_v071_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v11_21d_slope_v072_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v12_5d_slope_v073_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v12_21d_slope_v074_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v12_5d_slope_v075_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v12_21d_slope_v076_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v12_5d_slope_v077_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v12_21d_slope_v078_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v13_5d_slope_v079_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v13_21d_slope_v080_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v13_5d_slope_v081_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v13_21d_slope_v082_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v13_5d_slope_v083_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v13_21d_slope_v084_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v14_5d_slope_v085_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v14_21d_slope_v086_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v14_5d_slope_v087_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v14_21d_slope_v088_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v14_5d_slope_v089_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v14_21d_slope_v090_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v15_5d_slope_v091_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v15_21d_slope_v092_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v15_5d_slope_v093_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v15_21d_slope_v094_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v15_5d_slope_v095_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v15_21d_slope_v096_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v16_5d_slope_v097_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v16_21d_slope_v098_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v16_5d_slope_v099_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v16_21d_slope_v100_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v16_5d_slope_v101_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v16_21d_slope_v102_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v17_5d_slope_v103_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v17_21d_slope_v104_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v17_5d_slope_v105_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v17_21d_slope_v106_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v17_5d_slope_v107_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v17_21d_slope_v108_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v18_5d_slope_v109_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v18_21d_slope_v110_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v18_5d_slope_v111_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v18_21d_slope_v112_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v18_5d_slope_v113_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v18_21d_slope_v114_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v19_5d_slope_v115_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v19_21d_slope_v116_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v19_5d_slope_v117_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v19_21d_slope_v118_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v19_5d_slope_v119_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v19_21d_slope_v120_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v20_5d_slope_v121_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v20_21d_slope_v122_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v20_5d_slope_v123_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v20_21d_slope_v124_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v20_5d_slope_v125_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v20_21d_slope_v126_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v21_5d_slope_v127_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v21_21d_slope_v128_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v21_5d_slope_v129_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v21_21d_slope_v130_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v21_5d_slope_v131_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v21_21d_slope_v132_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v22_5d_slope_v133_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v22_21d_slope_v134_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v22_5d_slope_v135_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v22_21d_slope_v136_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v22_5d_slope_v137_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v22_21d_slope_v138_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v23_5d_slope_v139_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v23_21d_slope_v140_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v23_5d_slope_v141_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v23_21d_slope_v142_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v23_5d_slope_v143_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v23_21d_slope_v144_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=5d
def f28pvd_price_volume_divergence_s5r5v24_5d_slope_v145_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=5 roc=21d
def f28pvd_price_volume_divergence_s5r21v24_21d_slope_v146_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=5d
def f28pvd_price_volume_divergence_s21r5v24_5d_slope_v147_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=21 roc=21d
def f28pvd_price_volume_divergence_s21r21v24_21d_slope_v148_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 21)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=5d
def f28pvd_price_volume_divergence_s63r5v24_5d_slope_v149_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _pvd_price_trend w=63 roc=21d
def f28pvd_price_volume_divergence_s63r21v24_21d_slope_v150_signal(closeadj, volume):
    b=_pvd_price_trend(closeadj, 63)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)


REGISTRY = {
    "f28pvd_price_volume_divergence_s5r5_5d_slope_v001_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5_5d_slope_v001_signal},
    "f28pvd_price_volume_divergence_s5r21_21d_slope_v002_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21_21d_slope_v002_signal},
    "f28pvd_price_volume_divergence_s21r5_5d_slope_v003_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5_5d_slope_v003_signal},
    "f28pvd_price_volume_divergence_s21r21_21d_slope_v004_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21_21d_slope_v004_signal},
    "f28pvd_price_volume_divergence_s63r5_5d_slope_v005_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5_5d_slope_v005_signal},
    "f28pvd_price_volume_divergence_s63r21_21d_slope_v006_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21_21d_slope_v006_signal},
    "f28pvd_price_volume_divergence_s5r5v1_5d_slope_v007_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v1_5d_slope_v007_signal},
    "f28pvd_price_volume_divergence_s5r21v1_21d_slope_v008_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v1_21d_slope_v008_signal},
    "f28pvd_price_volume_divergence_s21r5v1_5d_slope_v009_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v1_5d_slope_v009_signal},
    "f28pvd_price_volume_divergence_s21r21v1_21d_slope_v010_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v1_21d_slope_v010_signal},
    "f28pvd_price_volume_divergence_s63r5v1_5d_slope_v011_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v1_5d_slope_v011_signal},
    "f28pvd_price_volume_divergence_s63r21v1_21d_slope_v012_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v1_21d_slope_v012_signal},
    "f28pvd_price_volume_divergence_s5r5v2_5d_slope_v013_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v2_5d_slope_v013_signal},
    "f28pvd_price_volume_divergence_s5r21v2_21d_slope_v014_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v2_21d_slope_v014_signal},
    "f28pvd_price_volume_divergence_s21r5v2_5d_slope_v015_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v2_5d_slope_v015_signal},
    "f28pvd_price_volume_divergence_s21r21v2_21d_slope_v016_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v2_21d_slope_v016_signal},
    "f28pvd_price_volume_divergence_s63r5v2_5d_slope_v017_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v2_5d_slope_v017_signal},
    "f28pvd_price_volume_divergence_s63r21v2_21d_slope_v018_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v2_21d_slope_v018_signal},
    "f28pvd_price_volume_divergence_s5r5v3_5d_slope_v019_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v3_5d_slope_v019_signal},
    "f28pvd_price_volume_divergence_s5r21v3_21d_slope_v020_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v3_21d_slope_v020_signal},
    "f28pvd_price_volume_divergence_s21r5v3_5d_slope_v021_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v3_5d_slope_v021_signal},
    "f28pvd_price_volume_divergence_s21r21v3_21d_slope_v022_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v3_21d_slope_v022_signal},
    "f28pvd_price_volume_divergence_s63r5v3_5d_slope_v023_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v3_5d_slope_v023_signal},
    "f28pvd_price_volume_divergence_s63r21v3_21d_slope_v024_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v3_21d_slope_v024_signal},
    "f28pvd_price_volume_divergence_s5r5v4_5d_slope_v025_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v4_5d_slope_v025_signal},
    "f28pvd_price_volume_divergence_s5r21v4_21d_slope_v026_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v4_21d_slope_v026_signal},
    "f28pvd_price_volume_divergence_s21r5v4_5d_slope_v027_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v4_5d_slope_v027_signal},
    "f28pvd_price_volume_divergence_s21r21v4_21d_slope_v028_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v4_21d_slope_v028_signal},
    "f28pvd_price_volume_divergence_s63r5v4_5d_slope_v029_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v4_5d_slope_v029_signal},
    "f28pvd_price_volume_divergence_s63r21v4_21d_slope_v030_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v4_21d_slope_v030_signal},
    "f28pvd_price_volume_divergence_s5r5v5_5d_slope_v031_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v5_5d_slope_v031_signal},
    "f28pvd_price_volume_divergence_s5r21v5_21d_slope_v032_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v5_21d_slope_v032_signal},
    "f28pvd_price_volume_divergence_s21r5v5_5d_slope_v033_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v5_5d_slope_v033_signal},
    "f28pvd_price_volume_divergence_s21r21v5_21d_slope_v034_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v5_21d_slope_v034_signal},
    "f28pvd_price_volume_divergence_s63r5v5_5d_slope_v035_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v5_5d_slope_v035_signal},
    "f28pvd_price_volume_divergence_s63r21v5_21d_slope_v036_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v5_21d_slope_v036_signal},
    "f28pvd_price_volume_divergence_s5r5v6_5d_slope_v037_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v6_5d_slope_v037_signal},
    "f28pvd_price_volume_divergence_s5r21v6_21d_slope_v038_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v6_21d_slope_v038_signal},
    "f28pvd_price_volume_divergence_s21r5v6_5d_slope_v039_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v6_5d_slope_v039_signal},
    "f28pvd_price_volume_divergence_s21r21v6_21d_slope_v040_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v6_21d_slope_v040_signal},
    "f28pvd_price_volume_divergence_s63r5v6_5d_slope_v041_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v6_5d_slope_v041_signal},
    "f28pvd_price_volume_divergence_s63r21v6_21d_slope_v042_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v6_21d_slope_v042_signal},
    "f28pvd_price_volume_divergence_s5r5v7_5d_slope_v043_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v7_5d_slope_v043_signal},
    "f28pvd_price_volume_divergence_s5r21v7_21d_slope_v044_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v7_21d_slope_v044_signal},
    "f28pvd_price_volume_divergence_s21r5v7_5d_slope_v045_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v7_5d_slope_v045_signal},
    "f28pvd_price_volume_divergence_s21r21v7_21d_slope_v046_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v7_21d_slope_v046_signal},
    "f28pvd_price_volume_divergence_s63r5v7_5d_slope_v047_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v7_5d_slope_v047_signal},
    "f28pvd_price_volume_divergence_s63r21v7_21d_slope_v048_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v7_21d_slope_v048_signal},
    "f28pvd_price_volume_divergence_s5r5v8_5d_slope_v049_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v8_5d_slope_v049_signal},
    "f28pvd_price_volume_divergence_s5r21v8_21d_slope_v050_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v8_21d_slope_v050_signal},
    "f28pvd_price_volume_divergence_s21r5v8_5d_slope_v051_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v8_5d_slope_v051_signal},
    "f28pvd_price_volume_divergence_s21r21v8_21d_slope_v052_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v8_21d_slope_v052_signal},
    "f28pvd_price_volume_divergence_s63r5v8_5d_slope_v053_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v8_5d_slope_v053_signal},
    "f28pvd_price_volume_divergence_s63r21v8_21d_slope_v054_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v8_21d_slope_v054_signal},
    "f28pvd_price_volume_divergence_s5r5v9_5d_slope_v055_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v9_5d_slope_v055_signal},
    "f28pvd_price_volume_divergence_s5r21v9_21d_slope_v056_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v9_21d_slope_v056_signal},
    "f28pvd_price_volume_divergence_s21r5v9_5d_slope_v057_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v9_5d_slope_v057_signal},
    "f28pvd_price_volume_divergence_s21r21v9_21d_slope_v058_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v9_21d_slope_v058_signal},
    "f28pvd_price_volume_divergence_s63r5v9_5d_slope_v059_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v9_5d_slope_v059_signal},
    "f28pvd_price_volume_divergence_s63r21v9_21d_slope_v060_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v9_21d_slope_v060_signal},
    "f28pvd_price_volume_divergence_s5r5v10_5d_slope_v061_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v10_5d_slope_v061_signal},
    "f28pvd_price_volume_divergence_s5r21v10_21d_slope_v062_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v10_21d_slope_v062_signal},
    "f28pvd_price_volume_divergence_s21r5v10_5d_slope_v063_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v10_5d_slope_v063_signal},
    "f28pvd_price_volume_divergence_s21r21v10_21d_slope_v064_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v10_21d_slope_v064_signal},
    "f28pvd_price_volume_divergence_s63r5v10_5d_slope_v065_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v10_5d_slope_v065_signal},
    "f28pvd_price_volume_divergence_s63r21v10_21d_slope_v066_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v10_21d_slope_v066_signal},
    "f28pvd_price_volume_divergence_s5r5v11_5d_slope_v067_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v11_5d_slope_v067_signal},
    "f28pvd_price_volume_divergence_s5r21v11_21d_slope_v068_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v11_21d_slope_v068_signal},
    "f28pvd_price_volume_divergence_s21r5v11_5d_slope_v069_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v11_5d_slope_v069_signal},
    "f28pvd_price_volume_divergence_s21r21v11_21d_slope_v070_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v11_21d_slope_v070_signal},
    "f28pvd_price_volume_divergence_s63r5v11_5d_slope_v071_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v11_5d_slope_v071_signal},
    "f28pvd_price_volume_divergence_s63r21v11_21d_slope_v072_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v11_21d_slope_v072_signal},
    "f28pvd_price_volume_divergence_s5r5v12_5d_slope_v073_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v12_5d_slope_v073_signal},
    "f28pvd_price_volume_divergence_s5r21v12_21d_slope_v074_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v12_21d_slope_v074_signal},
    "f28pvd_price_volume_divergence_s21r5v12_5d_slope_v075_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v12_5d_slope_v075_signal},
    "f28pvd_price_volume_divergence_s21r21v12_21d_slope_v076_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v12_21d_slope_v076_signal},
    "f28pvd_price_volume_divergence_s63r5v12_5d_slope_v077_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v12_5d_slope_v077_signal},
    "f28pvd_price_volume_divergence_s63r21v12_21d_slope_v078_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v12_21d_slope_v078_signal},
    "f28pvd_price_volume_divergence_s5r5v13_5d_slope_v079_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v13_5d_slope_v079_signal},
    "f28pvd_price_volume_divergence_s5r21v13_21d_slope_v080_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v13_21d_slope_v080_signal},
    "f28pvd_price_volume_divergence_s21r5v13_5d_slope_v081_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v13_5d_slope_v081_signal},
    "f28pvd_price_volume_divergence_s21r21v13_21d_slope_v082_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v13_21d_slope_v082_signal},
    "f28pvd_price_volume_divergence_s63r5v13_5d_slope_v083_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v13_5d_slope_v083_signal},
    "f28pvd_price_volume_divergence_s63r21v13_21d_slope_v084_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v13_21d_slope_v084_signal},
    "f28pvd_price_volume_divergence_s5r5v14_5d_slope_v085_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v14_5d_slope_v085_signal},
    "f28pvd_price_volume_divergence_s5r21v14_21d_slope_v086_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v14_21d_slope_v086_signal},
    "f28pvd_price_volume_divergence_s21r5v14_5d_slope_v087_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v14_5d_slope_v087_signal},
    "f28pvd_price_volume_divergence_s21r21v14_21d_slope_v088_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v14_21d_slope_v088_signal},
    "f28pvd_price_volume_divergence_s63r5v14_5d_slope_v089_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v14_5d_slope_v089_signal},
    "f28pvd_price_volume_divergence_s63r21v14_21d_slope_v090_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v14_21d_slope_v090_signal},
    "f28pvd_price_volume_divergence_s5r5v15_5d_slope_v091_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v15_5d_slope_v091_signal},
    "f28pvd_price_volume_divergence_s5r21v15_21d_slope_v092_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v15_21d_slope_v092_signal},
    "f28pvd_price_volume_divergence_s21r5v15_5d_slope_v093_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v15_5d_slope_v093_signal},
    "f28pvd_price_volume_divergence_s21r21v15_21d_slope_v094_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v15_21d_slope_v094_signal},
    "f28pvd_price_volume_divergence_s63r5v15_5d_slope_v095_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v15_5d_slope_v095_signal},
    "f28pvd_price_volume_divergence_s63r21v15_21d_slope_v096_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v15_21d_slope_v096_signal},
    "f28pvd_price_volume_divergence_s5r5v16_5d_slope_v097_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v16_5d_slope_v097_signal},
    "f28pvd_price_volume_divergence_s5r21v16_21d_slope_v098_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v16_21d_slope_v098_signal},
    "f28pvd_price_volume_divergence_s21r5v16_5d_slope_v099_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v16_5d_slope_v099_signal},
    "f28pvd_price_volume_divergence_s21r21v16_21d_slope_v100_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v16_21d_slope_v100_signal},
    "f28pvd_price_volume_divergence_s63r5v16_5d_slope_v101_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v16_5d_slope_v101_signal},
    "f28pvd_price_volume_divergence_s63r21v16_21d_slope_v102_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v16_21d_slope_v102_signal},
    "f28pvd_price_volume_divergence_s5r5v17_5d_slope_v103_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v17_5d_slope_v103_signal},
    "f28pvd_price_volume_divergence_s5r21v17_21d_slope_v104_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v17_21d_slope_v104_signal},
    "f28pvd_price_volume_divergence_s21r5v17_5d_slope_v105_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v17_5d_slope_v105_signal},
    "f28pvd_price_volume_divergence_s21r21v17_21d_slope_v106_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v17_21d_slope_v106_signal},
    "f28pvd_price_volume_divergence_s63r5v17_5d_slope_v107_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v17_5d_slope_v107_signal},
    "f28pvd_price_volume_divergence_s63r21v17_21d_slope_v108_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v17_21d_slope_v108_signal},
    "f28pvd_price_volume_divergence_s5r5v18_5d_slope_v109_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v18_5d_slope_v109_signal},
    "f28pvd_price_volume_divergence_s5r21v18_21d_slope_v110_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v18_21d_slope_v110_signal},
    "f28pvd_price_volume_divergence_s21r5v18_5d_slope_v111_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v18_5d_slope_v111_signal},
    "f28pvd_price_volume_divergence_s21r21v18_21d_slope_v112_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v18_21d_slope_v112_signal},
    "f28pvd_price_volume_divergence_s63r5v18_5d_slope_v113_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v18_5d_slope_v113_signal},
    "f28pvd_price_volume_divergence_s63r21v18_21d_slope_v114_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v18_21d_slope_v114_signal},
    "f28pvd_price_volume_divergence_s5r5v19_5d_slope_v115_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v19_5d_slope_v115_signal},
    "f28pvd_price_volume_divergence_s5r21v19_21d_slope_v116_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v19_21d_slope_v116_signal},
    "f28pvd_price_volume_divergence_s21r5v19_5d_slope_v117_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v19_5d_slope_v117_signal},
    "f28pvd_price_volume_divergence_s21r21v19_21d_slope_v118_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v19_21d_slope_v118_signal},
    "f28pvd_price_volume_divergence_s63r5v19_5d_slope_v119_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v19_5d_slope_v119_signal},
    "f28pvd_price_volume_divergence_s63r21v19_21d_slope_v120_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v19_21d_slope_v120_signal},
    "f28pvd_price_volume_divergence_s5r5v20_5d_slope_v121_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v20_5d_slope_v121_signal},
    "f28pvd_price_volume_divergence_s5r21v20_21d_slope_v122_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v20_21d_slope_v122_signal},
    "f28pvd_price_volume_divergence_s21r5v20_5d_slope_v123_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v20_5d_slope_v123_signal},
    "f28pvd_price_volume_divergence_s21r21v20_21d_slope_v124_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v20_21d_slope_v124_signal},
    "f28pvd_price_volume_divergence_s63r5v20_5d_slope_v125_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v20_5d_slope_v125_signal},
    "f28pvd_price_volume_divergence_s63r21v20_21d_slope_v126_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v20_21d_slope_v126_signal},
    "f28pvd_price_volume_divergence_s5r5v21_5d_slope_v127_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v21_5d_slope_v127_signal},
    "f28pvd_price_volume_divergence_s5r21v21_21d_slope_v128_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v21_21d_slope_v128_signal},
    "f28pvd_price_volume_divergence_s21r5v21_5d_slope_v129_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v21_5d_slope_v129_signal},
    "f28pvd_price_volume_divergence_s21r21v21_21d_slope_v130_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v21_21d_slope_v130_signal},
    "f28pvd_price_volume_divergence_s63r5v21_5d_slope_v131_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v21_5d_slope_v131_signal},
    "f28pvd_price_volume_divergence_s63r21v21_21d_slope_v132_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v21_21d_slope_v132_signal},
    "f28pvd_price_volume_divergence_s5r5v22_5d_slope_v133_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v22_5d_slope_v133_signal},
    "f28pvd_price_volume_divergence_s5r21v22_21d_slope_v134_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v22_21d_slope_v134_signal},
    "f28pvd_price_volume_divergence_s21r5v22_5d_slope_v135_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v22_5d_slope_v135_signal},
    "f28pvd_price_volume_divergence_s21r21v22_21d_slope_v136_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v22_21d_slope_v136_signal},
    "f28pvd_price_volume_divergence_s63r5v22_5d_slope_v137_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v22_5d_slope_v137_signal},
    "f28pvd_price_volume_divergence_s63r21v22_21d_slope_v138_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v22_21d_slope_v138_signal},
    "f28pvd_price_volume_divergence_s5r5v23_5d_slope_v139_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v23_5d_slope_v139_signal},
    "f28pvd_price_volume_divergence_s5r21v23_21d_slope_v140_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v23_21d_slope_v140_signal},
    "f28pvd_price_volume_divergence_s21r5v23_5d_slope_v141_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v23_5d_slope_v141_signal},
    "f28pvd_price_volume_divergence_s21r21v23_21d_slope_v142_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v23_21d_slope_v142_signal},
    "f28pvd_price_volume_divergence_s63r5v23_5d_slope_v143_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v23_5d_slope_v143_signal},
    "f28pvd_price_volume_divergence_s63r21v23_21d_slope_v144_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v23_21d_slope_v144_signal},
    "f28pvd_price_volume_divergence_s5r5v24_5d_slope_v145_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r5v24_5d_slope_v145_signal},
    "f28pvd_price_volume_divergence_s5r21v24_21d_slope_v146_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s5r21v24_21d_slope_v146_signal},
    "f28pvd_price_volume_divergence_s21r5v24_5d_slope_v147_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r5v24_5d_slope_v147_signal},
    "f28pvd_price_volume_divergence_s21r21v24_21d_slope_v148_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s21r21v24_21d_slope_v148_signal},
    "f28pvd_price_volume_divergence_s63r5v24_5d_slope_v149_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r5v24_5d_slope_v149_signal},
    "f28pvd_price_volume_divergence_s63r21v24_21d_slope_v150_signal": {"inputs": ["closeadj", "volume"], "func": f28pvd_price_volume_divergence_s63r21v24_21d_slope_v150_signal}
}
F28_PRICE_VOLUME_DIVERGENCE_REGISTRY_SLOPE = REGISTRY

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
        assert "_pvd_price_trend" in src or "_pvd_vol_trend" in src or "_pvd_divergence" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F28_PRICE_VOLUME_DIVERGENCE_REGISTRY_SLOPE")
