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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
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
# revenue ramp: 21d log growth (fast monthly ramp)
def f24ri_f24_revenue_inflection_rampup_revgrow_21d_base_v076_signal(revenue):
    b = _f24_growth(revenue, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd ramp: 126d log growth (USD half-year ramp)
def f24ri_f24_revenue_inflection_rampup_usdgrow_126d_base_v077_signal(revenueusd):
    b = _f24_growth(revenueusd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp ramp: 126d log growth (gross-profit half-year ramp)
def f24ri_f24_revenue_inflection_rampup_gpgrow_126d_base_v078_signal(gp):
    b = _f24_growth(gp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 1260d log growth (full-cycle inflection magnitude)
def f24ri_f24_revenue_inflection_rampup_revgrow_1260d_base_v079_signal(revenue):
    b = _f24_growth(revenue, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp-from-low 126d (short-horizon lift off trough)
def f24ri_f24_revenue_inflection_rampup_rampfromlow_126d_base_v080_signal(revenue):
    b = _f24_ramp_from_low(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp ramp-from-low 504d (multi-year gross-profit lift)
def f24ri_f24_revenue_inflection_rampup_gprampfromlow_504d_base_v081_signal(gp):
    b = _f24_ramp_from_low(gp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 1260d range position (full-cycle ramp phase)
def f24ri_f24_revenue_inflection_rampup_rangepos_1260d_base_v082_signal(revenue):
    hi = _rmax(revenue, 1260)
    lo = _rmin(revenue, 1260)
    b = (revenue - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp 504d range position (gross-profit cycle phase)
def f24ri_f24_revenue_inflection_rampup_gprangepos_504d_base_v083_signal(gp):
    hi = _rmax(gp, 504)
    lo = _rmin(gp, 504)
    b = (gp - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration 252d (slow ramp acceleration as a level)
def f24ri_f24_revenue_inflection_rampup_accel_252d_base_v084_signal(revenue):
    b = _f24_accel(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp acceleration 126d (profit-ramp acceleration as a level)
def f24ri_f24_revenue_inflection_rampup_gpaccel_126d_base_v085_signal(gp):
    b = _f24_accel(gp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd acceleration 126d (USD ramp acceleration)
def f24ri_f24_revenue_inflection_rampup_usdaccel_126d_base_v086_signal(revenueusd):
    b = _f24_accel(revenueusd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability 63d (short-run ramp consistency)
def f24ri_f24_revenue_inflection_rampup_stability_63d_base_v087_signal(revenue):
    b = _f24_stability(revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability 504d (multi-year ramp consistency)
def f24ri_f24_revenue_inflection_rampup_stability_504d_base_v088_signal(revenue):
    b = _f24_stability(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd growth stability 252d (USD ramp consistency)
def f24ri_f24_revenue_inflection_rampup_usdstability_252d_base_v089_signal(revenueusd):
    b = _f24_stability(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue z vs 504d history (long de-trended ramp surprise)
def f24ri_f24_revenue_inflection_rampup_revz_504d_base_v090_signal(revenue):
    b = _z(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp z vs 252d history (gross-profit surprise)
def f24ri_f24_revenue_inflection_rampup_gpz_252d_base_v091_signal(gp):
    b = _z(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth z vs 126d history (short growth surprise)
def f24ri_f24_revenue_inflection_rampup_growz_126d_base_v092_signal(revenue):
    g = _f24_growth(revenue, 63)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp growth percentile rank vs 504d history (profit-ramp position)
def f24ri_f24_revenue_inflection_rampup_gpgrowrank_504d_base_v093_signal(gp):
    g = _f24_growth(gp, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level rank vs 504d history (ramp position, medium horizon)
def f24ri_f24_revenue_inflection_rampup_levelrank_504d_base_v094_signal(revenue):
    b = _rank(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z-score vs 1260d history (long de-trended margin extremity)
def f24ri_f24_revenue_inflection_rampup_marginz_1260d_base_v095_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    b = _z(m, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue convexity short: 21d growth minus 126d growth (fast accel vs steady)
def f24ri_f24_revenue_inflection_rampup_convexity_21v126_base_v096_signal(revenue):
    b = _f24_growth(revenue, 21) - _f24_growth(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp convexity: 63d gp growth minus 252d gp growth
def f24ri_f24_revenue_inflection_rampup_gpconvexity_base_v097_signal(gp):
    b = _f24_growth(gp, 63) - _f24_growth(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue mean ratio 21v126 (very-short vs short ramp momentum)
def f24ri_f24_revenue_inflection_rampup_meanratio_21v126_base_v098_signal(revenue):
    s = _mean(revenue, 21)
    l = _mean(revenue, 126)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp mean ratio 126v504 (gross-profit slow ramp momentum)
def f24ri_f24_revenue_inflection_rampup_gpmeanratio_126v504_base_v099_signal(gp):
    s = _mean(gp, 126)
    l = _mean(gp, 504)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp breadth: share of last 504d setting a fresh 252d revenue high
def f24ri_f24_revenue_inflection_rampup_rampbreadth_504d_base_v100_signal(revenue):
    hi = revenue.rolling(252, min_periods=126).max()
    is_hi = (revenue >= hi * 0.99999).astype(float)
    b = is_hi.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd drawup off 1260d trough (USD long-run lift)
def f24ri_f24_revenue_inflection_rampup_usddrawup_1260d_base_v101_signal(revenueusd):
    lo = _rmin(revenueusd, 1260)
    b = np.log(revenueusd.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 504d with 126d growth positive (sustained-ramp share)
def f24ri_f24_revenue_inflection_rampup_growpos_504d_base_v102_signal(revenue):
    g = _f24_growth(revenue, 126)
    on = (g > 0).astype(float)
    b = on.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d with gp 63d growth positive (profit-ramp share)
def f24ri_f24_revenue_inflection_rampup_gpgrowpos_252d_base_v103_signal(gp):
    g = _f24_growth(gp, 63)
    on = (g > 0).astype(float)
    b = on.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd vs revenue diverge slope (FX/mix trend over a year)
def f24ri_f24_revenue_inflection_rampup_divergeslope_base_v104_signal(revenueusd, revenue):
    d = np.log(revenueusd.replace(0, np.nan) / revenue.replace(0, np.nan))
    b = _slope(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-vs-revenue growth gap over 126d (operating-leverage flavor, shorter)
def f24ri_f24_revenue_inflection_rampup_gpgrowgap_126d_base_v105_signal(gp, revenue):
    b = _f24_growth(gp, 126) - _f24_growth(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level smoothed (persistent ramp-quality EMA)
def f24ri_f24_revenue_inflection_rampup_marginema_base_v106_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    b = m.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin displacement: margin minus its slow EMA (margin shock)
def f24ri_f24_revenue_inflection_rampup_margindisp_base_v107_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    b = m - m.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue coefficient of variation 126d (ramp smoothness, negated)
def f24ri_f24_revenue_inflection_rampup_negcv_126d_base_v108_signal(revenue):
    cv = _std(revenue, 126) / _mean(revenue, 126).replace(0, np.nan)
    b = -cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp coefficient of variation 252d (gross-profit smoothness, negated)
def f24ri_f24_revenue_inflection_rampup_gpnegcv_252d_base_v109_signal(gp):
    cv = _std(gp, 252) / _mean(gp, 252).replace(0, np.nan)
    b = -cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp 63d growth risk-adjusted (short profit ramp per unit gp vol)
def f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_63d_base_v110_signal(gp):
    g = _f24_growth(gp, 63)
    vol = gp.pct_change().rolling(63, min_periods=21).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp 252d growth risk-adjusted (profit ramp per unit gp vol)
def f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_252d_base_v111_signal(gp):
    g = _f24_growth(gp, 252)
    vol = gp.pct_change().rolling(252, min_periods=126).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue YoY change 126d horizon (semi-annual growth momentum)
def f24ri_f24_revenue_inflection_rampup_growchg_126d_base_v112_signal(revenue):
    g = _f24_growth(revenue, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp YoY change (gross-profit growth momentum year over year)
def f24ri_f24_revenue_inflection_rampup_gpgrowchg_252d_base_v113_signal(gp):
    g = _f24_growth(gp, 252)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue tanh of 252d growth (bounded YoY ramp magnitude)
def f24ri_f24_revenue_inflection_rampup_growtanh_252d_base_v114_signal(revenue):
    g = _f24_growth(revenue, 252)
    b = np.tanh(2.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of 21d-sequential gp gains over 252d (profit ramp-step tally)
def f24ri_f24_revenue_inflection_rampup_gpstepcount_252d_base_v115_signal(gp):
    up = (gp > gp.shift(21) * 1.02).astype(float)
    b = up.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of last 126d revenue made a sequential 21d new high (ramp persistence)
def f24ri_f24_revenue_inflection_rampup_seqnewhi_126d_base_v116_signal(revenue):
    is_hi = (revenue >= revenue.rolling(21, min_periods=10).max() * 0.99999).astype(float)
    b = is_hi.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp time-since-trough over 504d (fraction elapsed since gp min; profit-ramp age)
def f24ri_f24_revenue_inflection_rampup_gpdaystrough_504d_base_v117_signal(gp):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = gp.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp-stall persistence: share of 252d sat >5% below 504d high
def f24ri_f24_revenue_inflection_rampup_rampstall_504d_base_v118_signal(revenue):
    hi = _rmax(revenue, 504)
    underr = revenue / hi.replace(0, np.nan) - 1.0
    stalled = (underr <= -0.05).astype(float)
    b = stalled.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin expansion over 126d (mix improvement, shorter horizon)
def f24ri_f24_revenue_inflection_rampup_gpmarginexp_126d_base_v119_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    b = m - m.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin rank vs 504d history (margin cycle position)
def f24ri_f24_revenue_inflection_rampup_marginrank_504d_base_v120_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp 21d slope normalized by level (very-short profit velocity)
def f24ri_f24_revenue_inflection_rampup_gpnormslope_21d_base_v121_signal(gp):
    sl = _slope(gp, 21)
    b = sl / _mean(gp, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp 252d slope normalized by level (gross-profit annual velocity)
def f24ri_f24_revenue_inflection_rampup_gpnormslope_252d_base_v122_signal(gp):
    sl = _slope(gp, 252)
    b = sl / _mean(gp, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue horizon dispersion 21/63/126 growth (short-horizon disagreement)
def f24ri_f24_revenue_inflection_rampup_shorthorizondisp_base_v123_signal(revenue):
    g1 = _f24_growth(revenue, 21)
    g2 = _f24_growth(revenue, 63)
    g3 = _f24_growth(revenue, 126)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue above its 126d mean fraction over 252d (ramp-trend persistence)
def f24ri_f24_revenue_inflection_rampup_abovemean_252d_base_v124_signal(revenue):
    ref = _mean(revenue, 126)
    on = (revenue > ref).astype(float)
    b = on.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp above its 252d median fraction over 252d (profit-trend persistence)
def f24ri_f24_revenue_inflection_rampup_gpabovemed_252d_base_v125_signal(gp):
    med = gp.rolling(252, min_periods=126).median()
    on = (gp > med).astype(float)
    b = on.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue regime half-shift over 252d (recent-126d vs prior-126d mean)
def f24ri_f24_revenue_inflection_rampup_halfshift_252d_base_v126_signal(revenue):
    recent = _mean(revenue, 126)
    prior = _mean(revenue, 126).shift(126)
    b = (recent - prior) / (recent + prior).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd vs revenue level ratio (USD mix level)
def f24ri_f24_revenue_inflection_rampup_usdratio_base_v127_signal(revenueusd, revenue):
    b = revenueusd / revenue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration risk-adjusted 252d (slow accel per unit growth vol)
def f24ri_f24_revenue_inflection_rampup_accelriskadj_252d_base_v128_signal(revenue):
    a = _f24_accel(revenue, 252)
    vol = _f24_growth(revenue, 126).rolling(252, min_periods=126).std()
    b = a / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue downside semideviation of growth 252d (ramp downside risk, negated)
def f24ri_f24_revenue_inflection_rampup_negdownsemi_252d_base_v129_signal(revenue):
    g = revenue.pct_change()
    downs = g.where(g < 0, 0.0)
    b = -((downs ** 2).rolling(252, min_periods=126).mean() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue jaggedness 252d (mean abs change of growth, negated)
def f24ri_f24_revenue_inflection_rampup_negjagged_252d_base_v130_signal(revenue):
    g = revenue.pct_change()
    b = -g.diff().abs().rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp ramp from 504d low tanh x margin (durable profit ramp composite)
def f24ri_f24_revenue_inflection_rampup_gpdurable_base_v131_signal(gp, revenue):
    lift = np.tanh(_f24_ramp_from_low(gp, 504))
    margin = _f24_gp_margin(gp, revenue).clip(lower=0, upper=1)
    b = lift * margin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp confirmed by stable margin (growth x margin-stability)
def f24ri_f24_revenue_inflection_rampup_stablemarginramp_base_v132_signal(revenue, gp):
    g = np.tanh(_f24_growth(revenue, 252))
    m = _f24_gp_margin(gp, revenue)
    mstab = -_std(m, 252)
    b = g * np.tanh(50.0 * mstab)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs 504d mean ratio (medium-run level above baseline)
def f24ri_f24_revenue_inflection_rampup_vsmean_504d_base_v133_signal(revenue):
    m = _mean(revenue, 504)
    b = revenue / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp vs 1260d mean ratio (long-run gross-profit level)
def f24ri_f24_revenue_inflection_rampup_gpvsmean_1260d_base_v134_signal(gp):
    m = _mean(gp, 1260)
    b = gp / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd growth convexity (63d vs 252d USD growth)
def f24ri_f24_revenue_inflection_rampup_usdconvexity_base_v135_signal(revenueusd):
    b = _f24_growth(revenueusd, 63) - _f24_growth(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth EMA fast minus slow (ramp momentum crossover)
def f24ri_f24_revenue_inflection_rampup_growxover_base_v136_signal(revenue):
    g = _f24_growth(revenue, 63)
    b = g.ewm(span=42, min_periods=21).mean() - g.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue log excess over 504d linear baseline (excess ramp, longer)
def f24ri_f24_revenue_inflection_rampup_excessramp_504d_base_v137_signal(revenue):
    lv = np.log(revenue.replace(0, np.nan))
    base = lv.rolling(504, min_periods=252).mean() + _slope(lv, 504) * 252.0
    b = lv - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue sign x sqrt accel 63d (bounded short inflection)
def f24ri_f24_revenue_inflection_rampup_accelsignmag_63d_base_v138_signal(revenue):
    a = _f24_accel(revenue, 63)
    b = np.sign(a) * np.sqrt(a.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp sign x sqrt accel 252d (bounded slow profit inflection)
def f24ri_f24_revenue_inflection_rampup_gpaccelsignmag_252d_base_v139_signal(gp):
    a = _f24_accel(gp, 252)
    b = np.sign(a) * np.sqrt(a.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d where margin expanded vs 63d ago (margin-improvement share)
def f24ri_f24_revenue_inflection_rampup_marginimprove_252d_base_v140_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    up = (m > m.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth ratio 63v252 (short-vs-long ramp pace ratio)
def f24ri_f24_revenue_inflection_rampup_growratio_63v252_base_v141_signal(revenue):
    g_s = _f24_growth(revenue, 63)
    g_l = _f24_growth(revenue, 252)
    b = g_s / g_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd level rank vs 504d (USD ramp position)
def f24ri_f24_revenue_inflection_rampup_usdlevelrank_504d_base_v142_signal(revenueusd):
    b = _rank(revenueusd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue blended ramp: avg of growth-stability and above-mean persistence
def f24ri_f24_revenue_inflection_rampup_blendlift_base_v143_signal(revenue):
    stab = np.tanh(_f24_stability(revenue, 252))
    persist = (revenue > _mean(revenue, 252)).astype(float).rolling(
        252, min_periods=126).mean() - 0.5
    b = 0.5 * (stab + 2.0 * persist)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp growth percentile rank vs 252d history (profit-ramp position, shorter)
def f24ri_f24_revenue_inflection_rampup_gpgrowrank_252d_base_v144_signal(gp):
    g = _f24_growth(gp, 63)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue stability x growth interaction (high-quality ramp score)
def f24ri_f24_revenue_inflection_rampup_qualityramp_base_v145_signal(revenue):
    stab = np.tanh(_f24_stability(revenue, 252))
    g = np.tanh(_f24_growth(revenue, 126))
    b = stab * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin spread: short EMA margin minus 504d median margin (margin regime)
def f24ri_f24_revenue_inflection_rampup_marginregime_base_v146_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    fast = m.ewm(span=63, min_periods=21).mean()
    base = m.rolling(504, min_periods=252).median()
    b = fast - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 504d-vs-126d growth gap (long-minus-short ramp, deceleration sign)
def f24ri_f24_revenue_inflection_rampup_longshortgap_base_v147_signal(revenue):
    b = _f24_growth(revenue, 504) / 2.0 - _f24_growth(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd ramp-from-low 252d (USD short lift off trough)
def f24ri_f24_revenue_inflection_rampup_usdrampfromlow_252d_base_v148_signal(revenueusd):
    b = _f24_ramp_from_low(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue inflection composite: convexity + stability + drawup (signed avg)
def f24ri_f24_revenue_inflection_rampup_inflectcomposite_base_v149_signal(revenue):
    conv = np.tanh(_f24_growth(revenue, 63) - _f24_growth(revenue, 252))
    stab = np.tanh(_f24_stability(revenue, 252))
    du = np.tanh(np.log(revenue.replace(0, np.nan) / _rmin(revenue, 504).replace(0, np.nan)))
    b = (conv + stab + du) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# producer-quality ramp: revenue growth x gross-margin level (revenue+gp)
def f24ri_f24_revenue_inflection_rampup_producerquality_base_v150_signal(revenue, gp):
    g = np.tanh(_f24_growth(revenue, 252))
    margin = _f24_gp_margin(gp, revenue).clip(lower=0, upper=1)
    b = g * margin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24ri_f24_revenue_inflection_rampup_revgrow_21d_base_v076_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrow_126d_base_v077_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrow_126d_base_v078_signal,
    f24ri_f24_revenue_inflection_rampup_revgrow_1260d_base_v079_signal,
    f24ri_f24_revenue_inflection_rampup_rampfromlow_126d_base_v080_signal,
    f24ri_f24_revenue_inflection_rampup_gprampfromlow_504d_base_v081_signal,
    f24ri_f24_revenue_inflection_rampup_rangepos_1260d_base_v082_signal,
    f24ri_f24_revenue_inflection_rampup_gprangepos_504d_base_v083_signal,
    f24ri_f24_revenue_inflection_rampup_accel_252d_base_v084_signal,
    f24ri_f24_revenue_inflection_rampup_gpaccel_126d_base_v085_signal,
    f24ri_f24_revenue_inflection_rampup_usdaccel_126d_base_v086_signal,
    f24ri_f24_revenue_inflection_rampup_stability_63d_base_v087_signal,
    f24ri_f24_revenue_inflection_rampup_stability_504d_base_v088_signal,
    f24ri_f24_revenue_inflection_rampup_usdstability_252d_base_v089_signal,
    f24ri_f24_revenue_inflection_rampup_revz_504d_base_v090_signal,
    f24ri_f24_revenue_inflection_rampup_gpz_252d_base_v091_signal,
    f24ri_f24_revenue_inflection_rampup_growz_126d_base_v092_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowrank_504d_base_v093_signal,
    f24ri_f24_revenue_inflection_rampup_levelrank_504d_base_v094_signal,
    f24ri_f24_revenue_inflection_rampup_marginz_1260d_base_v095_signal,
    f24ri_f24_revenue_inflection_rampup_convexity_21v126_base_v096_signal,
    f24ri_f24_revenue_inflection_rampup_gpconvexity_base_v097_signal,
    f24ri_f24_revenue_inflection_rampup_meanratio_21v126_base_v098_signal,
    f24ri_f24_revenue_inflection_rampup_gpmeanratio_126v504_base_v099_signal,
    f24ri_f24_revenue_inflection_rampup_rampbreadth_504d_base_v100_signal,
    f24ri_f24_revenue_inflection_rampup_usddrawup_1260d_base_v101_signal,
    f24ri_f24_revenue_inflection_rampup_growpos_504d_base_v102_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowpos_252d_base_v103_signal,
    f24ri_f24_revenue_inflection_rampup_divergeslope_base_v104_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowgap_126d_base_v105_signal,
    f24ri_f24_revenue_inflection_rampup_marginema_base_v106_signal,
    f24ri_f24_revenue_inflection_rampup_margindisp_base_v107_signal,
    f24ri_f24_revenue_inflection_rampup_negcv_126d_base_v108_signal,
    f24ri_f24_revenue_inflection_rampup_gpnegcv_252d_base_v109_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_63d_base_v110_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_252d_base_v111_signal,
    f24ri_f24_revenue_inflection_rampup_growchg_126d_base_v112_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowchg_252d_base_v113_signal,
    f24ri_f24_revenue_inflection_rampup_growtanh_252d_base_v114_signal,
    f24ri_f24_revenue_inflection_rampup_gpstepcount_252d_base_v115_signal,
    f24ri_f24_revenue_inflection_rampup_seqnewhi_126d_base_v116_signal,
    f24ri_f24_revenue_inflection_rampup_gpdaystrough_504d_base_v117_signal,
    f24ri_f24_revenue_inflection_rampup_rampstall_504d_base_v118_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginexp_126d_base_v119_signal,
    f24ri_f24_revenue_inflection_rampup_marginrank_504d_base_v120_signal,
    f24ri_f24_revenue_inflection_rampup_gpnormslope_21d_base_v121_signal,
    f24ri_f24_revenue_inflection_rampup_gpnormslope_252d_base_v122_signal,
    f24ri_f24_revenue_inflection_rampup_shorthorizondisp_base_v123_signal,
    f24ri_f24_revenue_inflection_rampup_abovemean_252d_base_v124_signal,
    f24ri_f24_revenue_inflection_rampup_gpabovemed_252d_base_v125_signal,
    f24ri_f24_revenue_inflection_rampup_halfshift_252d_base_v126_signal,
    f24ri_f24_revenue_inflection_rampup_usdratio_base_v127_signal,
    f24ri_f24_revenue_inflection_rampup_accelriskadj_252d_base_v128_signal,
    f24ri_f24_revenue_inflection_rampup_negdownsemi_252d_base_v129_signal,
    f24ri_f24_revenue_inflection_rampup_negjagged_252d_base_v130_signal,
    f24ri_f24_revenue_inflection_rampup_gpdurable_base_v131_signal,
    f24ri_f24_revenue_inflection_rampup_stablemarginramp_base_v132_signal,
    f24ri_f24_revenue_inflection_rampup_vsmean_504d_base_v133_signal,
    f24ri_f24_revenue_inflection_rampup_gpvsmean_1260d_base_v134_signal,
    f24ri_f24_revenue_inflection_rampup_usdconvexity_base_v135_signal,
    f24ri_f24_revenue_inflection_rampup_growxover_base_v136_signal,
    f24ri_f24_revenue_inflection_rampup_excessramp_504d_base_v137_signal,
    f24ri_f24_revenue_inflection_rampup_accelsignmag_63d_base_v138_signal,
    f24ri_f24_revenue_inflection_rampup_gpaccelsignmag_252d_base_v139_signal,
    f24ri_f24_revenue_inflection_rampup_marginimprove_252d_base_v140_signal,
    f24ri_f24_revenue_inflection_rampup_growratio_63v252_base_v141_signal,
    f24ri_f24_revenue_inflection_rampup_usdlevelrank_504d_base_v142_signal,
    f24ri_f24_revenue_inflection_rampup_blendlift_base_v143_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowrank_252d_base_v144_signal,
    f24ri_f24_revenue_inflection_rampup_qualityramp_base_v145_signal,
    f24ri_f24_revenue_inflection_rampup_marginregime_base_v146_signal,
    f24ri_f24_revenue_inflection_rampup_longshortgap_base_v147_signal,
    f24ri_f24_revenue_inflection_rampup_usdrampfromlow_252d_base_v148_signal,
    f24ri_f24_revenue_inflection_rampup_inflectcomposite_base_v149_signal,
    f24ri_f24_revenue_inflection_rampup_producerquality_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_REVENUE_INFLECTION_RAMPUP_REGISTRY_076_150 = REGISTRY


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

    print("OK f24_revenue_inflection_rampup_base_076_150_claude: %d features pass" % n_features)
