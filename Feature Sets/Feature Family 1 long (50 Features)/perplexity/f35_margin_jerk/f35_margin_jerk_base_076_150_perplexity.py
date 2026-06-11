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

def _mgj_gp_margin(gp, revenue):
    return _safe_div(gp, revenue.abs())
def _mgj_jerk(gp, revenue, w):
    m = _mgj_gp_margin(gp, revenue)
    return m.diff(w).diff(w)


# 4d z-score of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_zscore_4d_base_v076_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_prank_4d_base_v077_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_roc_4d_base_v078_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_mnmx_4d_base_v079_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmean_4d_base_v080_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rstd_4d_base_v081_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_z2_4d_base_v082_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_pk2_4d_base_v083_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_roc2_4d_base_v084_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_diff_4d_base_v085_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmax_4d_base_v086_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmin_4d_base_v087_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_expz_4d_base_v088_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of mgj_gp_margin at 4d for margin_jerk
def f35mgj_margin_jerk_sign_4d_base_v089_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_posfr_4d_base_v090_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_zscore_8d_base_v091_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_prank_8d_base_v092_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_roc_8d_base_v093_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_mnmx_8d_base_v094_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmean_8d_base_v095_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rstd_8d_base_v096_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_z2_8d_base_v097_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_pk2_8d_base_v098_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_roc2_8d_base_v099_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_diff_8d_base_v100_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmax_8d_base_v101_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmin_8d_base_v102_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_expz_8d_base_v103_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of mgj_gp_margin at 8d for margin_jerk
def f35mgj_margin_jerk_sign_8d_base_v104_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_posfr_8d_base_v105_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_zscore_16d_base_v106_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_prank_16d_base_v107_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_roc_16d_base_v108_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d minmax of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_mnmx_16d_base_v109_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_minmax(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling mean of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmean_16d_base_v110_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rstd_16d_base_v111_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(16,min_periods=max(1,16//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_z2_16d_base_v112_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 16)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_pk2_16d_base_v113_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 16)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_roc2_16d_base_v114_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 16)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d diff of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_diff_16d_base_v115_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.diff(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling max ratio of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmax_16d_base_v116_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mx=raw.rolling(16,min_periods=max(1,16//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling min-std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmin_16d_base_v117_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mn=raw.rolling(16,min_periods=max(1,16//2)).min()
    sd=raw.rolling(16,min_periods=max(1,16//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 16d) of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_expz_16d_base_v118_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mu=raw.expanding(min_periods=16).mean()
    sd=raw.expanding(min_periods=16).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of mgj_gp_margin at 16d for margin_jerk
def f35mgj_margin_jerk_sign_16d_base_v119_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d positive fraction of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_posfr_16d_base_v120_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=(raw>0).astype(float).rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_zscore_4d_base_v121_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_prank_4d_base_v122_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_roc_4d_base_v123_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_mnmx_4d_base_v124_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmean_4d_base_v125_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rstd_4d_base_v126_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_z2_4d_base_v127_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_pk2_4d_base_v128_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_roc2_4d_base_v129_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_diff_4d_base_v130_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmax_4d_base_v131_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmin_4d_base_v132_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_expz_4d_base_v133_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of mgj_gp_margin at 4d for margin_jerk
def f35mgj_margin_jerk_sign_4d_base_v134_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_posfr_4d_base_v135_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_zscore_8d_base_v136_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_prank_8d_base_v137_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_roc_8d_base_v138_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_mnmx_8d_base_v139_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmean_8d_base_v140_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rstd_8d_base_v141_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_z2_8d_base_v142_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_pk2_8d_base_v143_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of mgj_jerk for margin_jerk
def f35mgj_margin_jerk_roc2_8d_base_v144_signal(gp, revenue):
    raw=_mgj_jerk(gp, revenue, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_diff_8d_base_v145_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmax_8d_base_v146_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_rmin_8d_base_v147_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_expz_8d_base_v148_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of mgj_gp_margin at 8d for margin_jerk
def f35mgj_margin_jerk_sign_8d_base_v149_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of mgj_gp_margin for margin_jerk
def f35mgj_margin_jerk_posfr_8d_base_v150_signal(gp, revenue):
    raw=_mgj_gp_margin(gp, revenue)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f35mgj_margin_jerk_zscore_4d_base_v076_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_zscore_4d_base_v076_signal}, "f35mgj_margin_jerk_prank_4d_base_v077_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_prank_4d_base_v077_signal}, "f35mgj_margin_jerk_roc_4d_base_v078_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc_4d_base_v078_signal}, "f35mgj_margin_jerk_mnmx_4d_base_v079_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_mnmx_4d_base_v079_signal}, "f35mgj_margin_jerk_rmean_4d_base_v080_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmean_4d_base_v080_signal}, "f35mgj_margin_jerk_rstd_4d_base_v081_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rstd_4d_base_v081_signal}, "f35mgj_margin_jerk_z2_4d_base_v082_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_z2_4d_base_v082_signal}, "f35mgj_margin_jerk_pk2_4d_base_v083_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_pk2_4d_base_v083_signal}, "f35mgj_margin_jerk_roc2_4d_base_v084_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc2_4d_base_v084_signal}, "f35mgj_margin_jerk_diff_4d_base_v085_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_diff_4d_base_v085_signal}, "f35mgj_margin_jerk_rmax_4d_base_v086_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmax_4d_base_v086_signal}, "f35mgj_margin_jerk_rmin_4d_base_v087_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmin_4d_base_v087_signal}, "f35mgj_margin_jerk_expz_4d_base_v088_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_expz_4d_base_v088_signal}, "f35mgj_margin_jerk_sign_4d_base_v089_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_sign_4d_base_v089_signal}, "f35mgj_margin_jerk_posfr_4d_base_v090_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_posfr_4d_base_v090_signal}, "f35mgj_margin_jerk_zscore_8d_base_v091_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_zscore_8d_base_v091_signal}, "f35mgj_margin_jerk_prank_8d_base_v092_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_prank_8d_base_v092_signal}, "f35mgj_margin_jerk_roc_8d_base_v093_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc_8d_base_v093_signal}, "f35mgj_margin_jerk_mnmx_8d_base_v094_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_mnmx_8d_base_v094_signal}, "f35mgj_margin_jerk_rmean_8d_base_v095_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmean_8d_base_v095_signal}, "f35mgj_margin_jerk_rstd_8d_base_v096_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rstd_8d_base_v096_signal}, "f35mgj_margin_jerk_z2_8d_base_v097_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_z2_8d_base_v097_signal}, "f35mgj_margin_jerk_pk2_8d_base_v098_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_pk2_8d_base_v098_signal}, "f35mgj_margin_jerk_roc2_8d_base_v099_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc2_8d_base_v099_signal}, "f35mgj_margin_jerk_diff_8d_base_v100_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_diff_8d_base_v100_signal}, "f35mgj_margin_jerk_rmax_8d_base_v101_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmax_8d_base_v101_signal}, "f35mgj_margin_jerk_rmin_8d_base_v102_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmin_8d_base_v102_signal}, "f35mgj_margin_jerk_expz_8d_base_v103_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_expz_8d_base_v103_signal}, "f35mgj_margin_jerk_sign_8d_base_v104_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_sign_8d_base_v104_signal}, "f35mgj_margin_jerk_posfr_8d_base_v105_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_posfr_8d_base_v105_signal}, "f35mgj_margin_jerk_zscore_16d_base_v106_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_zscore_16d_base_v106_signal}, "f35mgj_margin_jerk_prank_16d_base_v107_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_prank_16d_base_v107_signal}, "f35mgj_margin_jerk_roc_16d_base_v108_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc_16d_base_v108_signal}, "f35mgj_margin_jerk_mnmx_16d_base_v109_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_mnmx_16d_base_v109_signal}, "f35mgj_margin_jerk_rmean_16d_base_v110_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmean_16d_base_v110_signal}, "f35mgj_margin_jerk_rstd_16d_base_v111_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rstd_16d_base_v111_signal}, "f35mgj_margin_jerk_z2_16d_base_v112_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_z2_16d_base_v112_signal}, "f35mgj_margin_jerk_pk2_16d_base_v113_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_pk2_16d_base_v113_signal}, "f35mgj_margin_jerk_roc2_16d_base_v114_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc2_16d_base_v114_signal}, "f35mgj_margin_jerk_diff_16d_base_v115_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_diff_16d_base_v115_signal}, "f35mgj_margin_jerk_rmax_16d_base_v116_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmax_16d_base_v116_signal}, "f35mgj_margin_jerk_rmin_16d_base_v117_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmin_16d_base_v117_signal}, "f35mgj_margin_jerk_expz_16d_base_v118_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_expz_16d_base_v118_signal}, "f35mgj_margin_jerk_sign_16d_base_v119_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_sign_16d_base_v119_signal}, "f35mgj_margin_jerk_posfr_16d_base_v120_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_posfr_16d_base_v120_signal}, "f35mgj_margin_jerk_zscore_4d_base_v121_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_zscore_4d_base_v121_signal}, "f35mgj_margin_jerk_prank_4d_base_v122_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_prank_4d_base_v122_signal}, "f35mgj_margin_jerk_roc_4d_base_v123_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc_4d_base_v123_signal}, "f35mgj_margin_jerk_mnmx_4d_base_v124_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_mnmx_4d_base_v124_signal}, "f35mgj_margin_jerk_rmean_4d_base_v125_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmean_4d_base_v125_signal}, "f35mgj_margin_jerk_rstd_4d_base_v126_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rstd_4d_base_v126_signal}, "f35mgj_margin_jerk_z2_4d_base_v127_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_z2_4d_base_v127_signal}, "f35mgj_margin_jerk_pk2_4d_base_v128_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_pk2_4d_base_v128_signal}, "f35mgj_margin_jerk_roc2_4d_base_v129_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc2_4d_base_v129_signal}, "f35mgj_margin_jerk_diff_4d_base_v130_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_diff_4d_base_v130_signal}, "f35mgj_margin_jerk_rmax_4d_base_v131_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmax_4d_base_v131_signal}, "f35mgj_margin_jerk_rmin_4d_base_v132_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmin_4d_base_v132_signal}, "f35mgj_margin_jerk_expz_4d_base_v133_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_expz_4d_base_v133_signal}, "f35mgj_margin_jerk_sign_4d_base_v134_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_sign_4d_base_v134_signal}, "f35mgj_margin_jerk_posfr_4d_base_v135_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_posfr_4d_base_v135_signal}, "f35mgj_margin_jerk_zscore_8d_base_v136_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_zscore_8d_base_v136_signal}, "f35mgj_margin_jerk_prank_8d_base_v137_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_prank_8d_base_v137_signal}, "f35mgj_margin_jerk_roc_8d_base_v138_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc_8d_base_v138_signal}, "f35mgj_margin_jerk_mnmx_8d_base_v139_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_mnmx_8d_base_v139_signal}, "f35mgj_margin_jerk_rmean_8d_base_v140_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmean_8d_base_v140_signal}, "f35mgj_margin_jerk_rstd_8d_base_v141_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rstd_8d_base_v141_signal}, "f35mgj_margin_jerk_z2_8d_base_v142_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_z2_8d_base_v142_signal}, "f35mgj_margin_jerk_pk2_8d_base_v143_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_pk2_8d_base_v143_signal}, "f35mgj_margin_jerk_roc2_8d_base_v144_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_roc2_8d_base_v144_signal}, "f35mgj_margin_jerk_diff_8d_base_v145_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_diff_8d_base_v145_signal}, "f35mgj_margin_jerk_rmax_8d_base_v146_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmax_8d_base_v146_signal}, "f35mgj_margin_jerk_rmin_8d_base_v147_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_rmin_8d_base_v147_signal}, "f35mgj_margin_jerk_expz_8d_base_v148_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_expz_8d_base_v148_signal}, "f35mgj_margin_jerk_sign_8d_base_v149_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_sign_8d_base_v149_signal}, "f35mgj_margin_jerk_posfr_8d_base_v150_signal": {"inputs": ['gp', 'revenue'], "func": f35mgj_margin_jerk_posfr_8d_base_v150_signal}}
F35_MARGIN_JERK_REGISTRY_076_150 = REGISTRY

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