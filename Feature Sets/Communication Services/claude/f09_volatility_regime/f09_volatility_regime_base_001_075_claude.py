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
# BASE FEATURES (volatility regime: compression / expansion ONLY)
# ==========================================================


# Bollinger-bandwidth compression: 5d band width over 21d band width (price-band short/long)
def f09vr_f09_volatility_regime_bbwcompress_5v21_base_v001_signal(closeadj):
    b = _f09_bbw(closeadj, 5) / _f09_bbw(closeadj, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger-bandwidth compression: 10d band width over 42d band width
def f09vr_f09_volatility_regime_bbwcompress_10v42_base_v002_signal(closeadj):
    b = _f09_bbw(closeadj, 10) / _f09_bbw(closeadj, 42).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol compression ratio 21d/63d (month vs quarter)
def f09vr_f09_volatility_regime_compress_21v63_base_v003_signal(closeadj):
    b = _f09_compress_ratio(closeadj, 21, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol compression ratio 10d/252d (fortnight vs year)
def f09vr_f09_volatility_regime_compress_10v252_base_v004_signal(closeadj):
    b = _f09_compress_ratio(closeadj, 10, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger-bandwidth compression: 63d band width over 252d band width (quarter vs year)
def f09vr_f09_volatility_regime_bbwcompress_63v252_base_v005_signal(closeadj):
    b = _f09_bbw(closeadj, 63) / _f09_bbw(closeadj, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log compression ratio 42d/126d (symmetric around 0)
def f09vr_f09_volatility_regime_compresslog_42v126_base_v006_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 42, 126)
    b = np.log(r.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression acceleration: 2nd difference of the 42/126 vol ratio over 21d steps (regime bending)
def f09vr_f09_volatility_regime_compressaccel_42v126_base_v007_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 42, 126)
    b = r - 2.0 * r.shift(21) + r.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression-ratio instability: 63d std of the 21/63 vol ratio
def f09vr_f09_volatility_regime_compressvol_21v63_base_v008_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in 21/63 compression ratio over 21d (regime-turn velocity)
def f09vr_f09_volatility_regime_compresschg_21v63_base_v009_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r - r.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio minus its own 63d EWM (displacement)
def f09vr_f09_volatility_regime_compressrevert_21v63_base_v010_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r - r.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio 10/63 percentile vs its own 252d history
def f09vr_f09_volatility_regime_compressrank_10v63_base_v011_signal(closeadj):
    b = _rank(_f09_compress_ratio(closeadj, 10, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deepest recent compression: min of 5/21 ratio over 63d
def f09vr_f09_volatility_regime_compressmin_5v21_base_v012_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 5, 21)
    b = r.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression persistence: fraction of 63d with 21/63 ratio below 1
def f09vr_f09_volatility_regime_compresspersist_21v63_base_v013_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    comp = (r < 1.0).astype(float)
    b = comp.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion persistence: mean excess of 21/63 ratio above 1 over 63d
def f09vr_f09_volatility_regime_expandpersist_21v63_base_v014_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    exc = (r - 1.0).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression efficiency: 21d net log-return magnitude over summed |daily ret| (low=choppy compression, high=trending)
def f09vr_f09_volatility_regime_compressefficiency_21d_base_v015_signal(closeadj):
    r = _f09_logret(closeadj)
    net = r.rolling(21, min_periods=10).sum().abs()
    gross = r.abs().rolling(21, min_periods=10).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Bollinger bandwidth z-scored vs its own 126d history
def f09vr_f09_volatility_regime_bbwz_21v126_base_v016_signal(closeadj):
    b = _z(_f09_bbw(closeadj, 21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Bollinger bandwidth z-scored vs its own 252d history
def f09vr_f09_volatility_regime_bbwz_63v252_base_v017_signal(closeadj):
    b = _z(_f09_bbw(closeadj, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth percentile rank vs 252d (width-cone position)
def f09vr_f09_volatility_regime_bbwrank_21v252_base_v018_signal(closeadj):
    b = _rank(_f09_bbw(closeadj, 21), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d bandwidth percentile rank vs 504d
def f09vr_f09_volatility_regime_bbwrank_63v504_base_v019_signal(closeadj):
    b = _rank(_f09_bbw(closeadj, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth ratio 21d/63d (short vs long width)
def f09vr_f09_volatility_regime_bbwratio_21v63_base_v020_signal(closeadj):
    b = _f09_bbw(closeadj, 21) / _f09_bbw(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth ratio 21d/126d (short vs long width)
def f09vr_f09_volatility_regime_bbwratio_21v126_base_v021_signal(closeadj):
    b = _f09_bbw(closeadj, 21) / _f09_bbw(closeadj, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth term spread: 21d minus 126d width
def f09vr_f09_volatility_regime_bbwspread_21v126_base_v022_signal(closeadj):
    b = _f09_bbw(closeadj, 21) - _f09_bbw(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in 21d bandwidth over 21d (width expansion velocity)
def f09vr_f09_volatility_regime_bbwchg_21d_base_v023_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    b = bb - bb.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth instability: 63d std of 21d bandwidth
def f09vr_f09_volatility_regime_bbwdisp_21d_base_v024_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    b = bb.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log 126d bandwidth minus log its own 504d mean (long width regime distance)
def f09vr_f09_volatility_regime_bbwlog_126d_base_v025_signal(closeadj):
    bb = _f09_bbw(closeadj, 126)
    b = np.log(bb.replace(0, np.nan)) - np.log(_mean(bb, 504).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth skew: signed-root of 21d bandwidth vs its 63d median
def f09vr_f09_volatility_regime_bbwskew_21d_base_v026_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    med = bb.rolling(63, min_periods=21).median()
    d = (bb - med) / med.replace(0, np.nan)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth vs its own 63d max (proximity to width peak)
def f09vr_f09_volatility_regime_bbwmaxratio_21d_base_v027_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    b = bb / bb.rolling(63, min_periods=21).max().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth vs 252d ago (year-over-year width regime)
def f09vr_f09_volatility_regime_bbwyoy_21d_base_v028_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    b = bb / bb.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth vs its 126d min (>1 = expanded off squeeze)
def f09vr_f09_volatility_regime_squeeze_21v126_base_v029_signal(closeadj):
    b = _f09_squeeze(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d bandwidth vs its 252d min
def f09vr_f09_volatility_regime_squeeze_63v252_base_v030_signal(closeadj):
    b = _f09_squeeze(closeadj, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d bandwidth vs its 504d min
def f09vr_f09_volatility_regime_squeeze_126v504_base_v031_signal(closeadj):
    b = _f09_squeeze(closeadj, 126, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log of 42d squeeze ratio vs its 189d min
def f09vr_f09_volatility_regime_squeezelog_42d_base_v032_signal(closeadj):
    s = _f09_squeeze(closeadj, 42, 189)
    b = np.log(s.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-on tightness: 126d-min bandwidth over current (1=at trough)
def f09vr_f09_volatility_regime_squeezeon_21d_base_v033_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    lo = bb.rolling(126, min_periods=63).min()
    b = (lo / bb.replace(0, np.nan)).clip(upper=1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 63d the 21d bandwidth sat in its bottom 252d quartile
def f09vr_f09_volatility_regime_squeezetime_21d_base_v034_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    insq = (rk <= 0.25).astype(float)
    b = insq.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep-squeeze occupancy: fraction of last 126d the 63d bandwidth sat in its bottom 252d quartile
def f09vr_f09_volatility_regime_squeezetime_63d_base_v035_signal(closeadj):
    bb = _f09_bbw(closeadj, 63)
    rk = bb.rolling(252, min_periods=84).rank(pct=True)
    insq = (rk <= 0.25).astype(float)
    b = insq.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-release acceleration: change in 21d squeeze ratio over 10d
def f09vr_f09_volatility_regime_squeezeaccel_21d_base_v036_signal(closeadj):
    sq = _f09_squeeze(closeadj, 21, 126)
    b = sq - sq.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-release: bandwidth now vs its 21d-ago 63d-min floor
def f09vr_f09_volatility_regime_squeezerelease_21d_base_v037_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    floor = bb.rolling(63, min_periods=21).min().shift(21)
    b = bb / floor.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-squeeze: prior 21d-ago bandwidth squeeze x current width expansion
def f09vr_f09_volatility_regime_brkoutsq_21d_base_v038_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    prior_sq = (1.0 - rk.shift(21)).clip(lower=0)
    expand = (bb / bb.shift(21).replace(0, np.nan) - 1.0).clip(lower=0)
    b = prior_sq * expand
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-squeeze 63d: prior squeeze x bandwidth expansion
def f09vr_f09_volatility_regime_brkoutsq_63d_base_v039_signal(closeadj):
    bb = _f09_bbw(closeadj, 63)
    rk = bb.rolling(504, min_periods=126).rank(pct=True)
    prior_sq = (1.0 - rk.shift(63)).clip(lower=0)
    expand = (bb / bb.shift(63).replace(0, np.nan) - 1.0).clip(lower=0)
    b = prior_sq * expand
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-compression: prior low compression-ratio rank x current ratio jump
def f09vr_f09_volatility_regime_brkoutcompress_21d_base_v040_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    rk = r.rolling(252, min_periods=63).rank(pct=True)
    prior_low = (1.0 - rk.shift(21)).clip(lower=0)
    jump = (r / r.shift(21).replace(0, np.nan) - 1.0).clip(lower=0)
    b = prior_low * jump
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# %B band position: where price sits within its own 21d Bollinger band
def f09vr_f09_volatility_regime_pctb_21d_base_v041_signal(closeadj):
    b = _f09_pctb(closeadj, 21) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# %B band position within its own 63d Bollinger band
def f09vr_f09_volatility_regime_pctb_63d_base_v042_signal(closeadj):
    b = _f09_pctb(closeadj, 63) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-edge pressure: |%B-0.5| EWM (how often price rides its own band edges)
def f09vr_f09_volatility_regime_pctbabs_21d_base_v043_signal(closeadj):
    pb = (_f09_pctb(closeadj, 21) - 0.5).abs()
    b = pb.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position persistence: 63d lag-1 autocorrelation of 21d %B (sticky vs whippy band travel)
def f09vr_f09_volatility_regime_pctbpersist_21d_base_v044_signal(closeadj):
    pb = _f09_pctb(closeadj, 21)
    b = pb.rolling(63, min_periods=21).corr(pb.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth-of-bandwidth: 63d coefficient-of-variation of 21d Bollinger bandwidth (band instability)
def f09vr_f09_volatility_regime_bbwofbbw_21v63_base_v045_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    b = bb.rolling(63, min_periods=21).std() / bb.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth-of-bandwidth: 126d coefficient-of-variation of 21d Bollinger bandwidth
def f09vr_f09_volatility_regime_bbwofbbw_21v126_base_v046_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    b = bb.rolling(126, min_periods=42).std() / bb.rolling(126, min_periods=42).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze instability: 63d std of the 21d squeeze ratio (how erratically the band coils/uncoils)
def f09vr_f09_volatility_regime_squeezeofsqueeze_21d_base_v047_signal(closeadj):
    sq = _f09_squeeze(closeadj, 21, 126)
    b = sq.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# robust vol-of-vol: 126d IQR of 21d vol over its median
def f09vr_f09_volatility_regime_volofvoliqr_21d_base_v048_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    q3 = rv.rolling(126, min_periods=42).quantile(0.75)
    q1 = rv.rolling(126, min_periods=42).quantile(0.25)
    med = rv.rolling(126, min_periods=42).median()
    b = (q3 - q1) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-instability momentum: change over 21d in 63d band-instability (band turning erratic)
def f09vr_f09_volatility_regime_bbwofbbwmom_21d_base_v049_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    bov = bb.rolling(63, min_periods=21).std() / bb.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = bov - bov.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-traverse amplitude: 63d range (max-min) of 21d %B (how fully price sweeps its own band)
def f09vr_f09_volatility_regime_pctbrange_21d_base_v050_signal(closeadj):
    pb = _f09_pctb(closeadj, 21)
    b = pb.rolling(63, min_periods=21).max() - pb.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol z-scored vs its own 126d history (vol-regime z, de-leveled)
def f09vr_f09_volatility_regime_rvolz_21v126_base_v051_signal(closeadj):
    b = _z(_f09_rvol(closeadj, 21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol z-scored vs its own 252d history (vol-regime z)
def f09vr_f09_volatility_regime_rvolz_63v252_base_v052_signal(closeadj):
    b = _z(_f09_rvol(closeadj, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Bollinger-bandwidth percentile rank vs 252d (price-band width-cone occupancy)
def f09vr_f09_volatility_regime_bbwrank_42v252_base_v053_signal(closeadj):
    b = _rank(_f09_bbw(closeadj, 42), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol percentile rank vs 504d (vol-cone occupancy)
def f09vr_f09_volatility_regime_rvolrank_63v504_base_v054_signal(closeadj):
    b = _rank(_f09_rvol(closeadj, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze dwell: consecutive days the 21d bandwidth stays in its bottom-third 252d band, scaled by depth
def f09vr_f09_volatility_regime_squeezedwell_21d_base_v055_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    insq = (rk <= 0.3333).astype(float)
    grp = (insq == 0).cumsum()
    dwell = insq.groupby(grp).cumsum()
    b = dwell * (1.0 + (0.3333 - rk).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# edge-emphasized vol-cone: signed-square of centered 21d-vol min-max position vs 252d
def f09vr_f09_volatility_regime_volcone_21d_base_v056_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    lo = rv.rolling(252, min_periods=63).min()
    hi = rv.rolling(252, min_periods=63).max()
    pos = (rv - lo) / (hi - lo).replace(0, np.nan) - 0.5
    b = np.sign(pos) * pos * pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone edge distance: how far 63d vol sits from the nearer of its own 504d min/max (regime-edge proximity)
def f09vr_f09_volatility_regime_volconedist_63d_base_v057_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    lo = rv.rolling(504, min_periods=126).min()
    hi = rv.rolling(504, min_periods=126).max()
    pos = (rv - lo) / (hi - lo).replace(0, np.nan)
    b = (pos - 0.5).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol drawup: 126d vol vs its own trailing 504d min (rise off calmest)
def f09vr_f09_volatility_regime_voldrawup_126d_base_v058_signal(closeadj):
    rv = _f09_rvol(closeadj, 126)
    b = rv / rv.rolling(504, min_periods=126).min().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# complacency gauge: 21d vol vs its 252d min x sign of recent change
def f09vr_f09_volatility_regime_volminratio_21d_base_v059_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    ratio = rv / rv.rolling(252, min_periods=63).min().replace(0, np.nan)
    turn = np.tanh(50.0 * (rv - rv.shift(10)))
    b = ratio * turn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-contraction streak vs 21d |ret| median (depth-weighted)
def f09vr_f09_volatility_regime_contractstreak_21d_base_v060_signal(closeadj):
    b = _f09_contraction_streak(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-contraction streak vs 63d |ret| median (depth-weighted)
def f09vr_f09_volatility_regime_contractstreak_63d_base_v061_signal(closeadj):
    b = _f09_contraction_streak(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-expansion streak vs 21d |ret| median (depth-weighted)
def f09vr_f09_volatility_regime_expandstreak_21d_base_v062_signal(closeadj):
    b = _f09_expansion_streak(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth-term convexity: (21/63 width ratio) minus (63/252 width ratio) (kink in the band-width curve)
def f09vr_f09_volatility_regime_bbwtermconvex_63d_base_v063_signal(closeadj):
    r_short = _f09_bbw(closeadj, 21) / _f09_bbw(closeadj, 63).replace(0, np.nan)
    r_long = _f09_bbw(closeadj, 63) / _f09_bbw(closeadj, 252).replace(0, np.nan)
    b = r_short - r_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized vol curvature: (42 - 2*84 + 168 vol) over 84d vol (long-end convexity)
def f09vr_f09_volatility_regime_volcurv_norm_84d_base_v064_signal(closeadj):
    c = _f09_rvol(closeadj, 42) - 2.0 * _f09_rvol(closeadj, 84) + _f09_rvol(closeadj, 168)
    b = c / _f09_rvol(closeadj, 84).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime divergence: 21d-vol z minus 63d-vol z (each vs its own 252d median/std)
def f09vr_f09_volatility_regime_regimedivg_63d_base_v065_signal(closeadj):
    rv21 = _f09_rvol(closeadj, 21)
    rv63 = _f09_rvol(closeadj, 63)
    d21 = (rv21 - rv21.rolling(252, min_periods=63).median()) / rv21.rolling(252, min_periods=63).std().replace(0, np.nan)
    d63 = (rv63 - rv63.rolling(252, min_periods=63).median()) / rv63.rolling(252, min_periods=63).std().replace(0, np.nan)
    b = d21 - d63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turbulence: mean squared standardized return vs its own 21d moments
def f09vr_f09_volatility_regime_turbulence_21d_base_v066_signal(closeadj):
    b = _f09_turbulence(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turbulence: mean squared standardized return vs its own 63d moments
def f09vr_f09_volatility_regime_turbulence_63d_base_v067_signal(closeadj):
    b = _f09_turbulence(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turbulence term ratio: 21d turbulence over 63d turbulence (short vs long turbulence)
def f09vr_f09_volatility_regime_turbratio_21v63_base_v068_signal(closeadj):
    b = _f09_turbulence(closeadj, 21) / _f09_turbulence(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol persistence: 63d lag-1 autocorrelation of 21d vol
def f09vr_f09_volatility_regime_volpersist_21d_base_v069_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(63, min_periods=21).corr(rv.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol displacement: fast EWM minus slow EWM of 21d vol, over 63d vol
def f09vr_f09_volatility_regime_rvolema_disp_21d_base_v070_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = (rv.ewm(span=21, min_periods=10).mean() - rv.ewm(span=63, min_periods=21).mean()) / _f09_rvol(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-pierce regime: 63d mean of how far 21d %B sits beyond its band edges (band-breaking volatility)
def f09vr_f09_volatility_regime_bandpierce_21d_base_v071_signal(closeadj):
    pb = _f09_pctb(closeadj, 21)
    pierce = (pb - pb.clip(0.0, 1.0)).abs()
    b = pierce.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-pierce regime over 63d band: mean distance of 63d %B outside [0,1]
def f09vr_f09_volatility_regime_bandpierce_63d_base_v072_signal(closeadj):
    pb = _f09_pctb(closeadj, 63)
    pierce = (pb - pb.clip(0.0, 1.0)).abs()
    b = pierce.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression-zone occupancy: signed depth of 21/63 ratio outside [0.8,1.2] band
def f09vr_f09_volatility_regime_compresszone_21v63_base_v073_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    comp = (0.8 - r).clip(lower=0)
    exp = (r - 1.2).clip(lower=0)
    b = exp - comp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze heat: how long since 21d bandwidth last hit a fresh 126d low (staleness of trough)
def f09vr_f09_volatility_regime_squeezeheat_21d_base_v074_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    atlow = (bb <= bb.rolling(126, min_periods=63).min() * 1.0001).astype(float)
    grp = atlow.cumsum()
    since = atlow.groupby(grp).cumcount().astype(float)
    b = since / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed compression state: EWM of the 21/63 vol ratio minus 1
def f09vr_f09_volatility_regime_volratioema_21v63_base_v075_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r.ewm(span=21, min_periods=10).mean() - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09vr_f09_volatility_regime_bbwcompress_5v21_base_v001_signal,
    f09vr_f09_volatility_regime_bbwcompress_10v42_base_v002_signal,
    f09vr_f09_volatility_regime_compress_21v63_base_v003_signal,
    f09vr_f09_volatility_regime_compress_10v252_base_v004_signal,
    f09vr_f09_volatility_regime_bbwcompress_63v252_base_v005_signal,
    f09vr_f09_volatility_regime_compresslog_42v126_base_v006_signal,
    f09vr_f09_volatility_regime_compressaccel_42v126_base_v007_signal,
    f09vr_f09_volatility_regime_compressvol_21v63_base_v008_signal,
    f09vr_f09_volatility_regime_compresschg_21v63_base_v009_signal,
    f09vr_f09_volatility_regime_compressrevert_21v63_base_v010_signal,
    f09vr_f09_volatility_regime_compressrank_10v63_base_v011_signal,
    f09vr_f09_volatility_regime_compressmin_5v21_base_v012_signal,
    f09vr_f09_volatility_regime_compresspersist_21v63_base_v013_signal,
    f09vr_f09_volatility_regime_expandpersist_21v63_base_v014_signal,
    f09vr_f09_volatility_regime_compressefficiency_21d_base_v015_signal,
    f09vr_f09_volatility_regime_bbwz_21v126_base_v016_signal,
    f09vr_f09_volatility_regime_bbwz_63v252_base_v017_signal,
    f09vr_f09_volatility_regime_bbwrank_21v252_base_v018_signal,
    f09vr_f09_volatility_regime_bbwrank_63v504_base_v019_signal,
    f09vr_f09_volatility_regime_bbwratio_21v63_base_v020_signal,
    f09vr_f09_volatility_regime_bbwratio_21v126_base_v021_signal,
    f09vr_f09_volatility_regime_bbwspread_21v126_base_v022_signal,
    f09vr_f09_volatility_regime_bbwchg_21d_base_v023_signal,
    f09vr_f09_volatility_regime_bbwdisp_21d_base_v024_signal,
    f09vr_f09_volatility_regime_bbwlog_126d_base_v025_signal,
    f09vr_f09_volatility_regime_bbwskew_21d_base_v026_signal,
    f09vr_f09_volatility_regime_bbwmaxratio_21d_base_v027_signal,
    f09vr_f09_volatility_regime_bbwyoy_21d_base_v028_signal,
    f09vr_f09_volatility_regime_squeeze_21v126_base_v029_signal,
    f09vr_f09_volatility_regime_squeeze_63v252_base_v030_signal,
    f09vr_f09_volatility_regime_squeeze_126v504_base_v031_signal,
    f09vr_f09_volatility_regime_squeezelog_42d_base_v032_signal,
    f09vr_f09_volatility_regime_squeezeon_21d_base_v033_signal,
    f09vr_f09_volatility_regime_squeezetime_21d_base_v034_signal,
    f09vr_f09_volatility_regime_squeezetime_63d_base_v035_signal,
    f09vr_f09_volatility_regime_squeezeaccel_21d_base_v036_signal,
    f09vr_f09_volatility_regime_squeezerelease_21d_base_v037_signal,
    f09vr_f09_volatility_regime_brkoutsq_21d_base_v038_signal,
    f09vr_f09_volatility_regime_brkoutsq_63d_base_v039_signal,
    f09vr_f09_volatility_regime_brkoutcompress_21d_base_v040_signal,
    f09vr_f09_volatility_regime_pctb_21d_base_v041_signal,
    f09vr_f09_volatility_regime_pctb_63d_base_v042_signal,
    f09vr_f09_volatility_regime_pctbabs_21d_base_v043_signal,
    f09vr_f09_volatility_regime_pctbpersist_21d_base_v044_signal,
    f09vr_f09_volatility_regime_bbwofbbw_21v63_base_v045_signal,
    f09vr_f09_volatility_regime_bbwofbbw_21v126_base_v046_signal,
    f09vr_f09_volatility_regime_squeezeofsqueeze_21d_base_v047_signal,
    f09vr_f09_volatility_regime_volofvoliqr_21d_base_v048_signal,
    f09vr_f09_volatility_regime_bbwofbbwmom_21d_base_v049_signal,
    f09vr_f09_volatility_regime_pctbrange_21d_base_v050_signal,
    f09vr_f09_volatility_regime_rvolz_21v126_base_v051_signal,
    f09vr_f09_volatility_regime_rvolz_63v252_base_v052_signal,
    f09vr_f09_volatility_regime_bbwrank_42v252_base_v053_signal,
    f09vr_f09_volatility_regime_rvolrank_63v504_base_v054_signal,
    f09vr_f09_volatility_regime_squeezedwell_21d_base_v055_signal,
    f09vr_f09_volatility_regime_volcone_21d_base_v056_signal,
    f09vr_f09_volatility_regime_volconedist_63d_base_v057_signal,
    f09vr_f09_volatility_regime_voldrawup_126d_base_v058_signal,
    f09vr_f09_volatility_regime_volminratio_21d_base_v059_signal,
    f09vr_f09_volatility_regime_contractstreak_21d_base_v060_signal,
    f09vr_f09_volatility_regime_contractstreak_63d_base_v061_signal,
    f09vr_f09_volatility_regime_expandstreak_21d_base_v062_signal,
    f09vr_f09_volatility_regime_bbwtermconvex_63d_base_v063_signal,
    f09vr_f09_volatility_regime_volcurv_norm_84d_base_v064_signal,
    f09vr_f09_volatility_regime_regimedivg_63d_base_v065_signal,
    f09vr_f09_volatility_regime_turbulence_21d_base_v066_signal,
    f09vr_f09_volatility_regime_turbulence_63d_base_v067_signal,
    f09vr_f09_volatility_regime_turbratio_21v63_base_v068_signal,
    f09vr_f09_volatility_regime_volpersist_21d_base_v069_signal,
    f09vr_f09_volatility_regime_rvolema_disp_21d_base_v070_signal,
    f09vr_f09_volatility_regime_bandpierce_21d_base_v071_signal,
    f09vr_f09_volatility_regime_bandpierce_63d_base_v072_signal,
    f09vr_f09_volatility_regime_compresszone_21v63_base_v073_signal,
    f09vr_f09_volatility_regime_squeezeheat_21d_base_v074_signal,
    f09vr_f09_volatility_regime_volratioema_21v63_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_REGIME_REGISTRY_001_075 = REGISTRY


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

    print("OK f09_volatility_regime_base_001_075_claude.py: %d features pass" % n_features)
