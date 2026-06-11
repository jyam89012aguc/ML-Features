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

def _pps_gp_margin(gp, revenue):
    return _safe_div(gp, revenue.abs())
def _pps_margin_momentum(gp, revenue, w):
    m = _pps_gp_margin(gp, revenue)
    return m.pct_change(w)


# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v001_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v002_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v003_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v004_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v005_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v006_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v007_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v008_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v009_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v010_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v011_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v012_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v013_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v014_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v015_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v016_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v017_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v018_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v019_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v020_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v021_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v022_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v023_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v024_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v025_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v026_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v027_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v028_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v029_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v030_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v031_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v032_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v033_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v034_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v035_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v036_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v037_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v038_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v039_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v040_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v041_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v042_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v043_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v044_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v045_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v046_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v047_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v048_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v049_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v050_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v051_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v052_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v053_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v054_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v055_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v056_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v057_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v058_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v059_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v060_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v061_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v062_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v063_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v064_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v065_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v066_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v067_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v068_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v069_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v070_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v071_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v072_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v073_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v074_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v075_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v076_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v077_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v078_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v079_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v080_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v081_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v082_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v083_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v084_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v085_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v086_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v087_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v088_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v089_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v090_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v091_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v092_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v093_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v094_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v095_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v096_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v097_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v098_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v099_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v100_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v101_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v102_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v103_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v104_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v105_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v106_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v107_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v108_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v109_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v110_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v111_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v112_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v113_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v114_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v115_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v116_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v117_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v118_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v119_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v120_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v121_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v122_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v123_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v124_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v125_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v126_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v127_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v128_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v129_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v130_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v131_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v132_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v133_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v134_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v135_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v136_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v137_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v138_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v139_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v140_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v141_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v142_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v143_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v144_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r2_4d_jerk_v145_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r4_8d_jerk_v146_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r2_12d_jerk_v147_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of pps_gp_margin w=4d
def f41pps_pricing_power_signal_jrk4r4_4d_jerk_v148_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of pps_gp_margin w=8d
def f41pps_pricing_power_signal_jrk8r2_8d_jerk_v149_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of pps_gp_margin w=12d
def f41pps_pricing_power_signal_jrk12r4_12d_jerk_v150_signal(gp, revenue):
    b=_pps_gp_margin(gp, revenue)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f41pps_pricing_power_signal_jrk4r2_4d_jerk_v001_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v001_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v002_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v002_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v003_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v003_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v004_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v004_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v005_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v005_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v006_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v006_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v007_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v007_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v008_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v008_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v009_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v009_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v010_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v010_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v011_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v011_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v012_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v012_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v013_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v013_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v014_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v014_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v015_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v015_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v016_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v016_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v017_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v017_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v018_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v018_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v019_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v019_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v020_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v020_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v021_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v021_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v022_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v022_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v023_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v023_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v024_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v024_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v025_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v025_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v026_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v026_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v027_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v027_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v028_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v028_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v029_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v029_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v030_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v030_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v031_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v031_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v032_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v032_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v033_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v033_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v034_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v034_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v035_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v035_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v036_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v036_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v037_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v037_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v038_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v038_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v039_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v039_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v040_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v040_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v041_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v041_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v042_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v042_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v043_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v043_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v044_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v044_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v045_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v045_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v046_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v046_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v047_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v047_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v048_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v048_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v049_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v049_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v050_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v050_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v051_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v051_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v052_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v052_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v053_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v053_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v054_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v054_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v055_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v055_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v056_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v056_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v057_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v057_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v058_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v058_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v059_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v059_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v060_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v060_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v061_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v061_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v062_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v062_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v063_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v063_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v064_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v064_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v065_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v065_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v066_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v066_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v067_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v067_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v068_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v068_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v069_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v069_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v070_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v070_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v071_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v071_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v072_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v072_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v073_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v073_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v074_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v074_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v075_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v075_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v076_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v076_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v077_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v077_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v078_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v078_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v079_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v079_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v080_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v080_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v081_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v081_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v082_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v082_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v083_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v083_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v084_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v084_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v085_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v085_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v086_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v086_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v087_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v087_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v088_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v088_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v089_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v089_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v090_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v090_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v091_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v091_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v092_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v092_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v093_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v093_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v094_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v094_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v095_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v095_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v096_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v096_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v097_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v097_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v098_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v098_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v099_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v099_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v100_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v100_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v101_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v101_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v102_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v102_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v103_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v103_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v104_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v104_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v105_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v105_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v106_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v106_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v107_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v107_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v108_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v108_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v109_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v109_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v110_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v110_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v111_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v111_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v112_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v112_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v113_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v113_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v114_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v114_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v115_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v115_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v116_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v116_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v117_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v117_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v118_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v118_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v119_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v119_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v120_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v120_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v121_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v121_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v122_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v122_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v123_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v123_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v124_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v124_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v125_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v125_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v126_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v126_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v127_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v127_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v128_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v128_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v129_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v129_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v130_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v130_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v131_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v131_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v132_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v132_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v133_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v133_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v134_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v134_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v135_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v135_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v136_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v136_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v137_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v137_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v138_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v138_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v139_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v139_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v140_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v140_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v141_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v141_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v142_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v142_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v143_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v143_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v144_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v144_signal}, "f41pps_pricing_power_signal_jrk4r2_4d_jerk_v145_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r2_4d_jerk_v145_signal}, "f41pps_pricing_power_signal_jrk8r4_8d_jerk_v146_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r4_8d_jerk_v146_signal}, "f41pps_pricing_power_signal_jrk12r2_12d_jerk_v147_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r2_12d_jerk_v147_signal}, "f41pps_pricing_power_signal_jrk4r4_4d_jerk_v148_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk4r4_4d_jerk_v148_signal}, "f41pps_pricing_power_signal_jrk8r2_8d_jerk_v149_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk8r2_8d_jerk_v149_signal}, "f41pps_pricing_power_signal_jrk12r4_12d_jerk_v150_signal": {"inputs": ['gp', 'revenue'], "func": f41pps_pricing_power_signal_jrk12r4_12d_jerk_v150_signal}}
F41_PRICING_POWER_SIGNAL_REGISTRY_JERK = REGISTRY

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