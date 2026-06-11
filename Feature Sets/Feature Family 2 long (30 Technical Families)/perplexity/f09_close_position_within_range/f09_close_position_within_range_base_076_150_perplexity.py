import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _cpwr_position(close, high, low):
    return (close - low) / (high - low).replace(0, np.nan)
def _cpwr_zscore(close, high, low, w):
    pos = _cpwr_position(close, high, low)
    mu = pos.rolling(w, min_periods=max(1, w//2)).mean()
    sd = pos.rolling(w, min_periods=max(1, w//2)).std()
    return (pos - mu) / sd.replace(0, np.nan)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_5_base_v076_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_21_base_v077_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_63_base_v078_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_126_base_v079_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_252_base_v080_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_pctrank_5_base_v081_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = b.rolling(5, min_periods=max(1, 5//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_pctrank_21_base_v082_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = b.rolling(21, min_periods=max(1, 21//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_pctrank_63_base_v083_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_pctrank_126_base_v084_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = b.rolling(126, min_periods=max(1, 126//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# roc of _cpwr_position period 5d
def f09cpwr_close_position_within_range_cpwr_position_roc_5_base_v085_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# roc of _cpwr_position period 21d
def f09cpwr_close_position_within_range_cpwr_position_roc_21_base_v086_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 21d max of _cpwr_position
def f09cpwr_close_position_within_range_cpwr_position_maxratio_21_base_v087_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    mx = b.rolling(21, min_periods=max(1, 21//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _cpwr_position
def f09cpwr_close_position_within_range_cpwr_position_maxratio_63_base_v088_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sma ratio of _cpwr_position sma=5d
def f09cpwr_close_position_within_range_cpwr_position_sma_ratio_5_base_v089_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    sma = b.rolling(5, min_periods=max(1, 5//4)).mean()
    result = (b / sma.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sma ratio of _cpwr_position sma=21d
def f09cpwr_close_position_within_range_cpwr_position_sma_ratio_21_base_v090_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    sma = b.rolling(21, min_periods=max(1, 21//4)).mean()
    result = (b / sma.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v091_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v092_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v093_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v094_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v095_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v096_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v097_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v098_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v099_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v100_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v101_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v102_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v103_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v104_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v105_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v106_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v107_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v108_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v109_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v110_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v111_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v112_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v113_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v114_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v115_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v116_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v117_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v118_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v119_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v120_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v121_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v122_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v123_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v124_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v125_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v126_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v127_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v128_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v129_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v130_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v131_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v132_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v133_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v134_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v135_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v136_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v137_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v138_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v139_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v140_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v141_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v142_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v143_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v144_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v145_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 5d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v146_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 21d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v147_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 63d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v148_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 126d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v149_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cpwr_position over 252d
def f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v150_signal(close, high, low):
    b = _cpwr_position(close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f09cpwr_close_position_within_range_cpwr_position_zscore_5_base_v076_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_5_base_v076_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_21_base_v077_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_21_base_v077_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_63_base_v078_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_63_base_v078_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_126_base_v079_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_126_base_v079_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_252_base_v080_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_252_base_v080_signal},
    "f09cpwr_close_position_within_range_cpwr_position_pctrank_5_base_v081_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_pctrank_5_base_v081_signal},
    "f09cpwr_close_position_within_range_cpwr_position_pctrank_21_base_v082_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_pctrank_21_base_v082_signal},
    "f09cpwr_close_position_within_range_cpwr_position_pctrank_63_base_v083_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_pctrank_63_base_v083_signal},
    "f09cpwr_close_position_within_range_cpwr_position_pctrank_126_base_v084_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_pctrank_126_base_v084_signal},
    "f09cpwr_close_position_within_range_cpwr_position_roc_5_base_v085_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_roc_5_base_v085_signal},
    "f09cpwr_close_position_within_range_cpwr_position_roc_21_base_v086_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_roc_21_base_v086_signal},
    "f09cpwr_close_position_within_range_cpwr_position_maxratio_21_base_v087_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_maxratio_21_base_v087_signal},
    "f09cpwr_close_position_within_range_cpwr_position_maxratio_63_base_v088_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_maxratio_63_base_v088_signal},
    "f09cpwr_close_position_within_range_cpwr_position_sma_ratio_5_base_v089_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_sma_ratio_5_base_v089_signal},
    "f09cpwr_close_position_within_range_cpwr_position_sma_ratio_21_base_v090_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_sma_ratio_21_base_v090_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v091_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v091_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v092_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v092_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v093_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v093_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v094_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v094_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v095_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v095_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v096_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v096_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v097_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v097_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v098_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v098_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v099_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v099_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v100_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v100_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v101_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v101_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v102_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v102_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v103_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v103_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v104_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v104_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v105_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v105_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v106_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v106_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v107_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v107_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v108_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v108_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v109_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v109_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v110_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v110_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v111_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v111_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v112_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v112_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v113_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v113_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v114_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v114_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v115_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v115_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v116_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v116_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v117_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v117_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v118_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v118_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v119_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v119_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v120_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v120_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v121_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v121_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v122_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v122_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v123_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v123_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v124_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v124_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v125_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v125_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v126_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v126_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v127_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v127_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v128_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v128_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v129_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v129_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v130_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v130_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v131_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v131_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v132_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v132_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v133_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v133_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v134_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v134_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v135_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v135_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v136_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v136_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v137_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v137_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v138_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v138_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v139_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v139_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v140_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v140_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v141_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v141_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v142_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v142_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v143_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v143_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v144_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v144_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v145_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v145_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v146_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_5_base_v146_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v147_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_21_base_v147_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v148_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_63_base_v148_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v149_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_126_base_v149_signal},
    "f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v150_signal": {"inputs": ["close", "high", "low"], "func": f09cpwr_close_position_within_range_cpwr_position_zscore_ext_252_base_v150_signal}
}
F09_CLOSE_POSITION_WITHIN_RANGE_REGISTRY_076_150 = REGISTRY

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
        assert "_cpwr_position" in src or "_cpwr_zscore" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F09_CLOSE_POSITION_WITHIN_RANGE_REGISTRY_076_150")
