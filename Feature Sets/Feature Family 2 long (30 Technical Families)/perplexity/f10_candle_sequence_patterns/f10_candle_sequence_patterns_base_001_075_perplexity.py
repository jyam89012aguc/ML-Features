import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _csp_direction(open_, close):
    return np.sign(close - open_)
def _csp_sequence_score(open_, close, w):
    d = _csp_direction(open_, close)
    return d.rolling(w, min_periods=max(1, w//2)).sum() / w

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_5_base_v001_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_21_base_v002_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_63_base_v003_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_126_base_v004_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_252_base_v005_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_pctrank_5_base_v006_signal(open_, close):
    b = _csp_direction(open_, close)
    result = b.rolling(5, min_periods=max(1, 5//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_pctrank_21_base_v007_signal(open_, close):
    b = _csp_direction(open_, close)
    result = b.rolling(21, min_periods=max(1, 21//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_pctrank_63_base_v008_signal(open_, close):
    b = _csp_direction(open_, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_pctrank_126_base_v009_signal(open_, close):
    b = _csp_direction(open_, close)
    result = b.rolling(126, min_periods=max(1, 126//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# roc of _csp_direction period 5d
def f10csp_candle_sequence_patterns_csp_direction_roc_5_base_v010_signal(open_, close):
    b = _csp_direction(open_, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# roc of _csp_direction period 21d
def f10csp_candle_sequence_patterns_csp_direction_roc_21_base_v011_signal(open_, close):
    b = _csp_direction(open_, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 21d max of _csp_direction
def f10csp_candle_sequence_patterns_csp_direction_maxratio_21_base_v012_signal(open_, close):
    b = _csp_direction(open_, close)
    mx = b.rolling(21, min_periods=max(1, 21//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _csp_direction
def f10csp_candle_sequence_patterns_csp_direction_maxratio_63_base_v013_signal(open_, close):
    b = _csp_direction(open_, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sma ratio of _csp_direction sma=5d
def f10csp_candle_sequence_patterns_csp_direction_sma_ratio_5_base_v014_signal(open_, close):
    b = _csp_direction(open_, close)
    sma = b.rolling(5, min_periods=max(1, 5//4)).mean()
    result = (b / sma.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sma ratio of _csp_direction sma=21d
def f10csp_candle_sequence_patterns_csp_direction_sma_ratio_21_base_v015_signal(open_, close):
    b = _csp_direction(open_, close)
    sma = b.rolling(21, min_periods=max(1, 21//4)).mean()
    result = (b / sma.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v016_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v017_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v018_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v019_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v020_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v021_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v022_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v023_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v024_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v025_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v026_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v027_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v028_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v029_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v030_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v031_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v032_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v033_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v034_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v035_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v036_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v037_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v038_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v039_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v040_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v041_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v042_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v043_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v044_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v045_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v046_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v047_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v048_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v049_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v050_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v051_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v052_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v053_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v054_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v055_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v056_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v057_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v058_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v059_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v060_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v061_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v062_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v063_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v064_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v065_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v066_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v067_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v068_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v069_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v070_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 5d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v071_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 21d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v072_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 63d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v073_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 126d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v074_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _csp_direction over 252d
def f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v075_signal(open_, close):
    b = _csp_direction(open_, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f10csp_candle_sequence_patterns_csp_direction_zscore_5_base_v001_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_5_base_v001_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_21_base_v002_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_21_base_v002_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_63_base_v003_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_63_base_v003_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_126_base_v004_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_126_base_v004_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_252_base_v005_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_252_base_v005_signal},
    "f10csp_candle_sequence_patterns_csp_direction_pctrank_5_base_v006_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_pctrank_5_base_v006_signal},
    "f10csp_candle_sequence_patterns_csp_direction_pctrank_21_base_v007_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_pctrank_21_base_v007_signal},
    "f10csp_candle_sequence_patterns_csp_direction_pctrank_63_base_v008_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_pctrank_63_base_v008_signal},
    "f10csp_candle_sequence_patterns_csp_direction_pctrank_126_base_v009_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_pctrank_126_base_v009_signal},
    "f10csp_candle_sequence_patterns_csp_direction_roc_5_base_v010_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_roc_5_base_v010_signal},
    "f10csp_candle_sequence_patterns_csp_direction_roc_21_base_v011_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_roc_21_base_v011_signal},
    "f10csp_candle_sequence_patterns_csp_direction_maxratio_21_base_v012_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_maxratio_21_base_v012_signal},
    "f10csp_candle_sequence_patterns_csp_direction_maxratio_63_base_v013_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_maxratio_63_base_v013_signal},
    "f10csp_candle_sequence_patterns_csp_direction_sma_ratio_5_base_v014_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_sma_ratio_5_base_v014_signal},
    "f10csp_candle_sequence_patterns_csp_direction_sma_ratio_21_base_v015_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_sma_ratio_21_base_v015_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v016_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v016_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v017_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v017_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v018_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v018_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v019_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v019_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v020_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v020_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v021_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v021_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v022_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v022_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v023_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v023_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v024_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v024_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v025_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v025_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v026_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v026_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v027_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v027_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v028_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v028_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v029_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v029_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v030_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v030_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v031_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v031_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v032_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v032_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v033_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v033_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v034_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v034_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v035_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v035_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v036_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v036_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v037_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v037_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v038_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v038_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v039_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v039_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v040_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v040_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v041_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v041_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v042_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v042_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v043_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v043_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v044_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v044_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v045_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v045_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v046_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v046_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v047_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v047_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v048_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v048_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v049_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v049_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v050_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v050_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v051_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v051_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v052_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v052_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v053_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v053_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v054_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v054_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v055_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v055_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v056_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v056_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v057_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v057_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v058_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v058_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v059_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v059_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v060_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v060_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v061_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v061_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v062_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v062_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v063_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v063_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v064_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v064_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v065_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v065_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v066_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v066_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v067_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v067_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v068_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v068_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v069_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v069_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v070_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v070_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v071_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_5_base_v071_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v072_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_21_base_v072_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v073_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_63_base_v073_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v074_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_126_base_v074_signal},
    "f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v075_signal": {"inputs": ["open_", "close"], "func": f10csp_candle_sequence_patterns_csp_direction_zscore_ext_252_base_v075_signal}
}
F10_CANDLE_SEQUENCE_PATTERNS_REGISTRY_001_075 = REGISTRY

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
        assert "_csp_direction" in src or "_csp_sequence_score" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F10_CANDLE_SEQUENCE_PATTERNS_REGISTRY_001_075")
