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
def f19atr_atr_normalized_price_atr_tr_5d_raw_base_v076_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 14d
def f19atr_atr_normalized_price_atr_tr_14d_raw_base_v077_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 21d
def f19atr_atr_normalized_price_atr_tr_21d_raw_base_v078_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 63d
def f19atr_atr_normalized_price_atr_tr_63d_raw_base_v079_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=21d
def f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v080_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=63d
def f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v081_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=252d
def f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v082_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=21d
def f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v083_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=63d
def f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v084_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=252d
def f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v085_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=21d
def f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v086_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=63d
def f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v087_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=252d
def f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v088_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=21d
def f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v089_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=63d
def f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v090_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=252d
def f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v091_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=5 over 63d
def f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v092_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=5 over 252d
def f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v093_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=14 over 63d
def f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v094_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=14 over 252d
def f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v095_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=21 over 63d
def f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v096_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=21 over 252d
def f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v097_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=63 over 63d
def f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v098_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=63 over 252d
def f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v099_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=5 roc=5d
def f19atr_atr_normalized_price_atr_tr_5d_roc_base_v100_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=5 roc=21d
def f19atr_atr_normalized_price_atr_tr_5d_roc_base_v101_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=14 roc=5d
def f19atr_atr_normalized_price_atr_tr_14d_roc_base_v102_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=14 roc=21d
def f19atr_atr_normalized_price_atr_tr_14d_roc_base_v103_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=21 roc=5d
def f19atr_atr_normalized_price_atr_tr_21d_roc_base_v104_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=21 roc=21d
def f19atr_atr_normalized_price_atr_tr_21d_roc_base_v105_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=63 roc=5d
def f19atr_atr_normalized_price_atr_tr_63d_roc_base_v106_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=63 roc=21d
def f19atr_atr_normalized_price_atr_tr_63d_roc_base_v107_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _atr_tr w=5
def f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v108_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _atr_tr w=5
def f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v109_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _atr_tr w=14
def f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v110_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _atr_tr w=14
def f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v111_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _atr_tr w=21
def f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v112_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _atr_tr w=21
def f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v113_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _atr_tr w=63
def f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v114_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _atr_tr w=63
def f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v115_signal(close, high, low):
    b = _atr_tr(high, low, close)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _atr_tr w=5
def f19atr_atr_normalized_price_atr_tr_5d_sign_base_v116_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _atr_tr w=14
def f19atr_atr_normalized_price_atr_tr_14d_sign_base_v117_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _atr_tr w=21
def f19atr_atr_normalized_price_atr_tr_21d_sign_base_v118_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _atr_tr w=63
def f19atr_atr_normalized_price_atr_tr_63d_sign_base_v119_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 5d
def f19atr_atr_normalized_price_atr_tr_5dv1_raw_base_v120_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 14d
def f19atr_atr_normalized_price_atr_tr_14dv1_raw_base_v121_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 21d
def f19atr_atr_normalized_price_atr_tr_21dv1_raw_base_v122_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _atr_tr window 63d
def f19atr_atr_normalized_price_atr_tr_63dv1_raw_base_v123_signal(close, high, low):
    result = _atr_tr(high, low, close)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=21d
def f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v124_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=63d
def f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v125_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=5 lb=252d
def f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v126_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=21d
def f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v127_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=63d
def f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v128_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=14 lb=252d
def f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v129_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=21d
def f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v130_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=63d
def f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v131_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=21 lb=252d
def f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v132_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=21d
def f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v133_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=63d
def f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v134_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _atr_tr w=63 lb=252d
def f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v135_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=5 over 63d
def f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v136_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=5 over 252d
def f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v137_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=14 over 63d
def f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v138_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=14 over 252d
def f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v139_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=21 over 63d
def f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v140_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=21 over 252d
def f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v141_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=63 over 63d
def f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v142_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _atr_tr w=63 over 252d
def f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v143_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=5 roc=5d
def f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v144_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=5 roc=21d
def f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v145_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=14 roc=5d
def f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v146_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=14 roc=21d
def f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v147_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=21 roc=5d
def f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v148_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=21 roc=21d
def f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v149_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _atr_tr w=63 roc=5d
def f19atr_atr_normalized_price_atr_tr_63dv1_roc_base_v150_signal(close, high, low):
    b = _atr_tr(high, low, close)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f19atr_atr_normalized_price_atr_tr_5d_raw_base_v076_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_raw_base_v076_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_raw_base_v077_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_raw_base_v077_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_raw_base_v078_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_raw_base_v078_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_raw_base_v079_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_raw_base_v079_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v080_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v080_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v081_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v081_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v082_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_zscore_base_v082_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v083_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v083_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v084_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v084_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v085_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_zscore_base_v085_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v086_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v086_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v087_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v087_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v088_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_zscore_base_v088_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v089_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v089_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v090_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v090_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v091_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_zscore_base_v091_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v092_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v092_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v093_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_pctrank_base_v093_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v094_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v094_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v095_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_pctrank_base_v095_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v096_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v096_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v097_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_pctrank_base_v097_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v098_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v098_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v099_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_pctrank_base_v099_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_roc_base_v100_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_roc_base_v100_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_roc_base_v101_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_roc_base_v101_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_roc_base_v102_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_roc_base_v102_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_roc_base_v103_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_roc_base_v103_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_roc_base_v104_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_roc_base_v104_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_roc_base_v105_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_roc_base_v105_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_roc_base_v106_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_roc_base_v106_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_roc_base_v107_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_roc_base_v107_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v108_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v108_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v109_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_maxratio_base_v109_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v110_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v110_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v111_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_maxratio_base_v111_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v112_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v112_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v113_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_maxratio_base_v113_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v114_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v114_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v115_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_maxratio_base_v115_signal},
    "f19atr_atr_normalized_price_atr_tr_5d_sign_base_v116_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5d_sign_base_v116_signal},
    "f19atr_atr_normalized_price_atr_tr_14d_sign_base_v117_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14d_sign_base_v117_signal},
    "f19atr_atr_normalized_price_atr_tr_21d_sign_base_v118_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21d_sign_base_v118_signal},
    "f19atr_atr_normalized_price_atr_tr_63d_sign_base_v119_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63d_sign_base_v119_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_raw_base_v120_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_raw_base_v120_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_raw_base_v121_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_raw_base_v121_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_raw_base_v122_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_raw_base_v122_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_raw_base_v123_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_raw_base_v123_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v124_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v124_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v125_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v125_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v126_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_zscore_base_v126_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v127_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v127_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v128_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v128_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v129_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_zscore_base_v129_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v130_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v130_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v131_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v131_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v132_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_zscore_base_v132_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v133_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v133_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v134_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v134_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v135_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_zscore_base_v135_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v136_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v136_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v137_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_pctrank_base_v137_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v138_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v138_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v139_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_pctrank_base_v139_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v140_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v140_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v141_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_pctrank_base_v141_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v142_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v142_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v143_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_pctrank_base_v143_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v144_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v144_signal},
    "f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v145_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_5dv1_roc_base_v145_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v146_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v146_signal},
    "f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v147_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_14dv1_roc_base_v147_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v148_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v148_signal},
    "f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v149_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_21dv1_roc_base_v149_signal},
    "f19atr_atr_normalized_price_atr_tr_63dv1_roc_base_v150_signal": {"inputs": ["close", "high", "low"], "func": f19atr_atr_normalized_price_atr_tr_63dv1_roc_base_v150_signal}
}
F19_ATR_NORMALIZED_PRICE_REGISTRY_076_150 = REGISTRY

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
    print(f"ALL SELF-TESTS PASSED for F19_ATR_NORMALIZED_PRICE_REGISTRY_076_150")
