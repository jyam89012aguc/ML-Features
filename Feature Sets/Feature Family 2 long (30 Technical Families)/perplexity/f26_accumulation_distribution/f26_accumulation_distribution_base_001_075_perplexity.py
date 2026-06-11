import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _ad_mfm(close, high, low):
    return (2 * close - high - low) / (high - low).replace(0, np.nan)
def _ad_mfv(close, high, low, volume):
    return _ad_mfm(close, high, low) * volume
def _ad_line(close, high, low, volume):
    return _ad_mfv(close, high, low, volume).cumsum()

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _ad_mfm window 5d
def f26ad_accumulation_distribution_ad_mfm_5d_raw_base_v001_signal(close, high, low, volume):
    result = _ad_mfm(close, high, low)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _ad_mfm window 21d
def f26ad_accumulation_distribution_ad_mfm_21d_raw_base_v002_signal(close, high, low, volume):
    result = _ad_mfm(close, high, low)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _ad_mfm window 63d
def f26ad_accumulation_distribution_ad_mfm_63d_raw_base_v003_signal(close, high, low, volume):
    result = _ad_mfm(close, high, low)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _ad_mfm window 126d
def f26ad_accumulation_distribution_ad_mfm_126d_raw_base_v004_signal(close, high, low, volume):
    result = _ad_mfm(close, high, low)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=5 lb=21d
def f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v005_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=5 lb=63d
def f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v006_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=5 lb=252d
def f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v007_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=21 lb=21d
def f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v008_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=21 lb=63d
def f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v009_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=21 lb=252d
def f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v010_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=63 lb=21d
def f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v011_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=63 lb=63d
def f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v012_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=63 lb=252d
def f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v013_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=126 lb=21d
def f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v014_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=126 lb=63d
def f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v015_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=126 lb=252d
def f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v016_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=5 over 63d
def f26ad_accumulation_distribution_ad_mfm_5d_pctrank_base_v017_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=5 over 252d
def f26ad_accumulation_distribution_ad_mfm_5d_pctrank_base_v018_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=21 over 63d
def f26ad_accumulation_distribution_ad_mfm_21d_pctrank_base_v019_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=21 over 252d
def f26ad_accumulation_distribution_ad_mfm_21d_pctrank_base_v020_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=63 over 63d
def f26ad_accumulation_distribution_ad_mfm_63d_pctrank_base_v021_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=63 over 252d
def f26ad_accumulation_distribution_ad_mfm_63d_pctrank_base_v022_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=126 over 63d
def f26ad_accumulation_distribution_ad_mfm_126d_pctrank_base_v023_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=126 over 252d
def f26ad_accumulation_distribution_ad_mfm_126d_pctrank_base_v024_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=5 roc=5d
def f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v025_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=5 roc=21d
def f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v026_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=5 roc=63d
def f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v027_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=21 roc=5d
def f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v028_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=21 roc=21d
def f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v029_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=21 roc=63d
def f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v030_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=63 roc=5d
def f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v031_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=63 roc=21d
def f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v032_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=63 roc=63d
def f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v033_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=126 roc=5d
def f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v034_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=126 roc=21d
def f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v035_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=126 roc=63d
def f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v036_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _ad_mfm w=5
def f26ad_accumulation_distribution_ad_mfm_5d_maxratio_base_v037_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _ad_mfm w=5
def f26ad_accumulation_distribution_ad_mfm_5d_maxratio_base_v038_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _ad_mfm w=21
def f26ad_accumulation_distribution_ad_mfm_21d_maxratio_base_v039_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _ad_mfm w=21
def f26ad_accumulation_distribution_ad_mfm_21d_maxratio_base_v040_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _ad_mfm w=63
def f26ad_accumulation_distribution_ad_mfm_63d_maxratio_base_v041_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _ad_mfm w=63
def f26ad_accumulation_distribution_ad_mfm_63d_maxratio_base_v042_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _ad_mfm w=126
def f26ad_accumulation_distribution_ad_mfm_126d_maxratio_base_v043_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _ad_mfm w=126
def f26ad_accumulation_distribution_ad_mfm_126d_maxratio_base_v044_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _ad_mfm w=5
def f26ad_accumulation_distribution_ad_mfm_5d_sign_base_v045_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _ad_mfm w=21
def f26ad_accumulation_distribution_ad_mfm_21d_sign_base_v046_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _ad_mfm w=63
def f26ad_accumulation_distribution_ad_mfm_63d_sign_base_v047_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _ad_mfm w=126
def f26ad_accumulation_distribution_ad_mfm_126d_sign_base_v048_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _ad_mfm window 5d
def f26ad_accumulation_distribution_ad_mfm_5dv1_raw_base_v049_signal(close, high, low, volume):
    result = _ad_mfm(close, high, low)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _ad_mfm window 21d
def f26ad_accumulation_distribution_ad_mfm_21dv1_raw_base_v050_signal(close, high, low, volume):
    result = _ad_mfm(close, high, low)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _ad_mfm window 63d
def f26ad_accumulation_distribution_ad_mfm_63dv1_raw_base_v051_signal(close, high, low, volume):
    result = _ad_mfm(close, high, low)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _ad_mfm window 126d
def f26ad_accumulation_distribution_ad_mfm_126dv1_raw_base_v052_signal(close, high, low, volume):
    result = _ad_mfm(close, high, low)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=5 lb=21d
def f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v053_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=5 lb=63d
def f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v054_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=5 lb=252d
def f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v055_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=21 lb=21d
def f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v056_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=21 lb=63d
def f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v057_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=21 lb=252d
def f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v058_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=63 lb=21d
def f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v059_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=63 lb=63d
def f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v060_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=63 lb=252d
def f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v061_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=126 lb=21d
def f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v062_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=126 lb=63d
def f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v063_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _ad_mfm w=126 lb=252d
def f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v064_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=5 over 63d
def f26ad_accumulation_distribution_ad_mfm_5dv1_pctrank_base_v065_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=5 over 252d
def f26ad_accumulation_distribution_ad_mfm_5dv1_pctrank_base_v066_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=21 over 63d
def f26ad_accumulation_distribution_ad_mfm_21dv1_pctrank_base_v067_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=21 over 252d
def f26ad_accumulation_distribution_ad_mfm_21dv1_pctrank_base_v068_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=63 over 63d
def f26ad_accumulation_distribution_ad_mfm_63dv1_pctrank_base_v069_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=63 over 252d
def f26ad_accumulation_distribution_ad_mfm_63dv1_pctrank_base_v070_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=126 over 63d
def f26ad_accumulation_distribution_ad_mfm_126dv1_pctrank_base_v071_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _ad_mfm w=126 over 252d
def f26ad_accumulation_distribution_ad_mfm_126dv1_pctrank_base_v072_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=5 roc=5d
def f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v073_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=5 roc=21d
def f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v074_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _ad_mfm w=5 roc=63d
def f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v075_signal(close, high, low, volume):
    b = _ad_mfm(close, high, low)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f26ad_accumulation_distribution_ad_mfm_5d_raw_base_v001_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_raw_base_v001_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_raw_base_v002_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_raw_base_v002_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_raw_base_v003_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_raw_base_v003_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_raw_base_v004_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_raw_base_v004_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v005_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v005_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v006_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v006_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v007_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_zscore_base_v007_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v008_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v008_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v009_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v009_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v010_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_zscore_base_v010_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v011_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v011_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v012_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v012_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v013_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_zscore_base_v013_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v014_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v014_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v015_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v015_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v016_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_zscore_base_v016_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_pctrank_base_v017_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_pctrank_base_v017_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_pctrank_base_v018_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_pctrank_base_v018_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_pctrank_base_v019_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_pctrank_base_v019_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_pctrank_base_v020_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_pctrank_base_v020_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_pctrank_base_v021_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_pctrank_base_v021_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_pctrank_base_v022_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_pctrank_base_v022_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_pctrank_base_v023_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_pctrank_base_v023_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_pctrank_base_v024_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_pctrank_base_v024_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v025_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v025_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v026_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v026_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v027_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_roc_base_v027_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v028_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v028_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v029_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v029_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v030_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_roc_base_v030_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v031_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v031_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v032_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v032_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v033_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_roc_base_v033_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v034_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v034_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v035_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v035_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v036_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_roc_base_v036_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_maxratio_base_v037_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_maxratio_base_v037_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_maxratio_base_v038_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_maxratio_base_v038_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_maxratio_base_v039_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_maxratio_base_v039_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_maxratio_base_v040_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_maxratio_base_v040_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_maxratio_base_v041_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_maxratio_base_v041_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_maxratio_base_v042_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_maxratio_base_v042_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_maxratio_base_v043_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_maxratio_base_v043_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_maxratio_base_v044_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_maxratio_base_v044_signal},
    "f26ad_accumulation_distribution_ad_mfm_5d_sign_base_v045_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5d_sign_base_v045_signal},
    "f26ad_accumulation_distribution_ad_mfm_21d_sign_base_v046_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21d_sign_base_v046_signal},
    "f26ad_accumulation_distribution_ad_mfm_63d_sign_base_v047_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63d_sign_base_v047_signal},
    "f26ad_accumulation_distribution_ad_mfm_126d_sign_base_v048_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126d_sign_base_v048_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_raw_base_v049_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_raw_base_v049_signal},
    "f26ad_accumulation_distribution_ad_mfm_21dv1_raw_base_v050_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21dv1_raw_base_v050_signal},
    "f26ad_accumulation_distribution_ad_mfm_63dv1_raw_base_v051_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63dv1_raw_base_v051_signal},
    "f26ad_accumulation_distribution_ad_mfm_126dv1_raw_base_v052_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126dv1_raw_base_v052_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v053_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v053_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v054_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v054_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v055_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_zscore_base_v055_signal},
    "f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v056_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v056_signal},
    "f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v057_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v057_signal},
    "f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v058_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21dv1_zscore_base_v058_signal},
    "f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v059_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v059_signal},
    "f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v060_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v060_signal},
    "f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v061_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63dv1_zscore_base_v061_signal},
    "f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v062_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v062_signal},
    "f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v063_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v063_signal},
    "f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v064_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126dv1_zscore_base_v064_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_pctrank_base_v065_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_pctrank_base_v065_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_pctrank_base_v066_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_pctrank_base_v066_signal},
    "f26ad_accumulation_distribution_ad_mfm_21dv1_pctrank_base_v067_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21dv1_pctrank_base_v067_signal},
    "f26ad_accumulation_distribution_ad_mfm_21dv1_pctrank_base_v068_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_21dv1_pctrank_base_v068_signal},
    "f26ad_accumulation_distribution_ad_mfm_63dv1_pctrank_base_v069_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63dv1_pctrank_base_v069_signal},
    "f26ad_accumulation_distribution_ad_mfm_63dv1_pctrank_base_v070_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_63dv1_pctrank_base_v070_signal},
    "f26ad_accumulation_distribution_ad_mfm_126dv1_pctrank_base_v071_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126dv1_pctrank_base_v071_signal},
    "f26ad_accumulation_distribution_ad_mfm_126dv1_pctrank_base_v072_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_126dv1_pctrank_base_v072_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v073_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v073_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v074_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v074_signal},
    "f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v075_signal": {"inputs": ["close", "high", "low", "volume"], "func": f26ad_accumulation_distribution_ad_mfm_5dv1_roc_base_v075_signal}
}
F26_ACCUMULATION_DISTRIBUTION_REGISTRY_001_075 = REGISTRY

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
        assert "_ad_mfm" in src or "_ad_mfv" in src or "_ad_line" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F26_ACCUMULATION_DISTRIBUTION_REGISTRY_001_075")
