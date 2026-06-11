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


# 4d z-score of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_zscore_4d_base_v001_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_prank_4d_base_v002_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_roc_4d_base_v003_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_mnmx_4d_base_v004_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmean_4d_base_v005_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rstd_4d_base_v006_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_z2_4d_base_v007_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_pk2_4d_base_v008_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_roc2_4d_base_v009_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_diff_4d_base_v010_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmax_4d_base_v011_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmin_4d_base_v012_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_expz_4d_base_v013_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of nge_inst_share_chg at 4d for network_growth_engine
def f45nge_network_growth_engine_sign_4d_base_v014_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_posfr_4d_base_v015_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_zscore_8d_base_v016_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_prank_8d_base_v017_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_roc_8d_base_v018_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_mnmx_8d_base_v019_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmean_8d_base_v020_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rstd_8d_base_v021_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_z2_8d_base_v022_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_pk2_8d_base_v023_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_roc2_8d_base_v024_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_diff_8d_base_v025_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmax_8d_base_v026_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmin_8d_base_v027_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_expz_8d_base_v028_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of nge_inst_share_chg at 8d for network_growth_engine
def f45nge_network_growth_engine_sign_8d_base_v029_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_posfr_8d_base_v030_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_zscore_16d_base_v031_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_prank_16d_base_v032_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_roc_16d_base_v033_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d minmax of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_mnmx_16d_base_v034_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=_minmax(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling mean of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmean_16d_base_v035_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=raw.rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rstd_16d_base_v036_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=raw.rolling(16,min_periods=max(1,16//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_z2_16d_base_v037_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 16)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_pk2_16d_base_v038_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 16)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_roc2_16d_base_v039_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 16)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d diff of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_diff_16d_base_v040_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=raw.diff(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling max ratio of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmax_16d_base_v041_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    mx=raw.rolling(16,min_periods=max(1,16//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling min-std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmin_16d_base_v042_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    mn=raw.rolling(16,min_periods=max(1,16//2)).min()
    sd=raw.rolling(16,min_periods=max(1,16//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 16d) of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_expz_16d_base_v043_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    mu=raw.expanding(min_periods=16).mean()
    sd=raw.expanding(min_periods=16).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of nge_inst_share_chg at 16d for network_growth_engine
def f45nge_network_growth_engine_sign_16d_base_v044_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d positive fraction of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_posfr_16d_base_v045_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 16)
    result=(raw>0).astype(float).rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_zscore_4d_base_v046_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_prank_4d_base_v047_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_roc_4d_base_v048_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_mnmx_4d_base_v049_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmean_4d_base_v050_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rstd_4d_base_v051_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_z2_4d_base_v052_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_pk2_4d_base_v053_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_roc2_4d_base_v054_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_diff_4d_base_v055_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmax_4d_base_v056_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmin_4d_base_v057_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_expz_4d_base_v058_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of nge_inst_share_chg at 4d for network_growth_engine
def f45nge_network_growth_engine_sign_4d_base_v059_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_posfr_4d_base_v060_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 4)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_zscore_8d_base_v061_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_prank_8d_base_v062_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_roc_8d_base_v063_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_mnmx_8d_base_v064_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmean_8d_base_v065_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rstd_8d_base_v066_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_z2_8d_base_v067_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_pk2_8d_base_v068_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of nge_inst_z for network_growth_engine
def f45nge_network_growth_engine_roc2_8d_base_v069_signal(sf3a_shares):
    raw=_nge_inst_z(sf3a_shares, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_diff_8d_base_v070_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmax_8d_base_v071_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_rmin_8d_base_v072_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_expz_8d_base_v073_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of nge_inst_share_chg at 8d for network_growth_engine
def f45nge_network_growth_engine_sign_8d_base_v074_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of nge_inst_share_chg for network_growth_engine
def f45nge_network_growth_engine_posfr_8d_base_v075_signal(sf3a_shares):
    raw=_nge_inst_share_chg(sf3a_shares, 8)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f45nge_network_growth_engine_zscore_4d_base_v001_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_zscore_4d_base_v001_signal}, "f45nge_network_growth_engine_prank_4d_base_v002_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_prank_4d_base_v002_signal}, "f45nge_network_growth_engine_roc_4d_base_v003_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc_4d_base_v003_signal}, "f45nge_network_growth_engine_mnmx_4d_base_v004_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_mnmx_4d_base_v004_signal}, "f45nge_network_growth_engine_rmean_4d_base_v005_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmean_4d_base_v005_signal}, "f45nge_network_growth_engine_rstd_4d_base_v006_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rstd_4d_base_v006_signal}, "f45nge_network_growth_engine_z2_4d_base_v007_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_z2_4d_base_v007_signal}, "f45nge_network_growth_engine_pk2_4d_base_v008_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_pk2_4d_base_v008_signal}, "f45nge_network_growth_engine_roc2_4d_base_v009_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc2_4d_base_v009_signal}, "f45nge_network_growth_engine_diff_4d_base_v010_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_diff_4d_base_v010_signal}, "f45nge_network_growth_engine_rmax_4d_base_v011_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmax_4d_base_v011_signal}, "f45nge_network_growth_engine_rmin_4d_base_v012_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmin_4d_base_v012_signal}, "f45nge_network_growth_engine_expz_4d_base_v013_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_expz_4d_base_v013_signal}, "f45nge_network_growth_engine_sign_4d_base_v014_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_sign_4d_base_v014_signal}, "f45nge_network_growth_engine_posfr_4d_base_v015_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_posfr_4d_base_v015_signal}, "f45nge_network_growth_engine_zscore_8d_base_v016_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_zscore_8d_base_v016_signal}, "f45nge_network_growth_engine_prank_8d_base_v017_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_prank_8d_base_v017_signal}, "f45nge_network_growth_engine_roc_8d_base_v018_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc_8d_base_v018_signal}, "f45nge_network_growth_engine_mnmx_8d_base_v019_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_mnmx_8d_base_v019_signal}, "f45nge_network_growth_engine_rmean_8d_base_v020_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmean_8d_base_v020_signal}, "f45nge_network_growth_engine_rstd_8d_base_v021_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rstd_8d_base_v021_signal}, "f45nge_network_growth_engine_z2_8d_base_v022_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_z2_8d_base_v022_signal}, "f45nge_network_growth_engine_pk2_8d_base_v023_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_pk2_8d_base_v023_signal}, "f45nge_network_growth_engine_roc2_8d_base_v024_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc2_8d_base_v024_signal}, "f45nge_network_growth_engine_diff_8d_base_v025_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_diff_8d_base_v025_signal}, "f45nge_network_growth_engine_rmax_8d_base_v026_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmax_8d_base_v026_signal}, "f45nge_network_growth_engine_rmin_8d_base_v027_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmin_8d_base_v027_signal}, "f45nge_network_growth_engine_expz_8d_base_v028_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_expz_8d_base_v028_signal}, "f45nge_network_growth_engine_sign_8d_base_v029_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_sign_8d_base_v029_signal}, "f45nge_network_growth_engine_posfr_8d_base_v030_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_posfr_8d_base_v030_signal}, "f45nge_network_growth_engine_zscore_16d_base_v031_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_zscore_16d_base_v031_signal}, "f45nge_network_growth_engine_prank_16d_base_v032_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_prank_16d_base_v032_signal}, "f45nge_network_growth_engine_roc_16d_base_v033_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc_16d_base_v033_signal}, "f45nge_network_growth_engine_mnmx_16d_base_v034_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_mnmx_16d_base_v034_signal}, "f45nge_network_growth_engine_rmean_16d_base_v035_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmean_16d_base_v035_signal}, "f45nge_network_growth_engine_rstd_16d_base_v036_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rstd_16d_base_v036_signal}, "f45nge_network_growth_engine_z2_16d_base_v037_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_z2_16d_base_v037_signal}, "f45nge_network_growth_engine_pk2_16d_base_v038_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_pk2_16d_base_v038_signal}, "f45nge_network_growth_engine_roc2_16d_base_v039_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc2_16d_base_v039_signal}, "f45nge_network_growth_engine_diff_16d_base_v040_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_diff_16d_base_v040_signal}, "f45nge_network_growth_engine_rmax_16d_base_v041_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmax_16d_base_v041_signal}, "f45nge_network_growth_engine_rmin_16d_base_v042_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmin_16d_base_v042_signal}, "f45nge_network_growth_engine_expz_16d_base_v043_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_expz_16d_base_v043_signal}, "f45nge_network_growth_engine_sign_16d_base_v044_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_sign_16d_base_v044_signal}, "f45nge_network_growth_engine_posfr_16d_base_v045_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_posfr_16d_base_v045_signal}, "f45nge_network_growth_engine_zscore_4d_base_v046_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_zscore_4d_base_v046_signal}, "f45nge_network_growth_engine_prank_4d_base_v047_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_prank_4d_base_v047_signal}, "f45nge_network_growth_engine_roc_4d_base_v048_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc_4d_base_v048_signal}, "f45nge_network_growth_engine_mnmx_4d_base_v049_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_mnmx_4d_base_v049_signal}, "f45nge_network_growth_engine_rmean_4d_base_v050_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmean_4d_base_v050_signal}, "f45nge_network_growth_engine_rstd_4d_base_v051_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rstd_4d_base_v051_signal}, "f45nge_network_growth_engine_z2_4d_base_v052_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_z2_4d_base_v052_signal}, "f45nge_network_growth_engine_pk2_4d_base_v053_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_pk2_4d_base_v053_signal}, "f45nge_network_growth_engine_roc2_4d_base_v054_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc2_4d_base_v054_signal}, "f45nge_network_growth_engine_diff_4d_base_v055_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_diff_4d_base_v055_signal}, "f45nge_network_growth_engine_rmax_4d_base_v056_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmax_4d_base_v056_signal}, "f45nge_network_growth_engine_rmin_4d_base_v057_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmin_4d_base_v057_signal}, "f45nge_network_growth_engine_expz_4d_base_v058_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_expz_4d_base_v058_signal}, "f45nge_network_growth_engine_sign_4d_base_v059_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_sign_4d_base_v059_signal}, "f45nge_network_growth_engine_posfr_4d_base_v060_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_posfr_4d_base_v060_signal}, "f45nge_network_growth_engine_zscore_8d_base_v061_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_zscore_8d_base_v061_signal}, "f45nge_network_growth_engine_prank_8d_base_v062_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_prank_8d_base_v062_signal}, "f45nge_network_growth_engine_roc_8d_base_v063_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc_8d_base_v063_signal}, "f45nge_network_growth_engine_mnmx_8d_base_v064_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_mnmx_8d_base_v064_signal}, "f45nge_network_growth_engine_rmean_8d_base_v065_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmean_8d_base_v065_signal}, "f45nge_network_growth_engine_rstd_8d_base_v066_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rstd_8d_base_v066_signal}, "f45nge_network_growth_engine_z2_8d_base_v067_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_z2_8d_base_v067_signal}, "f45nge_network_growth_engine_pk2_8d_base_v068_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_pk2_8d_base_v068_signal}, "f45nge_network_growth_engine_roc2_8d_base_v069_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_roc2_8d_base_v069_signal}, "f45nge_network_growth_engine_diff_8d_base_v070_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_diff_8d_base_v070_signal}, "f45nge_network_growth_engine_rmax_8d_base_v071_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmax_8d_base_v071_signal}, "f45nge_network_growth_engine_rmin_8d_base_v072_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_rmin_8d_base_v072_signal}, "f45nge_network_growth_engine_expz_8d_base_v073_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_expz_8d_base_v073_signal}, "f45nge_network_growth_engine_sign_8d_base_v074_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_sign_8d_base_v074_signal}, "f45nge_network_growth_engine_posfr_8d_base_v075_signal": {"inputs": ['sf3a_shares'], "func": f45nge_network_growth_engine_posfr_8d_base_v075_signal}}
F45_NETWORK_GROWTH_ENGINE_REGISTRY_001_075 = REGISTRY

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