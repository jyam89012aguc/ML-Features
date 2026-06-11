import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _mdi_price_roc(closeadj, w):
    return closeadj.pct_change(w)
def _mdi_price_vs_vol_div(closeadj, volume, w):
    return _mdi_price_roc(closeadj, w) - volume.pct_change(w)
def _mdi_fast_slow_div(closeadj, w_fast, w_slow):
    return _mdi_price_roc(closeadj, w_fast) - _mdi_price_roc(closeadj, w_slow)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _mdi_price_roc window 5d
def f14mdi_momentum_divergence_mdi_price_roc_5d_raw_base_v001_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mdi_price_roc window 21d
def f14mdi_momentum_divergence_mdi_price_roc_21d_raw_base_v002_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mdi_price_roc window 63d
def f14mdi_momentum_divergence_mdi_price_roc_63d_raw_base_v003_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=21d
def f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v004_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=63d
def f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v005_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=252d
def f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v006_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=21d
def f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v007_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=63d
def f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v008_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=252d
def f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v009_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=63 lb=21d
def f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v010_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=63 lb=63d
def f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v011_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=63 lb=252d
def f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v012_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=5 over 63d
def f14mdi_momentum_divergence_mdi_price_roc_5d_pctrank_base_v013_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=5 over 252d
def f14mdi_momentum_divergence_mdi_price_roc_5d_pctrank_base_v014_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=21 over 63d
def f14mdi_momentum_divergence_mdi_price_roc_21d_pctrank_base_v015_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=21 over 252d
def f14mdi_momentum_divergence_mdi_price_roc_21d_pctrank_base_v016_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=63 over 63d
def f14mdi_momentum_divergence_mdi_price_roc_63d_pctrank_base_v017_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=63 over 252d
def f14mdi_momentum_divergence_mdi_price_roc_63d_pctrank_base_v018_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=5 roc=5d
def f14mdi_momentum_divergence_mdi_price_roc_5d_roc_base_v019_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=5 roc=21d
def f14mdi_momentum_divergence_mdi_price_roc_5d_roc_base_v020_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=21 roc=5d
def f14mdi_momentum_divergence_mdi_price_roc_21d_roc_base_v021_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=21 roc=21d
def f14mdi_momentum_divergence_mdi_price_roc_21d_roc_base_v022_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=63 roc=5d
def f14mdi_momentum_divergence_mdi_price_roc_63d_roc_base_v023_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=63 roc=21d
def f14mdi_momentum_divergence_mdi_price_roc_63d_roc_base_v024_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mdi_price_roc w=5
def f14mdi_momentum_divergence_mdi_price_roc_5d_maxratio_base_v025_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mdi_price_roc w=5
def f14mdi_momentum_divergence_mdi_price_roc_5d_maxratio_base_v026_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mdi_price_roc w=21
def f14mdi_momentum_divergence_mdi_price_roc_21d_maxratio_base_v027_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mdi_price_roc w=21
def f14mdi_momentum_divergence_mdi_price_roc_21d_maxratio_base_v028_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mdi_price_roc w=63
def f14mdi_momentum_divergence_mdi_price_roc_63d_maxratio_base_v029_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mdi_price_roc w=63
def f14mdi_momentum_divergence_mdi_price_roc_63d_maxratio_base_v030_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mdi_price_roc w=5
def f14mdi_momentum_divergence_mdi_price_roc_5d_sign_base_v031_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mdi_price_roc w=21
def f14mdi_momentum_divergence_mdi_price_roc_21d_sign_base_v032_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mdi_price_roc w=63
def f14mdi_momentum_divergence_mdi_price_roc_63d_sign_base_v033_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mdi_price_roc window 5d
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_raw_base_v034_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mdi_price_roc window 21d
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_raw_base_v035_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mdi_price_roc window 63d
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_raw_base_v036_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=21d
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v037_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=63d
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v038_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=252d
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v039_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=21d
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v040_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=63d
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v041_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=252d
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v042_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=63 lb=21d
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v043_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=63 lb=63d
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v044_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=63 lb=252d
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v045_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=5 over 63d
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_pctrank_base_v046_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=5 over 252d
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_pctrank_base_v047_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=21 over 63d
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_pctrank_base_v048_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=21 over 252d
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_pctrank_base_v049_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=63 over 63d
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_pctrank_base_v050_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mdi_price_roc w=63 over 252d
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_pctrank_base_v051_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=5 roc=5d
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_roc_base_v052_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=5 roc=21d
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_roc_base_v053_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=21 roc=5d
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_roc_base_v054_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=21 roc=21d
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_roc_base_v055_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=63 roc=5d
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_roc_base_v056_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mdi_price_roc w=63 roc=21d
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_roc_base_v057_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mdi_price_roc w=5
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_maxratio_base_v058_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mdi_price_roc w=5
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_maxratio_base_v059_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mdi_price_roc w=21
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_maxratio_base_v060_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mdi_price_roc w=21
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_maxratio_base_v061_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mdi_price_roc w=63
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_maxratio_base_v062_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mdi_price_roc w=63
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_maxratio_base_v063_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mdi_price_roc w=5
def f14mdi_momentum_divergence_mdi_price_roc_5dv1_sign_base_v064_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mdi_price_roc w=21
def f14mdi_momentum_divergence_mdi_price_roc_21dv1_sign_base_v065_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mdi_price_roc w=63
def f14mdi_momentum_divergence_mdi_price_roc_63dv1_sign_base_v066_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mdi_price_roc window 5d
def f14mdi_momentum_divergence_mdi_price_roc_5dv2_raw_base_v067_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mdi_price_roc window 21d
def f14mdi_momentum_divergence_mdi_price_roc_21dv2_raw_base_v068_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mdi_price_roc window 63d
def f14mdi_momentum_divergence_mdi_price_roc_63dv2_raw_base_v069_signal(closeadj, volume):
    result = _mdi_price_roc(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=21d
def f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v070_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=63d
def f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v071_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=5 lb=252d
def f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v072_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=21d
def f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v073_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=63d
def f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v074_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mdi_price_roc w=21 lb=252d
def f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v075_signal(closeadj, volume):
    b = _mdi_price_roc(closeadj, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f14mdi_momentum_divergence_mdi_price_roc_5d_raw_base_v001_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_raw_base_v001_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_raw_base_v002_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_raw_base_v002_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_raw_base_v003_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_raw_base_v003_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v004_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v004_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v005_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v005_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v006_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_zscore_base_v006_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v007_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v007_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v008_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v008_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v009_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_zscore_base_v009_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v010_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v010_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v011_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v011_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v012_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_zscore_base_v012_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_pctrank_base_v013_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_pctrank_base_v013_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_pctrank_base_v014_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_pctrank_base_v014_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_pctrank_base_v015_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_pctrank_base_v015_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_pctrank_base_v016_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_pctrank_base_v016_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_pctrank_base_v017_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_pctrank_base_v017_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_pctrank_base_v018_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_pctrank_base_v018_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_roc_base_v019_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_roc_base_v019_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_roc_base_v020_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_roc_base_v020_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_roc_base_v021_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_roc_base_v021_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_roc_base_v022_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_roc_base_v022_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_roc_base_v023_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_roc_base_v023_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_roc_base_v024_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_roc_base_v024_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_maxratio_base_v025_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_maxratio_base_v025_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_maxratio_base_v026_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_maxratio_base_v026_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_maxratio_base_v027_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_maxratio_base_v027_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_maxratio_base_v028_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_maxratio_base_v028_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_maxratio_base_v029_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_maxratio_base_v029_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_maxratio_base_v030_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_maxratio_base_v030_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5d_sign_base_v031_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5d_sign_base_v031_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21d_sign_base_v032_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21d_sign_base_v032_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63d_sign_base_v033_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63d_sign_base_v033_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_raw_base_v034_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_raw_base_v034_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_raw_base_v035_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_raw_base_v035_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_raw_base_v036_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_raw_base_v036_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v037_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v037_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v038_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v038_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v039_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_zscore_base_v039_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v040_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v040_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v041_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v041_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v042_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_zscore_base_v042_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v043_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v043_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v044_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v044_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v045_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_zscore_base_v045_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_pctrank_base_v046_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_pctrank_base_v046_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_pctrank_base_v047_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_pctrank_base_v047_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_pctrank_base_v048_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_pctrank_base_v048_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_pctrank_base_v049_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_pctrank_base_v049_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_pctrank_base_v050_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_pctrank_base_v050_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_pctrank_base_v051_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_pctrank_base_v051_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_roc_base_v052_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_roc_base_v052_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_roc_base_v053_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_roc_base_v053_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_roc_base_v054_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_roc_base_v054_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_roc_base_v055_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_roc_base_v055_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_roc_base_v056_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_roc_base_v056_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_roc_base_v057_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_roc_base_v057_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_maxratio_base_v058_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_maxratio_base_v058_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_maxratio_base_v059_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_maxratio_base_v059_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_maxratio_base_v060_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_maxratio_base_v060_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_maxratio_base_v061_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_maxratio_base_v061_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_maxratio_base_v062_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_maxratio_base_v062_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_maxratio_base_v063_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_maxratio_base_v063_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv1_sign_base_v064_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv1_sign_base_v064_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv1_sign_base_v065_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv1_sign_base_v065_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv1_sign_base_v066_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv1_sign_base_v066_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv2_raw_base_v067_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv2_raw_base_v067_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv2_raw_base_v068_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv2_raw_base_v068_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_63dv2_raw_base_v069_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_63dv2_raw_base_v069_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v070_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v070_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v071_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v071_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v072_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_5dv2_zscore_base_v072_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v073_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v073_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v074_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v074_signal},
    "f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v075_signal": {"inputs": ["closeadj", "volume"], "func": f14mdi_momentum_divergence_mdi_price_roc_21dv2_zscore_base_v075_signal}
}
F14_MOMENTUM_DIVERGENCE_REGISTRY_001_075 = REGISTRY

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
        assert "_mdi_price_roc" in src or "_mdi_price_vs_vol_div" in src or "_mdi_fast_slow_div" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F14_MOMENTUM_DIVERGENCE_REGISTRY_001_075")
