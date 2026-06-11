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

def _dbt_debt_chg(debt, w):
    return debt.pct_change(w)
def _dbt_debt_z(debt, w):
    return _z(_dbt_debt_chg(debt, w), w)


# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v001_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v002_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v003_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v004_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v005_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v006_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v007_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v008_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v009_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v010_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v011_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v012_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v013_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v014_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v015_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v016_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v017_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v018_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v019_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v020_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v021_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v022_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v023_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v024_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v025_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v026_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v027_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v028_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v029_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v030_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v031_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v032_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v033_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v034_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v035_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v036_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v037_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v038_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v039_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v040_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v041_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v042_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v043_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v044_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v045_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v046_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v047_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v048_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v049_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v050_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v051_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v052_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v053_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v054_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v055_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v056_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v057_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v058_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v059_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v060_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v061_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v062_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v063_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v064_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v065_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v066_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v067_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v068_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v069_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v070_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v071_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v072_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v073_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v074_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v075_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v076_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v077_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v078_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v079_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v080_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v081_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v082_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v083_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v084_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v085_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v086_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v087_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v088_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v089_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v090_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v091_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v092_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v093_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v094_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v095_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v096_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v097_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v098_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v099_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v100_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v101_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v102_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v103_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v104_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v105_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v106_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v107_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v108_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v109_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v110_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v111_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v112_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v113_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v114_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v115_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v116_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v117_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v118_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v119_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v120_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v121_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v122_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v123_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v124_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v125_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v126_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v127_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v128_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v129_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v130_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v131_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v132_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v133_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v134_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v135_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v136_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v137_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v138_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v139_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v140_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v141_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v142_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v143_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v144_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v145_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v146_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v147_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v148_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of dbt_debt_chg w=4d
def f24dbt_debt_trajectory_slp4r2_4d_slope_v149_signal(debt):
    b=_dbt_debt_chg(debt, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of dbt_debt_chg w=8d
def f24dbt_debt_trajectory_slp8r4_8d_slope_v150_signal(debt):
    b=_dbt_debt_chg(debt, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f24dbt_debt_trajectory_slp4r2_4d_slope_v001_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v001_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v002_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v002_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v003_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v003_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v004_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v004_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v005_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v005_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v006_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v006_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v007_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v007_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v008_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v008_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v009_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v009_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v010_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v010_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v011_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v011_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v012_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v012_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v013_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v013_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v014_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v014_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v015_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v015_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v016_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v016_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v017_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v017_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v018_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v018_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v019_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v019_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v020_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v020_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v021_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v021_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v022_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v022_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v023_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v023_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v024_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v024_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v025_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v025_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v026_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v026_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v027_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v027_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v028_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v028_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v029_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v029_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v030_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v030_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v031_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v031_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v032_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v032_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v033_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v033_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v034_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v034_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v035_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v035_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v036_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v036_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v037_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v037_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v038_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v038_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v039_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v039_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v040_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v040_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v041_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v041_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v042_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v042_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v043_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v043_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v044_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v044_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v045_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v045_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v046_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v046_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v047_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v047_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v048_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v048_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v049_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v049_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v050_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v050_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v051_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v051_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v052_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v052_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v053_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v053_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v054_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v054_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v055_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v055_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v056_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v056_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v057_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v057_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v058_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v058_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v059_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v059_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v060_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v060_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v061_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v061_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v062_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v062_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v063_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v063_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v064_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v064_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v065_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v065_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v066_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v066_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v067_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v067_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v068_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v068_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v069_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v069_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v070_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v070_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v071_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v071_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v072_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v072_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v073_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v073_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v074_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v074_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v075_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v075_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v076_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v076_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v077_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v077_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v078_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v078_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v079_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v079_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v080_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v080_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v081_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v081_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v082_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v082_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v083_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v083_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v084_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v084_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v085_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v085_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v086_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v086_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v087_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v087_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v088_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v088_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v089_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v089_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v090_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v090_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v091_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v091_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v092_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v092_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v093_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v093_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v094_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v094_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v095_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v095_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v096_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v096_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v097_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v097_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v098_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v098_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v099_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v099_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v100_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v100_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v101_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v101_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v102_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v102_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v103_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v103_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v104_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v104_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v105_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v105_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v106_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v106_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v107_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v107_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v108_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v108_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v109_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v109_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v110_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v110_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v111_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v111_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v112_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v112_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v113_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v113_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v114_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v114_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v115_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v115_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v116_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v116_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v117_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v117_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v118_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v118_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v119_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v119_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v120_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v120_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v121_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v121_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v122_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v122_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v123_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v123_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v124_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v124_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v125_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v125_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v126_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v126_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v127_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v127_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v128_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v128_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v129_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v129_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v130_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v130_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v131_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v131_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v132_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v132_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v133_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v133_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v134_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v134_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v135_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v135_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v136_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v136_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v137_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v137_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v138_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v138_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v139_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v139_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v140_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v140_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v141_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v141_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v142_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v142_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v143_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v143_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v144_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v144_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v145_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v145_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v146_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v146_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v147_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v147_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v148_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v148_signal}, "f24dbt_debt_trajectory_slp4r2_4d_slope_v149_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp4r2_4d_slope_v149_signal}, "f24dbt_debt_trajectory_slp8r4_8d_slope_v150_signal": {"inputs": ['debt'], "func": f24dbt_debt_trajectory_slp8r4_8d_slope_v150_signal}}
F24_DEBT_TRAJECTORY_REGISTRY_SLOPE = REGISTRY

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