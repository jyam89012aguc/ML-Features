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

def _vlt_pe_trend(pe, w):
    return pe.pct_change(w)
def _vlt_evebitda_z(evebitda, w):
    return _z(evebitda, w)


# 4d z-score of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_zscore_4d_base_v001_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_prank_4d_base_v002_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_roc_4d_base_v003_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_mnmx_4d_base_v004_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmean_4d_base_v005_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rstd_4d_base_v006_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_z2_4d_base_v007_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_pk2_4d_base_v008_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_roc2_4d_base_v009_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_diff_4d_base_v010_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmax_4d_base_v011_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmin_4d_base_v012_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_expz_4d_base_v013_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of vlt_pe_trend at 4d for valuation_trajectory
def f28vlt_valuation_trajectory_sign_4d_base_v014_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_posfr_4d_base_v015_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_zscore_8d_base_v016_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_prank_8d_base_v017_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_roc_8d_base_v018_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_mnmx_8d_base_v019_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmean_8d_base_v020_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rstd_8d_base_v021_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_z2_8d_base_v022_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_pk2_8d_base_v023_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_roc2_8d_base_v024_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_diff_8d_base_v025_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmax_8d_base_v026_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmin_8d_base_v027_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_expz_8d_base_v028_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of vlt_pe_trend at 8d for valuation_trajectory
def f28vlt_valuation_trajectory_sign_8d_base_v029_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_posfr_8d_base_v030_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_zscore_16d_base_v031_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_prank_16d_base_v032_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_roc_16d_base_v033_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d minmax of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_mnmx_16d_base_v034_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=_minmax(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling mean of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmean_16d_base_v035_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=raw.rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rstd_16d_base_v036_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=raw.rolling(16,min_periods=max(1,16//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_z2_16d_base_v037_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 16)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_pk2_16d_base_v038_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 16)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_roc2_16d_base_v039_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 16)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d diff of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_diff_16d_base_v040_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=raw.diff(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling max ratio of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmax_16d_base_v041_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    mx=raw.rolling(16,min_periods=max(1,16//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling min-std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmin_16d_base_v042_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    mn=raw.rolling(16,min_periods=max(1,16//2)).min()
    sd=raw.rolling(16,min_periods=max(1,16//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 16d) of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_expz_16d_base_v043_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    mu=raw.expanding(min_periods=16).mean()
    sd=raw.expanding(min_periods=16).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of vlt_pe_trend at 16d for valuation_trajectory
def f28vlt_valuation_trajectory_sign_16d_base_v044_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d positive fraction of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_posfr_16d_base_v045_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 16)
    result=(raw>0).astype(float).rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_zscore_4d_base_v046_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_prank_4d_base_v047_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_roc_4d_base_v048_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_mnmx_4d_base_v049_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmean_4d_base_v050_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rstd_4d_base_v051_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_z2_4d_base_v052_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_pk2_4d_base_v053_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_roc2_4d_base_v054_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_diff_4d_base_v055_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmax_4d_base_v056_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmin_4d_base_v057_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_expz_4d_base_v058_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of vlt_pe_trend at 4d for valuation_trajectory
def f28vlt_valuation_trajectory_sign_4d_base_v059_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_posfr_4d_base_v060_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 4)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_zscore_8d_base_v061_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_prank_8d_base_v062_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_roc_8d_base_v063_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_mnmx_8d_base_v064_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmean_8d_base_v065_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rstd_8d_base_v066_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_z2_8d_base_v067_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_pk2_8d_base_v068_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of vlt_evebitda_z for valuation_trajectory
def f28vlt_valuation_trajectory_roc2_8d_base_v069_signal(pe, evebitda):
    raw=_vlt_evebitda_z(evebitda, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_diff_8d_base_v070_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmax_8d_base_v071_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_rmin_8d_base_v072_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_expz_8d_base_v073_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of vlt_pe_trend at 8d for valuation_trajectory
def f28vlt_valuation_trajectory_sign_8d_base_v074_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of vlt_pe_trend for valuation_trajectory
def f28vlt_valuation_trajectory_posfr_8d_base_v075_signal(pe, evebitda):
    raw=_vlt_pe_trend(pe, 8)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f28vlt_valuation_trajectory_zscore_4d_base_v001_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_zscore_4d_base_v001_signal}, "f28vlt_valuation_trajectory_prank_4d_base_v002_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_prank_4d_base_v002_signal}, "f28vlt_valuation_trajectory_roc_4d_base_v003_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc_4d_base_v003_signal}, "f28vlt_valuation_trajectory_mnmx_4d_base_v004_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_mnmx_4d_base_v004_signal}, "f28vlt_valuation_trajectory_rmean_4d_base_v005_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmean_4d_base_v005_signal}, "f28vlt_valuation_trajectory_rstd_4d_base_v006_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rstd_4d_base_v006_signal}, "f28vlt_valuation_trajectory_z2_4d_base_v007_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_z2_4d_base_v007_signal}, "f28vlt_valuation_trajectory_pk2_4d_base_v008_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_pk2_4d_base_v008_signal}, "f28vlt_valuation_trajectory_roc2_4d_base_v009_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc2_4d_base_v009_signal}, "f28vlt_valuation_trajectory_diff_4d_base_v010_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_diff_4d_base_v010_signal}, "f28vlt_valuation_trajectory_rmax_4d_base_v011_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmax_4d_base_v011_signal}, "f28vlt_valuation_trajectory_rmin_4d_base_v012_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmin_4d_base_v012_signal}, "f28vlt_valuation_trajectory_expz_4d_base_v013_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_expz_4d_base_v013_signal}, "f28vlt_valuation_trajectory_sign_4d_base_v014_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_sign_4d_base_v014_signal}, "f28vlt_valuation_trajectory_posfr_4d_base_v015_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_posfr_4d_base_v015_signal}, "f28vlt_valuation_trajectory_zscore_8d_base_v016_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_zscore_8d_base_v016_signal}, "f28vlt_valuation_trajectory_prank_8d_base_v017_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_prank_8d_base_v017_signal}, "f28vlt_valuation_trajectory_roc_8d_base_v018_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc_8d_base_v018_signal}, "f28vlt_valuation_trajectory_mnmx_8d_base_v019_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_mnmx_8d_base_v019_signal}, "f28vlt_valuation_trajectory_rmean_8d_base_v020_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmean_8d_base_v020_signal}, "f28vlt_valuation_trajectory_rstd_8d_base_v021_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rstd_8d_base_v021_signal}, "f28vlt_valuation_trajectory_z2_8d_base_v022_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_z2_8d_base_v022_signal}, "f28vlt_valuation_trajectory_pk2_8d_base_v023_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_pk2_8d_base_v023_signal}, "f28vlt_valuation_trajectory_roc2_8d_base_v024_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc2_8d_base_v024_signal}, "f28vlt_valuation_trajectory_diff_8d_base_v025_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_diff_8d_base_v025_signal}, "f28vlt_valuation_trajectory_rmax_8d_base_v026_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmax_8d_base_v026_signal}, "f28vlt_valuation_trajectory_rmin_8d_base_v027_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmin_8d_base_v027_signal}, "f28vlt_valuation_trajectory_expz_8d_base_v028_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_expz_8d_base_v028_signal}, "f28vlt_valuation_trajectory_sign_8d_base_v029_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_sign_8d_base_v029_signal}, "f28vlt_valuation_trajectory_posfr_8d_base_v030_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_posfr_8d_base_v030_signal}, "f28vlt_valuation_trajectory_zscore_16d_base_v031_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_zscore_16d_base_v031_signal}, "f28vlt_valuation_trajectory_prank_16d_base_v032_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_prank_16d_base_v032_signal}, "f28vlt_valuation_trajectory_roc_16d_base_v033_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc_16d_base_v033_signal}, "f28vlt_valuation_trajectory_mnmx_16d_base_v034_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_mnmx_16d_base_v034_signal}, "f28vlt_valuation_trajectory_rmean_16d_base_v035_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmean_16d_base_v035_signal}, "f28vlt_valuation_trajectory_rstd_16d_base_v036_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rstd_16d_base_v036_signal}, "f28vlt_valuation_trajectory_z2_16d_base_v037_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_z2_16d_base_v037_signal}, "f28vlt_valuation_trajectory_pk2_16d_base_v038_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_pk2_16d_base_v038_signal}, "f28vlt_valuation_trajectory_roc2_16d_base_v039_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc2_16d_base_v039_signal}, "f28vlt_valuation_trajectory_diff_16d_base_v040_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_diff_16d_base_v040_signal}, "f28vlt_valuation_trajectory_rmax_16d_base_v041_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmax_16d_base_v041_signal}, "f28vlt_valuation_trajectory_rmin_16d_base_v042_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmin_16d_base_v042_signal}, "f28vlt_valuation_trajectory_expz_16d_base_v043_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_expz_16d_base_v043_signal}, "f28vlt_valuation_trajectory_sign_16d_base_v044_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_sign_16d_base_v044_signal}, "f28vlt_valuation_trajectory_posfr_16d_base_v045_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_posfr_16d_base_v045_signal}, "f28vlt_valuation_trajectory_zscore_4d_base_v046_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_zscore_4d_base_v046_signal}, "f28vlt_valuation_trajectory_prank_4d_base_v047_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_prank_4d_base_v047_signal}, "f28vlt_valuation_trajectory_roc_4d_base_v048_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc_4d_base_v048_signal}, "f28vlt_valuation_trajectory_mnmx_4d_base_v049_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_mnmx_4d_base_v049_signal}, "f28vlt_valuation_trajectory_rmean_4d_base_v050_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmean_4d_base_v050_signal}, "f28vlt_valuation_trajectory_rstd_4d_base_v051_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rstd_4d_base_v051_signal}, "f28vlt_valuation_trajectory_z2_4d_base_v052_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_z2_4d_base_v052_signal}, "f28vlt_valuation_trajectory_pk2_4d_base_v053_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_pk2_4d_base_v053_signal}, "f28vlt_valuation_trajectory_roc2_4d_base_v054_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc2_4d_base_v054_signal}, "f28vlt_valuation_trajectory_diff_4d_base_v055_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_diff_4d_base_v055_signal}, "f28vlt_valuation_trajectory_rmax_4d_base_v056_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmax_4d_base_v056_signal}, "f28vlt_valuation_trajectory_rmin_4d_base_v057_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmin_4d_base_v057_signal}, "f28vlt_valuation_trajectory_expz_4d_base_v058_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_expz_4d_base_v058_signal}, "f28vlt_valuation_trajectory_sign_4d_base_v059_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_sign_4d_base_v059_signal}, "f28vlt_valuation_trajectory_posfr_4d_base_v060_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_posfr_4d_base_v060_signal}, "f28vlt_valuation_trajectory_zscore_8d_base_v061_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_zscore_8d_base_v061_signal}, "f28vlt_valuation_trajectory_prank_8d_base_v062_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_prank_8d_base_v062_signal}, "f28vlt_valuation_trajectory_roc_8d_base_v063_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc_8d_base_v063_signal}, "f28vlt_valuation_trajectory_mnmx_8d_base_v064_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_mnmx_8d_base_v064_signal}, "f28vlt_valuation_trajectory_rmean_8d_base_v065_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmean_8d_base_v065_signal}, "f28vlt_valuation_trajectory_rstd_8d_base_v066_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rstd_8d_base_v066_signal}, "f28vlt_valuation_trajectory_z2_8d_base_v067_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_z2_8d_base_v067_signal}, "f28vlt_valuation_trajectory_pk2_8d_base_v068_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_pk2_8d_base_v068_signal}, "f28vlt_valuation_trajectory_roc2_8d_base_v069_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_roc2_8d_base_v069_signal}, "f28vlt_valuation_trajectory_diff_8d_base_v070_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_diff_8d_base_v070_signal}, "f28vlt_valuation_trajectory_rmax_8d_base_v071_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmax_8d_base_v071_signal}, "f28vlt_valuation_trajectory_rmin_8d_base_v072_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_rmin_8d_base_v072_signal}, "f28vlt_valuation_trajectory_expz_8d_base_v073_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_expz_8d_base_v073_signal}, "f28vlt_valuation_trajectory_sign_8d_base_v074_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_sign_8d_base_v074_signal}, "f28vlt_valuation_trajectory_posfr_8d_base_v075_signal": {"inputs": ['pe', 'evebitda'], "func": f28vlt_valuation_trajectory_posfr_8d_base_v075_signal}}
F28_VALUATION_TRAJECTORY_REGISTRY_001_075 = REGISTRY

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