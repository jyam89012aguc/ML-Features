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

def _cdd_drawdown(closeadj, w):
    pk = closeadj.rolling(w, min_periods=max(1, w//2)).max()
    return (closeadj - pk) / pk.abs().replace(0, np.nan)
def _cdd_below_ma(closeadj, w):
    ma = closeadj.rolling(w, min_periods=max(1, w//2)).mean()
    return (closeadj < ma).astype(float)


# 21d z-score of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_zscore_21d_base_v001_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_prank_21d_base_v002_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_roc_21d_base_v003_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d minmax of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_mnmx_21d_base_v004_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=_minmax(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling mean of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmean_21d_base_v005_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rstd_21d_base_v006_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d z-score of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_z2_21d_base_v007_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_pk2_21d_base_v008_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_roc2_21d_base_v009_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_diff_21d_base_v010_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=raw.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling max ratio of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmax_21d_base_v011_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    mx=raw.rolling(21,min_periods=max(1,21//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling min-std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmin_21d_base_v012_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    mn=raw.rolling(21,min_periods=max(1,21//2)).min()
    sd=raw.rolling(21,min_periods=max(1,21//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 21d) of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_expz_21d_base_v013_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    mu=raw.expanding(min_periods=21).mean()
    sd=raw.expanding(min_periods=21).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cdd_drawdown at 21d for crash_depth_duration
def f03cdd_crash_depth_duration_sign_21d_base_v014_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d positive fraction of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_posfr_21d_base_v015_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=(raw>0).astype(float).rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d z-score of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_zscore_63d_base_v016_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=_z(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d pctrank of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_prank_63d_base_v017_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=_prank(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d roc of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_roc_63d_base_v018_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=raw.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d minmax of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_mnmx_63d_base_v019_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=_minmax(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling mean of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmean_63d_base_v020_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=raw.rolling(63,min_periods=max(1,63//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rstd_63d_base_v021_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=raw.rolling(63,min_periods=max(1,63//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d z-score of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_z2_63d_base_v022_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 63)
    result=_z(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d pctrank of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_pk2_63d_base_v023_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 63)
    result=_prank(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d roc of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_roc2_63d_base_v024_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 63)
    result=raw.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d diff of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_diff_63d_base_v025_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=raw.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling max ratio of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmax_63d_base_v026_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    mx=raw.rolling(63,min_periods=max(1,63//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling min-std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmin_63d_base_v027_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    mn=raw.rolling(63,min_periods=max(1,63//2)).min()
    sd=raw.rolling(63,min_periods=max(1,63//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 63d) of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_expz_63d_base_v028_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    mu=raw.expanding(min_periods=63).mean()
    sd=raw.expanding(min_periods=63).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cdd_drawdown at 63d for crash_depth_duration
def f03cdd_crash_depth_duration_sign_63d_base_v029_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d positive fraction of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_posfr_63d_base_v030_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 63)
    result=(raw>0).astype(float).rolling(63,min_periods=max(1,63//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d z-score of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_zscore_126d_base_v031_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=_z(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d pctrank of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_prank_126d_base_v032_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=_prank(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d roc of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_roc_126d_base_v033_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=raw.pct_change(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d minmax of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_mnmx_126d_base_v034_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=_minmax(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling mean of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmean_126d_base_v035_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=raw.rolling(126,min_periods=max(1,126//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rstd_126d_base_v036_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=raw.rolling(126,min_periods=max(1,126//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d z-score of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_z2_126d_base_v037_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 126)
    result=_z(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d pctrank of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_pk2_126d_base_v038_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 126)
    result=_prank(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d roc of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_roc2_126d_base_v039_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 126)
    result=raw.pct_change(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d diff of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_diff_126d_base_v040_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=raw.diff(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling max ratio of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmax_126d_base_v041_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    mx=raw.rolling(126,min_periods=max(1,126//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling min-std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmin_126d_base_v042_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    mn=raw.rolling(126,min_periods=max(1,126//2)).min()
    sd=raw.rolling(126,min_periods=max(1,126//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 126d) of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_expz_126d_base_v043_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    mu=raw.expanding(min_periods=126).mean()
    sd=raw.expanding(min_periods=126).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cdd_drawdown at 126d for crash_depth_duration
def f03cdd_crash_depth_duration_sign_126d_base_v044_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d positive fraction of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_posfr_126d_base_v045_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 126)
    result=(raw>0).astype(float).rolling(126,min_periods=max(1,126//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 252d z-score of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_zscore_252d_base_v046_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=_z(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d pctrank of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_prank_252d_base_v047_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=_prank(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d roc of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_roc_252d_base_v048_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=raw.pct_change(252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d minmax of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_mnmx_252d_base_v049_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=_minmax(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d rolling mean of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmean_252d_base_v050_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=raw.rolling(252,min_periods=max(1,252//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 252d rolling std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rstd_252d_base_v051_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=raw.rolling(252,min_periods=max(1,252//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 252d z-score of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_z2_252d_base_v052_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 252)
    result=_z(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d pctrank of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_pk2_252d_base_v053_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 252)
    result=_prank(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d roc of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_roc2_252d_base_v054_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 252)
    result=raw.pct_change(252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d diff of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_diff_252d_base_v055_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=raw.diff(252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d rolling max ratio of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmax_252d_base_v056_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    mx=raw.rolling(252,min_periods=max(1,252//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 252d rolling min-std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmin_252d_base_v057_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    mn=raw.rolling(252,min_periods=max(1,252//2)).min()
    sd=raw.rolling(252,min_periods=max(1,252//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 252d) of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_expz_252d_base_v058_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    mu=raw.expanding(min_periods=252).mean()
    sd=raw.expanding(min_periods=252).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cdd_drawdown at 252d for crash_depth_duration
def f03cdd_crash_depth_duration_sign_252d_base_v059_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d positive fraction of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_posfr_252d_base_v060_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 252)
    result=(raw>0).astype(float).rolling(252,min_periods=max(1,252//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d z-score of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_zscore_21d_base_v061_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_prank_21d_base_v062_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_roc_21d_base_v063_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d minmax of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_mnmx_21d_base_v064_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=_minmax(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling mean of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmean_21d_base_v065_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rstd_21d_base_v066_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d z-score of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_z2_21d_base_v067_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_pk2_21d_base_v068_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of cdd_below_ma for crash_depth_duration
def f03cdd_crash_depth_duration_roc2_21d_base_v069_signal(closeadj):
    raw=_cdd_below_ma(closeadj, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_diff_21d_base_v070_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=raw.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling max ratio of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmax_21d_base_v071_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    mx=raw.rolling(21,min_periods=max(1,21//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling min-std of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_rmin_21d_base_v072_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    mn=raw.rolling(21,min_periods=max(1,21//2)).min()
    sd=raw.rolling(21,min_periods=max(1,21//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 21d) of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_expz_21d_base_v073_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    mu=raw.expanding(min_periods=21).mean()
    sd=raw.expanding(min_periods=21).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of cdd_drawdown at 21d for crash_depth_duration
def f03cdd_crash_depth_duration_sign_21d_base_v074_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d positive fraction of cdd_drawdown for crash_depth_duration
def f03cdd_crash_depth_duration_posfr_21d_base_v075_signal(closeadj):
    raw=_cdd_drawdown(closeadj, 21)
    result=(raw>0).astype(float).rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f03cdd_crash_depth_duration_zscore_21d_base_v001_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_zscore_21d_base_v001_signal}, "f03cdd_crash_depth_duration_prank_21d_base_v002_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_prank_21d_base_v002_signal}, "f03cdd_crash_depth_duration_roc_21d_base_v003_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc_21d_base_v003_signal}, "f03cdd_crash_depth_duration_mnmx_21d_base_v004_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_mnmx_21d_base_v004_signal}, "f03cdd_crash_depth_duration_rmean_21d_base_v005_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmean_21d_base_v005_signal}, "f03cdd_crash_depth_duration_rstd_21d_base_v006_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rstd_21d_base_v006_signal}, "f03cdd_crash_depth_duration_z2_21d_base_v007_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_z2_21d_base_v007_signal}, "f03cdd_crash_depth_duration_pk2_21d_base_v008_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_pk2_21d_base_v008_signal}, "f03cdd_crash_depth_duration_roc2_21d_base_v009_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc2_21d_base_v009_signal}, "f03cdd_crash_depth_duration_diff_21d_base_v010_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_diff_21d_base_v010_signal}, "f03cdd_crash_depth_duration_rmax_21d_base_v011_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmax_21d_base_v011_signal}, "f03cdd_crash_depth_duration_rmin_21d_base_v012_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmin_21d_base_v012_signal}, "f03cdd_crash_depth_duration_expz_21d_base_v013_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_expz_21d_base_v013_signal}, "f03cdd_crash_depth_duration_sign_21d_base_v014_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_sign_21d_base_v014_signal}, "f03cdd_crash_depth_duration_posfr_21d_base_v015_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_posfr_21d_base_v015_signal}, "f03cdd_crash_depth_duration_zscore_63d_base_v016_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_zscore_63d_base_v016_signal}, "f03cdd_crash_depth_duration_prank_63d_base_v017_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_prank_63d_base_v017_signal}, "f03cdd_crash_depth_duration_roc_63d_base_v018_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc_63d_base_v018_signal}, "f03cdd_crash_depth_duration_mnmx_63d_base_v019_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_mnmx_63d_base_v019_signal}, "f03cdd_crash_depth_duration_rmean_63d_base_v020_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmean_63d_base_v020_signal}, "f03cdd_crash_depth_duration_rstd_63d_base_v021_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rstd_63d_base_v021_signal}, "f03cdd_crash_depth_duration_z2_63d_base_v022_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_z2_63d_base_v022_signal}, "f03cdd_crash_depth_duration_pk2_63d_base_v023_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_pk2_63d_base_v023_signal}, "f03cdd_crash_depth_duration_roc2_63d_base_v024_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc2_63d_base_v024_signal}, "f03cdd_crash_depth_duration_diff_63d_base_v025_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_diff_63d_base_v025_signal}, "f03cdd_crash_depth_duration_rmax_63d_base_v026_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmax_63d_base_v026_signal}, "f03cdd_crash_depth_duration_rmin_63d_base_v027_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmin_63d_base_v027_signal}, "f03cdd_crash_depth_duration_expz_63d_base_v028_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_expz_63d_base_v028_signal}, "f03cdd_crash_depth_duration_sign_63d_base_v029_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_sign_63d_base_v029_signal}, "f03cdd_crash_depth_duration_posfr_63d_base_v030_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_posfr_63d_base_v030_signal}, "f03cdd_crash_depth_duration_zscore_126d_base_v031_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_zscore_126d_base_v031_signal}, "f03cdd_crash_depth_duration_prank_126d_base_v032_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_prank_126d_base_v032_signal}, "f03cdd_crash_depth_duration_roc_126d_base_v033_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc_126d_base_v033_signal}, "f03cdd_crash_depth_duration_mnmx_126d_base_v034_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_mnmx_126d_base_v034_signal}, "f03cdd_crash_depth_duration_rmean_126d_base_v035_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmean_126d_base_v035_signal}, "f03cdd_crash_depth_duration_rstd_126d_base_v036_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rstd_126d_base_v036_signal}, "f03cdd_crash_depth_duration_z2_126d_base_v037_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_z2_126d_base_v037_signal}, "f03cdd_crash_depth_duration_pk2_126d_base_v038_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_pk2_126d_base_v038_signal}, "f03cdd_crash_depth_duration_roc2_126d_base_v039_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc2_126d_base_v039_signal}, "f03cdd_crash_depth_duration_diff_126d_base_v040_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_diff_126d_base_v040_signal}, "f03cdd_crash_depth_duration_rmax_126d_base_v041_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmax_126d_base_v041_signal}, "f03cdd_crash_depth_duration_rmin_126d_base_v042_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmin_126d_base_v042_signal}, "f03cdd_crash_depth_duration_expz_126d_base_v043_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_expz_126d_base_v043_signal}, "f03cdd_crash_depth_duration_sign_126d_base_v044_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_sign_126d_base_v044_signal}, "f03cdd_crash_depth_duration_posfr_126d_base_v045_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_posfr_126d_base_v045_signal}, "f03cdd_crash_depth_duration_zscore_252d_base_v046_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_zscore_252d_base_v046_signal}, "f03cdd_crash_depth_duration_prank_252d_base_v047_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_prank_252d_base_v047_signal}, "f03cdd_crash_depth_duration_roc_252d_base_v048_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc_252d_base_v048_signal}, "f03cdd_crash_depth_duration_mnmx_252d_base_v049_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_mnmx_252d_base_v049_signal}, "f03cdd_crash_depth_duration_rmean_252d_base_v050_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmean_252d_base_v050_signal}, "f03cdd_crash_depth_duration_rstd_252d_base_v051_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rstd_252d_base_v051_signal}, "f03cdd_crash_depth_duration_z2_252d_base_v052_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_z2_252d_base_v052_signal}, "f03cdd_crash_depth_duration_pk2_252d_base_v053_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_pk2_252d_base_v053_signal}, "f03cdd_crash_depth_duration_roc2_252d_base_v054_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc2_252d_base_v054_signal}, "f03cdd_crash_depth_duration_diff_252d_base_v055_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_diff_252d_base_v055_signal}, "f03cdd_crash_depth_duration_rmax_252d_base_v056_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmax_252d_base_v056_signal}, "f03cdd_crash_depth_duration_rmin_252d_base_v057_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmin_252d_base_v057_signal}, "f03cdd_crash_depth_duration_expz_252d_base_v058_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_expz_252d_base_v058_signal}, "f03cdd_crash_depth_duration_sign_252d_base_v059_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_sign_252d_base_v059_signal}, "f03cdd_crash_depth_duration_posfr_252d_base_v060_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_posfr_252d_base_v060_signal}, "f03cdd_crash_depth_duration_zscore_21d_base_v061_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_zscore_21d_base_v061_signal}, "f03cdd_crash_depth_duration_prank_21d_base_v062_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_prank_21d_base_v062_signal}, "f03cdd_crash_depth_duration_roc_21d_base_v063_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc_21d_base_v063_signal}, "f03cdd_crash_depth_duration_mnmx_21d_base_v064_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_mnmx_21d_base_v064_signal}, "f03cdd_crash_depth_duration_rmean_21d_base_v065_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmean_21d_base_v065_signal}, "f03cdd_crash_depth_duration_rstd_21d_base_v066_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rstd_21d_base_v066_signal}, "f03cdd_crash_depth_duration_z2_21d_base_v067_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_z2_21d_base_v067_signal}, "f03cdd_crash_depth_duration_pk2_21d_base_v068_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_pk2_21d_base_v068_signal}, "f03cdd_crash_depth_duration_roc2_21d_base_v069_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_roc2_21d_base_v069_signal}, "f03cdd_crash_depth_duration_diff_21d_base_v070_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_diff_21d_base_v070_signal}, "f03cdd_crash_depth_duration_rmax_21d_base_v071_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmax_21d_base_v071_signal}, "f03cdd_crash_depth_duration_rmin_21d_base_v072_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_rmin_21d_base_v072_signal}, "f03cdd_crash_depth_duration_expz_21d_base_v073_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_expz_21d_base_v073_signal}, "f03cdd_crash_depth_duration_sign_21d_base_v074_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_sign_21d_base_v074_signal}, "f03cdd_crash_depth_duration_posfr_21d_base_v075_signal": {"inputs": ['closeadj'], "func": f03cdd_crash_depth_duration_posfr_21d_base_v075_signal}}
F03_CRASH_DEPTH_DURATION_REGISTRY_001_075 = REGISTRY

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