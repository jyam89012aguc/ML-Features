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

def _cwr_burn_rate(ncfo, w):
    return ncfo.rolling(w, min_periods=max(1, w//2)).mean()
def _cwr_runway(fcf, debt, w):
    burn = _cwr_burn_rate(fcf, w)
    return _safe_div(debt, burn.abs())


# 4d z-score of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_zscore_4d_base_v076_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_prank_4d_base_v077_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_roc_4d_base_v078_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_mnmx_4d_base_v079_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmean_4d_base_v080_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rstd_4d_base_v081_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of cwr_runway for cash_runway
def f48cwr_cash_runway_z2_4d_base_v082_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of cwr_runway for cash_runway
def f48cwr_cash_runway_pk2_4d_base_v083_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of cwr_runway for cash_runway
def f48cwr_cash_runway_roc2_4d_base_v084_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_diff_4d_base_v085_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmax_4d_base_v086_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmin_4d_base_v087_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_expz_4d_base_v088_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cwr_burn_rate at 4d for cash_runway
def f48cwr_cash_runway_sign_4d_base_v089_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_posfr_4d_base_v090_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_zscore_8d_base_v091_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_prank_8d_base_v092_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_roc_8d_base_v093_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_mnmx_8d_base_v094_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmean_8d_base_v095_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rstd_8d_base_v096_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of cwr_runway for cash_runway
def f48cwr_cash_runway_z2_8d_base_v097_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of cwr_runway for cash_runway
def f48cwr_cash_runway_pk2_8d_base_v098_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of cwr_runway for cash_runway
def f48cwr_cash_runway_roc2_8d_base_v099_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_diff_8d_base_v100_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmax_8d_base_v101_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmin_8d_base_v102_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_expz_8d_base_v103_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cwr_burn_rate at 8d for cash_runway
def f48cwr_cash_runway_sign_8d_base_v104_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_posfr_8d_base_v105_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_zscore_16d_base_v106_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_prank_16d_base_v107_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_roc_16d_base_v108_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d minmax of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_mnmx_16d_base_v109_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=_minmax(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling mean of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmean_16d_base_v110_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=raw.rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rstd_16d_base_v111_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=raw.rolling(16,min_periods=max(1,16//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of cwr_runway for cash_runway
def f48cwr_cash_runway_z2_16d_base_v112_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 16)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of cwr_runway for cash_runway
def f48cwr_cash_runway_pk2_16d_base_v113_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 16)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of cwr_runway for cash_runway
def f48cwr_cash_runway_roc2_16d_base_v114_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 16)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d diff of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_diff_16d_base_v115_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=raw.diff(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling max ratio of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmax_16d_base_v116_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    mx=raw.rolling(16,min_periods=max(1,16//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling min-std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmin_16d_base_v117_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    mn=raw.rolling(16,min_periods=max(1,16//2)).min()
    sd=raw.rolling(16,min_periods=max(1,16//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 16d) of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_expz_16d_base_v118_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    mu=raw.expanding(min_periods=16).mean()
    sd=raw.expanding(min_periods=16).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cwr_burn_rate at 16d for cash_runway
def f48cwr_cash_runway_sign_16d_base_v119_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d positive fraction of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_posfr_16d_base_v120_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 16)
    result=(raw>0).astype(float).rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_zscore_4d_base_v121_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_prank_4d_base_v122_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_roc_4d_base_v123_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_mnmx_4d_base_v124_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmean_4d_base_v125_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rstd_4d_base_v126_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of cwr_runway for cash_runway
def f48cwr_cash_runway_z2_4d_base_v127_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of cwr_runway for cash_runway
def f48cwr_cash_runway_pk2_4d_base_v128_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of cwr_runway for cash_runway
def f48cwr_cash_runway_roc2_4d_base_v129_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_diff_4d_base_v130_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmax_4d_base_v131_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmin_4d_base_v132_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_expz_4d_base_v133_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cwr_burn_rate at 4d for cash_runway
def f48cwr_cash_runway_sign_4d_base_v134_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_posfr_4d_base_v135_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 4)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_zscore_8d_base_v136_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_prank_8d_base_v137_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_roc_8d_base_v138_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_mnmx_8d_base_v139_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmean_8d_base_v140_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rstd_8d_base_v141_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of cwr_runway for cash_runway
def f48cwr_cash_runway_z2_8d_base_v142_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of cwr_runway for cash_runway
def f48cwr_cash_runway_pk2_8d_base_v143_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of cwr_runway for cash_runway
def f48cwr_cash_runway_roc2_8d_base_v144_signal(fcf, debt, ncfo):
    raw=_cwr_runway(fcf, debt, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_diff_8d_base_v145_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmax_8d_base_v146_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_rmin_8d_base_v147_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_expz_8d_base_v148_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cwr_burn_rate at 8d for cash_runway
def f48cwr_cash_runway_sign_8d_base_v149_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of cwr_burn_rate for cash_runway
def f48cwr_cash_runway_posfr_8d_base_v150_signal(fcf, debt, ncfo):
    raw=_cwr_burn_rate(ncfo, 8)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f48cwr_cash_runway_zscore_4d_base_v076_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_zscore_4d_base_v076_signal}, "f48cwr_cash_runway_prank_4d_base_v077_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_prank_4d_base_v077_signal}, "f48cwr_cash_runway_roc_4d_base_v078_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc_4d_base_v078_signal}, "f48cwr_cash_runway_mnmx_4d_base_v079_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_mnmx_4d_base_v079_signal}, "f48cwr_cash_runway_rmean_4d_base_v080_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmean_4d_base_v080_signal}, "f48cwr_cash_runway_rstd_4d_base_v081_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rstd_4d_base_v081_signal}, "f48cwr_cash_runway_z2_4d_base_v082_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_z2_4d_base_v082_signal}, "f48cwr_cash_runway_pk2_4d_base_v083_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_pk2_4d_base_v083_signal}, "f48cwr_cash_runway_roc2_4d_base_v084_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc2_4d_base_v084_signal}, "f48cwr_cash_runway_diff_4d_base_v085_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_diff_4d_base_v085_signal}, "f48cwr_cash_runway_rmax_4d_base_v086_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmax_4d_base_v086_signal}, "f48cwr_cash_runway_rmin_4d_base_v087_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmin_4d_base_v087_signal}, "f48cwr_cash_runway_expz_4d_base_v088_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_expz_4d_base_v088_signal}, "f48cwr_cash_runway_sign_4d_base_v089_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_sign_4d_base_v089_signal}, "f48cwr_cash_runway_posfr_4d_base_v090_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_posfr_4d_base_v090_signal}, "f48cwr_cash_runway_zscore_8d_base_v091_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_zscore_8d_base_v091_signal}, "f48cwr_cash_runway_prank_8d_base_v092_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_prank_8d_base_v092_signal}, "f48cwr_cash_runway_roc_8d_base_v093_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc_8d_base_v093_signal}, "f48cwr_cash_runway_mnmx_8d_base_v094_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_mnmx_8d_base_v094_signal}, "f48cwr_cash_runway_rmean_8d_base_v095_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmean_8d_base_v095_signal}, "f48cwr_cash_runway_rstd_8d_base_v096_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rstd_8d_base_v096_signal}, "f48cwr_cash_runway_z2_8d_base_v097_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_z2_8d_base_v097_signal}, "f48cwr_cash_runway_pk2_8d_base_v098_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_pk2_8d_base_v098_signal}, "f48cwr_cash_runway_roc2_8d_base_v099_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc2_8d_base_v099_signal}, "f48cwr_cash_runway_diff_8d_base_v100_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_diff_8d_base_v100_signal}, "f48cwr_cash_runway_rmax_8d_base_v101_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmax_8d_base_v101_signal}, "f48cwr_cash_runway_rmin_8d_base_v102_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmin_8d_base_v102_signal}, "f48cwr_cash_runway_expz_8d_base_v103_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_expz_8d_base_v103_signal}, "f48cwr_cash_runway_sign_8d_base_v104_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_sign_8d_base_v104_signal}, "f48cwr_cash_runway_posfr_8d_base_v105_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_posfr_8d_base_v105_signal}, "f48cwr_cash_runway_zscore_16d_base_v106_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_zscore_16d_base_v106_signal}, "f48cwr_cash_runway_prank_16d_base_v107_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_prank_16d_base_v107_signal}, "f48cwr_cash_runway_roc_16d_base_v108_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc_16d_base_v108_signal}, "f48cwr_cash_runway_mnmx_16d_base_v109_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_mnmx_16d_base_v109_signal}, "f48cwr_cash_runway_rmean_16d_base_v110_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmean_16d_base_v110_signal}, "f48cwr_cash_runway_rstd_16d_base_v111_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rstd_16d_base_v111_signal}, "f48cwr_cash_runway_z2_16d_base_v112_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_z2_16d_base_v112_signal}, "f48cwr_cash_runway_pk2_16d_base_v113_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_pk2_16d_base_v113_signal}, "f48cwr_cash_runway_roc2_16d_base_v114_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc2_16d_base_v114_signal}, "f48cwr_cash_runway_diff_16d_base_v115_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_diff_16d_base_v115_signal}, "f48cwr_cash_runway_rmax_16d_base_v116_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmax_16d_base_v116_signal}, "f48cwr_cash_runway_rmin_16d_base_v117_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmin_16d_base_v117_signal}, "f48cwr_cash_runway_expz_16d_base_v118_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_expz_16d_base_v118_signal}, "f48cwr_cash_runway_sign_16d_base_v119_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_sign_16d_base_v119_signal}, "f48cwr_cash_runway_posfr_16d_base_v120_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_posfr_16d_base_v120_signal}, "f48cwr_cash_runway_zscore_4d_base_v121_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_zscore_4d_base_v121_signal}, "f48cwr_cash_runway_prank_4d_base_v122_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_prank_4d_base_v122_signal}, "f48cwr_cash_runway_roc_4d_base_v123_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc_4d_base_v123_signal}, "f48cwr_cash_runway_mnmx_4d_base_v124_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_mnmx_4d_base_v124_signal}, "f48cwr_cash_runway_rmean_4d_base_v125_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmean_4d_base_v125_signal}, "f48cwr_cash_runway_rstd_4d_base_v126_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rstd_4d_base_v126_signal}, "f48cwr_cash_runway_z2_4d_base_v127_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_z2_4d_base_v127_signal}, "f48cwr_cash_runway_pk2_4d_base_v128_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_pk2_4d_base_v128_signal}, "f48cwr_cash_runway_roc2_4d_base_v129_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc2_4d_base_v129_signal}, "f48cwr_cash_runway_diff_4d_base_v130_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_diff_4d_base_v130_signal}, "f48cwr_cash_runway_rmax_4d_base_v131_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmax_4d_base_v131_signal}, "f48cwr_cash_runway_rmin_4d_base_v132_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmin_4d_base_v132_signal}, "f48cwr_cash_runway_expz_4d_base_v133_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_expz_4d_base_v133_signal}, "f48cwr_cash_runway_sign_4d_base_v134_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_sign_4d_base_v134_signal}, "f48cwr_cash_runway_posfr_4d_base_v135_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_posfr_4d_base_v135_signal}, "f48cwr_cash_runway_zscore_8d_base_v136_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_zscore_8d_base_v136_signal}, "f48cwr_cash_runway_prank_8d_base_v137_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_prank_8d_base_v137_signal}, "f48cwr_cash_runway_roc_8d_base_v138_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc_8d_base_v138_signal}, "f48cwr_cash_runway_mnmx_8d_base_v139_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_mnmx_8d_base_v139_signal}, "f48cwr_cash_runway_rmean_8d_base_v140_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmean_8d_base_v140_signal}, "f48cwr_cash_runway_rstd_8d_base_v141_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rstd_8d_base_v141_signal}, "f48cwr_cash_runway_z2_8d_base_v142_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_z2_8d_base_v142_signal}, "f48cwr_cash_runway_pk2_8d_base_v143_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_pk2_8d_base_v143_signal}, "f48cwr_cash_runway_roc2_8d_base_v144_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_roc2_8d_base_v144_signal}, "f48cwr_cash_runway_diff_8d_base_v145_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_diff_8d_base_v145_signal}, "f48cwr_cash_runway_rmax_8d_base_v146_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmax_8d_base_v146_signal}, "f48cwr_cash_runway_rmin_8d_base_v147_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_rmin_8d_base_v147_signal}, "f48cwr_cash_runway_expz_8d_base_v148_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_expz_8d_base_v148_signal}, "f48cwr_cash_runway_sign_8d_base_v149_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_sign_8d_base_v149_signal}, "f48cwr_cash_runway_posfr_8d_base_v150_signal": {"inputs": ['fcf', 'debt', 'ncfo'], "func": f48cwr_cash_runway_posfr_8d_base_v150_signal}}
F48_CASH_RUNWAY_REGISTRY_076_150 = REGISTRY

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