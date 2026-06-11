import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _cbr_body_size(open_, close):
    return (close - open_).abs()
def _cbr_body_ratio(open_, close, high, low):
    body = _cbr_body_size(open_, close)
    total = (high - low).replace(0, np.nan)
    return body / total

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_5_base_v076_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_21_base_v077_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_63_base_v078_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_126_base_v079_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_252_base_v080_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_5_base_v081_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = b.rolling(5, min_periods=max(1, 5//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_21_base_v082_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = b.rolling(21, min_periods=max(1, 21//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_63_base_v083_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_126_base_v084_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = b.rolling(126, min_periods=max(1, 126//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# roc of _cbr_body_ratio period 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_roc_5_base_v085_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# roc of _cbr_body_ratio period 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_roc_21_base_v086_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 21d max of _cbr_body_ratio
def f06cbr_candle_body_ratios_cbr_body_ratio_maxratio_21_base_v087_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    mx = b.rolling(21, min_periods=max(1, 21//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _cbr_body_ratio
def f06cbr_candle_body_ratios_cbr_body_ratio_maxratio_63_base_v088_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sma ratio of _cbr_body_ratio sma=5d
def f06cbr_candle_body_ratios_cbr_body_ratio_sma_ratio_5_base_v089_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    sma = b.rolling(5, min_periods=max(1, 5//4)).mean()
    result = (b / sma.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sma ratio of _cbr_body_ratio sma=21d
def f06cbr_candle_body_ratios_cbr_body_ratio_sma_ratio_21_base_v090_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    sma = b.rolling(21, min_periods=max(1, 21//4)).mean()
    result = (b / sma.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v091_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v092_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v093_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v094_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v095_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v096_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v097_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v098_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v099_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v100_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v101_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v102_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v103_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v104_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v105_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v106_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v107_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v108_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v109_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v110_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v111_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v112_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v113_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v114_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v115_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v116_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v117_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v118_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v119_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v120_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v121_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v122_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v123_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v124_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v125_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v126_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v127_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v128_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v129_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v130_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v131_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v132_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v133_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v134_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v135_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v136_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v137_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v138_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v139_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v140_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v141_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v142_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v143_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v144_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v145_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 5d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v146_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 21d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v147_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 63d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v148_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 126d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v149_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _cbr_body_ratio over 252d
def f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v150_signal(open_, close, high, low):
    b = _cbr_body_ratio(open_, close, high, low)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_5_base_v076_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_5_base_v076_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_21_base_v077_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_21_base_v077_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_63_base_v078_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_63_base_v078_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_126_base_v079_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_126_base_v079_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_252_base_v080_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_252_base_v080_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_5_base_v081_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_5_base_v081_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_21_base_v082_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_21_base_v082_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_63_base_v083_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_63_base_v083_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_126_base_v084_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_pctrank_126_base_v084_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_roc_5_base_v085_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_roc_5_base_v085_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_roc_21_base_v086_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_roc_21_base_v086_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_maxratio_21_base_v087_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_maxratio_21_base_v087_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_maxratio_63_base_v088_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_maxratio_63_base_v088_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_sma_ratio_5_base_v089_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_sma_ratio_5_base_v089_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_sma_ratio_21_base_v090_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_sma_ratio_21_base_v090_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v091_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v091_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v092_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v092_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v093_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v093_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v094_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v094_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v095_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v095_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v096_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v096_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v097_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v097_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v098_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v098_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v099_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v099_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v100_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v100_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v101_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v101_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v102_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v102_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v103_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v103_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v104_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v104_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v105_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v105_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v106_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v106_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v107_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v107_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v108_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v108_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v109_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v109_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v110_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v110_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v111_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v111_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v112_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v112_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v113_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v113_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v114_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v114_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v115_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v115_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v116_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v116_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v117_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v117_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v118_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v118_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v119_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v119_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v120_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v120_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v121_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v121_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v122_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v122_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v123_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v123_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v124_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v124_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v125_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v125_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v126_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v126_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v127_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v127_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v128_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v128_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v129_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v129_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v130_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v130_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v131_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v131_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v132_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v132_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v133_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v133_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v134_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v134_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v135_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v135_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v136_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v136_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v137_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v137_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v138_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v138_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v139_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v139_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v140_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v140_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v141_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v141_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v142_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v142_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v143_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v143_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v144_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v144_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v145_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v145_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v146_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_5_base_v146_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v147_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_21_base_v147_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v148_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_63_base_v148_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v149_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_126_base_v149_signal},
    "f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v150_signal": {"inputs": ["open_", "close", "high", "low"], "func": f06cbr_candle_body_ratios_cbr_body_ratio_zscore_ext_252_base_v150_signal}
}
F06_CANDLE_BODY_RATIOS_REGISTRY_076_150 = REGISTRY

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
        assert "_cbr_body_size" in src or "_cbr_body_ratio" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F06_CANDLE_BODY_RATIOS_REGISTRY_076_150")
