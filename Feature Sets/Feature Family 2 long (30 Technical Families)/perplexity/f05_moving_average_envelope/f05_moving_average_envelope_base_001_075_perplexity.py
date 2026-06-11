import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _mae_upper_band(closeadj, w, pct):
    sma = closeadj.rolling(w, min_periods=max(1, w//2)).mean()
    return sma * (1 + pct)
def _mae_lower_band(closeadj, w, pct):
    sma = closeadj.rolling(w, min_periods=max(1, w//2)).mean()
    return sma * (1 - pct)
def _mae_position(closeadj, w, pct):
    upper = _mae_upper_band(closeadj, w, pct)
    lower = _mae_lower_band(closeadj, w, pct)
    return (closeadj - lower) / (upper - lower).replace(0, np.nan)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _mae_position window 5d
def f05mae_moving_average_envelope_mae_position_5d_raw_base_v001_signal(closeadj):
    result = _mae_position(closeadj, 5, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mae_position window 10d
def f05mae_moving_average_envelope_mae_position_10d_raw_base_v002_signal(closeadj):
    result = _mae_position(closeadj, 10, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mae_position window 21d
def f05mae_moving_average_envelope_mae_position_21d_raw_base_v003_signal(closeadj):
    result = _mae_position(closeadj, 21, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mae_position window 63d
def f05mae_moving_average_envelope_mae_position_63d_raw_base_v004_signal(closeadj):
    result = _mae_position(closeadj, 63, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mae_position window 126d
def f05mae_moving_average_envelope_mae_position_126d_raw_base_v005_signal(closeadj):
    result = _mae_position(closeadj, 126, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mae_position window 252d
def f05mae_moving_average_envelope_mae_position_252d_raw_base_v006_signal(closeadj):
    result = _mae_position(closeadj, 252, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=5 lb=21d
def f05mae_moving_average_envelope_mae_position_5d_zscore_base_v007_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=5 lb=63d
def f05mae_moving_average_envelope_mae_position_5d_zscore_base_v008_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=5 lb=252d
def f05mae_moving_average_envelope_mae_position_5d_zscore_base_v009_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=10 lb=21d
def f05mae_moving_average_envelope_mae_position_10d_zscore_base_v010_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=10 lb=63d
def f05mae_moving_average_envelope_mae_position_10d_zscore_base_v011_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=10 lb=252d
def f05mae_moving_average_envelope_mae_position_10d_zscore_base_v012_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=21 lb=21d
def f05mae_moving_average_envelope_mae_position_21d_zscore_base_v013_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=21 lb=63d
def f05mae_moving_average_envelope_mae_position_21d_zscore_base_v014_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=21 lb=252d
def f05mae_moving_average_envelope_mae_position_21d_zscore_base_v015_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=63 lb=21d
def f05mae_moving_average_envelope_mae_position_63d_zscore_base_v016_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=63 lb=63d
def f05mae_moving_average_envelope_mae_position_63d_zscore_base_v017_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=63 lb=252d
def f05mae_moving_average_envelope_mae_position_63d_zscore_base_v018_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=126 lb=21d
def f05mae_moving_average_envelope_mae_position_126d_zscore_base_v019_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=126 lb=63d
def f05mae_moving_average_envelope_mae_position_126d_zscore_base_v020_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=126 lb=252d
def f05mae_moving_average_envelope_mae_position_126d_zscore_base_v021_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=252 lb=21d
def f05mae_moving_average_envelope_mae_position_252d_zscore_base_v022_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=252 lb=63d
def f05mae_moving_average_envelope_mae_position_252d_zscore_base_v023_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _mae_position w=252 lb=252d
def f05mae_moving_average_envelope_mae_position_252d_zscore_base_v024_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=5 over 63d
def f05mae_moving_average_envelope_mae_position_5d_pctrank_base_v025_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=5 over 252d
def f05mae_moving_average_envelope_mae_position_5d_pctrank_base_v026_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=10 over 63d
def f05mae_moving_average_envelope_mae_position_10d_pctrank_base_v027_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=10 over 252d
def f05mae_moving_average_envelope_mae_position_10d_pctrank_base_v028_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=21 over 63d
def f05mae_moving_average_envelope_mae_position_21d_pctrank_base_v029_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=21 over 252d
def f05mae_moving_average_envelope_mae_position_21d_pctrank_base_v030_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=63 over 63d
def f05mae_moving_average_envelope_mae_position_63d_pctrank_base_v031_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=63 over 252d
def f05mae_moving_average_envelope_mae_position_63d_pctrank_base_v032_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=126 over 63d
def f05mae_moving_average_envelope_mae_position_126d_pctrank_base_v033_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=126 over 252d
def f05mae_moving_average_envelope_mae_position_126d_pctrank_base_v034_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=252 over 63d
def f05mae_moving_average_envelope_mae_position_252d_pctrank_base_v035_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _mae_position w=252 over 252d
def f05mae_moving_average_envelope_mae_position_252d_pctrank_base_v036_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=5 roc=5d
def f05mae_moving_average_envelope_mae_position_5d_roc_base_v037_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=5 roc=21d
def f05mae_moving_average_envelope_mae_position_5d_roc_base_v038_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=5 roc=63d
def f05mae_moving_average_envelope_mae_position_5d_roc_base_v039_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=10 roc=5d
def f05mae_moving_average_envelope_mae_position_10d_roc_base_v040_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=10 roc=21d
def f05mae_moving_average_envelope_mae_position_10d_roc_base_v041_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=10 roc=63d
def f05mae_moving_average_envelope_mae_position_10d_roc_base_v042_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=21 roc=5d
def f05mae_moving_average_envelope_mae_position_21d_roc_base_v043_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=21 roc=21d
def f05mae_moving_average_envelope_mae_position_21d_roc_base_v044_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=21 roc=63d
def f05mae_moving_average_envelope_mae_position_21d_roc_base_v045_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=63 roc=5d
def f05mae_moving_average_envelope_mae_position_63d_roc_base_v046_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=63 roc=21d
def f05mae_moving_average_envelope_mae_position_63d_roc_base_v047_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=63 roc=63d
def f05mae_moving_average_envelope_mae_position_63d_roc_base_v048_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=126 roc=5d
def f05mae_moving_average_envelope_mae_position_126d_roc_base_v049_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=126 roc=21d
def f05mae_moving_average_envelope_mae_position_126d_roc_base_v050_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=126 roc=63d
def f05mae_moving_average_envelope_mae_position_126d_roc_base_v051_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=252 roc=5d
def f05mae_moving_average_envelope_mae_position_252d_roc_base_v052_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=252 roc=21d
def f05mae_moving_average_envelope_mae_position_252d_roc_base_v053_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _mae_position w=252 roc=63d
def f05mae_moving_average_envelope_mae_position_252d_roc_base_v054_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mae_position w=5
def f05mae_moving_average_envelope_mae_position_5d_maxratio_base_v055_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mae_position w=5
def f05mae_moving_average_envelope_mae_position_5d_maxratio_base_v056_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mae_position w=10
def f05mae_moving_average_envelope_mae_position_10d_maxratio_base_v057_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mae_position w=10
def f05mae_moving_average_envelope_mae_position_10d_maxratio_base_v058_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mae_position w=21
def f05mae_moving_average_envelope_mae_position_21d_maxratio_base_v059_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mae_position w=21
def f05mae_moving_average_envelope_mae_position_21d_maxratio_base_v060_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mae_position w=63
def f05mae_moving_average_envelope_mae_position_63d_maxratio_base_v061_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mae_position w=63
def f05mae_moving_average_envelope_mae_position_63d_maxratio_base_v062_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mae_position w=126
def f05mae_moving_average_envelope_mae_position_126d_maxratio_base_v063_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mae_position w=126
def f05mae_moving_average_envelope_mae_position_126d_maxratio_base_v064_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _mae_position w=252
def f05mae_moving_average_envelope_mae_position_252d_maxratio_base_v065_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _mae_position w=252
def f05mae_moving_average_envelope_mae_position_252d_maxratio_base_v066_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mae_position w=5
def f05mae_moving_average_envelope_mae_position_5d_sign_base_v067_signal(closeadj):
    b = _mae_position(closeadj, 5, 0.05)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mae_position w=10
def f05mae_moving_average_envelope_mae_position_10d_sign_base_v068_signal(closeadj):
    b = _mae_position(closeadj, 10, 0.05)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mae_position w=21
def f05mae_moving_average_envelope_mae_position_21d_sign_base_v069_signal(closeadj):
    b = _mae_position(closeadj, 21, 0.05)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mae_position w=63
def f05mae_moving_average_envelope_mae_position_63d_sign_base_v070_signal(closeadj):
    b = _mae_position(closeadj, 63, 0.05)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mae_position w=126
def f05mae_moving_average_envelope_mae_position_126d_sign_base_v071_signal(closeadj):
    b = _mae_position(closeadj, 126, 0.05)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _mae_position w=252
def f05mae_moving_average_envelope_mae_position_252d_sign_base_v072_signal(closeadj):
    b = _mae_position(closeadj, 252, 0.05)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mae_position window 5d
def f05mae_moving_average_envelope_mae_position_5dv1_raw_base_v073_signal(closeadj):
    result = _mae_position(closeadj, 5, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mae_position window 10d
def f05mae_moving_average_envelope_mae_position_10dv1_raw_base_v074_signal(closeadj):
    result = _mae_position(closeadj, 10, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _mae_position window 21d
def f05mae_moving_average_envelope_mae_position_21dv1_raw_base_v075_signal(closeadj):
    result = _mae_position(closeadj, 21, 0.05)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f05mae_moving_average_envelope_mae_position_5d_raw_base_v001_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_raw_base_v001_signal},
    "f05mae_moving_average_envelope_mae_position_10d_raw_base_v002_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_raw_base_v002_signal},
    "f05mae_moving_average_envelope_mae_position_21d_raw_base_v003_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_raw_base_v003_signal},
    "f05mae_moving_average_envelope_mae_position_63d_raw_base_v004_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_raw_base_v004_signal},
    "f05mae_moving_average_envelope_mae_position_126d_raw_base_v005_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_raw_base_v005_signal},
    "f05mae_moving_average_envelope_mae_position_252d_raw_base_v006_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_raw_base_v006_signal},
    "f05mae_moving_average_envelope_mae_position_5d_zscore_base_v007_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_zscore_base_v007_signal},
    "f05mae_moving_average_envelope_mae_position_5d_zscore_base_v008_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_zscore_base_v008_signal},
    "f05mae_moving_average_envelope_mae_position_5d_zscore_base_v009_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_zscore_base_v009_signal},
    "f05mae_moving_average_envelope_mae_position_10d_zscore_base_v010_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_zscore_base_v010_signal},
    "f05mae_moving_average_envelope_mae_position_10d_zscore_base_v011_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_zscore_base_v011_signal},
    "f05mae_moving_average_envelope_mae_position_10d_zscore_base_v012_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_zscore_base_v012_signal},
    "f05mae_moving_average_envelope_mae_position_21d_zscore_base_v013_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_zscore_base_v013_signal},
    "f05mae_moving_average_envelope_mae_position_21d_zscore_base_v014_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_zscore_base_v014_signal},
    "f05mae_moving_average_envelope_mae_position_21d_zscore_base_v015_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_zscore_base_v015_signal},
    "f05mae_moving_average_envelope_mae_position_63d_zscore_base_v016_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_zscore_base_v016_signal},
    "f05mae_moving_average_envelope_mae_position_63d_zscore_base_v017_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_zscore_base_v017_signal},
    "f05mae_moving_average_envelope_mae_position_63d_zscore_base_v018_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_zscore_base_v018_signal},
    "f05mae_moving_average_envelope_mae_position_126d_zscore_base_v019_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_zscore_base_v019_signal},
    "f05mae_moving_average_envelope_mae_position_126d_zscore_base_v020_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_zscore_base_v020_signal},
    "f05mae_moving_average_envelope_mae_position_126d_zscore_base_v021_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_zscore_base_v021_signal},
    "f05mae_moving_average_envelope_mae_position_252d_zscore_base_v022_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_zscore_base_v022_signal},
    "f05mae_moving_average_envelope_mae_position_252d_zscore_base_v023_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_zscore_base_v023_signal},
    "f05mae_moving_average_envelope_mae_position_252d_zscore_base_v024_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_zscore_base_v024_signal},
    "f05mae_moving_average_envelope_mae_position_5d_pctrank_base_v025_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_pctrank_base_v025_signal},
    "f05mae_moving_average_envelope_mae_position_5d_pctrank_base_v026_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_pctrank_base_v026_signal},
    "f05mae_moving_average_envelope_mae_position_10d_pctrank_base_v027_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_pctrank_base_v027_signal},
    "f05mae_moving_average_envelope_mae_position_10d_pctrank_base_v028_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_pctrank_base_v028_signal},
    "f05mae_moving_average_envelope_mae_position_21d_pctrank_base_v029_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_pctrank_base_v029_signal},
    "f05mae_moving_average_envelope_mae_position_21d_pctrank_base_v030_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_pctrank_base_v030_signal},
    "f05mae_moving_average_envelope_mae_position_63d_pctrank_base_v031_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_pctrank_base_v031_signal},
    "f05mae_moving_average_envelope_mae_position_63d_pctrank_base_v032_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_pctrank_base_v032_signal},
    "f05mae_moving_average_envelope_mae_position_126d_pctrank_base_v033_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_pctrank_base_v033_signal},
    "f05mae_moving_average_envelope_mae_position_126d_pctrank_base_v034_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_pctrank_base_v034_signal},
    "f05mae_moving_average_envelope_mae_position_252d_pctrank_base_v035_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_pctrank_base_v035_signal},
    "f05mae_moving_average_envelope_mae_position_252d_pctrank_base_v036_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_pctrank_base_v036_signal},
    "f05mae_moving_average_envelope_mae_position_5d_roc_base_v037_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_roc_base_v037_signal},
    "f05mae_moving_average_envelope_mae_position_5d_roc_base_v038_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_roc_base_v038_signal},
    "f05mae_moving_average_envelope_mae_position_5d_roc_base_v039_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_roc_base_v039_signal},
    "f05mae_moving_average_envelope_mae_position_10d_roc_base_v040_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_roc_base_v040_signal},
    "f05mae_moving_average_envelope_mae_position_10d_roc_base_v041_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_roc_base_v041_signal},
    "f05mae_moving_average_envelope_mae_position_10d_roc_base_v042_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_roc_base_v042_signal},
    "f05mae_moving_average_envelope_mae_position_21d_roc_base_v043_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_roc_base_v043_signal},
    "f05mae_moving_average_envelope_mae_position_21d_roc_base_v044_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_roc_base_v044_signal},
    "f05mae_moving_average_envelope_mae_position_21d_roc_base_v045_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_roc_base_v045_signal},
    "f05mae_moving_average_envelope_mae_position_63d_roc_base_v046_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_roc_base_v046_signal},
    "f05mae_moving_average_envelope_mae_position_63d_roc_base_v047_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_roc_base_v047_signal},
    "f05mae_moving_average_envelope_mae_position_63d_roc_base_v048_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_roc_base_v048_signal},
    "f05mae_moving_average_envelope_mae_position_126d_roc_base_v049_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_roc_base_v049_signal},
    "f05mae_moving_average_envelope_mae_position_126d_roc_base_v050_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_roc_base_v050_signal},
    "f05mae_moving_average_envelope_mae_position_126d_roc_base_v051_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_roc_base_v051_signal},
    "f05mae_moving_average_envelope_mae_position_252d_roc_base_v052_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_roc_base_v052_signal},
    "f05mae_moving_average_envelope_mae_position_252d_roc_base_v053_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_roc_base_v053_signal},
    "f05mae_moving_average_envelope_mae_position_252d_roc_base_v054_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_roc_base_v054_signal},
    "f05mae_moving_average_envelope_mae_position_5d_maxratio_base_v055_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_maxratio_base_v055_signal},
    "f05mae_moving_average_envelope_mae_position_5d_maxratio_base_v056_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_maxratio_base_v056_signal},
    "f05mae_moving_average_envelope_mae_position_10d_maxratio_base_v057_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_maxratio_base_v057_signal},
    "f05mae_moving_average_envelope_mae_position_10d_maxratio_base_v058_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_maxratio_base_v058_signal},
    "f05mae_moving_average_envelope_mae_position_21d_maxratio_base_v059_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_maxratio_base_v059_signal},
    "f05mae_moving_average_envelope_mae_position_21d_maxratio_base_v060_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_maxratio_base_v060_signal},
    "f05mae_moving_average_envelope_mae_position_63d_maxratio_base_v061_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_maxratio_base_v061_signal},
    "f05mae_moving_average_envelope_mae_position_63d_maxratio_base_v062_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_maxratio_base_v062_signal},
    "f05mae_moving_average_envelope_mae_position_126d_maxratio_base_v063_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_maxratio_base_v063_signal},
    "f05mae_moving_average_envelope_mae_position_126d_maxratio_base_v064_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_maxratio_base_v064_signal},
    "f05mae_moving_average_envelope_mae_position_252d_maxratio_base_v065_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_maxratio_base_v065_signal},
    "f05mae_moving_average_envelope_mae_position_252d_maxratio_base_v066_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_maxratio_base_v066_signal},
    "f05mae_moving_average_envelope_mae_position_5d_sign_base_v067_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5d_sign_base_v067_signal},
    "f05mae_moving_average_envelope_mae_position_10d_sign_base_v068_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10d_sign_base_v068_signal},
    "f05mae_moving_average_envelope_mae_position_21d_sign_base_v069_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21d_sign_base_v069_signal},
    "f05mae_moving_average_envelope_mae_position_63d_sign_base_v070_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_63d_sign_base_v070_signal},
    "f05mae_moving_average_envelope_mae_position_126d_sign_base_v071_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_126d_sign_base_v071_signal},
    "f05mae_moving_average_envelope_mae_position_252d_sign_base_v072_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_252d_sign_base_v072_signal},
    "f05mae_moving_average_envelope_mae_position_5dv1_raw_base_v073_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_5dv1_raw_base_v073_signal},
    "f05mae_moving_average_envelope_mae_position_10dv1_raw_base_v074_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_10dv1_raw_base_v074_signal},
    "f05mae_moving_average_envelope_mae_position_21dv1_raw_base_v075_signal": {"inputs": ["closeadj"], "func": f05mae_moving_average_envelope_mae_position_21dv1_raw_base_v075_signal}
}
F05_MOVING_AVERAGE_ENVELOPE_REGISTRY_001_075 = REGISTRY

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
        assert "_mae_upper_band" in src or "_mae_lower_band" in src or "_mae_position" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F05_MOVING_AVERAGE_ENVELOPE_REGISTRY_001_075")
