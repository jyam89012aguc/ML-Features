import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _drm_peak(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w//2)).max()
def _drm_drawdown(closeadj, w):
    peak = _drm_peak(closeadj, w)
    return (closeadj / peak.replace(0, np.nan)) - 1.0
def _drm_recovery(closeadj, w):
    trough = closeadj.rolling(w, min_periods=max(1, w//2)).min()
    return (closeadj / trough.replace(0, np.nan)) - 1.0

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _drm_drawdown window 21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_raw_base_v076_signal(closeadj):
    result = _drm_drawdown(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_raw_base_v077_signal(closeadj):
    result = _drm_drawdown(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 126d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_raw_base_v078_signal(closeadj):
    result = _drm_drawdown(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_raw_base_v079_signal(closeadj):
    result = _drm_drawdown(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 504d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_raw_base_v080_signal(closeadj):
    result = _drm_drawdown(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=21 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v081_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=21 lb=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v082_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=21 lb=252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v083_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=63 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v084_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=63 lb=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v085_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=63 lb=252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v086_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=126 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v087_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=126 lb=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v088_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=126 lb=252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v089_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=252 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v090_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=252 lb=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v091_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=252 lb=252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v092_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=504 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v093_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=504 lb=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v094_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=504 lb=252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v095_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=21 over 63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_pctrank_base_v096_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=21 over 252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_pctrank_base_v097_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=63 over 63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_pctrank_base_v098_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=63 over 252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_pctrank_base_v099_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=126 over 63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_pctrank_base_v100_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=126 over 252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_pctrank_base_v101_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=252 over 63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_pctrank_base_v102_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=252 over 252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_pctrank_base_v103_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=504 over 63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_pctrank_base_v104_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _drm_drawdown w=504 over 252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_pctrank_base_v105_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=21 roc=5d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v106_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=21 roc=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v107_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=21 roc=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v108_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=63 roc=5d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v109_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=63 roc=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v110_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=63 roc=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v111_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=126 roc=5d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v112_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=126 roc=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v113_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=126 roc=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v114_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=252 roc=5d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v115_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=252 roc=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v116_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=252 roc=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v117_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=504 roc=5d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v118_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=504 roc=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v119_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _drm_drawdown w=504 roc=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v120_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _drm_drawdown w=21
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_maxratio_base_v121_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _drm_drawdown w=21
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_maxratio_base_v122_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _drm_drawdown w=63
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_maxratio_base_v123_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _drm_drawdown w=63
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_maxratio_base_v124_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _drm_drawdown w=126
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_maxratio_base_v125_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _drm_drawdown w=126
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_maxratio_base_v126_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _drm_drawdown w=252
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_maxratio_base_v127_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _drm_drawdown w=252
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_maxratio_base_v128_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _drm_drawdown w=504
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_maxratio_base_v129_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _drm_drawdown w=504
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_maxratio_base_v130_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _drm_drawdown w=21
def f30drm_drawdown_recovery_metrics_drm_drawdown_21d_sign_base_v131_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _drm_drawdown w=63
def f30drm_drawdown_recovery_metrics_drm_drawdown_63d_sign_base_v132_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _drm_drawdown w=126
def f30drm_drawdown_recovery_metrics_drm_drawdown_126d_sign_base_v133_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _drm_drawdown w=252
def f30drm_drawdown_recovery_metrics_drm_drawdown_252d_sign_base_v134_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _drm_drawdown w=504
def f30drm_drawdown_recovery_metrics_drm_drawdown_504d_sign_base_v135_signal(closeadj):
    b = _drm_drawdown(closeadj, 504)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_raw_base_v136_signal(closeadj):
    result = _drm_drawdown(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_raw_base_v137_signal(closeadj):
    result = _drm_drawdown(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 126d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_raw_base_v138_signal(closeadj):
    result = _drm_drawdown(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252dv1_raw_base_v139_signal(closeadj):
    result = _drm_drawdown(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _drm_drawdown window 504d
def f30drm_drawdown_recovery_metrics_drm_drawdown_504dv1_raw_base_v140_signal(closeadj):
    result = _drm_drawdown(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=21 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v141_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=21 lb=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v142_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=21 lb=252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v143_signal(closeadj):
    b = _drm_drawdown(closeadj, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=63 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v144_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=63 lb=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v145_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=63 lb=252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v146_signal(closeadj):
    b = _drm_drawdown(closeadj, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=126 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v147_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=126 lb=63d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v148_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=126 lb=252d
def f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v149_signal(closeadj):
    b = _drm_drawdown(closeadj, 126)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _drm_drawdown w=252 lb=21d
def f30drm_drawdown_recovery_metrics_drm_drawdown_252dv1_zscore_base_v150_signal(closeadj):
    b = _drm_drawdown(closeadj, 252)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_raw_base_v076_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_raw_base_v076_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_raw_base_v077_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_raw_base_v077_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_raw_base_v078_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_raw_base_v078_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_raw_base_v079_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_raw_base_v079_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_raw_base_v080_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_raw_base_v080_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v081_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v081_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v082_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v082_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v083_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_zscore_base_v083_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v084_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v084_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v085_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v085_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v086_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_zscore_base_v086_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v087_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v087_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v088_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v088_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v089_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_zscore_base_v089_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v090_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v090_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v091_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v091_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v092_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_zscore_base_v092_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v093_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v093_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v094_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v094_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v095_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_zscore_base_v095_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_pctrank_base_v096_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_pctrank_base_v096_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_pctrank_base_v097_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_pctrank_base_v097_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_pctrank_base_v098_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_pctrank_base_v098_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_pctrank_base_v099_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_pctrank_base_v099_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_pctrank_base_v100_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_pctrank_base_v100_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_pctrank_base_v101_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_pctrank_base_v101_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_pctrank_base_v102_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_pctrank_base_v102_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_pctrank_base_v103_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_pctrank_base_v103_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_pctrank_base_v104_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_pctrank_base_v104_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_pctrank_base_v105_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_pctrank_base_v105_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v106_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v106_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v107_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v107_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v108_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_roc_base_v108_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v109_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v109_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v110_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v110_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v111_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_roc_base_v111_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v112_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v112_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v113_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v113_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v114_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_roc_base_v114_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v115_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v115_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v116_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v116_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v117_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_roc_base_v117_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v118_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v118_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v119_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v119_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v120_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_roc_base_v120_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_maxratio_base_v121_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_maxratio_base_v121_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_maxratio_base_v122_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_maxratio_base_v122_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_maxratio_base_v123_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_maxratio_base_v123_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_maxratio_base_v124_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_maxratio_base_v124_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_maxratio_base_v125_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_maxratio_base_v125_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_maxratio_base_v126_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_maxratio_base_v126_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_maxratio_base_v127_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_maxratio_base_v127_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_maxratio_base_v128_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_maxratio_base_v128_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_maxratio_base_v129_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_maxratio_base_v129_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_maxratio_base_v130_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_maxratio_base_v130_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21d_sign_base_v131_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21d_sign_base_v131_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63d_sign_base_v132_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63d_sign_base_v132_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126d_sign_base_v133_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126d_sign_base_v133_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252d_sign_base_v134_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252d_sign_base_v134_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504d_sign_base_v135_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504d_sign_base_v135_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_raw_base_v136_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_raw_base_v136_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_raw_base_v137_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_raw_base_v137_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_raw_base_v138_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_raw_base_v138_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252dv1_raw_base_v139_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252dv1_raw_base_v139_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_504dv1_raw_base_v140_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_504dv1_raw_base_v140_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v141_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v141_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v142_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v142_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v143_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_21dv1_zscore_base_v143_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v144_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v144_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v145_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v145_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v146_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_63dv1_zscore_base_v146_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v147_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v147_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v148_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v148_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v149_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_126dv1_zscore_base_v149_signal},
    "f30drm_drawdown_recovery_metrics_drm_drawdown_252dv1_zscore_base_v150_signal": {"inputs": ["closeadj"], "func": f30drm_drawdown_recovery_metrics_drm_drawdown_252dv1_zscore_base_v150_signal}
}
F30_DRAWDOWN_RECOVERY_METRICS_REGISTRY_076_150 = REGISTRY

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
        assert "_drm_peak" in src or "_drm_drawdown" in src or "_drm_recovery" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F30_DRAWDOWN_RECOVERY_METRICS_REGISTRY_076_150")
