import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _pgk_parkinson(high, low, w):
    lhl = np.log(high / low.replace(0, np.nan))
    return np.sqrt(lhl.pow(2).rolling(w, min_periods=max(1, w//2)).mean() / (4 * np.log(2))) * np.sqrt(252)
def _pgk_garman_klass(open_, high, low, close, w):
    lhl = np.log(high / low.replace(0, np.nan))
    lco = np.log(close / open_.replace(0, np.nan))
    gk = 0.5 * lhl.pow(2) - (2 * np.log(2) - 1) * lco.pow(2)
    return np.sqrt(gk.rolling(w, min_periods=max(1, w//2)).mean() * 252)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _pgk_parkinson window 5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_raw_base_v001_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_raw_base_v002_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_raw_base_v003_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 126d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_raw_base_v004_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v005_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v006_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v007_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v008_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v009_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v010_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v011_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v012_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v013_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v014_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v015_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v016_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=5 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v017_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=5 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v018_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=21 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v019_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=21 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v020_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=63 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v021_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=63 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v022_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=126 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v023_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=126 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v024_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v025_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v026_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v027_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v028_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v029_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v030_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v031_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v032_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v033_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v034_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v035_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v036_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _pgk_parkinson w=5
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v037_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _pgk_parkinson w=5
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v038_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _pgk_parkinson w=21
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v039_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _pgk_parkinson w=21
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v040_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _pgk_parkinson w=63
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v041_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _pgk_parkinson w=63
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v042_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _pgk_parkinson w=126
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v043_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _pgk_parkinson w=126
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v044_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _pgk_parkinson w=5
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_sign_base_v045_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _pgk_parkinson w=21
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_sign_base_v046_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _pgk_parkinson w=63
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_sign_base_v047_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _pgk_parkinson w=126
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_sign_base_v048_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_raw_base_v049_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_raw_base_v050_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_raw_base_v051_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 126d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_raw_base_v052_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v053_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v054_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v055_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v056_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v057_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v058_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v059_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v060_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v061_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v062_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v063_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v064_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=5 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v065_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=5 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v066_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=21 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v067_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=21 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v068_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=63 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v069_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=63 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v070_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=126 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v071_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=126 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v072_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v073_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v074_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v075_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_raw_base_v001_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_raw_base_v001_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_raw_base_v002_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_raw_base_v002_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_raw_base_v003_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_raw_base_v003_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_raw_base_v004_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_raw_base_v004_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v005_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v005_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v006_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v006_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v007_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v007_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v008_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v008_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v009_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v009_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v010_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v010_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v011_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v011_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v012_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v012_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v013_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v013_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v014_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v014_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v015_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v015_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v016_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v016_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v017_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v017_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v018_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v018_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v019_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v019_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v020_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v020_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v021_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v021_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v022_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v022_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v023_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v023_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v024_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v024_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v025_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v025_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v026_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v026_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v027_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v027_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v028_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v028_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v029_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v029_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v030_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v030_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v031_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v031_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v032_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v032_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v033_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v033_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v034_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v034_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v035_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v035_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v036_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v036_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v037_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v037_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v038_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v038_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v039_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v039_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v040_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v040_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v041_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v041_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v042_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v042_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v043_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v043_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v044_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v044_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_sign_base_v045_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_sign_base_v045_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_sign_base_v046_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_sign_base_v046_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_sign_base_v047_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_sign_base_v047_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_sign_base_v048_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_sign_base_v048_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_raw_base_v049_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_raw_base_v049_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_raw_base_v050_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_raw_base_v050_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_raw_base_v051_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_raw_base_v051_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_raw_base_v052_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_raw_base_v052_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v053_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v053_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v054_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v054_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v055_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v055_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v056_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v056_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v057_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v057_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v058_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v058_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v059_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v059_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v060_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v060_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v061_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v061_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v062_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v062_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v063_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v063_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v064_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v064_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v065_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v065_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v066_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v066_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v067_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v067_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v068_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v068_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v069_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v069_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v070_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v070_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v071_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v071_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v072_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v072_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v073_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v073_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v074_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v074_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v075_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v075_signal}
}
F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_001_075 = REGISTRY

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
        assert "_pgk_parkinson" in src or "_pgk_garman_klass" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_001_075")
