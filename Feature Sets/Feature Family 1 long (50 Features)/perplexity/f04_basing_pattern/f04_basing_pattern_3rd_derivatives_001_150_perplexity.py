import numpy as np
import pandas as pd

def _z(x, w):
    mu = x.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = x.rolling(w, min_periods=max(1, w // 2)).std()
    return (x - mu) / sd.replace(0, np.nan)

def _prank(x, w):
    return x.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)

def _minmax(x, w):
    lo = x.rolling(w, min_periods=max(1, w // 2)).min()
    hi = x.rolling(w, min_periods=max(1, w // 2)).max()
    return (x - lo) / (hi - lo).replace(0, np.nan)

def _safe_div(a, b):
    return a / b.replace(0, np.nan)

def _bsp_range_compression(high, low, w):
    rng = (high - low) / low.abs().replace(0, np.nan)
    return rng / rng.rolling(w, min_periods=max(1, w//2)).mean().replace(0, np.nan)
def _bsp_price_flatness(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w//2)).std() / closeadj.rolling(w, min_periods=max(1, w//2)).mean().abs().replace(0, np.nan)


# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v001_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v002_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v003_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v004_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v005_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v006_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v007_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v008_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v009_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v010_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v011_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v012_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v013_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v014_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v015_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v016_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v017_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v018_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v019_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v020_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v021_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v022_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v023_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v024_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v025_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v026_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v027_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v028_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v029_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v030_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v031_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v032_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v033_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v034_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v035_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v036_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v037_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v038_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v039_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v040_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v041_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v042_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v043_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v044_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v045_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v046_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v047_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v048_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v049_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v050_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v051_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v052_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v053_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v054_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v055_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v056_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v057_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v058_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v059_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v060_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v061_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v062_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v063_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v064_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v065_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v066_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v067_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v068_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v069_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v070_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v071_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v072_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v073_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v074_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v075_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v076_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v077_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v078_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v079_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v080_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v081_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v082_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v083_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v084_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v085_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v086_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v087_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v088_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v089_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v090_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v091_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v092_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v093_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v094_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v095_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v096_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v097_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v098_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v099_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v100_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v101_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v102_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v103_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v104_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v105_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v106_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v107_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v108_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v109_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v110_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v111_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v112_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v113_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v114_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v115_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v116_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v117_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v118_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v119_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v120_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v121_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v122_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v123_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v124_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v125_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v126_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v127_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v128_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v129_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v130_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v131_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v132_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v133_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v134_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v135_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v136_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v137_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v138_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v139_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v140_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v141_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v142_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v143_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v144_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r5_21d_jerk_v145_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(5)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r21_63d_jerk_v146_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r5_126d_jerk_v147_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(5)
    result=s.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d jerk of bsp_range_compression w=21d
def f04bsp_basing_pattern_jrk21r21_21d_jerk_v148_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 21)
    s=b.pct_change(21)
    result=s.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of bsp_range_compression w=63d
def f04bsp_basing_pattern_jrk63r5_63d_jerk_v149_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 63)
    s=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    result=s.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of bsp_range_compression w=126d
def f04bsp_basing_pattern_jrk126r21_126d_jerk_v150_signal(closeadj, high, low):
    b=_bsp_range_compression(high, low, 126)
    s=b.pct_change(21)
    result=s.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f04bsp_basing_pattern_jrk21r5_21d_jerk_v001_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v001_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v002_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v002_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v003_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v003_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v004_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v004_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v005_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v005_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v006_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v006_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v007_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v007_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v008_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v008_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v009_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v009_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v010_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v010_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v011_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v011_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v012_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v012_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v013_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v013_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v014_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v014_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v015_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v015_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v016_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v016_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v017_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v017_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v018_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v018_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v019_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v019_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v020_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v020_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v021_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v021_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v022_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v022_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v023_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v023_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v024_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v024_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v025_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v025_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v026_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v026_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v027_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v027_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v028_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v028_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v029_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v029_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v030_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v030_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v031_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v031_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v032_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v032_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v033_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v033_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v034_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v034_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v035_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v035_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v036_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v036_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v037_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v037_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v038_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v038_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v039_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v039_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v040_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v040_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v041_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v041_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v042_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v042_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v043_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v043_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v044_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v044_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v045_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v045_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v046_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v046_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v047_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v047_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v048_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v048_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v049_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v049_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v050_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v050_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v051_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v051_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v052_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v052_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v053_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v053_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v054_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v054_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v055_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v055_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v056_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v056_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v057_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v057_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v058_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v058_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v059_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v059_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v060_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v060_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v061_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v061_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v062_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v062_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v063_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v063_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v064_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v064_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v065_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v065_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v066_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v066_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v067_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v067_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v068_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v068_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v069_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v069_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v070_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v070_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v071_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v071_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v072_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v072_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v073_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v073_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v074_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v074_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v075_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v075_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v076_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v076_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v077_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v077_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v078_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v078_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v079_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v079_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v080_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v080_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v081_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v081_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v082_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v082_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v083_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v083_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v084_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v084_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v085_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v085_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v086_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v086_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v087_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v087_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v088_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v088_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v089_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v089_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v090_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v090_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v091_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v091_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v092_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v092_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v093_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v093_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v094_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v094_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v095_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v095_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v096_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v096_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v097_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v097_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v098_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v098_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v099_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v099_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v100_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v100_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v101_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v101_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v102_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v102_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v103_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v103_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v104_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v104_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v105_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v105_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v106_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v106_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v107_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v107_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v108_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v108_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v109_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v109_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v110_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v110_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v111_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v111_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v112_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v112_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v113_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v113_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v114_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v114_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v115_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v115_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v116_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v116_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v117_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v117_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v118_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v118_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v119_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v119_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v120_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v120_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v121_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v121_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v122_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v122_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v123_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v123_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v124_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v124_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v125_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v125_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v126_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v126_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v127_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v127_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v128_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v128_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v129_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v129_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v130_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v130_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v131_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v131_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v132_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v132_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v133_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v133_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v134_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v134_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v135_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v135_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v136_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v136_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v137_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v137_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v138_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v138_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v139_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v139_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v140_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v140_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v141_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v141_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v142_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v142_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v143_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v143_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v144_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v144_signal}, "f04bsp_basing_pattern_jrk21r5_21d_jerk_v145_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r5_21d_jerk_v145_signal}, "f04bsp_basing_pattern_jrk63r21_63d_jerk_v146_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r21_63d_jerk_v146_signal}, "f04bsp_basing_pattern_jrk126r5_126d_jerk_v147_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r5_126d_jerk_v147_signal}, "f04bsp_basing_pattern_jrk21r21_21d_jerk_v148_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk21r21_21d_jerk_v148_signal}, "f04bsp_basing_pattern_jrk63r5_63d_jerk_v149_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk63r5_63d_jerk_v149_signal}, "f04bsp_basing_pattern_jrk126r21_126d_jerk_v150_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_jrk126r21_126d_jerk_v150_signal}}
F04_BASING_PATTERN_REGISTRY_JERK = REGISTRY

if __name__ == "__main__":
    import inspect
    np.random.seed(42); n=800
    idx=pd.date_range("2010-01-01",periods=n,freq="B")
    closeadj=pd.Series(100*np.exp(np.random.normal(0,0.01,n).cumsum()),index=idx)
    close=closeadj*(1+np.random.normal(0,0.001,n))
    high=close*(1+np.abs(np.random.normal(0,0.005,n)))
    low=close*(1-np.abs(np.random.normal(0,0.005,n)))
    open_=close.shift(1).fillna(close.iloc[0])
    volume=pd.Series(np.random.lognormal(15,0.5,n),index=idx)
    revenue=pd.Series(np.abs(np.random.normal(1e9,2e8,n)),index=idx)
    netinc=revenue*np.random.uniform(0.05,0.2,n)
    fcf=netinc*np.random.uniform(0.8,1.2,n)
    ncfo=netinc*np.random.uniform(0.9,1.3,n)
    equity=pd.Series(np.abs(np.random.normal(5e9,1e9,n)),index=idx)
    debt=pd.Series(np.abs(np.random.normal(2e9,5e8,n)),index=idx)
    assets=equity+debt
    capex=pd.Series(np.abs(np.random.normal(1e8,2e7,n)),index=idx)
    sharesbas=pd.Series(np.abs(np.random.normal(1e8,1e7,n)),index=idx)
    gp=revenue*np.random.uniform(0.3,0.7,n)
    opinc=revenue*np.random.uniform(0.05,0.3,n)
    liabilities=debt*np.random.uniform(1.0,1.5,n)
    eps=netinc/sharesbas
    marketcap=equity*np.random.uniform(1.5,4.0,n)
    ev=marketcap+debt
    evebitda=ev/(revenue*0.15+1e-6)
    evebit=ev/(opinc+1e-6)
    pe=marketcap/(netinc+1e-6)
    pb=marketcap/(equity+1e-6)
    ps=marketcap/(revenue+1e-6)
    sf3a_shares=pd.Series(np.abs(np.random.normal(5e7,1e7,n)),index=idx)
    sf3a_value=sf3a_shares*closeadj
    sf3b_shares=pd.Series(np.abs(np.random.normal(3e7,5e6,n)),index=idx)
    sf3b_value=sf3b_shares*closeadj
    pool=dict(closeadj=closeadj,close=close,high=high,low=low,open_=open_,volume=volume,
              revenue=revenue,netinc=netinc,fcf=fcf,ncfo=ncfo,equity=equity,
              debt=debt,assets=assets,capex=capex,sharesbas=sharesbas,
              gp=gp,opinc=opinc,liabilities=liabilities,eps=eps,
              marketcap=marketcap,ev=ev,evebitda=evebitda,evebit=evebit,
              pe=pe,pb=pb,ps=ps,
              sf3a_shares=sf3a_shares,sf3a_value=sf3a_value,
              sf3b_shares=sf3b_shares,sf3b_value=sf3b_value)
    nan_heavy=0
    for name,meta in REGISTRY.items():
        fn=meta["func"]; args=[pool.get(c,closeadj) for c in meta["inputs"]]
        y1=fn(*args); y2=fn(*args)
        pd.testing.assert_series_equal(y1,y2,check_names=False)
        q=y1.iloc[504:].dropna()
        assert len(q)>0,f"{name}: empty"
        assert q.std()>0,f"{name}: constant"
        assert q.nunique()>10,f"{name}: few unique"
        if y1.iloc[504:].isna().mean()>=0.5: nan_heavy+=1
    assert nan_heavy/len(REGISTRY)<=0.20,f"NaN heavy: {nan_heavy}/{len(REGISTRY)}"
    print("SELF-TEST PASSED:",len(REGISTRY),"features")