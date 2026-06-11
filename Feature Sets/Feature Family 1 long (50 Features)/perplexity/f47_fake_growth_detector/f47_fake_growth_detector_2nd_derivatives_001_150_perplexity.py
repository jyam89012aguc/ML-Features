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

def _fgd_asset_bloat(assets, revenue):
    return _safe_div(assets, revenue.abs())
def _fgd_bloat_z(assets, revenue, w):
    return _z(_fgd_asset_bloat(assets, revenue), w)


# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v001_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v002_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v003_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v004_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v005_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v006_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v007_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v008_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v009_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v010_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v011_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v012_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v013_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v014_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v015_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v016_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v017_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v018_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v019_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v020_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v021_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v022_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v023_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v024_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v025_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v026_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v027_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v028_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v029_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v030_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v031_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v032_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v033_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v034_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v035_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v036_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v037_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v038_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v039_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v040_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v041_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v042_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v043_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v044_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v045_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v046_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v047_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v048_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v049_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v050_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v051_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v052_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v053_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v054_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v055_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v056_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v057_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v058_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v059_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v060_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v061_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v062_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v063_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v064_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v065_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v066_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v067_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v068_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v069_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v070_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v071_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v072_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v073_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v074_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v075_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v076_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v077_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v078_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v079_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v080_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v081_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v082_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v083_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v084_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v085_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v086_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v087_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v088_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v089_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v090_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v091_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v092_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v093_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v094_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v095_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v096_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v097_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v098_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v099_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v100_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v101_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v102_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v103_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v104_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v105_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v106_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v107_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v108_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v109_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v110_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v111_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v112_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v113_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v114_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v115_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v116_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v117_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v118_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v119_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v120_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v121_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v122_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v123_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v124_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v125_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v126_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v127_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v128_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v129_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v130_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v131_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v132_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v133_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v134_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v135_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v136_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v137_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v138_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v139_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v140_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v141_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v142_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v143_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v144_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v145_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v146_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v147_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v148_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of fgd_asset_bloat w=4d
def f47fgd_fake_growth_detector_slp4r2_4d_slope_v149_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of fgd_asset_bloat w=8d
def f47fgd_fake_growth_detector_slp8r4_8d_slope_v150_signal(assets, revenue):
    b=_fgd_asset_bloat(assets, revenue)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f47fgd_fake_growth_detector_slp4r2_4d_slope_v001_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v001_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v002_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v002_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v003_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v003_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v004_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v004_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v005_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v005_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v006_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v006_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v007_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v007_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v008_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v008_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v009_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v009_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v010_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v010_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v011_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v011_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v012_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v012_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v013_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v013_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v014_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v014_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v015_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v015_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v016_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v016_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v017_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v017_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v018_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v018_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v019_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v019_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v020_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v020_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v021_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v021_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v022_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v022_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v023_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v023_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v024_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v024_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v025_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v025_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v026_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v026_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v027_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v027_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v028_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v028_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v029_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v029_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v030_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v030_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v031_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v031_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v032_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v032_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v033_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v033_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v034_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v034_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v035_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v035_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v036_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v036_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v037_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v037_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v038_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v038_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v039_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v039_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v040_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v040_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v041_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v041_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v042_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v042_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v043_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v043_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v044_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v044_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v045_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v045_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v046_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v046_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v047_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v047_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v048_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v048_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v049_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v049_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v050_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v050_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v051_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v051_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v052_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v052_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v053_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v053_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v054_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v054_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v055_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v055_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v056_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v056_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v057_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v057_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v058_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v058_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v059_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v059_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v060_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v060_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v061_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v061_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v062_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v062_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v063_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v063_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v064_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v064_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v065_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v065_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v066_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v066_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v067_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v067_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v068_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v068_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v069_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v069_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v070_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v070_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v071_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v071_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v072_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v072_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v073_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v073_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v074_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v074_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v075_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v075_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v076_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v076_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v077_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v077_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v078_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v078_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v079_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v079_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v080_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v080_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v081_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v081_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v082_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v082_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v083_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v083_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v084_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v084_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v085_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v085_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v086_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v086_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v087_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v087_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v088_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v088_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v089_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v089_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v090_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v090_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v091_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v091_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v092_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v092_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v093_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v093_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v094_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v094_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v095_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v095_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v096_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v096_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v097_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v097_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v098_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v098_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v099_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v099_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v100_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v100_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v101_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v101_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v102_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v102_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v103_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v103_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v104_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v104_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v105_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v105_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v106_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v106_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v107_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v107_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v108_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v108_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v109_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v109_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v110_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v110_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v111_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v111_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v112_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v112_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v113_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v113_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v114_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v114_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v115_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v115_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v116_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v116_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v117_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v117_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v118_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v118_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v119_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v119_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v120_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v120_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v121_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v121_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v122_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v122_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v123_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v123_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v124_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v124_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v125_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v125_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v126_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v126_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v127_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v127_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v128_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v128_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v129_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v129_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v130_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v130_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v131_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v131_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v132_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v132_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v133_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v133_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v134_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v134_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v135_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v135_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v136_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v136_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v137_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v137_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v138_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v138_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v139_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v139_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v140_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v140_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v141_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v141_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v142_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v142_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v143_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v143_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v144_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v144_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v145_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v145_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v146_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v146_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v147_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v147_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v148_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v148_signal}, "f47fgd_fake_growth_detector_slp4r2_4d_slope_v149_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp4r2_4d_slope_v149_signal}, "f47fgd_fake_growth_detector_slp8r4_8d_slope_v150_signal": {"inputs": ['assets', 'revenue'], "func": f47fgd_fake_growth_detector_slp8r4_8d_slope_v150_signal}}
F47_FAKE_GROWTH_DETECTOR_REGISTRY_SLOPE = REGISTRY

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