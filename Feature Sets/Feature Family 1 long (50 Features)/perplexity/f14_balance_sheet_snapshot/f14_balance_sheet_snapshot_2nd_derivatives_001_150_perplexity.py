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

def _bss_equity_ratio(equity, assets):
    return _safe_div(equity, assets.abs())
def _bss_equity_zscore(equity, assets, w):
    return _z(_bss_equity_ratio(equity, assets), w)


# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v001_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v002_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v003_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v004_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v005_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v006_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v007_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v008_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v009_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v010_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v011_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v012_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v013_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v014_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v015_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v016_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v017_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v018_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v019_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v020_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v021_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v022_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v023_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v024_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v025_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v026_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v027_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v028_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v029_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v030_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v031_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v032_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v033_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v034_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v035_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v036_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v037_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v038_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v039_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v040_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v041_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v042_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v043_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v044_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v045_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v046_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v047_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v048_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v049_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v050_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v051_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v052_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v053_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v054_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v055_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v056_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v057_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v058_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v059_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v060_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v061_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v062_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v063_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v064_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v065_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v066_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v067_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v068_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v069_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v070_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v071_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v072_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v073_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v074_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v075_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v076_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v077_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v078_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v079_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v080_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v081_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v082_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v083_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v084_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v085_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v086_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v087_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v088_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v089_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v090_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v091_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v092_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v093_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v094_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v095_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v096_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v097_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v098_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v099_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v100_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v101_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v102_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v103_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v104_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v105_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v106_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v107_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v108_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v109_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v110_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v111_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v112_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v113_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v114_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v115_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v116_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v117_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v118_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v119_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v120_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v121_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v122_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v123_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v124_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v125_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v126_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v127_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v128_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v129_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v130_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v131_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v132_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v133_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v134_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v135_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v136_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v137_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v138_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v139_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v140_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v141_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v142_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v143_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v144_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v145_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v146_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v147_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bss_equity_ratio w=4d
def f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v148_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bss_equity_ratio w=8d
def f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v149_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bss_equity_ratio w=12d
def f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v150_signal(equity, assets):
    b=_bss_equity_ratio(equity, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v001_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v001_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v002_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v002_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v003_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v003_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v004_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v004_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v005_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v005_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v006_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v006_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v007_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v007_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v008_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v008_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v009_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v009_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v010_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v010_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v011_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v011_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v012_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v012_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v013_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v013_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v014_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v014_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v015_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v015_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v016_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v016_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v017_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v017_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v018_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v018_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v019_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v019_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v020_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v020_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v021_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v021_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v022_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v022_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v023_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v023_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v024_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v024_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v025_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v025_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v026_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v026_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v027_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v027_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v028_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v028_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v029_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v029_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v030_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v030_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v031_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v031_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v032_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v032_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v033_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v033_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v034_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v034_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v035_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v035_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v036_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v036_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v037_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v037_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v038_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v038_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v039_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v039_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v040_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v040_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v041_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v041_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v042_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v042_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v043_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v043_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v044_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v044_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v045_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v045_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v046_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v046_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v047_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v047_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v048_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v048_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v049_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v049_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v050_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v050_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v051_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v051_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v052_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v052_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v053_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v053_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v054_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v054_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v055_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v055_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v056_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v056_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v057_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v057_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v058_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v058_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v059_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v059_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v060_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v060_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v061_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v061_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v062_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v062_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v063_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v063_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v064_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v064_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v065_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v065_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v066_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v066_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v067_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v067_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v068_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v068_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v069_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v069_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v070_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v070_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v071_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v071_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v072_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v072_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v073_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v073_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v074_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v074_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v075_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v075_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v076_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v076_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v077_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v077_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v078_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v078_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v079_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v079_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v080_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v080_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v081_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v081_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v082_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v082_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v083_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v083_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v084_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v084_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v085_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v085_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v086_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v086_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v087_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v087_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v088_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v088_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v089_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v089_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v090_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v090_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v091_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v091_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v092_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v092_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v093_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v093_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v094_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v094_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v095_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v095_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v096_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v096_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v097_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v097_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v098_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v098_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v099_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v099_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v100_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v100_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v101_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v101_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v102_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v102_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v103_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v103_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v104_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v104_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v105_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v105_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v106_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v106_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v107_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v107_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v108_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v108_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v109_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v109_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v110_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v110_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v111_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v111_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v112_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v112_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v113_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v113_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v114_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v114_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v115_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v115_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v116_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v116_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v117_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v117_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v118_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v118_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v119_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v119_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v120_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v120_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v121_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v121_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v122_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v122_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v123_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v123_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v124_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v124_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v125_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v125_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v126_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v126_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v127_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v127_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v128_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v128_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v129_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v129_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v130_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v130_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v131_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v131_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v132_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v132_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v133_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v133_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v134_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v134_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v135_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v135_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v136_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v136_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v137_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v137_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v138_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v138_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v139_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v139_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v140_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v140_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v141_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v141_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v142_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v142_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v143_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v143_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v144_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v144_signal}, "f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v145_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r2_4d_slope_v145_signal}, "f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v146_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r4_8d_slope_v146_signal}, "f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v147_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r2_12d_slope_v147_signal}, "f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v148_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp4r4_4d_slope_v148_signal}, "f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v149_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp8r2_8d_slope_v149_signal}, "f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v150_signal": {"inputs": ['equity', 'assets'], "func": f14bss_balance_sheet_snapshot_slp12r4_12d_slope_v150_signal}}
F14_BALANCE_SHEET_SNAPSHOT_REGISTRY_SLOPE = REGISTRY

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