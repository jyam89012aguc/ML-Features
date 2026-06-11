import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _atr_tr(high, low, close):
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
def _atr_value(high, low, close, w):
    tr = _atr_tr(high, low, close)
    return tr.rolling(w, min_periods=max(1, w//2)).mean()
def _atr_norm(close, high, low, w):
    atr = _atr_value(high, low, close, w)
    return close / atr.replace(0, np.nan)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _atr_tr window 5d
def f19atr_atr_normalized_price_atr_tr_5d_raw_base_v001_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 14d
def f19atr_atr_normalized_price_atr_tr_14d_raw_base_v002_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 21d
def f19atr_atr_normalized_price_atr_tr_21d_raw_base_v003_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 63d
def f19atr_atr_normalized_price_atr_tr_63d_raw_base_v004_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=21d
def f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v005_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=63d
def f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v006_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=252d
def f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v007_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=21d
def f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v008_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=63d
def f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v009_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=252d
def f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v010_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=21d
def f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v011_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=63d
def f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v012_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=252d
def f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v013_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=21d
def f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v014_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=63d
def f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v015_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=252d
def f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v016_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=5 over 63d
def f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v017_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=5 over 252d
def f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v018_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=14 over 63d
def f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v019_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=14 over 252d
def f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v020_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=21 over 63d
def f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v021_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=21 over 252d
def f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v022_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=63 over 63d
def f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v023_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=63 over 252d
def f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v024_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=5 roc=5d
def f19atr_atr_normalized_price_atr_tr_5d_roc_base_v025_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=5 roc=21d
def f19atr_atr_normalized_price_atr_tr_5d_roc_base_v026_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=14 roc=5d
def f19atr_atr_normalized_price_atr_tr_14d_roc_base_v027_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=14 roc=21d
def f19atr_atr_normalized_price_atr_tr_14d_roc_base_v028_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=21 roc=5d
def f19atr_atr_normalized_price_atr_tr_21d_roc_base_v029_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=21 roc=21d
def f19atr_atr_normalized_price_atr_tr_21d_roc_base_v030_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=63 roc=5d
def f19atr_atr_normalized_price_atr_tr_63d_roc_base_v031_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=63 roc=21d
def f19atr_atr_normalized_price_atr_tr_63d_roc_base_v032_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _atr_tr w=5
def f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v033_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _atr_tr w=5
def f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v034_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _atr_tr w=14
def f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v035_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _atr_tr w=14
def f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v036_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _atr_tr w=21
def f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v037_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _atr_tr w=21
def f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v038_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _atr_tr w=63
def f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v039_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _atr_tr w=63
def f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v040_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _atr_tr w=5
def f19atr_atr_normalized_price_atr_tr_5d_sign_base_v041_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _atr_tr w=14
def f19atr_atr_normalized_price_atr_tr_14d_sign_base_v042_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _atr_tr w=21
def f19atr_atr_normalized_price_atr_tr_21d_sign_base_v043_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _atr_tr w=63
def f19atr_atr_normalized_price_atr_tr_63d_sign_base_v044_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 5d
def f19atr_atr_normalized_price_atr_tr_5dv1_raw_base_v045_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 14d
def f19atr_atr_normalized_price_atr_tr_14dv1_raw_base_v046_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 21d
def f19atr_atr_normalized_price_atr_tr_21dv1_raw_base_v047_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 63d
def f19atr_atr_normalized_price_atr_tr_63dv1_raw_base_v048_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=21d
def f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v049_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=63d
def f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v050_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=252d
def f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v051_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=21d
def f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v052_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=63d
def f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v053_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=252d
def f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v054_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=21d
def f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v055_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=63d
def f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v056_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=252d
def f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v057_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=21d
def f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v058_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=63d
def f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v059_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=252d
def f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v060_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=5 over 63d
def f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v061_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=5 over 252d
def f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v062_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=14 over 63d
def f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v063_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=14 over 252d
def f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v064_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=21 over 63d
def f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v065_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=21 over 252d
def f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v066_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=63 over 63d
def f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v067_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=63 over 252d
def f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v068_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=5 roc=5d
def f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v069_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=5 roc=21d
def f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v070_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=14 roc=5d
def f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v071_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=14 roc=21d
def f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v072_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=21 roc=5d
def f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v073_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=21 roc=21d
def f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v074_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=63 roc=5d
def f19atr_atr_normalized_price_atr_tr_63dv1_roc_base_v075_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f19atr_atr_normalized_price_atr_tr_5d_raw_base_v001_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_raw_base_v001_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_raw_base_v002_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_raw_base_v002_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_raw_base_v003_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_raw_base_v003_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_raw_base_v004_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_raw_base_v004_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v005_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v005_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v006_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v006_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v007_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v007_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v008_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v008_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v009_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v009_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v010_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v010_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v011_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v011_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v012_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v012_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v013_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v013_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v014_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v014_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v015_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v015_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v016_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v016_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v017_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v017_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v018_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v018_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v019_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v019_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v020_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v020_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v021_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v021_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v022_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v022_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v023_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v023_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v024_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v024_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_roc_base_v025_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_roc_base_v025_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_roc_base_v026_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_roc_base_v026_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_roc_base_v027_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_roc_base_v027_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_roc_base_v028_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_roc_base_v028_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_roc_base_v029_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_roc_base_v029_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_roc_base_v030_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_roc_base_v030_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_roc_base_v031_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_roc_base_v031_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_roc_base_v032_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_roc_base_v032_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v033_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v033_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v034_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v034_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v035_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v035_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v036_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v036_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v037_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v037_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v038_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v038_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v039_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v039_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v040_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v040_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_sign_base_v041_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_sign_base_v041_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_sign_base_v042_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_sign_base_v042_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_sign_base_v043_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_sign_base_v043_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_sign_base_v044_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_sign_base_v044_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_raw_base_v045_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_raw_base_v045_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_raw_base_v046_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_raw_base_v046_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_raw_base_v047_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_raw_base_v047_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_raw_base_v048_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_raw_base_v048_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v049_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v049_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v050_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v050_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v051_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v051_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v052_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v052_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v053_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v053_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v054_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v054_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v055_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v055_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v056_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v056_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v057_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v057_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v058_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v058_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v059_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v059_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v060_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v060_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v061_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v061_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v062_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v062_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v063_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v063_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v064_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v064_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v065_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v065_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v066_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v066_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v067_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v067_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v068_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v068_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v069_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v069_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v070_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v070_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v071_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v071_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v072_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v072_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v073_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v073_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v074_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v074_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_roc_base_v075_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_roc_base_v075_signal}
}
F19_ATR_NORMALIZED_PRICE_REGISTRY_001_075 = REGISTRY

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
        assert "_atr_tr" in src or "_atr_value" in src or "_atr_norm" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F19_ATR_NORMALIZED_PRICE_REGISTRY_001_075")
