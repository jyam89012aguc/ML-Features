import inspect
import numpy as np
import pandas as pd

# f02_momentum_rotation (f02mr) — base features 076-150.
# TIGHTENED DOMAIN: RAW PRICE-MOMENTUM / ROC LEVELS ONLY (see file 001-075 header).
# This file adds: VOLUME-CONFIRMED raw momentum (dollar-volume = closeadj*volume, the one
# axis no sibling closeadj-only family touches), further skip-month / horizon ROC levels,
# cross-window dispersion & term-structure facets, acceleration/curvature-as-level (kept
# structurally distinct from f01's plain non-overlapping return acceleration), and
# spike/tail momentum magnitudes. NO efficiency ratio (f03), NO autocorr/variance-ratio/
# Hurst (f03), NO Sharpe/Sortino/vol-normalised risk-adjustment (f08), NO percentile/
# z-score vs own history (f08), NO price-vs-MA / MA-stacking (f01).
# Inputs: closeadj, optional volume.

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f02_roc(close, w):
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _f02_pace(close, w):
    return _f02_roc(close, w) / float(w)


def _f02_skip(close, wl, ws):
    return np.log(close.shift(ws).replace(0, np.nan) / close.shift(wl).replace(0, np.nan))


def _f02_signmag(roc):
    return np.sign(roc) * (roc.abs() ** 0.5)


def _f02_dollar(close, vol):
    # dollar-volume proxy = closeadj * volume
    return close * vol


def _f02_dvlog(close, vol):
    return np.log(_f02_dollar(close, vol).replace(0, np.nan))


# ============================================================
# ----- additional horizon ROC levels / skip variants not in file 1 -----
# ROC 10d (two-week momentum level)
def f02mr_f02_momentum_rotation_roc_10d_base_v076_signal(closeadj):
    b = _f02_roc(closeadj, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 42d (two-month momentum level)
def f02mr_f02_momentum_rotation_roc_42d_base_v077_signal(closeadj):
    b = _f02_roc(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 189d (nine-month momentum level)
def f02mr_f02_momentum_rotation_roc_189d_base_v078_signal(closeadj):
    b = _f02_roc(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-6 momentum: first half of the trailing year (252d ago -> 126d ago) — aged momentum
def f02mr_f02_momentum_rotation_mom126_252d_base_v079_signal(closeadj):
    b = _f02_skip(closeadj, 252, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-month momentum range-position: where the 42d ROC sits in its own 126d hi-lo band
# (level form, not a percentile rank) — distinct from any trend-acceleration measure
def f02mr_f02_momentum_rotation_rocpos_42d_base_v080_signal(closeadj):
    roc = _f02_roc(closeadj, 42)
    hi = roc.rolling(126, min_periods=63).max()
    lo = roc.rolling(126, min_periods=63).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- VOLUME-CONFIRMED raw momentum (dollar-volume = closeadj*volume) -----
# volume-weighted monthly momentum: 21d ROC scaled by tanh of dollar-volume surge vs 63d
def f02mr_f02_momentum_rotation_volmom_21d_base_v081_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    dv = _f02_dollar(closeadj, volume)
    surge = dv.rolling(21, min_periods=10).mean() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = roc * np.tanh(surge - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted quarterly momentum: 63d ROC times tanh of dollar-volume growth (21 vs 63)
def f02mr_f02_momentum_rotation_volmom_63d_base_v082_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 63)
    dv = _f02_dollar(closeadj, volume)
    g = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
               / dv.rolling(63, min_periods=21).mean().replace(0, np.nan))
    b = np.tanh(5.0 * roc) + np.tanh(2.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down dollar-volume momentum over 63d: signed-volume on up-days vs down-days (net flow)
def f02mr_f02_momentum_rotation_udvol_63d_base_v083_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = _f02_dollar(closeadj, volume)
    upv = dv.where(r > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(r < 0, 0.0).rolling(63, min_periods=21).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down dollar-volume momentum over 21d (faster net-flow rotation)
def f02mr_f02_momentum_rotation_udvol_21d_base_v084_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = _f02_dollar(closeadj, volume)
    upv = dv.where(r > 0, 0.0).rolling(21, min_periods=10).sum()
    dnv = dv.where(r < 0, 0.0).rolling(21, min_periods=10).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume-weighted average return over 63d (where the trading actually happened)
def f02mr_f02_momentum_rotation_dvwret_63d_base_v085_signal(closeadj, volume):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    dv = _f02_dollar(closeadj, volume)
    num = (r * dv).rolling(63, min_periods=21).sum()
    den = dv.rolling(63, min_periods=21).sum()
    b = num / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-momentum divergence: sign of 21d ROC vs sign of 21d dollar-volume trend
def f02mr_f02_momentum_rotation_voldiverg_21d_base_v086_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    dv = _f02_dvlog(closeadj, volume)
    dvtrend = dv - dv.shift(21)
    b = np.tanh(5.0 * roc) * np.tanh(2.0 * dvtrend)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-confirmed annual momentum: 252d ROC times tanh of dollar-volume trend over 126d
def f02mr_f02_momentum_rotation_volconf_252d_base_v087_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 252)
    dv = _f02_dvlog(closeadj, volume)
    dvtrend = dv.rolling(63, min_periods=21).mean() - dv.rolling(252, min_periods=126).mean()
    b = roc * np.tanh(dvtrend)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume thrust on the sign of monthly momentum: signed surge in 5d vs 63d turnover
def f02mr_f02_momentum_rotation_dvthrust_base_v088_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    dv = _f02_dollar(closeadj, volume)
    surge = dv.rolling(5, min_periods=3).mean() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = np.sign(roc) * np.tanh(surge - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum per unit of turnover: 21d ROC scaled by inverse log dollar-volume level
# (thin-name move premium — same move on lighter tape scores higher)
def f02mr_f02_momentum_rotation_momperdv_base_v089_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    dv = _f02_dvlog(closeadj, volume)
    dvc = dv - dv.rolling(252, min_periods=126).mean()
    b = roc * np.tanh(-dvc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-tilted breadth: net of dollar-volume on up vs down days over 126d, signed-sqrt
def f02mr_f02_momentum_rotation_udvol_126d_base_v090_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = _f02_dollar(closeadj, volume)
    upv = dv.where(r > 0, 0.0).rolling(126, min_periods=63).sum()
    dnv = dv.where(r < 0, 0.0).rolling(126, min_periods=63).sum()
    ratio = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    b = _f02_signmag(ratio)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- more cross-window dispersion / term-structure facets -----
# dispersion of ROC across the SHORT cluster (5/10/21) — short-horizon disagreement
def f02mr_f02_momentum_rotation_dispshort_base_v091_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (5, 10, 21)], axis=1)
    b = panel.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of ROC across the LONG cluster (126/189/252) — long-horizon disagreement
def f02mr_f02_momentum_rotation_displong_base_v092_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (126, 189, 252)], axis=1)
    b = panel.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pace term-structure curvature at the long end: 126d pace minus mean(63d, 252d) paces
def f02mr_f02_momentum_rotation_termcurv_126_base_v093_signal(closeadj):
    p63 = _f02_pace(closeadj, 63)
    p126 = _f02_pace(closeadj, 126)
    p252 = _f02_pace(closeadj, 252)
    b = (p126 - 0.5 * (p63 + p252)) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pace term-structure curvature at the short end: 10d pace minus mean(5d, 21d) paces
def f02mr_f02_momentum_rotation_termcurv_10_base_v094_signal(closeadj):
    p5 = _f02_pace(closeadj, 5)
    p10 = _f02_pace(closeadj, 10)
    p21 = _f02_pace(closeadj, 21)
    b = (p10 - 0.5 * (p5 + p21)) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pace skew across the long cluster: (max+min)/(max-min) of 63/126/189/252 paces
def f02mr_f02_momentum_rotation_paceskewlong_base_v095_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (63, 126, 189, 252)], axis=1)
    hi = panel.max(axis=1)
    lo = panel.min(axis=1)
    b = (hi + lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-window agreement count among the long horizons (how many of 63/126/189/252 positive)
def f02mr_f02_momentum_rotation_poscountlong_base_v096_signal(closeadj):
    paces = [_f02_pace(closeadj, w) for w in (63, 126, 189, 252)]
    cnt = sum((p > 0).astype(float) for p in paces)
    tilt = pd.concat([np.tanh(120.0 * p) for p in paces], axis=1).mean(axis=1)
    b = (cnt / 4.0 - 0.5) + 0.25 * tilt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range of the long-cluster ROC levels signed by annual direction (long-horizon span)
def f02mr_f02_momentum_rotation_spanlong_base_v097_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (63, 126, 189, 252)], axis=1)
    span = panel.max(axis=1) - panel.min(axis=1)
    b = span * np.sign(_f02_roc(closeadj, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration of |ROC| in the short cluster vs the whole panel (where the size lives)
def f02mr_f02_momentum_rotation_shortdomin_base_v098_signal(closeadj):
    sh = pd.concat([_f02_roc(closeadj, w).abs() for w in (5, 10, 21)], axis=1).sum(axis=1)
    al = pd.concat([_f02_roc(closeadj, w).abs() for w in (5, 10, 21, 63, 126, 252)], axis=1).sum(axis=1)
    b = sh / al.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- acceleration / curvature-as-level (distinct from f01 plain accel) -----
# overlapping acceleration of 42d ROC over 21 days (two-month jolt at off-grid horizon)
def f02mr_f02_momentum_rotation_accel_42d_base_v099_signal(closeadj):
    roc = _f02_roc(closeadj, 42)
    b = roc - roc.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-compressed acceleration of 126d ROC over a quarter (bounded half-year jolt)
def f02mr_f02_momentum_rotation_acceltanh_126d_base_v100_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = np.tanh(4.0 * (roc - roc.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# third difference of log price at 21d steps as a LEVEL (rate-of-change of curvature/jerk)
def f02mr_f02_momentum_rotation_jerk_21d_base_v101_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    b = lp - 3.0 * lp.shift(21) + 3.0 * lp.shift(42) - lp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# third difference of log price at 42d steps as a LEVEL (slower jerk)
def f02mr_f02_momentum_rotation_jerk_42d_base_v102_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    b = lp - 3.0 * lp.shift(42) + 3.0 * lp.shift(84) - lp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the 12-1 skip momentum over a half-year (long clean jolt)
def f02mr_f02_momentum_rotation_mom121accel2_base_v103_signal(closeadj):
    m = _f02_skip(closeadj, 252, 21)
    b = m - m.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt acceleration of 21d ROC over a quarter (compressed slow monthly jolt)
def f02mr_f02_momentum_rotation_accelsm_21d_base_v104_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = _f02_signmag(roc - roc.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration agreement: sign of 21d accel times sign of 126d accel, gated by magnitude
def f02mr_f02_momentum_rotation_accelagree_base_v105_signal(closeadj):
    r21 = _f02_roc(closeadj, 21)
    r126 = _f02_roc(closeadj, 126)
    a21 = r21 - r21.shift(21)
    a126 = r126 - r126.shift(126)
    agree = np.sign(a21) * np.sign(a126)
    mag = pd.concat([a21.abs(), a126.abs()], axis=1).min(axis=1)
    b = agree * np.tanh(20.0 * mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- momentum range-position-as-level, giveback / thrust at more horizons -----
# 21d ROC position within its own 126d hi-lo band, centred (level, not rank)
def f02mr_f02_momentum_rotation_rocpos_21d_base_v106_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    hi = roc.rolling(126, min_periods=63).max()
    lo = roc.rolling(126, min_periods=63).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROC position within its own 252d hi-lo band, centred (level)
def f02mr_f02_momentum_rotation_rocpos_126d_base_v107_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    hi = roc.rolling(252, min_periods=126).max()
    lo = roc.rolling(252, min_periods=126).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROC giveback: ROC minus its trailing 252d max (drop from peak half-year momentum)
def f02mr_f02_momentum_rotation_giveback_126d_base_v108_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = roc - roc.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROC thrust: ROC minus its trailing 252d min (rise from trough half-year momentum)
def f02mr_f02_momentum_rotation_thrust_126d_base_v109_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = roc - roc.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC giveback over a shorter memory: ROC minus trailing 63d max (fast momentum fade)
def f02mr_f02_momentum_rotation_giveback_21d_base_v110_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = roc - roc.rolling(63, min_periods=21).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC mid-band displacement over a 1260d... use 504d band (annual momentum vs its band)
def f02mr_f02_momentum_rotation_rocmid_126d_base_v111_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    hi = roc.rolling(504, min_periods=252).max()
    lo = roc.rolling(504, min_periods=252).min()
    b = roc - 0.5 * (hi + lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- magnitude composites / sign-mag at extra horizons -----
# signed-sqrt magnitude of weekly momentum (5d compressed strength)
def f02mr_f02_momentum_rotation_signmag_5d_base_v112_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt magnitude of two-month momentum (42d compressed strength)
def f02mr_f02_momentum_rotation_signmag_42d_base_v113_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 42))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute momentum magnitude at 21d (monthly move size, direction-blind)
def f02mr_f02_momentum_rotation_absmag_21d_base_v114_signal(closeadj):
    b = _f02_roc(closeadj, 21).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute momentum magnitude at 126d (half-year move size)
def f02mr_f02_momentum_rotation_absmag_126d_base_v115_signal(closeadj):
    b = _f02_roc(closeadj, 126).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-cluster signed-sqrt blend: compressed magnitudes of 63/126/252 summed (long strength)
def f02mr_f02_momentum_rotation_sqrtblendlong_base_v116_signal(closeadj):
    b = (_f02_signmag(_f02_roc(closeadj, 63))
         + _f02_signmag(_f02_roc(closeadj, 126))
         + _f02_signmag(_f02_roc(closeadj, 252)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted long composite: back-loaded blend favouring longer horizons (durable momentum)
def f02mr_f02_momentum_rotation_complong_base_v117_signal(closeadj):
    b = (0.1 * _f02_roc(closeadj, 21) + 0.2 * _f02_roc(closeadj, 63)
         + 0.3 * _f02_roc(closeadj, 126) + 0.4 * _f02_roc(closeadj, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of the mid cluster (21/42/63) ROC levels — mid-horizon disagreement (a spread,
# distinct from any directional long-cluster composite)
def f02mr_f02_momentum_rotation_dispmid_base_v118_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (21, 42, 63)], axis=1)
    b = panel.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- spike / tail momentum magnitudes (hit-driven names) -----
# tail asymmetry over 126d: mean of 5 largest up-days minus mean of 5 largest down-days
def f02mr_f02_momentum_rotation_tailasym_126d_base_v119_signal(closeadj):
    r = closeadj.pct_change()
    up5 = r.rolling(126, min_periods=63).apply(lambda a: np.mean(np.sort(a)[-5:]), raw=True)
    dn5 = r.rolling(126, min_periods=63).apply(lambda a: -np.mean(np.sort(a)[:5]), raw=True)
    b = (up5 - dn5) / (up5 + dn5).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-day momentum over 63d: net log-return contributed by days beyond 2 rolling-std moves
def f02mr_f02_momentum_rotation_spikemom_63d_base_v120_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    sd = r.rolling(63, min_periods=21).std()
    spike = r.where(r.abs() > 2.0 * sd, 0.0)
    b = spike.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest up-move over 21d minus largest down-move (monthly extreme-day asymmetry)
def f02mr_f02_momentum_rotation_extreme_21d_base_v121_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    mx = r.rolling(21, min_periods=10).max()
    mn = r.rolling(21, min_periods=10).min()
    b = mx + mn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# median daily-return drift over 63d (robust central momentum, spike-insensitive)
def f02mr_f02_momentum_rotation_medret_63d_base_v122_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    b = r.rolling(63, min_periods=21).median() * 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean minus median daily return over 63d (skew of the move: outlier-driven vs broad)
def f02mr_f02_momentum_rotation_momskew_63d_base_v123_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    mn = r.rolling(63, min_periods=21).mean()
    md = r.rolling(63, min_periods=21).median()
    b = (mn - md) * 1000.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- more rotation / interaction levels -----
# weekly-vs-monthly directed ratio: 5d ROC share signed by the monthly trend direction
def f02mr_f02_momentum_rotation_wmratio_base_v124_signal(closeadj):
    s = _f02_roc(closeadj, 5)
    m = _f02_roc(closeadj, 21)
    b = np.sign(m) * s / (m.abs() + s.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# front-loading of the year: tanh of 63d ROC over 252d ROC (recent-quarter share of year)
def f02mr_f02_momentum_rotation_frontload_q_base_v125_signal(closeadj):
    s = _f02_roc(closeadj, 63)
    l = _f02_roc(closeadj, 252)
    b = np.tanh(s / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum concentration: |63d ROC| share of (|63d| + |252d|) (mid vs long size mix)
def f02mr_f02_momentum_rotation_conc_63v252_base_v126_signal(closeadj):
    s = _f02_roc(closeadj, 63).abs()
    l = _f02_roc(closeadj, 252).abs()
    b = s / (s + l).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-short pace agreement: sign(252 pace) x sign(63 pace) gated by smaller |pace|
def f02mr_f02_momentum_rotation_lsagree_63v252_base_v127_signal(closeadj):
    l = _f02_pace(closeadj, 252)
    s = _f02_pace(closeadj, 63)
    agree = np.sign(l) * np.sign(s)
    mag = pd.concat([l.abs(), s.abs()], axis=1).min(axis=1)
    b = agree * np.tanh(150.0 * mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full-stack alignment magnitude over the long cluster: product of 63/126/252 pace signs
def f02mr_f02_momentum_rotation_stackmaglong_base_v128_signal(closeadj):
    paces = [_f02_pace(closeadj, w) for w in (63, 126, 252)]
    sgn = np.sign(pd.concat(paces, axis=1)).prod(axis=1)
    mag = pd.concat([p.abs() for p in paces], axis=1).min(axis=1)
    b = sgn * np.tanh(150.0 * mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# balance momentum at the long end: signed 63-vs-252 magnitude share, change over a quarter
def f02mr_f02_momentum_rotation_balancelong_base_v129_signal(closeadj):
    s = _f02_roc(closeadj, 63).abs()
    l = _f02_roc(closeadj, 252).abs()
    bal = (s - l) / (s + l).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pullback at the long horizon: 21d ROC opposing the 252d trend, sized by trend magnitude
def f02mr_f02_momentum_rotation_pullback_long_base_v130_signal(closeadj):
    short = _f02_roc(closeadj, 21)
    long = _f02_roc(closeadj, 252)
    b = -short * np.sign(long) * long.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# skip-month reversal at the quarter: 6-1 momentum minus twice the recent 21d return
def f02mr_f02_momentum_rotation_skiprev6_base_v131_signal(closeadj):
    m = _f02_skip(closeadj, 126, 21)
    recent = _f02_roc(closeadj, 21)
    b = m - 2.0 * recent
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum extension at short horizons: 6-1 momentum minus 3-1 momentum (medium extension)
def f02mr_f02_momentum_rotation_momext_short_base_v132_signal(closeadj):
    b = _f02_skip(closeadj, 126, 21) - _f02_skip(closeadj, 63, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- displacement / smoothing of raw momentum at extra horizons -----
# 21d ROC minus its trailing 63d mean ROC (monthly momentum surprise as a level)
def f02mr_f02_momentum_rotation_rocdisp_21d_base_v133_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = roc - roc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROC minus its trailing 126d mean ROC (half-year momentum surprise as a level)
def f02mr_f02_momentum_rotation_rocdisp_126d_base_v134_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = roc - roc.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 4-1 momentum: four-month return skipping the most recent month (84d -> 21d skip) —
# a clean intermediate skip-window momentum level
def f02mr_f02_momentum_rotation_mom41_84d_base_v135_signal(closeadj):
    b = _f02_skip(closeadj, 84, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change of 63d momentum (quarter momentum now vs a year ago)
def f02mr_f02_momentum_rotation_momyoy_63d_base_v136_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- whole-panel rotation leg locators (level form, not percentile rank) -----
# z-position of the 5d pace within the cross-window pace panel (weekly leg leadership)
def f02mr_f02_momentum_rotation_legpos_5d_base_v137_signal(closeadj):
    paces = {w: _f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)}
    panel = pd.concat([paces[w] for w in (5, 21, 63, 126, 252)], axis=1)
    b = (paces[5] - panel.mean(axis=1)) / panel.std(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-position of the 21d pace within the cross-window pace panel (monthly leg leadership)
def f02mr_f02_momentum_rotation_legpos_21d_base_v138_signal(closeadj):
    paces = {w: _f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)}
    panel = pd.concat([paces[w] for w in (5, 21, 63, 126, 252)], axis=1)
    b = (paces[21] - panel.mean(axis=1)) / panel.std(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-position of the 126d pace within the cross-window pace panel (half-year leg leadership)
def f02mr_f02_momentum_rotation_legpos_126d_base_v139_signal(closeadj):
    paces = {w: _f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)}
    panel = pd.concat([paces[w] for w in (5, 21, 63, 126, 252)], axis=1)
    b = (paces[126] - panel.mean(axis=1)) / panel.std(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-position of the 252d pace within the cross-window pace panel (annual leg leadership)
def f02mr_f02_momentum_rotation_legpos_252d_base_v140_signal(closeadj):
    paces = {w: _f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)}
    panel = pd.concat([paces[w] for w in (5, 21, 63, 126, 252)], axis=1)
    b = (paces[252] - panel.mean(axis=1)) / panel.std(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- remaining raw-momentum structure levels -----
# half-year vs quarter pace curvature, change over a quarter (term-shape rotation, long end)
def f02mr_f02_momentum_rotation_termshift_long_base_v141_signal(closeadj):
    curv = (_f02_pace(closeadj, 126) - 0.5 * (_f02_pace(closeadj, 63)
            + _f02_pace(closeadj, 252))) * 252.0
    b = curv - curv.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 189d ROC mid-band displacement: nine-month momentum minus the midpoint of its own 504d
# hi-lo band (level form of where long momentum sits relative to its multi-year range)
def f02mr_f02_momentum_rotation_rocmid_189d_base_v142_signal(closeadj):
    roc = _f02_roc(closeadj, 189)
    hi = roc.rolling(504, min_periods=252).max()
    lo = roc.rolling(504, min_periods=252).min()
    b = roc - 0.5 * (hi + lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted hit-rate over 126d: mean tanh of daily returns minus the net pace
# (broad-vs-spiky advance: positive when many small ups beyond the net drift)
def f02mr_f02_momentum_rotation_breadthex_126d_base_v143_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    tb = np.tanh(8.0 * r).rolling(126, min_periods=63).mean()
    netpace = np.tanh(8.0 * _f02_pace(closeadj, 126))
    b = tb - netpace
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly momentum exhaustion: short 5d ROC opposing the 21d trend, gated by trend strength
def f02mr_f02_momentum_rotation_exhaust_5v21_base_v144_signal(closeadj):
    short = _f02_roc(closeadj, 5)
    trend = _f02_roc(closeadj, 21)
    b = -np.sign(trend) * short * np.tanh(15.0 * trend.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum span over the full panel divided by the median |pace| (relative span, level)
def f02mr_f02_momentum_rotation_relspan_base_v145_signal(closeadj):
    paces = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    span = paces.max(axis=1) - paces.min(axis=1)
    med = paces.abs().median(axis=1)
    b = span / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the composite momentum: front-loaded blend now minus a quarter ago
def f02mr_f02_momentum_rotation_compaccel_base_v146_signal(closeadj):
    comp = (0.4 * _f02_roc(closeadj, 21) + 0.3 * _f02_roc(closeadj, 63)
            + 0.2 * _f02_roc(closeadj, 126) + 0.1 * _f02_roc(closeadj, 252))
    b = comp - comp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-month vs half-year momentum gap as a level (medium-horizon leadership)
def f02mr_f02_momentum_rotation_pacegap_42v126_base_v147_signal(closeadj):
    b = np.tanh((_f02_pace(closeadj, 42) - _f02_pace(closeadj, 126)) * 252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net up-day count over 21d weighted by per-day magnitude (continuous monthly breadth level)
def f02mr_f02_momentum_rotation_netup_21d_base_v148_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    sgn = np.sign(r)
    b = (sgn * np.tanh(40.0 * r.abs())).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume-confirmed acceleration: 21d ROC acceleration gated by dollar-volume surge
def f02mr_f02_momentum_rotation_volaccel_base_v149_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    accel = roc - roc.shift(21)
    dv = _f02_dollar(closeadj, volume)
    surge = dv.rolling(10, min_periods=5).mean() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = accel * np.tanh(surge - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite rotation score: short-vs-long pace leadership, cross-window pace span, and the
# 63d-vs-126d term gap (a rotation-structure blend, not a net-direction composite)
def f02mr_f02_momentum_rotation_composite2_base_v150_signal(closeadj):
    paces = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    span = (paces.max(axis=1) - paces.min(axis=1)) * 252.0
    lead = (_f02_pace(closeadj, 21) - _f02_pace(closeadj, 252)) * 252.0
    gap = (_f02_pace(closeadj, 63) - _f02_pace(closeadj, 126)) * 252.0
    b = np.tanh(lead) + 0.4 * np.tanh(span) + 0.4 * np.tanh(gap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02mr_f02_momentum_rotation_roc_10d_base_v076_signal,
    f02mr_f02_momentum_rotation_roc_42d_base_v077_signal,
    f02mr_f02_momentum_rotation_roc_189d_base_v078_signal,
    f02mr_f02_momentum_rotation_mom126_252d_base_v079_signal,
    f02mr_f02_momentum_rotation_rocpos_42d_base_v080_signal,
    f02mr_f02_momentum_rotation_volmom_21d_base_v081_signal,
    f02mr_f02_momentum_rotation_volmom_63d_base_v082_signal,
    f02mr_f02_momentum_rotation_udvol_63d_base_v083_signal,
    f02mr_f02_momentum_rotation_udvol_21d_base_v084_signal,
    f02mr_f02_momentum_rotation_dvwret_63d_base_v085_signal,
    f02mr_f02_momentum_rotation_voldiverg_21d_base_v086_signal,
    f02mr_f02_momentum_rotation_volconf_252d_base_v087_signal,
    f02mr_f02_momentum_rotation_dvthrust_base_v088_signal,
    f02mr_f02_momentum_rotation_momperdv_base_v089_signal,
    f02mr_f02_momentum_rotation_udvol_126d_base_v090_signal,
    f02mr_f02_momentum_rotation_dispshort_base_v091_signal,
    f02mr_f02_momentum_rotation_displong_base_v092_signal,
    f02mr_f02_momentum_rotation_termcurv_126_base_v093_signal,
    f02mr_f02_momentum_rotation_termcurv_10_base_v094_signal,
    f02mr_f02_momentum_rotation_paceskewlong_base_v095_signal,
    f02mr_f02_momentum_rotation_poscountlong_base_v096_signal,
    f02mr_f02_momentum_rotation_spanlong_base_v097_signal,
    f02mr_f02_momentum_rotation_shortdomin_base_v098_signal,
    f02mr_f02_momentum_rotation_accel_42d_base_v099_signal,
    f02mr_f02_momentum_rotation_acceltanh_126d_base_v100_signal,
    f02mr_f02_momentum_rotation_jerk_21d_base_v101_signal,
    f02mr_f02_momentum_rotation_jerk_42d_base_v102_signal,
    f02mr_f02_momentum_rotation_mom121accel2_base_v103_signal,
    f02mr_f02_momentum_rotation_accelsm_21d_base_v104_signal,
    f02mr_f02_momentum_rotation_accelagree_base_v105_signal,
    f02mr_f02_momentum_rotation_rocpos_21d_base_v106_signal,
    f02mr_f02_momentum_rotation_rocpos_126d_base_v107_signal,
    f02mr_f02_momentum_rotation_giveback_126d_base_v108_signal,
    f02mr_f02_momentum_rotation_thrust_126d_base_v109_signal,
    f02mr_f02_momentum_rotation_giveback_21d_base_v110_signal,
    f02mr_f02_momentum_rotation_rocmid_126d_base_v111_signal,
    f02mr_f02_momentum_rotation_signmag_5d_base_v112_signal,
    f02mr_f02_momentum_rotation_signmag_42d_base_v113_signal,
    f02mr_f02_momentum_rotation_absmag_21d_base_v114_signal,
    f02mr_f02_momentum_rotation_absmag_126d_base_v115_signal,
    f02mr_f02_momentum_rotation_sqrtblendlong_base_v116_signal,
    f02mr_f02_momentum_rotation_complong_base_v117_signal,
    f02mr_f02_momentum_rotation_dispmid_base_v118_signal,
    f02mr_f02_momentum_rotation_tailasym_126d_base_v119_signal,
    f02mr_f02_momentum_rotation_spikemom_63d_base_v120_signal,
    f02mr_f02_momentum_rotation_extreme_21d_base_v121_signal,
    f02mr_f02_momentum_rotation_medret_63d_base_v122_signal,
    f02mr_f02_momentum_rotation_momskew_63d_base_v123_signal,
    f02mr_f02_momentum_rotation_wmratio_base_v124_signal,
    f02mr_f02_momentum_rotation_frontload_q_base_v125_signal,
    f02mr_f02_momentum_rotation_conc_63v252_base_v126_signal,
    f02mr_f02_momentum_rotation_lsagree_63v252_base_v127_signal,
    f02mr_f02_momentum_rotation_stackmaglong_base_v128_signal,
    f02mr_f02_momentum_rotation_balancelong_base_v129_signal,
    f02mr_f02_momentum_rotation_pullback_long_base_v130_signal,
    f02mr_f02_momentum_rotation_skiprev6_base_v131_signal,
    f02mr_f02_momentum_rotation_momext_short_base_v132_signal,
    f02mr_f02_momentum_rotation_rocdisp_21d_base_v133_signal,
    f02mr_f02_momentum_rotation_rocdisp_126d_base_v134_signal,
    f02mr_f02_momentum_rotation_mom41_84d_base_v135_signal,
    f02mr_f02_momentum_rotation_momyoy_63d_base_v136_signal,
    f02mr_f02_momentum_rotation_legpos_5d_base_v137_signal,
    f02mr_f02_momentum_rotation_legpos_21d_base_v138_signal,
    f02mr_f02_momentum_rotation_legpos_126d_base_v139_signal,
    f02mr_f02_momentum_rotation_legpos_252d_base_v140_signal,
    f02mr_f02_momentum_rotation_termshift_long_base_v141_signal,
    f02mr_f02_momentum_rotation_rocmid_189d_base_v142_signal,
    f02mr_f02_momentum_rotation_breadthex_126d_base_v143_signal,
    f02mr_f02_momentum_rotation_exhaust_5v21_base_v144_signal,
    f02mr_f02_momentum_rotation_relspan_base_v145_signal,
    f02mr_f02_momentum_rotation_compaccel_base_v146_signal,
    f02mr_f02_momentum_rotation_pacegap_42v126_base_v147_signal,
    f02mr_f02_momentum_rotation_netup_21d_base_v148_signal,
    f02mr_f02_momentum_rotation_volaccel_base_v149_signal,
    f02mr_f02_momentum_rotation_composite2_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_MOMENTUM_ROTATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f02_momentum_rotation_base_076_150_claude: %d features pass" % n_features)
