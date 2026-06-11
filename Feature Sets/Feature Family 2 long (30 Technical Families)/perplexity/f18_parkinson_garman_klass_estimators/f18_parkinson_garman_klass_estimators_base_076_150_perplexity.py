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
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_raw_base_v076_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_raw_base_v077_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_raw_base_v078_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 126d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_raw_base_v079_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v080_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v081_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v082_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v083_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v084_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v085_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v086_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v087_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v088_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v089_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v090_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v091_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=5 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v092_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=5 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v093_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=21 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v094_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=21 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v095_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=63 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v096_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=63 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v097_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=126 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v098_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=126 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v099_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v100_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v101_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v102_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=21 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v103_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=21 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v104_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=21 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v105_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=63 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v106_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=63 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v107_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=63 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v108_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=126 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v109_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=126 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v110_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=126 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v111_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _pgk_parkinson w=5
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v112_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _pgk_parkinson w=5
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v113_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _pgk_parkinson w=21
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v114_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _pgk_parkinson w=21
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v115_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _pgk_parkinson w=63
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v116_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _pgk_parkinson w=63
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v117_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _pgk_parkinson w=126
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v118_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _pgk_parkinson w=126
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v119_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _pgk_parkinson w=5
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_sign_base_v120_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _pgk_parkinson w=21
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_sign_base_v121_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _pgk_parkinson w=63
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_sign_base_v122_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _pgk_parkinson w=126
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_sign_base_v123_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_raw_base_v124_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_raw_base_v125_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_raw_base_v126_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _pgk_parkinson window 126d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_raw_base_v127_signal(open_, high, low, close):
    result = _pgk_parkinson(high, low, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v128_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v129_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=5 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v130_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v131_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v132_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=21 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v133_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v134_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v135_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=63 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v136_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v137_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v138_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _pgk_parkinson w=126 lb=252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v139_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=5 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v140_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=5 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v141_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=21 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v142_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=21 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v143_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=63 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v144_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=63 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v145_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=126 over 63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v146_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _pgk_parkinson w=126 over 252d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v147_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 126)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=5d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v148_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=21d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v149_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _pgk_parkinson w=5 roc=63d
def f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v150_signal(open_, high, low, close):
    b = _pgk_parkinson(high, low, 5)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_raw_base_v076_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_raw_base_v076_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_raw_base_v077_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_raw_base_v077_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_raw_base_v078_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_raw_base_v078_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_raw_base_v079_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_raw_base_v079_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v080_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v080_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v081_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v081_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v082_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_zscore_base_v082_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v083_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v083_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v084_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v084_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v085_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_zscore_base_v085_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v086_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v086_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v087_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v087_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v088_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_zscore_base_v088_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v089_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v089_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v090_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v090_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v091_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_zscore_base_v091_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v092_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v092_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v093_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_pctrank_base_v093_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v094_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v094_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v095_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_pctrank_base_v095_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v096_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v096_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v097_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_pctrank_base_v097_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v098_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v098_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v099_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_pctrank_base_v099_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v100_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v100_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v101_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v101_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v102_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_roc_base_v102_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v103_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v103_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v104_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v104_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v105_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_roc_base_v105_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v106_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v106_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v107_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v107_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v108_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_roc_base_v108_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v109_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v109_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v110_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v110_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v111_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_roc_base_v111_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v112_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v112_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v113_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_maxratio_base_v113_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v114_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v114_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v115_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_maxratio_base_v115_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v116_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v116_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v117_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_maxratio_base_v117_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v118_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v118_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v119_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_maxratio_base_v119_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_sign_base_v120_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5d_sign_base_v120_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_sign_base_v121_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21d_sign_base_v121_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_sign_base_v122_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63d_sign_base_v122_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_sign_base_v123_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126d_sign_base_v123_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_raw_base_v124_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_raw_base_v124_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_raw_base_v125_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_raw_base_v125_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_raw_base_v126_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_raw_base_v126_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_raw_base_v127_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_raw_base_v127_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v128_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v128_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v129_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v129_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v130_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_zscore_base_v130_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v131_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v131_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v132_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v132_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v133_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_zscore_base_v133_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v134_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v134_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v135_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v135_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v136_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_zscore_base_v136_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v137_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v137_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v138_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v138_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v139_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_zscore_base_v139_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v140_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v140_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v141_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_pctrank_base_v141_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v142_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v142_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v143_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_21dv1_pctrank_base_v143_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v144_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v144_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v145_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_63dv1_pctrank_base_v145_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v146_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v146_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v147_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_126dv1_pctrank_base_v147_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v148_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v148_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v149_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v149_signal},
    "f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v150_signal": {"inputs": ["open_", "high", "low", "close"], "func": f18pgk_parkinson_garman_klass_estimators_pgk_parkinson_5dv1_roc_base_v150_signal}
}
F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_076_150 = REGISTRY

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
    print(f"ALL SELF-TESTS PASSED for F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_076_150")
