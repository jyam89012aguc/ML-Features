import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _tsm_tr(high, low, close):
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
def _tsm_dm_plus(high, low):
    up = high.diff(1)
    dn = -low.diff(1)
    return up.where((up > dn) & (up > 0), 0.0)
def _tsm_adx(high, low, close, w):
    tr = _tsm_tr(high, low, close)
    dmp = _tsm_dm_plus(high, low)
    dmn = (-low.diff(1)).where((-low.diff(1) > high.diff(1)) & (-low.diff(1) > 0), 0.0)
    atr = tr.ewm(span=w, min_periods=max(1, w//2), adjust=False).mean()
    pdi = 100 * dmp.ewm(span=w, min_periods=max(1, w//2), adjust=False).mean() / atr.replace(0, np.nan)
    ndi = 100 * dmn.ewm(span=w, min_periods=max(1, w//2), adjust=False).mean() / atr.replace(0, np.nan)
    dx = 100 * (pdi - ndi).abs() / (pdi + ndi).replace(0, np.nan)
    return dx.ewm(span=w, min_periods=max(1, w//2), adjust=False).mean()

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _tsm_adx window 5d
def f03tsm_trend_strength_metrics_tsm_adx_5d_raw_base_v001_signal(close, high, low):
    result = _tsm_adx(high, low, close, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _tsm_adx window 14d
def f03tsm_trend_strength_metrics_tsm_adx_14d_raw_base_v002_signal(close, high, low):
    result = _tsm_adx(high, low, close, 14)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _tsm_adx window 21d
def f03tsm_trend_strength_metrics_tsm_adx_21d_raw_base_v003_signal(close, high, low):
    result = _tsm_adx(high, low, close, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _tsm_adx window 63d
def f03tsm_trend_strength_metrics_tsm_adx_63d_raw_base_v004_signal(close, high, low):
    result = _tsm_adx(high, low, close, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=5 lb=21d
def f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v005_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=5 lb=63d
def f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v006_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=5 lb=252d
def f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v007_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=14 lb=21d
def f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v008_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=14 lb=63d
def f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v009_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=14 lb=252d
def f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v010_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=21 lb=21d
def f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v011_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=21 lb=63d
def f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v012_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=21 lb=252d
def f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v013_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=63 lb=21d
def f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v014_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=63 lb=63d
def f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v015_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=63 lb=252d
def f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v016_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=5 over 63d
def f03tsm_trend_strength_metrics_tsm_adx_5d_pctrank_base_v017_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=5 over 252d
def f03tsm_trend_strength_metrics_tsm_adx_5d_pctrank_base_v018_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=14 over 63d
def f03tsm_trend_strength_metrics_tsm_adx_14d_pctrank_base_v019_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=14 over 252d
def f03tsm_trend_strength_metrics_tsm_adx_14d_pctrank_base_v020_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=21 over 63d
def f03tsm_trend_strength_metrics_tsm_adx_21d_pctrank_base_v021_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=21 over 252d
def f03tsm_trend_strength_metrics_tsm_adx_21d_pctrank_base_v022_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=63 over 63d
def f03tsm_trend_strength_metrics_tsm_adx_63d_pctrank_base_v023_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=63 over 252d
def f03tsm_trend_strength_metrics_tsm_adx_63d_pctrank_base_v024_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=5 roc=5d
def f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v025_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=5 roc=21d
def f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v026_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=5 roc=63d
def f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v027_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=14 roc=5d
def f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v028_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=14 roc=21d
def f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v029_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=14 roc=63d
def f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v030_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=21 roc=5d
def f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v031_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=21 roc=21d
def f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v032_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=21 roc=63d
def f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v033_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=63 roc=5d
def f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v034_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=63 roc=21d
def f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v035_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=63 roc=63d
def f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v036_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _tsm_adx w=5
def f03tsm_trend_strength_metrics_tsm_adx_5d_maxratio_base_v037_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _tsm_adx w=5
def f03tsm_trend_strength_metrics_tsm_adx_5d_maxratio_base_v038_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _tsm_adx w=14
def f03tsm_trend_strength_metrics_tsm_adx_14d_maxratio_base_v039_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _tsm_adx w=14
def f03tsm_trend_strength_metrics_tsm_adx_14d_maxratio_base_v040_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _tsm_adx w=21
def f03tsm_trend_strength_metrics_tsm_adx_21d_maxratio_base_v041_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _tsm_adx w=21
def f03tsm_trend_strength_metrics_tsm_adx_21d_maxratio_base_v042_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _tsm_adx w=63
def f03tsm_trend_strength_metrics_tsm_adx_63d_maxratio_base_v043_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _tsm_adx w=63
def f03tsm_trend_strength_metrics_tsm_adx_63d_maxratio_base_v044_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _tsm_adx w=5
def f03tsm_trend_strength_metrics_tsm_adx_5d_sign_base_v045_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _tsm_adx w=14
def f03tsm_trend_strength_metrics_tsm_adx_14d_sign_base_v046_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _tsm_adx w=21
def f03tsm_trend_strength_metrics_tsm_adx_21d_sign_base_v047_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _tsm_adx w=63
def f03tsm_trend_strength_metrics_tsm_adx_63d_sign_base_v048_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _tsm_adx window 5d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_raw_base_v049_signal(close, high, low):
    result = _tsm_adx(high, low, close, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _tsm_adx window 14d
def f03tsm_trend_strength_metrics_tsm_adx_14dv1_raw_base_v050_signal(close, high, low):
    result = _tsm_adx(high, low, close, 14)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _tsm_adx window 21d
def f03tsm_trend_strength_metrics_tsm_adx_21dv1_raw_base_v051_signal(close, high, low):
    result = _tsm_adx(high, low, close, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _tsm_adx window 63d
def f03tsm_trend_strength_metrics_tsm_adx_63dv1_raw_base_v052_signal(close, high, low):
    result = _tsm_adx(high, low, close, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=5 lb=21d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v053_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=5 lb=63d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v054_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=5 lb=252d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v055_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=14 lb=21d
def f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v056_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=14 lb=63d
def f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v057_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=14 lb=252d
def f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v058_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=21 lb=21d
def f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v059_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=21 lb=63d
def f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v060_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=21 lb=252d
def f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v061_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=63 lb=21d
def f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v062_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=63 lb=63d
def f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v063_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _tsm_adx w=63 lb=252d
def f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v064_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=5 over 63d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_pctrank_base_v065_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=5 over 252d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_pctrank_base_v066_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=14 over 63d
def f03tsm_trend_strength_metrics_tsm_adx_14dv1_pctrank_base_v067_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=14 over 252d
def f03tsm_trend_strength_metrics_tsm_adx_14dv1_pctrank_base_v068_signal(close, high, low):
    b = _tsm_adx(high, low, close, 14)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=21 over 63d
def f03tsm_trend_strength_metrics_tsm_adx_21dv1_pctrank_base_v069_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=21 over 252d
def f03tsm_trend_strength_metrics_tsm_adx_21dv1_pctrank_base_v070_signal(close, high, low):
    b = _tsm_adx(high, low, close, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=63 over 63d
def f03tsm_trend_strength_metrics_tsm_adx_63dv1_pctrank_base_v071_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _tsm_adx w=63 over 252d
def f03tsm_trend_strength_metrics_tsm_adx_63dv1_pctrank_base_v072_signal(close, high, low):
    b = _tsm_adx(high, low, close, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=5 roc=5d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v073_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=5 roc=21d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v074_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _tsm_adx w=5 roc=63d
def f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v075_signal(close, high, low):
    b = _tsm_adx(high, low, close, 5)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f03tsm_trend_strength_metrics_tsm_adx_5d_raw_base_v001_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_raw_base_v001_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_raw_base_v002_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_raw_base_v002_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_raw_base_v003_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_raw_base_v003_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_raw_base_v004_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_raw_base_v004_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v005_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v005_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v006_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v006_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v007_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_zscore_base_v007_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v008_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v008_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v009_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v009_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v010_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_zscore_base_v010_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v011_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v011_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v012_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v012_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v013_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_zscore_base_v013_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v014_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v014_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v015_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v015_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v016_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_zscore_base_v016_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_pctrank_base_v017_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_pctrank_base_v017_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_pctrank_base_v018_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_pctrank_base_v018_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_pctrank_base_v019_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_pctrank_base_v019_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_pctrank_base_v020_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_pctrank_base_v020_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_pctrank_base_v021_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_pctrank_base_v021_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_pctrank_base_v022_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_pctrank_base_v022_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_pctrank_base_v023_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_pctrank_base_v023_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_pctrank_base_v024_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_pctrank_base_v024_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v025_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v025_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v026_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v026_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v027_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_roc_base_v027_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v028_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v028_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v029_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v029_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v030_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_roc_base_v030_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v031_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v031_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v032_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v032_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v033_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_roc_base_v033_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v034_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v034_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v035_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v035_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v036_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_roc_base_v036_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_maxratio_base_v037_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_maxratio_base_v037_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_maxratio_base_v038_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_maxratio_base_v038_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_maxratio_base_v039_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_maxratio_base_v039_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_maxratio_base_v040_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_maxratio_base_v040_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_maxratio_base_v041_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_maxratio_base_v041_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_maxratio_base_v042_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_maxratio_base_v042_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_maxratio_base_v043_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_maxratio_base_v043_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_maxratio_base_v044_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_maxratio_base_v044_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5d_sign_base_v045_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5d_sign_base_v045_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14d_sign_base_v046_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14d_sign_base_v046_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21d_sign_base_v047_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21d_sign_base_v047_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63d_sign_base_v048_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63d_sign_base_v048_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_raw_base_v049_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_raw_base_v049_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14dv1_raw_base_v050_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14dv1_raw_base_v050_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21dv1_raw_base_v051_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21dv1_raw_base_v051_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63dv1_raw_base_v052_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63dv1_raw_base_v052_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v053_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v053_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v054_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v054_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v055_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_zscore_base_v055_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v056_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v056_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v057_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v057_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v058_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14dv1_zscore_base_v058_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v059_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v059_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v060_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v060_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v061_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21dv1_zscore_base_v061_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v062_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v062_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v063_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v063_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v064_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63dv1_zscore_base_v064_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_pctrank_base_v065_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_pctrank_base_v065_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_pctrank_base_v066_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_pctrank_base_v066_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14dv1_pctrank_base_v067_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14dv1_pctrank_base_v067_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_14dv1_pctrank_base_v068_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_14dv1_pctrank_base_v068_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21dv1_pctrank_base_v069_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21dv1_pctrank_base_v069_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_21dv1_pctrank_base_v070_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_21dv1_pctrank_base_v070_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63dv1_pctrank_base_v071_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63dv1_pctrank_base_v071_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_63dv1_pctrank_base_v072_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_63dv1_pctrank_base_v072_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v073_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v073_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v074_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v074_signal},
    "f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v075_signal": {"inputs": ["close", "high", "low"], "func": f03tsm_trend_strength_metrics_tsm_adx_5dv1_roc_base_v075_signal}
}
F03_TREND_STRENGTH_METRICS_REGISTRY_001_075 = REGISTRY

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
        assert "_tsm_tr" in src or "_tsm_dm_plus" in src or "_tsm_adx" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F03_TREND_STRENGTH_METRICS_REGISTRY_001_075")
