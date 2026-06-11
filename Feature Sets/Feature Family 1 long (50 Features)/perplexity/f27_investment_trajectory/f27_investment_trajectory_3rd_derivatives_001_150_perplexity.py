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

def _ivt_capex_z(capex, w):
    return _z(capex, w)
def _ivt_capex_trend(capex, w):
    return capex.rolling(w, min_periods=max(1, w//2)).mean()


# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v001_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v002_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v003_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v004_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v005_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v006_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v007_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v008_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v009_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v010_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v011_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v012_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v013_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v014_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v015_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v016_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v017_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v018_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v019_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v020_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v021_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v022_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v023_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v024_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v025_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v026_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v027_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v028_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v029_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v030_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v031_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v032_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v033_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v034_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v035_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v036_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v037_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v038_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v039_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v040_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v041_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v042_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v043_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v044_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v045_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v046_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v047_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v048_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v049_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v050_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v051_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v052_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v053_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v054_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v055_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v056_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v057_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v058_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v059_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v060_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v061_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v062_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v063_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v064_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v065_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v066_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v067_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v068_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v069_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v070_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v071_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v072_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v073_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v074_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v075_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v076_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v077_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v078_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v079_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v080_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v081_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v082_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v083_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v084_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v085_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v086_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v087_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v088_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v089_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v090_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v091_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v092_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v093_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v094_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v095_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v096_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v097_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v098_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v099_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v100_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v101_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v102_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v103_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v104_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v105_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v106_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v107_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v108_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v109_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v110_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v111_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v112_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v113_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v114_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v115_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v116_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v117_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v118_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v119_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v120_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v121_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v122_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v123_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v124_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v125_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v126_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v127_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v128_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v129_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v130_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v131_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v132_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v133_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v134_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v135_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v136_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v137_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v138_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v139_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v140_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v141_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v142_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v143_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v144_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 2d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r2_4d_jerk_v145_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(2)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r4_8d_jerk_v146_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(4)/b.shift(4).abs().replace(0,np.nan)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r2_12d_jerk_v147_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(2)
    result=s.pct_change(2)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d jerk of ivt_capex_z w=4d
def f27ivt_investment_trajectory_jrk4r4_4d_jerk_v148_signal(capex):
    b=_ivt_capex_z(capex, 4)
    s=b.pct_change(4)
    result=s.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# diff-diff jerk of ivt_capex_z w=8d
def f27ivt_investment_trajectory_jrk8r2_8d_jerk_v149_signal(capex):
    b=_ivt_capex_z(capex, 8)
    s=b.diff(2)/b.shift(2).abs().replace(0,np.nan)
    result=s.diff(2)
    return result.replace([np.inf,-np.inf],np.nan)

# pct-pct jerk of ivt_capex_z w=12d
def f27ivt_investment_trajectory_jrk12r4_12d_jerk_v150_signal(capex):
    b=_ivt_capex_z(capex, 12)
    s=b.pct_change(4)
    result=s.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f27ivt_investment_trajectory_jrk4r2_4d_jerk_v001_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v001_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v002_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v002_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v003_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v003_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v004_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v004_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v005_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v005_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v006_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v006_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v007_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v007_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v008_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v008_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v009_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v009_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v010_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v010_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v011_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v011_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v012_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v012_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v013_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v013_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v014_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v014_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v015_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v015_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v016_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v016_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v017_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v017_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v018_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v018_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v019_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v019_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v020_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v020_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v021_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v021_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v022_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v022_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v023_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v023_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v024_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v024_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v025_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v025_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v026_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v026_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v027_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v027_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v028_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v028_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v029_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v029_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v030_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v030_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v031_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v031_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v032_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v032_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v033_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v033_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v034_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v034_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v035_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v035_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v036_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v036_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v037_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v037_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v038_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v038_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v039_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v039_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v040_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v040_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v041_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v041_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v042_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v042_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v043_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v043_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v044_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v044_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v045_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v045_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v046_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v046_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v047_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v047_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v048_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v048_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v049_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v049_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v050_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v050_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v051_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v051_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v052_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v052_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v053_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v053_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v054_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v054_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v055_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v055_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v056_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v056_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v057_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v057_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v058_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v058_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v059_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v059_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v060_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v060_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v061_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v061_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v062_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v062_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v063_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v063_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v064_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v064_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v065_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v065_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v066_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v066_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v067_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v067_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v068_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v068_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v069_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v069_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v070_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v070_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v071_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v071_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v072_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v072_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v073_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v073_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v074_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v074_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v075_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v075_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v076_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v076_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v077_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v077_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v078_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v078_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v079_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v079_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v080_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v080_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v081_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v081_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v082_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v082_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v083_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v083_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v084_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v084_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v085_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v085_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v086_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v086_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v087_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v087_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v088_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v088_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v089_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v089_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v090_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v090_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v091_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v091_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v092_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v092_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v093_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v093_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v094_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v094_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v095_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v095_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v096_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v096_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v097_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v097_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v098_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v098_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v099_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v099_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v100_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v100_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v101_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v101_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v102_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v102_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v103_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v103_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v104_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v104_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v105_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v105_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v106_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v106_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v107_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v107_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v108_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v108_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v109_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v109_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v110_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v110_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v111_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v111_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v112_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v112_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v113_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v113_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v114_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v114_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v115_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v115_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v116_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v116_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v117_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v117_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v118_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v118_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v119_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v119_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v120_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v120_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v121_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v121_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v122_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v122_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v123_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v123_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v124_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v124_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v125_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v125_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v126_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v126_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v127_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v127_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v128_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v128_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v129_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v129_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v130_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v130_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v131_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v131_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v132_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v132_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v133_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v133_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v134_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v134_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v135_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v135_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v136_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v136_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v137_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v137_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v138_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v138_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v139_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v139_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v140_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v140_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v141_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v141_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v142_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v142_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v143_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v143_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v144_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v144_signal}, "f27ivt_investment_trajectory_jrk4r2_4d_jerk_v145_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r2_4d_jerk_v145_signal}, "f27ivt_investment_trajectory_jrk8r4_8d_jerk_v146_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r4_8d_jerk_v146_signal}, "f27ivt_investment_trajectory_jrk12r2_12d_jerk_v147_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r2_12d_jerk_v147_signal}, "f27ivt_investment_trajectory_jrk4r4_4d_jerk_v148_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk4r4_4d_jerk_v148_signal}, "f27ivt_investment_trajectory_jrk8r2_8d_jerk_v149_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk8r2_8d_jerk_v149_signal}, "f27ivt_investment_trajectory_jrk12r4_12d_jerk_v150_signal": {"inputs": ['capex'], "func": f27ivt_investment_trajectory_jrk12r4_12d_jerk_v150_signal}}
F27_INVESTMENT_TRAJECTORY_REGISTRY_JERK = REGISTRY

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