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

def _nge_inst_share_chg(sf3a_shares, w):
    return sf3a_shares.pct_change(w)
def _nge_inst_z(sf3a_shares, w):
    return _z(_nge_inst_share_chg(sf3a_shares, w), w)


# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v001_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v002_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v003_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v004_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v005_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v006_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v007_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v008_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v009_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v010_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v011_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v012_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v013_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v014_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v015_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v016_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v017_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v018_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v019_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v020_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v021_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v022_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v023_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v024_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v025_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v026_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v027_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v028_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v029_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v030_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v031_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v032_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v033_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v034_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v035_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v036_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v037_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v038_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v039_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v040_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v041_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v042_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v043_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v044_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v045_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v046_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v047_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v048_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v049_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v050_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v051_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v052_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v053_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v054_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v055_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v056_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v057_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v058_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v059_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v060_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v061_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v062_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v063_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v064_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v065_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v066_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v067_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v068_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v069_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v070_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v071_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v072_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v073_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v074_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v075_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v076_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v077_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v078_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v079_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v080_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v081_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v082_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v083_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v084_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v085_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v086_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v087_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v088_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v089_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v090_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v091_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v092_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v093_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v094_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v095_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v096_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v097_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v098_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v099_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v100_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v101_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v102_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v103_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v104_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v105_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v106_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v107_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v108_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v109_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v110_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v111_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v112_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v113_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v114_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v115_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v116_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v117_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v118_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v119_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v120_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v121_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v122_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v123_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v124_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v125_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v126_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v127_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v128_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v129_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v130_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v131_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v132_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v133_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v134_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v135_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v136_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v137_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v138_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v139_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v140_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v141_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v142_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v143_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v144_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v145_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v146_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v147_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    s=b.pct_change(2)
    result=_z(s,max(2*2,4))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v148_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of nge_inst_share_chg w=4d
def f45nge_network_growth_engine_slp4r2_4d_slope_v149_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 4)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of nge_inst_share_chg w=8d
def f45nge_network_growth_engine_slp8r4_8d_slope_v150_signal(sf3a_shares):
    b=_nge_inst_share_chg(sf3a_shares, 8)
    s=b.pct_change(4)
    result=_z(s,max(4*2,8))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f45nge_network_growth_engine_slp4r2_4d_slope_v001_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v001_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v002_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v002_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v003_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v003_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v004_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v004_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v005_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v005_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v006_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v006_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v007_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v007_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v008_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v008_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v009_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v009_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v010_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v010_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v011_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v011_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v012_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v012_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v013_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v013_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v014_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v014_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v015_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v015_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v016_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v016_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v017_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v017_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v018_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v018_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v019_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v019_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v020_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v020_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v021_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v021_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v022_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v022_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v023_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v023_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v024_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v024_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v025_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v025_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v026_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v026_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v027_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v027_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v028_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v028_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v029_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v029_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v030_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v030_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v031_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v031_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v032_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v032_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v033_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v033_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v034_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v034_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v035_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v035_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v036_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v036_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v037_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v037_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v038_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v038_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v039_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v039_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v040_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v040_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v041_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v041_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v042_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v042_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v043_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v043_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v044_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v044_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v045_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v045_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v046_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v046_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v047_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v047_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v048_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v048_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v049_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v049_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v050_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v050_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v051_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v051_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v052_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v052_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v053_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v053_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v054_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v054_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v055_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v055_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v056_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v056_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v057_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v057_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v058_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v058_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v059_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v059_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v060_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v060_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v061_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v061_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v062_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v062_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v063_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v063_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v064_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v064_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v065_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v065_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v066_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v066_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v067_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v067_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v068_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v068_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v069_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v069_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v070_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v070_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v071_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v071_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v072_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v072_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v073_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v073_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v074_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v074_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v075_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v075_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v076_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v076_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v077_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v077_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v078_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v078_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v079_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v079_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v080_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v080_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v081_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v081_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v082_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v082_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v083_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v083_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v084_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v084_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v085_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v085_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v086_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v086_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v087_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v087_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v088_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v088_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v089_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v089_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v090_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v090_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v091_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v091_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v092_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v092_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v093_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v093_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v094_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v094_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v095_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v095_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v096_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v096_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v097_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v097_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v098_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v098_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v099_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v099_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v100_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v100_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v101_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v101_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v102_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v102_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v103_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v103_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v104_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v104_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v105_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v105_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v106_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v106_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v107_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v107_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v108_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v108_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v109_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v109_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v110_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v110_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v111_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v111_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v112_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v112_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v113_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v113_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v114_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v114_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v115_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v115_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v116_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v116_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v117_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v117_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v118_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v118_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v119_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v119_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v120_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v120_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v121_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v121_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v122_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v122_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v123_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v123_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v124_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v124_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v125_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v125_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v126_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v126_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v127_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v127_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v128_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v128_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v129_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v129_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v130_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v130_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v131_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v131_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v132_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v132_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v133_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v133_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v134_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v134_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v135_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v135_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v136_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v136_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v137_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v137_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v138_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v138_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v139_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v139_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v140_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v140_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v141_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v141_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v142_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v142_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v143_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v143_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v144_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v144_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v145_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v145_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v146_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v146_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v147_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v147_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v148_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v148_signal}, "f45nge_network_growth_engine_slp4r2_4d_slope_v149_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp4r2_4d_slope_v149_signal}, "f45nge_network_growth_engine_slp8r4_8d_slope_v150_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_slp8r4_8d_slope_v150_signal}}
F45_NETWORK_GROWTH_ENGINE_REGISTRY_SLOPE = REGISTRY

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