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
    # log growth of revenue over w trading days (the ramp slope)
    return np.log(rev.replace(0, np.nan) / rev.shift(w).replace(0, np.nan))


def _f24_ramp_from_low(rev, w):
    # revenue now vs its trailing-window minimum (ramp from ~0 base)
    lo = rev.rolling(w, min_periods=max(1, w // 2)).min()
    return rev / lo.replace(0, np.nan) - 1.0


def _f24_pos_streak(rev, thresh, w):
    # fraction of last w days with revenue above a small positive threshold
    on = (rev > thresh).astype(float)
    return on.rolling(w, min_periods=max(1, w // 2)).mean()


def _f24_accel(rev, w):
    # acceleration of the ramp as a level: short growth minus long growth
    g_s = np.log(rev.replace(0, np.nan) / rev.shift(w).replace(0, np.nan))
    g_l = np.log(rev.shift(w).replace(0, np.nan) / rev.shift(2 * w).replace(0, np.nan))
    return g_s - g_l


def _f24_gp_margin(gp, rev):
    return gp / rev.replace(0, np.nan)


def _f24_stability(rev, w):
    # growth stability = mean growth / dispersion of growth (consistency of ramp)
    g = rev.pct_change()
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


# ============================================================
# revenue ramp: 63d log growth (sequential quarter ramp)
def f24ri_f24_revenue_inflection_rampup_revgrow_63d_base_v001_signal(revenue):
    b = _f24_growth(revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp: 126d log growth (half-year ramp)
def f24ri_f24_revenue_inflection_rampup_revgrow_126d_base_v002_signal(revenue):
    b = _f24_growth(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp: 252d log growth (year-over-year inflection)
def f24ri_f24_revenue_inflection_rampup_revgrow_252d_base_v003_signal(revenue):
    b = _f24_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd ramp: 252d log growth (USD-normalized YoY inflection)
def f24ri_f24_revenue_inflection_rampup_revusdgrow_252d_base_v004_signal(revenueusd):
    b = _f24_growth(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit ramp: 252d log growth (margin-bearing revenue inflection)
def f24ri_f24_revenue_inflection_rampup_gpgrow_252d_base_v005_signal(gp):
    b = _f24_growth(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-since-revenue-trough: fraction of 252d window elapsed since the min (ramp age)
def f24ri_f24_revenue_inflection_rampup_daystrough_252d_base_v006_signal(revenue):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = revenue.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ramp-from-zero: revenue vs its 504d trough (multi-year ramp lift)
def f24ri_f24_revenue_inflection_rampup_rampfromlow_504d_base_v007_signal(revenue):
    b = _f24_ramp_from_low(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ramp-from-zero: gross profit vs its 252d trough (profit ramp)
def f24ri_f24_revenue_inflection_rampup_gprampfromlow_252d_base_v008_signal(gp):
    b = _f24_ramp_from_low(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-above-trend streak: fraction of last 252d above its own 252d mean
def f24ri_f24_revenue_inflection_rampup_posstreak_252d_base_v009_signal(revenue):
    ref = _mean(revenue, 252)
    on = (revenue > ref).astype(float)
    b = on.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-above-trend streak: fraction of last 504d above its own 504d median
def f24ri_f24_revenue_inflection_rampup_posstreak_504d_base_v010_signal(revenue):
    ref = revenue.rolling(504, min_periods=252).median()
    on = (revenue > ref).astype(float)
    b = on.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ramp acceleration as a level: 63d growth minus prior 63d growth
def f24ri_f24_revenue_inflection_rampup_accel_63d_base_v011_signal(revenue):
    b = _f24_accel(revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ramp acceleration as a level: 126d growth minus prior 126d growth
def f24ri_f24_revenue_inflection_rampup_accel_126d_base_v012_signal(revenue):
    b = _f24_accel(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit ramp acceleration: 63d gp growth minus prior 63d
def f24ri_f24_revenue_inflection_rampup_gpaccel_63d_base_v013_signal(gp):
    b = _f24_accel(gp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability: mean revenue growth / dispersion over 126d (consistent ramp)
def f24ri_f24_revenue_inflection_rampup_stability_126d_base_v014_signal(revenue):
    b = _f24_stability(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability over 252d (year-long ramp consistency)
def f24ri_f24_revenue_inflection_rampup_stability_252d_base_v015_signal(revenue):
    b = _f24_stability(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth stability over 252d
def f24ri_f24_revenue_inflection_rampup_gpstability_252d_base_v016_signal(gp):
    b = _f24_stability(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level (gp/revenue) — quality of the ramp
def f24ri_f24_revenue_inflection_rampup_gpmargin_base_v017_signal(gp, revenue):
    b = _f24_gp_margin(gp, revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin expansion: margin now vs 252d ago (mix improving as it ramps)
def f24ri_f24_revenue_inflection_rampup_gpmarginexp_252d_base_v018_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth percentile-rank vs its own 504d history (where in ramp cycle)
def f24ri_f24_revenue_inflection_rampup_growrank_252d_base_v019_signal(revenue):
    g = _f24_growth(revenue, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level percentile-rank vs own 1260d history (multi-year ramp position)
def f24ri_f24_revenue_inflection_rampup_levelrank_1260d_base_v020_signal(revenue):
    b = _rank(revenue, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue z-scored vs own 252d history (de-trended ramp surprise)
def f24ri_f24_revenue_inflection_rampup_revz_252d_base_v021_signal(revenue):
    b = _z(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth z-scored vs own 252d history (growth surprise)
def f24ri_f24_revenue_inflection_rampup_growz_252d_base_v022_signal(revenue):
    g = _f24_growth(revenue, 63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs its own 252d trailing mean (level above ramp baseline)
def f24ri_f24_revenue_inflection_rampup_revvsmean_252d_base_v023_signal(revenue):
    m = _mean(revenue, 252)
    b = revenue / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long revenue mean ratio (ramp momentum across MAs)
def f24ri_f24_revenue_inflection_rampup_meanratio_63v252_base_v024_signal(revenue):
    s = _mean(revenue, 63)
    l = _mean(revenue, 252)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd short-vs-long mean ratio (USD ramp momentum)
def f24ri_f24_revenue_inflection_rampup_usdmeanratio_63v252_base_v025_signal(revenueusd):
    s = _mean(revenueusd, 63)
    l = _mean(revenueusd, 252)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit short-vs-long mean ratio (profit ramp momentum)
def f24ri_f24_revenue_inflection_rampup_gpmeanratio_63v252_base_v026_signal(gp):
    s = _mean(gp, 63)
    l = _mean(gp, 252)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue drawup off 1260d trough (how far above the all-time-low base)
def f24ri_f24_revenue_inflection_rampup_drawup_1260d_base_v027_signal(revenue):
    lo = _rmin(revenue, 1260)
    b = np.log(revenue.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inflection flag: fraction of last 252d where 63d growth was positive
def f24ri_f24_revenue_inflection_rampup_growpos_252d_base_v028_signal(revenue):
    g = _f24_growth(revenue, 63)
    on = (g > 0).astype(float)
    b = on.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue regime shift: recent-252d mean vs prior-252d mean (half-over-half ramp)
def f24ri_f24_revenue_inflection_rampup_halfshift_504d_base_v029_signal(revenue):
    recent = _mean(revenue, 252)
    prior = _mean(revenue, 252).shift(252)
    b = (recent - prior) / (recent + prior).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ramp velocity ratio: 21d proportional slope vs 252d proportional slope
def f24ri_f24_revenue_inflection_rampup_velratio_21v252_base_v030_signal(revenue):
    fast = _slope(revenue, 21) / _mean(revenue, 21).replace(0, np.nan)
    slow = _slope(revenue, 252) / _mean(revenue, 252).replace(0, np.nan)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd vs revenue divergence (FX/mix component of the ramp)
def f24ri_f24_revenue_inflection_rampup_usddiverge_base_v031_signal(revenueusd, revenue):
    b = np.log(revenueusd.replace(0, np.nan) / revenue.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence: usd revenue growth minus reported revenue growth
def f24ri_f24_revenue_inflection_rampup_growdiverge_252d_base_v032_signal(revenueusd, revenue):
    b = _f24_growth(revenueusd, 252) - _f24_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-vs-revenue growth gap (operating-leverage flavor of the ramp)
def f24ri_f24_revenue_inflection_rampup_gpgrowgap_252d_base_v033_signal(gp, revenue):
    b = _f24_growth(gp, 252) - _f24_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ramp convexity: 63d growth minus 252d growth (accelerating vs steady)
def f24ri_f24_revenue_inflection_rampup_convexity_base_v034_signal(revenue):
    b = _f24_growth(revenue, 63) - _f24_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue coefficient of variation over 252d (lower => smoother ramp); negated
def f24ri_f24_revenue_inflection_rampup_negcv_252d_base_v035_signal(revenue):
    cv = _std(revenue, 252) / _mean(revenue, 252).replace(0, np.nan)
    b = -cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit above-trend streak (share of last 252d gp above its 252d mean)
def f24ri_f24_revenue_inflection_rampup_gpposstreak_252d_base_v036_signal(gp):
    ref = _mean(gp, 252)
    on = (gp > ref).astype(float)
    b = on.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd acceleration sign-magnitude over 63d (USD inflection, bounded)
def f24ri_f24_revenue_inflection_rampup_usdaccelsignmag_63d_base_v037_signal(revenueusd):
    a = _f24_accel(revenueusd, 63)
    b = np.sign(a) * np.sqrt(a.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp ramp vs cycle peak: current gp / 1260d max gp (profit saturation distance)
def f24ri_f24_revenue_inflection_rampup_gppeakprox_1260d_base_v038_signal(gp):
    hi = _rmax(gp, 1260)
    b = gp / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth smoothed (persistent ramp rate, EMA of 63d growth)
def f24ri_f24_revenue_inflection_rampup_growema_base_v039_signal(revenue):
    g = _f24_growth(revenue, 63)
    b = g.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ramp displacement: growth minus its own slow EMA (acceleration shock)
def f24ri_f24_revenue_inflection_rampup_growdisp_base_v040_signal(revenue):
    g = _f24_growth(revenue, 63)
    b = g - g.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z vs own 252d history (margin inflection surprise)
def f24ri_f24_revenue_inflection_rampup_gpmarginz_252d_base_v041_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue YoY-of-YoY: 252d growth minus the 252d growth one year ago
def f24ri_f24_revenue_inflection_rampup_growyoy_base_v042_signal(revenue):
    g = _f24_growth(revenue, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue above mid of its 504d range (ramp position in range)
def f24ri_f24_revenue_inflection_rampup_rangepos_504d_base_v043_signal(revenue):
    hi = _rmax(revenue, 504)
    lo = _rmin(revenue, 504)
    b = (revenue - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd ramp from 504d low (USD ramp lift)
def f24ri_f24_revenue_inflection_rampup_usdrampfromlow_504d_base_v044_signal(revenueusd):
    b = _f24_ramp_from_low(revenueusd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue downside-ramp risk: 126d growth per unit of downside (negative) vol
def f24ri_f24_revenue_inflection_rampup_growdownside_126d_base_v045_signal(revenue):
    g = revenue.pct_change()
    downs = g.where(g < 0, 0.0)
    semidev = (downs ** 2).rolling(126, min_periods=63).mean() ** 0.5
    b = _f24_growth(revenue, 126) / semidev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d that set a new 252d revenue high (fresh-ramp frequency)
def f24ri_f24_revenue_inflection_rampup_newhifreq_252d_base_v046_signal(revenue):
    hi = revenue.rolling(252, min_periods=126).max()
    is_hi = (revenue >= hi * 0.99999).astype(float)
    b = is_hi.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp growth risk-adjusted over 126d (quality ramp per unit gp vol)
def f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_126d_base_v047_signal(gp):
    g = _f24_growth(gp, 126)
    vol = gp.pct_change().rolling(126, min_periods=63).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd ramp curvature: 21d-step 2nd diff of log-level (USD inflection, bounded)
def f24ri_f24_revenue_inflection_rampup_usdlogcurv_21d_base_v048_signal(revenueusd):
    lv = np.log(revenueusd.replace(0, np.nan))
    curv = lv - 2.0 * lv.shift(21) + lv.shift(42)
    b = np.tanh(15.0 * curv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp vs its 252d-mean baseline ratio (gross-profit level above ramp baseline)
def f24ri_f24_revenue_inflection_rampup_gpbaselinegap_base_v049_signal(gp):
    base = _mean(gp, 252)
    b = gp / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit dollar ramp slope normalized by level (profit velocity)
def f24ri_f24_revenue_inflection_rampup_gpnormslope_126d_base_v050_signal(gp):
    sl = _slope(gp, 126)
    b = sl / _mean(gp, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp ramp dispersion across horizons (63/126/252 gp-growth disagreement)
def f24ri_f24_revenue_inflection_rampup_gphorizondisp_base_v051_signal(gp):
    g1 = _f24_growth(gp, 63)
    g2 = _f24_growth(gp, 126)
    g3 = _f24_growth(gp, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp consistency: fraction of last 126d with sequential rev increase
def f24ri_f24_revenue_inflection_rampup_seqincr_126d_base_v052_signal(revenue):
    up = (revenue > revenue.shift(21)).astype(float)
    b = up.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd z-score vs own 252d history (USD ramp surprise)
def f24ri_f24_revenue_inflection_rampup_usdz_252d_base_v053_signal(revenueusd):
    b = _z(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin range position over 504d (margin cycle phase)
def f24ri_f24_revenue_inflection_rampup_marginrangepos_504d_base_v054_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    hi = _rmax(m, 504)
    lo = _rmin(m, 504)
    b = (m - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp half-life proxy: 126d growth divided by 252d growth
def f24ri_f24_revenue_inflection_rampup_growratio_126v252_base_v055_signal(revenue):
    g_s = _f24_growth(revenue, 126)
    g_l = _f24_growth(revenue, 252)
    b = g_s / g_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp new-252d-high frequency: share of last 126d that set a fresh 252d gp high
def f24ri_f24_revenue_inflection_rampup_gpnewhifreq_base_v056_signal(gp):
    hi = gp.rolling(252, min_periods=126).max()
    is_hi = (gp >= hi * 0.99999).astype(float)
    b = is_hi.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d above the 252d revenue median (sustained-ramp share)
def f24ri_f24_revenue_inflection_rampup_abovemed_252d_base_v057_signal(revenue):
    med = revenue.rolling(252, min_periods=126).median()
    on = (revenue > med).astype(float)
    b = on.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit YoY-of-YoY (profit ramp acceleration year over year)
def f24ri_f24_revenue_inflection_rampup_gpgrowyoy_base_v058_signal(gp):
    g = _f24_growth(gp, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion-of-changes (jaggedness of the ramp); negated
def f24ri_f24_revenue_inflection_rampup_negjagged_126d_base_v059_signal(revenue):
    g = revenue.pct_change()
    b = -g.diff().abs().rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-ramp composite: growth-stability x gross-margin level (quality ramp)
def f24ri_f24_revenue_inflection_rampup_durableramp_base_v060_signal(revenue, gp):
    stab = np.tanh(_f24_stability(revenue, 252))
    margin = _f24_gp_margin(gp, revenue).clip(lower=0, upper=1)
    b = stab * margin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp vs gp ramp interaction (revenue ramp confirmed by profit ramp)
def f24ri_f24_revenue_inflection_rampup_confirmedramp_base_v061_signal(revenue, gp):
    rg = _f24_growth(revenue, 252)
    gg = _f24_growth(gp, 252)
    b = np.sign(rg) * np.sqrt((rg * gg).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level relative to 1260d mean (long-run ramp magnitude)
def f24ri_f24_revenue_inflection_rampup_vslongmean_1260d_base_v062_signal(revenue):
    m = _mean(revenue, 1260)
    b = revenue / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd growth percentile rank over 504d (USD ramp position)
def f24ri_f24_revenue_inflection_rampup_usdgrowrank_504d_base_v063_signal(revenueusd):
    g = _f24_growth(revenueusd, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin curvature: 2nd diff of margin over a quarter (margin inflection)
def f24ri_f24_revenue_inflection_rampup_margincurv_63d_base_v064_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    b = m - 2.0 * m.shift(63) + m.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of 21d-sequential revenue gains in last 252d (ramp-step tally)
def f24ri_f24_revenue_inflection_rampup_stepcount_252d_base_v065_signal(revenue):
    up = (revenue > revenue.shift(21) * 1.02).astype(float)
    b = up.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ramp-stall persistence: share of last 126d revenue sat >3% below 252d high
def f24ri_f24_revenue_inflection_rampup_rampstall_252d_base_v066_signal(revenue):
    hi = _rmax(revenue, 252)
    underr = revenue / hi.replace(0, np.nan) - 1.0
    stalled = (underr <= -0.03).astype(float)
    b = stalled.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp ramp from 1260d low (long-run gross-profit lift)
def f24ri_f24_revenue_inflection_rampup_gpdrawup_1260d_base_v067_signal(gp):
    lo = _rmin(gp, 1260)
    b = np.log(gp.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit acceleration risk-adjusted (gp accel per unit gp-growth vol, 63d)
def f24ri_f24_revenue_inflection_rampup_gpaccelriskadj_63d_base_v068_signal(gp):
    a = _f24_accel(gp, 63)
    vol = _f24_growth(gp, 21).rolling(126, min_periods=63).std()
    b = a / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs revenueusd ramp blend (avg of the two YoY growths)
def f24ri_f24_revenue_inflection_rampup_blendgrow_252d_base_v069_signal(revenue, revenueusd):
    b = 0.5 * (_f24_growth(revenue, 252) + _f24_growth(revenueusd, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin EMA crossover gap (fast vs slow margin trend during ramp)
def f24ri_f24_revenue_inflection_rampup_marginemagap_base_v070_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    fast = m.ewm(span=42, min_periods=21).mean()
    slow = m.ewm(span=189, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of last 504d with gp margin above its 504d median (margin durability)
def f24ri_f24_revenue_inflection_rampup_marginabovemed_504d_base_v071_signal(gp, revenue):
    m = _f24_gp_margin(gp, revenue)
    med = m.rolling(504, min_periods=252).median()
    on = (m > med).astype(float)
    b = on.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp velocity vs prior-year velocity (inflection of the slope)
def f24ri_f24_revenue_inflection_rampup_velchange_base_v072_signal(revenue):
    v = _slope(revenue, 126) / _mean(revenue, 126).replace(0, np.nan)
    b = v - v.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenueusd vs revenue level ratio z-scored (FX/mix surprise of ramp)
def f24ri_f24_revenue_inflection_rampup_usdratioz_base_v073_signal(revenueusd, revenue):
    r = revenueusd / revenue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue ramp purity: log-level minus its 252d linear baseline (excess ramp)
def f24ri_f24_revenue_inflection_rampup_excessramp_252d_base_v074_signal(revenue):
    lv = np.log(revenue.replace(0, np.nan))
    base = lv.rolling(252, min_periods=126).mean() + _slope(lv, 252) * 126.0
    b = lv - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite inflection score: growth x ramp-from-low x margin-expansion
def f24ri_f24_revenue_inflection_rampup_inflectscore_base_v075_signal(revenue, gp):
    g = np.tanh(_f24_growth(revenue, 252))
    lift = np.tanh(_f24_ramp_from_low(revenue, 504))
    me = np.tanh(50.0 * (_f24_gp_margin(gp, revenue) - _f24_gp_margin(gp, revenue).shift(252)))
    b = (g + lift + me) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24ri_f24_revenue_inflection_rampup_revgrow_63d_base_v001_signal,
    f24ri_f24_revenue_inflection_rampup_revgrow_126d_base_v002_signal,
    f24ri_f24_revenue_inflection_rampup_revgrow_252d_base_v003_signal,
    f24ri_f24_revenue_inflection_rampup_revusdgrow_252d_base_v004_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrow_252d_base_v005_signal,
    f24ri_f24_revenue_inflection_rampup_daystrough_252d_base_v006_signal,
    f24ri_f24_revenue_inflection_rampup_rampfromlow_504d_base_v007_signal,
    f24ri_f24_revenue_inflection_rampup_gprampfromlow_252d_base_v008_signal,
    f24ri_f24_revenue_inflection_rampup_posstreak_252d_base_v009_signal,
    f24ri_f24_revenue_inflection_rampup_posstreak_504d_base_v010_signal,
    f24ri_f24_revenue_inflection_rampup_accel_63d_base_v011_signal,
    f24ri_f24_revenue_inflection_rampup_accel_126d_base_v012_signal,
    f24ri_f24_revenue_inflection_rampup_gpaccel_63d_base_v013_signal,
    f24ri_f24_revenue_inflection_rampup_stability_126d_base_v014_signal,
    f24ri_f24_revenue_inflection_rampup_stability_252d_base_v015_signal,
    f24ri_f24_revenue_inflection_rampup_gpstability_252d_base_v016_signal,
    f24ri_f24_revenue_inflection_rampup_gpmargin_base_v017_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginexp_252d_base_v018_signal,
    f24ri_f24_revenue_inflection_rampup_growrank_252d_base_v019_signal,
    f24ri_f24_revenue_inflection_rampup_levelrank_1260d_base_v020_signal,
    f24ri_f24_revenue_inflection_rampup_revz_252d_base_v021_signal,
    f24ri_f24_revenue_inflection_rampup_growz_252d_base_v022_signal,
    f24ri_f24_revenue_inflection_rampup_revvsmean_252d_base_v023_signal,
    f24ri_f24_revenue_inflection_rampup_meanratio_63v252_base_v024_signal,
    f24ri_f24_revenue_inflection_rampup_usdmeanratio_63v252_base_v025_signal,
    f24ri_f24_revenue_inflection_rampup_gpmeanratio_63v252_base_v026_signal,
    f24ri_f24_revenue_inflection_rampup_drawup_1260d_base_v027_signal,
    f24ri_f24_revenue_inflection_rampup_growpos_252d_base_v028_signal,
    f24ri_f24_revenue_inflection_rampup_halfshift_504d_base_v029_signal,
    f24ri_f24_revenue_inflection_rampup_velratio_21v252_base_v030_signal,
    f24ri_f24_revenue_inflection_rampup_usddiverge_base_v031_signal,
    f24ri_f24_revenue_inflection_rampup_growdiverge_252d_base_v032_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowgap_252d_base_v033_signal,
    f24ri_f24_revenue_inflection_rampup_convexity_base_v034_signal,
    f24ri_f24_revenue_inflection_rampup_negcv_252d_base_v035_signal,
    f24ri_f24_revenue_inflection_rampup_gpposstreak_252d_base_v036_signal,
    f24ri_f24_revenue_inflection_rampup_usdaccelsignmag_63d_base_v037_signal,
    f24ri_f24_revenue_inflection_rampup_gppeakprox_1260d_base_v038_signal,
    f24ri_f24_revenue_inflection_rampup_growema_base_v039_signal,
    f24ri_f24_revenue_inflection_rampup_growdisp_base_v040_signal,
    f24ri_f24_revenue_inflection_rampup_gpmarginz_252d_base_v041_signal,
    f24ri_f24_revenue_inflection_rampup_growyoy_base_v042_signal,
    f24ri_f24_revenue_inflection_rampup_rangepos_504d_base_v043_signal,
    f24ri_f24_revenue_inflection_rampup_usdrampfromlow_504d_base_v044_signal,
    f24ri_f24_revenue_inflection_rampup_growdownside_126d_base_v045_signal,
    f24ri_f24_revenue_inflection_rampup_newhifreq_252d_base_v046_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowriskadj_126d_base_v047_signal,
    f24ri_f24_revenue_inflection_rampup_usdlogcurv_21d_base_v048_signal,
    f24ri_f24_revenue_inflection_rampup_gpbaselinegap_base_v049_signal,
    f24ri_f24_revenue_inflection_rampup_gpnormslope_126d_base_v050_signal,
    f24ri_f24_revenue_inflection_rampup_gphorizondisp_base_v051_signal,
    f24ri_f24_revenue_inflection_rampup_seqincr_126d_base_v052_signal,
    f24ri_f24_revenue_inflection_rampup_usdz_252d_base_v053_signal,
    f24ri_f24_revenue_inflection_rampup_marginrangepos_504d_base_v054_signal,
    f24ri_f24_revenue_inflection_rampup_growratio_126v252_base_v055_signal,
    f24ri_f24_revenue_inflection_rampup_gpnewhifreq_base_v056_signal,
    f24ri_f24_revenue_inflection_rampup_abovemed_252d_base_v057_signal,
    f24ri_f24_revenue_inflection_rampup_gpgrowyoy_base_v058_signal,
    f24ri_f24_revenue_inflection_rampup_negjagged_126d_base_v059_signal,
    f24ri_f24_revenue_inflection_rampup_durableramp_base_v060_signal,
    f24ri_f24_revenue_inflection_rampup_confirmedramp_base_v061_signal,
    f24ri_f24_revenue_inflection_rampup_vslongmean_1260d_base_v062_signal,
    f24ri_f24_revenue_inflection_rampup_usdgrowrank_504d_base_v063_signal,
    f24ri_f24_revenue_inflection_rampup_margincurv_63d_base_v064_signal,
    f24ri_f24_revenue_inflection_rampup_stepcount_252d_base_v065_signal,
    f24ri_f24_revenue_inflection_rampup_rampstall_252d_base_v066_signal,
    f24ri_f24_revenue_inflection_rampup_gpdrawup_1260d_base_v067_signal,
    f24ri_f24_revenue_inflection_rampup_gpaccelriskadj_63d_base_v068_signal,
    f24ri_f24_revenue_inflection_rampup_blendgrow_252d_base_v069_signal,
    f24ri_f24_revenue_inflection_rampup_marginemagap_base_v070_signal,
    f24ri_f24_revenue_inflection_rampup_marginabovemed_504d_base_v071_signal,
    f24ri_f24_revenue_inflection_rampup_velchange_base_v072_signal,
    f24ri_f24_revenue_inflection_rampup_usdratioz_base_v073_signal,
    f24ri_f24_revenue_inflection_rampup_excessramp_252d_base_v074_signal,
    f24ri_f24_revenue_inflection_rampup_inflectscore_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_REVENUE_INFLECTION_RAMPUP_REGISTRY_001_075 = REGISTRY


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

    # revenue ramps up strongly (explorer -> producer); gp follows with margin noise
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

    print("OK f24_revenue_inflection_rampup_base_001_075_claude: %d features pass" % n_features)
