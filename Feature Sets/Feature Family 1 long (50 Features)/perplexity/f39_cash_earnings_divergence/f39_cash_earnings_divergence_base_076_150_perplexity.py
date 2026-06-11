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

def _ced_gap(fcf, netinc):
    return fcf - netinc
def _ced_gap_z(fcf, netinc, w):
    return _z(_ced_gap(fcf, netinc), w)


# 4d z-score of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_zscore_4d_base_v076_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_prank_4d_base_v077_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc_4d_base_v078_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d minmax of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_mnmx_4d_base_v079_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_minmax(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling mean of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmean_4d_base_v080_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rstd_4d_base_v081_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(4,min_periods=max(1,4//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 4d z-score of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_z2_4d_base_v082_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 4)
    result=_z(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d pctrank of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_pk2_4d_base_v083_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 4)
    result=_prank(raw,4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d roc of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc2_4d_base_v084_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 4)
    result=raw.pct_change(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d diff of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_diff_4d_base_v085_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.diff(4)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling max ratio of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmax_4d_base_v086_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mx=raw.rolling(4,min_periods=max(1,4//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 4d rolling min-std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmin_4d_base_v087_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mn=raw.rolling(4,min_periods=max(1,4//2)).min()
    sd=raw.rolling(4,min_periods=max(1,4//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 4d) of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_expz_4d_base_v088_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mu=raw.expanding(min_periods=4).mean()
    sd=raw.expanding(min_periods=4).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of ced_gap at 4d for cash_earnings_divergence
def f39ced_cash_earnings_divergence_sign_4d_base_v089_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 4d positive fraction of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_posfr_4d_base_v090_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=(raw>0).astype(float).rolling(4,min_periods=max(1,4//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_zscore_8d_base_v091_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_prank_8d_base_v092_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc_8d_base_v093_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d minmax of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_mnmx_8d_base_v094_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_minmax(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling mean of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmean_8d_base_v095_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rstd_8d_base_v096_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(8,min_periods=max(1,8//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 8d z-score of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_z2_8d_base_v097_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 8)
    result=_z(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d pctrank of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_pk2_8d_base_v098_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 8)
    result=_prank(raw,8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d roc of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc2_8d_base_v099_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 8)
    result=raw.pct_change(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d diff of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_diff_8d_base_v100_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.diff(8)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling max ratio of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmax_8d_base_v101_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mx=raw.rolling(8,min_periods=max(1,8//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 8d rolling min-std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmin_8d_base_v102_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mn=raw.rolling(8,min_periods=max(1,8//2)).min()
    sd=raw.rolling(8,min_periods=max(1,8//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 8d) of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_expz_8d_base_v103_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mu=raw.expanding(min_periods=8).mean()
    sd=raw.expanding(min_periods=8).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of ced_gap at 8d for cash_earnings_divergence
def f39ced_cash_earnings_divergence_sign_8d_base_v104_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 8d positive fraction of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_posfr_8d_base_v105_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=(raw>0).astype(float).rolling(8,min_periods=max(1,8//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 12d z-score of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_zscore_12d_base_v106_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_z(raw,12)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d pctrank of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_prank_12d_base_v107_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_prank(raw,12)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d roc of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc_12d_base_v108_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.pct_change(12)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d minmax of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_mnmx_12d_base_v109_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_minmax(raw,12)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d rolling mean of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmean_12d_base_v110_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(12,min_periods=max(1,12//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 12d rolling std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rstd_12d_base_v111_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(12,min_periods=max(1,12//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 12d z-score of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_z2_12d_base_v112_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 12)
    result=_z(raw,12)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d pctrank of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_pk2_12d_base_v113_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 12)
    result=_prank(raw,12)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d roc of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc2_12d_base_v114_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 12)
    result=raw.pct_change(12)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d diff of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_diff_12d_base_v115_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.diff(12)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d rolling max ratio of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmax_12d_base_v116_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mx=raw.rolling(12,min_periods=max(1,12//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 12d rolling min-std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmin_12d_base_v117_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mn=raw.rolling(12,min_periods=max(1,12//2)).min()
    sd=raw.rolling(12,min_periods=max(1,12//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 12d) of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_expz_12d_base_v118_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mu=raw.expanding(min_periods=12).mean()
    sd=raw.expanding(min_periods=12).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of ced_gap at 12d for cash_earnings_divergence
def f39ced_cash_earnings_divergence_sign_12d_base_v119_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 12d positive fraction of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_posfr_12d_base_v120_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=(raw>0).astype(float).rolling(12,min_periods=max(1,12//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_zscore_16d_base_v121_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_prank_16d_base_v122_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc_16d_base_v123_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d minmax of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_mnmx_16d_base_v124_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_minmax(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling mean of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmean_16d_base_v125_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rstd_16d_base_v126_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(16,min_periods=max(1,16//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 16d z-score of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_z2_16d_base_v127_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 16)
    result=_z(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d pctrank of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_pk2_16d_base_v128_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 16)
    result=_prank(raw,16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d roc of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc2_16d_base_v129_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 16)
    result=raw.pct_change(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d diff of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_diff_16d_base_v130_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.diff(16)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling max ratio of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmax_16d_base_v131_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mx=raw.rolling(16,min_periods=max(1,16//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 16d rolling min-std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmin_16d_base_v132_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mn=raw.rolling(16,min_periods=max(1,16//2)).min()
    sd=raw.rolling(16,min_periods=max(1,16//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 16d) of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_expz_16d_base_v133_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mu=raw.expanding(min_periods=16).mean()
    sd=raw.expanding(min_periods=16).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of ced_gap at 16d for cash_earnings_divergence
def f39ced_cash_earnings_divergence_sign_16d_base_v134_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 16d positive fraction of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_posfr_16d_base_v135_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=(raw>0).astype(float).rolling(16,min_periods=max(1,16//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 24d z-score of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_zscore_24d_base_v136_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_z(raw,24)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d pctrank of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_prank_24d_base_v137_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_prank(raw,24)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d roc of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc_24d_base_v138_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.pct_change(24)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d minmax of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_mnmx_24d_base_v139_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=_minmax(raw,24)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d rolling mean of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmean_24d_base_v140_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(24,min_periods=max(1,24//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 24d rolling std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rstd_24d_base_v141_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.rolling(24,min_periods=max(1,24//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 24d z-score of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_z2_24d_base_v142_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 24)
    result=_z(raw,24)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d pctrank of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_pk2_24d_base_v143_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 24)
    result=_prank(raw,24)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d roc of ced_gap_z for cash_earnings_divergence
def f39ced_cash_earnings_divergence_roc2_24d_base_v144_signal(fcf, netinc):
    raw=_ced_gap_z(fcf, netinc, 24)
    result=raw.pct_change(24)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d diff of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_diff_24d_base_v145_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=raw.diff(24)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d rolling max ratio of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmax_24d_base_v146_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mx=raw.rolling(24,min_periods=max(1,24//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 24d rolling min-std of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_rmin_24d_base_v147_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mn=raw.rolling(24,min_periods=max(1,24//2)).min()
    sd=raw.rolling(24,min_periods=max(1,24//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 24d) of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_expz_24d_base_v148_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    mu=raw.expanding(min_periods=24).mean()
    sd=raw.expanding(min_periods=24).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of ced_gap at 24d for cash_earnings_divergence
def f39ced_cash_earnings_divergence_sign_24d_base_v149_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 24d positive fraction of ced_gap for cash_earnings_divergence
def f39ced_cash_earnings_divergence_posfr_24d_base_v150_signal(fcf, netinc):
    raw=_ced_gap(fcf, netinc)
    result=(raw>0).astype(float).rolling(24,min_periods=max(1,24//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f39ced_cash_earnings_divergence_zscore_4d_base_v076_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_zscore_4d_base_v076_signal}, "f39ced_cash_earnings_divergence_prank_4d_base_v077_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_prank_4d_base_v077_signal}, "f39ced_cash_earnings_divergence_roc_4d_base_v078_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc_4d_base_v078_signal}, "f39ced_cash_earnings_divergence_mnmx_4d_base_v079_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_mnmx_4d_base_v079_signal}, "f39ced_cash_earnings_divergence_rmean_4d_base_v080_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmean_4d_base_v080_signal}, "f39ced_cash_earnings_divergence_rstd_4d_base_v081_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rstd_4d_base_v081_signal}, "f39ced_cash_earnings_divergence_z2_4d_base_v082_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_z2_4d_base_v082_signal}, "f39ced_cash_earnings_divergence_pk2_4d_base_v083_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_pk2_4d_base_v083_signal}, "f39ced_cash_earnings_divergence_roc2_4d_base_v084_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc2_4d_base_v084_signal}, "f39ced_cash_earnings_divergence_diff_4d_base_v085_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_diff_4d_base_v085_signal}, "f39ced_cash_earnings_divergence_rmax_4d_base_v086_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmax_4d_base_v086_signal}, "f39ced_cash_earnings_divergence_rmin_4d_base_v087_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmin_4d_base_v087_signal}, "f39ced_cash_earnings_divergence_expz_4d_base_v088_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_expz_4d_base_v088_signal}, "f39ced_cash_earnings_divergence_sign_4d_base_v089_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_sign_4d_base_v089_signal}, "f39ced_cash_earnings_divergence_posfr_4d_base_v090_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_posfr_4d_base_v090_signal}, "f39ced_cash_earnings_divergence_zscore_8d_base_v091_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_zscore_8d_base_v091_signal}, "f39ced_cash_earnings_divergence_prank_8d_base_v092_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_prank_8d_base_v092_signal}, "f39ced_cash_earnings_divergence_roc_8d_base_v093_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc_8d_base_v093_signal}, "f39ced_cash_earnings_divergence_mnmx_8d_base_v094_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_mnmx_8d_base_v094_signal}, "f39ced_cash_earnings_divergence_rmean_8d_base_v095_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmean_8d_base_v095_signal}, "f39ced_cash_earnings_divergence_rstd_8d_base_v096_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rstd_8d_base_v096_signal}, "f39ced_cash_earnings_divergence_z2_8d_base_v097_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_z2_8d_base_v097_signal}, "f39ced_cash_earnings_divergence_pk2_8d_base_v098_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_pk2_8d_base_v098_signal}, "f39ced_cash_earnings_divergence_roc2_8d_base_v099_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc2_8d_base_v099_signal}, "f39ced_cash_earnings_divergence_diff_8d_base_v100_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_diff_8d_base_v100_signal}, "f39ced_cash_earnings_divergence_rmax_8d_base_v101_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmax_8d_base_v101_signal}, "f39ced_cash_earnings_divergence_rmin_8d_base_v102_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmin_8d_base_v102_signal}, "f39ced_cash_earnings_divergence_expz_8d_base_v103_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_expz_8d_base_v103_signal}, "f39ced_cash_earnings_divergence_sign_8d_base_v104_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_sign_8d_base_v104_signal}, "f39ced_cash_earnings_divergence_posfr_8d_base_v105_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_posfr_8d_base_v105_signal}, "f39ced_cash_earnings_divergence_zscore_12d_base_v106_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_zscore_12d_base_v106_signal}, "f39ced_cash_earnings_divergence_prank_12d_base_v107_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_prank_12d_base_v107_signal}, "f39ced_cash_earnings_divergence_roc_12d_base_v108_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc_12d_base_v108_signal}, "f39ced_cash_earnings_divergence_mnmx_12d_base_v109_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_mnmx_12d_base_v109_signal}, "f39ced_cash_earnings_divergence_rmean_12d_base_v110_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmean_12d_base_v110_signal}, "f39ced_cash_earnings_divergence_rstd_12d_base_v111_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rstd_12d_base_v111_signal}, "f39ced_cash_earnings_divergence_z2_12d_base_v112_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_z2_12d_base_v112_signal}, "f39ced_cash_earnings_divergence_pk2_12d_base_v113_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_pk2_12d_base_v113_signal}, "f39ced_cash_earnings_divergence_roc2_12d_base_v114_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc2_12d_base_v114_signal}, "f39ced_cash_earnings_divergence_diff_12d_base_v115_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_diff_12d_base_v115_signal}, "f39ced_cash_earnings_divergence_rmax_12d_base_v116_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmax_12d_base_v116_signal}, "f39ced_cash_earnings_divergence_rmin_12d_base_v117_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmin_12d_base_v117_signal}, "f39ced_cash_earnings_divergence_expz_12d_base_v118_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_expz_12d_base_v118_signal}, "f39ced_cash_earnings_divergence_sign_12d_base_v119_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_sign_12d_base_v119_signal}, "f39ced_cash_earnings_divergence_posfr_12d_base_v120_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_posfr_12d_base_v120_signal}, "f39ced_cash_earnings_divergence_zscore_16d_base_v121_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_zscore_16d_base_v121_signal}, "f39ced_cash_earnings_divergence_prank_16d_base_v122_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_prank_16d_base_v122_signal}, "f39ced_cash_earnings_divergence_roc_16d_base_v123_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc_16d_base_v123_signal}, "f39ced_cash_earnings_divergence_mnmx_16d_base_v124_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_mnmx_16d_base_v124_signal}, "f39ced_cash_earnings_divergence_rmean_16d_base_v125_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmean_16d_base_v125_signal}, "f39ced_cash_earnings_divergence_rstd_16d_base_v126_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rstd_16d_base_v126_signal}, "f39ced_cash_earnings_divergence_z2_16d_base_v127_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_z2_16d_base_v127_signal}, "f39ced_cash_earnings_divergence_pk2_16d_base_v128_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_pk2_16d_base_v128_signal}, "f39ced_cash_earnings_divergence_roc2_16d_base_v129_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc2_16d_base_v129_signal}, "f39ced_cash_earnings_divergence_diff_16d_base_v130_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_diff_16d_base_v130_signal}, "f39ced_cash_earnings_divergence_rmax_16d_base_v131_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmax_16d_base_v131_signal}, "f39ced_cash_earnings_divergence_rmin_16d_base_v132_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmin_16d_base_v132_signal}, "f39ced_cash_earnings_divergence_expz_16d_base_v133_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_expz_16d_base_v133_signal}, "f39ced_cash_earnings_divergence_sign_16d_base_v134_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_sign_16d_base_v134_signal}, "f39ced_cash_earnings_divergence_posfr_16d_base_v135_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_posfr_16d_base_v135_signal}, "f39ced_cash_earnings_divergence_zscore_24d_base_v136_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_zscore_24d_base_v136_signal}, "f39ced_cash_earnings_divergence_prank_24d_base_v137_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_prank_24d_base_v137_signal}, "f39ced_cash_earnings_divergence_roc_24d_base_v138_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc_24d_base_v138_signal}, "f39ced_cash_earnings_divergence_mnmx_24d_base_v139_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_mnmx_24d_base_v139_signal}, "f39ced_cash_earnings_divergence_rmean_24d_base_v140_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmean_24d_base_v140_signal}, "f39ced_cash_earnings_divergence_rstd_24d_base_v141_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rstd_24d_base_v141_signal}, "f39ced_cash_earnings_divergence_z2_24d_base_v142_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_z2_24d_base_v142_signal}, "f39ced_cash_earnings_divergence_pk2_24d_base_v143_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_pk2_24d_base_v143_signal}, "f39ced_cash_earnings_divergence_roc2_24d_base_v144_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_roc2_24d_base_v144_signal}, "f39ced_cash_earnings_divergence_diff_24d_base_v145_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_diff_24d_base_v145_signal}, "f39ced_cash_earnings_divergence_rmax_24d_base_v146_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmax_24d_base_v146_signal}, "f39ced_cash_earnings_divergence_rmin_24d_base_v147_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_rmin_24d_base_v147_signal}, "f39ced_cash_earnings_divergence_expz_24d_base_v148_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_expz_24d_base_v148_signal}, "f39ced_cash_earnings_divergence_sign_24d_base_v149_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_sign_24d_base_v149_signal}, "f39ced_cash_earnings_divergence_posfr_24d_base_v150_signal": {"inputs": ['fcf', 'netinc'], "func": f39ced_cash_earnings_divergence_posfr_24d_base_v150_signal}}
F39_CASH_EARNINGS_DIVERGENCE_REGISTRY_076_150 = REGISTRY

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