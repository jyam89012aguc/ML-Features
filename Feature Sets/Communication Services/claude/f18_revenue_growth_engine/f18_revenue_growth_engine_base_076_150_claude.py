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
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (revenue growth engine) =====
def _f18_growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f18_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f18_cagr(s, w, periods_per_year=252.0):
    r = s / s.shift(w).replace(0, np.nan)
    expo = periods_per_year / float(w)
    return np.power(r.clip(lower=1e-9), expo) - 1.0


def _f18_growth_accel(s, w):
    g = s / s.shift(w).replace(0, np.nan) - 1.0
    return g - g.shift(w)


def _f18_growth_stability(s, w):
    dl = np.log(s.replace(0, np.nan)).diff()
    m = dl.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = dl.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


# ============================================================
# revenue growth z (21d growth vs 126d history) — short-window normalized impulse
def f18rg_f18_revenue_growth_engine_gz_21d_base_v076_signal(revenue):
    g = _f18_growth(revenue, 21)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth rank (21d growth vs 252d history)
def f18rg_f18_revenue_growth_engine_grank_21d_base_v077_signal(revenue):
    g = _f18_growth(revenue, 21)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-revenue growth z (63d vs 252d history)
def f18rg_f18_revenue_growth_engine_gzusd_63d_base_v078_signal(revenueusd):
    g = _f18_growth(revenueusd, 63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth rank (63d vs 504d history)
def f18rg_f18_revenue_growth_engine_grankgp_63d_base_v079_signal(gp):
    g = _f18_growth(gp, 63)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration (USD, 126d) as level
def f18rg_f18_revenue_growth_engine_accelusd_126d_base_v080_signal(revenueusd):
    b = _f18_growth_accel(revenueusd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration (gp, 126d) as level
def f18rg_f18_revenue_growth_engine_accelgp_126d_base_v081_signal(gp):
    b = _f18_growth_accel(gp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration (gp, 252d) as level
def f18rg_f18_revenue_growth_engine_accelgp_252d_base_v082_signal(gp):
    b = _f18_growth_accel(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth dispersion of USD revenue (std of 63d growth over a year)
def f18rg_f18_revenue_growth_engine_gdispusd_252d_base_v083_signal(revenueusd):
    g = _f18_growth(revenueusd, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth dispersion (std of 63d gp-growth over a year)
def f18rg_f18_revenue_growth_engine_gdispgp_252d_base_v084_signal(gp):
    g = _f18_growth(gp, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of revenue level over a year (inverse stability scale)
def f18rg_f18_revenue_growth_engine_revcv_252d_base_v085_signal(revenue):
    b = _std(revenue, 252) / _mean(revenue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit coefficient of variation over a year
def f18rg_f18_revenue_growth_engine_gpcv_252d_base_v086_signal(gp):
    b = _std(gp, 252) / _mean(gp, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level vs its own 126d trailing mean (scale-detrended momentum)
def f18rg_f18_revenue_growth_engine_lvlmean_126d_base_v087_signal(revenue):
    b = revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD revenue level vs its own 252d trailing mean
def f18rg_f18_revenue_growth_engine_lvlmeanusd_252d_base_v088_signal(revenueusd):
    b = revenueusd / _mean(revenueusd, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level position in its own 252d range (growth-cycle maturity)
def f18rg_f18_revenue_growth_engine_lvlpos_252d_base_v089_signal(revenue):
    hi = revenue.rolling(252, min_periods=126).max()
    lo = revenue.rolling(252, min_periods=126).min()
    b = (revenue - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit level position in its own 252d range
def f18rg_f18_revenue_growth_engine_gplvlpos_252d_base_v090_signal(gp):
    hi = gp.rolling(252, min_periods=126).max()
    lo = gp.rolling(252, min_periods=126).min()
    b = (gp - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-revenue-high frequency over the last quarter (growth-engine vigor)
def f18rg_f18_revenue_growth_engine_newhi_252d_base_v091_signal(revenue):
    hi = revenue.rolling(252, min_periods=126).max()
    is_hi = (revenue >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since last revenue high (staleness of the growth engine)
def f18rg_f18_revenue_growth_engine_dsrh_252d_base_v092_signal(revenue):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = revenue.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue drawdown from trailing-year peak (growth stall depth)
def f18rg_f18_revenue_growth_engine_revdd_252d_base_v093_signal(revenue):
    peak = revenue.rolling(252, min_periods=126).max()
    b = revenue / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit drawdown from trailing-year peak
def f18rg_f18_revenue_growth_engine_gpdd_252d_base_v094_signal(gp):
    peak = gp.rolling(252, min_periods=126).max()
    b = gp / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue recovery off trailing-year trough (re-acceleration)
def f18rg_f18_revenue_growth_engine_revrec_252d_base_v095_signal(revenue):
    trough = revenue.rolling(252, min_periods=126).min()
    b = revenue / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-acceleration rank (126d accel vs 504d history)
def f18rg_f18_revenue_growth_engine_accrank_126d_base_v096_signal(revenue):
    a = _f18_growth_accel(revenue, 126)
    b = _rank(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-acceleration z (252d accel vs 504d history)
def f18rg_f18_revenue_growth_engine_accz_252d_base_v097_signal(revenue):
    a = _f18_growth_accel(revenue, 252)
    b = _z(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-vs-USD level divergence (FX / mix gap as a level)
def f18rg_f18_revenue_growth_engine_fxlvl_base_v098_signal(revenueusd, revenue):
    b = revenueusd / revenue.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in revenue-vs-USD divergence over a quarter (FX momentum)
def f18rg_f18_revenue_growth_engine_fxmom_63d_base_v099_signal(revenueusd, revenue):
    ratio = revenueusd / revenue.replace(0, np.nan)
    b = ratio / ratio.shift(63).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin proxy from gp/revenue (level of value-capture in growth)
def f18rg_f18_revenue_growth_engine_gpmargin_base_v100_signal(gp, revenue):
    b = gp / revenue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin-proxy trend: change in gp/revenue over a half-year
def f18rg_f18_revenue_growth_engine_gpmargmom_126d_base_v101_signal(gp, revenue):
    m = gp / revenue.replace(0, np.nan)
    b = m - m.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin-proxy z-score vs own year (value-capture regime)
def f18rg_f18_revenue_growth_engine_gpmargz_252d_base_v102_signal(gp, revenue):
    m = gp / revenue.replace(0, np.nan)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth quality: 126d revenue growth times gross-margin-proxy z-score (quality-weighted)
def f18rg_f18_revenue_growth_engine_gqual_63d_base_v103_signal(revenue, gp):
    g = _f18_growth(revenue, 126)
    m = gp / revenue.replace(0, np.nan)
    b = g * _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth positive-quarter count over two years (durability tally)
def f18rg_f18_revenue_growth_engine_poscount_504d_base_v104_signal(revenue):
    g = _f18_growth(revenue, 63)
    pos = (g > 0).astype(float)
    b = pos.rolling(504, min_periods=252).sum() / 504.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth acceleration positive-fraction over a year (improving trend tally)
def f18rg_f18_revenue_growth_engine_accpos_252d_base_v105_signal(revenue):
    a = _f18_growth_accel(revenue, 63)
    pos = (a > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth skewness proxy: (mean - median) of 21d growth over a year
def f18rg_f18_revenue_growth_engine_gskew_252d_base_v106_signal(revenue):
    g = _f18_growth(revenue, 21)
    m = g.rolling(252, min_periods=126).mean()
    med = g.rolling(252, min_periods=126).median()
    b = (m - med) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth skewness proxy over a year
def f18rg_f18_revenue_growth_engine_gpskew_252d_base_v107_signal(gp):
    g = _f18_growth(gp, 21)
    m = g.rolling(252, min_periods=126).mean()
    med = g.rolling(252, min_periods=126).median()
    b = (m - med) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth upside semi-deviation: std of positive 21d growth deviations over a year
def f18rg_f18_revenue_growth_engine_gupsemi_252d_base_v108_signal(revenue):
    g = _f18_growth(revenue, 21)
    m = g.rolling(252, min_periods=126).mean()
    dev = (g - m).clip(lower=0)
    b = (dev ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth downside semi-deviation: std of negative 21d growth deviations (stall risk)
def f18rg_f18_revenue_growth_engine_gdnsemi_252d_base_v109_signal(revenue):
    g = _f18_growth(revenue, 21)
    m = g.rolling(252, min_periods=126).mean()
    dev = (g - m).clip(upper=0)
    b = (dev ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth semi-deviation skew: upside minus downside semi-deviation
def f18rg_f18_revenue_growth_engine_gsemiskew_252d_base_v110_signal(revenue):
    g = _f18_growth(revenue, 21)
    m = g.rolling(252, min_periods=126).mean()
    up = ((g - m).clip(lower=0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    dn = ((g - m).clip(upper=0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth vol-of-vol: std over a quarter of the 63d-rolling growth dispersion
def f18rg_f18_revenue_growth_engine_gvov_base_v111_signal(revenue):
    g = _f18_growth(revenue, 21)
    disp = _std(g, 63)
    b = _std(disp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth efficiency ratio: net 252d move over summed monthly abs moves
def f18rg_f18_revenue_growth_engine_geff_252d_base_v112_signal(revenue):
    net = (revenue - revenue.shift(252)).abs()
    path = (revenue - revenue.shift(21)).abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth efficiency ratio over a year
def f18rg_f18_revenue_growth_engine_gpeff_252d_base_v113_signal(gp):
    net = (gp - gp.shift(252)).abs()
    path = (gp - gp.shift(21)).abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth autocorrelation proxy: corr of 21d growth with its 21d lag (1yr)
def f18rg_f18_revenue_growth_engine_gautoc_252d_base_v114_signal(revenue):
    g = _f18_growth(revenue, 21)
    b = g.rolling(252, min_periods=126).corr(g.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs gross-profit growth co-movement: rolling corr of their 21d growths
def f18rg_f18_revenue_growth_engine_revgpcorr_252d_base_v115_signal(revenue, gp):
    gr = _f18_growth(revenue, 21)
    gg = _f18_growth(gp, 21)
    b = gr.rolling(252, min_periods=126).corr(gg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth term ratio: 21d-annualized over 252d growth (near-term pace premium)
def f18rg_f18_revenue_growth_engine_gtermr_21v252_base_v116_signal(revenue):
    near = (1.0 + _f18_growth(revenue, 21)).clip(lower=1e-9) ** 12 - 1.0
    longg = _f18_growth(revenue, 252)
    b = near - longg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD growth term-structure: 63d minus 252d USD growth
def f18rg_f18_revenue_growth_engine_gtermusd_base_v117_signal(revenueusd):
    s = _f18_growth(revenueusd, 63)
    l = _f18_growth(revenueusd, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth term-structure: 63d minus 252d gp growth
def f18rg_f18_revenue_growth_engine_gtermgp_base_v118_signal(gp):
    s = _f18_growth(gp, 63)
    l = _f18_growth(gp, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth EMA (126d growth smoothed) — persistent half-year pace
def f18rg_f18_revenue_growth_engine_gema_126d_base_v119_signal(revenue):
    g = _f18_growth(revenue, 126)
    b = g.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth EMA displacement (63d gp-growth minus its slow EMA)
def f18rg_f18_revenue_growth_engine_gpemadisp_base_v120_signal(gp):
    g = _f18_growth(gp, 63)
    b = g - g.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth tanh of its z-score (bounded regime extremity, 63d/252d)
def f18rg_f18_revenue_growth_engine_gztanh_63d_base_v121_signal(revenue):
    z = _z(_f18_growth(revenue, 63), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth sign-magnitude of 126d growth (compressed YoY-ish growth)
def f18rg_f18_revenue_growth_engine_gsignmag_126d_base_v122_signal(revenue):
    g = _f18_growth(revenue, 126)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-revenue growth sign-magnitude (252d, compressed)
def f18rg_f18_revenue_growth_engine_gsignmagusd_252d_base_v123_signal(revenueusd):
    g = _f18_growth(revenueusd, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted gross-profit growth: 252d gp-growth over its 63d-growth dispersion
def f18rg_f18_revenue_growth_engine_radjgp_252d_base_v124_signal(gp):
    g = _f18_growth(gp, 252)
    disp = _std(_f18_growth(gp, 63), 252)
    b = g / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted USD growth: 252d USD-growth over its 63d-growth dispersion
def f18rg_f18_revenue_growth_engine_radjusd_252d_base_v125_signal(revenueusd):
    g = _f18_growth(revenueusd, 252)
    disp = _std(_f18_growth(revenueusd, 63), 252)
    b = g / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality spread (USD vs gp, 126d): which side scales faster
def f18rg_f18_revenue_growth_engine_gqsprusdgp_base_v126_signal(revenueusd, gp):
    gu = _f18_growth(revenueusd, 126)
    gg = _f18_growth(gp, 126)
    b = gg - gu
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth concavity: 1+g over 126d minus square of 1+g over 63d (path concavity)
def f18rg_f18_revenue_growth_engine_gconcav_base_v127_signal(revenue):
    g63 = _f18_growth(revenue, 63)
    g126 = _f18_growth(revenue, 126)
    b = (1.0 + g126) - (1.0 + g63) ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth concavity (126 vs 63 compounding)
def f18rg_f18_revenue_growth_engine_gpconcav_base_v128_signal(gp):
    g63 = _f18_growth(gp, 63)
    g126 = _f18_growth(gp, 126)
    b = (1.0 + g126) - (1.0 + g63) ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth momentum: 21d growth smoothed, change over a month (short impulse)
def f18rg_f18_revenue_growth_engine_gmom_21lag_base_v129_signal(revenue):
    g = _f18_growth(revenue, 21).rolling(21, min_periods=10).mean()
    b = g - g.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-revenue growth momentum: 126d growth change over a quarter
def f18rg_f18_revenue_growth_engine_gmomusd_63lag_base_v130_signal(revenueusd):
    g = _f18_growth(revenueusd, 126)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth half-life proxy: ratio of recent-quarter to prior-quarter dispersion
def f18rg_f18_revenue_growth_engine_gdisprat_base_v131_signal(revenue):
    g = _f18_growth(revenue, 21)
    recent = _std(g, 63)
    prior = _std(g, 63).shift(63)
    b = recent / prior.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level log-acceleration over half-year spans, smoothed (persistent curvature)
def f18rg_f18_revenue_growth_engine_logaccel_base_v132_signal(revenue):
    lg = np.log(revenue.replace(0, np.nan))
    accel = (lg - lg.shift(126)) - (lg.shift(126) - lg.shift(252))
    b = accel.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit log-acceleration over half-year spans, z-scored vs two-year history
def f18rg_f18_revenue_growth_engine_gplogaccel_base_v133_signal(gp):
    lg = np.log(gp.replace(0, np.nan))
    accel = (lg - lg.shift(126)) - (lg.shift(126) - lg.shift(252))
    b = _z(accel, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth percentile crossover: 63d-growth rank minus 252d-growth rank
def f18rg_f18_revenue_growth_engine_grankspr_base_v134_signal(revenue):
    r1 = _rank(_f18_growth(revenue, 63), 504)
    r2 = _rank(_f18_growth(revenue, 252), 504)
    b = r1 - r2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability spread: revenue stability minus gross-profit stability (252d)
def f18rg_f18_revenue_growth_engine_stabspr_base_v135_signal(revenue, gp):
    sr = _f18_growth_stability(revenue, 252)
    sg = _f18_growth_stability(gp, 252)
    b = sr - sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth z minus USD growth z (where reported vs USD growth diverge, 63d)
def f18rg_f18_revenue_growth_engine_gzfxspr_base_v136_signal(revenue, revenueusd):
    zr = _z(_f18_growth(revenue, 63), 252)
    zu = _z(_f18_growth(revenueusd, 63), 252)
    b = zr - zu
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth above-trend streak: months 21d-growth exceeds its yearly median
def f18rg_f18_revenue_growth_engine_gabovestreak_base_v137_signal(revenue):
    g = _f18_growth(revenue, 21)
    med = g.rolling(252, min_periods=126).median()
    above = (g > med).astype(float)
    grp = (above != above.shift(1)).cumsum()
    streak = above.groupby(grp).cumsum()
    b = (streak * above).clip(upper=126) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit new-high frequency over a quarter (margin-dollar vigor)
def f18rg_f18_revenue_growth_engine_gpnewhi_base_v138_signal(gp):
    hi = gp.rolling(252, min_periods=126).max()
    is_hi = (gp >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration-to-growth ratio (how much of growth is acceleration, 126d)
def f18rg_f18_revenue_growth_engine_acc2g_126d_base_v139_signal(revenue):
    g = _f18_growth(revenue, 126)
    a = _f18_growth_accel(revenue, 126)
    b = a / (g.abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-weighted margin expansion: gp-margin trend times revenue growth (63d)
def f18rg_f18_revenue_growth_engine_marggrow_base_v140_signal(gp, revenue):
    m = gp / revenue.replace(0, np.nan)
    mtrend = m - m.shift(63)
    g = _f18_growth(revenue, 63)
    b = mtrend * np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue compounding consistency: std of log monthly growth normalized by drift (252d)
def f18rg_f18_revenue_growth_engine_gcompcons_base_v141_signal(revenue):
    dl = np.log(revenue.replace(0, np.nan)).diff(21)
    b = dl.rolling(252, min_periods=126).std() / dl.rolling(252, min_periods=126).mean().abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD CAGR (252d) ranked vs its own two-year history
def f18rg_f18_revenue_growth_engine_cagrusdrank_base_v142_signal(revenueusd):
    c = _f18_cagr(revenueusd, 252)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit CAGR (126d) momentum: change in annualized gp-CAGR over a quarter
def f18rg_f18_revenue_growth_engine_cagrgpz_base_v143_signal(gp):
    c = _f18_cagr(gp, 126)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth range width: max minus min of 63d growth over a year (cycle amplitude)
def f18rg_f18_revenue_growth_engine_grange_252d_base_v144_signal(revenue):
    g = _f18_growth(revenue, 63)
    hi = g.rolling(252, min_periods=126).max()
    lo = g.rolling(252, min_periods=126).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth range width over a year
def f18rg_f18_revenue_growth_engine_gprange_252d_base_v145_signal(gp):
    g = _f18_growth(gp, 63)
    hi = g.rolling(252, min_periods=126).max()
    lo = g.rolling(252, min_periods=126).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth distance from year-high growth (how far off peak pace)
def f18rg_f18_revenue_growth_engine_gpeakdist_base_v146_signal(revenue):
    g = _f18_growth(revenue, 63)
    hi = g.rolling(252, min_periods=126).max()
    b = (g - hi) / (hi.abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth quality composite: rank of growth times margin-proxy level (63d)
def f18rg_f18_revenue_growth_engine_gqualcomp_base_v147_signal(revenue, gp):
    rnk = _rank(_f18_growth(revenue, 63), 504)
    m = gp / revenue.replace(0, np.nan)
    b = rnk * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth: positive-growth fraction times mean 63d growth (durability x pace)
def f18rg_f18_revenue_growth_engine_durcomp_base_v148_signal(revenue):
    g = _f18_growth(revenue, 63)
    frac = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    b = frac * _mean(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accel-quality: revenue growth acceleration times gross-margin proxy (improving & profitable)
def f18rg_f18_revenue_growth_engine_accqual_base_v149_signal(revenue, gp):
    a = _f18_growth_accel(revenue, 63)
    m = gp / revenue.replace(0, np.nan)
    b = np.sign(a) * (a.abs() ** 0.5) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-engine composite: stability x rank x margin-proxy (durable profitable growth)
def f18rg_f18_revenue_growth_engine_engine_base_v150_signal(revenue, gp):
    stab = np.tanh(_f18_growth_stability(revenue, 252))
    rnk = _rank(_f18_growth(revenue, 126), 504)
    m = gp / revenue.replace(0, np.nan)
    b = stab * rnk * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18rg_f18_revenue_growth_engine_gz_21d_base_v076_signal,
    f18rg_f18_revenue_growth_engine_grank_21d_base_v077_signal,
    f18rg_f18_revenue_growth_engine_gzusd_63d_base_v078_signal,
    f18rg_f18_revenue_growth_engine_grankgp_63d_base_v079_signal,
    f18rg_f18_revenue_growth_engine_accelusd_126d_base_v080_signal,
    f18rg_f18_revenue_growth_engine_accelgp_126d_base_v081_signal,
    f18rg_f18_revenue_growth_engine_accelgp_252d_base_v082_signal,
    f18rg_f18_revenue_growth_engine_gdispusd_252d_base_v083_signal,
    f18rg_f18_revenue_growth_engine_gdispgp_252d_base_v084_signal,
    f18rg_f18_revenue_growth_engine_revcv_252d_base_v085_signal,
    f18rg_f18_revenue_growth_engine_gpcv_252d_base_v086_signal,
    f18rg_f18_revenue_growth_engine_lvlmean_126d_base_v087_signal,
    f18rg_f18_revenue_growth_engine_lvlmeanusd_252d_base_v088_signal,
    f18rg_f18_revenue_growth_engine_lvlpos_252d_base_v089_signal,
    f18rg_f18_revenue_growth_engine_gplvlpos_252d_base_v090_signal,
    f18rg_f18_revenue_growth_engine_newhi_252d_base_v091_signal,
    f18rg_f18_revenue_growth_engine_dsrh_252d_base_v092_signal,
    f18rg_f18_revenue_growth_engine_revdd_252d_base_v093_signal,
    f18rg_f18_revenue_growth_engine_gpdd_252d_base_v094_signal,
    f18rg_f18_revenue_growth_engine_revrec_252d_base_v095_signal,
    f18rg_f18_revenue_growth_engine_accrank_126d_base_v096_signal,
    f18rg_f18_revenue_growth_engine_accz_252d_base_v097_signal,
    f18rg_f18_revenue_growth_engine_fxlvl_base_v098_signal,
    f18rg_f18_revenue_growth_engine_fxmom_63d_base_v099_signal,
    f18rg_f18_revenue_growth_engine_gpmargin_base_v100_signal,
    f18rg_f18_revenue_growth_engine_gpmargmom_126d_base_v101_signal,
    f18rg_f18_revenue_growth_engine_gpmargz_252d_base_v102_signal,
    f18rg_f18_revenue_growth_engine_gqual_63d_base_v103_signal,
    f18rg_f18_revenue_growth_engine_poscount_504d_base_v104_signal,
    f18rg_f18_revenue_growth_engine_accpos_252d_base_v105_signal,
    f18rg_f18_revenue_growth_engine_gskew_252d_base_v106_signal,
    f18rg_f18_revenue_growth_engine_gpskew_252d_base_v107_signal,
    f18rg_f18_revenue_growth_engine_gupsemi_252d_base_v108_signal,
    f18rg_f18_revenue_growth_engine_gdnsemi_252d_base_v109_signal,
    f18rg_f18_revenue_growth_engine_gsemiskew_252d_base_v110_signal,
    f18rg_f18_revenue_growth_engine_gvov_base_v111_signal,
    f18rg_f18_revenue_growth_engine_geff_252d_base_v112_signal,
    f18rg_f18_revenue_growth_engine_gpeff_252d_base_v113_signal,
    f18rg_f18_revenue_growth_engine_gautoc_252d_base_v114_signal,
    f18rg_f18_revenue_growth_engine_revgpcorr_252d_base_v115_signal,
    f18rg_f18_revenue_growth_engine_gtermr_21v252_base_v116_signal,
    f18rg_f18_revenue_growth_engine_gtermusd_base_v117_signal,
    f18rg_f18_revenue_growth_engine_gtermgp_base_v118_signal,
    f18rg_f18_revenue_growth_engine_gema_126d_base_v119_signal,
    f18rg_f18_revenue_growth_engine_gpemadisp_base_v120_signal,
    f18rg_f18_revenue_growth_engine_gztanh_63d_base_v121_signal,
    f18rg_f18_revenue_growth_engine_gsignmag_126d_base_v122_signal,
    f18rg_f18_revenue_growth_engine_gsignmagusd_252d_base_v123_signal,
    f18rg_f18_revenue_growth_engine_radjgp_252d_base_v124_signal,
    f18rg_f18_revenue_growth_engine_radjusd_252d_base_v125_signal,
    f18rg_f18_revenue_growth_engine_gqsprusdgp_base_v126_signal,
    f18rg_f18_revenue_growth_engine_gconcav_base_v127_signal,
    f18rg_f18_revenue_growth_engine_gpconcav_base_v128_signal,
    f18rg_f18_revenue_growth_engine_gmom_21lag_base_v129_signal,
    f18rg_f18_revenue_growth_engine_gmomusd_63lag_base_v130_signal,
    f18rg_f18_revenue_growth_engine_gdisprat_base_v131_signal,
    f18rg_f18_revenue_growth_engine_logaccel_base_v132_signal,
    f18rg_f18_revenue_growth_engine_gplogaccel_base_v133_signal,
    f18rg_f18_revenue_growth_engine_grankspr_base_v134_signal,
    f18rg_f18_revenue_growth_engine_stabspr_base_v135_signal,
    f18rg_f18_revenue_growth_engine_gzfxspr_base_v136_signal,
    f18rg_f18_revenue_growth_engine_gabovestreak_base_v137_signal,
    f18rg_f18_revenue_growth_engine_gpnewhi_base_v138_signal,
    f18rg_f18_revenue_growth_engine_acc2g_126d_base_v139_signal,
    f18rg_f18_revenue_growth_engine_marggrow_base_v140_signal,
    f18rg_f18_revenue_growth_engine_gcompcons_base_v141_signal,
    f18rg_f18_revenue_growth_engine_cagrusdrank_base_v142_signal,
    f18rg_f18_revenue_growth_engine_cagrgpz_base_v143_signal,
    f18rg_f18_revenue_growth_engine_grange_252d_base_v144_signal,
    f18rg_f18_revenue_growth_engine_gprange_252d_base_v145_signal,
    f18rg_f18_revenue_growth_engine_gpeakdist_base_v146_signal,
    f18rg_f18_revenue_growth_engine_gqualcomp_base_v147_signal,
    f18rg_f18_revenue_growth_engine_durcomp_base_v148_signal,
    f18rg_f18_revenue_growth_engine_accqual_base_v149_signal,
    f18rg_f18_revenue_growth_engine_engine_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_REVENUE_GROWTH_ENGINE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(101, base=1.5e8, drift=0.035, vol=0.08).rename("revenue")
    revenueusd = _fund(102, base=1.5e8, drift=0.033, vol=0.085).rename("revenueusd")
    gp = _fund(103, base=6.0e7, drift=0.040, vol=0.10).rename("gp")

    cols = {"revenue": revenue, "revenueusd": revenueusd, "gp": gp}

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

    print("OK f18_revenue_growth_engine_base_076_150_claude: %d features pass" % n_features)
