import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives: range-based volatility estimators =====
# RANGE-BASED VOLATILITY ESTIMATORS ONLY. No close-location-in-range / CLV (f13),
# no close-to-close single-window realized-vol levels (f10).
def _f11_log_hl(high, low):
    return np.log(high.replace(0, np.nan) / low.replace(0, np.nan))


def _f11_parkinson(high, low, w):
    r2 = _f11_log_hl(high, low) ** 2
    c = 1.0 / (4.0 * np.log(2.0))
    return np.sqrt((c * r2).rolling(w, min_periods=max(2, w // 2)).mean())


def _f11_gk_term(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    return 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2


def _f11_garman_klass(open, high, low, close, w):
    t = _f11_gk_term(open, high, low, close)
    return np.sqrt(t.rolling(w, min_periods=max(2, w // 2)).mean().clip(lower=0))


def _f11_rs_term(open, high, low, close):
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    return hc * ho + lc * lo


def _f11_rogers_satchell(open, high, low, close, w):
    t = _f11_rs_term(open, high, low, close)
    return np.sqrt(t.rolling(w, min_periods=max(2, w // 2)).mean().clip(lower=0))


def _f11_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f11_atr(high, low, close, w):
    return _f11_true_range(high, low, close).rolling(
        w, min_periods=max(2, w // 2)).mean()


def _f11_overnight(open, close):
    return np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))


def _f11_intraday(open, close):
    return np.log(close.replace(0, np.nan) / open.replace(0, np.nan))


def _f11_yang_zhang(open, high, low, close, w):
    o = _f11_overnight(open, close)
    c = _f11_intraday(open, close)
    vo = ((o - o.rolling(w, min_periods=max(2, w // 2)).mean()) ** 2).rolling(
        w, min_periods=max(2, w // 2)).mean()
    vc = ((c - c.rolling(w, min_periods=max(2, w // 2)).mean()) ** 2).rolling(
        w, min_periods=max(2, w // 2)).mean()
    rs = _f11_rs_term(open, high, low, close).rolling(
        w, min_periods=max(2, w // 2)).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    return np.sqrt((vo + k * vc + (1.0 - k) * rs).clip(lower=0))


# ============================================================
# Yang-Zhang volatility, 21d (full drift-robust estimator level)
def f11re_f11_range_vol_estimators_yz_21d_base_v076_signal(open, high, low, close):
    b = _f11_yang_zhang(open, high, low, close, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang 63d relative to Parkinson 63d (full-estimator premium over pure-range).
# Ratio decorrelates from raw Parkinson-63 level.
def f11re_f11_range_vol_estimators_yz_63d_base_v077_signal(open, high, low, close):
    yz = _f11_yang_zhang(open, high, low, close, 63)
    pk = _f11_parkinson(high, low, 63)
    b = yz / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang 126d slope over a quarter relative to level (slow full-vol change rate)
def f11re_f11_range_vol_estimators_yz_126d_base_v078_signal(open, high, low, close):
    yz = _f11_yang_zhang(open, high, low, close, 126)
    b = _slope(yz, 63) / yz.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang vs Rogers-Satchell ratio (overnight+open content premium over RS)
def f11re_f11_range_vol_estimators_yzrsratio_63d_base_v079_signal(open, high, low, close):
    yz = _f11_yang_zhang(open, high, low, close, 63)
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    b = yz / rs.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang term-structure z (regime change in full-vol curve)
def f11re_f11_range_vol_estimators_yztermz_base_v080_signal(open, high, low, close):
    s = _f11_yang_zhang(open, high, low, close, 21)
    l = _f11_yang_zhang(open, high, low, close, 63)
    ratio = s / l.replace(0, np.nan)
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Overnight-gap volatility (std of overnight log returns), 21d
def f11re_f11_range_vol_estimators_overnightvol_21d_base_v081_signal(open, close):
    o = _f11_overnight(open, close)
    b = _std(o, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Overnight-gap vol 63d as share of total 63d closeadj realized vol (>21d gap share)
def f11re_f11_range_vol_estimators_overnightvol_63d_base_v082_signal(open, close, closeadj):
    o = _f11_overnight(open, close)
    gapv = _std(o, 63)
    totv = closeadj.pct_change().rolling(63, min_periods=32).std()
    b = gapv / totv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Intraday (close-to-open) volatility, 21d (session vol)
def f11re_f11_range_vol_estimators_intravol_21d_base_v083_signal(open, close):
    c = _f11_intraday(open, close)
    b = _std(c, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Overnight-gap vol regime: 63d overnight vol z-scored vs its own 252d history
# (de-trended gap-vol level; distinct from overnight/intraday and gap-share ratios)
def f11re_f11_range_vol_estimators_overintravol_base_v084_signal(open, close):
    o = _std(_f11_overnight(open, close), 63)
    b = _z(o, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Upside semi-range vol: high-open log range on up-bars, 21d (upside range energy)
def f11re_f11_range_vol_estimators_upsemirange_21d_base_v085_signal(open, high, low, close):
    up = np.log(high.replace(0, np.nan) / open.replace(0, np.nan)).clip(lower=0)
    b = np.sqrt((up ** 2).rolling(21, min_periods=11).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Downside semi-range vol: open-low log range, 21d (downside range energy)
def f11re_f11_range_vol_estimators_downsemirange_21d_base_v086_signal(open, high, low, close):
    dn = np.log(open.replace(0, np.nan) / low.replace(0, np.nan)).clip(lower=0)
    b = np.sqrt((dn ** 2).rolling(21, min_periods=11).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range semi-vol skew: up-range vs down-range asymmetry, 63d (vol asymmetry)
def f11re_f11_range_vol_estimators_semirangeskew_63d_base_v087_signal(open, high, low, close):
    up = np.log(high.replace(0, np.nan) / open.replace(0, np.nan)).clip(lower=0)
    dn = np.log(open.replace(0, np.nan) / low.replace(0, np.nan)).clip(lower=0)
    uv = np.sqrt((up ** 2).rolling(63, min_periods=32).mean())
    dv = np.sqrt((dn ** 2).rolling(63, min_periods=32).mean())
    b = (uv - dv) / (uv + dv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson coefficient-of-variation of daily log-range over 63d, change vs 63d ago
# (range-distribution roughness drift; momentum decorrelates from f13 rngcov level)
def f11re_f11_range_vol_estimators_parkcvmom_63d_base_v088_signal(high, low):
    hl = _f11_log_hl(high, low).abs()
    cv = _std(hl, 63) / _mean(hl, 63).replace(0, np.nan)
    b = cv - cv.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 5d (fast range vol), normalized by close
def f11re_f11_range_vol_estimators_parkfast_5d_base_v089_signal(high, low, close):
    pk = _f11_parkinson(high, low, 5)
    b = pk / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 5d / 21d ratio (very-short squeeze/expansion)
def f11re_f11_range_vol_estimators_parkfastterm_base_v090_signal(high, low):
    s = _f11_parkinson(high, low, 5)
    l = _f11_parkinson(high, low, 21)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR 21d vs ATR 126d ratio (true-range term structure)
def f11re_f11_range_vol_estimators_atrterm_21v126_base_v091_signal(high, low, close):
    s = _f11_atr(high, low, close, 21)
    l = _f11_atr(high, low, close, 126)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price 252d normalized by closeadj, de-meaned vs 252d trailing mean (>21d anomaly)
def f11re_f11_range_vol_estimators_atrp_252d_base_v092_signal(high, low, close, closeadj):
    atrp = _f11_atr(high, low, close, 252) / closeadj.replace(0, np.nan)
    b = atrp - atrp.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price rank vs 504d history (long true-range regime position)
def f11re_f11_range_vol_estimators_atrprank504_base_v093_signal(high, low, close, closeadj):
    atrp = _f11_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    b = _rank(atrp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range gap component fraction of TR, 63d (gap-driven true range share).
# Distinct from f13 single-day trgap (this is a 63d fraction-of-TR, not raw level).
def f11re_f11_range_vol_estimators_trgapfrac_63d_base_v094_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    hl = (high - low)
    b = _mean((tr - hl), 63) / _mean(tr, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range gap component momentum: 21d gap-in-TR fraction change vs a quarter ago
def f11re_f11_range_vol_estimators_trgapmom_base_v095_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    hl = (high - low)
    frac = _mean((tr - hl), 21) / _mean(tr, 21).replace(0, np.nan)
    b = frac - frac.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 252d normalized by closeadj, vol-cone position over 504d (long-level cone;
# structurally a min-max cone, not the short-window mean-reversion of parkmr_126d)
def f11re_f11_range_vol_estimators_parkmr_252d_base_v096_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 252) / closeadj.replace(0, np.nan)
    mn = pk.rolling(504, min_periods=252).min()
    mx = pk.rolling(504, min_periods=252).max()
    b = (pk - mn) / (mx - mn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass elevated-regime duration: fraction of the last 63d that GK 21d sat above
# its trailing 252d median, weighted by mean excess depth (count-friendly vol regime)
def f11re_f11_range_vol_estimators_gkconemid_base_v097_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    med = gk.rolling(252, min_periods=126).median()
    above = (gk > med).astype(float)
    frac = above.rolling(63, min_periods=32).mean()
    depth = (gk / med.replace(0, np.nan) - 1.0).clip(lower=0).rolling(
        63, min_periods=32).mean()
    b = frac + 2.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson-implied vol vs close-vol divergence z-scored, 63d (range-premium regime)
def f11re_f11_range_vol_estimators_parkrvdivz_63d_base_v098_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 63)
    rv = closeadj.pct_change().rolling(63, min_periods=32).std()
    ratio = pk / rv.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass vs close-vol divergence, 126d (slow range-premium level)
def f11re_f11_range_vol_estimators_gkrvdiv_126d_base_v099_signal(open, high, low, close, closeadj):
    gk = _f11_garman_klass(open, high, low, close, 126)
    rv = closeadj.pct_change().rolling(126, min_periods=63).std()
    b = gk / rv.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell drift content: RS minus Parkinson divergence, 126d (how much the
# drift-robust estimator differs from pure-range; not a close-vol divergence)
def f11re_f11_range_vol_estimators_rsrvdiv_126d_base_v100_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 126)
    pk = _f11_parkinson(high, low, 126)
    b = (rs - pk) / (rs + pk).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Vol-of-Parkinson over 126d (range-vol instability, long)
def f11re_f11_range_vol_estimators_parkvov_126d_base_v101_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    b = _std(pk, 126) / _mean(pk, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell vol-of-vol over 63d (drift-free estimator instability)
def f11re_f11_range_vol_estimators_rsvov_63d_base_v102_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 21)
    b = _std(rs, 63) / _mean(rs, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR Chande-style: signed by close direction, scaled by ATR/price, 63d
def f11re_f11_range_vol_estimators_atrdir_63d_base_v103_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    dirn = np.sign(close - close.shift(21))
    b = _mean(dirn * atrp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson skew over time: rolling skewness of daily Parkinson terms, 126d
def f11re_f11_range_vol_estimators_parkskew_126d_base_v104_signal(high, low):
    r2 = _f11_log_hl(high, low) ** 2
    b = r2.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range kurtosis: fat tails in daily true-range distribution, 126d
def f11re_f11_range_vol_estimators_trkurt_126d_base_v105_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    b = tr.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 90th-percentile TR vs median TR over 63d (range tail ratio)
def f11re_f11_range_vol_estimators_trq90_63d_base_v106_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    q90 = tr.rolling(63, min_periods=32).quantile(0.9)
    med = tr.rolling(63, min_periods=32).median()
    b = q90 / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 10th-percentile (calm-day) TR vs median over 63d (floor-vol ratio)
def f11re_f11_range_vol_estimators_trq10_63d_base_v107_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    q10 = tr.rolling(63, min_periods=32).quantile(0.1)
    med = tr.rolling(63, min_periods=32).median()
    b = q10 / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range interquartile spread relative to median over 63d (range dispersion shape)
def f11re_f11_range_vol_estimators_triqr_63d_base_v108_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    q75 = tr.rolling(63, min_periods=32).quantile(0.75)
    q25 = tr.rolling(63, min_periods=32).quantile(0.25)
    med = tr.rolling(63, min_periods=32).median()
    b = (q75 - q25) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol-cone position over 504d (long cone level)
def f11re_f11_range_vol_estimators_parkcone504_base_v109_signal(high, low):
    pk = _f11_parkinson(high, low, 63)
    mn = pk.rolling(504, min_periods=252).min()
    mx = pk.rolling(504, min_periods=252).max()
    b = (pk - mn) / (mx - mn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang vol-cone position over 252d (full-estimator cone level)
def f11re_f11_range_vol_estimators_yzcone_252d_base_v110_signal(open, high, low, close):
    yz = _f11_yang_zhang(open, high, low, close, 21)
    mn = yz.rolling(252, min_periods=126).min()
    mx = yz.rolling(252, min_periods=126).max()
    b = (yz - mn) / (mx - mn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range expansion burst: count entries above 2x median TR over 63d (shock count)
def f11re_f11_range_vol_estimators_trburst_63d_base_v111_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    med = tr.rolling(63, min_periods=32).median()
    shock = (tr > 2.0 * med).astype(float)
    entries = ((shock == 1) & (shock.shift(1) == 0)).astype(float)
    rate = entries.rolling(63, min_periods=32).sum()
    depth = (tr / med.replace(0, np.nan) - 2.0).clip(lower=0).rolling(
        21, min_periods=11).mean()
    b = rate + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson regime distance: current 21d Parkinson vs its 252d mean, in std units
def f11re_f11_range_vol_estimators_parkregime_base_v112_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    b = (pk - _mean(pk, 252)) / _std(pk, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price acceleration: 2nd difference of 21d ATR/price (range-vol curvature)
def f11re_f11_range_vol_estimators_atrpaccel_base_v113_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = atrp - 2.0 * atrp.shift(21) + atrp.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass momentum over a quarter (medium GK expansion rate, quarter horizon)
def f11re_f11_range_vol_estimators_gkmom_q_base_v114_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 63)
    b = gk / gk.shift(63).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Open-jump variance vs Garman-Klass total, 63d (overnight share of GK-style vol).
# Uses GK denominator (not YZ) so it decorrelates from the GKYZ gapshare in file 1.
def f11re_f11_range_vol_estimators_gkgapshare_base_v115_signal(open, high, low, close):
    o = _f11_overnight(open, close) ** 2
    gkt = _f11_gk_term(open, high, low, close).clip(lower=0)
    b = o.rolling(63, min_periods=32).mean() / (
        o + gkt).rolling(63, min_periods=32).mean().replace(0, np.nan)
    # subtract its own slow mean so this is a regime, not the file-1 raw share level
    b = b - b.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range efficiency: net move vs total range traveled, 21d (trend vs chop in vol)
def f11re_f11_range_vol_estimators_rangeff_21d_base_v116_signal(high, low, close):
    net = (close - close.shift(21)).abs()
    path = (high - low).rolling(21, min_periods=11).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range efficiency 63d normalized by closeadj path (>21d)
def f11re_f11_range_vol_estimators_rangeff_63d_base_v117_signal(high, low, closeadj):
    net = (closeadj - closeadj.shift(63)).abs()
    path = (high - low).rolling(63, min_periods=32).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson-to-ATR ratio (RMS range vs mean true range, fat-tail indicator), 63d
def f11re_f11_range_vol_estimators_parkatrratio_base_v118_signal(high, low, close):
    pk = _f11_parkinson(high, low, 63) * close
    atr = _f11_atr(high, low, close, 63)
    b = pk / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Close-to-close vs Parkinson variance-ratio momentum, 126d (range-efficiency shift)
def f11re_f11_range_vol_estimators_ccparkvr_126d_base_v119_signal(high, low, closeadj):
    cc = closeadj.pct_change().rolling(126, min_periods=63).std()
    pk = _f11_parkinson(high, low, 126)
    vr = (cc / pk.replace(0, np.nan)) ** 2
    b = vr - vr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 126d slope over a half-year relative to level (slow GK trend rate)
def f11re_f11_range_vol_estimators_gkslope_63d_base_v120_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 126)
    b = _slope(gk, 126) / gk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell EWMA RELATIVE to Parkinson EWMA (persistent drift-free premium).
# Ratio decorrelates from the Parkinson EWMA level in file 1.
def f11re_f11_range_vol_estimators_rsewma_base_v121_signal(open, high, low, close):
    t = _f11_rs_term(open, high, low, close).clip(lower=0)
    rs_e = np.sqrt(t.ewm(span=42, min_periods=21).mean())
    r2 = _f11_log_hl(high, low) ** 2
    pk_e = np.sqrt((1.0 / (4.0 * np.log(2.0)) * r2).ewm(span=42, min_periods=21).mean())
    b = rs_e / pk_e.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass displacement from EWMA RELATIVE to level (GK vol shock, normalized).
# Normalizing by level decorrelates from the Parkinson absolute shock in file 1.
def f11re_f11_range_vol_estimators_gkdisp_base_v122_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    ewm = gk.ewm(span=63, min_periods=21).mean()
    b = (gk - ewm) / ewm.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range compression-then-expansion: low 126d Parkinson followed by 5d surge (squeeze pop)
def f11re_f11_range_vol_estimators_squeezepop_base_v123_signal(high, low):
    pk21 = _f11_parkinson(high, low, 21)
    pk126 = _f11_parkinson(high, low, 126)
    compressed = (pk126 - pk21).clip(lower=0) / pk126.replace(0, np.nan)
    pk5 = _f11_parkinson(high, low, 5)
    pop = (pk5 / pk21.replace(0, np.nan) - 1.0).clip(lower=0)
    b = compressed.shift(5) * pop
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson range autocorrelation: persistence of daily log-range, 63d
def f11re_f11_range_vol_estimators_rangeautocorr_base_v124_signal(high, low):
    hl = _f11_log_hl(high, low).abs()
    def _ac(a):
        x = a[:-1]
        y = a[1:]
        if np.std(x) == 0 or np.std(y) == 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    b = hl.rolling(63, min_periods=40).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range trend: slope of 21d ATR/price over 63d
def f11re_f11_range_vol_estimators_atrtrend_base_v125_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _slope(atrp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 126d normalized by closeadj, percentile rank vs 504d (>21d regime)
def f11re_f11_range_vol_estimators_parkrank504_base_v126_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 126) / closeadj.replace(0, np.nan)
    b = _rank(pk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass-Yang-Zhang full estimator (gap + GK), 21d, normalized by close (gap-vol level)
def f11re_f11_range_vol_estimators_gkyzlevel_base_v127_signal(open, high, low, close):
    o = _f11_overnight(open, close)
    t = o ** 2 + _f11_gk_term(open, high, low, close)
    gkyz = np.sqrt(t.rolling(21, min_periods=11).mean().clip(lower=0))
    b = gkyz / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass-Yang-Zhang vs Yang-Zhang ratio, 63d (gap-weighting vs drift-robust mix)
def f11re_f11_range_vol_estimators_gkyzyz_63d_base_v128_signal(open, high, low, close):
    o = _f11_overnight(open, close)
    t = o ** 2 + _f11_gk_term(open, high, low, close)
    gkyz = np.sqrt(t.rolling(63, min_periods=32).mean().clip(lower=0))
    yz = _f11_yang_zhang(open, high, low, close, 63)
    b = gkyz / yz.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Intraday-session vol vs Parkinson range vol, 63d (close-to-open vs hi-lo content)
def f11re_f11_range_vol_estimators_intrapkratio_base_v129_signal(open, high, low, close):
    iv = _std(_f11_intraday(open, close), 63)
    pk = _f11_parkinson(high, low, 63)
    b = iv / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass-Yang-Zhang vs Parkinson divergence, 126d (gap content over long horizon)
def f11re_f11_range_vol_estimators_gkyzpkdiv_base_v130_signal(open, high, low, close):
    o = _f11_overnight(open, close)
    t = o ** 2 + _f11_gk_term(open, high, low, close)
    gkyz = np.sqrt(t.rolling(126, min_periods=63).mean().clip(lower=0))
    pk = _f11_parkinson(high, low, 126)
    b = gkyz / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range vol acceleration regime: sign of 21d minus 63d Parkinson, magnitude-weighted
def f11re_f11_range_vol_estimators_parkaccelreg_base_v131_signal(high, low):
    s = _f11_parkinson(high, low, 21)
    l = _f11_parkinson(high, low, 63)
    diff = (s - l) / l.replace(0, np.nan)
    b = np.sign(diff) * np.sqrt(diff.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price vs overnight-gap vol interaction (range vs gap dominance), 63d
def f11re_f11_range_vol_estimators_atrgapint_base_v132_signal(open, high, low, close):
    atrp = _f11_atr(high, low, close, 63) / close.replace(0, np.nan)
    gapv = _std(_f11_overnight(open, close), 63)
    b = atrp - gapv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range-vol persistence: avg positive excess of Parkinson 5d above its 63d median
def f11re_f11_range_vol_estimators_parkpersist_base_v133_signal(high, low):
    pk5 = _f11_parkinson(high, low, 5)
    med = pk5.rolling(63, min_periods=32).median()
    excess = (pk5 / med.replace(0, np.nan) - 1.0).clip(lower=0)
    b = excess.rolling(63, min_periods=32).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass normalized by closeadj, percentile rank vs 252d (>21d GK regime, medium)
def f11re_f11_range_vol_estimators_gkrank252_base_v134_signal(open, high, low, close, closeadj):
    gk = _f11_garman_klass(open, high, low, close, 126) / closeadj.replace(0, np.nan)
    b = _rank(gk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range z signed by gap direction (vol shock with overnight sign), 21d
def f11re_f11_range_vol_estimators_trzgapsign_base_v135_signal(open, high, low, close):
    tr = _f11_true_range(high, low, close)
    z = _z(tr, 63)
    gapsign = np.sign(open - close.shift(1))
    b = _mean(z * gapsign, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass tanh-bounded month-over-month log change (squashed GK momentum)
def f11re_f11_range_vol_estimators_gktanhreg_base_v136_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    chg = np.log(gk.replace(0, np.nan) / gk.shift(21).replace(0, np.nan))
    b = np.tanh(3.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson range vol vs close-to-close abs-move ratio, 126d (range-vs-net-move)
def f11re_f11_range_vol_estimators_rngccratio_base_v137_signal(high, low, closeadj):
    pk = _mean(_f11_parkinson(high, low, 21), 126)
    cc = closeadj.pct_change().abs().rolling(126, min_periods=63).mean()
    b = pk / cc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell normalized rank vs 252d (drift-free regime, medium)
def f11re_f11_range_vol_estimators_rsrank_126d_base_v138_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 21)
    b = _rank(rs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Vol-curve curvature: Parkinson 5/21/63 second difference (term-structure shape)
def f11re_f11_range_vol_estimators_parkcurve_shape_base_v139_signal(high, low):
    p5 = _f11_parkinson(high, low, 5)
    p21 = _f11_parkinson(high, low, 21)
    p63 = _f11_parkinson(high, low, 63)
    b = (p5 - 2.0 * p21 + p63) / p21.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR expansion streak scaled by depth: consecutive 5d-ATR > 21d-ATR days
def f11re_f11_range_vol_estimators_atrexpstreak_base_v140_signal(high, low, close):
    short = _f11_atr(high, low, close, 5)
    long = _f11_atr(high, low, close, 21)
    ratio = short / long.replace(0, np.nan)
    hot = (ratio > 1.0).astype(float)
    grp = (hot == 0).cumsum()
    run = hot.groupby(grp).cumsum()
    b = run * (ratio - 1.0).clip(lower=0).rolling(5, min_periods=2).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell term-structure z (regime change in drift-free vol curve)
def f11re_f11_range_vol_estimators_rstermz_base_v141_signal(open, high, low, close):
    s = _f11_rogers_satchell(open, high, low, close, 21)
    l = _f11_rogers_satchell(open, high, low, close, 63)
    ratio = s / l.replace(0, np.nan)
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Realized-vs-range gap z: (Parkinson - close vol) z-scored, 63d (range premium regime)
def f11re_f11_range_vol_estimators_parkrvgapz_base_v142_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 63)
    rv = closeadj.pct_change().rolling(63, min_periods=32).std()
    spr = pk - rv
    b = _z(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up-day vs down-day range asymmetry (range bigger on down days = panic), 63d
def f11re_f11_range_vol_estimators_updownrange_base_v143_signal(high, low, close):
    hl = _f11_log_hl(high, low)
    up = (close > close.shift(1))
    up_r = hl.where(up).rolling(63, min_periods=20).mean()
    dn_r = hl.where(~up).rolling(63, min_periods=20).mean()
    b = (dn_r - up_r) / (dn_r + up_r).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Long-horizon Yang-Zhang vs Garman-Klass ratio, 252d (full vs gap+close, >21d)
def f11re_f11_range_vol_estimators_yzgk_252d_base_v144_signal(open, high, low, close):
    yz = _f11_yang_zhang(open, high, low, close, 252)
    gk = _f11_garman_klass(open, high, low, close, 252)
    b = yz / gk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 63d / GK 63d / RS 63d max-min dispersion (estimator disagreement breadth)
def f11re_f11_range_vol_estimators_estdisp_63d_base_v145_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 63)
    gk = _f11_garman_klass(open, high, low, close, 63)
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    stacked = pd.concat([pk, gk, rs], axis=1)
    b = (stacked.max(axis=1) - stacked.min(axis=1)) / stacked.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range concentration: max single-day TR over 63d as fraction of window sum
def f11re_f11_range_vol_estimators_trconcentration_base_v146_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    s = tr.rolling(63, min_periods=32).sum()
    mx = tr.rolling(63, min_periods=32).max()
    b = mx / s.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price slow EWMA, displacement of 21d level from it (true-range regime shock)
def f11re_f11_range_vol_estimators_atrpewma_base_v147_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    ewm = atrp.ewm(span=126, min_periods=42).mean()
    b = atrp / ewm.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Overnight gap vol vs Garman-Klass intraday vol ratio (gap-vs-GK vol mix), 63d.
# Uses GK denominator (not Parkinson) to decorrelate from any gap/range mix in file 1.
def f11re_f11_range_vol_estimators_gapgkmix_base_v148_signal(open, high, low, close):
    gapv = _std(_f11_overnight(open, close), 63)
    gk = _f11_garman_klass(open, high, low, close, 63)
    b = gapv / gk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range-vol drawdown: current 21d Parkinson vs its 126d max (calm relative to peak)
def f11re_f11_range_vol_estimators_parkdd_base_v149_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    pk_peak = pk.rolling(126, min_periods=63).max()
    b = pk / pk_peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Combined range-vol composite: ATR/price x (1 - range-efficiency) (vol with chop quality)
def f11re_f11_range_vol_estimators_volqualcomp_base_v150_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    net = (close - close.shift(21)).abs()
    path = (high - low).rolling(21, min_periods=11).sum()
    eff = net / path.replace(0, np.nan)
    b = atrp * (1.0 - eff)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11re_f11_range_vol_estimators_yz_21d_base_v076_signal,
    f11re_f11_range_vol_estimators_yz_63d_base_v077_signal,
    f11re_f11_range_vol_estimators_yz_126d_base_v078_signal,
    f11re_f11_range_vol_estimators_yzrsratio_63d_base_v079_signal,
    f11re_f11_range_vol_estimators_yztermz_base_v080_signal,
    f11re_f11_range_vol_estimators_overnightvol_21d_base_v081_signal,
    f11re_f11_range_vol_estimators_overnightvol_63d_base_v082_signal,
    f11re_f11_range_vol_estimators_intravol_21d_base_v083_signal,
    f11re_f11_range_vol_estimators_overintravol_base_v084_signal,
    f11re_f11_range_vol_estimators_upsemirange_21d_base_v085_signal,
    f11re_f11_range_vol_estimators_downsemirange_21d_base_v086_signal,
    f11re_f11_range_vol_estimators_semirangeskew_63d_base_v087_signal,
    f11re_f11_range_vol_estimators_parkcvmom_63d_base_v088_signal,
    f11re_f11_range_vol_estimators_parkfast_5d_base_v089_signal,
    f11re_f11_range_vol_estimators_parkfastterm_base_v090_signal,
    f11re_f11_range_vol_estimators_atrterm_21v126_base_v091_signal,
    f11re_f11_range_vol_estimators_atrp_252d_base_v092_signal,
    f11re_f11_range_vol_estimators_atrprank504_base_v093_signal,
    f11re_f11_range_vol_estimators_trgapfrac_63d_base_v094_signal,
    f11re_f11_range_vol_estimators_trgapmom_base_v095_signal,
    f11re_f11_range_vol_estimators_parkmr_252d_base_v096_signal,
    f11re_f11_range_vol_estimators_gkconemid_base_v097_signal,
    f11re_f11_range_vol_estimators_parkrvdivz_63d_base_v098_signal,
    f11re_f11_range_vol_estimators_gkrvdiv_126d_base_v099_signal,
    f11re_f11_range_vol_estimators_rsrvdiv_126d_base_v100_signal,
    f11re_f11_range_vol_estimators_parkvov_126d_base_v101_signal,
    f11re_f11_range_vol_estimators_rsvov_63d_base_v102_signal,
    f11re_f11_range_vol_estimators_atrdir_63d_base_v103_signal,
    f11re_f11_range_vol_estimators_parkskew_126d_base_v104_signal,
    f11re_f11_range_vol_estimators_trkurt_126d_base_v105_signal,
    f11re_f11_range_vol_estimators_trq90_63d_base_v106_signal,
    f11re_f11_range_vol_estimators_trq10_63d_base_v107_signal,
    f11re_f11_range_vol_estimators_triqr_63d_base_v108_signal,
    f11re_f11_range_vol_estimators_parkcone504_base_v109_signal,
    f11re_f11_range_vol_estimators_yzcone_252d_base_v110_signal,
    f11re_f11_range_vol_estimators_trburst_63d_base_v111_signal,
    f11re_f11_range_vol_estimators_parkregime_base_v112_signal,
    f11re_f11_range_vol_estimators_atrpaccel_base_v113_signal,
    f11re_f11_range_vol_estimators_gkmom_q_base_v114_signal,
    f11re_f11_range_vol_estimators_gkgapshare_base_v115_signal,
    f11re_f11_range_vol_estimators_rangeff_21d_base_v116_signal,
    f11re_f11_range_vol_estimators_rangeff_63d_base_v117_signal,
    f11re_f11_range_vol_estimators_parkatrratio_base_v118_signal,
    f11re_f11_range_vol_estimators_ccparkvr_126d_base_v119_signal,
    f11re_f11_range_vol_estimators_gkslope_63d_base_v120_signal,
    f11re_f11_range_vol_estimators_rsewma_base_v121_signal,
    f11re_f11_range_vol_estimators_gkdisp_base_v122_signal,
    f11re_f11_range_vol_estimators_squeezepop_base_v123_signal,
    f11re_f11_range_vol_estimators_rangeautocorr_base_v124_signal,
    f11re_f11_range_vol_estimators_atrtrend_base_v125_signal,
    f11re_f11_range_vol_estimators_parkrank504_base_v126_signal,
    f11re_f11_range_vol_estimators_gkyzlevel_base_v127_signal,
    f11re_f11_range_vol_estimators_gkyzyz_63d_base_v128_signal,
    f11re_f11_range_vol_estimators_intrapkratio_base_v129_signal,
    f11re_f11_range_vol_estimators_gkyzpkdiv_base_v130_signal,
    f11re_f11_range_vol_estimators_parkaccelreg_base_v131_signal,
    f11re_f11_range_vol_estimators_atrgapint_base_v132_signal,
    f11re_f11_range_vol_estimators_parkpersist_base_v133_signal,
    f11re_f11_range_vol_estimators_gkrank252_base_v134_signal,
    f11re_f11_range_vol_estimators_trzgapsign_base_v135_signal,
    f11re_f11_range_vol_estimators_gktanhreg_base_v136_signal,
    f11re_f11_range_vol_estimators_rngccratio_base_v137_signal,
    f11re_f11_range_vol_estimators_rsrank_126d_base_v138_signal,
    f11re_f11_range_vol_estimators_parkcurve_shape_base_v139_signal,
    f11re_f11_range_vol_estimators_atrexpstreak_base_v140_signal,
    f11re_f11_range_vol_estimators_rstermz_base_v141_signal,
    f11re_f11_range_vol_estimators_parkrvgapz_base_v142_signal,
    f11re_f11_range_vol_estimators_updownrange_base_v143_signal,
    f11re_f11_range_vol_estimators_yzgk_252d_base_v144_signal,
    f11re_f11_range_vol_estimators_estdisp_63d_base_v145_signal,
    f11re_f11_range_vol_estimators_trconcentration_base_v146_signal,
    f11re_f11_range_vol_estimators_atrpewma_base_v147_signal,
    f11re_f11_range_vol_estimators_gapgkmix_base_v148_signal,
    f11re_f11_range_vol_estimators_parkdd_base_v149_signal,
    f11re_f11_range_vol_estimators_volqualcomp_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RANGE_VOL_ESTIMATORS_REGISTRY_076_150 = REGISTRY


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

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

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

    print("OK f11_range_vol_estimators_base_076_150_claude: %d features pass" % n_features)
