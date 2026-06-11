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

def _vac_vol_surge(volume, w):
    return volume / volume.rolling(w, min_periods=max(1, w//2)).mean().replace(0, np.nan)
def _vac_dolvol_surge(closeadj, volume, w):
    dv = closeadj * volume
    return dv / dv.rolling(w, min_periods=max(1, w//2)).mean().replace(0, np.nan)


# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v001_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v002_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v003_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v004_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v005_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v006_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v007_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v008_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v009_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v010_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v011_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v012_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v013_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v014_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v015_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v016_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v017_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v018_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v019_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v020_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v021_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v022_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v023_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v024_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v025_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v026_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v027_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v028_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v029_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v030_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v031_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v032_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v033_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v034_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v035_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v036_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v037_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v038_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v039_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v040_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v041_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v042_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v043_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v044_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v045_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v046_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v047_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v048_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v049_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v050_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v051_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v052_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v053_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v054_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v055_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v056_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v057_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v058_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v059_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v060_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v061_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v062_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v063_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v064_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v065_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v066_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v067_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v068_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v069_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v070_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v071_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v072_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v073_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v074_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v075_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v076_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v077_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v078_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v079_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v080_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v081_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v082_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v083_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v084_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v085_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v086_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v087_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v088_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v089_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v090_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v091_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v092_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v093_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v094_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v095_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v096_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v097_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v098_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v099_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v100_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v101_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v102_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v103_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v104_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v105_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v106_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v107_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v108_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v109_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v110_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v111_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v112_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v113_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v114_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v115_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v116_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v117_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v118_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v119_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v120_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v121_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v122_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v123_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v124_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v125_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v126_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v127_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v128_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v129_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v130_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v131_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v132_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v133_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v134_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v135_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v136_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v137_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v138_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v139_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v140_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v141_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v142_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v143_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v144_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r5_5d_slope_v145_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r21_21d_slope_v146_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(21)/b.shift(21).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 5d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r5_63d_slope_v147_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(5)
    result=_z(s,max(5*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pct_change slope of vac_vol_surge w=5d
def f05vac_volume_at_capitulation_slp5r21_5d_slope_v148_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 5)
    result=b.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff slope of vac_vol_surge w=21d
def f05vac_volume_at_capitulation_slp21r5_21d_slope_v149_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 21)
    result=b.diff(5)/b.shift(5).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 21d slope of vac_vol_surge w=63d
def f05vac_volume_at_capitulation_slp63r21_63d_slope_v150_signal(closeadj, volume):
    b=_vac_vol_surge(volume, 63)
    s=b.pct_change(21)
    result=_z(s,max(21*2,63))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f05vac_volume_at_capitulation_slp5r5_5d_slope_v001_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v001_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v002_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v002_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v003_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v003_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v004_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v004_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v005_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v005_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v006_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v006_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v007_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v007_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v008_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v008_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v009_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v009_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v010_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v010_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v011_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v011_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v012_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v012_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v013_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v013_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v014_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v014_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v015_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v015_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v016_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v016_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v017_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v017_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v018_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v018_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v019_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v019_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v020_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v020_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v021_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v021_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v022_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v022_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v023_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v023_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v024_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v024_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v025_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v025_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v026_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v026_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v027_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v027_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v028_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v028_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v029_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v029_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v030_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v030_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v031_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v031_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v032_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v032_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v033_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v033_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v034_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v034_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v035_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v035_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v036_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v036_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v037_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v037_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v038_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v038_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v039_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v039_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v040_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v040_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v041_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v041_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v042_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v042_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v043_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v043_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v044_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v044_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v045_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v045_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v046_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v046_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v047_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v047_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v048_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v048_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v049_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v049_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v050_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v050_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v051_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v051_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v052_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v052_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v053_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v053_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v054_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v054_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v055_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v055_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v056_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v056_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v057_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v057_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v058_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v058_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v059_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v059_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v060_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v060_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v061_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v061_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v062_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v062_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v063_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v063_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v064_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v064_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v065_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v065_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v066_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v066_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v067_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v067_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v068_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v068_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v069_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v069_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v070_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v070_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v071_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v071_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v072_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v072_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v073_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v073_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v074_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v074_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v075_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v075_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v076_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v076_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v077_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v077_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v078_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v078_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v079_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v079_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v080_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v080_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v081_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v081_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v082_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v082_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v083_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v083_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v084_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v084_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v085_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v085_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v086_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v086_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v087_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v087_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v088_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v088_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v089_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v089_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v090_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v090_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v091_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v091_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v092_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v092_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v093_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v093_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v094_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v094_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v095_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v095_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v096_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v096_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v097_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v097_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v098_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v098_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v099_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v099_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v100_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v100_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v101_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v101_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v102_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v102_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v103_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v103_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v104_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v104_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v105_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v105_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v106_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v106_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v107_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v107_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v108_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v108_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v109_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v109_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v110_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v110_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v111_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v111_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v112_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v112_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v113_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v113_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v114_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v114_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v115_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v115_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v116_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v116_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v117_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v117_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v118_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v118_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v119_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v119_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v120_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v120_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v121_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v121_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v122_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v122_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v123_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v123_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v124_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v124_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v125_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v125_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v126_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v126_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v127_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v127_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v128_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v128_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v129_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v129_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v130_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v130_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v131_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v131_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v132_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v132_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v133_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v133_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v134_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v134_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v135_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v135_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v136_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v136_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v137_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v137_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v138_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v138_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v139_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v139_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v140_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v140_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v141_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v141_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v142_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v142_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v143_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v143_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v144_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v144_signal}, "f05vac_volume_at_capitulation_slp5r5_5d_slope_v145_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r5_5d_slope_v145_signal}, "f05vac_volume_at_capitulation_slp21r21_21d_slope_v146_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r21_21d_slope_v146_signal}, "f05vac_volume_at_capitulation_slp63r5_63d_slope_v147_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r5_63d_slope_v147_signal}, "f05vac_volume_at_capitulation_slp5r21_5d_slope_v148_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp5r21_5d_slope_v148_signal}, "f05vac_volume_at_capitulation_slp21r5_21d_slope_v149_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp21r5_21d_slope_v149_signal}, "f05vac_volume_at_capitulation_slp63r21_63d_slope_v150_signal": {"inputs": ['closeadj', 'volume'], "func": f05vac_volume_at_capitulation_slp63r21_63d_slope_v150_signal}}
F05_VOLUME_AT_CAPITULATION_REGISTRY_SLOPE = REGISTRY

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