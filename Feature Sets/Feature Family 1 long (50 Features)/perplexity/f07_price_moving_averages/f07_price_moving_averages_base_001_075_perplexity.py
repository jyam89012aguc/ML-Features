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

def _pma_sma(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w//2)).mean()
def _pma_price_vs_sma(closeadj, w):
    return (closeadj - _pma_sma(closeadj, w)) / _pma_sma(closeadj, w).abs().replace(0, np.nan)


# 5d z-score of pma_sma for price_moving_averages
def f07pma_price_moving_averages_zscore_5d_base_v001_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=_z(raw,5)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pctrank of pma_sma for price_moving_averages
def f07pma_price_moving_averages_prank_5d_base_v002_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=_prank(raw,5)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d roc of pma_sma for price_moving_averages
def f07pma_price_moving_averages_roc_5d_base_v003_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=raw.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d minmax of pma_sma for price_moving_averages
def f07pma_price_moving_averages_mnmx_5d_base_v004_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=_minmax(raw,5)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d rolling mean of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmean_5d_base_v005_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=raw.rolling(5,min_periods=max(1,5//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 5d rolling std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rstd_5d_base_v006_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=raw.rolling(5,min_periods=max(1,5//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 5d z-score of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_z2_5d_base_v007_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 5)
    result=_z(raw,5)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d pctrank of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_pk2_5d_base_v008_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 5)
    result=_prank(raw,5)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d roc of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_roc2_5d_base_v009_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 5)
    result=raw.pct_change(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d diff of pma_sma for price_moving_averages
def f07pma_price_moving_averages_diff_5d_base_v010_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=raw.diff(5)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d rolling max ratio of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmax_5d_base_v011_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    mx=raw.rolling(5,min_periods=max(1,5//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 5d rolling min-std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmin_5d_base_v012_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    mn=raw.rolling(5,min_periods=max(1,5//2)).min()
    sd=raw.rolling(5,min_periods=max(1,5//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 5d) of pma_sma for price_moving_averages
def f07pma_price_moving_averages_expz_5d_base_v013_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    mu=raw.expanding(min_periods=5).mean()
    sd=raw.expanding(min_periods=5).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of pma_sma at 5d for price_moving_averages
def f07pma_price_moving_averages_sign_5d_base_v014_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 5d positive fraction of pma_sma for price_moving_averages
def f07pma_price_moving_averages_posfr_5d_base_v015_signal(closeadj):
    raw=_pma_sma(closeadj, 5)
    result=(raw>0).astype(float).rolling(5,min_periods=max(1,5//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d z-score of pma_sma for price_moving_averages
def f07pma_price_moving_averages_zscore_21d_base_v016_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of pma_sma for price_moving_averages
def f07pma_price_moving_averages_prank_21d_base_v017_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of pma_sma for price_moving_averages
def f07pma_price_moving_averages_roc_21d_base_v018_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d minmax of pma_sma for price_moving_averages
def f07pma_price_moving_averages_mnmx_21d_base_v019_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=_minmax(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling mean of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmean_21d_base_v020_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rstd_21d_base_v021_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=raw.rolling(21,min_periods=max(1,21//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 21d z-score of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_z2_21d_base_v022_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 21)
    result=_z(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d pctrank of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_pk2_21d_base_v023_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 21)
    result=_prank(raw,21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d roc of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_roc2_21d_base_v024_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 21)
    result=raw.pct_change(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d diff of pma_sma for price_moving_averages
def f07pma_price_moving_averages_diff_21d_base_v025_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=raw.diff(21)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling max ratio of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmax_21d_base_v026_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    mx=raw.rolling(21,min_periods=max(1,21//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 21d rolling min-std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmin_21d_base_v027_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    mn=raw.rolling(21,min_periods=max(1,21//2)).min()
    sd=raw.rolling(21,min_periods=max(1,21//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 21d) of pma_sma for price_moving_averages
def f07pma_price_moving_averages_expz_21d_base_v028_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    mu=raw.expanding(min_periods=21).mean()
    sd=raw.expanding(min_periods=21).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of pma_sma at 21d for price_moving_averages
def f07pma_price_moving_averages_sign_21d_base_v029_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 21d positive fraction of pma_sma for price_moving_averages
def f07pma_price_moving_averages_posfr_21d_base_v030_signal(closeadj):
    raw=_pma_sma(closeadj, 21)
    result=(raw>0).astype(float).rolling(21,min_periods=max(1,21//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d z-score of pma_sma for price_moving_averages
def f07pma_price_moving_averages_zscore_63d_base_v031_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=_z(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d pctrank of pma_sma for price_moving_averages
def f07pma_price_moving_averages_prank_63d_base_v032_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=_prank(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d roc of pma_sma for price_moving_averages
def f07pma_price_moving_averages_roc_63d_base_v033_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=raw.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d minmax of pma_sma for price_moving_averages
def f07pma_price_moving_averages_mnmx_63d_base_v034_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=_minmax(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling mean of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmean_63d_base_v035_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=raw.rolling(63,min_periods=max(1,63//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rstd_63d_base_v036_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=raw.rolling(63,min_periods=max(1,63//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 63d z-score of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_z2_63d_base_v037_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 63)
    result=_z(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d pctrank of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_pk2_63d_base_v038_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 63)
    result=_prank(raw,63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d roc of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_roc2_63d_base_v039_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 63)
    result=raw.pct_change(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d diff of pma_sma for price_moving_averages
def f07pma_price_moving_averages_diff_63d_base_v040_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=raw.diff(63)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling max ratio of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmax_63d_base_v041_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    mx=raw.rolling(63,min_periods=max(1,63//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 63d rolling min-std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmin_63d_base_v042_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    mn=raw.rolling(63,min_periods=max(1,63//2)).min()
    sd=raw.rolling(63,min_periods=max(1,63//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 63d) of pma_sma for price_moving_averages
def f07pma_price_moving_averages_expz_63d_base_v043_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    mu=raw.expanding(min_periods=63).mean()
    sd=raw.expanding(min_periods=63).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of pma_sma at 63d for price_moving_averages
def f07pma_price_moving_averages_sign_63d_base_v044_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 63d positive fraction of pma_sma for price_moving_averages
def f07pma_price_moving_averages_posfr_63d_base_v045_signal(closeadj):
    raw=_pma_sma(closeadj, 63)
    result=(raw>0).astype(float).rolling(63,min_periods=max(1,63//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d z-score of pma_sma for price_moving_averages
def f07pma_price_moving_averages_zscore_126d_base_v046_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=_z(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d pctrank of pma_sma for price_moving_averages
def f07pma_price_moving_averages_prank_126d_base_v047_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=_prank(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d roc of pma_sma for price_moving_averages
def f07pma_price_moving_averages_roc_126d_base_v048_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=raw.pct_change(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d minmax of pma_sma for price_moving_averages
def f07pma_price_moving_averages_mnmx_126d_base_v049_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=_minmax(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling mean of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmean_126d_base_v050_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=raw.rolling(126,min_periods=max(1,126//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rstd_126d_base_v051_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=raw.rolling(126,min_periods=max(1,126//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 126d z-score of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_z2_126d_base_v052_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 126)
    result=_z(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d pctrank of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_pk2_126d_base_v053_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 126)
    result=_prank(raw,126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d roc of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_roc2_126d_base_v054_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 126)
    result=raw.pct_change(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d diff of pma_sma for price_moving_averages
def f07pma_price_moving_averages_diff_126d_base_v055_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=raw.diff(126)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling max ratio of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmax_126d_base_v056_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    mx=raw.rolling(126,min_periods=max(1,126//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 126d rolling min-std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmin_126d_base_v057_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    mn=raw.rolling(126,min_periods=max(1,126//2)).min()
    sd=raw.rolling(126,min_periods=max(1,126//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 126d) of pma_sma for price_moving_averages
def f07pma_price_moving_averages_expz_126d_base_v058_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    mu=raw.expanding(min_periods=126).mean()
    sd=raw.expanding(min_periods=126).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of pma_sma at 126d for price_moving_averages
def f07pma_price_moving_averages_sign_126d_base_v059_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 126d positive fraction of pma_sma for price_moving_averages
def f07pma_price_moving_averages_posfr_126d_base_v060_signal(closeadj):
    raw=_pma_sma(closeadj, 126)
    result=(raw>0).astype(float).rolling(126,min_periods=max(1,126//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 252d z-score of pma_sma for price_moving_averages
def f07pma_price_moving_averages_zscore_252d_base_v061_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=_z(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d pctrank of pma_sma for price_moving_averages
def f07pma_price_moving_averages_prank_252d_base_v062_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=_prank(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d roc of pma_sma for price_moving_averages
def f07pma_price_moving_averages_roc_252d_base_v063_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=raw.pct_change(252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d minmax of pma_sma for price_moving_averages
def f07pma_price_moving_averages_mnmx_252d_base_v064_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=_minmax(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d rolling mean of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmean_252d_base_v065_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=raw.rolling(252,min_periods=max(1,252//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

# 252d rolling std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rstd_252d_base_v066_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=raw.rolling(252,min_periods=max(1,252//2)).std()
    return result.replace([np.inf,-np.inf],np.nan)

# 252d z-score of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_z2_252d_base_v067_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 252)
    result=_z(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d pctrank of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_pk2_252d_base_v068_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 252)
    result=_prank(raw,252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d roc of pma_price_vs_sma for price_moving_averages
def f07pma_price_moving_averages_roc2_252d_base_v069_signal(closeadj):
    raw=_pma_price_vs_sma(closeadj, 252)
    result=raw.pct_change(252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d diff of pma_sma for price_moving_averages
def f07pma_price_moving_averages_diff_252d_base_v070_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=raw.diff(252)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d rolling max ratio of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmax_252d_base_v071_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    mx=raw.rolling(252,min_periods=max(1,252//2)).max()
    result=(raw/mx.replace(0,np.nan))-1.0
    return result.replace([np.inf,-np.inf],np.nan)

# 252d rolling min-std of pma_sma for price_moving_averages
def f07pma_price_moving_averages_rmin_252d_base_v072_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    mn=raw.rolling(252,min_periods=max(1,252//2)).min()
    sd=raw.rolling(252,min_periods=max(1,252//2)).std().replace(0,np.nan)
    result=(raw-mn)/sd
    return result.replace([np.inf,-np.inf],np.nan)

# expanding z-score (min 252d) of pma_sma for price_moving_averages
def f07pma_price_moving_averages_expz_252d_base_v073_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    mu=raw.expanding(min_periods=252).mean()
    sd=raw.expanding(min_periods=252).std()
    result=(raw-mu)/sd.replace(0,np.nan)
    return result.replace([np.inf,-np.inf],np.nan)

# sign of pma_sma at 252d for price_moving_averages
def f07pma_price_moving_averages_sign_252d_base_v074_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=np.sign(raw).astype(float)
    return result.replace([np.inf,-np.inf],np.nan)

# 252d positive fraction of pma_sma for price_moving_averages
def f07pma_price_moving_averages_posfr_252d_base_v075_signal(closeadj):
    raw=_pma_sma(closeadj, 252)
    result=(raw>0).astype(float).rolling(252,min_periods=max(1,252//2)).mean()
    return result.replace([np.inf,-np.inf],np.nan)

REGISTRY = {"f07pma_price_moving_averages_zscore_5d_base_v001_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_zscore_5d_base_v001_signal}, "f07pma_price_moving_averages_prank_5d_base_v002_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_prank_5d_base_v002_signal}, "f07pma_price_moving_averages_roc_5d_base_v003_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc_5d_base_v003_signal}, "f07pma_price_moving_averages_mnmx_5d_base_v004_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_mnmx_5d_base_v004_signal}, "f07pma_price_moving_averages_rmean_5d_base_v005_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmean_5d_base_v005_signal}, "f07pma_price_moving_averages_rstd_5d_base_v006_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rstd_5d_base_v006_signal}, "f07pma_price_moving_averages_z2_5d_base_v007_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_z2_5d_base_v007_signal}, "f07pma_price_moving_averages_pk2_5d_base_v008_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_pk2_5d_base_v008_signal}, "f07pma_price_moving_averages_roc2_5d_base_v009_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc2_5d_base_v009_signal}, "f07pma_price_moving_averages_diff_5d_base_v010_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_diff_5d_base_v010_signal}, "f07pma_price_moving_averages_rmax_5d_base_v011_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmax_5d_base_v011_signal}, "f07pma_price_moving_averages_rmin_5d_base_v012_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmin_5d_base_v012_signal}, "f07pma_price_moving_averages_expz_5d_base_v013_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_expz_5d_base_v013_signal}, "f07pma_price_moving_averages_sign_5d_base_v014_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_sign_5d_base_v014_signal}, "f07pma_price_moving_averages_posfr_5d_base_v015_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_posfr_5d_base_v015_signal}, "f07pma_price_moving_averages_zscore_21d_base_v016_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_zscore_21d_base_v016_signal}, "f07pma_price_moving_averages_prank_21d_base_v017_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_prank_21d_base_v017_signal}, "f07pma_price_moving_averages_roc_21d_base_v018_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc_21d_base_v018_signal}, "f07pma_price_moving_averages_mnmx_21d_base_v019_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_mnmx_21d_base_v019_signal}, "f07pma_price_moving_averages_rmean_21d_base_v020_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmean_21d_base_v020_signal}, "f07pma_price_moving_averages_rstd_21d_base_v021_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rstd_21d_base_v021_signal}, "f07pma_price_moving_averages_z2_21d_base_v022_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_z2_21d_base_v022_signal}, "f07pma_price_moving_averages_pk2_21d_base_v023_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_pk2_21d_base_v023_signal}, "f07pma_price_moving_averages_roc2_21d_base_v024_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc2_21d_base_v024_signal}, "f07pma_price_moving_averages_diff_21d_base_v025_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_diff_21d_base_v025_signal}, "f07pma_price_moving_averages_rmax_21d_base_v026_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmax_21d_base_v026_signal}, "f07pma_price_moving_averages_rmin_21d_base_v027_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmin_21d_base_v027_signal}, "f07pma_price_moving_averages_expz_21d_base_v028_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_expz_21d_base_v028_signal}, "f07pma_price_moving_averages_sign_21d_base_v029_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_sign_21d_base_v029_signal}, "f07pma_price_moving_averages_posfr_21d_base_v030_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_posfr_21d_base_v030_signal}, "f07pma_price_moving_averages_zscore_63d_base_v031_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_zscore_63d_base_v031_signal}, "f07pma_price_moving_averages_prank_63d_base_v032_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_prank_63d_base_v032_signal}, "f07pma_price_moving_averages_roc_63d_base_v033_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc_63d_base_v033_signal}, "f07pma_price_moving_averages_mnmx_63d_base_v034_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_mnmx_63d_base_v034_signal}, "f07pma_price_moving_averages_rmean_63d_base_v035_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmean_63d_base_v035_signal}, "f07pma_price_moving_averages_rstd_63d_base_v036_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rstd_63d_base_v036_signal}, "f07pma_price_moving_averages_z2_63d_base_v037_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_z2_63d_base_v037_signal}, "f07pma_price_moving_averages_pk2_63d_base_v038_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_pk2_63d_base_v038_signal}, "f07pma_price_moving_averages_roc2_63d_base_v039_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc2_63d_base_v039_signal}, "f07pma_price_moving_averages_diff_63d_base_v040_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_diff_63d_base_v040_signal}, "f07pma_price_moving_averages_rmax_63d_base_v041_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmax_63d_base_v041_signal}, "f07pma_price_moving_averages_rmin_63d_base_v042_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmin_63d_base_v042_signal}, "f07pma_price_moving_averages_expz_63d_base_v043_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_expz_63d_base_v043_signal}, "f07pma_price_moving_averages_sign_63d_base_v044_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_sign_63d_base_v044_signal}, "f07pma_price_moving_averages_posfr_63d_base_v045_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_posfr_63d_base_v045_signal}, "f07pma_price_moving_averages_zscore_126d_base_v046_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_zscore_126d_base_v046_signal}, "f07pma_price_moving_averages_prank_126d_base_v047_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_prank_126d_base_v047_signal}, "f07pma_price_moving_averages_roc_126d_base_v048_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc_126d_base_v048_signal}, "f07pma_price_moving_averages_mnmx_126d_base_v049_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_mnmx_126d_base_v049_signal}, "f07pma_price_moving_averages_rmean_126d_base_v050_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmean_126d_base_v050_signal}, "f07pma_price_moving_averages_rstd_126d_base_v051_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rstd_126d_base_v051_signal}, "f07pma_price_moving_averages_z2_126d_base_v052_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_z2_126d_base_v052_signal}, "f07pma_price_moving_averages_pk2_126d_base_v053_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_pk2_126d_base_v053_signal}, "f07pma_price_moving_averages_roc2_126d_base_v054_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc2_126d_base_v054_signal}, "f07pma_price_moving_averages_diff_126d_base_v055_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_diff_126d_base_v055_signal}, "f07pma_price_moving_averages_rmax_126d_base_v056_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmax_126d_base_v056_signal}, "f07pma_price_moving_averages_rmin_126d_base_v057_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmin_126d_base_v057_signal}, "f07pma_price_moving_averages_expz_126d_base_v058_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_expz_126d_base_v058_signal}, "f07pma_price_moving_averages_sign_126d_base_v059_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_sign_126d_base_v059_signal}, "f07pma_price_moving_averages_posfr_126d_base_v060_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_posfr_126d_base_v060_signal}, "f07pma_price_moving_averages_zscore_252d_base_v061_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_zscore_252d_base_v061_signal}, "f07pma_price_moving_averages_prank_252d_base_v062_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_prank_252d_base_v062_signal}, "f07pma_price_moving_averages_roc_252d_base_v063_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc_252d_base_v063_signal}, "f07pma_price_moving_averages_mnmx_252d_base_v064_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_mnmx_252d_base_v064_signal}, "f07pma_price_moving_averages_rmean_252d_base_v065_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmean_252d_base_v065_signal}, "f07pma_price_moving_averages_rstd_252d_base_v066_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rstd_252d_base_v066_signal}, "f07pma_price_moving_averages_z2_252d_base_v067_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_z2_252d_base_v067_signal}, "f07pma_price_moving_averages_pk2_252d_base_v068_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_pk2_252d_base_v068_signal}, "f07pma_price_moving_averages_roc2_252d_base_v069_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_roc2_252d_base_v069_signal}, "f07pma_price_moving_averages_diff_252d_base_v070_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_diff_252d_base_v070_signal}, "f07pma_price_moving_averages_rmax_252d_base_v071_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmax_252d_base_v071_signal}, "f07pma_price_moving_averages_rmin_252d_base_v072_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_rmin_252d_base_v072_signal}, "f07pma_price_moving_averages_expz_252d_base_v073_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_expz_252d_base_v073_signal}, "f07pma_price_moving_averages_sign_252d_base_v074_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_sign_252d_base_v074_signal}, "f07pma_price_moving_averages_posfr_252d_base_v075_signal": {"inputs": ['closeadj'], "func": f07pma_price_moving_averages_posfr_252d_base_v075_signal}}
F07_PRICE_MOVING_AVERAGES_REGISTRY_001_075 = REGISTRY

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