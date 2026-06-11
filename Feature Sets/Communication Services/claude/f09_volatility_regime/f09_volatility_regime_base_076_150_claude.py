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


# bandwidth compression term ratio: 42d Bollinger bandwidth over 252d bandwidth (width month vs year)
def f09vr_f09_volatility_regime_bbwcompress_42v252_base_v076_signal(closeadj):
    b = _f09_bbw(closeadj, 42) / _f09_bbw(closeadj, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger-bandwidth compression: 21d band width over 189d band width (month vs three-quarters)
def f09vr_f09_volatility_regime_bbwcompress_21v189_base_v077_signal(closeadj):
    b = _f09_bbw(closeadj, 21) / _f09_bbw(closeadj, 189).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log compression ratio 10d/63d
def f09vr_f09_volatility_regime_compresslog_10v63_base_v078_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 10, 63)
    b = np.log(r.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in 21/63 compression ratio over 63d (regime turn)
def f09vr_f09_volatility_regime_compressratiochg_63d_base_v079_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of short/long vol ratios across 5/21, 5/63, 21/63
def f09vr_f09_volatility_regime_compressdispersion_21d_base_v080_signal(closeadj):
    r1 = _f09_compress_ratio(closeadj, 5, 21)
    r2 = _f09_compress_ratio(closeadj, 5, 63)
    r3 = _f09_compress_ratio(closeadj, 21, 63)
    b = pd.concat([r1, r2, r3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression breadth: avg log-shortfall of 5/10/21d vols below 63d vol
def f09vr_f09_volatility_regime_compressbreadth_21d_base_v081_signal(closeadj):
    lv = _f09_rvol(closeadj, 63)
    s1 = np.log(lv.replace(0, np.nan) / _f09_rvol(closeadj, 5).replace(0, np.nan))
    s2 = np.log(lv.replace(0, np.nan) / _f09_rvol(closeadj, 10).replace(0, np.nan))
    s3 = np.log(lv.replace(0, np.nan) / _f09_rvol(closeadj, 21).replace(0, np.nan))
    b = (s1 + s2 + s3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression-expansion cycle position: 42/126 ratio vs its 126d midpoint over range
def f09vr_f09_volatility_regime_compressexpcycle_126d_base_v082_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 42, 126)
    lo = r.rolling(126, min_periods=42).min()
    hi = r.rolling(126, min_periods=42).max()
    mid = (hi + lo) / 2.0
    b = (r - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression-ratio churn: 42d std of the 42/126 vol ratio
def f09vr_f09_volatility_regime_compressratiovol_42v126_base_v083_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 42, 126)
    b = r.rolling(42, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width term spread in std units: (63d minus 21d bandwidth) over 63d std of 21d bandwidth
def f09vr_f09_volatility_regime_bbwspreadz_21v63_base_v084_signal(closeadj):
    sb = _f09_bbw(closeadj, 21)
    lb = _f09_bbw(closeadj, 63)
    b = (lb - sb) / sb.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-slope occupancy: (126d-42d vol)/126d vol percentile-ranked vs its own 252d history
def f09vr_f09_volatility_regime_volspreadrank_42v126_base_v085_signal(closeadj):
    lv = _f09_rvol(closeadj, 126)
    sp = (lv - _f09_rvol(closeadj, 42)) / lv.replace(0, np.nan)
    b = _rank(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized short vol curvature: (21 - 2*42 + 63 vol)/42d vol
def f09vr_f09_volatility_regime_volcurv_norm_42d_base_v086_signal(closeadj):
    c = _f09_rvol(closeadj, 21) - 2.0 * _f09_rvol(closeadj, 42) + _f09_rvol(closeadj, 63)
    b = c / _f09_rvol(closeadj, 42).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-touch asymmetry: 63d net of upper-band rides minus lower-band rides via 21d %B (which edge price hugs)
def f09vr_f09_volatility_regime_bandtouchskew_21d_base_v087_signal(closeadj):
    pb = _f09_pctb(closeadj, 21)
    up = (pb > 0.8).astype(float)
    dn = (pb < 0.2).astype(float)
    b = (up - dn).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-touch asymmetry over 63d band: net upper vs lower edge-riding via 63d %B
def f09vr_f09_volatility_regime_bandtouchskew_63d_base_v088_signal(closeadj):
    pb = _f09_pctb(closeadj, 63)
    up = (pb > 0.8).astype(float)
    dn = (pb < 0.2).astype(float)
    b = (up - dn).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-vol convexity: 126d down-semi over up-semi minus its own 252d EWM (long asymmetry regime distance)
def f09vr_f09_volatility_regime_semivolconvex_126d_base_v089_signal(closeadj):
    r = _f09_logret(closeadj)
    dn = np.sqrt((r.where(r < 0, 0.0) ** 2).rolling(126, min_periods=42).mean())
    up = np.sqrt((r.where(r > 0, 0.0) ** 2).rolling(126, min_periods=42).mean())
    ratio = dn / up.replace(0, np.nan)
    b = np.log(ratio.replace(0, np.nan)) - np.log(ratio.replace(0, np.nan)).ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in 21d vol asymmetry over 21d (asymmetry regime turn)
def f09vr_f09_volatility_regime_semiskewchg_21d_base_v090_signal(closeadj):
    r = _f09_logret(closeadj)
    dn = np.sqrt((r.where(r < 0, 0.0) ** 2).rolling(21, min_periods=10).mean())
    up = np.sqrt((r.where(r > 0, 0.0) ** 2).rolling(21, min_periods=10).mean())
    sk = (dn - up) / (dn + up).replace(0, np.nan)
    b = sk - sk.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return kurtosis z-scored vs its own 252d history (tail-regime z)
def f09vr_f09_volatility_regime_volkurtz_63d_base_v091_signal(closeadj):
    r = _f09_logret(closeadj)
    k = r.rolling(63, min_periods=21).kurt()
    b = _z(k, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return skew z-scored vs its own 252d history (crash-asymmetry regime z)
def f09vr_f09_volatility_regime_retskewz_63d_base_v092_signal(closeadj):
    r = _f09_logret(closeadj)
    sk = r.rolling(63, min_periods=21).skew()
    b = _z(sk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-expansion energy: 63d mean excess of 21d bandwidth above its 2-sigma band-width envelope (width-blowup propensity)
def f09vr_f09_volatility_regime_bandexpandenergy_63d_base_v093_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    m = bb.rolling(63, min_periods=21).mean()
    sd = bb.rolling(63, min_periods=21).std()
    exc = ((bb - (m + 2.0 * sd)) / m.replace(0, np.nan)).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jump gauge: 21d max |ret| over its 21d median |ret| (gappiness)
def f09vr_f09_volatility_regime_gapvol_21d_base_v094_signal(closeadj):
    r = _f09_logret(closeadj).abs()
    b = r.rolling(21, min_periods=10).max() / r.rolling(21, min_periods=10).median().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d bandwidth z-scored vs its own 63d history (fast width regime z)
def f09vr_f09_volatility_regime_bbwz_5v63_base_v095_signal(closeadj):
    b = _z(_f09_bbw(closeadj, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d bandwidth z-scored vs its own 504d history (long width regime z)
def f09vr_f09_volatility_regime_bbwz_252v504_base_v096_signal(closeadj):
    b = _z(_f09_bbw(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d bandwidth vs 126d ago (long width regime momentum)
def f09vr_f09_volatility_regime_bbwstate_63d_base_v097_signal(closeadj):
    bb = _f09_bbw(closeadj, 63)
    b = bb / bb.shift(126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth expansion persistence: mean excess of 21d bbw above its 63d mean
def f09vr_f09_volatility_regime_bbwexpandstate_21d_base_v098_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    m = bb.rolling(63, min_periods=21).mean()
    exc = ((bb - m) / m.replace(0, np.nan)).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tightest-squeeze level: 63d-min 21d bandwidth over current bandwidth
def f09vr_f09_volatility_regime_bbwmin_ratio_21d_base_v099_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    b = bb.rolling(63, min_periods=21).min() / bb.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth acceleration direction: signed-root of 21d bbw 2nd difference
def f09vr_f09_volatility_regime_bbwacceldir_21d_base_v100_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    a = bb.diff(21).diff(21)
    b = np.sign(a) * (a.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-onset intensity: 252d count of bottom-quartile-bandwidth entries, depth-weighted
def f09vr_f09_volatility_regime_squeezecount_21d_base_v101_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    insq = (rk <= 0.25).astype(float)
    entry = ((insq == 1) & (insq.shift(1) == 0)).astype(float)
    weighted = entry * (0.25 - rk).clip(lower=0)
    b = entry.rolling(252, min_periods=63).sum() + 50.0 * weighted.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion-burst intensity: 252d count of top-quartile-bandwidth onsets, depth-weighted
def f09vr_f09_volatility_regime_expandcount_21d_base_v102_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    exp = (rk >= 0.75).astype(float)
    entry = ((exp == 1) & (exp.shift(1) == 0)).astype(float)
    weighted = entry * (rk - 0.75).clip(lower=0)
    b = entry.rolling(252, min_periods=63).sum() + 50.0 * weighted.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# double compression: both 21d vol and 21d bandwidth in bottom 252d quartile
def f09vr_f09_volatility_regime_doublesqueeze_21d_base_v103_signal(closeadj):
    vr = _f09_rvol(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    br = _f09_bbw(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    b = (1.0 - vr) * (1.0 - br)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pre-expansion coil: low current bandwidth rank x rising vol-of-vol
def f09vr_f09_volatility_regime_preexpcompress_21d_base_v104_signal(closeadj):
    br = 1.0 - _f09_bbw(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    vov = _f09_volofvol(closeadj, 21, 63)
    vovchg = (vov - vov.shift(21)).clip(lower=0)
    b = br * vovchg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze firepower: bandwidth depth below 252d median x vol-of-vol
def f09vr_f09_volatility_regime_squeezefirepower_21d_base_v105_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    med = bb.rolling(252, min_periods=63).median()
    depth = ((med - bb) / med.replace(0, np.nan)).clip(lower=0)
    b = depth * _f09_volofvol(closeadj, 21, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coiled spring: vol-contraction streak x prior-low vol rank (loaded for breakout)
def f09vr_f09_volatility_regime_coiledspring_21d_base_v106_signal(closeadj):
    streak = _f09_contraction_streak(closeadj, 21)
    rv = _f09_rvol(closeadj, 21)
    rk = rv.rolling(252, min_periods=63).rank(pct=True)
    b = streak * (1.0 - rk)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-expansion composite: log squeeze minus log compression
def f09vr_f09_volatility_regime_squeezeexpcombo_21d_base_v107_signal(closeadj):
    sq = np.log(_f09_squeeze(closeadj, 21, 126).replace(0, np.nan))
    cm = np.log(_f09_compress_ratio(closeadj, 21, 63).replace(0, np.nan))
    b = sq - cm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-then-expand: prior bandwidth squeeze x current vol-ratio burst
def f09vr_f09_volatility_regime_squeezethenexp_21d_base_v108_signal(closeadj):
    bb = _f09_bbw(closeadj, 21)
    rk = bb.rolling(252, min_periods=63).rank(pct=True)
    prior_sq = (1.0 - rk.shift(21)).clip(lower=0)
    r = _f09_compress_ratio(closeadj, 5, 21)
    burst = (r - 1.0).clip(lower=0)
    b = prior_sq * burst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime momentum: 63d vol change over 63d, normalized by prior vol
def f09vr_f09_volatility_regime_volaccel_63d_base_v109_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    b = (rv - rv.shift(63)) / rv.shift(63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol trend sign x magnitude: signed-root of 21d vol change vs 63d ago
def f09vr_f09_volatility_regime_voltrendsign_21d_base_v110_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    chg = rv - rv.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol momentum acceleration: change in (21d vol / its 63d EWM) over 10d
def f09vr_f09_volatility_regime_volmomratio_21d_base_v111_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    ratio = rv / rv.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    b = ratio - ratio.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol shock gap: (5d vol minus 21d vol) over 63d vol-of-vol (jump in std units)
def f09vr_f09_volatility_regime_volshockgap_5d_base_v112_signal(closeadj):
    sv = _f09_rvol(closeadj, 5)
    mv = _f09_rvol(closeadj, 21)
    vov = mv.rolling(63, min_periods=21).std()
    b = (sv - mv) / vov.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net contraction pressure: mean of normalized negative 21d-vol daily changes over 63d
def f09vr_f09_volatility_regime_volcontract_pressure_21d_base_v113_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    dn = (-rv.diff()).clip(lower=0) / rv.shift(1).replace(0, np.nan)
    b = dn.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol expansion burst: 63d max 21d vol over its 63d median
def f09vr_f09_volatility_regime_volexpburst_21d_base_v114_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(63, min_periods=21).max() / rv.rolling(63, min_periods=21).median().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime ladder: how many of 63/126/252d vols the 21d vol exceeds, plus tanh deviation
def f09vr_f09_volatility_regime_volregimebin_21d_base_v115_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    above = ((rv > _f09_rvol(closeadj, 63)).astype(float) + (rv > _f09_rvol(closeadj, 126)).astype(float) + (rv > _f09_rvol(closeadj, 252)).astype(float)) - 1.5
    dev = (rv - _f09_rvol(closeadj, 126)) / _f09_rvol(closeadj, 126).replace(0, np.nan)
    b = above + np.tanh(2.0 * dev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime dwell: consecutive days vol-rank stays in same tercile, scaled by extremity
def f09vr_f09_volatility_regime_volregimedwell_21d_base_v116_signal(closeadj):
    rk = _f09_rvol(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    terc = np.floor(rk.clip(0, 0.999) * 3.0)
    same = (terc == terc.shift(1)).astype(float)
    grp = (same == 0).cumsum()
    dwell = same.groupby(grp).cumsum()
    b = dwell * (1.0 + (rk - 0.5).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime travel: 63d range of the 21d-vol percentile rank (regime mobility)
def f09vr_f09_volatility_regime_volentropy_63d_base_v117_signal(closeadj):
    rk = _f09_rvol(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    b = rk.rolling(63, min_periods=21).max() - rk.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime disagreement: dispersion of vol-z across 21/63/126 windows
def f09vr_f09_volatility_regime_volzdispersion_21d_base_v118_signal(closeadj):
    z1 = _z(_f09_rvol(closeadj, 21), 126)
    z2 = _z(_f09_rvol(closeadj, 63), 252)
    z3 = _z(_f09_rvol(closeadj, 126), 504)
    b = pd.concat([z1, z2, z3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# calmness: 63d mean depth-shortfall of |ret| below its own 63d median
def f09vr_f09_volatility_regime_calmratio_63d_base_v119_signal(closeadj):
    r = _f09_logret(closeadj).abs()
    med = r.rolling(63, min_periods=21).median()
    calm = ((med - r) / med.replace(0, np.nan)).clip(lower=0)
    b = calm.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unstable-wide regime: 21d bandwidth z x vol-of-vol z
def f09vr_f09_volatility_regime_bbwvolofvol_21d_base_v120_signal(closeadj):
    b = _z(_f09_bbw(closeadj, 21), 252) * _z(_f09_volofvol(closeadj, 21, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol whipsaw energy: 63d sum of |vol 2nd-difference| normalized by vol
def f09vr_f09_volatility_regime_volwhipsaw_63d_base_v121_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    jag = rv.diff().diff().abs() / rv.replace(0, np.nan)
    b = jag.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol mean-reversion proxy: 63d corr of 21d vol with its own 21d lag
def f09vr_f09_volatility_regime_volhalflife_63d_base_v122_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(63, min_periods=21).corr(rv.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position instability: 63d std of 21d %B (how much price roams its band)
def f09vr_f09_volatility_regime_pctbdisp_21d_base_v123_signal(closeadj):
    pb = _f09_pctb(closeadj, 21)
    b = pb.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position trend: change in 21d %B over 21d (riding toward a band edge)
def f09vr_f09_volatility_regime_pctbtrend_21d_base_v124_signal(closeadj):
    pb = _f09_pctb(closeadj, 21) - 0.5
    b = pb - pb.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-walk persistence: fraction of 63d %B stayed above 0.8 or below 0.2 (edge-riding)
def f09vr_f09_volatility_regime_bandwalk_21d_base_v125_signal(closeadj):
    pb = _f09_pctb(closeadj, 21)
    edge = ((pb > 0.8) | (pb < 0.2)).astype(float)
    b = edge.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turbulence momentum: change in 21d turbulence over 21d
def f09vr_f09_volatility_regime_turbchg_21d_base_v126_signal(closeadj):
    t = _f09_turbulence(closeadj, 21)
    b = t - t.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turbulence persistence: fraction of 63d turbulence sat above its 252d median
def f09vr_f09_volatility_regime_turbpersist_63d_base_v127_signal(closeadj):
    t = _f09_turbulence(closeadj, 21)
    med = t.rolling(252, min_periods=63).median()
    hot = (t > med).astype(float)
    b = hot.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long vol regime curvature: normalized 2nd diff of 126d vol over 63d steps
def f09vr_f09_volatility_regime_volregimecurv_126d_base_v128_signal(closeadj):
    rv = _f09_rvol(closeadj, 126)
    c = rv - 2.0 * rv.shift(63) + rv.shift(126)
    b = c / rv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-ratio travel: 63d range (max-min) of the 42/126 vol ratio (regime swing amplitude)
def f09vr_f09_volatility_regime_rvolratiorange_42v126_base_v129_signal(closeadj):
    r = _f09_rvol(closeadj, 42) / _f09_rvol(closeadj, 126).replace(0, np.nan)
    b = r.rolling(63, min_periods=21).max() - r.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 10d vol z-scored vs its own 63d history (fast vol-regime z)
def f09vr_f09_volatility_regime_rvolzfast_10d_base_v130_signal(closeadj):
    b = _z(_f09_rvol(closeadj, 10), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 42d vol z-scored vs its own 252d history
def f09vr_f09_volatility_regime_rvolz_42v252_base_v131_signal(closeadj):
    b = _z(_f09_rvol(closeadj, 42), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turbulence clustering: 63d lag-1 autocorrelation of 21d turbulence (turbulence stickiness)
def f09vr_f09_volatility_regime_turbpersist_clust_21d_base_v132_signal(closeadj):
    t = _f09_turbulence(closeadj, 21)
    b = t.rolling(63, min_periods=21).corr(t.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion onset: prior-low compression-rank x current ratio crossing above 1
def f09vr_f09_volatility_regime_expandonset_21d_base_v133_signal(closeadj):
    r = _f09_compress_ratio(closeadj, 21, 63)
    rk = r.rolling(252, min_periods=63).rank(pct=True)
    cross = ((r > 1.0) & (r.shift(1) <= 1.0)).astype(float)
    wt = (1.0 - rk.shift(1)).clip(lower=0)
    b = (cross * wt).rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# contraction depth: mean normalized shortfall of 21d vol below its 63d median over 63d
def f09vr_f09_volatility_regime_contractdepth_63d_base_v134_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    med = rv.rolling(63, min_periods=21).median()
    sf = ((med - rv) / med.replace(0, np.nan)).clip(lower=0)
    b = sf.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-vs-overnight regime: 21d mean HL-range over 21d close-to-close vol
def f09vr_f09_volatility_regime_intraover_ratio_21d_base_v135_signal(high, low, closeadj):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = rng / _f09_rvol(closeadj, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-overnight compression: 21d mean (HL-range/close-vol ratio) over its own 126d mean (efficiency regime short/long)
def f09vr_f09_volatility_regime_intraover_compress_21d_base_v136_signal(high, low, closeadj):
    ratio = ((high - low) / closeadj.replace(0, np.nan)) / _f09_logret(closeadj).abs().replace(0, np.nan)
    ratio = ratio.replace([np.inf, -np.inf], np.nan)
    sm = ratio.rolling(21, min_periods=10).mean()
    b = sm / ratio.rolling(126, min_periods=42).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HL-range compression: 21d mean range over 63d mean range (range short/long ratio)
def f09vr_f09_volatility_regime_rangecompress_21v63_base_v137_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = rng.rolling(21, min_periods=10).mean() / rng.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HL-range compression: 42d mean range over 126d mean range
def f09vr_f09_volatility_regime_rangecompress_42v126_base_v138_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = rng.rolling(42, min_periods=21).mean() / rng.rolling(126, min_periods=42).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# single-day range expansion: today's HL-range over its 21d mean (intraday burst)
def f09vr_f09_volatility_regime_rangeexpand_21d_base_v139_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = rng / rng.rolling(21, min_periods=10).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HL-range cone: 21d mean range vs its 63d-lagged 126d-min floor (expansion off floor)
def f09vr_f09_volatility_regime_rangecone_21d_base_v140_signal(high, low, closeadj):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    floor = rng.rolling(126, min_periods=42).min().shift(63)
    b = rng / floor.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range contraction depth: log of 21d mean range vs its trailing 63d max
def f09vr_f09_volatility_regime_rangecontractmag_21d_base_v141_signal(high, low, closeadj):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    peak = rng.rolling(63, min_periods=21).max()
    b = np.log(rng.replace(0, np.nan) / peak.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range compression occupancy: where 21d mean range sits in its own 126d min-max band
def f09vr_f09_volatility_regime_rangecontractpct_21d_base_v142_signal(high, low, closeadj):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    lo = rng.rolling(126, min_periods=42).min()
    hi = rng.rolling(126, min_periods=42).max()
    b = (rng - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coiling: 21d count of narrow-range bars (narrowest of trailing 7d), depth-weighted
def f09vr_f09_volatility_regime_nrbarcount_21d_base_v143_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    isnr = (rng <= rng.rolling(7, min_periods=4).min() * 1.0001).astype(float)
    depth = (rng.rolling(7, min_periods=4).mean() - rng).clip(lower=0)
    b = (isnr * (1.0 + 20.0 * depth)).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion streak: consecutive days HL-range above its 21d median, depth-weighted
def f09vr_f09_volatility_regime_rangeexpandstreak_21d_base_v144_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    med = rng.rolling(21, min_periods=10).median()
    cond = (rng > med).astype(float)
    grp = (cond == 0).cumsum()
    streak = cond.groupby(grp).cumsum()
    depth = ((rng - med) / med.replace(0, np.nan)).clip(lower=0)
    cumd = depth.where(cond == 1, 0.0).groupby(grp).cumsum()
    b = streak + cumd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction streak: consecutive days HL-range below its 63d median, depth-weighted
def f09vr_f09_volatility_regime_rangecontractstreak_63d_base_v145_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    med = rng.rolling(63, min_periods=21).median()
    cond = (rng < med).astype(float)
    grp = (cond == 0).cumsum()
    streak = cond.groupby(grp).cumsum()
    depth = ((med - rng) / med.replace(0, np.nan)).clip(lower=0)
    cumd = depth.where(cond == 1, 0.0).groupby(grp).cumsum()
    b = streak + cumd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vs-close estimator divergence: 21d mean-range z minus 21d close-vol z
def f09vr_f09_volatility_regime_rangevolspread_21d_base_v146_signal(high, low, closeadj):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = _z(rng, 252) - _z(_f09_rvol(closeadj, 21), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-efficiency compression: 21d (Parkinson/close-vol) over 126d (Parkinson/close-vol) (efficiency regime short/long)
def f09vr_f09_volatility_regime_efficiencycompress_63d_base_v147_signal(high, low, closeadj):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    pk21 = np.sqrt((hl ** 2).rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    pk126 = np.sqrt((hl ** 2).rolling(126, min_periods=42).mean() / (4.0 * np.log(2.0)))
    e21 = pk21 / _f09_rvol(closeadj, 21).replace(0, np.nan)
    e126 = pk126 / _f09_rvol(closeadj, 126).replace(0, np.nan)
    b = e21 / e126.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday jump share: 21d max HL-range over its 63d median (range gappiness)
def f09vr_f09_volatility_regime_rangejumpshare_21d_base_v148_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = rng.rolling(21, min_periods=10).max() / rng.rolling(63, min_periods=21).median().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# contraction prevalence: 63d mean depth of HL-range below its own 21d median
def f09vr_f09_volatility_regime_rangecontractfrac_21d_base_v149_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    med = rng.rolling(21, min_periods=10).median()
    depth = ((med - rng) / med.replace(0, np.nan)).clip(lower=0)
    b = depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-overnight regime turn: change over 21d in 21d range/close-vol ratio
def f09vr_f09_volatility_regime_rangevolratiochg_21d_base_v150_signal(high, low, closeadj):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    ratio = rng / _f09_rvol(closeadj, 21).replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09vr_f09_volatility_regime_bbwcompress_42v252_base_v076_signal,
    f09vr_f09_volatility_regime_bbwcompress_21v189_base_v077_signal,
    f09vr_f09_volatility_regime_compresslog_10v63_base_v078_signal,
    f09vr_f09_volatility_regime_compressratiochg_63d_base_v079_signal,
    f09vr_f09_volatility_regime_compressdispersion_21d_base_v080_signal,
    f09vr_f09_volatility_regime_compressbreadth_21d_base_v081_signal,
    f09vr_f09_volatility_regime_compressexpcycle_126d_base_v082_signal,
    f09vr_f09_volatility_regime_compressratiovol_42v126_base_v083_signal,
    f09vr_f09_volatility_regime_bbwspreadz_21v63_base_v084_signal,
    f09vr_f09_volatility_regime_volspreadrank_42v126_base_v085_signal,
    f09vr_f09_volatility_regime_volcurv_norm_42d_base_v086_signal,
    f09vr_f09_volatility_regime_bandtouchskew_21d_base_v087_signal,
    f09vr_f09_volatility_regime_bandtouchskew_63d_base_v088_signal,
    f09vr_f09_volatility_regime_semivolconvex_126d_base_v089_signal,
    f09vr_f09_volatility_regime_semiskewchg_21d_base_v090_signal,
    f09vr_f09_volatility_regime_volkurtz_63d_base_v091_signal,
    f09vr_f09_volatility_regime_retskewz_63d_base_v092_signal,
    f09vr_f09_volatility_regime_bandexpandenergy_63d_base_v093_signal,
    f09vr_f09_volatility_regime_gapvol_21d_base_v094_signal,
    f09vr_f09_volatility_regime_bbwz_5v63_base_v095_signal,
    f09vr_f09_volatility_regime_bbwz_252v504_base_v096_signal,
    f09vr_f09_volatility_regime_bbwstate_63d_base_v097_signal,
    f09vr_f09_volatility_regime_bbwexpandstate_21d_base_v098_signal,
    f09vr_f09_volatility_regime_bbwmin_ratio_21d_base_v099_signal,
    f09vr_f09_volatility_regime_bbwacceldir_21d_base_v100_signal,
    f09vr_f09_volatility_regime_squeezecount_21d_base_v101_signal,
    f09vr_f09_volatility_regime_expandcount_21d_base_v102_signal,
    f09vr_f09_volatility_regime_doublesqueeze_21d_base_v103_signal,
    f09vr_f09_volatility_regime_preexpcompress_21d_base_v104_signal,
    f09vr_f09_volatility_regime_squeezefirepower_21d_base_v105_signal,
    f09vr_f09_volatility_regime_coiledspring_21d_base_v106_signal,
    f09vr_f09_volatility_regime_squeezeexpcombo_21d_base_v107_signal,
    f09vr_f09_volatility_regime_squeezethenexp_21d_base_v108_signal,
    f09vr_f09_volatility_regime_volaccel_63d_base_v109_signal,
    f09vr_f09_volatility_regime_voltrendsign_21d_base_v110_signal,
    f09vr_f09_volatility_regime_volmomratio_21d_base_v111_signal,
    f09vr_f09_volatility_regime_volshockgap_5d_base_v112_signal,
    f09vr_f09_volatility_regime_volcontract_pressure_21d_base_v113_signal,
    f09vr_f09_volatility_regime_volexpburst_21d_base_v114_signal,
    f09vr_f09_volatility_regime_volregimebin_21d_base_v115_signal,
    f09vr_f09_volatility_regime_volregimedwell_21d_base_v116_signal,
    f09vr_f09_volatility_regime_volentropy_63d_base_v117_signal,
    f09vr_f09_volatility_regime_volzdispersion_21d_base_v118_signal,
    f09vr_f09_volatility_regime_calmratio_63d_base_v119_signal,
    f09vr_f09_volatility_regime_bbwvolofvol_21d_base_v120_signal,
    f09vr_f09_volatility_regime_volwhipsaw_63d_base_v121_signal,
    f09vr_f09_volatility_regime_volhalflife_63d_base_v122_signal,
    f09vr_f09_volatility_regime_pctbdisp_21d_base_v123_signal,
    f09vr_f09_volatility_regime_pctbtrend_21d_base_v124_signal,
    f09vr_f09_volatility_regime_bandwalk_21d_base_v125_signal,
    f09vr_f09_volatility_regime_turbchg_21d_base_v126_signal,
    f09vr_f09_volatility_regime_turbpersist_63d_base_v127_signal,
    f09vr_f09_volatility_regime_volregimecurv_126d_base_v128_signal,
    f09vr_f09_volatility_regime_rvolratiorange_42v126_base_v129_signal,
    f09vr_f09_volatility_regime_rvolzfast_10d_base_v130_signal,
    f09vr_f09_volatility_regime_rvolz_42v252_base_v131_signal,
    f09vr_f09_volatility_regime_turbpersist_clust_21d_base_v132_signal,
    f09vr_f09_volatility_regime_expandonset_21d_base_v133_signal,
    f09vr_f09_volatility_regime_contractdepth_63d_base_v134_signal,
    f09vr_f09_volatility_regime_intraover_ratio_21d_base_v135_signal,
    f09vr_f09_volatility_regime_intraover_compress_21d_base_v136_signal,
    f09vr_f09_volatility_regime_rangecompress_21v63_base_v137_signal,
    f09vr_f09_volatility_regime_rangecompress_42v126_base_v138_signal,
    f09vr_f09_volatility_regime_rangeexpand_21d_base_v139_signal,
    f09vr_f09_volatility_regime_rangecone_21d_base_v140_signal,
    f09vr_f09_volatility_regime_rangecontractmag_21d_base_v141_signal,
    f09vr_f09_volatility_regime_rangecontractpct_21d_base_v142_signal,
    f09vr_f09_volatility_regime_nrbarcount_21d_base_v143_signal,
    f09vr_f09_volatility_regime_rangeexpandstreak_21d_base_v144_signal,
    f09vr_f09_volatility_regime_rangecontractstreak_63d_base_v145_signal,
    f09vr_f09_volatility_regime_rangevolspread_21d_base_v146_signal,
    f09vr_f09_volatility_regime_efficiencycompress_63d_base_v147_signal,
    f09vr_f09_volatility_regime_rangejumpshare_21d_base_v148_signal,
    f09vr_f09_volatility_regime_rangecontractfrac_21d_base_v149_signal,
    f09vr_f09_volatility_regime_rangevolratiochg_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_REGIME_REGISTRY_076_150 = REGISTRY


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

    print("OK f09_volatility_regime_base_076_150_claude.py: %d features pass" % n_features)
