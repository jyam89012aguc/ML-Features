import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _vwd_tp(high, low, close):
    return (high + low + close) / 3.0
def _vwd_vwap(high, low, close, volume, w):
    tp = _vwd_tp(high, low, close)
    return (tp * volume).rolling(w, min_periods=max(1, w//2)).sum() / volume.rolling(w, min_periods=max(1, w//2)).sum().replace(0, np.nan)
def _vwd_dev(high, low, close, volume, w):
    vwap = _vwd_vwap(high, low, close, volume, w)
    return (close / vwap.replace(0, np.nan)) - 1.0

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5_5d_slope_v001_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21_21d_slope_v002_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5_5d_slope_v003_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21_21d_slope_v004_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5_5d_slope_v005_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21_21d_slope_v006_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v1_5d_slope_v007_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v1_21d_slope_v008_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v1_5d_slope_v009_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v1_21d_slope_v010_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v1_5d_slope_v011_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v1_21d_slope_v012_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v2_5d_slope_v013_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v2_21d_slope_v014_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v2_5d_slope_v015_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v2_21d_slope_v016_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v2_5d_slope_v017_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v2_21d_slope_v018_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v3_5d_slope_v019_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v3_21d_slope_v020_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v3_5d_slope_v021_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v3_21d_slope_v022_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v3_5d_slope_v023_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v3_21d_slope_v024_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v4_5d_slope_v025_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v4_21d_slope_v026_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v4_5d_slope_v027_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v4_21d_slope_v028_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v4_5d_slope_v029_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v4_21d_slope_v030_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v5_5d_slope_v031_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v5_21d_slope_v032_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v5_5d_slope_v033_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v5_21d_slope_v034_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v5_5d_slope_v035_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v5_21d_slope_v036_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v6_5d_slope_v037_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v6_21d_slope_v038_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v6_5d_slope_v039_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v6_21d_slope_v040_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v6_5d_slope_v041_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v6_21d_slope_v042_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v7_5d_slope_v043_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v7_21d_slope_v044_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v7_5d_slope_v045_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v7_21d_slope_v046_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v7_5d_slope_v047_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v7_21d_slope_v048_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v8_5d_slope_v049_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v8_21d_slope_v050_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v8_5d_slope_v051_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v8_21d_slope_v052_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v8_5d_slope_v053_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v8_21d_slope_v054_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v9_5d_slope_v055_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v9_21d_slope_v056_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v9_5d_slope_v057_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v9_21d_slope_v058_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v9_5d_slope_v059_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v9_21d_slope_v060_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v10_5d_slope_v061_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v10_21d_slope_v062_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v10_5d_slope_v063_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v10_21d_slope_v064_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v10_5d_slope_v065_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v10_21d_slope_v066_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v11_5d_slope_v067_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v11_21d_slope_v068_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v11_5d_slope_v069_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v11_21d_slope_v070_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v11_5d_slope_v071_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v11_21d_slope_v072_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v12_5d_slope_v073_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v12_21d_slope_v074_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v12_5d_slope_v075_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v12_21d_slope_v076_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v12_5d_slope_v077_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v12_21d_slope_v078_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v13_5d_slope_v079_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v13_21d_slope_v080_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v13_5d_slope_v081_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v13_21d_slope_v082_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v13_5d_slope_v083_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v13_21d_slope_v084_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v14_5d_slope_v085_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v14_21d_slope_v086_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v14_5d_slope_v087_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v14_21d_slope_v088_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v14_5d_slope_v089_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v14_21d_slope_v090_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v15_5d_slope_v091_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v15_21d_slope_v092_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v15_5d_slope_v093_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v15_21d_slope_v094_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v15_5d_slope_v095_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v15_21d_slope_v096_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v16_5d_slope_v097_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v16_21d_slope_v098_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v16_5d_slope_v099_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v16_21d_slope_v100_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v16_5d_slope_v101_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v16_21d_slope_v102_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v17_5d_slope_v103_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v17_21d_slope_v104_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v17_5d_slope_v105_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v17_21d_slope_v106_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v17_5d_slope_v107_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v17_21d_slope_v108_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v18_5d_slope_v109_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v18_21d_slope_v110_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v18_5d_slope_v111_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v18_21d_slope_v112_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v18_5d_slope_v113_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v18_21d_slope_v114_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v19_5d_slope_v115_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v19_21d_slope_v116_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v19_5d_slope_v117_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v19_21d_slope_v118_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v19_5d_slope_v119_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v19_21d_slope_v120_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v20_5d_slope_v121_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v20_21d_slope_v122_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v20_5d_slope_v123_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v20_21d_slope_v124_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v20_5d_slope_v125_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v20_21d_slope_v126_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v21_5d_slope_v127_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v21_21d_slope_v128_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v21_5d_slope_v129_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v21_21d_slope_v130_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v21_5d_slope_v131_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v21_21d_slope_v132_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v22_5d_slope_v133_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v22_21d_slope_v134_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v22_5d_slope_v135_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v22_21d_slope_v136_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v22_5d_slope_v137_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v22_21d_slope_v138_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v23_5d_slope_v139_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v23_21d_slope_v140_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v23_5d_slope_v141_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v23_21d_slope_v142_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v23_5d_slope_v143_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(5),21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v23_21d_slope_v144_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=_z(b.pct_change(21),84)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=5d
def f25vwd_vwap_deviation_s5r5v24_5d_slope_v145_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=5 roc=21d
def f25vwd_vwap_deviation_s5r21v24_21d_slope_v146_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=5d
def f25vwd_vwap_deviation_s21r5v24_5d_slope_v147_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=21 roc=21d
def f25vwd_vwap_deviation_s21r21v24_21d_slope_v148_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=5d
def f25vwd_vwap_deviation_s63r5v24_5d_slope_v149_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# slope of _vwd_tp w=63 roc=21d
def f25vwd_vwap_deviation_s63r21v24_21d_slope_v150_signal(close, high, low, volume):
    b=_vwd_tp(high, low, close)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)


REGISTRY = {
    "f25vwd_vwap_deviation_s5r5_5d_slope_v001_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5_5d_slope_v001_signal},
    "f25vwd_vwap_deviation_s5r21_21d_slope_v002_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21_21d_slope_v002_signal},
    "f25vwd_vwap_deviation_s21r5_5d_slope_v003_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5_5d_slope_v003_signal},
    "f25vwd_vwap_deviation_s21r21_21d_slope_v004_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21_21d_slope_v004_signal},
    "f25vwd_vwap_deviation_s63r5_5d_slope_v005_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5_5d_slope_v005_signal},
    "f25vwd_vwap_deviation_s63r21_21d_slope_v006_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21_21d_slope_v006_signal},
    "f25vwd_vwap_deviation_s5r5v1_5d_slope_v007_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v1_5d_slope_v007_signal},
    "f25vwd_vwap_deviation_s5r21v1_21d_slope_v008_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v1_21d_slope_v008_signal},
    "f25vwd_vwap_deviation_s21r5v1_5d_slope_v009_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v1_5d_slope_v009_signal},
    "f25vwd_vwap_deviation_s21r21v1_21d_slope_v010_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v1_21d_slope_v010_signal},
    "f25vwd_vwap_deviation_s63r5v1_5d_slope_v011_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v1_5d_slope_v011_signal},
    "f25vwd_vwap_deviation_s63r21v1_21d_slope_v012_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v1_21d_slope_v012_signal},
    "f25vwd_vwap_deviation_s5r5v2_5d_slope_v013_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v2_5d_slope_v013_signal},
    "f25vwd_vwap_deviation_s5r21v2_21d_slope_v014_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v2_21d_slope_v014_signal},
    "f25vwd_vwap_deviation_s21r5v2_5d_slope_v015_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v2_5d_slope_v015_signal},
    "f25vwd_vwap_deviation_s21r21v2_21d_slope_v016_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v2_21d_slope_v016_signal},
    "f25vwd_vwap_deviation_s63r5v2_5d_slope_v017_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v2_5d_slope_v017_signal},
    "f25vwd_vwap_deviation_s63r21v2_21d_slope_v018_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v2_21d_slope_v018_signal},
    "f25vwd_vwap_deviation_s5r5v3_5d_slope_v019_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v3_5d_slope_v019_signal},
    "f25vwd_vwap_deviation_s5r21v3_21d_slope_v020_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v3_21d_slope_v020_signal},
    "f25vwd_vwap_deviation_s21r5v3_5d_slope_v021_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v3_5d_slope_v021_signal},
    "f25vwd_vwap_deviation_s21r21v3_21d_slope_v022_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v3_21d_slope_v022_signal},
    "f25vwd_vwap_deviation_s63r5v3_5d_slope_v023_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v3_5d_slope_v023_signal},
    "f25vwd_vwap_deviation_s63r21v3_21d_slope_v024_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v3_21d_slope_v024_signal},
    "f25vwd_vwap_deviation_s5r5v4_5d_slope_v025_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v4_5d_slope_v025_signal},
    "f25vwd_vwap_deviation_s5r21v4_21d_slope_v026_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v4_21d_slope_v026_signal},
    "f25vwd_vwap_deviation_s21r5v4_5d_slope_v027_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v4_5d_slope_v027_signal},
    "f25vwd_vwap_deviation_s21r21v4_21d_slope_v028_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v4_21d_slope_v028_signal},
    "f25vwd_vwap_deviation_s63r5v4_5d_slope_v029_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v4_5d_slope_v029_signal},
    "f25vwd_vwap_deviation_s63r21v4_21d_slope_v030_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v4_21d_slope_v030_signal},
    "f25vwd_vwap_deviation_s5r5v5_5d_slope_v031_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v5_5d_slope_v031_signal},
    "f25vwd_vwap_deviation_s5r21v5_21d_slope_v032_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v5_21d_slope_v032_signal},
    "f25vwd_vwap_deviation_s21r5v5_5d_slope_v033_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v5_5d_slope_v033_signal},
    "f25vwd_vwap_deviation_s21r21v5_21d_slope_v034_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v5_21d_slope_v034_signal},
    "f25vwd_vwap_deviation_s63r5v5_5d_slope_v035_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v5_5d_slope_v035_signal},
    "f25vwd_vwap_deviation_s63r21v5_21d_slope_v036_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v5_21d_slope_v036_signal},
    "f25vwd_vwap_deviation_s5r5v6_5d_slope_v037_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v6_5d_slope_v037_signal},
    "f25vwd_vwap_deviation_s5r21v6_21d_slope_v038_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v6_21d_slope_v038_signal},
    "f25vwd_vwap_deviation_s21r5v6_5d_slope_v039_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v6_5d_slope_v039_signal},
    "f25vwd_vwap_deviation_s21r21v6_21d_slope_v040_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v6_21d_slope_v040_signal},
    "f25vwd_vwap_deviation_s63r5v6_5d_slope_v041_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v6_5d_slope_v041_signal},
    "f25vwd_vwap_deviation_s63r21v6_21d_slope_v042_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v6_21d_slope_v042_signal},
    "f25vwd_vwap_deviation_s5r5v7_5d_slope_v043_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v7_5d_slope_v043_signal},
    "f25vwd_vwap_deviation_s5r21v7_21d_slope_v044_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v7_21d_slope_v044_signal},
    "f25vwd_vwap_deviation_s21r5v7_5d_slope_v045_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v7_5d_slope_v045_signal},
    "f25vwd_vwap_deviation_s21r21v7_21d_slope_v046_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v7_21d_slope_v046_signal},
    "f25vwd_vwap_deviation_s63r5v7_5d_slope_v047_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v7_5d_slope_v047_signal},
    "f25vwd_vwap_deviation_s63r21v7_21d_slope_v048_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v7_21d_slope_v048_signal},
    "f25vwd_vwap_deviation_s5r5v8_5d_slope_v049_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v8_5d_slope_v049_signal},
    "f25vwd_vwap_deviation_s5r21v8_21d_slope_v050_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v8_21d_slope_v050_signal},
    "f25vwd_vwap_deviation_s21r5v8_5d_slope_v051_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v8_5d_slope_v051_signal},
    "f25vwd_vwap_deviation_s21r21v8_21d_slope_v052_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v8_21d_slope_v052_signal},
    "f25vwd_vwap_deviation_s63r5v8_5d_slope_v053_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v8_5d_slope_v053_signal},
    "f25vwd_vwap_deviation_s63r21v8_21d_slope_v054_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v8_21d_slope_v054_signal},
    "f25vwd_vwap_deviation_s5r5v9_5d_slope_v055_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v9_5d_slope_v055_signal},
    "f25vwd_vwap_deviation_s5r21v9_21d_slope_v056_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v9_21d_slope_v056_signal},
    "f25vwd_vwap_deviation_s21r5v9_5d_slope_v057_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v9_5d_slope_v057_signal},
    "f25vwd_vwap_deviation_s21r21v9_21d_slope_v058_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v9_21d_slope_v058_signal},
    "f25vwd_vwap_deviation_s63r5v9_5d_slope_v059_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v9_5d_slope_v059_signal},
    "f25vwd_vwap_deviation_s63r21v9_21d_slope_v060_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v9_21d_slope_v060_signal},
    "f25vwd_vwap_deviation_s5r5v10_5d_slope_v061_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v10_5d_slope_v061_signal},
    "f25vwd_vwap_deviation_s5r21v10_21d_slope_v062_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v10_21d_slope_v062_signal},
    "f25vwd_vwap_deviation_s21r5v10_5d_slope_v063_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v10_5d_slope_v063_signal},
    "f25vwd_vwap_deviation_s21r21v10_21d_slope_v064_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v10_21d_slope_v064_signal},
    "f25vwd_vwap_deviation_s63r5v10_5d_slope_v065_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v10_5d_slope_v065_signal},
    "f25vwd_vwap_deviation_s63r21v10_21d_slope_v066_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v10_21d_slope_v066_signal},
    "f25vwd_vwap_deviation_s5r5v11_5d_slope_v067_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v11_5d_slope_v067_signal},
    "f25vwd_vwap_deviation_s5r21v11_21d_slope_v068_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v11_21d_slope_v068_signal},
    "f25vwd_vwap_deviation_s21r5v11_5d_slope_v069_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v11_5d_slope_v069_signal},
    "f25vwd_vwap_deviation_s21r21v11_21d_slope_v070_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v11_21d_slope_v070_signal},
    "f25vwd_vwap_deviation_s63r5v11_5d_slope_v071_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v11_5d_slope_v071_signal},
    "f25vwd_vwap_deviation_s63r21v11_21d_slope_v072_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v11_21d_slope_v072_signal},
    "f25vwd_vwap_deviation_s5r5v12_5d_slope_v073_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v12_5d_slope_v073_signal},
    "f25vwd_vwap_deviation_s5r21v12_21d_slope_v074_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v12_21d_slope_v074_signal},
    "f25vwd_vwap_deviation_s21r5v12_5d_slope_v075_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v12_5d_slope_v075_signal},
    "f25vwd_vwap_deviation_s21r21v12_21d_slope_v076_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v12_21d_slope_v076_signal},
    "f25vwd_vwap_deviation_s63r5v12_5d_slope_v077_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v12_5d_slope_v077_signal},
    "f25vwd_vwap_deviation_s63r21v12_21d_slope_v078_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v12_21d_slope_v078_signal},
    "f25vwd_vwap_deviation_s5r5v13_5d_slope_v079_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v13_5d_slope_v079_signal},
    "f25vwd_vwap_deviation_s5r21v13_21d_slope_v080_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v13_21d_slope_v080_signal},
    "f25vwd_vwap_deviation_s21r5v13_5d_slope_v081_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v13_5d_slope_v081_signal},
    "f25vwd_vwap_deviation_s21r21v13_21d_slope_v082_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v13_21d_slope_v082_signal},
    "f25vwd_vwap_deviation_s63r5v13_5d_slope_v083_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v13_5d_slope_v083_signal},
    "f25vwd_vwap_deviation_s63r21v13_21d_slope_v084_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v13_21d_slope_v084_signal},
    "f25vwd_vwap_deviation_s5r5v14_5d_slope_v085_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v14_5d_slope_v085_signal},
    "f25vwd_vwap_deviation_s5r21v14_21d_slope_v086_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v14_21d_slope_v086_signal},
    "f25vwd_vwap_deviation_s21r5v14_5d_slope_v087_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v14_5d_slope_v087_signal},
    "f25vwd_vwap_deviation_s21r21v14_21d_slope_v088_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v14_21d_slope_v088_signal},
    "f25vwd_vwap_deviation_s63r5v14_5d_slope_v089_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v14_5d_slope_v089_signal},
    "f25vwd_vwap_deviation_s63r21v14_21d_slope_v090_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v14_21d_slope_v090_signal},
    "f25vwd_vwap_deviation_s5r5v15_5d_slope_v091_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v15_5d_slope_v091_signal},
    "f25vwd_vwap_deviation_s5r21v15_21d_slope_v092_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v15_21d_slope_v092_signal},
    "f25vwd_vwap_deviation_s21r5v15_5d_slope_v093_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v15_5d_slope_v093_signal},
    "f25vwd_vwap_deviation_s21r21v15_21d_slope_v094_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v15_21d_slope_v094_signal},
    "f25vwd_vwap_deviation_s63r5v15_5d_slope_v095_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v15_5d_slope_v095_signal},
    "f25vwd_vwap_deviation_s63r21v15_21d_slope_v096_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v15_21d_slope_v096_signal},
    "f25vwd_vwap_deviation_s5r5v16_5d_slope_v097_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v16_5d_slope_v097_signal},
    "f25vwd_vwap_deviation_s5r21v16_21d_slope_v098_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v16_21d_slope_v098_signal},
    "f25vwd_vwap_deviation_s21r5v16_5d_slope_v099_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v16_5d_slope_v099_signal},
    "f25vwd_vwap_deviation_s21r21v16_21d_slope_v100_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v16_21d_slope_v100_signal},
    "f25vwd_vwap_deviation_s63r5v16_5d_slope_v101_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v16_5d_slope_v101_signal},
    "f25vwd_vwap_deviation_s63r21v16_21d_slope_v102_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v16_21d_slope_v102_signal},
    "f25vwd_vwap_deviation_s5r5v17_5d_slope_v103_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v17_5d_slope_v103_signal},
    "f25vwd_vwap_deviation_s5r21v17_21d_slope_v104_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v17_21d_slope_v104_signal},
    "f25vwd_vwap_deviation_s21r5v17_5d_slope_v105_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v17_5d_slope_v105_signal},
    "f25vwd_vwap_deviation_s21r21v17_21d_slope_v106_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v17_21d_slope_v106_signal},
    "f25vwd_vwap_deviation_s63r5v17_5d_slope_v107_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v17_5d_slope_v107_signal},
    "f25vwd_vwap_deviation_s63r21v17_21d_slope_v108_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v17_21d_slope_v108_signal},
    "f25vwd_vwap_deviation_s5r5v18_5d_slope_v109_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v18_5d_slope_v109_signal},
    "f25vwd_vwap_deviation_s5r21v18_21d_slope_v110_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v18_21d_slope_v110_signal},
    "f25vwd_vwap_deviation_s21r5v18_5d_slope_v111_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v18_5d_slope_v111_signal},
    "f25vwd_vwap_deviation_s21r21v18_21d_slope_v112_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v18_21d_slope_v112_signal},
    "f25vwd_vwap_deviation_s63r5v18_5d_slope_v113_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v18_5d_slope_v113_signal},
    "f25vwd_vwap_deviation_s63r21v18_21d_slope_v114_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v18_21d_slope_v114_signal},
    "f25vwd_vwap_deviation_s5r5v19_5d_slope_v115_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v19_5d_slope_v115_signal},
    "f25vwd_vwap_deviation_s5r21v19_21d_slope_v116_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v19_21d_slope_v116_signal},
    "f25vwd_vwap_deviation_s21r5v19_5d_slope_v117_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v19_5d_slope_v117_signal},
    "f25vwd_vwap_deviation_s21r21v19_21d_slope_v118_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v19_21d_slope_v118_signal},
    "f25vwd_vwap_deviation_s63r5v19_5d_slope_v119_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v19_5d_slope_v119_signal},
    "f25vwd_vwap_deviation_s63r21v19_21d_slope_v120_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v19_21d_slope_v120_signal},
    "f25vwd_vwap_deviation_s5r5v20_5d_slope_v121_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v20_5d_slope_v121_signal},
    "f25vwd_vwap_deviation_s5r21v20_21d_slope_v122_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v20_21d_slope_v122_signal},
    "f25vwd_vwap_deviation_s21r5v20_5d_slope_v123_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v20_5d_slope_v123_signal},
    "f25vwd_vwap_deviation_s21r21v20_21d_slope_v124_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v20_21d_slope_v124_signal},
    "f25vwd_vwap_deviation_s63r5v20_5d_slope_v125_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v20_5d_slope_v125_signal},
    "f25vwd_vwap_deviation_s63r21v20_21d_slope_v126_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v20_21d_slope_v126_signal},
    "f25vwd_vwap_deviation_s5r5v21_5d_slope_v127_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v21_5d_slope_v127_signal},
    "f25vwd_vwap_deviation_s5r21v21_21d_slope_v128_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v21_21d_slope_v128_signal},
    "f25vwd_vwap_deviation_s21r5v21_5d_slope_v129_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v21_5d_slope_v129_signal},
    "f25vwd_vwap_deviation_s21r21v21_21d_slope_v130_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v21_21d_slope_v130_signal},
    "f25vwd_vwap_deviation_s63r5v21_5d_slope_v131_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v21_5d_slope_v131_signal},
    "f25vwd_vwap_deviation_s63r21v21_21d_slope_v132_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v21_21d_slope_v132_signal},
    "f25vwd_vwap_deviation_s5r5v22_5d_slope_v133_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v22_5d_slope_v133_signal},
    "f25vwd_vwap_deviation_s5r21v22_21d_slope_v134_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v22_21d_slope_v134_signal},
    "f25vwd_vwap_deviation_s21r5v22_5d_slope_v135_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v22_5d_slope_v135_signal},
    "f25vwd_vwap_deviation_s21r21v22_21d_slope_v136_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v22_21d_slope_v136_signal},
    "f25vwd_vwap_deviation_s63r5v22_5d_slope_v137_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v22_5d_slope_v137_signal},
    "f25vwd_vwap_deviation_s63r21v22_21d_slope_v138_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v22_21d_slope_v138_signal},
    "f25vwd_vwap_deviation_s5r5v23_5d_slope_v139_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v23_5d_slope_v139_signal},
    "f25vwd_vwap_deviation_s5r21v23_21d_slope_v140_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v23_21d_slope_v140_signal},
    "f25vwd_vwap_deviation_s21r5v23_5d_slope_v141_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v23_5d_slope_v141_signal},
    "f25vwd_vwap_deviation_s21r21v23_21d_slope_v142_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v23_21d_slope_v142_signal},
    "f25vwd_vwap_deviation_s63r5v23_5d_slope_v143_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v23_5d_slope_v143_signal},
    "f25vwd_vwap_deviation_s63r21v23_21d_slope_v144_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v23_21d_slope_v144_signal},
    "f25vwd_vwap_deviation_s5r5v24_5d_slope_v145_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r5v24_5d_slope_v145_signal},
    "f25vwd_vwap_deviation_s5r21v24_21d_slope_v146_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s5r21v24_21d_slope_v146_signal},
    "f25vwd_vwap_deviation_s21r5v24_5d_slope_v147_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r5v24_5d_slope_v147_signal},
    "f25vwd_vwap_deviation_s21r21v24_21d_slope_v148_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s21r21v24_21d_slope_v148_signal},
    "f25vwd_vwap_deviation_s63r5v24_5d_slope_v149_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r5v24_5d_slope_v149_signal},
    "f25vwd_vwap_deviation_s63r21v24_21d_slope_v150_signal": {"inputs": ["close", "high", "low", "volume"], "func": f25vwd_vwap_deviation_s63r21v24_21d_slope_v150_signal}
}
F25_VWAP_DEVIATION_REGISTRY_SLOPE = REGISTRY

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
        assert "_vwd_tp" in src or "_vwd_vwap" in src or "_vwd_dev" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F25_VWAP_DEVIATION_REGISTRY_SLOPE")
