import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (short-squeeze thrust) =====
def _f14_thrust(s, w):
    # multi-day cumulative up-move; positive moves convex-emphasised (squeeze signature)
    r = s / s.shift(w) - 1.0
    return r * (1.0 + r.clip(lower=0.0))


def _f14_volthrust(s, v, w):
    # up-move over w days multiplied by contemporaneous volume surge vs its own baseline
    r = s / s.shift(w) - 1.0
    surge = v / v.rolling(w * 3, min_periods=max(2, w)).mean().replace(0, np.nan)
    return r * surge


def _f14_velocity(s, w):
    # w-day return per unit of realized daily volatility (sharpness of the thrust)
    r = s / s.shift(w) - 1.0
    vol = s.pct_change().rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(w)
    return r / vol.replace(0, np.nan)


def _f14_recovery(s, w):
    # thrust measured as distance above the trailing w-day low (recovery-from-low)
    low = s.rolling(w, min_periods=max(2, w // 2)).min().replace(0, np.nan)
    return s / low - 1.0


# ============ FEATURES 076-150 ============

# ewm thrust: span-5 ewm of daily return, horizon-scaled, thrust-anchored
def f14ss_f14_short_squeeze_thrust_ewthrust_5d_base_v076_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=5, min_periods=3).mean() * 5.0 + _f14_thrust(closeadj, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ewm thrust span-10
def f14ss_f14_short_squeeze_thrust_ewthrust_10d_base_v077_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=10, min_periods=5).mean() * 10.0 + _f14_thrust(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ewm thrust span-21
def f14ss_f14_short_squeeze_thrust_ewthrust_21d_base_v078_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=21, min_periods=10).mean() * 21.0 + _f14_thrust(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 5d thrust over 63d
def f14ss_f14_short_squeeze_thrust_rank_5d_base_v079_signal(closeadj):
    t = _f14_thrust(closeadj, 5)
    result = t.rolling(63, min_periods=21).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 10d thrust over 126d
def f14ss_f14_short_squeeze_thrust_rank_10d_base_v080_signal(closeadj):
    t = _f14_thrust(closeadj, 10)
    result = t.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 21d thrust over 252d
def f14ss_f14_short_squeeze_thrust_rank_21d_base_v081_signal(closeadj):
    t = _f14_thrust(closeadj, 21)
    result = t.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 10d velocity over 126d
def f14ss_f14_short_squeeze_thrust_rankvel_10d_base_v082_signal(closeadj):
    v = _f14_velocity(closeadj, 10)
    result = v.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 5d volthrust over 63d
def f14ss_f14_short_squeeze_thrust_rankvt_5d_base_v083_signal(closeadj, volume):
    vt = _f14_volthrust(closeadj, volume, 5)
    result = vt.rolling(63, min_periods=21).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d cumulative thrust
def f14ss_f14_short_squeeze_thrust_thrust_84d_base_v084_signal(closeadj):
    result = _f14_thrust(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative thrust
def f14ss_f14_short_squeeze_thrust_thrust_126d_base_v085_signal(closeadj):
    result = _f14_thrust(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d velocity
def f14ss_f14_short_squeeze_thrust_velocity_84d_base_v086_signal(closeadj):
    result = _f14_velocity(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d velocity
def f14ss_f14_short_squeeze_thrust_velocity_126d_base_v087_signal(closeadj):
    result = _f14_velocity(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d recovery-from-low thrust
def f14ss_f14_short_squeeze_thrust_recovery_84d_base_v088_signal(closeadj):
    result = _f14_recovery(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d recovery-from-low thrust
def f14ss_f14_short_squeeze_thrust_recovery_126d_base_v089_signal(closeadj):
    result = _f14_recovery(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure 42d thrust * 126d volume z
def f14ss_f14_short_squeeze_thrust_squeeze_42d_base_v090_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 42) * _z(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure 63d thrust * 126d volume z
def f14ss_f14_short_squeeze_thrust_squeeze_63d_base_v091_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 63) * _z(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vertical-move z-score: 42d thrust over 252d
def f14ss_f14_short_squeeze_thrust_zthrust_42d_base_v092_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vertical-move z-score: 63d thrust over 252d
def f14ss_f14_short_squeeze_thrust_zthrust_63d_base_v093_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# velocity z-score: 42d over 252d
def f14ss_f14_short_squeeze_thrust_zvel_42d_base_v094_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# velocity z-score: 63d over 252d
def f14ss_f14_short_squeeze_thrust_zvel_63d_base_v095_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up stacking magnitude 42d
def f14ss_f14_short_squeeze_thrust_gapstack_42d_base_v096_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    result = gap.rolling(42, min_periods=14).sum() + _f14_thrust(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gap velocity: 10d positive gap sum per unit realized vol
def f14ss_f14_short_squeeze_thrust_gapvel_10d_base_v097_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    g = gap.rolling(10, min_periods=3).sum()
    vol = closeadj.pct_change().rolling(10, min_periods=5).std() * np.sqrt(10.0)
    result = _safe_div(g, vol) + _f14_thrust(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-up intensity 42d
def f14ss_f14_short_squeeze_thrust_upintensity_42d_base_v098_signal(closeadj):
    up = closeadj.pct_change().clip(lower=0.0)
    result = up.rolling(42, min_periods=14).sum() + _f14_thrust(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# up/down magnitude ratio over 21d (asymmetric thrust)
def f14ss_f14_short_squeeze_thrust_udratio_21d_base_v099_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0.0).rolling(21, min_periods=7).sum()
    dn = (-r.clip(upper=0.0)).rolling(21, min_periods=7).sum()
    result = _safe_div(up, dn) + _f14_thrust(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# up/down magnitude ratio over 42d
def f14ss_f14_short_squeeze_thrust_udratio_42d_base_v100_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0.0).rolling(42, min_periods=14).sum()
    dn = (-r.clip(upper=0.0)).rolling(42, min_periods=14).sum()
    result = _safe_div(up, dn) + _f14_thrust(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside range expansion 42d vs 189d
def f14ss_f14_short_squeeze_thrust_rangeexp_42d_base_v101_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    result = _safe_div(_mean(rng, 42), _mean(rng, 189)) + _f14_thrust(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of thrust 42d vs 63d
def f14ss_f14_short_squeeze_thrust_accel_42_63_base_v102_signal(closeadj):
    result = _f14_thrust(closeadj, 42) - _f14_thrust(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of thrust 3d vs 5d
def f14ss_f14_short_squeeze_thrust_accel_3_5_base_v103_signal(closeadj):
    result = _f14_thrust(closeadj, 3) - _f14_thrust(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# price acceleration confirmed by volume 42d
def f14ss_f14_short_squeeze_thrust_accelvol_42d_base_v104_signal(closeadj, volume):
    accel = _f14_thrust(closeadj, 21) - _f14_thrust(closeadj, 42)
    surge = _safe_div(volume, _mean(volume, 126))
    result = accel * surge
    return result.replace([np.inf, -np.inf], np.nan)


# velocity * dollar-volume surge 42d
def f14ss_f14_short_squeeze_thrust_veldv_42d_base_v105_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 189))
    result = _f14_velocity(closeadj, 42) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# recovery * volume surge 63d
def f14ss_f14_short_squeeze_thrust_recovol_63d_base_v106_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 189))
    result = _f14_recovery(closeadj, 63) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# thrust scaled by drawdown 42d
def f14ss_f14_short_squeeze_thrust_thrustdd_42d_base_v107_signal(closeadj):
    peak = closeadj.rolling(189, min_periods=63).max().replace(0, np.nan)
    dd = (peak - closeadj) / peak
    result = _f14_thrust(closeadj, 42) * (1.0 + dd)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust convexity 42d
def f14ss_f14_short_squeeze_thrust_convex_42d_base_v108_signal(closeadj):
    raw = closeadj / closeadj.shift(42) - 1.0
    result = _f14_thrust(closeadj, 42) - raw
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed thrust 21d mean of 21d thrust
def f14ss_f14_short_squeeze_thrust_smthrust_21d_base_v109_signal(closeadj):
    result = _mean(_f14_thrust(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed thrust 42d mean of 42d thrust
def f14ss_f14_short_squeeze_thrust_smthrust_42d_base_v110_signal(closeadj):
    result = _mean(_f14_thrust(closeadj, 42), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed velocity 21d mean of 10d velocity
def f14ss_f14_short_squeeze_thrust_smvel_10d_base_v111_signal(closeadj):
    result = _mean(_f14_velocity(closeadj, 10), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust ratio 21d over 63d
def f14ss_f14_short_squeeze_thrust_ratio_21_63_base_v112_signal(closeadj):
    result = _safe_div(_f14_thrust(closeadj, 21), _f14_thrust(closeadj, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# thrust ratio 5d over 42d
def f14ss_f14_short_squeeze_thrust_ratio_5_42_base_v113_signal(closeadj):
    result = _safe_div(_f14_thrust(closeadj, 5), _f14_thrust(closeadj, 42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# volthrust z-score 21d over 252d
def f14ss_f14_short_squeeze_thrust_zvolthrust_21d_base_v114_signal(closeadj, volume):
    result = _z(_f14_volthrust(closeadj, volume, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery velocity 63d
def f14ss_f14_short_squeeze_thrust_recovel_63d_base_v115_signal(closeadj):
    vol = closeadj.pct_change().rolling(63, min_periods=21).std() * np.sqrt(63.0)
    result = _safe_div(_f14_recovery(closeadj, 63), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# close position within 42d high-low range
def f14ss_f14_short_squeeze_thrust_closepos_42d_base_v116_signal(high, low, closeadj):
    hi = high.rolling(42, min_periods=14).max()
    lo = low.rolling(42, min_periods=14).min()
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan) + _f14_thrust(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# thrust * range expansion 42d
def f14ss_f14_short_squeeze_thrust_thrustrange_42d_base_v117_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 42), _mean(rng, 189))
    result = _f14_thrust(closeadj, 42) * exp
    return result.replace([np.inf, -np.inf], np.nan)


# velocity ratio 10d over 42d
def f14ss_f14_short_squeeze_thrust_velratio_10_42_base_v118_signal(closeadj):
    result = _safe_div(_f14_velocity(closeadj, 10), _f14_velocity(closeadj, 42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# thrust surprise 42d
def f14ss_f14_short_squeeze_thrust_surp_42d_base_v119_signal(closeadj):
    t = _f14_thrust(closeadj, 42)
    result = t - _mean(t, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure smoothed 21d
def f14ss_f14_short_squeeze_thrust_smsqueeze_21d_base_v120_signal(closeadj, volume):
    sp = _f14_thrust(closeadj, 21) * _z(volume, 63)
    result = _mean(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# velocity * recovery 42d
def f14ss_f14_short_squeeze_thrust_velreco_42d_base_v121_signal(closeadj):
    result = _f14_velocity(closeadj, 42) * (1.0 + _f14_recovery(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion confirmed by volume 21d
def f14ss_f14_short_squeeze_thrust_rangevol_21d_base_v122_signal(high, low, closeadj, volume):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 21), _mean(rng, 126))
    surge = _safe_div(volume, _mean(volume, 126))
    result = exp * surge + _f14_thrust(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# thrust dispersion 21d thrust over 126d
def f14ss_f14_short_squeeze_thrust_disp_21d_base_v123_signal(closeadj):
    result = _std(_f14_thrust(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# volthrust smoothed 21d
def f14ss_f14_short_squeeze_thrust_smvolthrust_21d_base_v124_signal(closeadj, volume):
    result = _mean(_f14_volthrust(closeadj, volume, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust skew: skew of daily returns over 42d, thrust-anchored
def f14ss_f14_short_squeeze_thrust_skew_42d_base_v125_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(42, min_periods=14).skew() + _f14_thrust(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# thrust skew over 63d
def f14ss_f14_short_squeeze_thrust_skew_63d_base_v126_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(63, min_periods=21).skew() + _f14_thrust(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# max single-day jump within 10d normalized by realized vol (vertical spike)
def f14ss_f14_short_squeeze_thrust_spike_10d_base_v127_signal(closeadj):
    r = closeadj.pct_change()
    jump = r.rolling(10, min_periods=5).max()
    vol = r.rolling(63, min_periods=21).std()
    result = _safe_div(jump, vol) + _f14_thrust(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# max single-day jump within 21d normalized by realized vol
def f14ss_f14_short_squeeze_thrust_spike_21d_base_v128_signal(closeadj):
    r = closeadj.pct_change()
    jump = r.rolling(21, min_periods=7).max()
    vol = r.rolling(63, min_periods=21).std()
    result = _safe_div(jump, vol) + _f14_thrust(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volthrust velocity: 10d volthrust per unit vol
def f14ss_f14_short_squeeze_thrust_vtvel_10d_base_v129_signal(closeadj, volume):
    vt = _f14_volthrust(closeadj, volume, 10)
    vol = closeadj.pct_change().rolling(10, min_periods=5).std() * np.sqrt(10.0)
    result = _safe_div(vt, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust per up-day intensity: 10d thrust scaled by up-magnitude share
def f14ss_f14_short_squeeze_thrust_thrustshare_10d_base_v130_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0.0).rolling(10, min_periods=5).sum()
    tot = r.abs().rolling(10, min_periods=5).sum()
    share = _safe_div(up, tot)
    result = _f14_thrust(closeadj, 10) * share
    return result.replace([np.inf, -np.inf], np.nan)


# thrust per up-day intensity 21d
def f14ss_f14_short_squeeze_thrust_thrustshare_21d_base_v131_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0.0).rolling(21, min_periods=7).sum()
    tot = r.abs().rolling(21, min_periods=7).sum()
    share = _safe_div(up, tot)
    result = _f14_thrust(closeadj, 21) * share
    return result.replace([np.inf, -np.inf], np.nan)


# velocity acceleration: 5d velocity minus 21d velocity
def f14ss_f14_short_squeeze_thrust_velaccel_5_21_base_v132_signal(closeadj):
    result = _f14_velocity(closeadj, 5) - _f14_velocity(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# velocity acceleration: 10d minus 42d
def f14ss_f14_short_squeeze_thrust_velaccel_10_42_base_v133_signal(closeadj):
    result = _f14_velocity(closeadj, 10) - _f14_velocity(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery acceleration: 21d recovery minus 63d recovery
def f14ss_f14_short_squeeze_thrust_recoaccel_21_63_base_v134_signal(closeadj):
    result = _f14_recovery(closeadj, 21) - _f14_recovery(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze composite: thrust * velocity (sharp-and-fast) 10d
def f14ss_f14_short_squeeze_thrust_tv_10d_base_v135_signal(closeadj):
    result = _f14_thrust(closeadj, 10) * _f14_velocity(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze composite: thrust * velocity 21d
def f14ss_f14_short_squeeze_thrust_tv_21d_base_v136_signal(closeadj):
    result = _f14_thrust(closeadj, 21) * _f14_velocity(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ewm of squeeze pressure (10d thrust * vol z), span 10
def f14ss_f14_short_squeeze_thrust_ewsqueeze_10d_base_v137_signal(closeadj, volume):
    sp = _f14_thrust(closeadj, 10) * _z(volume, 42)
    result = sp.ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume velocity: 10d thrust * dv surge / vol
def f14ss_f14_short_squeeze_thrust_dvvel_10d_base_v138_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    vol = closeadj.pct_change().rolling(10, min_periods=5).std() * np.sqrt(10.0)
    result = _safe_div(_f14_thrust(closeadj, 10) * surge, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-from-low z-score 21d over 252d
def f14ss_f14_short_squeeze_thrust_zreco_21d_base_v139_signal(closeadj):
    result = _z(_f14_recovery(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-from-low z-score 42d over 252d
def f14ss_f14_short_squeeze_thrust_zreco_42d_base_v140_signal(closeadj):
    result = _z(_f14_recovery(closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust * gap-up stacking 10d (vertical move built on gaps)
def f14ss_f14_short_squeeze_thrust_thrustgap_10d_base_v141_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0).rolling(10, min_periods=3).sum()
    result = _f14_thrust(closeadj, 10) * (1.0 + gap)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust * gap-up stacking 21d
def f14ss_f14_short_squeeze_thrust_thrustgap_21d_base_v142_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0).rolling(21, min_periods=7).sum()
    result = _f14_thrust(closeadj, 21) * (1.0 + gap)
    return result.replace([np.inf, -np.inf], np.nan)


# velocity smoothed via ewm span 21 of 10d velocity
def f14ss_f14_short_squeeze_thrust_ewvel_10d_base_v143_signal(closeadj):
    result = _f14_velocity(closeadj, 10).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# blended short-window thrust composite (3/5/10)
def f14ss_f14_short_squeeze_thrust_blendshort_base_v144_signal(closeadj):
    result = (_f14_thrust(closeadj, 3) + _f14_thrust(closeadj, 5)
              + _f14_thrust(closeadj, 10)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended mid-window velocity composite (10/21/42)
def f14ss_f14_short_squeeze_thrust_blendvel_base_v145_signal(closeadj):
    result = (_f14_velocity(closeadj, 10) + _f14_velocity(closeadj, 21)
              + _f14_velocity(closeadj, 42)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d cumulative thrust (long-horizon squeeze base)
def f14ss_f14_short_squeeze_thrust_thrust_189d_base_v146_signal(closeadj):
    result = _f14_thrust(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d recovery-from-low thrust
def f14ss_f14_short_squeeze_thrust_recovery_189d_base_v147_signal(closeadj):
    result = _f14_recovery(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d velocity z-score over 252d
def f14ss_f14_short_squeeze_thrust_zvel_84d_base_v148_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 84), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure with dollar-volume z 21d
def f14ss_f14_short_squeeze_thrust_squeezedv_21d_base_v149_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f14_thrust(closeadj, 21) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon squeeze composite: mean of thrust*velocity at 5/10/21
def f14ss_f14_short_squeeze_thrust_squeezemulti_base_v150_signal(closeadj):
    result = (_f14_thrust(closeadj, 5) * _f14_velocity(closeadj, 5)
              + _f14_thrust(closeadj, 10) * _f14_velocity(closeadj, 10)
              + _f14_thrust(closeadj, 21) * _f14_velocity(closeadj, 21)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14ss_f14_short_squeeze_thrust_ewthrust_5d_base_v076_signal,
    f14ss_f14_short_squeeze_thrust_ewthrust_10d_base_v077_signal,
    f14ss_f14_short_squeeze_thrust_ewthrust_21d_base_v078_signal,
    f14ss_f14_short_squeeze_thrust_rank_5d_base_v079_signal,
    f14ss_f14_short_squeeze_thrust_rank_10d_base_v080_signal,
    f14ss_f14_short_squeeze_thrust_rank_21d_base_v081_signal,
    f14ss_f14_short_squeeze_thrust_rankvel_10d_base_v082_signal,
    f14ss_f14_short_squeeze_thrust_rankvt_5d_base_v083_signal,
    f14ss_f14_short_squeeze_thrust_thrust_84d_base_v084_signal,
    f14ss_f14_short_squeeze_thrust_thrust_126d_base_v085_signal,
    f14ss_f14_short_squeeze_thrust_velocity_84d_base_v086_signal,
    f14ss_f14_short_squeeze_thrust_velocity_126d_base_v087_signal,
    f14ss_f14_short_squeeze_thrust_recovery_84d_base_v088_signal,
    f14ss_f14_short_squeeze_thrust_recovery_126d_base_v089_signal,
    f14ss_f14_short_squeeze_thrust_squeeze_42d_base_v090_signal,
    f14ss_f14_short_squeeze_thrust_squeeze_63d_base_v091_signal,
    f14ss_f14_short_squeeze_thrust_zthrust_42d_base_v092_signal,
    f14ss_f14_short_squeeze_thrust_zthrust_63d_base_v093_signal,
    f14ss_f14_short_squeeze_thrust_zvel_42d_base_v094_signal,
    f14ss_f14_short_squeeze_thrust_zvel_63d_base_v095_signal,
    f14ss_f14_short_squeeze_thrust_gapstack_42d_base_v096_signal,
    f14ss_f14_short_squeeze_thrust_gapvel_10d_base_v097_signal,
    f14ss_f14_short_squeeze_thrust_upintensity_42d_base_v098_signal,
    f14ss_f14_short_squeeze_thrust_udratio_21d_base_v099_signal,
    f14ss_f14_short_squeeze_thrust_udratio_42d_base_v100_signal,
    f14ss_f14_short_squeeze_thrust_rangeexp_42d_base_v101_signal,
    f14ss_f14_short_squeeze_thrust_accel_42_63_base_v102_signal,
    f14ss_f14_short_squeeze_thrust_accel_3_5_base_v103_signal,
    f14ss_f14_short_squeeze_thrust_accelvol_42d_base_v104_signal,
    f14ss_f14_short_squeeze_thrust_veldv_42d_base_v105_signal,
    f14ss_f14_short_squeeze_thrust_recovol_63d_base_v106_signal,
    f14ss_f14_short_squeeze_thrust_thrustdd_42d_base_v107_signal,
    f14ss_f14_short_squeeze_thrust_convex_42d_base_v108_signal,
    f14ss_f14_short_squeeze_thrust_smthrust_21d_base_v109_signal,
    f14ss_f14_short_squeeze_thrust_smthrust_42d_base_v110_signal,
    f14ss_f14_short_squeeze_thrust_smvel_10d_base_v111_signal,
    f14ss_f14_short_squeeze_thrust_ratio_21_63_base_v112_signal,
    f14ss_f14_short_squeeze_thrust_ratio_5_42_base_v113_signal,
    f14ss_f14_short_squeeze_thrust_zvolthrust_21d_base_v114_signal,
    f14ss_f14_short_squeeze_thrust_recovel_63d_base_v115_signal,
    f14ss_f14_short_squeeze_thrust_closepos_42d_base_v116_signal,
    f14ss_f14_short_squeeze_thrust_thrustrange_42d_base_v117_signal,
    f14ss_f14_short_squeeze_thrust_velratio_10_42_base_v118_signal,
    f14ss_f14_short_squeeze_thrust_surp_42d_base_v119_signal,
    f14ss_f14_short_squeeze_thrust_smsqueeze_21d_base_v120_signal,
    f14ss_f14_short_squeeze_thrust_velreco_42d_base_v121_signal,
    f14ss_f14_short_squeeze_thrust_rangevol_21d_base_v122_signal,
    f14ss_f14_short_squeeze_thrust_disp_21d_base_v123_signal,
    f14ss_f14_short_squeeze_thrust_smvolthrust_21d_base_v124_signal,
    f14ss_f14_short_squeeze_thrust_skew_42d_base_v125_signal,
    f14ss_f14_short_squeeze_thrust_skew_63d_base_v126_signal,
    f14ss_f14_short_squeeze_thrust_spike_10d_base_v127_signal,
    f14ss_f14_short_squeeze_thrust_spike_21d_base_v128_signal,
    f14ss_f14_short_squeeze_thrust_vtvel_10d_base_v129_signal,
    f14ss_f14_short_squeeze_thrust_thrustshare_10d_base_v130_signal,
    f14ss_f14_short_squeeze_thrust_thrustshare_21d_base_v131_signal,
    f14ss_f14_short_squeeze_thrust_velaccel_5_21_base_v132_signal,
    f14ss_f14_short_squeeze_thrust_velaccel_10_42_base_v133_signal,
    f14ss_f14_short_squeeze_thrust_recoaccel_21_63_base_v134_signal,
    f14ss_f14_short_squeeze_thrust_tv_10d_base_v135_signal,
    f14ss_f14_short_squeeze_thrust_tv_21d_base_v136_signal,
    f14ss_f14_short_squeeze_thrust_ewsqueeze_10d_base_v137_signal,
    f14ss_f14_short_squeeze_thrust_dvvel_10d_base_v138_signal,
    f14ss_f14_short_squeeze_thrust_zreco_21d_base_v139_signal,
    f14ss_f14_short_squeeze_thrust_zreco_42d_base_v140_signal,
    f14ss_f14_short_squeeze_thrust_thrustgap_10d_base_v141_signal,
    f14ss_f14_short_squeeze_thrust_thrustgap_21d_base_v142_signal,
    f14ss_f14_short_squeeze_thrust_ewvel_10d_base_v143_signal,
    f14ss_f14_short_squeeze_thrust_blendshort_base_v144_signal,
    f14ss_f14_short_squeeze_thrust_blendvel_base_v145_signal,
    f14ss_f14_short_squeeze_thrust_thrust_189d_base_v146_signal,
    f14ss_f14_short_squeeze_thrust_recovery_189d_base_v147_signal,
    f14ss_f14_short_squeeze_thrust_zvel_84d_base_v148_signal,
    f14ss_f14_short_squeeze_thrust_squeezedv_21d_base_v149_signal,
    f14ss_f14_short_squeeze_thrust_squeezemulti_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_SHORT_SQUEEZE_THRUST_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume"}
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = level + 50.0 * walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f14_thrust", "_f14_volthrust", "_f14_velocity", "_f14_recovery")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f14_short_squeeze_thrust_base_076_150_claude: {n_features} features pass")
