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

def _bds_liab_ratio(liabilities, assets):
    return _safe_div(liabilities, assets.abs())
def _bds_spiral_z(liabilities, assets, w):
    return _z(_bds_liab_ratio(liabilities, assets), w)


# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v001_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v002_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v003_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v004_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v005_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v006_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v007_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v008_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v009_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v010_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v011_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v012_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v013_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v014_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v015_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v016_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v017_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v018_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v019_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v020_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v021_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v022_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v023_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v024_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v025_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v026_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v027_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v028_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v029_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v030_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v031_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v032_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v033_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v034_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v035_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v036_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v037_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v038_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v039_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v040_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v041_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v042_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v043_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v044_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v045_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v046_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v047_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v048_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v049_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v050_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v051_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v052_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v053_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v054_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v055_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v056_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v057_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v058_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v059_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v060_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v061_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v062_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v063_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v064_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v065_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v066_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v067_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v068_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v069_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v070_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v071_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v072_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v073_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v074_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v075_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v076_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v077_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v078_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v079_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v080_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v081_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v082_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v083_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v084_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v085_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v086_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v087_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v088_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v089_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v090_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v091_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v092_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v093_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v094_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v095_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v096_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v097_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v098_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v099_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v100_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v101_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v102_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v103_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v104_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v105_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v106_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v107_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v108_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v109_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v110_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v111_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v112_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v113_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v114_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v115_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v116_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v117_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v118_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v119_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v120_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v121_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v122_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v123_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v124_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v125_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v126_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v127_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v128_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v129_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v130_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v131_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v132_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v133_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v134_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v135_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v136_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v137_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v138_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v139_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v140_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v141_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v142_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v143_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v144_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v145_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v146_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v147_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of bds_liab_ratio w=4d
def f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v148_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of bds_liab_ratio w=8d
def f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v149_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of bds_liab_ratio w=12d
def f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v150_signal(liabilities, assets):
    b=_bds_liab_ratio(liabilities, assets)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v001_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v001_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v002_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v002_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v003_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v003_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v004_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v004_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v005_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v005_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v006_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v006_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v007_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v007_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v008_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v008_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v009_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v009_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v010_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v010_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v011_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v011_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v012_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v012_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v013_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v013_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v014_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v014_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v015_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v015_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v016_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v016_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v017_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v017_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v018_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v018_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v019_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v019_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v020_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v020_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v021_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v021_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v022_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v022_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v023_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v023_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v024_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v024_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v025_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v025_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v026_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v026_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v027_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v027_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v028_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v028_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v029_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v029_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v030_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v030_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v031_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v031_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v032_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v032_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v033_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v033_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v034_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v034_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v035_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v035_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v036_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v036_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v037_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v037_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v038_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v038_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v039_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v039_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v040_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v040_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v041_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v041_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v042_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v042_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v043_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v043_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v044_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v044_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v045_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v045_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v046_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v046_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v047_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v047_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v048_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v048_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v049_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v049_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v050_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v050_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v051_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v051_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v052_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v052_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v053_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v053_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v054_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v054_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v055_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v055_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v056_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v056_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v057_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v057_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v058_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v058_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v059_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v059_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v060_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v060_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v061_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v061_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v062_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v062_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v063_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v063_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v064_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v064_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v065_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v065_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v066_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v066_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v067_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v067_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v068_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v068_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v069_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v069_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v070_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v070_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v071_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v071_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v072_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v072_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v073_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v073_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v074_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v074_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v075_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v075_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v076_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v076_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v077_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v077_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v078_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v078_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v079_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v079_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v080_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v080_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v081_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v081_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v082_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v082_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v083_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v083_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v084_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v084_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v085_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v085_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v086_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v086_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v087_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v087_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v088_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v088_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v089_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v089_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v090_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v090_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v091_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v091_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v092_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v092_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v093_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v093_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v094_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v094_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v095_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v095_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v096_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v096_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v097_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v097_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v098_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v098_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v099_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v099_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v100_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v100_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v101_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v101_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v102_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v102_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v103_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v103_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v104_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v104_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v105_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v105_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v106_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v106_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v107_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v107_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v108_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v108_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v109_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v109_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v110_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v110_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v111_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v111_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v112_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v112_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v113_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v113_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v114_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v114_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v115_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v115_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v116_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v116_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v117_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v117_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v118_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v118_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v119_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v119_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v120_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v120_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v121_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v121_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v122_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v122_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v123_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v123_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v124_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v124_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v125_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v125_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v126_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v126_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v127_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v127_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v128_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v128_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v129_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v129_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v130_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v130_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v131_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v131_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v132_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v132_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v133_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v133_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v134_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v134_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v135_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v135_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v136_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v136_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v137_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v137_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v138_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v138_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v139_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v139_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v140_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v140_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v141_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v141_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v142_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v142_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v143_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v143_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v144_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v144_signal}, "f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v145_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r2_4d_slope_v145_signal}, "f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v146_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r4_8d_slope_v146_signal}, "f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v147_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r2_12d_slope_v147_signal}, "f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v148_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp4r4_4d_slope_v148_signal}, "f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v149_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp8r2_8d_slope_v149_signal}, "f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v150_signal": {"inputs": ['liabilities', 'assets'], "func": f49bds_balance_sheet_death_spiral_slp12r4_12d_slope_v150_signal}}
F49_BALANCE_SHEET_DEATH_SPIRAL_REGISTRY_SLOPE = REGISTRY

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