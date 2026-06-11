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

def _sds_share_chg(sharesbas, w):
    return sharesbas.pct_change(w)
def _sds_dil_zscore(sharesbas, w):
    return _z(_sds_share_chg(sharesbas, w), w)


# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v001_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v002_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v003_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v004_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v005_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v006_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v007_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v008_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v009_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v010_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v011_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v012_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v013_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v014_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v015_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v016_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v017_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v018_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v019_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v020_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v021_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v022_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v023_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v024_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v025_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v026_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v027_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v028_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v029_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v030_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v031_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v032_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v033_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v034_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v035_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v036_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v037_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v038_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v039_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v040_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v041_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v042_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v043_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v044_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v045_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v046_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v047_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v048_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v049_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v050_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v051_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v052_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v053_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v054_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v055_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v056_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v057_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v058_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v059_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v060_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v061_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v062_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v063_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v064_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v065_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v066_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v067_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v068_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v069_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v070_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v071_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v072_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v073_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v074_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v075_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v076_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v077_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v078_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v079_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v080_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v081_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v082_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v083_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v084_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v085_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v086_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v087_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v088_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v089_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v090_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v091_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v092_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v093_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v094_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v095_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v096_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v097_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v098_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v099_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v100_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v101_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v102_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v103_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v104_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v105_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v106_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v107_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v108_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v109_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v110_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v111_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v112_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v113_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v114_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v115_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v116_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v117_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v118_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v119_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v120_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v121_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v122_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v123_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v124_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v125_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v126_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v127_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v128_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v129_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v130_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v131_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v132_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v133_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v134_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v135_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v136_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v137_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v138_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v139_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v140_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v141_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v142_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v143_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v144_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v145_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v146_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v147_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of sds_share_chg w=4d
def f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v148_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 4)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of sds_share_chg w=8d
def f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v149_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 8)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of sds_share_chg w=12d
def f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v150_signal(sharesbas):
    b=_sds_share_chg(sharesbas, 12)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v001_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v001_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v002_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v002_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v003_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v003_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v004_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v004_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v005_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v005_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v006_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v006_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v007_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v007_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v008_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v008_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v009_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v009_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v010_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v010_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v011_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v011_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v012_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v012_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v013_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v013_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v014_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v014_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v015_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v015_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v016_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v016_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v017_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v017_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v018_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v018_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v019_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v019_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v020_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v020_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v021_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v021_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v022_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v022_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v023_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v023_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v024_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v024_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v025_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v025_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v026_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v026_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v027_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v027_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v028_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v028_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v029_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v029_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v030_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v030_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v031_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v031_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v032_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v032_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v033_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v033_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v034_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v034_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v035_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v035_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v036_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v036_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v037_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v037_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v038_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v038_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v039_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v039_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v040_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v040_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v041_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v041_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v042_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v042_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v043_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v043_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v044_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v044_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v045_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v045_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v046_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v046_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v047_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v047_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v048_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v048_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v049_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v049_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v050_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v050_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v051_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v051_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v052_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v052_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v053_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v053_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v054_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v054_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v055_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v055_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v056_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v056_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v057_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v057_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v058_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v058_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v059_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v059_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v060_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v060_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v061_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v061_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v062_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v062_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v063_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v063_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v064_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v064_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v065_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v065_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v066_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v066_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v067_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v067_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v068_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v068_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v069_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v069_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v070_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v070_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v071_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v071_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v072_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v072_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v073_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v073_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v074_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v074_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v075_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v075_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v076_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v076_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v077_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v077_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v078_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v078_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v079_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v079_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v080_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v080_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v081_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v081_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v082_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v082_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v083_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v083_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v084_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v084_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v085_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v085_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v086_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v086_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v087_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v087_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v088_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v088_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v089_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v089_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v090_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v090_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v091_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v091_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v092_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v092_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v093_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v093_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v094_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v094_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v095_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v095_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v096_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v096_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v097_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v097_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v098_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v098_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v099_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v099_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v100_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v100_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v101_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v101_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v102_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v102_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v103_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v103_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v104_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v104_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v105_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v105_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v106_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v106_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v107_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v107_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v108_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v108_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v109_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v109_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v110_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v110_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v111_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v111_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v112_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v112_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v113_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v113_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v114_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v114_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v115_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v115_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v116_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v116_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v117_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v117_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v118_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v118_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v119_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v119_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v120_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v120_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v121_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v121_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v122_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v122_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v123_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v123_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v124_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v124_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v125_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v125_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v126_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v126_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v127_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v127_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v128_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v128_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v129_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v129_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v130_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v130_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v131_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v131_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v132_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v132_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v133_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v133_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v134_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v134_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v135_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v135_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v136_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v136_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v137_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v137_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v138_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v138_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v139_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v139_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v140_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v140_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v141_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v141_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v142_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v142_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v143_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v143_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v144_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v144_signal}, "f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v145_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r2_4d_slope_v145_signal}, "f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v146_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r4_8d_slope_v146_signal}, "f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v147_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r2_12d_slope_v147_signal}, "f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v148_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp4r4_4d_slope_v148_signal}, "f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v149_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp8r2_8d_slope_v149_signal}, "f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v150_signal": {"inputs": ['sharesbas'], "func": f19sds_share_and_dilution_snapshot_slp12r4_12d_slope_v150_signal}}
F19_SHARE_AND_DILUTION_SNAPSHOT_REGISTRY_SLOPE = REGISTRY

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