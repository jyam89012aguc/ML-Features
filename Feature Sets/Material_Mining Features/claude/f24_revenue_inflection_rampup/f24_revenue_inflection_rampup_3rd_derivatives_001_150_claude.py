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
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (revenue inflection / ramp-up) =====
def _f24_growth(rev, w):
    return np.log(rev.replace(0, np.nan) / rev.shift(w).replace(0, np.nan))


def _f24_ramp_from_low(rev, w):
    lo = rev.rolling(w, min_periods=max(1, w // 2)).min()
    return rev / lo.replace(0, np.nan) - 1.0


def _f24_accel(rev, w):
    g_s = np.log(rev.replace(0, np.nan) / rev.shift(w).replace(0, np.nan))
    g_l = np.log(rev.shift(w).replace(0, np.nan) / rev.shift(2 * w).replace(0, np.nan))
    return g_s - g_l


def _f24_gp_margin(gp, rev):
    return gp / rev.replace(0, np.nan)


def _f24_stability(rev, w):
    g = rev.pct_change()
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)



# ============================================================
# Each feature builds a ramp/inflection base inline, then takes its
# 2nd math derivative (jerk) over a window matched to the base window.


# slope of 63d log-growth of revenue (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_revgrow_63d_jerk_v001_signal(revenue):
    base = _f24_growth(revenue, 63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d log-growth of revenue (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_revgrow_126d_jerk_v002_signal(revenue):
    base = _f24_growth(revenue, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d log-growth of revenue (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_revgrow_252d_jerk_v003_signal(revenue):
    base = _f24_growth(revenue, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d log-growth of revenueusd (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_usdgrow_63d_jerk_v004_signal(revenueusd):
    base = _f24_growth(revenueusd, 63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d log-growth of revenueusd (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_usdgrow_126d_jerk_v005_signal(revenueusd):
    base = _f24_growth(revenueusd, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d log-growth of revenueusd (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_usdgrow_252d_jerk_v006_signal(revenueusd):
    base = _f24_growth(revenueusd, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d log-growth of gp (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_gpgrow_63d_jerk_v007_signal(gp):
    base = _f24_growth(gp, 63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d log-growth of gp (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_gpgrow_126d_jerk_v008_signal(gp):
    base = _f24_growth(gp, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d log-growth of gp (ramp velocity)
def f24ri_f24_revenue_inflection_rampup_gpgrow_252d_jerk_v009_signal(gp):
    base = _f24_growth(gp, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue lift off its 252d trough
def f24ri_f24_revenue_inflection_rampup_rampfromlow_252d_jerk_v010_signal(revenue):
    base = _f24_ramp_from_low(revenue, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue lift off its 504d trough
def f24ri_f24_revenue_inflection_rampup_rampfromlow_504d_jerk_v011_signal(revenue):
    base = _f24_ramp_from_low(revenue, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp lift off its 252d trough
def f24ri_f24_revenue_inflection_rampup_gprampfromlow_252d_jerk_v012_signal(gp):
    base = _f24_ramp_from_low(gp, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp lift off its 504d trough
def f24ri_f24_revenue_inflection_rampup_gprampfromlow_504d_jerk_v013_signal(gp):
    base = _f24_ramp_from_low(gp, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd lift off its 252d trough
def f24ri_f24_revenue_inflection_rampup_usdrampfromlow_252d_jerk_v014_signal(revenueusd):
    base = _f24_ramp_from_low(revenueusd, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log lift of revenue above its 1260d minimum
def f24ri_f24_revenue_inflection_rampup_drawup_1260d_jerk_v015_signal(revenue):
    lo = _rmin(revenue, 1260)
    base = np.log(revenue.replace(0, np.nan) / lo.replace(0, np.nan))
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log lift of gp above its 1260d minimum
def f24ri_f24_revenue_inflection_rampup_gpdrawup_1260d_jerk_v016_signal(gp):
    lo = _rmin(gp, 1260)
    base = np.log(gp.replace(0, np.nan) / lo.replace(0, np.nan))
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log lift of revenueusd above its 1260d minimum
def f24ri_f24_revenue_inflection_rampup_usddrawup_1260d_jerk_v017_signal(revenueusd):
    lo = _rmin(revenueusd, 1260)
    base = np.log(revenueusd.replace(0, np.nan) / lo.replace(0, np.nan))
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue position within its 504d range
def f24ri_f24_revenue_inflection_rampup_rangepos_504d_jerk_v018_signal(revenue):
    hi = _rmax(revenue, 504)
    lo = _rmin(revenue, 504)
    base = (revenue - lo) / (hi - lo).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue position within its 1260d range
def f24ri_f24_revenue_inflection_rampup_rangepos_1260d_jerk_v019_signal(revenue):
    hi = _rmax(revenue, 1260)
    lo = _rmin(revenue, 1260)
    base = (revenue - lo) / (hi - lo).replace(0, np.nan)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp position within its 504d range
def f24ri_f24_revenue_inflection_rampup_gprangepos_504d_jerk_v020_signal(gp):
    hi = _rmax(gp, 504)
    lo = _rmin(gp, 504)
    base = (gp - lo) / (hi - lo).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd position within its 504d range
def f24ri_f24_revenue_inflection_rampup_usdrangepos_504d_jerk_v021_signal(revenueusd):
    hi = _rmax(revenueusd, 504)
    lo = _rmin(revenueusd, 504)
    base = (revenueusd - lo) / (hi - lo).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue ramp-acceleration level (63d)
def f24ri_f24_revenue_inflection_rampup_accel_63d_jerk_v022_signal(revenue):
    base = _f24_accel(revenue, 63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue ramp-acceleration level (126d)
def f24ri_f24_revenue_inflection_rampup_accel_126d_jerk_v023_signal(revenue):
    base = _f24_accel(revenue, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue ramp-acceleration level (252d)
def f24ri_f24_revenue_inflection_rampup_accel_252d_jerk_v024_signal(revenue):
    base = _f24_accel(revenue, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp ramp-acceleration level (63d)
def f24ri_f24_revenue_inflection_rampup_gpaccel_63d_jerk_v025_signal(gp):
    base = _f24_accel(gp, 63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp ramp-acceleration level (126d)
def f24ri_f24_revenue_inflection_rampup_gpaccel_126d_jerk_v026_signal(gp):
    base = _f24_accel(gp, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd ramp-acceleration level (126d)
def f24ri_f24_revenue_inflection_rampup_usdaccel_126d_jerk_v027_signal(revenueusd):
    base = _f24_accel(revenueusd, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue growth-stability (126d)
def f24ri_f24_revenue_inflection_rampup_stability_126d_jerk_v028_signal(revenue):
    base = _f24_stability(revenue, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue growth-stability (252d)
def f24ri_f24_revenue_inflection_rampup_stability_252d_jerk_v029_signal(revenue):
    base = _f24_stability(revenue, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp growth-stability (252d)
def f24ri_f24_revenue_inflection_rampup_gpstability_252d_jerk_v030_signal(gp):
    base = _f24_stability(gp, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd growth-stability (252d)
def f24ri_f24_revenue_inflection_rampup_usdstability_252d_jerk_v031_signal(revenueusd):
    base = _f24_stability(revenueusd, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gross margin gp/revenue (margin velocity)
def f24ri_f24_revenue_inflection_rampup_gpmargin_base_jerk_v032_signal(gp, revenue):
    base = _f24_gp_margin(gp, revenue)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed gross margin (persistent margin trend)
def f24ri_f24_revenue_inflection_rampup_gpmarginsm_base_jerk_v033_signal(gp, revenue):
    base = _f24_gp_margin(gp, revenue).ewm(span=63, min_periods=21).mean()
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue z-score vs its 252d history
def f24ri_f24_revenue_inflection_rampup_revz_252d_jerk_v034_signal(revenue):
    base = _z(revenue, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue z-score vs its 504d history
def f24ri_f24_revenue_inflection_rampup_revz_504d_jerk_v035_signal(revenue):
    base = _z(revenue, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp z-score vs its 252d history
def f24ri_f24_revenue_inflection_rampup_gpz_252d_jerk_v036_signal(gp):
    base = _z(gp, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd z-score vs its 252d history
def f24ri_f24_revenue_inflection_rampup_usdz_252d_jerk_v037_signal(revenueusd):
    base = _z(revenueusd, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d-growth percentile rank of revenue
def f24ri_f24_revenue_inflection_rampup_growrank_504d_jerk_v038_signal(revenue):
    g = _f24_growth(revenue, 252)
    base = _rank(g, 504)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue level percentile rank (504d)
def f24ri_f24_revenue_inflection_rampup_levelrank_504d_jerk_v039_signal(revenue):
    base = _rank(revenue, 504)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue level percentile rank (1260d)
def f24ri_f24_revenue_inflection_rampup_levelrank_1260d_jerk_v040_signal(revenue):
    base = _rank(revenue, 1260)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp level percentile rank (1260d)
def f24ri_f24_revenue_inflection_rampup_gplevelrank_1260d_jerk_v041_signal(gp):
    base = _rank(gp, 1260)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 63d/252d mean ratio (ramp momentum)
def f24ri_f24_revenue_inflection_rampup_meanratio_63v252d_jerk_v042_signal(revenue):
    base = _mean(revenue, 63) / _mean(revenue, 252).replace(0, np.nan) - 1.0
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 21d/126d mean ratio (ramp momentum)
def f24ri_f24_revenue_inflection_rampup_meanratio_21v126d_jerk_v043_signal(revenue):
    base = _mean(revenue, 21) / _mean(revenue, 126).replace(0, np.nan) - 1.0
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 63d/252d mean ratio (ramp momentum)
def f24ri_f24_revenue_inflection_rampup_gpmeanratio_63v252d_jerk_v044_signal(gp):
    base = _mean(gp, 63) / _mean(gp, 252).replace(0, np.nan) - 1.0
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd 63d/252d mean ratio (ramp momentum)
def f24ri_f24_revenue_inflection_rampup_usdmeanratio_63v252d_jerk_v045_signal(revenueusd):
    base = _mean(revenueusd, 63) / _mean(revenueusd, 252).replace(0, np.nan) - 1.0
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue vs its 252d mean (level-above-baseline velocity)
def f24ri_f24_revenue_inflection_rampup_vsmean_252d_jerk_v046_signal(revenue):
    base = revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue vs its 504d mean (level-above-baseline velocity)
def f24ri_f24_revenue_inflection_rampup_vsmean_504d_jerk_v047_signal(revenue):
    base = revenue / _mean(revenue, 504).replace(0, np.nan) - 1.0
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp vs its 252d mean (level-above-baseline velocity)
def f24ri_f24_revenue_inflection_rampup_gpvsmean_252d_jerk_v048_signal(gp):
    base = gp / _mean(gp, 252).replace(0, np.nan) - 1.0
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue convexity (63d minus 252d growth)
def f24ri_f24_revenue_inflection_rampup_convexity_63v252d_jerk_v049_signal(revenue):
    base = _f24_growth(revenue, 63) - _f24_growth(revenue, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp convexity (63d minus 252d growth)
def f24ri_f24_revenue_inflection_rampup_gpconvexity_63v252d_jerk_v050_signal(gp):
    base = _f24_growth(gp, 63) - _f24_growth(gp, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd convexity (63d minus 252d growth)
def f24ri_f24_revenue_inflection_rampup_usdconvexity_63v252d_jerk_v051_signal(revenueusd):
    base = _f24_growth(revenueusd, 63) - _f24_growth(revenueusd, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of negative coeff-of-variation of revenue (252d smoothness)
def f24ri_f24_revenue_inflection_rampup_negcv_252d_jerk_v052_signal(revenue):
    base = -(_std(revenue, 252) / _mean(revenue, 252).replace(0, np.nan))
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of negative coeff-of-variation of revenue (126d smoothness)
def f24ri_f24_revenue_inflection_rampup_negcv_126d_jerk_v053_signal(revenue):
    base = -(_std(revenue, 126) / _mean(revenue, 126).replace(0, np.nan))
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of negative coeff-of-variation of gp (252d smoothness)
def f24ri_f24_revenue_inflection_rampup_gpnegcv_252d_jerk_v054_signal(gp):
    base = -(_std(gp, 252) / _mean(gp, 252).replace(0, np.nan))
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue growth per unit vol (126d risk-adj ramp)
def f24ri_f24_revenue_inflection_rampup_growriskadj_126d_jerk_v055_signal(revenue):
    g = _f24_growth(revenue, 126)
    rng = (_rmax(revenue, 126) - _rmin(revenue, 126)) / _mean(revenue, 126).replace(0, np.nan)
    base = g / rng.replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp growth per unit vol (126d risk-adj ramp)
def f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_126d_jerk_v056_signal(gp):
    g = _f24_growth(gp, 126)
    rng = (_rmax(gp, 126) - _rmin(gp, 126)) / _mean(gp, 126).replace(0, np.nan)
    base = g / rng.replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd growth per unit vol (252d risk-adj ramp)
def f24ri_f24_revenue_inflection_rampup_usdgrowriskadj_252d_jerk_v057_signal(revenueusd):
    g = _f24_growth(revenueusd, 252)
    rng = (_rmax(revenueusd, 252) - _rmin(revenueusd, 252)) / _mean(revenueusd, 252).replace(0, np.nan)
    base = g / rng.replace(0, np.nan)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d gross-margin expansion (margin-improvement velocity)
def f24ri_f24_revenue_inflection_rampup_gpmarginexp_252d_jerk_v058_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    base = m - m.shift(252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d gross-margin expansion
def f24ri_f24_revenue_inflection_rampup_gpmarginexp_126d_jerk_v059_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    base = m - m.shift(126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-252d revenue above its 252d mean (ramp-streak velocity)
def f24ri_f24_revenue_inflection_rampup_posstreak_252d_jerk_v060_signal(revenue):
    on = (revenue > _mean(revenue, 252)).astype(float)
    base = on.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-252d gp above its 252d median
def f24ri_f24_revenue_inflection_rampup_gpabovemed_252d_jerk_v061_signal(gp):
    med = gp.rolling(252, min_periods=126).median()
    on = (gp > med).astype(float)
    base = on.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of new-252d-high frequency of revenue (fresh-ramp velocity)
def f24ri_f24_revenue_inflection_rampup_newhifreq_252d_jerk_v062_signal(revenue):
    hi = revenue.rolling(252, min_periods=126).max()
    is_hi = (revenue >= hi * 0.99999).astype(float)
    base = is_hi.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of new-252d-high frequency of gp
def f24ri_f24_revenue_inflection_rampup_gpnewhifreq_252d_jerk_v063_signal(gp):
    hi = gp.rolling(252, min_periods=126).max()
    is_hi = (gp >= hi * 0.99999).astype(float)
    base = is_hi.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp-minus-revenue 252d growth gap (operating-leverage velocity)
def f24ri_f24_revenue_inflection_rampup_gpgrowgap_252d_jerk_v064_signal(gp, revenue):
    base = _f24_growth(gp, 252) - _f24_growth(revenue, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp-minus-revenue 126d growth gap
def f24ri_f24_revenue_inflection_rampup_gpgrowgap_126d_jerk_v065_signal(gp, revenue):
    base = _f24_growth(gp, 126) - _f24_growth(revenue, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log(revenueusd/revenue) FX/mix divergence
def f24ri_f24_revenue_inflection_rampup_usddiverge_base_jerk_v066_signal(revenueusd, revenue):
    base = np.log(revenueusd.replace(0, np.nan) / revenue.replace(0, np.nan))
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue excess over its 252d linear baseline
def f24ri_f24_revenue_inflection_rampup_excessramp_252d_jerk_v067_signal(revenue):
    lv = np.log(revenue.replace(0, np.nan))
    base = lv - (lv.rolling(252, min_periods=126).mean() + _slope(lv, 252) * 126.0)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gross-margin position in its 504d range
def f24ri_f24_revenue_inflection_rampup_marginrangepos_504d_jerk_v068_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    hi = _rmax(m, 504)
    lo = _rmin(m, 504)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue proximity to its 252d peak (stall/saturation velocity)
def f24ri_f24_revenue_inflection_rampup_peakprox_252d_jerk_v069_signal(revenue):
    base = revenue / _rmax(revenue, 252).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp proximity to its 252d peak
def f24ri_f24_revenue_inflection_rampup_gppeakprox_252d_jerk_v070_signal(gp):
    base = gp / _rmax(gp, 252).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed 63d revenue growth (persistent ramp velocity)
def f24ri_f24_revenue_inflection_rampup_growema_base_jerk_v071_signal(revenue):
    base = _f24_growth(revenue, 63).ewm(span=126, min_periods=42).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed 63d gp growth
def f24ri_f24_revenue_inflection_rampup_gpgrowema_base_jerk_v072_signal(gp):
    base = _f24_growth(gp, 63).ewm(span=126, min_periods=42).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of blended revenue+usd 252d growth
def f24ri_f24_revenue_inflection_rampup_blendgrow_252d_jerk_v073_signal(revenue, revenueusd):
    base = 0.5 * (_f24_growth(revenue, 252) + _f24_growth(revenueusd, 252))
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of signed-sqrt revenue acceleration (bounded inflection velocity)
def f24ri_f24_revenue_inflection_rampup_accelsignmag_126d_jerk_v074_signal(revenue):
    a = _f24_accel(revenue, 126)
    base = np.sign(a) * np.sqrt(a.abs())
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of signed-sqrt gp acceleration
def f24ri_f24_revenue_inflection_rampup_gpaccelsignmag_126d_jerk_v075_signal(gp):
    a = _f24_accel(gp, 126)
    base = np.sign(a) * np.sqrt(a.abs())
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cross-horizon revenue-growth dispersion (ramp coherence velocity)
def f24ri_f24_revenue_inflection_rampup_horizondisp_base_jerk_v076_signal(revenue):
    g1 = _f24_growth(revenue, 63)
    g2 = _f24_growth(revenue, 126)
    g3 = _f24_growth(revenue, 252)
    base = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-126d with sequential 21d revenue rise
def f24ri_f24_revenue_inflection_rampup_seqincr_126d_jerk_v077_signal(revenue):
    up = (revenue > revenue.shift(21)).astype(float)
    base = up.rolling(126, min_periods=63).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fast-minus-slow gross-margin EMA crossover
def f24ri_f24_revenue_inflection_rampup_marginemagap_base_jerk_v078_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    base = m.ewm(span=42, min_periods=21).mean() - m.ewm(span=189, min_periods=63).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 252d growth-change (annual momentum velocity)
def f24ri_f24_revenue_inflection_rampup_growchg_252d_jerk_v079_signal(revenue):
    g = _f24_growth(revenue, 252)
    base = g - g.shift(63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 252d growth-change
def f24ri_f24_revenue_inflection_rampup_gpgrowchg_252d_jerk_v080_signal(gp):
    g = _f24_growth(gp, 252)
    base = g - g.shift(126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of usd 252d growth-change
def f24ri_f24_revenue_inflection_rampup_usdgrowchg_252d_jerk_v081_signal(revenueusd):
    g = _f24_growth(revenueusd, 252)
    base = g - g.shift(126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tanh-bounded revenue 252d growth
def f24ri_f24_revenue_inflection_rampup_growtanh_252d_jerk_v082_signal(revenue):
    base = np.tanh(2.0 * _f24_growth(revenue, 252))
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tanh-bounded gp 252d growth
def f24ri_f24_revenue_inflection_rampup_gpgrowtanh_252d_jerk_v083_signal(gp):
    base = np.tanh(2.0 * _f24_growth(gp, 252))
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of negative downside-semideviation of revenue growth (252d)
def f24ri_f24_revenue_inflection_rampup_negdownsemi_252d_jerk_v084_signal(revenue):
    g = revenue.pct_change()
    downs = g.where(g < 0, 0.0)
    base = -((downs ** 2).rolling(252, min_periods=126).mean() ** 0.5)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of negative ramp-jaggedness of revenue (126d)
def f24ri_f24_revenue_inflection_rampup_negjagged_126d_jerk_v085_signal(revenue):
    g = revenue.pct_change()
    base = -g.diff().abs().rolling(126, min_periods=63).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 126d/252d growth ratio
def f24ri_f24_revenue_inflection_rampup_growratio_126v252d_jerk_v086_signal(revenue):
    base = _f24_growth(revenue, 126) / _f24_growth(revenue, 252).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue recent-vs-prior 252d-mean half-shift
def f24ri_f24_revenue_inflection_rampup_halfshift_504d_jerk_v087_signal(revenue):
    recent = _mean(revenue, 252)
    prior = _mean(revenue, 252).shift(252)
    base = (recent - prior) / (recent + prior).replace(0, np.nan)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z-scored revenueusd/revenue ratio (252d FX/mix surprise)
def f24ri_f24_revenue_inflection_rampup_usdratioz_252d_jerk_v088_signal(revenueusd, revenue):
    base = _z(revenueusd / revenue.replace(0, np.nan), 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-252d gp above its 252d mean (profit-streak velocity)
def f24ri_f24_revenue_inflection_rampup_gpposstreak_252d_jerk_v089_signal(gp):
    on = (gp > _mean(gp, 252)).astype(float)
    base = on.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gross-margin 63d-step curvature
def f24ri_f24_revenue_inflection_rampup_margincurv_63d_jerk_v090_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    base = m - 2.0 * m.shift(63) + m.shift(126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of share-of-252d gross-margin above its 504d median
def f24ri_f24_revenue_inflection_rampup_marginabovemed_504d_jerk_v091_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    med = m.rolling(504, min_periods=252).median()
    on = (m > med).astype(float)
    base = on.rolling(252, min_periods=126).mean()
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d gross-margin expansion (long margin-improvement velocity)
def f24ri_f24_revenue_inflection_rampup_gpmarginexp_504d_jerk_v092_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    base = m - m.shift(504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of count of 21d-sequential revenue gains over 252d
def f24ri_f24_revenue_inflection_rampup_stepcount_252d_jerk_v093_signal(revenue):
    up = (revenue > revenue.shift(21) * 1.02).astype(float)
    base = up.rolling(252, min_periods=126).sum()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue ramp-stall persistence (share below 252d high)
def f24ri_f24_revenue_inflection_rampup_rampstall_252d_jerk_v094_signal(revenue):
    hi = _rmax(revenue, 252)
    underr = revenue / hi.replace(0, np.nan) - 1.0
    stalled = (underr <= -0.03).astype(float)
    base = stalled.rolling(126, min_periods=63).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue time-since-252d-trough (ramp-age velocity)
def f24ri_f24_revenue_inflection_rampup_daystrough_252d_jerk_v095_signal(revenue):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    base = revenue.rolling(252, min_periods=126).apply(_f, raw=True)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of producer-quality (growth x gross-margin) composite
def f24ri_f24_revenue_inflection_rampup_producerquality_base_jerk_v096_signal(revenue, gp):
    g = np.tanh(_f24_growth(revenue, 252))
    margin = _f24_gp_margin(gp, revenue).clip(lower=0, upper=1)
    base = g * margin
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gross-margin regime (fast EMA minus 504d median)
def f24ri_f24_revenue_inflection_rampup_marginregime_base_jerk_v097_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    base = m.ewm(span=63, min_periods=21).mean() - m.rolling(504, min_periods=252).median()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd proximity to its 252d peak
def f24ri_f24_revenue_inflection_rampup_usdpeakprox_252d_jerk_v098_signal(revenueusd):
    base = revenueusd / _rmax(revenueusd, 252).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gross-margin z-score (252d)
def f24ri_f24_revenue_inflection_rampup_gpmarginz_252d_jerk_v099_signal(gp, revenue):
    base = _z(_f24_gp_margin(gp, revenue), 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue growth EMA crossover (fast minus slow)
def f24ri_f24_revenue_inflection_rampup_growxover_base_jerk_v100_signal(revenue):
    g = _f24_growth(revenue, 63)
    base = g.ewm(span=42, min_periods=21).mean() - g.ewm(span=189, min_periods=63).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd short convexity (21d minus 126d growth)
def f24ri_f24_revenue_inflection_rampup_usdconvexity2_21v126d_jerk_v101_signal(revenueusd):
    base = _f24_growth(revenueusd, 21) - _f24_growth(revenueusd, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 63d/252d growth ratio (profit ramp pace ratio)
def f24ri_f24_revenue_inflection_rampup_gpgrowratio_63v252d_jerk_v102_signal(gp):
    base = _f24_growth(gp, 63) / _f24_growth(gp, 252).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd vs its 252d mean
def f24ri_f24_revenue_inflection_rampup_usdvsmean_252d_jerk_v103_signal(revenueusd):
    base = revenueusd / _mean(revenueusd, 252).replace(0, np.nan) - 1.0
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp position within its 1260d range
def f24ri_f24_revenue_inflection_rampup_gprangepos_1260d_jerk_v104_signal(gp):
    hi = _rmax(gp, 1260)
    lo = _rmin(gp, 1260)
    base = (gp - lo) / (hi - lo).replace(0, np.nan)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fast 21d revenue log-growth
def f24ri_f24_revenue_inflection_rampup_revgrow_21d_jerk_v105_signal(revenue):
    base = _f24_growth(revenue, 21)
    v = _slope(base, 5)
    b = _slope(v, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fast 21d gp log-growth
def f24ri_f24_revenue_inflection_rampup_gpgrow_21d_jerk_v106_signal(gp):
    base = _f24_growth(gp, 21)
    v = _slope(base, 5)
    b = _slope(v, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of margin-improvement share (margin up vs 63d ago)
def f24ri_f24_revenue_inflection_rampup_marginimprove_252d_jerk_v107_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    up = (m > m.shift(63)).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of count of 21d-sequential gp gains over 252d
def f24ri_f24_revenue_inflection_rampup_gpstepcount_252d_jerk_v108_signal(gp):
    up = (gp > gp.shift(21) * 1.02).astype(float)
    base = up.rolling(252, min_periods=126).sum()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 504d log-growth (multi-year ramp velocity)
def f24ri_f24_revenue_inflection_rampup_revgrow_504d_jerk_v109_signal(revenue):
    base = _f24_growth(revenue, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 504d log-growth
def f24ri_f24_revenue_inflection_rampup_gpgrow_504d_jerk_v110_signal(gp):
    base = _f24_growth(gp, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd 504d log-growth
def f24ri_f24_revenue_inflection_rampup_usdgrow_504d_jerk_v111_signal(revenueusd):
    base = _f24_growth(revenueusd, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 252d-growth-minus-prior-252d-growth (YoY-of-YoY)
def f24ri_f24_revenue_inflection_rampup_growyoy_base_jerk_v112_signal(revenue):
    g = _f24_growth(revenue, 252)
    base = g - g.shift(252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 63d growth-stability
def f24ri_f24_revenue_inflection_rampup_stability_63d_jerk_v113_signal(revenue):
    base = _f24_stability(revenue, 63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 504d growth-stability
def f24ri_f24_revenue_inflection_rampup_stability_504d_jerk_v114_signal(revenue):
    base = _f24_stability(revenue, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 126d growth-stability
def f24ri_f24_revenue_inflection_rampup_gpstability_126d_jerk_v115_signal(gp):
    base = _f24_stability(gp, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue z-score vs its 126d history
def f24ri_f24_revenue_inflection_rampup_revz_126d_jerk_v116_signal(revenue):
    base = _z(revenue, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp z-score vs its 504d history
def f24ri_f24_revenue_inflection_rampup_gpz_504d_jerk_v117_signal(gp):
    base = _z(gp, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd z-score vs its 504d history
def f24ri_f24_revenue_inflection_rampup_usdz_504d_jerk_v118_signal(revenueusd):
    base = _z(revenueusd, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 63d-growth z-score vs its 252d history
def f24ri_f24_revenue_inflection_rampup_growz_252d_jerk_v119_signal(revenue):
    g = _f24_growth(revenue, 63)
    base = _z(g, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 63d-growth z-score vs its 252d history
def f24ri_f24_revenue_inflection_rampup_gpgrowz_252d_jerk_v120_signal(gp):
    g = _f24_growth(gp, 63)
    base = _z(g, 252)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue lift off its 126d trough
def f24ri_f24_revenue_inflection_rampup_rampfromlow_126d_jerk_v121_signal(revenue):
    base = _f24_ramp_from_low(revenue, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp lift off its 126d trough
def f24ri_f24_revenue_inflection_rampup_gprampfromlow_126d_jerk_v122_signal(gp):
    base = _f24_ramp_from_low(gp, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-504d with positive 126d revenueusd growth
def f24ri_f24_revenue_inflection_rampup_usdgrowpos_504d_jerk_v123_signal(revenueusd):
    on = (_f24_growth(revenueusd, 126) > 0).astype(float)
    base = on.rolling(504, min_periods=252).mean()
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-504d with positive 126d gp growth
def f24ri_f24_revenue_inflection_rampup_gpgrowpos_504d_jerk_v124_signal(gp):
    on = (_f24_growth(gp, 126) > 0).astype(float)
    base = on.rolling(504, min_periods=252).mean()
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-504d revenue above its 504d median
def f24ri_f24_revenue_inflection_rampup_revabovemed_504d_jerk_v125_signal(revenue):
    med = revenue.rolling(504, min_periods=252).median()
    on = (revenue > med).astype(float)
    base = on.rolling(252, min_periods=126).mean()
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue position within its 252d range
def f24ri_f24_revenue_inflection_rampup_rangepos_252d_jerk_v126_signal(revenue):
    hi = _rmax(revenue, 252)
    lo = _rmin(revenue, 252)
    base = (revenue - lo) / (hi - lo).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd position within its 1260d range
def f24ri_f24_revenue_inflection_rampup_usdrangepos_1260d_jerk_v127_signal(revenueusd):
    hi = _rmax(revenueusd, 1260)
    lo = _rmin(revenueusd, 1260)
    base = (revenueusd - lo) / (hi - lo).replace(0, np.nan)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 504d ramp-acceleration level
def f24ri_f24_revenue_inflection_rampup_accel_504d_jerk_v128_signal(revenue):
    base = _f24_accel(revenue, 504)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 252d ramp-acceleration level
def f24ri_f24_revenue_inflection_rampup_gpaccel_252d_jerk_v129_signal(gp):
    base = _f24_accel(gp, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd 252d ramp-acceleration level
def f24ri_f24_revenue_inflection_rampup_usdaccel_252d_jerk_v130_signal(revenueusd):
    base = _f24_accel(revenueusd, 252)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 126d/504d mean ratio
def f24ri_f24_revenue_inflection_rampup_meanratio_126v504d_jerk_v131_signal(revenue):
    base = _mean(revenue, 126) / _mean(revenue, 504).replace(0, np.nan) - 1.0
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 126d/504d mean ratio
def f24ri_f24_revenue_inflection_rampup_gpmeanratio_126v504d_jerk_v132_signal(gp):
    base = _mean(gp, 126) / _mean(gp, 504).replace(0, np.nan) - 1.0
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd vs its 504d mean
def f24ri_f24_revenue_inflection_rampup_usdvsmean_504d_jerk_v133_signal(revenueusd):
    base = revenueusd / _mean(revenueusd, 504).replace(0, np.nan) - 1.0
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gross-margin vs its 252d mean (margin level-above-baseline)
def f24ri_f24_revenue_inflection_rampup_marginvsmean_252d_jerk_v134_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    base = m / _mean(m, 252).replace(0, np.nan) - 1.0
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue convexity (21d minus 63d growth)
def f24ri_f24_revenue_inflection_rampup_convexity_21v63d_jerk_v135_signal(revenue):
    base = _f24_growth(revenue, 21) - _f24_growth(revenue, 63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp convexity (21d minus 126d growth)
def f24ri_f24_revenue_inflection_rampup_gpconvexity_21v126d_jerk_v136_signal(gp):
    base = _f24_growth(gp, 21) - _f24_growth(gp, 126)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 63d growth per unit range (risk-adj ramp)
def f24ri_f24_revenue_inflection_rampup_growriskadj_63d_jerk_v137_signal(revenue):
    g = _f24_growth(revenue, 63)
    rng = (_rmax(revenue, 63) - _rmin(revenue, 63)) / _mean(revenue, 63).replace(0, np.nan)
    base = g / rng.replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp 252d growth per unit range
def f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_252d_jerk_v138_signal(gp):
    g = _f24_growth(gp, 252)
    rng = (_rmax(gp, 252) - _rmin(gp, 252)) / _mean(gp, 252).replace(0, np.nan)
    base = g / rng.replace(0, np.nan)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d gross-margin expansion
def f24ri_f24_revenue_inflection_rampup_gpmarginexp_63d_jerk_v139_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    base = m - m.shift(63)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gross-margin percentile rank (504d)
def f24ri_f24_revenue_inflection_rampup_marginrank_504d_jerk_v140_signal(gp, revenue):
    base = _rank(_f24_gp_margin(gp, revenue), 504)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-252d revenue above its 126d mean
def f24ri_f24_revenue_inflection_rampup_abovemean_252d_jerk_v141_signal(revenue):
    on = (revenue > _mean(revenue, 126)).astype(float)
    base = on.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-252d with positive 63d revenue growth
def f24ri_f24_revenue_inflection_rampup_growpos_252d_jerk_v142_signal(revenue):
    on = (_f24_growth(revenue, 63) > 0).astype(float)
    base = on.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fraction-of-252d with positive 63d gp growth
def f24ri_f24_revenue_inflection_rampup_gpgrowpos_252d_jerk_v143_signal(gp):
    on = (_f24_growth(gp, 63) > 0).astype(float)
    base = on.rolling(252, min_periods=126).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of share-of-126d revenue making a 21d sequential new high
def f24ri_f24_revenue_inflection_rampup_seqnewhi_126d_jerk_v144_signal(revenue):
    is_hi = (revenue >= revenue.rolling(21, min_periods=10).max() * 0.99999).astype(float)
    base = is_hi.rolling(126, min_periods=63).mean()
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of long margin-improvement share (margin up vs 126d ago)
def f24ri_f24_revenue_inflection_rampup_marginimprove2_504d_jerk_v145_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    up = (m > m.shift(126)).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue log-level 63d-step curvature (bounded)
def f24ri_f24_revenue_inflection_rampup_logcurv_63d_jerk_v146_signal(revenue):
    lv = np.log(revenue.replace(0, np.nan))
    base = np.tanh(8.0 * (lv - 2.0 * lv.shift(63) + lv.shift(126)))
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenueusd log-level 21d-step curvature (bounded)
def f24ri_f24_revenue_inflection_rampup_usdlogcurv_21d_jerk_v147_signal(revenueusd):
    lv = np.log(revenueusd.replace(0, np.nan))
    base = np.tanh(15.0 * (lv - 2.0 * lv.shift(21) + lv.shift(42)))
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gp recent-vs-prior 252d-mean half-shift
def f24ri_f24_revenue_inflection_rampup_gphalfshift_504d_jerk_v148_signal(gp):
    recent = _mean(gp, 252)
    prior = _mean(gp, 252).shift(252)
    base = (recent - prior) / (recent + prior).replace(0, np.nan)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue excess over its 504d linear baseline
def f24ri_f24_revenue_inflection_rampup_excessramp_504d_jerk_v149_signal(revenue):
    lv = np.log(revenue.replace(0, np.nan))
    base = lv - (lv.rolling(504, min_periods=252).mean() + _slope(lv, 504) * 252.0)
    v = _slope(base, 63)
    b = _slope(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue 63d/252d growth ratio
def f24ri_f24_revenue_inflection_rampup_growratio_63v252d_jerk_v150_signal(revenue):
    base = _f24_growth(revenue, 63) / _f24_growth(revenue, 252).replace(0, np.nan)
    v = _slope(base, 21)
    b = _slope(v, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24ri_f24_revenue_inflection_rampup_revgrow_63d_jerk_v001_signal,
    f24ri_f24_revenue_inflection_rampup_revgrow_126d_jerk_v002_signal,
    f24ri_f24_revenue_inflection_rampup_revgrow_252d_jerk_v003_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrow_63d_jerk_v004_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrow_126d_jerk_v005_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrow_252d_jerk_v006_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrow_63d_jerk_v007_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrow_126d_jerk_v008_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrow_252d_jerk_v009_signal,
    f24ri_f24_revenue_inflection_rampup_rampfromlow_252d_jerk_v010_signal,
    f24ri_f24_revenue_inflection_rampup_rampfromlow_504d_jerk_v011_signal,
    f24ri_f24_revenue_inflection_rampup_gprampfromlow_252d_jerk_v012_signal,
    f24ri_f24_revenue_inflection_rampup_gprampfromlow_504d_jerk_v013_signal,
    f24ri_f24_revenue_inflection_rampup_usdrampfromlow_252d_jerk_v014_signal,
    f24ri_f24_revenue_inflection_rampup_drawup_1260d_jerk_v015_signal,
    f24ri_f24_revenue_inflection_rampup_gpdrawup_1260d_jerk_v016_signal,
    f24ri_f24_revenue_inflection_rampup_usddrawup_1260d_jerk_v017_signal,
    f24ri_f24_revenue_inflection_rampup_rangepos_504d_jerk_v018_signal,
    f24ri_f24_revenue_inflection_rampup_rangepos_1260d_jerk_v019_signal,
    f24ri_f24_revenue_inflection_rampup_gprangepos_504d_jerk_v020_signal,
    f24ri_f24_revenue_inflection_rampup_usdrangepos_504d_jerk_v021_signal,
    f24ri_f24_revenue_inflection_rampup_accel_63d_jerk_v022_signal,
    f24ri_f24_revenue_inflection_rampup_accel_126d_jerk_v023_signal,
    f24ri_f24_revenue_inflection_rampup_accel_252d_jerk_v024_signal,
    f24ri_f24_revenue_inflection_rampup_gpaccel_63d_jerk_v025_signal,
    f24ri_f24_revenue_inflection_rampup_gpaccel_126d_jerk_v026_signal,
    f24ri_f24_revenue_inflection_rampup_usdaccel_126d_jerk_v027_signal,
    f24ri_f24_revenue_inflection_rampup_stability_126d_jerk_v028_signal,
    f24ri_f24_revenue_inflection_rampup_stability_252d_jerk_v029_signal,
    f24ri_f24_revenue_inflection_rampup_gpstability_252d_jerk_v030_signal,
    f24ri_f24_revenue_inflection_rampup_usdstability_252d_jerk_v031_signal,
    f24ri_f24_revenue_inflection_rampup_gpmargin_base_jerk_v032_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginsm_base_jerk_v033_signal,
    f24ri_f24_revenue_inflection_rampup_revz_252d_jerk_v034_signal,
    f24ri_f24_revenue_inflection_rampup_revz_504d_jerk_v035_signal,
    f24ri_f24_revenue_inflection_rampup_gpz_252d_jerk_v036_signal,
    f24ri_f24_revenue_inflection_rampup_usdz_252d_jerk_v037_signal,
    f24ri_f24_revenue_inflection_rampup_growrank_504d_jerk_v038_signal,
    f24ri_f24_revenue_inflection_rampup_levelrank_504d_jerk_v039_signal,
    f24ri_f24_revenue_inflection_rampup_levelrank_1260d_jerk_v040_signal,
    f24ri_f24_revenue_inflection_rampup_gplevelrank_1260d_jerk_v041_signal,
    f24ri_f24_revenue_inflection_rampup_meanratio_63v252d_jerk_v042_signal,
    f24ri_f24_revenue_inflection_rampup_meanratio_21v126d_jerk_v043_signal,
    f24ri_f24_revenue_inflection_rampup_gpmeanratio_63v252d_jerk_v044_signal,
    f24ri_f24_revenue_inflection_rampup_usdmeanratio_63v252d_jerk_v045_signal,
    f24ri_f24_revenue_inflection_rampup_vsmean_252d_jerk_v046_signal,
    f24ri_f24_revenue_inflection_rampup_vsmean_504d_jerk_v047_signal,
    f24ri_f24_revenue_inflection_rampup_gpvsmean_252d_jerk_v048_signal,
    f24ri_f24_revenue_inflection_rampup_convexity_63v252d_jerk_v049_signal,
    f24ri_f24_revenue_inflection_rampup_gpconvexity_63v252d_jerk_v050_signal,
    f24ri_f24_revenue_inflection_rampup_usdconvexity_63v252d_jerk_v051_signal,
    f24ri_f24_revenue_inflection_rampup_negcv_252d_jerk_v052_signal,
    f24ri_f24_revenue_inflection_rampup_negcv_126d_jerk_v053_signal,
    f24ri_f24_revenue_inflection_rampup_gpnegcv_252d_jerk_v054_signal,
    f24ri_f24_revenue_inflection_rampup_growriskadj_126d_jerk_v055_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_126d_jerk_v056_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrowriskadj_252d_jerk_v057_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginexp_252d_jerk_v058_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginexp_126d_jerk_v059_signal,
    f24ri_f24_revenue_inflection_rampup_posstreak_252d_jerk_v060_signal,
    f24ri_f24_revenue_inflection_rampup_gpabovemed_252d_jerk_v061_signal,
    f24ri_f24_revenue_inflection_rampup_newhifreq_252d_jerk_v062_signal,
    f24ri_f24_revenue_inflection_rampup_gpnewhifreq_252d_jerk_v063_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowgap_252d_jerk_v064_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowgap_126d_jerk_v065_signal,
    f24ri_f24_revenue_inflection_rampup_usddiverge_base_jerk_v066_signal,
    f24ri_f24_revenue_inflection_rampup_excessramp_252d_jerk_v067_signal,
    f24ri_f24_revenue_inflection_rampup_marginrangepos_504d_jerk_v068_signal,
    f24ri_f24_revenue_inflection_rampup_peakprox_252d_jerk_v069_signal,
    f24ri_f24_revenue_inflection_rampup_gppeakprox_252d_jerk_v070_signal,
    f24ri_f24_revenue_inflection_rampup_growema_base_jerk_v071_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowema_base_jerk_v072_signal,
    f24ri_f24_revenue_inflection_rampup_blendgrow_252d_jerk_v073_signal,
    f24ri_f24_revenue_inflection_rampup_accelsignmag_126d_jerk_v074_signal,
    f24ri_f24_revenue_inflection_rampup_gpaccelsignmag_126d_jerk_v075_signal,
    f24ri_f24_revenue_inflection_rampup_horizondisp_base_jerk_v076_signal,
    f24ri_f24_revenue_inflection_rampup_seqincr_126d_jerk_v077_signal,
    f24ri_f24_revenue_inflection_rampup_marginemagap_base_jerk_v078_signal,
    f24ri_f24_revenue_inflection_rampup_growchg_252d_jerk_v079_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowchg_252d_jerk_v080_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrowchg_252d_jerk_v081_signal,
    f24ri_f24_revenue_inflection_rampup_growtanh_252d_jerk_v082_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowtanh_252d_jerk_v083_signal,
    f24ri_f24_revenue_inflection_rampup_negdownsemi_252d_jerk_v084_signal,
    f24ri_f24_revenue_inflection_rampup_negjagged_126d_jerk_v085_signal,
    f24ri_f24_revenue_inflection_rampup_growratio_126v252d_jerk_v086_signal,
    f24ri_f24_revenue_inflection_rampup_halfshift_504d_jerk_v087_signal,
    f24ri_f24_revenue_inflection_rampup_usdratioz_252d_jerk_v088_signal,
    f24ri_f24_revenue_inflection_rampup_gpposstreak_252d_jerk_v089_signal,
    f24ri_f24_revenue_inflection_rampup_margincurv_63d_jerk_v090_signal,
    f24ri_f24_revenue_inflection_rampup_marginabovemed_504d_jerk_v091_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginexp_504d_jerk_v092_signal,
    f24ri_f24_revenue_inflection_rampup_stepcount_252d_jerk_v093_signal,
    f24ri_f24_revenue_inflection_rampup_rampstall_252d_jerk_v094_signal,
    f24ri_f24_revenue_inflection_rampup_daystrough_252d_jerk_v095_signal,
    f24ri_f24_revenue_inflection_rampup_producerquality_base_jerk_v096_signal,
    f24ri_f24_revenue_inflection_rampup_marginregime_base_jerk_v097_signal,
    f24ri_f24_revenue_inflection_rampup_usdpeakprox_252d_jerk_v098_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginz_252d_jerk_v099_signal,
    f24ri_f24_revenue_inflection_rampup_growxover_base_jerk_v100_signal,
    f24ri_f24_revenue_inflection_rampup_usdconvexity2_21v126d_jerk_v101_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowratio_63v252d_jerk_v102_signal,
    f24ri_f24_revenue_inflection_rampup_usdvsmean_252d_jerk_v103_signal,
    f24ri_f24_revenue_inflection_rampup_gprangepos_1260d_jerk_v104_signal,
    f24ri_f24_revenue_inflection_rampup_revgrow_21d_jerk_v105_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrow_21d_jerk_v106_signal,
    f24ri_f24_revenue_inflection_rampup_marginimprove_252d_jerk_v107_signal,
    f24ri_f24_revenue_inflection_rampup_gpstepcount_252d_jerk_v108_signal,
    f24ri_f24_revenue_inflection_rampup_revgrow_504d_jerk_v109_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrow_504d_jerk_v110_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrow_504d_jerk_v111_signal,
    f24ri_f24_revenue_inflection_rampup_growyoy_base_jerk_v112_signal,
    f24ri_f24_revenue_inflection_rampup_stability_63d_jerk_v113_signal,
    f24ri_f24_revenue_inflection_rampup_stability_504d_jerk_v114_signal,
    f24ri_f24_revenue_inflection_rampup_gpstability_126d_jerk_v115_signal,
    f24ri_f24_revenue_inflection_rampup_revz_126d_jerk_v116_signal,
    f24ri_f24_revenue_inflection_rampup_gpz_504d_jerk_v117_signal,
    f24ri_f24_revenue_inflection_rampup_usdz_504d_jerk_v118_signal,
    f24ri_f24_revenue_inflection_rampup_growz_252d_jerk_v119_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowz_252d_jerk_v120_signal,
    f24ri_f24_revenue_inflection_rampup_rampfromlow_126d_jerk_v121_signal,
    f24ri_f24_revenue_inflection_rampup_gprampfromlow_126d_jerk_v122_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrowpos_504d_jerk_v123_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowpos_504d_jerk_v124_signal,
    f24ri_f24_revenue_inflection_rampup_revabovemed_504d_jerk_v125_signal,
    f24ri_f24_revenue_inflection_rampup_rangepos_252d_jerk_v126_signal,
    f24ri_f24_revenue_inflection_rampup_usdrangepos_1260d_jerk_v127_signal,
    f24ri_f24_revenue_inflection_rampup_accel_504d_jerk_v128_signal,
    f24ri_f24_revenue_inflection_rampup_gpaccel_252d_jerk_v129_signal,
    f24ri_f24_revenue_inflection_rampup_usdaccel_252d_jerk_v130_signal,
    f24ri_f24_revenue_inflection_rampup_meanratio_126v504d_jerk_v131_signal,
    f24ri_f24_revenue_inflection_rampup_gpmeanratio_126v504d_jerk_v132_signal,
    f24ri_f24_revenue_inflection_rampup_usdvsmean_504d_jerk_v133_signal,
    f24ri_f24_revenue_inflection_rampup_marginvsmean_252d_jerk_v134_signal,
    f24ri_f24_revenue_inflection_rampup_convexity_21v63d_jerk_v135_signal,
    f24ri_f24_revenue_inflection_rampup_gpconvexity_21v126d_jerk_v136_signal,
    f24ri_f24_revenue_inflection_rampup_growriskadj_63d_jerk_v137_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_252d_jerk_v138_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginexp_63d_jerk_v139_signal,
    f24ri_f24_revenue_inflection_rampup_marginrank_504d_jerk_v140_signal,
    f24ri_f24_revenue_inflection_rampup_abovemean_252d_jerk_v141_signal,
    f24ri_f24_revenue_inflection_rampup_growpos_252d_jerk_v142_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowpos_252d_jerk_v143_signal,
    f24ri_f24_revenue_inflection_rampup_seqnewhi_126d_jerk_v144_signal,
    f24ri_f24_revenue_inflection_rampup_marginimprove2_504d_jerk_v145_signal,
    f24ri_f24_revenue_inflection_rampup_logcurv_63d_jerk_v146_signal,
    f24ri_f24_revenue_inflection_rampup_usdlogcurv_21d_jerk_v147_signal,
    f24ri_f24_revenue_inflection_rampup_gphalfshift_504d_jerk_v148_signal,
    f24ri_f24_revenue_inflection_rampup_excessramp_504d_jerk_v149_signal,
    f24ri_f24_revenue_inflection_rampup_growratio_63v252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_REVENUE_INFLECTION_RAMPUP_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    revenue = _fund(2401, base=2e7, drift=0.05, vol=0.12).rename("revenue")
    revenueusd = (_fund(2402, base=2.05e7, drift=0.05, vol=0.12)
                  * (1.0 + 0.05 * np.sin(np.linspace(0, 9, n)))).rename("revenueusd")
    gp = (_fund(2403, base=7e6, drift=0.055, vol=0.16)).rename("gp")

    cols = {"revenue": revenue, "revenueusd": revenueusd, "gp": gp}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("revenue", "revenueusd", "gp") for c in meta["inputs"]), name
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

    print("OK f24_revenue_inflection_rampup_3rd_derivatives_001_150_claude: %d features pass" % n_features)
