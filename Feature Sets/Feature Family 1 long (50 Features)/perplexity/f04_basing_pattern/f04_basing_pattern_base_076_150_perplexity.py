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

def _bsp_range_compression(high, low, w):
    rng = (high - low) / low.abs().replace(0, np.nan)
    return rng / rng.rolling(w, min_periods=max(1, w//2)).mean().replace(0, np.nan)
def _bsp_price_flatness(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w//2)).std() / closeadj.rolling(w, min_periods=max(1, w//2)).mean().abs().replace(0, np.nan)


# 21d z-score of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_zscore_21d_base_v076_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_prank_21d_base_v077_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_roc_21d_base_v078_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d minmax of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_mnmx_21d_base_v079_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=_minmax(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling mean of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmean_21d_base_v080_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rstd_21d_base_v081_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d z-score of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_z2_21d_base_v082_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_pk2_21d_base_v083_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_roc2_21d_base_v084_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_diff_21d_base_v085_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=raw.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling max ratio of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmax_21d_base_v086_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    mx=raw.rolling(21,min_periods=max(1,21//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling min-std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmin_21d_base_v087_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    mn=raw.rolling(21,min_periods=max(1,21//2)).min()
    sd=raw.rolling(21,min_periods=max(1,21//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 21d) of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_expz_21d_base_v088_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    mu=raw.expanding(min_periods=21).mean()
    sd=raw.expanding(min_periods=21).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of bsp_range_compression at 21d for basing_pattern
def f04bsp_basing_pattern_sign_21d_base_v089_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d positive fraction of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_posfr_21d_base_v090_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=(raw>0).astype(float).rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d z-score of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_zscore_63d_base_v091_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=_z(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d pctrank of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_prank_63d_base_v092_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=_prank(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d roc of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_roc_63d_base_v093_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=raw.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d minmax of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_mnmx_63d_base_v094_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=_minmax(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling mean of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmean_63d_base_v095_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=raw.rolling(63,min_periods=max(1,63//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rstd_63d_base_v096_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=raw.rolling(63,min_periods=max(1,63//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d z-score of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_z2_63d_base_v097_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 63)
    result=_z(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d pctrank of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_pk2_63d_base_v098_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 63)
    result=_prank(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d roc of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_roc2_63d_base_v099_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 63)
    result=raw.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d diff of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_diff_63d_base_v100_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=raw.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling max ratio of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmax_63d_base_v101_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    mx=raw.rolling(63,min_periods=max(1,63//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling min-std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmin_63d_base_v102_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    mn=raw.rolling(63,min_periods=max(1,63//2)).min()
    sd=raw.rolling(63,min_periods=max(1,63//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 63d) of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_expz_63d_base_v103_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    mu=raw.expanding(min_periods=63).mean()
    sd=raw.expanding(min_periods=63).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of bsp_range_compression at 63d for basing_pattern
def f04bsp_basing_pattern_sign_63d_base_v104_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d positive fraction of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_posfr_63d_base_v105_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=(raw>0).astype(float).rolling(63,min_periods=max(1,63//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d z-score of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_zscore_126d_base_v106_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=_z(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d pctrank of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_prank_126d_base_v107_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=_prank(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d roc of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_roc_126d_base_v108_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=raw.pct_change(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d minmax of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_mnmx_126d_base_v109_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=_minmax(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling mean of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmean_126d_base_v110_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=raw.rolling(126,min_periods=max(1,126//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rstd_126d_base_v111_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=raw.rolling(126,min_periods=max(1,126//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d z-score of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_z2_126d_base_v112_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 126)
    result=_z(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d pctrank of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_pk2_126d_base_v113_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 126)
    result=_prank(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d roc of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_roc2_126d_base_v114_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 126)
    result=raw.pct_change(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d diff of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_diff_126d_base_v115_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=raw.diff(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling max ratio of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmax_126d_base_v116_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    mx=raw.rolling(126,min_periods=max(1,126//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling min-std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmin_126d_base_v117_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    mn=raw.rolling(126,min_periods=max(1,126//2)).min()
    sd=raw.rolling(126,min_periods=max(1,126//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 126d) of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_expz_126d_base_v118_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    mu=raw.expanding(min_periods=126).mean()
    sd=raw.expanding(min_periods=126).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of bsp_range_compression at 126d for basing_pattern
def f04bsp_basing_pattern_sign_126d_base_v119_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d positive fraction of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_posfr_126d_base_v120_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 126)
    result=(raw>0).astype(float).rolling(126,min_periods=max(1,126//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d z-score of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_zscore_21d_base_v121_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_prank_21d_base_v122_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_roc_21d_base_v123_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d minmax of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_mnmx_21d_base_v124_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=_minmax(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling mean of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmean_21d_base_v125_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rstd_21d_base_v126_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d z-score of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_z2_21d_base_v127_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_pk2_21d_base_v128_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_roc2_21d_base_v129_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_diff_21d_base_v130_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=raw.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling max ratio of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmax_21d_base_v131_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    mx=raw.rolling(21,min_periods=max(1,21//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling min-std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmin_21d_base_v132_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    mn=raw.rolling(21,min_periods=max(1,21//2)).min()
    sd=raw.rolling(21,min_periods=max(1,21//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 21d) of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_expz_21d_base_v133_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    mu=raw.expanding(min_periods=21).mean()
    sd=raw.expanding(min_periods=21).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of bsp_range_compression at 21d for basing_pattern
def f04bsp_basing_pattern_sign_21d_base_v134_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d positive fraction of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_posfr_21d_base_v135_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 21)
    result=(raw>0).astype(float).rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d z-score of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_zscore_63d_base_v136_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=_z(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d pctrank of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_prank_63d_base_v137_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=_prank(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d roc of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_roc_63d_base_v138_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=raw.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d minmax of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_mnmx_63d_base_v139_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=_minmax(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling mean of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmean_63d_base_v140_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=raw.rolling(63,min_periods=max(1,63//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rstd_63d_base_v141_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=raw.rolling(63,min_periods=max(1,63//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d z-score of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_z2_63d_base_v142_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 63)
    result=_z(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d pctrank of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_pk2_63d_base_v143_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 63)
    result=_prank(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d roc of bsp_price_flatness for basing_pattern
def f04bsp_basing_pattern_roc2_63d_base_v144_signal(closeadj, high, low):
    raw=_bsp_price_flatness(closeadj, 63)
    result=raw.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d diff of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_diff_63d_base_v145_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=raw.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling max ratio of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmax_63d_base_v146_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    mx=raw.rolling(63,min_periods=max(1,63//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling min-std of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_rmin_63d_base_v147_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    mn=raw.rolling(63,min_periods=max(1,63//2)).min()
    sd=raw.rolling(63,min_periods=max(1,63//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 63d) of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_expz_63d_base_v148_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    mu=raw.expanding(min_periods=63).mean()
    sd=raw.expanding(min_periods=63).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of bsp_range_compression at 63d for basing_pattern
def f04bsp_basing_pattern_sign_63d_base_v149_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d positive fraction of bsp_range_compression for basing_pattern
def f04bsp_basing_pattern_posfr_63d_base_v150_signal(closeadj, high, low):
    raw=_bsp_range_compression(high, low, 63)
    result=(raw>0).astype(float).rolling(63,min_periods=max(1,63//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f04bsp_basing_pattern_zscore_21d_base_v076_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_zscore_21d_base_v076_signal}, "f04bsp_basing_pattern_prank_21d_base_v077_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_prank_21d_base_v077_signal}, "f04bsp_basing_pattern_roc_21d_base_v078_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc_21d_base_v078_signal}, "f04bsp_basing_pattern_mnmx_21d_base_v079_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_mnmx_21d_base_v079_signal}, "f04bsp_basing_pattern_rmean_21d_base_v080_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmean_21d_base_v080_signal}, "f04bsp_basing_pattern_rstd_21d_base_v081_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rstd_21d_base_v081_signal}, "f04bsp_basing_pattern_z2_21d_base_v082_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_z2_21d_base_v082_signal}, "f04bsp_basing_pattern_pk2_21d_base_v083_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_pk2_21d_base_v083_signal}, "f04bsp_basing_pattern_roc2_21d_base_v084_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc2_21d_base_v084_signal}, "f04bsp_basing_pattern_diff_21d_base_v085_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_diff_21d_base_v085_signal}, "f04bsp_basing_pattern_rmax_21d_base_v086_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmax_21d_base_v086_signal}, "f04bsp_basing_pattern_rmin_21d_base_v087_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmin_21d_base_v087_signal}, "f04bsp_basing_pattern_expz_21d_base_v088_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_expz_21d_base_v088_signal}, "f04bsp_basing_pattern_sign_21d_base_v089_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_sign_21d_base_v089_signal}, "f04bsp_basing_pattern_posfr_21d_base_v090_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_posfr_21d_base_v090_signal}, "f04bsp_basing_pattern_zscore_63d_base_v091_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_zscore_63d_base_v091_signal}, "f04bsp_basing_pattern_prank_63d_base_v092_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_prank_63d_base_v092_signal}, "f04bsp_basing_pattern_roc_63d_base_v093_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc_63d_base_v093_signal}, "f04bsp_basing_pattern_mnmx_63d_base_v094_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_mnmx_63d_base_v094_signal}, "f04bsp_basing_pattern_rmean_63d_base_v095_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmean_63d_base_v095_signal}, "f04bsp_basing_pattern_rstd_63d_base_v096_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rstd_63d_base_v096_signal}, "f04bsp_basing_pattern_z2_63d_base_v097_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_z2_63d_base_v097_signal}, "f04bsp_basing_pattern_pk2_63d_base_v098_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_pk2_63d_base_v098_signal}, "f04bsp_basing_pattern_roc2_63d_base_v099_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc2_63d_base_v099_signal}, "f04bsp_basing_pattern_diff_63d_base_v100_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_diff_63d_base_v100_signal}, "f04bsp_basing_pattern_rmax_63d_base_v101_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmax_63d_base_v101_signal}, "f04bsp_basing_pattern_rmin_63d_base_v102_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmin_63d_base_v102_signal}, "f04bsp_basing_pattern_expz_63d_base_v103_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_expz_63d_base_v103_signal}, "f04bsp_basing_pattern_sign_63d_base_v104_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_sign_63d_base_v104_signal}, "f04bsp_basing_pattern_posfr_63d_base_v105_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_posfr_63d_base_v105_signal}, "f04bsp_basing_pattern_zscore_126d_base_v106_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_zscore_126d_base_v106_signal}, "f04bsp_basing_pattern_prank_126d_base_v107_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_prank_126d_base_v107_signal}, "f04bsp_basing_pattern_roc_126d_base_v108_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc_126d_base_v108_signal}, "f04bsp_basing_pattern_mnmx_126d_base_v109_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_mnmx_126d_base_v109_signal}, "f04bsp_basing_pattern_rmean_126d_base_v110_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmean_126d_base_v110_signal}, "f04bsp_basing_pattern_rstd_126d_base_v111_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rstd_126d_base_v111_signal}, "f04bsp_basing_pattern_z2_126d_base_v112_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_z2_126d_base_v112_signal}, "f04bsp_basing_pattern_pk2_126d_base_v113_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_pk2_126d_base_v113_signal}, "f04bsp_basing_pattern_roc2_126d_base_v114_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc2_126d_base_v114_signal}, "f04bsp_basing_pattern_diff_126d_base_v115_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_diff_126d_base_v115_signal}, "f04bsp_basing_pattern_rmax_126d_base_v116_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmax_126d_base_v116_signal}, "f04bsp_basing_pattern_rmin_126d_base_v117_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmin_126d_base_v117_signal}, "f04bsp_basing_pattern_expz_126d_base_v118_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_expz_126d_base_v118_signal}, "f04bsp_basing_pattern_sign_126d_base_v119_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_sign_126d_base_v119_signal}, "f04bsp_basing_pattern_posfr_126d_base_v120_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_posfr_126d_base_v120_signal}, "f04bsp_basing_pattern_zscore_21d_base_v121_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_zscore_21d_base_v121_signal}, "f04bsp_basing_pattern_prank_21d_base_v122_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_prank_21d_base_v122_signal}, "f04bsp_basing_pattern_roc_21d_base_v123_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc_21d_base_v123_signal}, "f04bsp_basing_pattern_mnmx_21d_base_v124_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_mnmx_21d_base_v124_signal}, "f04bsp_basing_pattern_rmean_21d_base_v125_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmean_21d_base_v125_signal}, "f04bsp_basing_pattern_rstd_21d_base_v126_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rstd_21d_base_v126_signal}, "f04bsp_basing_pattern_z2_21d_base_v127_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_z2_21d_base_v127_signal}, "f04bsp_basing_pattern_pk2_21d_base_v128_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_pk2_21d_base_v128_signal}, "f04bsp_basing_pattern_roc2_21d_base_v129_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc2_21d_base_v129_signal}, "f04bsp_basing_pattern_diff_21d_base_v130_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_diff_21d_base_v130_signal}, "f04bsp_basing_pattern_rmax_21d_base_v131_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmax_21d_base_v131_signal}, "f04bsp_basing_pattern_rmin_21d_base_v132_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmin_21d_base_v132_signal}, "f04bsp_basing_pattern_expz_21d_base_v133_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_expz_21d_base_v133_signal}, "f04bsp_basing_pattern_sign_21d_base_v134_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_sign_21d_base_v134_signal}, "f04bsp_basing_pattern_posfr_21d_base_v135_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_posfr_21d_base_v135_signal}, "f04bsp_basing_pattern_zscore_63d_base_v136_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_zscore_63d_base_v136_signal}, "f04bsp_basing_pattern_prank_63d_base_v137_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_prank_63d_base_v137_signal}, "f04bsp_basing_pattern_roc_63d_base_v138_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc_63d_base_v138_signal}, "f04bsp_basing_pattern_mnmx_63d_base_v139_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_mnmx_63d_base_v139_signal}, "f04bsp_basing_pattern_rmean_63d_base_v140_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmean_63d_base_v140_signal}, "f04bsp_basing_pattern_rstd_63d_base_v141_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rstd_63d_base_v141_signal}, "f04bsp_basing_pattern_z2_63d_base_v142_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_z2_63d_base_v142_signal}, "f04bsp_basing_pattern_pk2_63d_base_v143_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_pk2_63d_base_v143_signal}, "f04bsp_basing_pattern_roc2_63d_base_v144_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_roc2_63d_base_v144_signal}, "f04bsp_basing_pattern_diff_63d_base_v145_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_diff_63d_base_v145_signal}, "f04bsp_basing_pattern_rmax_63d_base_v146_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmax_63d_base_v146_signal}, "f04bsp_basing_pattern_rmin_63d_base_v147_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_rmin_63d_base_v147_signal}, "f04bsp_basing_pattern_expz_63d_base_v148_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_expz_63d_base_v148_signal}, "f04bsp_basing_pattern_sign_63d_base_v149_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_sign_63d_base_v149_signal}, "f04bsp_basing_pattern_posfr_63d_base_v150_signal": {"inputs": ['closeadj', 'high', 'low'], "func": f04bsp_basing_pattern_posfr_63d_base_v150_signal}}
F04_BASING_PATTERN_REGISTRY_076_150 = REGISTRY

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