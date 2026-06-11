import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (volatility REGIME: compression / expansion ONLY) =====
# NOTE: this family emits NO raw realized-vol LEVELS at single windows (those are f10)
# and NO raw high-low range / Parkinson / GK estimators (those are f11). Every primitive
# below is a RATIO / Z / RANK / STREAK / OCCUPANCY / DISPERSION regime mechanic.
def _f09_logret(close):
    return np.log(close.replace(0, np.nan) / close.shift(1).replace(0, np.nan))


def _f09_rvol(close, w):
    # internal building block ONLY (never emitted as a standalone level feature)
    r = np.log(close.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f09_bbw(close, w):
    # Bollinger bandwidth = 4*sigma / mean (upper-lower over mid) -- a width RATIO
    m = close.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(2, w // 2)).std()
    return (4.0 * sd) / m.replace(0, np.nan)


def _f09_pctb(close, w):
    # %B: position of price within its own Bollinger band (band-relative occupancy)
    m = close.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(2, w // 2)).std()
    upper = m + 2.0 * sd
    lower = m - 2.0 * sd
    return (close - lower) / (upper - lower).replace(0, np.nan)


def _f09_squeeze(close, w, lw):
    # squeeze = current bandwidth relative to its own min over lookback lw (>=1 => widest)
    bbw = _f09_bbw(close, w)
    lo = bbw.rolling(lw, min_periods=max(2, lw // 2)).min()
    return bbw / lo.replace(0, np.nan)


def _f09_volofvol(close, w, vw):
    rv = _f09_rvol(close, w)
    return rv.rolling(vw, min_periods=max(2, vw // 2)).std() / rv.rolling(
        vw, min_periods=max(2, vw // 2)).mean().replace(0, np.nan)


def _f09_compress_ratio(close, sw, lw):
    # short vol / long vol : <1 compression, >1 expansion (the core regime signal)
    return _f09_rvol(close, sw) / _f09_rvol(close, lw).replace(0, np.nan)


def _f09_contraction_streak(close, w):
    # consecutive days |ret| stays below its w-day median (vol contraction streak),
    # weighted by contraction depth so it is continuous (not a small-integer count).
    r = _f09_logret(close).abs()
    med = r.rolling(w, min_periods=max(2, w // 2)).median()
    cond = (r < med).astype(float)
    grp = (cond == 0).cumsum()
    streak = cond.groupby(grp).cumsum()
    depth = ((med - r) / med.replace(0, np.nan)).clip(lower=0)
    cumdepth = depth.where(cond == 1, 0.0).groupby(grp).cumsum()
    return streak + cumdepth


def _f09_expansion_streak(close, w):
    # consecutive days |ret| stays above its w-day median (vol expansion streak), depth-weighted
    r = _f09_logret(close).abs()
    med = r.rolling(w, min_periods=max(2, w // 2)).median()
    cond = (r > med).astype(float)
    grp = (cond == 0).cumsum()
    streak = cond.groupby(grp).cumsum()
    depth = ((r - med) / med.replace(0, np.nan)).clip(lower=0)
    cumdepth = depth.where(cond == 1, 0.0).groupby(grp).cumsum()
    return streak + cumdepth


def _f09_turbulence(close, w):
    # Mahalanobis-style turbulence: squared standardized return vs its own w-window moments
    r = _f09_logret(close)
    m = r.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = r.rolling(w, min_periods=max(2, w // 2)).std()
    z = (r - m) / sd.replace(0, np.nan)
    return (z * z).rolling(w, min_periods=max(2, w // 2)).mean()


# ==========================================================
# JERK FEATURES (2nd math derivative of a volatility-regime base)
# ==========================================================

def f09vr_f09_volatility_regime_bbwcompress_5v21_jerk_v001_signal(closeadj):  # jerk 21d of: bbwcompress_5v21
    b = _f09_bbw(closeadj, 5) / _f09_bbw(closeadj, 21).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwcompress_10v42_jerk_v002_signal(closeadj):  # jerk 21d of: bbwcompress_10v42
    b = _f09_bbw(closeadj, 10) / _f09_bbw(closeadj, 42).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compress_21v63_jerk_v003_signal(closeadj):  # jerk 21d of: compress_21v63
    b = _f09_compress_ratio(closeadj, 21, 63)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compress_10v252_jerk_v004_signal(closeadj):  # jerk 21d of: compress_10v252
    b = _f09_compress_ratio(closeadj, 10, 252)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwcompress_63v252_jerk_v005_signal(closeadj):  # jerk 63d of: bbwcompress_63v252
    b = _f09_bbw(closeadj, 63) / _f09_bbw(closeadj, 252).replace(0, np.nan)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compresslog_42v126_jerk_v006_signal(closeadj):  # jerk 21d of: compresslog_42v126
    r = _f09_compress_ratio(closeadj, 42, 126)
    b = np.log(r.replace(0, np.nan))
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressaccel_42v126_jerk_v007_signal(closeadj):  # jerk 21d of: compressaccel_42v126
    r = _f09_compress_ratio(closeadj, 42, 126)
    b = r - 2.0 * r.shift(21) + r.shift(42)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressvol_21v63_jerk_v008_signal(closeadj):  # jerk 21d of: compressvol_21v63
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r.rolling(63, min_periods=21).std()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compresschg_21v63_jerk_v009_signal(closeadj):  # jerk 21d of: compresschg_21v63
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r - r.shift(21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressrevert_21v63_jerk_v010_signal(closeadj):  # jerk 21d of: compressrevert_21v63
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r - r.ewm(span=63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressrank_10v63_jerk_v011_signal(closeadj):  # jerk 21d of: compressrank_10v63
    b = _rank(_f09_compress_ratio(closeadj, 10, 63), 252)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressmin_5v21_jerk_v012_signal(closeadj):  # jerk 21d of: compressmin_5v21
    r = _f09_compress_ratio(closeadj, 5, 21)
    b = r.rolling(63, min_periods=21).min()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compresspersist_21v63_jerk_v013_signal(closeadj):  # jerk 21d of: compresspersist_21v63
    r = _f09_compress_ratio(closeadj, 21, 63)
    comp = (r < 1.0).astype(float)
    b = comp.rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_expandpersist_21v63_jerk_v014_signal(closeadj):  # jerk 21d of: expandpersist_21v63
    r = _f09_compress_ratio(closeadj, 21, 63)
    exc = (r - 1.0).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressefficiency_21d_jerk_v015_signal(closeadj):  # jerk 21d of: compressefficiency_21d
    r = _f09_logret(closeadj)
    net = r.rolling(21, min_periods=10).sum().abs()
    gross = r.abs().rolling(21, min_periods=10).sum()
    b = net / gross.replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwz_21v126_jerk_v016_signal(closeadj):  # jerk 21d of: bbwz_21v126
    b = _z(_f09_bbw(closeadj, 21), 126)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwz_63v252_jerk_v017_signal(closeadj):  # jerk 63d of: bbwz_63v252
    b = _z(_f09_bbw(closeadj, 63), 252)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwrank_21v252_jerk_v018_signal(closeadj):  # jerk 21d of: bbwrank_21v252
    b = _rank(_f09_bbw(closeadj, 21), 252)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwrank_63v504_jerk_v019_signal(closeadj):  # jerk 63d of: bbwrank_63v504
    b = _rank(_f09_bbw(closeadj, 63), 504)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwratio_21v63_jerk_v020_signal(closeadj):  # jerk 21d of: bbwratio_21v63
    b = _f09_bbw(closeadj, 21) / _f09_bbw(closeadj, 63).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwratio_21v126_jerk_v021_signal(closeadj):  # jerk 21d of: bbwratio_21v126
    b = _f09_bbw(closeadj, 21) / _f09_bbw(closeadj, 126).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwspread_21v126_jerk_v022_signal(closeadj):  # jerk 21d of: bbwspread_21v126
    b = _f09_bbw(closeadj, 21) - _f09_bbw(closeadj, 126)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwchg_21d_jerk_v023_signal(closeadj):  # jerk 21d of: bbwchg_21d
    bb = _f09_bbw(closeadj, 21)
    b = bb - bb.shift(21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwdisp_21d_jerk_v024_signal(closeadj):  # jerk 21d of: bbwdisp_21d
    bb = _f09_bbw(closeadj, 21)
    b = bb.rolling(63, min_periods=21).std()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwlog_126d_jerk_v025_signal(closeadj):  # jerk 63d of: bbwlog_126d
    bb = _f09_bbw(closeadj, 126)
    b = np.log(bb.replace(0, np.nan)) - np.log(_mean(bb, 504).replace(0, np.nan))
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwskew_21d_jerk_v026_signal(closeadj):  # jerk 21d of: bbwskew_21d
    bb = _f09_bbw(closeadj, 21)
    med = bb.rolling(63, min_periods=21).median()
    d = (bb - med) / med.replace(0, np.nan)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwmaxratio_21d_jerk_v027_signal(closeadj):  # jerk 21d of: bbwmaxratio_21d
    bb = _f09_bbw(closeadj, 21)
    b = bb / bb.rolling(63, min_periods=21).max().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwyoy_21d_jerk_v028_signal(closeadj):  # jerk 21d of: bbwyoy_21d
    bb = _f09_bbw(closeadj, 21)
    b = bb / bb.shift(252).replace(0, np.nan) - 1.0
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeeze_21v126_jerk_v029_signal(closeadj):  # jerk 21d of: squeeze_21v126
    b = _f09_squeeze(closeadj, 21, 126)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeeze_63v252_jerk_v030_signal(closeadj):  # jerk 63d of: squeeze_63v252
    b = _f09_squeeze(closeadj, 63, 252)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeeze_126v504_jerk_v031_signal(closeadj):  # jerk 63d of: squeeze_126v504
    b = _f09_squeeze(closeadj, 126, 504)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezelog_42d_jerk_v032_signal(closeadj):  # jerk 21d of: squeezelog_42d
    s = _f09_squeeze(closeadj, 42, 189)
    b = np.log(s.replace(0, np.nan))
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezeon_21d_jerk_v033_signal(closeadj):  # jerk 21d of: squeezeon_21d
    bb = _f09_bbw(closeadj, 21)
    lo = bb.rolling(126, min_periods=63).min()
    b = (lo / bb.replace(0, np.nan)).clip(upper=1.0)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezetime_21d_jerk_v034_signal(closeadj):  # jerk 21d of: squeezetime_21d
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    insq = (rk <= 0.25).astype(float)
    b = insq.rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezetime_63d_jerk_v035_signal(closeadj):  # jerk 63d of: squeezetime_63d
    bb = _f09_bbw(closeadj, 63)
    rk = bb.rolling(252, min_periods=84).rank(pct=True)
    insq = (rk <= 0.25).astype(float)
    b = insq.rolling(126, min_periods=42).mean()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezeaccel_21d_jerk_v036_signal(closeadj):  # jerk 21d of: squeezeaccel_21d
    sq = _f09_squeeze(closeadj, 21, 126)
    b = sq - sq.shift(10)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezerelease_21d_jerk_v037_signal(closeadj):  # jerk 21d of: squeezerelease_21d
    bb = _f09_bbw(closeadj, 21)
    floor = bb.rolling(63, min_periods=21).min().shift(21)
    b = bb / floor.replace(0, np.nan) - 1.0
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_brkoutsq_21d_jerk_v038_signal(closeadj):  # jerk 21d of: brkoutsq_21d
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    prior_sq = (1.0 - rk.shift(21)).clip(lower=0)
    expand = (bb / bb.shift(21).replace(0, np.nan) - 1.0).clip(lower=0)
    b = prior_sq * expand
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_brkoutsq_63d_jerk_v039_signal(closeadj):  # jerk 63d of: brkoutsq_63d
    bb = _f09_bbw(closeadj, 63)
    rk = bb.rolling(504, min_periods=126).rank(pct=True)
    prior_sq = (1.0 - rk.shift(63)).clip(lower=0)
    expand = (bb / bb.shift(63).replace(0, np.nan) - 1.0).clip(lower=0)
    b = prior_sq * expand
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_brkoutcompress_21d_jerk_v040_signal(closeadj):  # jerk 21d of: brkoutcompress_21d
    r = _f09_compress_ratio(closeadj, 21, 63)
    rk = r.rolling(252, min_periods=63).rank(pct=True)
    prior_low = (1.0 - rk.shift(21)).clip(lower=0)
    jump = (r / r.shift(21).replace(0, np.nan) - 1.0).clip(lower=0)
    b = prior_low * jump
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_pctb_21d_jerk_v041_signal(closeadj):  # jerk 21d of: pctb_21d
    b = _f09_pctb(closeadj, 21) - 0.5
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_pctb_63d_jerk_v042_signal(closeadj):  # jerk 63d of: pctb_63d
    b = _f09_pctb(closeadj, 63) - 0.5
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_pctbabs_21d_jerk_v043_signal(closeadj):  # jerk 21d of: pctbabs_21d
    pb = (_f09_pctb(closeadj, 21) - 0.5).abs()
    b = pb.ewm(span=21, min_periods=10).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_pctbpersist_21d_jerk_v044_signal(closeadj):  # jerk 21d of: pctbpersist_21d
    pb = _f09_pctb(closeadj, 21)
    b = pb.rolling(63, min_periods=21).corr(pb.shift(1))
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwofbbw_21v63_jerk_v045_signal(closeadj):  # jerk 21d of: bbwofbbw_21v63
    bb = _f09_bbw(closeadj, 21)
    b = bb.rolling(63, min_periods=21).std() / bb.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwofbbw_21v126_jerk_v046_signal(closeadj):  # jerk 21d of: bbwofbbw_21v126
    bb = _f09_bbw(closeadj, 21)
    b = bb.rolling(126, min_periods=42).std() / bb.rolling(126, min_periods=42).mean().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezeofsqueeze_21d_jerk_v047_signal(closeadj):  # jerk 21d of: squeezeofsqueeze_21d
    sq = _f09_squeeze(closeadj, 21, 126)
    b = sq.rolling(63, min_periods=21).std()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volofvoliqr_21d_jerk_v048_signal(closeadj):  # jerk 21d of: volofvoliqr_21d
    rv = _f09_rvol(closeadj, 21)
    q3 = rv.rolling(126, min_periods=42).quantile(0.75)
    q1 = rv.rolling(126, min_periods=42).quantile(0.25)
    med = rv.rolling(126, min_periods=42).median()
    b = (q3 - q1) / med.replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwofbbwmom_21d_jerk_v049_signal(closeadj):  # jerk 21d of: bbwofbbwmom_21d
    bb = _f09_bbw(closeadj, 21)
    bov = bb.rolling(63, min_periods=21).std() / bb.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = bov - bov.shift(21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_pctbrange_21d_jerk_v050_signal(closeadj):  # jerk 21d of: pctbrange_21d
    pb = _f09_pctb(closeadj, 21)
    b = pb.rolling(63, min_periods=21).max() - pb.rolling(63, min_periods=21).min()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rvolz_21v126_jerk_v051_signal(closeadj):  # jerk 21d of: rvolz_21v126
    b = _z(_f09_rvol(closeadj, 21), 126)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rvolz_63v252_jerk_v052_signal(closeadj):  # jerk 63d of: rvolz_63v252
    b = _z(_f09_rvol(closeadj, 63), 252)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwrank_42v252_jerk_v053_signal(closeadj):  # jerk 21d of: bbwrank_42v252
    b = _rank(_f09_bbw(closeadj, 42), 252)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rvolrank_63v504_jerk_v054_signal(closeadj):  # jerk 63d of: rvolrank_63v504
    b = _rank(_f09_rvol(closeadj, 63), 504)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezedwell_21d_jerk_v055_signal(closeadj):  # jerk 21d of: squeezedwell_21d
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    insq = (rk <= 0.3333).astype(float)
    grp = (insq == 0).cumsum()
    dwell = insq.groupby(grp).cumsum()
    b = dwell * (1.0 + (0.3333 - rk).clip(lower=0))
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volcone_21d_jerk_v056_signal(closeadj):  # jerk 21d of: volcone_21d
    rv = _f09_rvol(closeadj, 21)
    lo = rv.rolling(252, min_periods=63).min()
    hi = rv.rolling(252, min_periods=63).max()
    pos = (rv - lo) / (hi - lo).replace(0, np.nan) - 0.5
    b = np.sign(pos) * pos * pos
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volconedist_63d_jerk_v057_signal(closeadj):  # jerk 63d of: volconedist_63d
    rv = _f09_rvol(closeadj, 63)
    lo = rv.rolling(504, min_periods=126).min()
    hi = rv.rolling(504, min_periods=126).max()
    pos = (rv - lo) / (hi - lo).replace(0, np.nan)
    b = (pos - 0.5).abs()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_voldrawup_126d_jerk_v058_signal(closeadj):  # jerk 63d of: voldrawup_126d
    rv = _f09_rvol(closeadj, 126)
    b = rv / rv.rolling(504, min_periods=126).min().replace(0, np.nan) - 1.0
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volminratio_21d_jerk_v059_signal(closeadj):  # jerk 21d of: volminratio_21d
    rv = _f09_rvol(closeadj, 21)
    ratio = rv / rv.rolling(252, min_periods=63).min().replace(0, np.nan)
    turn = np.tanh(50.0 * (rv - rv.shift(10)))
    b = ratio * turn
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_contractstreak_21d_jerk_v060_signal(closeadj):  # jerk 21d of: contractstreak_21d
    b = _f09_contraction_streak(closeadj, 21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_contractstreak_63d_jerk_v061_signal(closeadj):  # jerk 63d of: contractstreak_63d
    b = _f09_contraction_streak(closeadj, 63)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_expandstreak_21d_jerk_v062_signal(closeadj):  # jerk 21d of: expandstreak_21d
    b = _f09_expansion_streak(closeadj, 21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwtermconvex_63d_jerk_v063_signal(closeadj):  # jerk 63d of: bbwtermconvex_63d
    r_short = _f09_bbw(closeadj, 21) / _f09_bbw(closeadj, 63).replace(0, np.nan)
    r_long = _f09_bbw(closeadj, 63) / _f09_bbw(closeadj, 252).replace(0, np.nan)
    b = r_short - r_long
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volcurv_norm_84d_jerk_v064_signal(closeadj):  # jerk 63d of: volcurv_norm_84d
    c = _f09_rvol(closeadj, 42) - 2.0 * _f09_rvol(closeadj, 84) + _f09_rvol(closeadj, 168)
    b = c / _f09_rvol(closeadj, 84).replace(0, np.nan)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_regimedivg_63d_jerk_v065_signal(closeadj):  # jerk 63d of: regimedivg_63d
    rv21 = _f09_rvol(closeadj, 21)
    rv63 = _f09_rvol(closeadj, 63)
    d21 = (rv21 - rv21.rolling(252, min_periods=63).median()) / rv21.rolling(252, min_periods=63).std().replace(0, np.nan)
    d63 = (rv63 - rv63.rolling(252, min_periods=63).median()) / rv63.rolling(252, min_periods=63).std().replace(0, np.nan)
    b = d21 - d63
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_turbulence_21d_jerk_v066_signal(closeadj):  # jerk 21d of: turbulence_21d
    b = _f09_turbulence(closeadj, 21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_turbulence_63d_jerk_v067_signal(closeadj):  # jerk 63d of: turbulence_63d
    b = _f09_turbulence(closeadj, 63)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_turbratio_21v63_jerk_v068_signal(closeadj):  # jerk 21d of: turbratio_21v63
    b = _f09_turbulence(closeadj, 21) / _f09_turbulence(closeadj, 63).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volpersist_21d_jerk_v069_signal(closeadj):  # jerk 21d of: volpersist_21d
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(63, min_periods=21).corr(rv.shift(1))
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rvolema_disp_21d_jerk_v070_signal(closeadj):  # jerk 21d of: rvolema_disp_21d
    rv = _f09_rvol(closeadj, 21)
    b = (rv.ewm(span=21, min_periods=10).mean() - rv.ewm(span=63, min_periods=21).mean()) / _f09_rvol(closeadj, 63).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bandpierce_21d_jerk_v071_signal(closeadj):  # jerk 21d of: bandpierce_21d
    pb = _f09_pctb(closeadj, 21)
    pierce = (pb - pb.clip(0.0, 1.0)).abs()
    b = pierce.rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bandpierce_63d_jerk_v072_signal(closeadj):  # jerk 63d of: bandpierce_63d
    pb = _f09_pctb(closeadj, 63)
    pierce = (pb - pb.clip(0.0, 1.0)).abs()
    b = pierce.rolling(63, min_periods=21).mean()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compresszone_21v63_jerk_v073_signal(closeadj):  # jerk 21d of: compresszone_21v63
    r = _f09_compress_ratio(closeadj, 21, 63)
    comp = (0.8 - r).clip(lower=0)
    exp = (r - 1.2).clip(lower=0)
    b = exp - comp
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezeheat_21d_jerk_v074_signal(closeadj):  # jerk 21d of: squeezeheat_21d
    bb = _f09_bbw(closeadj, 21)
    atlow = (bb <= bb.rolling(126, min_periods=63).min() * 1.0001).astype(float)
    grp = atlow.cumsum()
    since = atlow.groupby(grp).cumcount().astype(float)
    b = since / 126.0
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volratioema_21v63_jerk_v075_signal(closeadj):  # jerk 21d of: volratioema_21v63
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r.ewm(span=21, min_periods=10).mean() - 1.0
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwcompress_42v252_jerk_v076_signal(closeadj):  # jerk 63d of: bbwcompress_42v252
    b = _f09_bbw(closeadj, 42) / _f09_bbw(closeadj, 252).replace(0, np.nan)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwcompress_21v189_jerk_v077_signal(closeadj):  # jerk 21d of: bbwcompress_21v189
    b = _f09_bbw(closeadj, 21) / _f09_bbw(closeadj, 189).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compresslog_10v63_jerk_v078_signal(closeadj):  # jerk 21d of: compresslog_10v63
    r = _f09_compress_ratio(closeadj, 10, 63)
    b = np.log(r.replace(0, np.nan))
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressratiochg_63d_jerk_v079_signal(closeadj):  # jerk 63d of: compressratiochg_63d
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r - r.shift(63)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressdispersion_21d_jerk_v080_signal(closeadj):  # jerk 21d of: compressdispersion_21d
    r1 = _f09_compress_ratio(closeadj, 5, 21)
    r2 = _f09_compress_ratio(closeadj, 5, 63)
    r3 = _f09_compress_ratio(closeadj, 21, 63)
    b = pd.concat([r1, r2, r3], axis=1).std(axis=1)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressbreadth_21d_jerk_v081_signal(closeadj):  # jerk 21d of: compressbreadth_21d
    lv = _f09_rvol(closeadj, 63)
    s1 = np.log(lv.replace(0, np.nan) / _f09_rvol(closeadj, 5).replace(0, np.nan))
    s2 = np.log(lv.replace(0, np.nan) / _f09_rvol(closeadj, 10).replace(0, np.nan))
    s3 = np.log(lv.replace(0, np.nan) / _f09_rvol(closeadj, 21).replace(0, np.nan))
    b = (s1 + s2 + s3) / 3.0
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressexpcycle_126d_jerk_v082_signal(closeadj):  # jerk 63d of: compressexpcycle_126d
    r = _f09_compress_ratio(closeadj, 42, 126)
    lo = r.rolling(126, min_periods=42).min()
    hi = r.rolling(126, min_periods=42).max()
    mid = (hi + lo) / 2.0
    b = (r - mid) / (hi - lo).replace(0, np.nan)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_compressratiovol_42v126_jerk_v083_signal(closeadj):  # jerk 21d of: compressratiovol_42v126
    r = _f09_compress_ratio(closeadj, 42, 126)
    b = r.rolling(42, min_periods=21).std()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwspreadz_21v63_jerk_v084_signal(closeadj):  # jerk 21d of: bbwspreadz_21v63
    sb = _f09_bbw(closeadj, 21)
    lb = _f09_bbw(closeadj, 63)
    b = (lb - sb) / sb.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volspreadrank_42v126_jerk_v085_signal(closeadj):  # jerk 21d of: volspreadrank_42v126
    lv = _f09_rvol(closeadj, 126)
    sp = (lv - _f09_rvol(closeadj, 42)) / lv.replace(0, np.nan)
    b = _rank(sp, 252)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volcurv_norm_42d_jerk_v086_signal(closeadj):  # jerk 21d of: volcurv_norm_42d
    c = _f09_rvol(closeadj, 21) - 2.0 * _f09_rvol(closeadj, 42) + _f09_rvol(closeadj, 63)
    b = c / _f09_rvol(closeadj, 42).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bandtouchskew_21d_jerk_v087_signal(closeadj):  # jerk 21d of: bandtouchskew_21d
    pb = _f09_pctb(closeadj, 21)
    up = (pb > 0.8).astype(float)
    dn = (pb < 0.2).astype(float)
    b = (up - dn).rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bandtouchskew_63d_jerk_v088_signal(closeadj):  # jerk 63d of: bandtouchskew_63d
    pb = _f09_pctb(closeadj, 63)
    up = (pb > 0.8).astype(float)
    dn = (pb < 0.2).astype(float)
    b = (up - dn).rolling(63, min_periods=21).mean()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_semivolconvex_126d_jerk_v089_signal(closeadj):  # jerk 63d of: semivolconvex_126d
    r = _f09_logret(closeadj)
    dn = np.sqrt((r.where(r < 0, 0.0) ** 2).rolling(126, min_periods=42).mean())
    up = np.sqrt((r.where(r > 0, 0.0) ** 2).rolling(126, min_periods=42).mean())
    ratio = dn / up.replace(0, np.nan)
    b = np.log(ratio.replace(0, np.nan)) - np.log(ratio.replace(0, np.nan)).ewm(span=252, min_periods=84).mean()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_semiskewchg_21d_jerk_v090_signal(closeadj):  # jerk 21d of: semiskewchg_21d
    r = _f09_logret(closeadj)
    dn = np.sqrt((r.where(r < 0, 0.0) ** 2).rolling(21, min_periods=10).mean())
    up = np.sqrt((r.where(r > 0, 0.0) ** 2).rolling(21, min_periods=10).mean())
    sk = (dn - up) / (dn + up).replace(0, np.nan)
    b = sk - sk.shift(21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volkurtz_63d_jerk_v091_signal(closeadj):  # jerk 63d of: volkurtz_63d
    r = _f09_logret(closeadj)
    k = r.rolling(63, min_periods=21).kurt()
    b = _z(k, 252)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_retskewz_63d_jerk_v092_signal(closeadj):  # jerk 63d of: retskewz_63d
    r = _f09_logret(closeadj)
    sk = r.rolling(63, min_periods=21).skew()
    b = _z(sk, 252)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bandexpandenergy_63d_jerk_v093_signal(closeadj):  # jerk 63d of: bandexpandenergy_63d
    bb = _f09_bbw(closeadj, 21)
    m = bb.rolling(63, min_periods=21).mean()
    sd = bb.rolling(63, min_periods=21).std()
    exc = ((bb - (m + 2.0 * sd)) / m.replace(0, np.nan)).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_gapvol_21d_jerk_v094_signal(closeadj):  # jerk 21d of: gapvol_21d
    r = _f09_logret(closeadj).abs()
    b = r.rolling(21, min_periods=10).max() / r.rolling(21, min_periods=10).median().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwz_5v63_jerk_v095_signal(closeadj):  # jerk 21d of: bbwz_5v63
    b = _z(_f09_bbw(closeadj, 5), 63)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwz_252v504_jerk_v096_signal(closeadj):  # jerk 63d of: bbwz_252v504
    b = _z(_f09_bbw(closeadj, 252), 504)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwstate_63d_jerk_v097_signal(closeadj):  # jerk 63d of: bbwstate_63d
    bb = _f09_bbw(closeadj, 63)
    b = bb / bb.shift(126).replace(0, np.nan) - 1.0
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwexpandstate_21d_jerk_v098_signal(closeadj):  # jerk 21d of: bbwexpandstate_21d
    bb = _f09_bbw(closeadj, 21)
    m = bb.rolling(63, min_periods=21).mean()
    exc = ((bb - m) / m.replace(0, np.nan)).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwmin_ratio_21d_jerk_v099_signal(closeadj):  # jerk 21d of: bbwmin_ratio_21d
    bb = _f09_bbw(closeadj, 21)
    b = bb.rolling(63, min_periods=21).min() / bb.replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwacceldir_21d_jerk_v100_signal(closeadj):  # jerk 21d of: bbwacceldir_21d
    bb = _f09_bbw(closeadj, 21)
    a = bb.diff(21).diff(21)
    b = np.sign(a) * (a.abs() ** 0.5)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezecount_21d_jerk_v101_signal(closeadj):  # jerk 21d of: squeezecount_21d
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    insq = (rk <= 0.25).astype(float)
    entry = ((insq == 1) & (insq.shift(1) == 0)).astype(float)
    weighted = entry * (0.25 - rk).clip(lower=0)
    b = entry.rolling(252, min_periods=63).sum() + 50.0 * weighted.rolling(252, min_periods=63).sum()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_expandcount_21d_jerk_v102_signal(closeadj):  # jerk 21d of: expandcount_21d
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    exp = (rk >= 0.75).astype(float)
    entry = ((exp == 1) & (exp.shift(1) == 0)).astype(float)
    weighted = entry * (rk - 0.75).clip(lower=0)
    b = entry.rolling(252, min_periods=63).sum() + 50.0 * weighted.rolling(252, min_periods=63).sum()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_doublesqueeze_21d_jerk_v103_signal(closeadj):  # jerk 21d of: doublesqueeze_21d
    vr = _f09_rvol(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    br = _f09_bbw(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    b = (1.0 - vr) * (1.0 - br)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_preexpcompress_21d_jerk_v104_signal(closeadj):  # jerk 21d of: preexpcompress_21d
    br = 1.0 - _f09_bbw(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    vov = _f09_volofvol(closeadj, 21, 63)
    vovchg = (vov - vov.shift(21)).clip(lower=0)
    b = br * vovchg
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezefirepower_21d_jerk_v105_signal(closeadj):  # jerk 21d of: squeezefirepower_21d
    bb = _f09_bbw(closeadj, 21)
    med = bb.rolling(252, min_periods=63).median()
    depth = ((med - bb) / med.replace(0, np.nan)).clip(lower=0)
    b = depth * _f09_volofvol(closeadj, 21, 63)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_coiledspring_21d_jerk_v106_signal(closeadj):  # jerk 21d of: coiledspring_21d
    streak = _f09_contraction_streak(closeadj, 21)
    rv = _f09_rvol(closeadj, 21)
    rk = rv.rolling(252, min_periods=63).rank(pct=True)
    b = streak * (1.0 - rk)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezeexpcombo_21d_jerk_v107_signal(closeadj):  # jerk 21d of: squeezeexpcombo_21d
    sq = np.log(_f09_squeeze(closeadj, 21, 126).replace(0, np.nan))
    cm = np.log(_f09_compress_ratio(closeadj, 21, 63).replace(0, np.nan))
    b = sq - cm
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_squeezethenexp_21d_jerk_v108_signal(closeadj):  # jerk 21d of: squeezethenexp_21d
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    prior_sq = (1.0 - rk.shift(21)).clip(lower=0)
    r = _f09_compress_ratio(closeadj, 5, 21)
    burst = (r - 1.0).clip(lower=0)
    b = prior_sq * burst
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volaccel_63d_jerk_v109_signal(closeadj):  # jerk 63d of: volaccel_63d
    rv = _f09_rvol(closeadj, 63)
    b = (rv - rv.shift(63)) / rv.shift(63).replace(0, np.nan)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_voltrendsign_21d_jerk_v110_signal(closeadj):  # jerk 21d of: voltrendsign_21d
    rv = _f09_rvol(closeadj, 21)
    chg = rv - rv.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volmomratio_21d_jerk_v111_signal(closeadj):  # jerk 21d of: volmomratio_21d
    rv = _f09_rvol(closeadj, 21)
    ratio = rv / rv.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    b = ratio - ratio.shift(10)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volshockgap_5d_jerk_v112_signal(closeadj):  # jerk 21d of: volshockgap_5d
    sv = _f09_rvol(closeadj, 5)
    mv = _f09_rvol(closeadj, 21)
    vov = mv.rolling(63, min_periods=21).std()
    b = (sv - mv) / vov.replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volcontract_pressure_21d_jerk_v113_signal(closeadj):  # jerk 21d of: volcontract_pressure_21d
    rv = _f09_rvol(closeadj, 21)
    dn = (-rv.diff()).clip(lower=0) / rv.shift(1).replace(0, np.nan)
    b = dn.rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volexpburst_21d_jerk_v114_signal(closeadj):  # jerk 21d of: volexpburst_21d
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(63, min_periods=21).max() / rv.rolling(63, min_periods=21).median().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volregimebin_21d_jerk_v115_signal(closeadj):  # jerk 21d of: volregimebin_21d
    rv = _f09_rvol(closeadj, 21)
    above = ((rv > _f09_rvol(closeadj, 63)).astype(float) + (rv > _f09_rvol(closeadj, 126)).astype(float) + (rv > _f09_rvol(closeadj, 252)).astype(float)) - 1.5
    dev = (rv - _f09_rvol(closeadj, 126)) / _f09_rvol(closeadj, 126).replace(0, np.nan)
    b = above + np.tanh(2.0 * dev)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volregimedwell_21d_jerk_v116_signal(closeadj):  # jerk 21d of: volregimedwell_21d
    rk = _f09_rvol(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    terc = np.floor(rk.clip(0, 0.999) * 3.0)
    same = (terc == terc.shift(1)).astype(float)
    grp = (same == 0).cumsum()
    dwell = same.groupby(grp).cumsum()
    b = dwell * (1.0 + (rk - 0.5).abs())
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volentropy_63d_jerk_v117_signal(closeadj):  # jerk 63d of: volentropy_63d
    rk = _f09_rvol(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    b = rk.rolling(63, min_periods=21).max() - rk.rolling(63, min_periods=21).min()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volzdispersion_21d_jerk_v118_signal(closeadj):  # jerk 21d of: volzdispersion_21d
    z1 = _z(_f09_rvol(closeadj, 21), 126)
    z2 = _z(_f09_rvol(closeadj, 63), 252)
    z3 = _z(_f09_rvol(closeadj, 126), 504)
    b = pd.concat([z1, z2, z3], axis=1).std(axis=1)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_calmratio_63d_jerk_v119_signal(closeadj):  # jerk 63d of: calmratio_63d
    r = _f09_logret(closeadj).abs()
    med = r.rolling(63, min_periods=21).median()
    calm = ((med - r) / med.replace(0, np.nan)).clip(lower=0)
    b = calm.rolling(63, min_periods=21).mean()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bbwvolofvol_21d_jerk_v120_signal(closeadj):  # jerk 21d of: bbwvolofvol_21d
    b = _z(_f09_bbw(closeadj, 21), 252) * _z(_f09_volofvol(closeadj, 21, 63), 252)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volwhipsaw_63d_jerk_v121_signal(closeadj):  # jerk 63d of: volwhipsaw_63d
    rv = _f09_rvol(closeadj, 21)
    jag = rv.diff().diff().abs() / rv.replace(0, np.nan)
    b = jag.rolling(63, min_periods=21).sum()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volhalflife_63d_jerk_v122_signal(closeadj):  # jerk 63d of: volhalflife_63d
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(63, min_periods=21).corr(rv.shift(21))
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_pctbdisp_21d_jerk_v123_signal(closeadj):  # jerk 21d of: pctbdisp_21d
    pb = _f09_pctb(closeadj, 21)
    b = pb.rolling(63, min_periods=21).std()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_pctbtrend_21d_jerk_v124_signal(closeadj):  # jerk 21d of: pctbtrend_21d
    pb = _f09_pctb(closeadj, 21) - 0.5
    b = pb - pb.shift(21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_bandwalk_21d_jerk_v125_signal(closeadj):  # jerk 21d of: bandwalk_21d
    pb = _f09_pctb(closeadj, 21)
    edge = ((pb > 0.8) | (pb < 0.2)).astype(float)
    b = edge.rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_turbchg_21d_jerk_v126_signal(closeadj):  # jerk 21d of: turbchg_21d
    t = _f09_turbulence(closeadj, 21)
    b = t - t.shift(21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_turbpersist_63d_jerk_v127_signal(closeadj):  # jerk 63d of: turbpersist_63d
    t = _f09_turbulence(closeadj, 21)
    med = t.rolling(252, min_periods=63).median()
    hot = (t > med).astype(float)
    b = hot.rolling(63, min_periods=21).mean()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_volregimecurv_126d_jerk_v128_signal(closeadj):  # jerk 63d of: volregimecurv_126d
    rv = _f09_rvol(closeadj, 126)
    c = rv - 2.0 * rv.shift(63) + rv.shift(126)
    b = c / rv.replace(0, np.nan)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rvolratiorange_42v126_jerk_v129_signal(closeadj):  # jerk 21d of: rvolratiorange_42v126
    r = _f09_rvol(closeadj, 42) / _f09_rvol(closeadj, 126).replace(0, np.nan)
    b = r.rolling(63, min_periods=21).max() - r.rolling(63, min_periods=21).min()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rvolzfast_10d_jerk_v130_signal(closeadj):  # jerk 21d of: rvolzfast_10d
    b = _z(_f09_rvol(closeadj, 10), 63)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rvolz_42v252_jerk_v131_signal(closeadj):  # jerk 21d of: rvolz_42v252
    b = _z(_f09_rvol(closeadj, 42), 252)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_turbpersist_clust_21d_jerk_v132_signal(closeadj):  # jerk 21d of: turbpersist_clust_21d
    t = _f09_turbulence(closeadj, 21)
    b = t.rolling(63, min_periods=21).corr(t.shift(1))
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_expandonset_21d_jerk_v133_signal(closeadj):  # jerk 21d of: expandonset_21d
    r = _f09_compress_ratio(closeadj, 21, 63)
    rk = r.rolling(252, min_periods=63).rank(pct=True)
    cross = ((r > 1.0) & (r.shift(1) <= 1.0)).astype(float)
    wt = (1.0 - rk.shift(1)).clip(lower=0)
    b = (cross * wt).rolling(63, min_periods=21).sum()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_contractdepth_63d_jerk_v134_signal(closeadj):  # jerk 63d of: contractdepth_63d
    rv = _f09_rvol(closeadj, 21)
    med = rv.rolling(63, min_periods=21).median()
    sf = ((med - rv) / med.replace(0, np.nan)).clip(lower=0)
    b = sf.rolling(63, min_periods=21).mean()
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_intraover_ratio_21d_jerk_v135_signal(high, low, closeadj):  # jerk 21d of: intraover_ratio_21d
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = rng / _f09_rvol(closeadj, 21).replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_intraover_compress_21d_jerk_v136_signal(high, low, closeadj):  # jerk 21d of: intraover_compress_21d
    ratio = ((high - low) / closeadj.replace(0, np.nan)) / _f09_logret(closeadj).abs().replace(0, np.nan)
    ratio = ratio.replace([np.inf, -np.inf], np.nan)
    sm = ratio.rolling(21, min_periods=10).mean()
    b = sm / ratio.rolling(126, min_periods=42).mean().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangecompress_21v63_jerk_v137_signal(high, low, closeadj):  # jerk 21d of: rangecompress_21v63
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = rng.rolling(21, min_periods=10).mean() / rng.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangecompress_42v126_jerk_v138_signal(high, low, closeadj):  # jerk 21d of: rangecompress_42v126
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = rng.rolling(42, min_periods=21).mean() / rng.rolling(126, min_periods=42).mean().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangeexpand_21d_jerk_v139_signal(high, low, closeadj):  # jerk 21d of: rangeexpand_21d
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = rng / rng.rolling(21, min_periods=10).mean().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangecone_21d_jerk_v140_signal(high, low, closeadj):  # jerk 21d of: rangecone_21d
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    floor = rng.rolling(126, min_periods=42).min().shift(63)
    b = rng / floor.replace(0, np.nan) - 1.0
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangecontractmag_21d_jerk_v141_signal(high, low, closeadj):  # jerk 21d of: rangecontractmag_21d
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    peak = rng.rolling(63, min_periods=21).max()
    b = np.log(rng.replace(0, np.nan) / peak.replace(0, np.nan))
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangecontractpct_21d_jerk_v142_signal(high, low, closeadj):  # jerk 21d of: rangecontractpct_21d
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    lo = rng.rolling(126, min_periods=42).min()
    hi = rng.rolling(126, min_periods=42).max()
    b = (rng - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_nrbarcount_21d_jerk_v143_signal(high, low, closeadj):  # jerk 21d of: nrbarcount_21d
    rng = (high - low) / closeadj.replace(0, np.nan)
    isnr = (rng <= rng.rolling(7, min_periods=4).min() * 1.0001).astype(float)
    depth = (rng.rolling(7, min_periods=4).mean() - rng).clip(lower=0)
    b = (isnr * (1.0 + 20.0 * depth)).rolling(21, min_periods=10).sum()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangeexpandstreak_21d_jerk_v144_signal(high, low, closeadj):  # jerk 21d of: rangeexpandstreak_21d
    rng = (high - low) / closeadj.replace(0, np.nan)
    med = rng.rolling(21, min_periods=10).median()
    cond = (rng > med).astype(float)
    grp = (cond == 0).cumsum()
    streak = cond.groupby(grp).cumsum()
    depth = ((rng - med) / med.replace(0, np.nan)).clip(lower=0)
    cumd = depth.where(cond == 1, 0.0).groupby(grp).cumsum()
    b = streak + cumd
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangecontractstreak_63d_jerk_v145_signal(high, low, closeadj):  # jerk 63d of: rangecontractstreak_63d
    rng = (high - low) / closeadj.replace(0, np.nan)
    med = rng.rolling(63, min_periods=21).median()
    cond = (rng < med).astype(float)
    grp = (cond == 0).cumsum()
    streak = cond.groupby(grp).cumsum()
    depth = ((med - rng) / med.replace(0, np.nan)).clip(lower=0)
    cumd = depth.where(cond == 1, 0.0).groupby(grp).cumsum()
    b = streak + cumd
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangevolspread_21d_jerk_v146_signal(high, low, closeadj):  # jerk 21d of: rangevolspread_21d
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = _z(rng, 252) - _z(_f09_rvol(closeadj, 21), 252)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_efficiencycompress_63d_jerk_v147_signal(high, low, closeadj):  # jerk 63d of: efficiencycompress_63d
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    pk21 = np.sqrt((hl ** 2).rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    pk126 = np.sqrt((hl ** 2).rolling(126, min_periods=42).mean() / (4.0 * np.log(2.0)))
    e21 = pk21 / _f09_rvol(closeadj, 21).replace(0, np.nan)
    e126 = pk126 / _f09_rvol(closeadj, 126).replace(0, np.nan)
    b = e21 / e126.replace(0, np.nan)
    result = b.diff(63).diff(63) / float(3969)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangejumpshare_21d_jerk_v148_signal(high, low, closeadj):  # jerk 21d of: rangejumpshare_21d
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = rng.rolling(21, min_periods=10).max() / rng.rolling(63, min_periods=21).median().replace(0, np.nan)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangecontractfrac_21d_jerk_v149_signal(high, low, closeadj):  # jerk 21d of: rangecontractfrac_21d
    rng = (high - low) / closeadj.replace(0, np.nan)
    med = rng.rolling(21, min_periods=10).median()
    depth = ((med - rng) / med.replace(0, np.nan)).clip(lower=0)
    b = depth.rolling(63, min_periods=21).mean()
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)
def f09vr_f09_volatility_regime_rangevolratiochg_21d_jerk_v150_signal(high, low, closeadj):  # jerk 21d of: rangevolratiochg_21d
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    ratio = rng / _f09_rvol(closeadj, 21).replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b.diff(21).diff(21) / float(441)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f09vr_f09_volatility_regime_bbwcompress_5v21_jerk_v001_signal,
    f09vr_f09_volatility_regime_bbwcompress_10v42_jerk_v002_signal,
    f09vr_f09_volatility_regime_compress_21v63_jerk_v003_signal,
    f09vr_f09_volatility_regime_compress_10v252_jerk_v004_signal,
    f09vr_f09_volatility_regime_bbwcompress_63v252_jerk_v005_signal,
    f09vr_f09_volatility_regime_compresslog_42v126_jerk_v006_signal,
    f09vr_f09_volatility_regime_compressaccel_42v126_jerk_v007_signal,
    f09vr_f09_volatility_regime_compressvol_21v63_jerk_v008_signal,
    f09vr_f09_volatility_regime_compresschg_21v63_jerk_v009_signal,
    f09vr_f09_volatility_regime_compressrevert_21v63_jerk_v010_signal,
    f09vr_f09_volatility_regime_compressrank_10v63_jerk_v011_signal,
    f09vr_f09_volatility_regime_compressmin_5v21_jerk_v012_signal,
    f09vr_f09_volatility_regime_compresspersist_21v63_jerk_v013_signal,
    f09vr_f09_volatility_regime_expandpersist_21v63_jerk_v014_signal,
    f09vr_f09_volatility_regime_compressefficiency_21d_jerk_v015_signal,
    f09vr_f09_volatility_regime_bbwz_21v126_jerk_v016_signal,
    f09vr_f09_volatility_regime_bbwz_63v252_jerk_v017_signal,
    f09vr_f09_volatility_regime_bbwrank_21v252_jerk_v018_signal,
    f09vr_f09_volatility_regime_bbwrank_63v504_jerk_v019_signal,
    f09vr_f09_volatility_regime_bbwratio_21v63_jerk_v020_signal,
    f09vr_f09_volatility_regime_bbwratio_21v126_jerk_v021_signal,
    f09vr_f09_volatility_regime_bbwspread_21v126_jerk_v022_signal,
    f09vr_f09_volatility_regime_bbwchg_21d_jerk_v023_signal,
    f09vr_f09_volatility_regime_bbwdisp_21d_jerk_v024_signal,
    f09vr_f09_volatility_regime_bbwlog_126d_jerk_v025_signal,
    f09vr_f09_volatility_regime_bbwskew_21d_jerk_v026_signal,
    f09vr_f09_volatility_regime_bbwmaxratio_21d_jerk_v027_signal,
    f09vr_f09_volatility_regime_bbwyoy_21d_jerk_v028_signal,
    f09vr_f09_volatility_regime_squeeze_21v126_jerk_v029_signal,
    f09vr_f09_volatility_regime_squeeze_63v252_jerk_v030_signal,
    f09vr_f09_volatility_regime_squeeze_126v504_jerk_v031_signal,
    f09vr_f09_volatility_regime_squeezelog_42d_jerk_v032_signal,
    f09vr_f09_volatility_regime_squeezeon_21d_jerk_v033_signal,
    f09vr_f09_volatility_regime_squeezetime_21d_jerk_v034_signal,
    f09vr_f09_volatility_regime_squeezetime_63d_jerk_v035_signal,
    f09vr_f09_volatility_regime_squeezeaccel_21d_jerk_v036_signal,
    f09vr_f09_volatility_regime_squeezerelease_21d_jerk_v037_signal,
    f09vr_f09_volatility_regime_brkoutsq_21d_jerk_v038_signal,
    f09vr_f09_volatility_regime_brkoutsq_63d_jerk_v039_signal,
    f09vr_f09_volatility_regime_brkoutcompress_21d_jerk_v040_signal,
    f09vr_f09_volatility_regime_pctb_21d_jerk_v041_signal,
    f09vr_f09_volatility_regime_pctb_63d_jerk_v042_signal,
    f09vr_f09_volatility_regime_pctbabs_21d_jerk_v043_signal,
    f09vr_f09_volatility_regime_pctbpersist_21d_jerk_v044_signal,
    f09vr_f09_volatility_regime_bbwofbbw_21v63_jerk_v045_signal,
    f09vr_f09_volatility_regime_bbwofbbw_21v126_jerk_v046_signal,
    f09vr_f09_volatility_regime_squeezeofsqueeze_21d_jerk_v047_signal,
    f09vr_f09_volatility_regime_volofvoliqr_21d_jerk_v048_signal,
    f09vr_f09_volatility_regime_bbwofbbwmom_21d_jerk_v049_signal,
    f09vr_f09_volatility_regime_pctbrange_21d_jerk_v050_signal,
    f09vr_f09_volatility_regime_rvolz_21v126_jerk_v051_signal,
    f09vr_f09_volatility_regime_rvolz_63v252_jerk_v052_signal,
    f09vr_f09_volatility_regime_bbwrank_42v252_jerk_v053_signal,
    f09vr_f09_volatility_regime_rvolrank_63v504_jerk_v054_signal,
    f09vr_f09_volatility_regime_squeezedwell_21d_jerk_v055_signal,
    f09vr_f09_volatility_regime_volcone_21d_jerk_v056_signal,
    f09vr_f09_volatility_regime_volconedist_63d_jerk_v057_signal,
    f09vr_f09_volatility_regime_voldrawup_126d_jerk_v058_signal,
    f09vr_f09_volatility_regime_volminratio_21d_jerk_v059_signal,
    f09vr_f09_volatility_regime_contractstreak_21d_jerk_v060_signal,
    f09vr_f09_volatility_regime_contractstreak_63d_jerk_v061_signal,
    f09vr_f09_volatility_regime_expandstreak_21d_jerk_v062_signal,
    f09vr_f09_volatility_regime_bbwtermconvex_63d_jerk_v063_signal,
    f09vr_f09_volatility_regime_volcurv_norm_84d_jerk_v064_signal,
    f09vr_f09_volatility_regime_regimedivg_63d_jerk_v065_signal,
    f09vr_f09_volatility_regime_turbulence_21d_jerk_v066_signal,
    f09vr_f09_volatility_regime_turbulence_63d_jerk_v067_signal,
    f09vr_f09_volatility_regime_turbratio_21v63_jerk_v068_signal,
    f09vr_f09_volatility_regime_volpersist_21d_jerk_v069_signal,
    f09vr_f09_volatility_regime_rvolema_disp_21d_jerk_v070_signal,
    f09vr_f09_volatility_regime_bandpierce_21d_jerk_v071_signal,
    f09vr_f09_volatility_regime_bandpierce_63d_jerk_v072_signal,
    f09vr_f09_volatility_regime_compresszone_21v63_jerk_v073_signal,
    f09vr_f09_volatility_regime_squeezeheat_21d_jerk_v074_signal,
    f09vr_f09_volatility_regime_volratioema_21v63_jerk_v075_signal,
    f09vr_f09_volatility_regime_bbwcompress_42v252_jerk_v076_signal,
    f09vr_f09_volatility_regime_bbwcompress_21v189_jerk_v077_signal,
    f09vr_f09_volatility_regime_compresslog_10v63_jerk_v078_signal,
    f09vr_f09_volatility_regime_compressratiochg_63d_jerk_v079_signal,
    f09vr_f09_volatility_regime_compressdispersion_21d_jerk_v080_signal,
    f09vr_f09_volatility_regime_compressbreadth_21d_jerk_v081_signal,
    f09vr_f09_volatility_regime_compressexpcycle_126d_jerk_v082_signal,
    f09vr_f09_volatility_regime_compressratiovol_42v126_jerk_v083_signal,
    f09vr_f09_volatility_regime_bbwspreadz_21v63_jerk_v084_signal,
    f09vr_f09_volatility_regime_volspreadrank_42v126_jerk_v085_signal,
    f09vr_f09_volatility_regime_volcurv_norm_42d_jerk_v086_signal,
    f09vr_f09_volatility_regime_bandtouchskew_21d_jerk_v087_signal,
    f09vr_f09_volatility_regime_bandtouchskew_63d_jerk_v088_signal,
    f09vr_f09_volatility_regime_semivolconvex_126d_jerk_v089_signal,
    f09vr_f09_volatility_regime_semiskewchg_21d_jerk_v090_signal,
    f09vr_f09_volatility_regime_volkurtz_63d_jerk_v091_signal,
    f09vr_f09_volatility_regime_retskewz_63d_jerk_v092_signal,
    f09vr_f09_volatility_regime_bandexpandenergy_63d_jerk_v093_signal,
    f09vr_f09_volatility_regime_gapvol_21d_jerk_v094_signal,
    f09vr_f09_volatility_regime_bbwz_5v63_jerk_v095_signal,
    f09vr_f09_volatility_regime_bbwz_252v504_jerk_v096_signal,
    f09vr_f09_volatility_regime_bbwstate_63d_jerk_v097_signal,
    f09vr_f09_volatility_regime_bbwexpandstate_21d_jerk_v098_signal,
    f09vr_f09_volatility_regime_bbwmin_ratio_21d_jerk_v099_signal,
    f09vr_f09_volatility_regime_bbwacceldir_21d_jerk_v100_signal,
    f09vr_f09_volatility_regime_squeezecount_21d_jerk_v101_signal,
    f09vr_f09_volatility_regime_expandcount_21d_jerk_v102_signal,
    f09vr_f09_volatility_regime_doublesqueeze_21d_jerk_v103_signal,
    f09vr_f09_volatility_regime_preexpcompress_21d_jerk_v104_signal,
    f09vr_f09_volatility_regime_squeezefirepower_21d_jerk_v105_signal,
    f09vr_f09_volatility_regime_coiledspring_21d_jerk_v106_signal,
    f09vr_f09_volatility_regime_squeezeexpcombo_21d_jerk_v107_signal,
    f09vr_f09_volatility_regime_squeezethenexp_21d_jerk_v108_signal,
    f09vr_f09_volatility_regime_volaccel_63d_jerk_v109_signal,
    f09vr_f09_volatility_regime_voltrendsign_21d_jerk_v110_signal,
    f09vr_f09_volatility_regime_volmomratio_21d_jerk_v111_signal,
    f09vr_f09_volatility_regime_volshockgap_5d_jerk_v112_signal,
    f09vr_f09_volatility_regime_volcontract_pressure_21d_jerk_v113_signal,
    f09vr_f09_volatility_regime_volexpburst_21d_jerk_v114_signal,
    f09vr_f09_volatility_regime_volregimebin_21d_jerk_v115_signal,
    f09vr_f09_volatility_regime_volregimedwell_21d_jerk_v116_signal,
    f09vr_f09_volatility_regime_volentropy_63d_jerk_v117_signal,
    f09vr_f09_volatility_regime_volzdispersion_21d_jerk_v118_signal,
    f09vr_f09_volatility_regime_calmratio_63d_jerk_v119_signal,
    f09vr_f09_volatility_regime_bbwvolofvol_21d_jerk_v120_signal,
    f09vr_f09_volatility_regime_volwhipsaw_63d_jerk_v121_signal,
    f09vr_f09_volatility_regime_volhalflife_63d_jerk_v122_signal,
    f09vr_f09_volatility_regime_pctbdisp_21d_jerk_v123_signal,
    f09vr_f09_volatility_regime_pctbtrend_21d_jerk_v124_signal,
    f09vr_f09_volatility_regime_bandwalk_21d_jerk_v125_signal,
    f09vr_f09_volatility_regime_turbchg_21d_jerk_v126_signal,
    f09vr_f09_volatility_regime_turbpersist_63d_jerk_v127_signal,
    f09vr_f09_volatility_regime_volregimecurv_126d_jerk_v128_signal,
    f09vr_f09_volatility_regime_rvolratiorange_42v126_jerk_v129_signal,
    f09vr_f09_volatility_regime_rvolzfast_10d_jerk_v130_signal,
    f09vr_f09_volatility_regime_rvolz_42v252_jerk_v131_signal,
    f09vr_f09_volatility_regime_turbpersist_clust_21d_jerk_v132_signal,
    f09vr_f09_volatility_regime_expandonset_21d_jerk_v133_signal,
    f09vr_f09_volatility_regime_contractdepth_63d_jerk_v134_signal,
    f09vr_f09_volatility_regime_intraover_ratio_21d_jerk_v135_signal,
    f09vr_f09_volatility_regime_intraover_compress_21d_jerk_v136_signal,
    f09vr_f09_volatility_regime_rangecompress_21v63_jerk_v137_signal,
    f09vr_f09_volatility_regime_rangecompress_42v126_jerk_v138_signal,
    f09vr_f09_volatility_regime_rangeexpand_21d_jerk_v139_signal,
    f09vr_f09_volatility_regime_rangecone_21d_jerk_v140_signal,
    f09vr_f09_volatility_regime_rangecontractmag_21d_jerk_v141_signal,
    f09vr_f09_volatility_regime_rangecontractpct_21d_jerk_v142_signal,
    f09vr_f09_volatility_regime_nrbarcount_21d_jerk_v143_signal,
    f09vr_f09_volatility_regime_rangeexpandstreak_21d_jerk_v144_signal,
    f09vr_f09_volatility_regime_rangecontractstreak_63d_jerk_v145_signal,
    f09vr_f09_volatility_regime_rangevolspread_21d_jerk_v146_signal,
    f09vr_f09_volatility_regime_efficiencycompress_63d_jerk_v147_signal,
    f09vr_f09_volatility_regime_rangejumpshare_21d_jerk_v148_signal,
    f09vr_f09_volatility_regime_rangecontractfrac_21d_jerk_v149_signal,
    f09vr_f09_volatility_regime_rangevolratiochg_21d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_REGIME_REGISTRY_3RD_001_150 = REGISTRY


if __name__ == "__main__":
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

    # HARD: every feature's inputs must be a subset of the SPEC allowlist.
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
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

    print("OK f09_volatility_regime_3rd_derivatives_001_150_claude.py: %d features pass" % n_features)
