import inspect
import numpy as np
import pandas as pd

# f02_momentum_rotation (f02mr) - 3rd derivatives 001-150.
# Each feature = 2nd math derivative of a raw-momentum base (see base files).
# 3rd = jerk = 2nd discrete math derivative of a base. Derivative horizon chosen appropriate to the base window.
# Same tightened domain (raw ROC / momentum levels); inputs: closeadj, optional volume.

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


# ===== folder domain primitives (raw momentum / ROC levels) =====
def _f02_roc(close, w):
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _f02_pace(close, w):
    return _f02_roc(close, w) / float(w)


def _f02_skip(close, wl, ws):
    return np.log(close.shift(ws).replace(0, np.nan) / close.shift(wl).replace(0, np.nan))


def _f02_signmag(roc):
    return np.sign(roc) * (roc.abs() ** 0.5)


def _f02_hit(close, w):
    up = (close.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(1, w // 2)).mean() - 0.5


def _f02_dollar(close, vol):
    return close * vol


def _f02_dvlog(close, vol):
    return np.log(_f02_dollar(close, vol).replace(0, np.nan))


# jerk (2nd deriv) of base roc_5d over 3d
def f02mr_f02_momentum_rotation_roc_5d_3d_jerk_v001_signal(closeadj):
    b = _f02_roc(closeadj, 5)
    s = (b - b.shift(3)) / float(3)
    d = (s - s.shift(3)) / float(3)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base roc_21d over 13d
def f02mr_f02_momentum_rotation_roc_21d_13d_jerk_v002_signal(closeadj):
    b = _f02_roc(closeadj, 21)
    s = (b - b.shift(13)) / float(13)
    d = (s - s.shift(13)) / float(13)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base roc_63d over 42d
def f02mr_f02_momentum_rotation_roc_63d_42d_jerk_v003_signal(closeadj):
    b = _f02_roc(closeadj, 63)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base roc_126d over 31d
def f02mr_f02_momentum_rotation_roc_126d_31d_jerk_v004_signal(closeadj):
    b = _f02_roc(closeadj, 126)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base roc_252d over 84d
def f02mr_f02_momentum_rotation_roc_252d_84d_jerk_v005_signal(closeadj):
    b = _f02_roc(closeadj, 252)
    s = (b - b.shift(84)) / float(84)
    d = (s - s.shift(84)) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom121_252d over 42d
def f02mr_f02_momentum_rotation_mom121_252d_42d_jerk_v006_signal(closeadj):
    b = _f02_skip(closeadj, 252, 21)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom61_126d over 31d
def f02mr_f02_momentum_rotation_mom61_126d_31d_jerk_v007_signal(closeadj):
    b = _f02_skip(closeadj, 126, 21)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom31_63d over 21d
def f02mr_f02_momentum_rotation_mom31_63d_21d_jerk_v008_signal(closeadj):
    b = _f02_skip(closeadj, 63, 5)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom91_189d over 31d
def f02mr_f02_momentum_rotation_mom91_189d_31d_jerk_v009_signal(closeadj):
    b = _f02_skip(closeadj, 189, 21)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom122_252d over 84d
def f02mr_f02_momentum_rotation_mom122_252d_84d_jerk_v010_signal(closeadj):
    b = _f02_skip(closeadj, 252, 42)
    s = (b - b.shift(84)) / float(84)
    d = (s - s.shift(84)) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom93_189d over 31d
def f02mr_f02_momentum_rotation_mom93_189d_31d_jerk_v011_signal(closeadj):
    b = _f02_skip(closeadj, 189, 63)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base signmag_21d over 8d
def f02mr_f02_momentum_rotation_signmag_21d_8d_jerk_v012_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 21))
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base signmag_63d over 42d
def f02mr_f02_momentum_rotation_signmag_63d_42d_jerk_v013_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 63))
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base signmag_126d over 26d
def f02mr_f02_momentum_rotation_signmag_126d_26d_jerk_v014_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 126))
    s = (b - b.shift(26)) / float(26)
    d = (s - s.shift(26)) / float(26)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base signmag_252d over 63d
def f02mr_f02_momentum_rotation_signmag_252d_63d_jerk_v015_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 252))
    s = (b - b.shift(63)) / float(63)
    d = (s - s.shift(63)) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base absmag_63d over 42d
def f02mr_f02_momentum_rotation_absmag_63d_42d_jerk_v016_signal(closeadj):
    b = _f02_roc(closeadj, 63).abs()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base absmag_252d over 42d
def f02mr_f02_momentum_rotation_absmag_252d_42d_jerk_v017_signal(closeadj):
    b = _f02_roc(closeadj, 252).abs()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom21_42d over 21d
def f02mr_f02_momentum_rotation_mom21_42d_21d_jerk_v018_signal(closeadj):
    b = _f02_skip(closeadj, 42, 21)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base medmom_126d over 31d
def f02mr_f02_momentum_rotation_medmom_126d_31d_jerk_v019_signal(closeadj):
    roc21 = _f02_roc(closeadj, 21)
    b = roc21.rolling(126, min_periods=63).median()
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base comom_21x126 over 31d
def f02mr_f02_momentum_rotation_comom_21x126_31d_jerk_v020_signal(closeadj):
    b = np.tanh(6.0 * _f02_roc(closeadj, 21)) * np.tanh(2.0 * _f02_roc(closeadj, 126))
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base disp_roc over 15d
def f02mr_f02_momentum_rotation_disp_roc_15d_jerk_v021_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = panel.std(axis=1)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base paceconc over 31d
def f02mr_f02_momentum_rotation_paceconc_31d_jerk_v022_signal(closeadj):
    paces = [_f02_pace(closeadj, w).abs() for w in (5, 21, 63, 126, 252)]
    panel = pd.concat(paces, axis=1)
    tot = panel.sum(axis=1)
    b = panel.max(axis=1) / tot.replace(0, np.nan) - 0.2
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pacerange over 21d
def f02mr_f02_momentum_rotation_pacerange_21d_jerk_v023_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = (panel.max(axis=1) - panel.min(axis=1)) * 252.0
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base bestpace over 42d
def f02mr_f02_momentum_rotation_bestpace_42d_jerk_v024_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = panel.max(axis=1) * 252.0
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base worstpace over 21d
def f02mr_f02_momentum_rotation_worstpace_21d_jerk_v025_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = panel.min(axis=1) * 252.0
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base dispshare over 21d
def f02mr_f02_momentum_rotation_dispshare_21d_jerk_v026_signal(closeadj):
    sh = pd.concat([_f02_roc(closeadj, w) for w in (5, 21)], axis=1).std(axis=1)
    lo = pd.concat([_f02_roc(closeadj, w) for w in (126, 252)], axis=1).std(axis=1)
    b = sh / (sh + lo).replace(0, np.nan) - 0.5
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pacecv over 21d
def f02mr_f02_momentum_rotation_pacecv_21d_jerk_v027_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    b = panel.std(axis=1) / panel.abs().mean(axis=1).replace(0, np.nan)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pacespr_63v252 over 21d
def f02mr_f02_momentum_rotation_pacespr_63v252_21d_jerk_v028_signal(closeadj):
    b = (_f02_pace(closeadj, 63) - _f02_pace(closeadj, 252)) * 252.0
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pacespr_21v126 over 15d
def f02mr_f02_momentum_rotation_pacespr_21v126_15d_jerk_v029_signal(closeadj):
    b = (_f02_pace(closeadj, 21) - _f02_pace(closeadj, 126)) * 252.0
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pacespr_5v63 over 42d
def f02mr_f02_momentum_rotation_pacespr_5v63_42d_jerk_v030_signal(closeadj):
    b = (_f02_pace(closeadj, 5) - _f02_pace(closeadj, 63)) * 252.0
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pacespr_21v252 over 31d
def f02mr_f02_momentum_rotation_pacespr_21v252_31d_jerk_v031_signal(closeadj):
    b = (_f02_pace(closeadj, 21) - _f02_pace(closeadj, 252)) * 252.0
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base termcurv_63 over 15d
def f02mr_f02_momentum_rotation_termcurv_63_15d_jerk_v032_signal(closeadj):
    p21 = _f02_pace(closeadj, 21)
    p63 = _f02_pace(closeadj, 63)
    p126 = _f02_pace(closeadj, 126)
    b = (p63 - 0.5 * (p21 + p126)) * 252.0
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base curv_21d over 8d
def f02mr_f02_momentum_rotation_curv_21d_8d_jerk_v033_signal(closeadj):
    b = _f02_roc(closeadj, 21) - 0.5 * (_f02_roc(closeadj, 5) + _f02_roc(closeadj, 63))
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base termmono over 42d
def f02mr_f02_momentum_rotation_termmono_42d_jerk_v034_signal(closeadj):
    rocs = [_f02_roc(closeadj, w) for w in (5, 21, 63, 126, 252)]
    diffs = [rocs[k + 1] - rocs[k] for k in range(len(rocs) - 1)]
    b = pd.concat([np.tanh(20.0 * d) for d in diffs], axis=1).mean(axis=1)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base momext over 21d
def f02mr_f02_momentum_rotation_momext_21d_jerk_v035_signal(closeadj):
    b = _f02_skip(closeadj, 252, 21) - 2.0 * _f02_skip(closeadj, 126, 21)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accel_21h over 31d
def f02mr_f02_momentum_rotation_accel_21h_31d_jerk_v036_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = roc - roc.shift(10)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base acceltanh_63d over 15d
def f02mr_f02_momentum_rotation_acceltanh_63d_15d_jerk_v037_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = np.tanh(8.0 * (roc - roc.shift(63)))
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accelsm_126d over 31d
def f02mr_f02_momentum_rotation_accelsm_126d_31d_jerk_v038_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = _f02_signmag(roc - roc.shift(126))
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accel_252d over 42d
def f02mr_f02_momentum_rotation_accel_252d_42d_jerk_v039_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    b = roc - roc.shift(252)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accelspr over 21d
def f02mr_f02_momentum_rotation_accelspr_21d_jerk_v040_signal(closeadj):
    r21 = _f02_roc(closeadj, 21)
    r63 = _f02_roc(closeadj, 63)
    a21 = (r21 - r21.shift(21)) / 21.0
    a63 = (r63 - r63.shift(63)) / 63.0
    b = (a21 - a63) * 252.0
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base paceaccel_5d over 8d
def f02mr_f02_momentum_rotation_paceaccel_5d_8d_jerk_v041_signal(closeadj):
    p = _f02_pace(closeadj, 5) * 252.0
    b = p - p.shift(21)
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom121accel over 42d
def f02mr_f02_momentum_rotation_mom121accel_42d_jerk_v042_signal(closeadj):
    m = _f02_skip(closeadj, 252, 21)
    b = m - m.shift(63)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accelratio_21d over 8d
def f02mr_f02_momentum_rotation_accelratio_21d_8d_jerk_v043_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    chg = roc - roc.shift(21)
    b = np.tanh(chg / roc.abs().replace(0, np.nan))
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accelnorm_63d over 15d
def f02mr_f02_momentum_rotation_accelnorm_63d_15d_jerk_v044_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    prior = 0.5 * (roc.shift(63) + roc.shift(126))
    b = roc - prior
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base hit_21d over 8d
def f02mr_f02_momentum_rotation_hit_21d_8d_jerk_v045_signal(closeadj):
    r = closeadj.pct_change()
    b = _f02_hit(closeadj, 21) + 2.0 * r.rolling(21, min_periods=10).mean()
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom32_63d over 15d
def f02mr_f02_momentum_rotation_mom32_63d_15d_jerk_v046_signal(closeadj):
    b = _f02_skip(closeadj, 63, 10)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base hit_252d over 42d
def f02mr_f02_momentum_rotation_hit_252d_42d_jerk_v047_signal(closeadj):
    r = closeadj.pct_change()
    b = _f02_hit(closeadj, 252) + 4.0 * r.rolling(252, min_periods=126).mean()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base dispmidshort over 31d
def f02mr_f02_momentum_rotation_dispmidshort_31d_jerk_v048_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (10, 21, 42)], axis=1)
    b = panel.std(axis=1)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom63_126d over 26d
def f02mr_f02_momentum_rotation_mom63_126d_26d_jerk_v049_signal(closeadj):
    b = _f02_skip(closeadj, 126, 63)
    s = (b - b.shift(26)) / float(26)
    d = (s - s.shift(26)) / float(26)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base poscount over 21d
def f02mr_f02_momentum_rotation_poscount_21d_jerk_v050_signal(closeadj):
    paces = [_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)]
    cnt = sum((p > 0).astype(float) for p in paces)
    tilt = pd.concat([np.tanh(120.0 * p) for p in paces], axis=1).mean(axis=1)
    b = (cnt / 5.0 - 0.5) + 0.25 * tilt
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base align over 31d
def f02mr_f02_momentum_rotation_align_31d_jerk_v051_signal(closeadj):
    parts = [np.tanh(8.0 * _f02_roc(closeadj, w)) for w in (5, 21, 63, 126, 252)]
    b = pd.concat(parts, axis=1).mean(axis=1)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base composite over 42d
def f02mr_f02_momentum_rotation_composite_42d_jerk_v052_signal(closeadj):
    b = (0.4 * _f02_roc(closeadj, 21) + 0.3 * _f02_roc(closeadj, 63)
         + 0.2 * _f02_roc(closeadj, 126) + 0.1 * _f02_roc(closeadj, 252))
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base sqrtblend over 15d
def f02mr_f02_momentum_rotation_sqrtblend_15d_jerk_v053_signal(closeadj):
    b = (_f02_signmag(_f02_roc(closeadj, 21))
         + _f02_signmag(_f02_roc(closeadj, 63))
         + _f02_signmag(_f02_roc(closeadj, 126)))
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base stackmag over 21d
def f02mr_f02_momentum_rotation_stackmag_21d_jerk_v054_signal(closeadj):
    paces = [_f02_pace(closeadj, w) for w in (21, 63, 126, 252)]
    sgn = np.sign(pd.concat(paces, axis=1)).prod(axis=1)
    mag = pd.concat([p.abs() for p in paces], axis=1).min(axis=1)
    b = sgn * np.tanh(150.0 * mag)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base span over 21d
def f02mr_f02_momentum_rotation_span_21d_jerk_v055_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    span = panel.max(axis=1) - panel.min(axis=1)
    b = span * np.sign(_f02_roc(closeadj, 126))
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base paceskew over 42d
def f02mr_f02_momentum_rotation_paceskew_42d_jerk_v056_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    hi = panel.max(axis=1)
    lo = panel.min(axis=1)
    b = (hi + lo) / (hi - lo).replace(0, np.nan)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base conc_21v252 over 21d
def f02mr_f02_momentum_rotation_conc_21v252_21d_jerk_v057_signal(closeadj):
    s = _f02_roc(closeadj, 21).abs()
    l = _f02_roc(closeadj, 252).abs()
    b = s / (s + l).replace(0, np.nan) - 0.5
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base frontload over 42d
def f02mr_f02_momentum_rotation_frontload_42d_jerk_v058_signal(closeadj):
    s = _f02_roc(closeadj, 21)
    l = _f02_roc(closeadj, 126)
    b = np.tanh(s / l.replace(0, np.nan))
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base wkqratio over 21d
def f02mr_f02_momentum_rotation_wkqratio_21d_jerk_v059_signal(closeadj):
    s = _f02_roc(closeadj, 5)
    l = _f02_roc(closeadj, 63)
    b = np.sign(l) * s / (l.abs() + s.abs()).replace(0, np.nan)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base balance over 31d
def f02mr_f02_momentum_rotation_balance_31d_jerk_v060_signal(closeadj):
    s = _f02_roc(closeadj, 21).abs()
    l = _f02_roc(closeadj, 126).abs()
    bal = (s - l) / (s + l).replace(0, np.nan)
    b = bal - bal.shift(63)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocpos_5d over 8d
def f02mr_f02_momentum_rotation_rocpos_5d_8d_jerk_v061_signal(closeadj):
    roc = _f02_roc(closeadj, 5)
    hi = roc.rolling(63, min_periods=21).max()
    lo = roc.rolling(63, min_periods=21).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base spikeshare_63d over 21d
def f02mr_f02_momentum_rotation_spikeshare_63d_21d_jerk_v062_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    net = r.rolling(63, min_periods=21).sum()
    mx = r.rolling(63, min_periods=21).apply(
        lambda a: a[np.argmax(np.abs(a))], raw=True)
    b = mx / net.replace(0, np.nan)
    b = np.tanh(b)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocdisp_63d over 42d
def f02mr_f02_momentum_rotation_rocdisp_63d_42d_jerk_v063_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.rolling(63, min_periods=21).mean()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base giveback_63d over 15d
def f02mr_f02_momentum_rotation_giveback_63d_15d_jerk_v064_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.rolling(126, min_periods=63).max()
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base thrust_63d over 42d
def f02mr_f02_momentum_rotation_thrust_63d_42d_jerk_v065_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.rolling(126, min_periods=63).min()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocmid_252d over 84d
def f02mr_f02_momentum_rotation_rocmid_252d_84d_jerk_v066_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    hi = roc.rolling(504, min_periods=252).max()
    lo = roc.rolling(504, min_periods=252).min()
    b = roc - 0.5 * (hi + lo)
    s = (b - b.shift(84)) / float(84)
    d = (s - s.shift(84)) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pullback over 21d
def f02mr_f02_momentum_rotation_pullback_21d_jerk_v067_signal(closeadj):
    short = _f02_roc(closeadj, 5)
    long = _f02_roc(closeadj, 126)
    b = -short * np.sign(long) * long.abs()
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base revsig_5v63 over 42d
def f02mr_f02_momentum_rotation_revsig_5v63_42d_jerk_v068_signal(closeadj):
    short = _f02_roc(closeadj, 5)
    trend = _f02_roc(closeadj, 63)
    b = -np.sign(trend) * short * np.tanh(10.0 * trend.abs())
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base skiprev over 21d
def f02mr_f02_momentum_rotation_skiprev_21d_jerk_v069_signal(closeadj):
    m = _f02_skip(closeadj, 252, 21)
    recent = _f02_roc(closeadj, 21)
    b = m - 2.0 * recent
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base paceratio_126v252 over 21d
def f02mr_f02_momentum_rotation_paceratio_126v252_21d_jerk_v070_signal(closeadj):
    p126 = _f02_pace(closeadj, 126)
    p252 = _f02_pace(closeadj, 252)
    b = np.tanh(p126 / p252.replace(0, np.nan)) - np.tanh(252.0 * p252)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base lsagree over 31d
def f02mr_f02_momentum_rotation_lsagree_31d_jerk_v071_signal(closeadj):
    l = _f02_pace(closeadj, 252)
    s = _f02_pace(closeadj, 21)
    agree = np.sign(l) * np.sign(s)
    mag = pd.concat([l.abs(), s.abs()], axis=1).min(axis=1)
    b = agree * np.tanh(200.0 * mag)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pacegap_126v63 over 15d
def f02mr_f02_momentum_rotation_pacegap_126v63_15d_jerk_v072_signal(closeadj):
    b = np.tanh((_f02_pace(closeadj, 126) - _f02_pace(closeadj, 63)) * 252.0)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base fastdelta_252d over 84d
def f02mr_f02_momentum_rotation_fastdelta_252d_84d_jerk_v073_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    b = roc - roc.shift(21)
    s = (b - b.shift(84)) / float(84)
    d = (s - s.shift(84)) / float(84)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base momyoy over 15d
def f02mr_f02_momentum_rotation_momyoy_15d_jerk_v074_signal(closeadj):
    m = _f02_skip(closeadj, 252, 21)
    b = m - m.shift(252)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base termshift over 21d
def f02mr_f02_momentum_rotation_termshift_21d_jerk_v075_signal(closeadj):
    curv = (_f02_pace(closeadj, 63) - 0.5 * (_f02_pace(closeadj, 21)
            + _f02_pace(closeadj, 126))) * 252.0
    b = curv - curv.shift(63)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base roc_10d over 8d
def f02mr_f02_momentum_rotation_roc_10d_8d_jerk_v076_signal(closeadj):
    b = _f02_roc(closeadj, 10)
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base roc_42d over 21d
def f02mr_f02_momentum_rotation_roc_42d_21d_jerk_v077_signal(closeadj):
    b = _f02_roc(closeadj, 42)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base roc_189d over 63d
def f02mr_f02_momentum_rotation_roc_189d_63d_jerk_v078_signal(closeadj):
    b = _f02_roc(closeadj, 189)
    s = (b - b.shift(63)) / float(63)
    d = (s - s.shift(63)) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom126_252d over 42d
def f02mr_f02_momentum_rotation_mom126_252d_42d_jerk_v079_signal(closeadj):
    b = _f02_skip(closeadj, 252, 126)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocpos_42d over 15d
def f02mr_f02_momentum_rotation_rocpos_42d_15d_jerk_v080_signal(closeadj):
    roc = _f02_roc(closeadj, 42)
    hi = roc.rolling(126, min_periods=63).max()
    lo = roc.rolling(126, min_periods=63).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base volmom_21d over 5d
def f02mr_f02_momentum_rotation_volmom_21d_5d_jerk_v081_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    dv = _f02_dollar(closeadj, volume)
    surge = dv.rolling(21, min_periods=10).mean() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = roc * np.tanh(surge - 1.0)
    s = (b - b.shift(5)) / float(5)
    d = (s - s.shift(5)) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base volmom_63d over 15d
def f02mr_f02_momentum_rotation_volmom_63d_15d_jerk_v082_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 63)
    dv = _f02_dollar(closeadj, volume)
    g = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
               / dv.rolling(63, min_periods=21).mean().replace(0, np.nan))
    b = np.tanh(5.0 * roc) + np.tanh(2.0 * g)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base udvol_63d over 21d
def f02mr_f02_momentum_rotation_udvol_63d_21d_jerk_v083_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = _f02_dollar(closeadj, volume)
    upv = dv.where(r > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(r < 0, 0.0).rolling(63, min_periods=21).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base udvol_21d over 13d
def f02mr_f02_momentum_rotation_udvol_21d_13d_jerk_v084_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = _f02_dollar(closeadj, volume)
    upv = dv.where(r > 0, 0.0).rolling(21, min_periods=10).sum()
    dnv = dv.where(r < 0, 0.0).rolling(21, min_periods=10).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    s = (b - b.shift(13)) / float(13)
    d = (s - s.shift(13)) / float(13)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base dvwret_63d over 21d
def f02mr_f02_momentum_rotation_dvwret_63d_21d_jerk_v085_signal(closeadj, volume):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    dv = _f02_dollar(closeadj, volume)
    num = (r * dv).rolling(63, min_periods=21).sum()
    den = dv.rolling(63, min_periods=21).sum()
    b = num / den.replace(0, np.nan)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base voldiverg_21d over 13d
def f02mr_f02_momentum_rotation_voldiverg_21d_13d_jerk_v086_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    dv = _f02_dvlog(closeadj, volume)
    dvtrend = dv - dv.shift(21)
    b = np.tanh(5.0 * roc) * np.tanh(2.0 * dvtrend)
    s = (b - b.shift(13)) / float(13)
    d = (s - s.shift(13)) / float(13)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base volconf_252d over 42d
def f02mr_f02_momentum_rotation_volconf_252d_42d_jerk_v087_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 252)
    dv = _f02_dvlog(closeadj, volume)
    dvtrend = dv.rolling(63, min_periods=21).mean() - dv.rolling(252, min_periods=126).mean()
    b = roc * np.tanh(dvtrend)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base dvthrust over 15d
def f02mr_f02_momentum_rotation_dvthrust_15d_jerk_v088_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    dv = _f02_dollar(closeadj, volume)
    surge = dv.rolling(5, min_periods=3).mean() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = np.sign(roc) * np.tanh(surge - 1.0)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base momperdv over 42d
def f02mr_f02_momentum_rotation_momperdv_42d_jerk_v089_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    dv = _f02_dvlog(closeadj, volume)
    dvc = dv - dv.rolling(252, min_periods=126).mean()
    b = roc * np.tanh(-dvc)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base udvol_126d over 42d
def f02mr_f02_momentum_rotation_udvol_126d_42d_jerk_v090_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = _f02_dollar(closeadj, volume)
    upv = dv.where(r > 0, 0.0).rolling(126, min_periods=63).sum()
    dnv = dv.where(r < 0, 0.0).rolling(126, min_periods=63).sum()
    ratio = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    b = _f02_signmag(ratio)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base dispshort over 42d
def f02mr_f02_momentum_rotation_dispshort_42d_jerk_v091_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (5, 10, 21)], axis=1)
    b = panel.std(axis=1)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base displong over 15d
def f02mr_f02_momentum_rotation_displong_15d_jerk_v092_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (126, 189, 252)], axis=1)
    b = panel.std(axis=1)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base termcurv_126 over 21d
def f02mr_f02_momentum_rotation_termcurv_126_21d_jerk_v093_signal(closeadj):
    p63 = _f02_pace(closeadj, 63)
    p126 = _f02_pace(closeadj, 126)
    p252 = _f02_pace(closeadj, 252)
    b = (p126 - 0.5 * (p63 + p252)) * 252.0
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base termcurv_10 over 31d
def f02mr_f02_momentum_rotation_termcurv_10_31d_jerk_v094_signal(closeadj):
    p5 = _f02_pace(closeadj, 5)
    p10 = _f02_pace(closeadj, 10)
    p21 = _f02_pace(closeadj, 21)
    b = (p10 - 0.5 * (p5 + p21)) * 252.0
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base paceskewlong over 31d
def f02mr_f02_momentum_rotation_paceskewlong_31d_jerk_v095_signal(closeadj):
    panel = pd.concat([_f02_pace(closeadj, w) for w in (63, 126, 189, 252)], axis=1)
    hi = panel.max(axis=1)
    lo = panel.min(axis=1)
    b = (hi + lo) / (hi - lo).replace(0, np.nan)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base poscountlong over 42d
def f02mr_f02_momentum_rotation_poscountlong_42d_jerk_v096_signal(closeadj):
    paces = [_f02_pace(closeadj, w) for w in (63, 126, 189, 252)]
    cnt = sum((p > 0).astype(float) for p in paces)
    tilt = pd.concat([np.tanh(120.0 * p) for p in paces], axis=1).mean(axis=1)
    b = (cnt / 4.0 - 0.5) + 0.25 * tilt
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base spanlong over 42d
def f02mr_f02_momentum_rotation_spanlong_42d_jerk_v097_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (63, 126, 189, 252)], axis=1)
    span = panel.max(axis=1) - panel.min(axis=1)
    b = span * np.sign(_f02_roc(closeadj, 252))
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base shortdomin over 21d
def f02mr_f02_momentum_rotation_shortdomin_21d_jerk_v098_signal(closeadj):
    sh = pd.concat([_f02_roc(closeadj, w).abs() for w in (5, 10, 21)], axis=1).sum(axis=1)
    al = pd.concat([_f02_roc(closeadj, w).abs() for w in (5, 10, 21, 63, 126, 252)], axis=1).sum(axis=1)
    b = sh / al.replace(0, np.nan) - 0.5
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accel_42d over 10d
def f02mr_f02_momentum_rotation_accel_42d_10d_jerk_v099_signal(closeadj):
    roc = _f02_roc(closeadj, 42)
    b = roc - roc.shift(21)
    s = (b - b.shift(10)) / float(10)
    d = (s - s.shift(10)) / float(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base acceltanh_126d over 42d
def f02mr_f02_momentum_rotation_acceltanh_126d_42d_jerk_v100_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = np.tanh(4.0 * (roc - roc.shift(63)))
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base jerk_21d over 8d
def f02mr_f02_momentum_rotation_jerk_21d_8d_jerk_v101_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    b = lp - 3.0 * lp.shift(21) + 3.0 * lp.shift(42) - lp.shift(63)
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base jerk_42d over 21d
def f02mr_f02_momentum_rotation_jerk_42d_21d_jerk_v102_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    b = lp - 3.0 * lp.shift(42) + 3.0 * lp.shift(84) - lp.shift(126)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom121accel2 over 31d
def f02mr_f02_momentum_rotation_mom121accel2_31d_jerk_v103_signal(closeadj):
    m = _f02_skip(closeadj, 252, 21)
    b = m - m.shift(126)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accelsm_21d over 8d
def f02mr_f02_momentum_rotation_accelsm_21d_8d_jerk_v104_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = _f02_signmag(roc - roc.shift(63))
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base accelagree over 21d
def f02mr_f02_momentum_rotation_accelagree_21d_jerk_v105_signal(closeadj):
    r21 = _f02_roc(closeadj, 21)
    r126 = _f02_roc(closeadj, 126)
    a21 = r21 - r21.shift(21)
    a126 = r126 - r126.shift(126)
    agree = np.sign(a21) * np.sign(a126)
    mag = pd.concat([a21.abs(), a126.abs()], axis=1).min(axis=1)
    b = agree * np.tanh(20.0 * mag)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocpos_21d over 5d
def f02mr_f02_momentum_rotation_rocpos_21d_5d_jerk_v106_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    hi = roc.rolling(126, min_periods=63).max()
    lo = roc.rolling(126, min_periods=63).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    s = (b - b.shift(5)) / float(5)
    d = (s - s.shift(5)) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocpos_126d over 31d
def f02mr_f02_momentum_rotation_rocpos_126d_31d_jerk_v107_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    hi = roc.rolling(252, min_periods=126).max()
    lo = roc.rolling(252, min_periods=126).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base giveback_126d over 26d
def f02mr_f02_momentum_rotation_giveback_126d_26d_jerk_v108_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = roc - roc.rolling(252, min_periods=126).max()
    s = (b - b.shift(26)) / float(26)
    d = (s - s.shift(26)) / float(26)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base thrust_126d over 42d
def f02mr_f02_momentum_rotation_thrust_126d_42d_jerk_v109_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = roc - roc.rolling(252, min_periods=126).min()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base giveback_21d over 13d
def f02mr_f02_momentum_rotation_giveback_21d_13d_jerk_v110_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = roc - roc.rolling(63, min_periods=21).max()
    s = (b - b.shift(13)) / float(13)
    d = (s - s.shift(13)) / float(13)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocmid_126d over 42d
def f02mr_f02_momentum_rotation_rocmid_126d_42d_jerk_v111_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    hi = roc.rolling(504, min_periods=252).max()
    lo = roc.rolling(504, min_periods=252).min()
    b = roc - 0.5 * (hi + lo)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base signmag_5d over 5d
def f02mr_f02_momentum_rotation_signmag_5d_5d_jerk_v112_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 5))
    s = (b - b.shift(5)) / float(5)
    d = (s - s.shift(5)) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base signmag_42d over 10d
def f02mr_f02_momentum_rotation_signmag_42d_10d_jerk_v113_signal(closeadj):
    b = _f02_signmag(_f02_roc(closeadj, 42))
    s = (b - b.shift(10)) / float(10)
    d = (s - s.shift(10)) / float(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base absmag_21d over 8d
def f02mr_f02_momentum_rotation_absmag_21d_8d_jerk_v114_signal(closeadj):
    b = _f02_roc(closeadj, 21).abs()
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base absmag_126d over 42d
def f02mr_f02_momentum_rotation_absmag_126d_42d_jerk_v115_signal(closeadj):
    b = _f02_roc(closeadj, 126).abs()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base sqrtblendlong over 42d
def f02mr_f02_momentum_rotation_sqrtblendlong_42d_jerk_v116_signal(closeadj):
    b = (_f02_signmag(_f02_roc(closeadj, 63))
         + _f02_signmag(_f02_roc(closeadj, 126))
         + _f02_signmag(_f02_roc(closeadj, 252)))
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base complong over 15d
def f02mr_f02_momentum_rotation_complong_15d_jerk_v117_signal(closeadj):
    b = (0.1 * _f02_roc(closeadj, 21) + 0.2 * _f02_roc(closeadj, 63)
         + 0.3 * _f02_roc(closeadj, 126) + 0.4 * _f02_roc(closeadj, 252))
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base dispmid over 15d
def f02mr_f02_momentum_rotation_dispmid_15d_jerk_v118_signal(closeadj):
    panel = pd.concat([_f02_roc(closeadj, w) for w in (21, 42, 63)], axis=1)
    b = panel.std(axis=1)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base tailasym_126d over 26d
def f02mr_f02_momentum_rotation_tailasym_126d_26d_jerk_v119_signal(closeadj):
    r = closeadj.pct_change()
    up5 = r.rolling(126, min_periods=63).apply(lambda a: np.mean(np.sort(a)[-5:]), raw=True)
    dn5 = r.rolling(126, min_periods=63).apply(lambda a: -np.mean(np.sort(a)[:5]), raw=True)
    b = (up5 - dn5) / (up5 + dn5).replace(0, np.nan)
    s = (b - b.shift(26)) / float(26)
    d = (s - s.shift(26)) / float(26)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base spikemom_63d over 21d
def f02mr_f02_momentum_rotation_spikemom_63d_21d_jerk_v120_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    sd = r.rolling(63, min_periods=21).std()
    spike = r.where(r.abs() > 2.0 * sd, 0.0)
    b = spike.rolling(63, min_periods=21).sum()
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base extreme_21d over 8d
def f02mr_f02_momentum_rotation_extreme_21d_8d_jerk_v121_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    mx = r.rolling(21, min_periods=10).max()
    mn = r.rolling(21, min_periods=10).min()
    b = mx + mn
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base medret_63d over 42d
def f02mr_f02_momentum_rotation_medret_63d_42d_jerk_v122_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    b = r.rolling(63, min_periods=21).median() * 63.0
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base momskew_63d over 31d
def f02mr_f02_momentum_rotation_momskew_63d_31d_jerk_v123_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    mn = r.rolling(63, min_periods=21).mean()
    md = r.rolling(63, min_periods=21).median()
    b = (mn - md) * 1000.0
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base wmratio over 42d
def f02mr_f02_momentum_rotation_wmratio_42d_jerk_v124_signal(closeadj):
    s = _f02_roc(closeadj, 5)
    m = _f02_roc(closeadj, 21)
    b = np.sign(m) * s / (m.abs() + s.abs()).replace(0, np.nan)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base frontload_q over 31d
def f02mr_f02_momentum_rotation_frontload_q_31d_jerk_v125_signal(closeadj):
    s = _f02_roc(closeadj, 63)
    l = _f02_roc(closeadj, 252)
    b = np.tanh(s / l.replace(0, np.nan))
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base conc_63v252 over 15d
def f02mr_f02_momentum_rotation_conc_63v252_15d_jerk_v126_signal(closeadj):
    s = _f02_roc(closeadj, 63).abs()
    l = _f02_roc(closeadj, 252).abs()
    b = s / (s + l).replace(0, np.nan) - 0.5
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base lsagree_63v252 over 21d
def f02mr_f02_momentum_rotation_lsagree_63v252_21d_jerk_v127_signal(closeadj):
    l = _f02_pace(closeadj, 252)
    s = _f02_pace(closeadj, 63)
    agree = np.sign(l) * np.sign(s)
    mag = pd.concat([l.abs(), s.abs()], axis=1).min(axis=1)
    b = agree * np.tanh(150.0 * mag)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base stackmaglong over 42d
def f02mr_f02_momentum_rotation_stackmaglong_42d_jerk_v128_signal(closeadj):
    paces = [_f02_pace(closeadj, w) for w in (63, 126, 252)]
    sgn = np.sign(pd.concat(paces, axis=1)).prod(axis=1)
    mag = pd.concat([p.abs() for p in paces], axis=1).min(axis=1)
    b = sgn * np.tanh(150.0 * mag)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base balancelong over 42d
def f02mr_f02_momentum_rotation_balancelong_42d_jerk_v129_signal(closeadj):
    s = _f02_roc(closeadj, 63).abs()
    l = _f02_roc(closeadj, 252).abs()
    bal = (s - l) / (s + l).replace(0, np.nan)
    b = bal - bal.shift(63)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pullback_long over 42d
def f02mr_f02_momentum_rotation_pullback_long_42d_jerk_v130_signal(closeadj):
    short = _f02_roc(closeadj, 21)
    long = _f02_roc(closeadj, 252)
    b = -short * np.sign(long) * long.abs()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base skiprev6 over 21d
def f02mr_f02_momentum_rotation_skiprev6_21d_jerk_v131_signal(closeadj):
    m = _f02_skip(closeadj, 126, 21)
    recent = _f02_roc(closeadj, 21)
    b = m - 2.0 * recent
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base momext_short over 21d
def f02mr_f02_momentum_rotation_momext_short_21d_jerk_v132_signal(closeadj):
    b = _f02_skip(closeadj, 126, 21) - _f02_skip(closeadj, 63, 5)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocdisp_21d over 8d
def f02mr_f02_momentum_rotation_rocdisp_21d_8d_jerk_v133_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = roc - roc.rolling(63, min_periods=21).mean()
    s = (b - b.shift(8)) / float(8)
    d = (s - s.shift(8)) / float(8)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocdisp_126d over 42d
def f02mr_f02_momentum_rotation_rocdisp_126d_42d_jerk_v134_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = roc - roc.rolling(126, min_periods=63).mean()
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base mom41_84d over 31d
def f02mr_f02_momentum_rotation_mom41_84d_31d_jerk_v135_signal(closeadj):
    b = _f02_skip(closeadj, 84, 21)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base momyoy_63d over 31d
def f02mr_f02_momentum_rotation_momyoy_63d_31d_jerk_v136_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.shift(252)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base legpos_5d over 3d
def f02mr_f02_momentum_rotation_legpos_5d_3d_jerk_v137_signal(closeadj):
    paces = {w: _f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)}
    panel = pd.concat([paces[w] for w in (5, 21, 63, 126, 252)], axis=1)
    b = (paces[5] - panel.mean(axis=1)) / panel.std(axis=1).replace(0, np.nan)
    s = (b - b.shift(3)) / float(3)
    d = (s - s.shift(3)) / float(3)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base legpos_21d over 13d
def f02mr_f02_momentum_rotation_legpos_21d_13d_jerk_v138_signal(closeadj):
    paces = {w: _f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)}
    panel = pd.concat([paces[w] for w in (5, 21, 63, 126, 252)], axis=1)
    b = (paces[21] - panel.mean(axis=1)) / panel.std(axis=1).replace(0, np.nan)
    s = (b - b.shift(13)) / float(13)
    d = (s - s.shift(13)) / float(13)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base legpos_126d over 26d
def f02mr_f02_momentum_rotation_legpos_126d_26d_jerk_v139_signal(closeadj):
    paces = {w: _f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)}
    panel = pd.concat([paces[w] for w in (5, 21, 63, 126, 252)], axis=1)
    b = (paces[126] - panel.mean(axis=1)) / panel.std(axis=1).replace(0, np.nan)
    s = (b - b.shift(26)) / float(26)
    d = (s - s.shift(26)) / float(26)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base legpos_252d over 63d
def f02mr_f02_momentum_rotation_legpos_252d_63d_jerk_v140_signal(closeadj):
    paces = {w: _f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)}
    panel = pd.concat([paces[w] for w in (5, 21, 63, 126, 252)], axis=1)
    b = (paces[252] - panel.mean(axis=1)) / panel.std(axis=1).replace(0, np.nan)
    s = (b - b.shift(63)) / float(63)
    d = (s - s.shift(63)) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base termshift_long over 31d
def f02mr_f02_momentum_rotation_termshift_long_31d_jerk_v141_signal(closeadj):
    curv = (_f02_pace(closeadj, 126) - 0.5 * (_f02_pace(closeadj, 63)
            + _f02_pace(closeadj, 252))) * 252.0
    b = curv - curv.shift(63)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base rocmid_189d over 31d
def f02mr_f02_momentum_rotation_rocmid_189d_31d_jerk_v142_signal(closeadj):
    roc = _f02_roc(closeadj, 189)
    hi = roc.rolling(504, min_periods=252).max()
    lo = roc.rolling(504, min_periods=252).min()
    b = roc - 0.5 * (hi + lo)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base breadthex_126d over 42d
def f02mr_f02_momentum_rotation_breadthex_126d_42d_jerk_v143_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    tb = np.tanh(8.0 * r).rolling(126, min_periods=63).mean()
    netpace = np.tanh(8.0 * _f02_pace(closeadj, 126))
    b = tb - netpace
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base exhaust_5v21 over 42d
def f02mr_f02_momentum_rotation_exhaust_5v21_42d_jerk_v144_signal(closeadj):
    short = _f02_roc(closeadj, 5)
    trend = _f02_roc(closeadj, 21)
    b = -np.sign(trend) * short * np.tanh(15.0 * trend.abs())
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base relspan over 31d
def f02mr_f02_momentum_rotation_relspan_31d_jerk_v145_signal(closeadj):
    paces = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    span = paces.max(axis=1) - paces.min(axis=1)
    med = paces.abs().median(axis=1)
    b = span / med.replace(0, np.nan)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base compaccel over 21d
def f02mr_f02_momentum_rotation_compaccel_21d_jerk_v146_signal(closeadj):
    comp = (0.4 * _f02_roc(closeadj, 21) + 0.3 * _f02_roc(closeadj, 63)
            + 0.2 * _f02_roc(closeadj, 126) + 0.1 * _f02_roc(closeadj, 252))
    b = comp - comp.shift(63)
    s = (b - b.shift(21)) / float(21)
    d = (s - s.shift(21)) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base pacegap_42v126 over 15d
def f02mr_f02_momentum_rotation_pacegap_42v126_15d_jerk_v147_signal(closeadj):
    b = np.tanh((_f02_pace(closeadj, 42) - _f02_pace(closeadj, 126)) * 252.0)
    s = (b - b.shift(15)) / float(15)
    d = (s - s.shift(15)) / float(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base netup_21d over 13d
def f02mr_f02_momentum_rotation_netup_21d_13d_jerk_v148_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    sgn = np.sign(r)
    b = (sgn * np.tanh(40.0 * r.abs())).rolling(21, min_periods=10).mean()
    s = (b - b.shift(13)) / float(13)
    d = (s - s.shift(13)) / float(13)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base volaccel over 31d
def f02mr_f02_momentum_rotation_volaccel_31d_jerk_v149_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 21)
    accel = roc - roc.shift(21)
    dv = _f02_dollar(closeadj, volume)
    surge = dv.rolling(10, min_periods=5).mean() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = accel * np.tanh(surge - 1.0)
    s = (b - b.shift(31)) / float(31)
    d = (s - s.shift(31)) / float(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd deriv) of base composite2 over 42d
def f02mr_f02_momentum_rotation_composite2_42d_jerk_v150_signal(closeadj):
    paces = pd.concat([_f02_pace(closeadj, w) for w in (5, 21, 63, 126, 252)], axis=1)
    span = (paces.max(axis=1) - paces.min(axis=1)) * 252.0
    lead = (_f02_pace(closeadj, 21) - _f02_pace(closeadj, 252)) * 252.0
    gap = (_f02_pace(closeadj, 63) - _f02_pace(closeadj, 126)) * 252.0
    b = np.tanh(lead) + 0.4 * np.tanh(span) + 0.4 * np.tanh(gap)
    s = (b - b.shift(42)) / float(42)
    d = (s - s.shift(42)) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f02mr_f02_momentum_rotation_roc_5d_3d_jerk_v001_signal,
    f02mr_f02_momentum_rotation_roc_21d_13d_jerk_v002_signal,
    f02mr_f02_momentum_rotation_roc_63d_42d_jerk_v003_signal,
    f02mr_f02_momentum_rotation_roc_126d_31d_jerk_v004_signal,
    f02mr_f02_momentum_rotation_roc_252d_84d_jerk_v005_signal,
    f02mr_f02_momentum_rotation_mom121_252d_42d_jerk_v006_signal,
    f02mr_f02_momentum_rotation_mom61_126d_31d_jerk_v007_signal,
    f02mr_f02_momentum_rotation_mom31_63d_21d_jerk_v008_signal,
    f02mr_f02_momentum_rotation_mom91_189d_31d_jerk_v009_signal,
    f02mr_f02_momentum_rotation_mom122_252d_84d_jerk_v010_signal,
    f02mr_f02_momentum_rotation_mom93_189d_31d_jerk_v011_signal,
    f02mr_f02_momentum_rotation_signmag_21d_8d_jerk_v012_signal,
    f02mr_f02_momentum_rotation_signmag_63d_42d_jerk_v013_signal,
    f02mr_f02_momentum_rotation_signmag_126d_26d_jerk_v014_signal,
    f02mr_f02_momentum_rotation_signmag_252d_63d_jerk_v015_signal,
    f02mr_f02_momentum_rotation_absmag_63d_42d_jerk_v016_signal,
    f02mr_f02_momentum_rotation_absmag_252d_42d_jerk_v017_signal,
    f02mr_f02_momentum_rotation_mom21_42d_21d_jerk_v018_signal,
    f02mr_f02_momentum_rotation_medmom_126d_31d_jerk_v019_signal,
    f02mr_f02_momentum_rotation_comom_21x126_31d_jerk_v020_signal,
    f02mr_f02_momentum_rotation_disp_roc_15d_jerk_v021_signal,
    f02mr_f02_momentum_rotation_paceconc_31d_jerk_v022_signal,
    f02mr_f02_momentum_rotation_pacerange_21d_jerk_v023_signal,
    f02mr_f02_momentum_rotation_bestpace_42d_jerk_v024_signal,
    f02mr_f02_momentum_rotation_worstpace_21d_jerk_v025_signal,
    f02mr_f02_momentum_rotation_dispshare_21d_jerk_v026_signal,
    f02mr_f02_momentum_rotation_pacecv_21d_jerk_v027_signal,
    f02mr_f02_momentum_rotation_pacespr_63v252_21d_jerk_v028_signal,
    f02mr_f02_momentum_rotation_pacespr_21v126_15d_jerk_v029_signal,
    f02mr_f02_momentum_rotation_pacespr_5v63_42d_jerk_v030_signal,
    f02mr_f02_momentum_rotation_pacespr_21v252_31d_jerk_v031_signal,
    f02mr_f02_momentum_rotation_termcurv_63_15d_jerk_v032_signal,
    f02mr_f02_momentum_rotation_curv_21d_8d_jerk_v033_signal,
    f02mr_f02_momentum_rotation_termmono_42d_jerk_v034_signal,
    f02mr_f02_momentum_rotation_momext_21d_jerk_v035_signal,
    f02mr_f02_momentum_rotation_accel_21h_31d_jerk_v036_signal,
    f02mr_f02_momentum_rotation_acceltanh_63d_15d_jerk_v037_signal,
    f02mr_f02_momentum_rotation_accelsm_126d_31d_jerk_v038_signal,
    f02mr_f02_momentum_rotation_accel_252d_42d_jerk_v039_signal,
    f02mr_f02_momentum_rotation_accelspr_21d_jerk_v040_signal,
    f02mr_f02_momentum_rotation_paceaccel_5d_8d_jerk_v041_signal,
    f02mr_f02_momentum_rotation_mom121accel_42d_jerk_v042_signal,
    f02mr_f02_momentum_rotation_accelratio_21d_8d_jerk_v043_signal,
    f02mr_f02_momentum_rotation_accelnorm_63d_15d_jerk_v044_signal,
    f02mr_f02_momentum_rotation_hit_21d_8d_jerk_v045_signal,
    f02mr_f02_momentum_rotation_mom32_63d_15d_jerk_v046_signal,
    f02mr_f02_momentum_rotation_hit_252d_42d_jerk_v047_signal,
    f02mr_f02_momentum_rotation_dispmidshort_31d_jerk_v048_signal,
    f02mr_f02_momentum_rotation_mom63_126d_26d_jerk_v049_signal,
    f02mr_f02_momentum_rotation_poscount_21d_jerk_v050_signal,
    f02mr_f02_momentum_rotation_align_31d_jerk_v051_signal,
    f02mr_f02_momentum_rotation_composite_42d_jerk_v052_signal,
    f02mr_f02_momentum_rotation_sqrtblend_15d_jerk_v053_signal,
    f02mr_f02_momentum_rotation_stackmag_21d_jerk_v054_signal,
    f02mr_f02_momentum_rotation_span_21d_jerk_v055_signal,
    f02mr_f02_momentum_rotation_paceskew_42d_jerk_v056_signal,
    f02mr_f02_momentum_rotation_conc_21v252_21d_jerk_v057_signal,
    f02mr_f02_momentum_rotation_frontload_42d_jerk_v058_signal,
    f02mr_f02_momentum_rotation_wkqratio_21d_jerk_v059_signal,
    f02mr_f02_momentum_rotation_balance_31d_jerk_v060_signal,
    f02mr_f02_momentum_rotation_rocpos_5d_8d_jerk_v061_signal,
    f02mr_f02_momentum_rotation_spikeshare_63d_21d_jerk_v062_signal,
    f02mr_f02_momentum_rotation_rocdisp_63d_42d_jerk_v063_signal,
    f02mr_f02_momentum_rotation_giveback_63d_15d_jerk_v064_signal,
    f02mr_f02_momentum_rotation_thrust_63d_42d_jerk_v065_signal,
    f02mr_f02_momentum_rotation_rocmid_252d_84d_jerk_v066_signal,
    f02mr_f02_momentum_rotation_pullback_21d_jerk_v067_signal,
    f02mr_f02_momentum_rotation_revsig_5v63_42d_jerk_v068_signal,
    f02mr_f02_momentum_rotation_skiprev_21d_jerk_v069_signal,
    f02mr_f02_momentum_rotation_paceratio_126v252_21d_jerk_v070_signal,
    f02mr_f02_momentum_rotation_lsagree_31d_jerk_v071_signal,
    f02mr_f02_momentum_rotation_pacegap_126v63_15d_jerk_v072_signal,
    f02mr_f02_momentum_rotation_fastdelta_252d_84d_jerk_v073_signal,
    f02mr_f02_momentum_rotation_momyoy_15d_jerk_v074_signal,
    f02mr_f02_momentum_rotation_termshift_21d_jerk_v075_signal,
    f02mr_f02_momentum_rotation_roc_10d_8d_jerk_v076_signal,
    f02mr_f02_momentum_rotation_roc_42d_21d_jerk_v077_signal,
    f02mr_f02_momentum_rotation_roc_189d_63d_jerk_v078_signal,
    f02mr_f02_momentum_rotation_mom126_252d_42d_jerk_v079_signal,
    f02mr_f02_momentum_rotation_rocpos_42d_15d_jerk_v080_signal,
    f02mr_f02_momentum_rotation_volmom_21d_5d_jerk_v081_signal,
    f02mr_f02_momentum_rotation_volmom_63d_15d_jerk_v082_signal,
    f02mr_f02_momentum_rotation_udvol_63d_21d_jerk_v083_signal,
    f02mr_f02_momentum_rotation_udvol_21d_13d_jerk_v084_signal,
    f02mr_f02_momentum_rotation_dvwret_63d_21d_jerk_v085_signal,
    f02mr_f02_momentum_rotation_voldiverg_21d_13d_jerk_v086_signal,
    f02mr_f02_momentum_rotation_volconf_252d_42d_jerk_v087_signal,
    f02mr_f02_momentum_rotation_dvthrust_15d_jerk_v088_signal,
    f02mr_f02_momentum_rotation_momperdv_42d_jerk_v089_signal,
    f02mr_f02_momentum_rotation_udvol_126d_42d_jerk_v090_signal,
    f02mr_f02_momentum_rotation_dispshort_42d_jerk_v091_signal,
    f02mr_f02_momentum_rotation_displong_15d_jerk_v092_signal,
    f02mr_f02_momentum_rotation_termcurv_126_21d_jerk_v093_signal,
    f02mr_f02_momentum_rotation_termcurv_10_31d_jerk_v094_signal,
    f02mr_f02_momentum_rotation_paceskewlong_31d_jerk_v095_signal,
    f02mr_f02_momentum_rotation_poscountlong_42d_jerk_v096_signal,
    f02mr_f02_momentum_rotation_spanlong_42d_jerk_v097_signal,
    f02mr_f02_momentum_rotation_shortdomin_21d_jerk_v098_signal,
    f02mr_f02_momentum_rotation_accel_42d_10d_jerk_v099_signal,
    f02mr_f02_momentum_rotation_acceltanh_126d_42d_jerk_v100_signal,
    f02mr_f02_momentum_rotation_jerk_21d_8d_jerk_v101_signal,
    f02mr_f02_momentum_rotation_jerk_42d_21d_jerk_v102_signal,
    f02mr_f02_momentum_rotation_mom121accel2_31d_jerk_v103_signal,
    f02mr_f02_momentum_rotation_accelsm_21d_8d_jerk_v104_signal,
    f02mr_f02_momentum_rotation_accelagree_21d_jerk_v105_signal,
    f02mr_f02_momentum_rotation_rocpos_21d_5d_jerk_v106_signal,
    f02mr_f02_momentum_rotation_rocpos_126d_31d_jerk_v107_signal,
    f02mr_f02_momentum_rotation_giveback_126d_26d_jerk_v108_signal,
    f02mr_f02_momentum_rotation_thrust_126d_42d_jerk_v109_signal,
    f02mr_f02_momentum_rotation_giveback_21d_13d_jerk_v110_signal,
    f02mr_f02_momentum_rotation_rocmid_126d_42d_jerk_v111_signal,
    f02mr_f02_momentum_rotation_signmag_5d_5d_jerk_v112_signal,
    f02mr_f02_momentum_rotation_signmag_42d_10d_jerk_v113_signal,
    f02mr_f02_momentum_rotation_absmag_21d_8d_jerk_v114_signal,
    f02mr_f02_momentum_rotation_absmag_126d_42d_jerk_v115_signal,
    f02mr_f02_momentum_rotation_sqrtblendlong_42d_jerk_v116_signal,
    f02mr_f02_momentum_rotation_complong_15d_jerk_v117_signal,
    f02mr_f02_momentum_rotation_dispmid_15d_jerk_v118_signal,
    f02mr_f02_momentum_rotation_tailasym_126d_26d_jerk_v119_signal,
    f02mr_f02_momentum_rotation_spikemom_63d_21d_jerk_v120_signal,
    f02mr_f02_momentum_rotation_extreme_21d_8d_jerk_v121_signal,
    f02mr_f02_momentum_rotation_medret_63d_42d_jerk_v122_signal,
    f02mr_f02_momentum_rotation_momskew_63d_31d_jerk_v123_signal,
    f02mr_f02_momentum_rotation_wmratio_42d_jerk_v124_signal,
    f02mr_f02_momentum_rotation_frontload_q_31d_jerk_v125_signal,
    f02mr_f02_momentum_rotation_conc_63v252_15d_jerk_v126_signal,
    f02mr_f02_momentum_rotation_lsagree_63v252_21d_jerk_v127_signal,
    f02mr_f02_momentum_rotation_stackmaglong_42d_jerk_v128_signal,
    f02mr_f02_momentum_rotation_balancelong_42d_jerk_v129_signal,
    f02mr_f02_momentum_rotation_pullback_long_42d_jerk_v130_signal,
    f02mr_f02_momentum_rotation_skiprev6_21d_jerk_v131_signal,
    f02mr_f02_momentum_rotation_momext_short_21d_jerk_v132_signal,
    f02mr_f02_momentum_rotation_rocdisp_21d_8d_jerk_v133_signal,
    f02mr_f02_momentum_rotation_rocdisp_126d_42d_jerk_v134_signal,
    f02mr_f02_momentum_rotation_mom41_84d_31d_jerk_v135_signal,
    f02mr_f02_momentum_rotation_momyoy_63d_31d_jerk_v136_signal,
    f02mr_f02_momentum_rotation_legpos_5d_3d_jerk_v137_signal,
    f02mr_f02_momentum_rotation_legpos_21d_13d_jerk_v138_signal,
    f02mr_f02_momentum_rotation_legpos_126d_26d_jerk_v139_signal,
    f02mr_f02_momentum_rotation_legpos_252d_63d_jerk_v140_signal,
    f02mr_f02_momentum_rotation_termshift_long_31d_jerk_v141_signal,
    f02mr_f02_momentum_rotation_rocmid_189d_31d_jerk_v142_signal,
    f02mr_f02_momentum_rotation_breadthex_126d_42d_jerk_v143_signal,
    f02mr_f02_momentum_rotation_exhaust_5v21_42d_jerk_v144_signal,
    f02mr_f02_momentum_rotation_relspan_31d_jerk_v145_signal,
    f02mr_f02_momentum_rotation_compaccel_21d_jerk_v146_signal,
    f02mr_f02_momentum_rotation_pacegap_42v126_15d_jerk_v147_signal,
    f02mr_f02_momentum_rotation_netup_21d_13d_jerk_v148_signal,
    f02mr_f02_momentum_rotation_volaccel_31d_jerk_v149_signal,
    f02mr_f02_momentum_rotation_composite2_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_MOMENTUM_ROTATION_REGISTRY_3RD_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f02_momentum_rotation_3rd_derivatives_001_150_claude: %d features pass" % n_features)
