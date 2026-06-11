import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _rvm_vol_sma(volume, w):
    return volume.rolling(w, min_periods=max(1, w//2)).mean()
def _rvm_vol_ratio(volume, w):
    return volume / _rvm_vol_sma(volume, w).replace(0, np.nan)
def _rvm_vol_zscore(volume, w):
    mu = _rvm_vol_sma(volume, w)
    sd = volume.rolling(w, min_periods=max(1, w//2)).std()
    return (volume - mu) / sd.replace(0, np.nan)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _rvm_vol_ratio window 5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_raw_base_v001_signal(volume):
    result = _rvm_vol_ratio(volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_raw_base_v002_signal(volume):
    result = _rvm_vol_ratio(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_raw_base_v003_signal(volume):
    result = _rvm_vol_ratio(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 126d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_raw_base_v004_signal(volume):
    result = _rvm_vol_ratio(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_raw_base_v005_signal(volume):
    result = _rvm_vol_ratio(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v006_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v007_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v008_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v009_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v010_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v011_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v012_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v013_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v014_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=126 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v015_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=126 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v016_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=126 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v017_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=252 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v018_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=252 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v019_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=252 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v020_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=5 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v021_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=5 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v022_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=21 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v023_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=21 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v024_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=63 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v025_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=63 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v026_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=126 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v027_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=126 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v028_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=252 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v029_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=252 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v030_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=5 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v031_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=5 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v032_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=5 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v033_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=21 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v034_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=21 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v035_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=21 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v036_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=63 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v037_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=63 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v038_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=63 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v039_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=126 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v040_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=126 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v041_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=126 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v042_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=252 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v043_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=252 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v044_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=252 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v045_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=5
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v046_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=5
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v047_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=21
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v048_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=21
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v049_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=63
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v050_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=63
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v051_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=126
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v052_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=126
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v053_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=252
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v054_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=252
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v055_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=5
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_sign_base_v056_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=21
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_sign_base_v057_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=63
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_sign_base_v058_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=126
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_sign_base_v059_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=252
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_sign_base_v060_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_raw_base_v061_signal(volume):
    result = _rvm_vol_ratio(volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_raw_base_v062_signal(volume):
    result = _rvm_vol_ratio(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_raw_base_v063_signal(volume):
    result = _rvm_vol_ratio(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 126d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_raw_base_v064_signal(volume):
    result = _rvm_vol_ratio(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252dv1_raw_base_v065_signal(volume):
    result = _rvm_vol_ratio(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v066_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v067_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v068_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v069_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v070_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v071_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v072_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v073_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v074_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=126 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_zscore_base_v075_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_raw_base_v001_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_raw_base_v001_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_raw_base_v002_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_raw_base_v002_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_raw_base_v003_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_raw_base_v003_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_raw_base_v004_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_raw_base_v004_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_raw_base_v005_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_raw_base_v005_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v006_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v006_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v007_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v007_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v008_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v008_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v009_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v009_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v010_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v010_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v011_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v011_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v012_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v012_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v013_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v013_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v014_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v014_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v015_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v015_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v016_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v016_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v017_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v017_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v018_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v018_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v019_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v019_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v020_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v020_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v021_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v021_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v022_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v022_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v023_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v023_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v024_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v024_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v025_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v025_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v026_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v026_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v027_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v027_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v028_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v028_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v029_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v029_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v030_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v030_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v031_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v031_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v032_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v032_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v033_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v033_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v034_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v034_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v035_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v035_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v036_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v036_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v037_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v037_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v038_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v038_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v039_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v039_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v040_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v040_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v041_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v041_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v042_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v042_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v043_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v043_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v044_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v044_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v045_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v045_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v046_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v046_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v047_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v047_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v048_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v048_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v049_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v049_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v050_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v050_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v051_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v051_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v052_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v052_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v053_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v053_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v054_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v054_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v055_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v055_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_sign_base_v056_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_sign_base_v056_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_sign_base_v057_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_sign_base_v057_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_sign_base_v058_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_sign_base_v058_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_sign_base_v059_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_sign_base_v059_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_sign_base_v060_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_sign_base_v060_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_raw_base_v061_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_raw_base_v061_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_raw_base_v062_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_raw_base_v062_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_raw_base_v063_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_raw_base_v063_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_raw_base_v064_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_raw_base_v064_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252dv1_raw_base_v065_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252dv1_raw_base_v065_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v066_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v066_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v067_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v067_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v068_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v068_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v069_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v069_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v070_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v070_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v071_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v071_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v072_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v072_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v073_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v073_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v074_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v074_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_zscore_base_v075_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_zscore_base_v075_signal}
}
F21_RAW_VOLUME_METRICS_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    idx = pd.date_range("2020-01-01", periods=n, freq="B")
    closeadj = pd.Series(100 * np.exp(np.random.normal(0, 0.01, n).cumsum()), index=idx)
    close = closeadj * (1 + np.random.normal(0, 0.001, n))
    high = close * (1 + np.abs(np.random.normal(0, 0.005, n)))
    low = close * (1 - np.abs(np.random.normal(0, 0.005, n)))
    open_ = close.shift(1).fillna(close.iloc[0])
    volume = pd.Series(np.random.lognormal(15, 0.5, n), index=idx)
    bench = pd.Series(100 * np.exp(np.random.normal(0, 0.009, n).cumsum()), index=idx)
    args_pool = dict(closeadj=closeadj, close=close, high=high, low=low,
                     open_=open_, volume=volume, bench=bench)
    nan_fracs = []
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [args_pool.get(c, closeadj) for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2, check_names=False)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, f"{name}: empty after warm-up"
        assert q.std() > 0, f"{name}: constant output"
        src = inspect.getsource(fn)
        assert "_rvm_vol_sma" in src or "_rvm_vol_ratio" in src or "_rvm_vol_zscore" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F21_RAW_VOLUME_METRICS_REGISTRY_001_075")
