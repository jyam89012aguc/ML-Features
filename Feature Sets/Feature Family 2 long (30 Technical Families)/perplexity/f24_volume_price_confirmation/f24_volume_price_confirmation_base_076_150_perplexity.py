import numpy as np
import pandas as pd

# ── domain primitives ─────────────────────────────────────
def _vpc_price_roc(closeadj, w):
    return closeadj.pct_change(w)
def _vpc_vol_roc(volume, w):
    return volume.pct_change(w)
def _vpc_confirmation(closeadj, volume, w):
    return _vpc_price_roc(closeadj, w) * np.sign(_vpc_vol_roc(volume, w))

# ── helpers ──────────────────────────────────────────────
def _z(s, w):
    mu = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - mu) / sd.replace(0, np.nan)

# raw _vpc_price_roc window 5d
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_raw_base_v076_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _vpc_price_roc window 21d
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_raw_base_v077_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _vpc_price_roc window 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_raw_base_v078_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v079_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=63d
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v080_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=252d
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v081_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v082_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=63d
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v083_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=252d
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v084_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=63 lb=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v085_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=63 lb=63d
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v086_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=63 lb=252d
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v087_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=5 over 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_pctrank_base_v088_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=5 over 252d
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_pctrank_base_v089_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=21 over 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_pctrank_base_v090_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=21 over 252d
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_pctrank_base_v091_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=63 over 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_pctrank_base_v092_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=63 over 252d
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_pctrank_base_v093_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=5 roc=5d
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_roc_base_v094_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=5 roc=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_roc_base_v095_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=21 roc=5d
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_roc_base_v096_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=21 roc=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_roc_base_v097_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=63 roc=5d
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_roc_base_v098_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=63 roc=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_roc_base_v099_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _vpc_price_roc w=5
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_maxratio_base_v100_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _vpc_price_roc w=5
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_maxratio_base_v101_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _vpc_price_roc w=21
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_maxratio_base_v102_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _vpc_price_roc w=21
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_maxratio_base_v103_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _vpc_price_roc w=63
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_maxratio_base_v104_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _vpc_price_roc w=63
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_maxratio_base_v105_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _vpc_price_roc w=5
def f24vpc_volume_price_confirmation_vpc_price_roc_5d_sign_base_v106_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _vpc_price_roc w=21
def f24vpc_volume_price_confirmation_vpc_price_roc_21d_sign_base_v107_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _vpc_price_roc w=63
def f24vpc_volume_price_confirmation_vpc_price_roc_63d_sign_base_v108_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _vpc_price_roc window 5d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_raw_base_v109_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _vpc_price_roc window 21d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_raw_base_v110_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _vpc_price_roc window 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_raw_base_v111_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v112_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=63d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v113_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=252d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v114_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v115_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=63d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v116_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=252d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v117_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=63 lb=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v118_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=63 lb=63d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v119_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=63 lb=252d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v120_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=5 over 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_pctrank_base_v121_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=5 over 252d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_pctrank_base_v122_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=21 over 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_pctrank_base_v123_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=21 over 252d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_pctrank_base_v124_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=63 over 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_pctrank_base_v125_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = b.rolling(63, min_periods=max(1, 63//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# pctrank of _vpc_price_roc w=63 over 252d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_pctrank_base_v126_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = b.rolling(252, min_periods=max(1, 252//4)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=5 roc=5d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_roc_base_v127_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=5 roc=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_roc_base_v128_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=21 roc=5d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_roc_base_v129_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=21 roc=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_roc_base_v130_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=63 roc=5d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_roc_base_v131_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = b.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

# rate-of-change of _vpc_price_roc w=63 roc=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_roc_base_v132_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = b.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _vpc_price_roc w=5
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_maxratio_base_v133_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _vpc_price_roc w=5
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_maxratio_base_v134_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _vpc_price_roc w=21
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_maxratio_base_v135_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _vpc_price_roc w=21
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_maxratio_base_v136_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 63d max of _vpc_price_roc w=63
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_maxratio_base_v137_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    mx = b.rolling(63, min_periods=max(1, 63//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# ratio to 252d max of _vpc_price_roc w=63
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_maxratio_base_v138_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    mx = b.rolling(252, min_periods=max(1, 252//4)).max()
    result = (b / mx.replace(0, np.nan)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _vpc_price_roc w=5
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_sign_base_v139_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _vpc_price_roc w=21
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_sign_base_v140_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# sign (direction) of _vpc_price_roc w=63
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_sign_base_v141_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 63)
    result = np.sign(b)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _vpc_price_roc window 5d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_raw_base_v142_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _vpc_price_roc window 21d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_raw_base_v143_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# raw _vpc_price_roc window 63d
def f24vpc_volume_price_confirmation_vpc_price_roc_63dv2_raw_base_v144_signal(closeadj, volume):
    result = _vpc_price_roc(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v145_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=63d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v146_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=5 lb=252d
def f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v147_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 5)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=21d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v148_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=63d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v149_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# z-score of _vpc_price_roc w=21 lb=252d
def f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v150_signal(closeadj, volume):
    b = _vpc_price_roc(closeadj, 21)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_raw_base_v076_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_raw_base_v076_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_raw_base_v077_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_raw_base_v077_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_raw_base_v078_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_raw_base_v078_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v079_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v079_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v080_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v080_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v081_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_zscore_base_v081_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v082_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v082_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v083_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v083_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v084_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_zscore_base_v084_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v085_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v085_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v086_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v086_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v087_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_zscore_base_v087_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_pctrank_base_v088_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_pctrank_base_v088_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_pctrank_base_v089_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_pctrank_base_v089_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_pctrank_base_v090_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_pctrank_base_v090_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_pctrank_base_v091_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_pctrank_base_v091_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_pctrank_base_v092_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_pctrank_base_v092_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_pctrank_base_v093_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_pctrank_base_v093_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_roc_base_v094_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_roc_base_v094_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_roc_base_v095_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_roc_base_v095_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_roc_base_v096_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_roc_base_v096_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_roc_base_v097_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_roc_base_v097_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_roc_base_v098_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_roc_base_v098_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_roc_base_v099_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_roc_base_v099_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_maxratio_base_v100_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_maxratio_base_v100_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_maxratio_base_v101_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_maxratio_base_v101_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_maxratio_base_v102_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_maxratio_base_v102_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_maxratio_base_v103_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_maxratio_base_v103_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_maxratio_base_v104_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_maxratio_base_v104_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_maxratio_base_v105_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_maxratio_base_v105_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5d_sign_base_v106_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5d_sign_base_v106_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21d_sign_base_v107_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21d_sign_base_v107_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63d_sign_base_v108_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63d_sign_base_v108_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_raw_base_v109_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_raw_base_v109_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_raw_base_v110_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_raw_base_v110_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_raw_base_v111_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_raw_base_v111_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v112_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v112_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v113_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v113_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v114_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_zscore_base_v114_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v115_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v115_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v116_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v116_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v117_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_zscore_base_v117_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v118_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v118_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v119_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v119_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v120_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_zscore_base_v120_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_pctrank_base_v121_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_pctrank_base_v121_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_pctrank_base_v122_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_pctrank_base_v122_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_pctrank_base_v123_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_pctrank_base_v123_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_pctrank_base_v124_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_pctrank_base_v124_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_pctrank_base_v125_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_pctrank_base_v125_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_pctrank_base_v126_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_pctrank_base_v126_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_roc_base_v127_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_roc_base_v127_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_roc_base_v128_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_roc_base_v128_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_roc_base_v129_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_roc_base_v129_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_roc_base_v130_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_roc_base_v130_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_roc_base_v131_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_roc_base_v131_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_roc_base_v132_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_roc_base_v132_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_maxratio_base_v133_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_maxratio_base_v133_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_maxratio_base_v134_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_maxratio_base_v134_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_maxratio_base_v135_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_maxratio_base_v135_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_maxratio_base_v136_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_maxratio_base_v136_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_maxratio_base_v137_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_maxratio_base_v137_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_maxratio_base_v138_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_maxratio_base_v138_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_sign_base_v139_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv1_sign_base_v139_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_sign_base_v140_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv1_sign_base_v140_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_sign_base_v141_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv1_sign_base_v141_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_raw_base_v142_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_raw_base_v142_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_raw_base_v143_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_raw_base_v143_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_63dv2_raw_base_v144_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_63dv2_raw_base_v144_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v145_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v145_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v146_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v146_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v147_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_5dv2_zscore_base_v147_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v148_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v148_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v149_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v149_signal},
    "f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v150_signal": {"inputs": ["closeadj", "volume"], "func": f24vpc_volume_price_confirmation_vpc_price_roc_21dv2_zscore_base_v150_signal}
}
F24_VOLUME_PRICE_CONFIRMATION_REGISTRY_076_150 = REGISTRY

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
        assert "_vpc_price_roc" in src or "_vpc_vol_roc" in src or "_vpc_confirmation" in src, f"{name}: missing domain primitive"
        nan_fracs.append(y1.iloc[504:].isna().mean())
    assert sum(1 for r in nan_fracs if r < 0.5) / len(nan_fracs) >= 0.8, "Too many NaN-heavy features"
    print(f"ALL SELF-TESTS PASSED for F24_VOLUME_PRICE_CONFIRMATION_REGISTRY_076_150")
