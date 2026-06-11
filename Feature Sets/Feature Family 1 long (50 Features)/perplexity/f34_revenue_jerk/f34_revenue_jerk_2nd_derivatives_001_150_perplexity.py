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

def _rvj_growth(revenue, w):
    return revenue.pct_change(w)
def _rvj_jerk(revenue, w):
    g = _rvj_growth(revenue, w)
    return g.diff(w).diff(w)


# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v001_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v002_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v003_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v004_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v005_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v006_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v007_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v008_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v009_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v010_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v011_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v012_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v013_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v014_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v015_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v016_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v017_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v018_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v019_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v020_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v021_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v022_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v023_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v024_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v025_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v026_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v027_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v028_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v029_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v030_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v031_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v032_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v033_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v034_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v035_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v036_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v037_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v038_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v039_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v040_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v041_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v042_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v043_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v044_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v045_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v046_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v047_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v048_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v049_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v050_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v051_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v052_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v053_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v054_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v055_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v056_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v057_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v058_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v059_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v060_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v061_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v062_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v063_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v064_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v065_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v066_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v067_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v068_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v069_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v070_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v071_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v072_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v073_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v074_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v075_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v076_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v077_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v078_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v079_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v080_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v081_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v082_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v083_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v084_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v085_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v086_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v087_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v088_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v089_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v090_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v091_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v092_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v093_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v094_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v095_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v096_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v097_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v098_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v099_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v100_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v101_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v102_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v103_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v104_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v105_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v106_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v107_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v108_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v109_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v110_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v111_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v112_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v113_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v114_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v115_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v116_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v117_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v118_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v119_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v120_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v121_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v122_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v123_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v124_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v125_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v126_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v127_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v128_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v129_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v130_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v131_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v132_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v133_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v134_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v135_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v136_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v137_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v138_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v139_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v140_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v141_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v142_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v143_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v144_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v145_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v146_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v147_signal(revenue):
    b=_rvj_growth(revenue, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v148_signal(revenue):
    b=_rvj_growth(revenue, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of rvj_growth w=4d
def f34rvj_revenue_jerk_slp4r2_4d_slope_v149_signal(revenue):
    b=_rvj_growth(revenue, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of rvj_growth w=8d
def f34rvj_revenue_jerk_slp8r4_8d_slope_v150_signal(revenue):
    b=_rvj_growth(revenue, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f34rvj_revenue_jerk_slp4r2_4d_slope_v001_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v001_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v002_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v002_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v003_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v003_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v004_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v004_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v005_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v005_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v006_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v006_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v007_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v007_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v008_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v008_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v009_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v009_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v010_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v010_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v011_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v011_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v012_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v012_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v013_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v013_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v014_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v014_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v015_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v015_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v016_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v016_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v017_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v017_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v018_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v018_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v019_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v019_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v020_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v020_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v021_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v021_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v022_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v022_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v023_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v023_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v024_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v024_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v025_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v025_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v026_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v026_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v027_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v027_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v028_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v028_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v029_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v029_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v030_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v030_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v031_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v031_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v032_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v032_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v033_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v033_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v034_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v034_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v035_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v035_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v036_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v036_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v037_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v037_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v038_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v038_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v039_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v039_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v040_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v040_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v041_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v041_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v042_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v042_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v043_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v043_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v044_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v044_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v045_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v045_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v046_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v046_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v047_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v047_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v048_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v048_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v049_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v049_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v050_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v050_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v051_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v051_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v052_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v052_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v053_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v053_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v054_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v054_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v055_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v055_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v056_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v056_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v057_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v057_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v058_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v058_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v059_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v059_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v060_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v060_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v061_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v061_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v062_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v062_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v063_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v063_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v064_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v064_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v065_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v065_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v066_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v066_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v067_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v067_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v068_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v068_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v069_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v069_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v070_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v070_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v071_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v071_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v072_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v072_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v073_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v073_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v074_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v074_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v075_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v075_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v076_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v076_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v077_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v077_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v078_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v078_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v079_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v079_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v080_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v080_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v081_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v081_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v082_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v082_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v083_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v083_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v084_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v084_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v085_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v085_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v086_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v086_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v087_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v087_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v088_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v088_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v089_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v089_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v090_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v090_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v091_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v091_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v092_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v092_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v093_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v093_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v094_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v094_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v095_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v095_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v096_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v096_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v097_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v097_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v098_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v098_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v099_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v099_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v100_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v100_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v101_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v101_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v102_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v102_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v103_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v103_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v104_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v104_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v105_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v105_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v106_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v106_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v107_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v107_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v108_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v108_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v109_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v109_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v110_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v110_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v111_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v111_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v112_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v112_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v113_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v113_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v114_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v114_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v115_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v115_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v116_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v116_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v117_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v117_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v118_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v118_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v119_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v119_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v120_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v120_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v121_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v121_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v122_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v122_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v123_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v123_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v124_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v124_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v125_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v125_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v126_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v126_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v127_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v127_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v128_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v128_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v129_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v129_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v130_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v130_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v131_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v131_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v132_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v132_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v133_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v133_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v134_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v134_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v135_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v135_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v136_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v136_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v137_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v137_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v138_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v138_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v139_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v139_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v140_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v140_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v141_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v141_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v142_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v142_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v143_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v143_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v144_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v144_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v145_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v145_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v146_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v146_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v147_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v147_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v148_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v148_signal}, "f34rvj_revenue_jerk_slp4r2_4d_slope_v149_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp4r2_4d_slope_v149_signal}, "f34rvj_revenue_jerk_slp8r4_8d_slope_v150_signal": {"inputs": ['revenue'], "func": f34rvj_revenue_jerk_slp8r4_8d_slope_v150_signal}}
F34_REVENUE_JERK_REGISTRY_SLOPE = REGISTRY

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