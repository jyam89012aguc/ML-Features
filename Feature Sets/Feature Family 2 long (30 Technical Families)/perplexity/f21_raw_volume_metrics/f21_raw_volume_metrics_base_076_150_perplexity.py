import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _rvm_vol_sma(volume, w):
    return volume.rolling(w, min_periods=max(1, w//2)).mean()
def _rvm_vol_ratio(volume, w):
    return volume / _rvm_vol_sma(volume, w).replace(0, np.nan)
def _rvm_vol_zscore(volume, w):
    mu = _rvm_vol_sma(volume, w)
    sd = volume.rolling(w, min_periods=max(1, w//2)).std()
    return (volume - mu) / sd.replace(0, np.nan)

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _rvm_vol_ratio window 5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_raw_base_v076_signal(volume):
    result = _rvm_vol_ratio(volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_raw_base_v077_signal(volume):
    result = _rvm_vol_ratio(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_raw_base_v078_signal(volume):
    result = _rvm_vol_ratio(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 126d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_raw_base_v079_signal(volume):
    result = _rvm_vol_ratio(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_raw_base_v080_signal(volume):
    result = _rvm_vol_ratio(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v081_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v082_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v083_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v084_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v085_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v086_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v087_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v088_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v089_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=126 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v090_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=126 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v091_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=126 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v092_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=252 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v093_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=252 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v094_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=252 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v095_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=5 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v096_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=5 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v097_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=21 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v098_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=21 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v099_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=63 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v100_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=63 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v101_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=126 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v102_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=126 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v103_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=252 over 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v104_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _rvm_vol_ratio w=252 over 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v105_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=5 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v106_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=5 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v107_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=5 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v108_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=21 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v109_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=21 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v110_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=21 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v111_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=63 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v112_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=63 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v113_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=63 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v114_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=126 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v115_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=126 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v116_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=126 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v117_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=252 roc=5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v118_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=252 roc=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v119_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _rvm_vol_ratio w=252 roc=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v120_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = b.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=5
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v121_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=5
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v122_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=21
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v123_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=21
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v124_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=63
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v125_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=63
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v126_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=126
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v127_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=126
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v128_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _rvm_vol_ratio w=252
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v129_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _rvm_vol_ratio w=252
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v130_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=5
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_sign_base_v131_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=21
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_sign_base_v132_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=63
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_sign_base_v133_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=126
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_sign_base_v134_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _rvm_vol_ratio w=252
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_sign_base_v135_signal(volume):
    b = _rvm_vol_ratio(volume, 252)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 5d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_raw_base_v136_signal(volume):
    result = _rvm_vol_ratio(volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_raw_base_v137_signal(volume):
    result = _rvm_vol_ratio(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_raw_base_v138_signal(volume):
    result = _rvm_vol_ratio(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 126d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_raw_base_v139_signal(volume):
    result = _rvm_vol_ratio(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _rvm_vol_ratio window 252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_252dv1_raw_base_v140_signal(volume):
    result = _rvm_vol_ratio(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v141_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v142_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=5 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v143_signal(volume):
    b = _rvm_vol_ratio(volume, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v144_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v145_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=21 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v146_signal(volume):
    b = _rvm_vol_ratio(volume, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v147_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=63d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v148_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=63 lb=252d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v149_signal(volume):
    b = _rvm_vol_ratio(volume, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _rvm_vol_ratio w=126 lb=21d
def f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_zscore_base_v150_signal(volume):
    b = _rvm_vol_ratio(volume, 126)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_raw_base_v076_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_raw_base_v076_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_raw_base_v077_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_raw_base_v077_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_raw_base_v078_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_raw_base_v078_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_raw_base_v079_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_raw_base_v079_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_raw_base_v080_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_raw_base_v080_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v081_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v081_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v082_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v082_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v083_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_zscore_base_v083_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v084_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v084_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v085_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v085_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v086_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_zscore_base_v086_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v087_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v087_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v088_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v088_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v089_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_zscore_base_v089_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v090_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v090_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v091_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v091_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v092_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_zscore_base_v092_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v093_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v093_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v094_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v094_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v095_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_zscore_base_v095_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v096_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v096_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v097_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_pctrank_base_v097_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v098_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v098_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v099_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_pctrank_base_v099_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v100_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v100_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v101_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_pctrank_base_v101_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v102_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v102_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v103_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_pctrank_base_v103_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v104_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v104_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v105_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_pctrank_base_v105_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v106_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v106_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v107_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v107_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v108_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_roc_base_v108_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v109_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v109_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v110_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v110_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v111_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_roc_base_v111_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v112_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v112_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v113_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v113_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v114_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_roc_base_v114_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v115_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v115_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v116_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v116_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v117_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_roc_base_v117_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v118_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v118_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v119_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v119_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v120_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_roc_base_v120_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v121_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v121_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v122_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_maxratio_base_v122_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v123_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v123_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v124_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_maxratio_base_v124_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v125_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v125_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v126_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_maxratio_base_v126_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v127_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v127_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v128_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_maxratio_base_v128_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v129_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v129_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v130_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_maxratio_base_v130_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_sign_base_v131_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5d_sign_base_v131_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_sign_base_v132_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21d_sign_base_v132_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_sign_base_v133_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63d_sign_base_v133_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_sign_base_v134_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126d_sign_base_v134_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_sign_base_v135_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252d_sign_base_v135_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_raw_base_v136_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_raw_base_v136_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_raw_base_v137_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_raw_base_v137_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_raw_base_v138_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_raw_base_v138_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_raw_base_v139_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_raw_base_v139_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_252dv1_raw_base_v140_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_252dv1_raw_base_v140_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v141_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v141_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v142_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v142_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v143_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_5dv1_zscore_base_v143_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v144_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v144_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v145_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v145_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v146_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_21dv1_zscore_base_v146_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v147_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v147_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v148_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v148_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v149_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_63dv1_zscore_base_v149_signal},
    "f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_zscore_base_v150_signal": {"inputs": ["volume"], "func": f21rvm_raw_volume_metrics_rvm_vol_ratio_126dv1_zscore_base_v150_signal}
}
F21_RAW_VOLUME_METRICS_REGISTRY_076_150 = REGISTRY

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
        assert "_rvm_vol_sma" in src or "_rvm_vol_ratio" in src or "_rvm_vol_zscore" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F21_RAW_VOLUME_METRICS_REGISTRY_076_150")
