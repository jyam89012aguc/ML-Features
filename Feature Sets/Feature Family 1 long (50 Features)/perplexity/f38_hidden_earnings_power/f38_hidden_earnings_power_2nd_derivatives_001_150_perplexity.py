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

def _hep_ncfo_vs_netinc(ncfo, netinc):
    return _safe_div(ncfo, netinc.abs())
def _hep_power_z(ncfo, netinc, w):
    return _z(_hep_ncfo_vs_netinc(ncfo, netinc), w)


# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v001_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v002_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v003_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v004_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v005_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v006_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v007_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v008_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v009_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v010_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v011_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v012_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v013_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v014_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v015_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v016_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v017_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v018_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v019_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v020_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v021_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v022_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v023_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v024_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v025_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v026_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v027_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v028_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v029_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v030_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v031_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v032_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v033_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v034_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v035_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v036_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v037_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v038_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v039_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v040_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v041_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v042_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v043_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v044_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v045_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v046_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v047_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v048_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v049_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v050_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v051_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v052_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v053_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v054_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v055_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v056_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v057_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v058_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v059_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v060_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v061_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v062_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v063_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v064_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v065_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v066_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v067_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v068_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v069_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v070_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v071_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v072_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v073_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v074_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v075_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v076_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v077_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v078_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v079_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v080_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v081_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v082_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v083_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v084_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v085_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v086_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v087_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v088_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v089_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v090_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v091_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v092_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v093_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v094_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v095_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v096_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v097_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v098_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v099_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v100_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v101_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v102_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v103_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v104_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v105_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v106_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v107_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v108_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v109_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v110_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v111_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v112_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v113_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v114_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v115_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v116_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v117_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v118_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v119_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v120_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v121_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v122_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v123_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v124_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v125_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v126_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v127_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v128_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v129_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v130_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v131_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v132_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v133_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v134_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v135_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v136_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v137_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v138_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v139_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v140_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v141_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v142_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v143_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v144_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 2d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r2_4d_slope_v145_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r4_8d_slope_v146_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 2d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r2_12d_slope_v147_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(2)
    result=_z(s,max(2*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pct_change slope of hep_ncfo_vs_netinc w=4d
def f38hep_hidden_earnings_power_slp4r4_4d_slope_v148_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d diff slope of hep_ncfo_vs_netinc w=8d
def f38hep_hidden_earnings_power_slp8r2_8d_slope_v149_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    result=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# z-scored 4d slope of hep_ncfo_vs_netinc w=12d
def f38hep_hidden_earnings_power_slp12r4_12d_slope_v150_signal(ncfo, netinc):
    b=_hep_ncfo_vs_netinc(ncfo, netinc)
    s=b.pct_change(4)
    result=_z(s,max(4*2,12))
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f38hep_hidden_earnings_power_slp4r2_4d_slope_v001_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v001_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v002_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v002_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v003_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v003_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v004_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v004_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v005_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v005_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v006_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v006_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v007_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v007_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v008_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v008_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v009_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v009_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v010_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v010_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v011_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v011_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v012_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v012_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v013_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v013_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v014_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v014_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v015_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v015_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v016_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v016_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v017_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v017_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v018_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v018_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v019_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v019_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v020_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v020_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v021_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v021_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v022_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v022_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v023_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v023_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v024_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v024_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v025_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v025_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v026_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v026_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v027_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v027_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v028_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v028_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v029_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v029_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v030_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v030_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v031_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v031_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v032_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v032_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v033_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v033_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v034_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v034_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v035_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v035_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v036_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v036_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v037_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v037_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v038_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v038_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v039_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v039_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v040_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v040_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v041_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v041_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v042_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v042_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v043_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v043_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v044_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v044_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v045_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v045_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v046_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v046_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v047_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v047_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v048_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v048_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v049_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v049_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v050_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v050_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v051_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v051_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v052_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v052_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v053_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v053_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v054_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v054_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v055_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v055_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v056_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v056_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v057_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v057_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v058_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v058_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v059_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v059_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v060_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v060_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v061_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v061_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v062_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v062_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v063_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v063_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v064_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v064_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v065_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v065_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v066_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v066_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v067_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v067_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v068_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v068_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v069_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v069_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v070_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v070_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v071_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v071_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v072_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v072_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v073_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v073_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v074_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v074_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v075_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v075_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v076_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v076_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v077_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v077_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v078_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v078_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v079_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v079_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v080_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v080_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v081_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v081_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v082_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v082_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v083_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v083_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v084_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v084_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v085_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v085_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v086_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v086_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v087_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v087_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v088_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v088_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v089_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v089_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v090_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v090_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v091_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v091_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v092_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v092_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v093_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v093_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v094_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v094_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v095_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v095_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v096_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v096_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v097_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v097_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v098_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v098_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v099_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v099_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v100_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v100_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v101_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v101_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v102_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v102_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v103_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v103_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v104_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v104_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v105_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v105_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v106_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v106_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v107_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v107_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v108_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v108_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v109_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v109_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v110_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v110_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v111_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v111_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v112_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v112_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v113_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v113_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v114_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v114_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v115_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v115_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v116_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v116_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v117_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v117_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v118_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v118_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v119_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v119_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v120_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v120_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v121_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v121_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v122_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v122_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v123_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v123_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v124_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v124_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v125_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v125_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v126_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v126_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v127_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v127_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v128_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v128_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v129_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v129_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v130_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v130_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v131_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v131_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v132_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v132_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v133_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v133_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v134_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v134_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v135_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v135_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v136_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v136_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v137_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v137_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v138_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v138_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v139_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v139_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v140_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v140_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v141_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v141_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v142_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v142_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v143_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v143_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v144_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v144_signal}, "f38hep_hidden_earnings_power_slp4r2_4d_slope_v145_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r2_4d_slope_v145_signal}, "f38hep_hidden_earnings_power_slp8r4_8d_slope_v146_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r4_8d_slope_v146_signal}, "f38hep_hidden_earnings_power_slp12r2_12d_slope_v147_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r2_12d_slope_v147_signal}, "f38hep_hidden_earnings_power_slp4r4_4d_slope_v148_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp4r4_4d_slope_v148_signal}, "f38hep_hidden_earnings_power_slp8r2_8d_slope_v149_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp8r2_8d_slope_v149_signal}, "f38hep_hidden_earnings_power_slp12r4_12d_slope_v150_signal": {"inputs": ['ncfo', 'netinc'], "func": f38hep_hidden_earnings_power_slp12r4_12d_slope_v150_signal}}
F38_HIDDEN_EARNINGS_POWER_REGISTRY_SLOPE = REGISTRY

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