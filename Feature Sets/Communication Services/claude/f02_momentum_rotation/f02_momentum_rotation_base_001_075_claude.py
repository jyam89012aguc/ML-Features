import inspect
import numpy as np
import pandas as pd

# f02_momentum_rotation (f02mr) — Communication Services SASS signal features.
# TIGHTENED DOMAIN: RAW PRICE-MOMENTUM / ROC LEVELS ONLY.
#   ROC at 5/21/63/126/252, skip-month (12-1 = 252-21) momentum, momentum
#   strength/magnitude (sign x sqrt|roc|, tanh-compressed roc), cross-window
#   momentum DISPERSION / term-structure spreads, momentum acceleration-AS-LEVEL
#   (roc_now - roc_then ; second/third differences of log price), up-day hit-rate.
# DELIBERATELY EXCLUDED (live in sibling families, kept out to avoid overlap):
#   - Kaufman efficiency ratio / path-efficiency / fractal           -> f03
#   - return autocorrelation / variance ratio / Hurst / run-streaks  -> f03
#   - Sharpe/Sortino/vol-normalised risk-adjusted momentum           -> f08
#   - percentile-rank / z-score vs OWN history (self-relative rank)  -> f08
#   - price-vs-moving-average / MA stacking / MA slope               -> f01
# Inputs: closeadj only here (windows >21d use closeadj per SPEC).

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers (no fillna(0) in computations) =====
def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (raw momentum / ROC levels) =====
def _f02_roc(close, w):
    # rate of change over w trading days (log return = raw momentum level)
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _f02_pace(close, w):
    # per-day momentum pace = log ROC divided by horizon (term-structure unit)
    return _f02_roc(close, w) / float(w)


def _f02_skip(close, wl, ws):
    # skip-month/skip-week momentum: return from wl days ago to ws days ago
    return np.log(close.shift(ws).replace(0, np.nan) / close.shift(wl).replace(0, np.nan))


def _f02_signmag(roc):
    # signed sqrt-magnitude: compress fat momentum tails while keeping sign
    return np.sign(roc) * (roc.abs() ** 0.5)


def _f02_hit(close, w):
    # up-day hit-rate (fraction of up days minus 0.5) over w days
    up = (close.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(1, w // 2)).mean() - 0.5


# ============================================================
# ----- raw ROC levels at the canonical horizons -----
# ROC 5d (weekly momentum level)
def f02mr_f02_momentum_rotation_roc_5d_base_v001_signal(closeadj):
    b = _f02_roc(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 21d (monthly momentum level)
def f02mr_f02_momentum_rotation_roc_21d_base_v002_signal(closeadj):
    b = _f02_roc(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 63d (quarterly momentum level)
def f02mr_f02_momentum_rotation_roc_63d_base_v003_signal(closeadj):
    b = _f02_roc(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 126d (half-year momentum level)
def f02mr_f02_momentum_rotation_roc_126d_base_v004_signal(closeadj):
    b = _f02_roc(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 252d (annual momentum level)
def f02mr_f02_momentum_rotation_roc_252d_base_v005_signal(closeadj):
    b = _f02_roc(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- skip-month / skip-week momentum levels -----
# 12-1 momentum (252d return skipping the most recent 21d) — classic skip-month
def f02mr_f02_momentum_rotation_mom121_252d_base_v006_signal(closeadj):
    b = _f02_skip(closeadj, 252, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 6-1 momentum (126d return skipping recent month)
def f02mr_f02_momentum_rotation_mom61_126d_base_v007_signal(closeadj):
    b = _f02_skip(closeadj, 126, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 3-1 momentum (63d return skipping recent week)
def f02mr_f02_momentum_rotation_mom31_63d_base_v008_signal(closeadj):
    b = _f02_skip(closeadj, 63, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 9-1 momentum (189d return skipping recent month)
def f02mr_f02_momentum_rotation_mom91_189d_base_v009_signal(closeadj):
    b = _f02_skip(closeadj, 189, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-2 momentum (252d return skipping the most recent 2 months) — longer reversal purge
def f02mr_f02_momentum_rotation_mom122_252d_base_v010_signal(closeadj):
    b = _f02_skip(closeadj, 252, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intermediate-horizon momentum: 189d return skipping the most recent quarter (9-3)
def f02mr_f02_momentum_rotation_mom93_189d_base_v011_signal(closeadj):
    b = _f02_skip(closeadj, 189, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- momentum strength / magnitude (sign x compressed magnitude) -----
# signed sqrt-magnitude of 21d momentum (monthly strength, gappy-name friendly)
def f02mr_f02_momentum_rotation_signmag_21d_base_v012_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed sqrt-magnitude of 63d momentum (quarterly strength)
def f02mr_f02_momentum_rotation_signmag_63d_base_v013_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed sqrt-magnitude of 126d momentum (half-year strength)
def f02mr_f02_momentum_rotation_signmag_126d_base_v014_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed sqrt-magnitude of 252d momentum (annual strength)
def f02mr_f02_momentum_rotation_signmag_252d_base_v015_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute momentum magnitude at 63d (how big the quarterly move is, direction-blind)
def f02mr_f02_momentum_rotation_absmag_63d_base_v016_signal(closeadj):
    b = _f02_roc(closeadj, 63).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute momentum magnitude at 252d (annual move size)
def f02mr_f02_momentum_rotation_absmag_252d_base_v017_signal(closeadj):
    b = _f02_roc(closeadj, 252).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 2-1 momentum: two-month return skipping the most recent month (42d -> 21d skip) —
# a clean skip-window momentum level, distinct from any smoothed price-vs-trend measure
def f02mr_f02_momentum_rotation_mom21_42d_base_v018_signal(closeadj):
    b = _f02_skip(closeadj, 42, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year momentum measured from sub-window medians: median of overlapping 21d ROC over
# 126d (robust central momentum, dampens single-spike days — distinct from flat 126d ROC)
def f02mr_f02_momentum_rotation_medmom_126d_base_v019_signal(closeadj):
    roc21 = _f02_roc(closeadj, 21)
    b = roc21.rolling(126, min_periods=63).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# co-momentum: product of bounded short (21d) and long (126d) momentum (aligned strength
# amplified, opposing horizons cancelled) — distinct from any single-horizon ROC transform
def f02mr_f02_momentum_rotation_comom_21x126_base_v020_signal(closeadj):
    b = np.tanh(6.0 * _f02_roc(closeadj, 21)) * np.tanh(2.0 * _f02_roc(closeadj, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- cross-window momentum DISPERSION -----
# dispersion: std of ROC across 5/21/63/126/252 (how much horizons disagree in size)
def f02mr_f02_momentum_rotation_disp_roc_base_v021_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = panel.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# horizon concentration: share of total |per-day pace| held by the single strongest
# horizon (is momentum concentrated in one leg or spread across horizons?) — distinct from
# a std/range dispersion (a Herfindahl-style concentration, not a spread)
def f02mr_f02_momentum_rotation_paceconc_base_v022_signal(closeadj):
    paces = [_f02_pace(closeadj, w).abs() for w in (5, 21, 63, 126, 252)]
    panel = pd.concat(paces, axis=1)
    tot = panel.sum(axis=1)
    b = panel.max(axis=1) / tot.replace(0, np.nan) - 0.2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pace range: fastest minus slowest per-day pace across windows (horizon span)
def f02mr_f02_momentum_rotation_pacerange_base_v023_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = (panel.max(axis=1) - panel.min(axis=1)) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# best-leg pace: strongest per-day pace across windows, annualised (leading rotation leg)
def f02mr_f02_momentum_rotation_bestpace_base_v024_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = panel.max(axis=1) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# worst-leg pace: weakest per-day pace across windows, annualised (lagging rotation leg)
def f02mr_f02_momentum_rotation_worstpace_base_v025_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = panel.min(axis=1) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-horizon dispersion vs long-horizon dispersion (where the disagreement concentrates)
def f02mr_f02_momentum_rotation_dispshare_base_v026_signal(closeadj):
    sh = pd.concat([_f02_roc(closeadj, w) for w in (5, 21)], axis=1).std(axis=1)
    lo = pd.concat([_f02_roc(closeadj, w) for w in (126, 252)], axis=1).std(axis=1)
    b = sh / (sh + lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pace coefficient-of-dispersion: pace std over mean |pace| (relative horizon scatter)
def f02mr_f02_momentum_rotation_pacecv_base_v027_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = panel.std(axis=1) / panel.abs().mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- cross-window term-structure SPREADS (per-day PACE spreads — NOT equal to any
#       skip-return, since they difference horizon-normalised paces, not raw ROC levels) -----
# pace spread: quarterly per-day pace minus annual per-day pace (quarter-vs-year leadership)
def f02mr_f02_momentum_rotation_pacespr_63v252_base_v028_signal(closeadj):
    b = (_f02_pace(closeadj, 63) - _f02_pace(closeadj, 252)) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pace spread: monthly per-day pace minus half-year per-day pace (month-vs-half leadership)
def f02mr_f02_momentum_rotation_pacespr_21v126_base_v029_signal(closeadj):
    b = (_f02_pace(closeadj, 21) - _f02_pace(closeadj, 126)) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pace spread: weekly per-day pace minus quarterly per-day pace (week-vs-quarter leadership)
def f02mr_f02_momentum_rotation_pacespr_5v63_base_v030_signal(closeadj):
    b = (_f02_pace(closeadj, 5) - _f02_pace(closeadj, 63)) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-day pace spread: monthly pace minus annual pace (short-leg leadership, term units)
def f02mr_f02_momentum_rotation_pacespr_21v252_base_v031_signal(closeadj):
    b = (_f02_pace(closeadj, 21) - _f02_pace(closeadj, 252)) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure curvature: 63d pace minus the mean of the 21d and 126d paces (mid bulge)
def f02mr_f02_momentum_rotation_termcurv_63_base_v032_signal(closeadj):
    p21 = _f02_pace(closeadj, 21)
    p63 = _f02_pace(closeadj, 63)
    p126 = _f02_pace(closeadj, 126)
    b = (p63 - 0.5 * (p21 + p126)) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure curvature: 21d ROC minus the mean of the 5d and 63d ROC (short bulge)
def f02mr_f02_momentum_rotation_curv_21d_base_v033_signal(closeadj):
    b = _f02_roc(closeadj, 21) - 0.5 * (_f02_roc(closeadj, 5) + _f02_roc(closeadj, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure monotonicity: mean of tanh of adjacent ROC-level differences ordered
# short->long (is cumulative momentum building or decaying across horizons?)
def f02mr_f02_momentum_rotation_termmono_base_v034_signal(closeadj):
    rocs = [_f02_roc(closeadj, w) for w in (5, 21, 63, 126, 252)]
    diffs = [rocs[k + 1] - rocs[k] for k in range(len(rocs) - 1)]
    b = pd.concat([np.tanh(20.0 * d) for d in diffs], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum extension: 12-1 momentum versus twice the 6-1 momentum (does the full-year skip
# momentum exceed what the recent half alone projects? long-horizon over-/under-extension)
def f02mr_f02_momentum_rotation_momext_base_v035_signal(closeadj):
    b = _f02_skip(closeadj, 252, 21) - 2.0 * _f02_skip(closeadj, 126, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- momentum acceleration AS A LEVEL (differences of ROC), distinct from f01's
#       plain non-overlapping return-accel by compression / normalisation / blending -----
# overlap acceleration over a half-step: 21d ROC minus the 21d ROC 10 days ago (fast jolt)
def f02mr_f02_momentum_rotation_accel_21h_base_v036_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = roc - roc.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-compressed quarterly acceleration: bounded change in 63d ROC over a quarter
def f02mr_f02_momentum_rotation_acceltanh_63d_base_v037_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = np.tanh(8.0 * (roc - roc.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt half-year acceleration: compressed change in 126d ROC over a half-year
def f02mr_f02_momentum_rotation_accelsm_126d_base_v038_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = _f02_signmag(roc - roc.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual acceleration: 252d ROC now minus 252d ROC a year ago (long jolt, f01 has no 252 accel)
def f02mr_f02_momentum_rotation_accel_252d_base_v039_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    b = roc - roc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration term-structure: 21d acceleration minus 63d acceleration (where the jolt sits)
def f02mr_f02_momentum_rotation_accelspr_base_v040_signal(closeadj):
    r21 = _f02_roc(closeadj, 21)
    r63 = _f02_roc(closeadj, 63)
    a21 = (r21 - r21.shift(21)) / 21.0
    a63 = (r63 - r63.shift(63)) / 63.0
    b = (a21 - a63) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pace acceleration: change in the 5d per-day pace over a month (short-leg jolt, term units)
def f02mr_f02_momentum_rotation_paceaccel_5d_base_v041_signal(closeadj):
    p = _f02_pace(closeadj, 5) * 252.0
    b = p - p.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of 12-1 momentum: skip-month momentum now minus a quarter ago (clean jolt)
def f02mr_f02_momentum_rotation_mom121accel_base_v042_signal(closeadj):
    m = _f02_skip(closeadj, 252, 21)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration ratio: 21d ROC change over a month divided by the 21d ROC level (tanh-bounded)
def f02mr_f02_momentum_rotation_accelratio_21d_base_v043_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    chg = roc - roc.shift(21)
    b = np.tanh(chg / roc.abs().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jolt vs recent norm: 63d ROC minus the average of its two prior non-overlapping 63d ROCs
def f02mr_f02_momentum_rotation_accelnorm_63d_base_v044_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    prior = 0.5 * (roc.shift(63) + roc.shift(126))
    b = roc - prior
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- up-day hit-rate (the one count-based breadth facet the domain calls for, kept to
#       just two horizons; magnitude-blended for continuous resolution) + adjacent
#       raw-momentum structure levels in place of the rest -----
# up-day hit-rate over 21d, magnitude-blended (monthly breadth of advance)
def f02mr_f02_momentum_rotation_hit_21d_base_v045_signal(closeadj):
    r = closeadj.pct_change()
    b = _f02_hit(closeadj, 21) + 2.0 * r.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 3-2 momentum: 63d return skipping the most recent two weeks (63d -> 10d skip)
def f02mr_f02_momentum_rotation_mom32_63d_base_v046_signal(closeadj):
    b = _f02_skip(closeadj, 63, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-day hit-rate over 252d, magnitude-blended (annual breadth of advance)
def f02mr_f02_momentum_rotation_hit_252d_base_v047_signal(closeadj):
    r = closeadj.pct_change()
    b = _f02_hit(closeadj, 252) + 4.0 * r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mid-cluster momentum dispersion: std of ROC across 10/21/42 (short-mid disagreement)
def f02mr_f02_momentum_rotation_dispmidshort_base_v048_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (10, 21, 42)], axis=1)
    b = panel.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lagged-window momentum (6-3): the older quarter inside the half-year (126d ago -> 63d ago)
# captures momentum that has already aged out of the recent quarter (rotation memory)
def f02mr_f02_momentum_rotation_mom63_126d_base_v049_signal(closeadj):
    b = _f02_skip(closeadj, 126, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- cross-window alignment / composites of raw momentum -----
# count of positive horizons among the five windows, plus a small tanh-pace tilt so the
# discrete horizon-breadth count resolves continuously (momentum breadth across horizons)
def f02mr_f02_momentum_rotation_poscount_base_v050_signal(closeadj):
    paces = [_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)]
    cnt = sum((p > 0).astype(float) for p in paces)
    tilt = pd.concat([np.tanh(120.0 * p) for p in paces], axis=1).mean(axis=1)
    b = (cnt / 5.0 - 0.5) + 0.25 * tilt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-mean alignment of ROC across five windows (consensus momentum direction)
def f02mr_f02_momentum_rotation_align_base_v051_signal(closeadj):
    parts = [np.tanh(8.0 * _f02_roc(closeadj, w)) for w in (5, 21, 63, 126, 252)]
    b = pd.concat(parts, axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted composite momentum: front-loaded blend of 21/63/126/252 ROC levels
def f02mr_f02_momentum_rotation_composite_base_v052_signal(closeadj):
    b = (0.4 * _f02_roc(closeadj, 21) + 0.3 * _f02_roc(closeadj, 63)
         + 0.2 * _f02_roc(closeadj, 126) + 0.1 * _f02_roc(closeadj, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt composite: sum of compressed momentum magnitudes across three horizons
def f02mr_f02_momentum_rotation_sqrtblend_base_v053_signal(closeadj):
    b = (_f02_signmag(_f02_roc(closeadj, 21))
         + _f02_signmag(_f02_roc(closeadj, 63))
         + _f02_signmag(_f02_roc(closeadj, 126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full-stack alignment magnitude: product of horizon signs gated by the smallest |pace|
def f02mr_f02_momentum_rotation_stackmag_base_v054_signal(closeadj):
    paces = [_f02_pace(closeadj, w) for w in (21, 63, 126, 252)]
    sgn = np.sign(pd.concat(paces, axis=1)).prod(axis=1)
    mag = pd.concat([p.abs() for p in paces], axis=1).min(axis=1)
    b = sgn * np.tanh(150.0 * mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum span signed by the medium-horizon direction (range of horizon ROCs, directed)
def f02mr_f02_momentum_rotation_span_base_v055_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    span = panel.max(axis=1) - panel.min(axis=1)
    b = span * np.sign(_f02_roc(closeadj, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-window momentum skew: (max + min) / (max - min) of paces (asymmetry of horizons)
def f02mr_f02_momentum_rotation_paceskew_base_v056_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    hi = panel.max(axis=1)
    lo = panel.min(axis=1)
    b = (hi + lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- momentum concentration / ratio magnitudes -----
# concentration: |21d ROC| share of (|21d| + |252d|) momentum (short vs long size mix)
def f02mr_f02_momentum_rotation_conc_21v252_base_v057_signal(closeadj):
    s = _f02_roc(closeadj, 21).abs()
    l = _f02_roc(closeadj, 252).abs()
    b = s / (s + l).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# front-loading: tanh of 21d ROC over 126d ROC (how much of the move is recent)
def f02mr_f02_momentum_rotation_frontload_base_v058_signal(closeadj):
    s = _f02_roc(closeadj, 21)
    l = _f02_roc(closeadj, 126)
    b = np.tanh(s / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly-vs-quarterly directed ratio: 5d ROC share signed by the quarterly trend direction
def f02mr_f02_momentum_rotation_wkqratio_base_v059_signal(closeadj):
    s = _f02_roc(closeadj, 5)
    l = _f02_roc(closeadj, 63)
    b = np.sign(l) * s / (l.abs() + s.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# balance momentum: signed short-vs-long magnitude share, change over a quarter
def f02mr_f02_momentum_rotation_balance_base_v060_signal(closeadj):
    s = _f02_roc(closeadj, 21).abs()
    l = _f02_roc(closeadj, 126).abs()
    bal = (s - l) / (s + l).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- short-window momentum levels (raw momentum, not MA-distance) -----
# weekly momentum range-position: where the current 5d ROC sits in its own 63d hi-lo band
def f02mr_f02_momentum_rotation_rocpos_5d_base_v061_signal(closeadj):
    roc = _f02_roc(closeadj, 5)
    hi = roc.rolling(63, min_periods=21).max()
    lo = roc.rolling(63, min_periods=21).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike concentration of momentum: share of the 63d net log-return delivered by the single
# largest-magnitude day (hit-driven gaming/retail spikes — distinct momentum-quality facet)
def f02mr_f02_momentum_rotation_spikeshare_63d_base_v062_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    net = r.rolling(63, min_periods=21).sum()
    mx = r.rolling(63, min_periods=21).apply(
        lambda a: a[np.argmax(np.abs(a))], raw=True)
    b = mx / net.replace(0, np.nan)
    b = np.tanh(b)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum displacement: 63d ROC minus its trailing 63d mean ROC (surprise as level)
def f02mr_f02_momentum_rotation_rocdisp_63d_base_v063_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum giveback: 63d ROC minus its trailing 126d max (drop from peak momentum)
def f02mr_f02_momentum_rotation_giveback_63d_base_v064_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.rolling(126, min_periods=63).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum thrust: 63d ROC minus its trailing 126d min (rise from trough momentum)
def f02mr_f02_momentum_rotation_thrust_63d_base_v065_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.rolling(126, min_periods=63).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum mid-range position of 252d ROC within its own 504d hi-lo band (level, not rank)
def f02mr_f02_momentum_rotation_rocmid_252d_base_v066_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    hi = roc.rolling(504, min_periods=252).max()
    lo = roc.rolling(504, min_periods=252).min()
    b = roc - 0.5 * (hi + lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- pullback / reversal magnitudes (raw-momentum interactions) -----
# pullback: short 5d ROC opposing the 126d trend, sized by the trend magnitude
def f02mr_f02_momentum_rotation_pullback_base_v067_signal(closeadj):
    short = _f02_roc(closeadj, 5)
    long = _f02_roc(closeadj, 126)
    b = -short * np.sign(long) * long.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reversal signal: short 5d ROC against the 63d trend, gated by trend strength (tanh)
def f02mr_f02_momentum_rotation_revsig_5v63_base_v068_signal(closeadj):
    short = _f02_roc(closeadj, 5)
    trend = _f02_roc(closeadj, 63)
    b = -np.sign(trend) * short * np.tanh(10.0 * trend.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# skip-month reversal blend: 12-1 momentum minus twice the recent 21d return (reversal lean)
def f02mr_f02_momentum_rotation_skiprev_base_v069_signal(closeadj):
    m = _f02_skip(closeadj, 252, 21)
    recent = _f02_roc(closeadj, 21)
    b = m - 2.0 * recent
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- longer composite / quality-as-magnitude (raw momentum only) -----
# half-year vs annual momentum-pace ratio: per-day pace at 126d over per-day pace at 252d
# magnitude (is the recent half delivering more per-day than the full year? bounded)
def f02mr_f02_momentum_rotation_paceratio_126v252_base_v070_signal(closeadj):
    p126 = _f02_pace(closeadj, 126)
    p252 = _f02_pace(closeadj, 252)
    b = np.tanh(p126 / p252.replace(0, np.nan)) - np.tanh(252.0 * p252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-short agreement: 252d sign times 21d sign, weighted by smaller pace magnitude
def f02mr_f02_momentum_rotation_lsagree_base_v071_signal(closeadj):
    l = _f02_pace(closeadj, 252)
    s = _f02_pace(closeadj, 21)
    agree = np.sign(l) * np.sign(s)
    mag = pd.concat([l.abs(), s.abs()], axis=1).min(axis=1)
    b = agree * np.tanh(200.0 * mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mid-horizon pace leadership: half-year per-day pace minus quarterly per-day pace,
# tanh-bounded (is the half-year delivering faster per-day than the quarter?)
def f02mr_f02_momentum_rotation_pacegap_126v63_base_v072_signal(closeadj):
    b = np.tanh((_f02_pace(closeadj, 126) - _f02_pace(closeadj, 63)) * 252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast annual-momentum delta: change in 252d ROC over a single month (long momentum is
# turning quickly) — an acceleration-as-level at a short observation step
def f02mr_f02_momentum_rotation_fastdelta_252d_base_v073_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    b = roc - roc.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year momentum change: 12-1 momentum now minus 12-1 one year ago
def f02mr_f02_momentum_rotation_momyoy_base_v074_signal(closeadj):
    m = _f02_skip(closeadj, 252, 21)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year vs quarter pace curvature, change over a quarter (rotation of term shape)
def f02mr_f02_momentum_rotation_termshift_base_v075_signal(closeadj):
    curv = (_f02_pace(closeadj, 63) - 0.5 * (_f02_pace(closeadj, 21)
            + _f02_pace(closeadj, 126))) * 252.0
    b = curv - curv.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02mr_f02_momentum_rotation_roc_5d_base_v001_signal,
    f02mr_f02_momentum_rotation_roc_21d_base_v002_signal,
    f02mr_f02_momentum_rotation_roc_63d_base_v003_signal,
    f02mr_f02_momentum_rotation_roc_126d_base_v004_signal,
    f02mr_f02_momentum_rotation_roc_252d_base_v005_signal,
    f02mr_f02_momentum_rotation_mom121_252d_base_v006_signal,
    f02mr_f02_momentum_rotation_mom61_126d_base_v007_signal,
    f02mr_f02_momentum_rotation_mom31_63d_base_v008_signal,
    f02mr_f02_momentum_rotation_mom91_189d_base_v009_signal,
    f02mr_f02_momentum_rotation_mom122_252d_base_v010_signal,
    f02mr_f02_momentum_rotation_mom93_189d_base_v011_signal,
    f02mr_f02_momentum_rotation_signmag_21d_base_v012_signal,
    f02mr_f02_momentum_rotation_signmag_63d_base_v013_signal,
    f02mr_f02_momentum_rotation_signmag_126d_base_v014_signal,
    f02mr_f02_momentum_rotation_signmag_252d_base_v015_signal,
    f02mr_f02_momentum_rotation_absmag_63d_base_v016_signal,
    f02mr_f02_momentum_rotation_absmag_252d_base_v017_signal,
    f02mr_f02_momentum_rotation_mom21_42d_base_v018_signal,
    f02mr_f02_momentum_rotation_medmom_126d_base_v019_signal,
    f02mr_f02_momentum_rotation_comom_21x126_base_v020_signal,
    f02mr_f02_momentum_rotation_disp_roc_base_v021_signal,
    f02mr_f02_momentum_rotation_paceconc_base_v022_signal,
    f02mr_f02_momentum_rotation_pacerange_base_v023_signal,
    f02mr_f02_momentum_rotation_bestpace_base_v024_signal,
    f02mr_f02_momentum_rotation_worstpace_base_v025_signal,
    f02mr_f02_momentum_rotation_dispshare_base_v026_signal,
    f02mr_f02_momentum_rotation_pacecv_base_v027_signal,
    f02mr_f02_momentum_rotation_pacespr_63v252_base_v028_signal,
    f02mr_f02_momentum_rotation_pacespr_21v126_base_v029_signal,
    f02mr_f02_momentum_rotation_pacespr_5v63_base_v030_signal,
    f02mr_f02_momentum_rotation_pacespr_21v252_base_v031_signal,
    f02mr_f02_momentum_rotation_termcurv_63_base_v032_signal,
    f02mr_f02_momentum_rotation_curv_21d_base_v033_signal,
    f02mr_f02_momentum_rotation_termmono_base_v034_signal,
    f02mr_f02_momentum_rotation_momext_base_v035_signal,
    f02mr_f02_momentum_rotation_accel_21h_base_v036_signal,
    f02mr_f02_momentum_rotation_acceltanh_63d_base_v037_signal,
    f02mr_f02_momentum_rotation_accelsm_126d_base_v038_signal,
    f02mr_f02_momentum_rotation_accel_252d_base_v039_signal,
    f02mr_f02_momentum_rotation_accelspr_base_v040_signal,
    f02mr_f02_momentum_rotation_paceaccel_5d_base_v041_signal,
    f02mr_f02_momentum_rotation_mom121accel_base_v042_signal,
    f02mr_f02_momentum_rotation_accelratio_21d_base_v043_signal,
    f02mr_f02_momentum_rotation_accelnorm_63d_base_v044_signal,
    f02mr_f02_momentum_rotation_hit_21d_base_v045_signal,
    f02mr_f02_momentum_rotation_mom32_63d_base_v046_signal,
    f02mr_f02_momentum_rotation_hit_252d_base_v047_signal,
    f02mr_f02_momentum_rotation_dispmidshort_base_v048_signal,
    f02mr_f02_momentum_rotation_mom63_126d_base_v049_signal,
    f02mr_f02_momentum_rotation_poscount_base_v050_signal,
    f02mr_f02_momentum_rotation_align_base_v051_signal,
    f02mr_f02_momentum_rotation_composite_base_v052_signal,
    f02mr_f02_momentum_rotation_sqrtblend_base_v053_signal,
    f02mr_f02_momentum_rotation_stackmag_base_v054_signal,
    f02mr_f02_momentum_rotation_span_base_v055_signal,
    f02mr_f02_momentum_rotation_paceskew_base_v056_signal,
    f02mr_f02_momentum_rotation_conc_21v252_base_v057_signal,
    f02mr_f02_momentum_rotation_frontload_base_v058_signal,
    f02mr_f02_momentum_rotation_wkqratio_base_v059_signal,
    f02mr_f02_momentum_rotation_balance_base_v060_signal,
    f02mr_f02_momentum_rotation_rocpos_5d_base_v061_signal,
    f02mr_f02_momentum_rotation_spikeshare_63d_base_v062_signal,
    f02mr_f02_momentum_rotation_rocdisp_63d_base_v063_signal,
    f02mr_f02_momentum_rotation_giveback_63d_base_v064_signal,
    f02mr_f02_momentum_rotation_thrust_63d_base_v065_signal,
    f02mr_f02_momentum_rotation_rocmid_252d_base_v066_signal,
    f02mr_f02_momentum_rotation_pullback_base_v067_signal,
    f02mr_f02_momentum_rotation_revsig_5v63_base_v068_signal,
    f02mr_f02_momentum_rotation_skiprev_base_v069_signal,
    f02mr_f02_momentum_rotation_paceratio_126v252_base_v070_signal,
    f02mr_f02_momentum_rotation_lsagree_base_v071_signal,
    f02mr_f02_momentum_rotation_pacegap_126v63_base_v072_signal,
    f02mr_f02_momentum_rotation_fastdelta_252d_base_v073_signal,
    f02mr_f02_momentum_rotation_momyoy_base_v074_signal,
    f02mr_f02_momentum_rotation_termshift_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_MOMENTUM_ROTATION_REGISTRY_001_075 = REGISTRY


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

    print("OK f02_momentum_rotation_base_001_075_claude: %d features pass" % n_features)
