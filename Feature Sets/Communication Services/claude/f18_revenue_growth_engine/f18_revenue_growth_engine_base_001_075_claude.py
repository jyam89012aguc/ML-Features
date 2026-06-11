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
    # simple growth over w days: level now vs level w days ago
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f18_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f18_cagr(s, w, periods_per_year=252.0):
    # annualized growth proxy from a w-day window
    r = s / s.shift(w).replace(0, np.nan)
    expo = periods_per_year / float(w)
    return np.power(r.clip(lower=1e-9), expo) - 1.0


def _f18_seq_growth(s, w):
    # sequential (period-over-period) growth using non-overlapping w-day steps
    g = s / s.shift(w).replace(0, np.nan) - 1.0
    return g


def _f18_growth_accel(s, w):
    # acceleration-as-level: growth now minus growth one window ago
    g = s / s.shift(w).replace(0, np.nan) - 1.0
    return g - g.shift(w)


def _f18_growth_stability(s, w):
    # stability = mean(daily log change) / std(daily log change) over w
    dl = np.log(s.replace(0, np.nan)).diff()
    m = dl.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = dl.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


# ============================================================
# 21d revenue growth (monthly book-build pace)
def f18rg_f18_revenue_growth_engine_revg_21d_base_v001_signal(revenue):
    b = _f18_growth(revenue, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth (quarterly)
def f18rg_f18_revenue_growth_engine_revg_63d_base_v002_signal(revenue):
    b = _f18_growth(revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue growth (half-year)
def f18rg_f18_revenue_growth_engine_revg_126d_base_v003_signal(revenue):
    b = _f18_growth(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth (year-over-year)
def f18rg_f18_revenue_growth_engine_revg_252d_base_v004_signal(revenue):
    b = _f18_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue growth (two-year)
def f18rg_f18_revenue_growth_engine_revg_504d_base_v005_signal(revenue):
    b = _f18_growth(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d USD-revenue growth (FX-clean view)
def f18rg_f18_revenue_growth_engine_revusdg_63d_base_v006_signal(revenueusd):
    b = _f18_growth(revenueusd, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d USD-revenue growth
def f18rg_f18_revenue_growth_engine_revusdg_252d_base_v007_signal(revenueusd):
    b = _f18_growth(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross-profit growth (scaling quality of growth)
def f18rg_f18_revenue_growth_engine_gpg_252d_base_v008_signal(gp):
    b = _f18_growth(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross-profit growth
def f18rg_f18_revenue_growth_engine_gpg_63d_base_v009_signal(gp):
    b = _f18_growth(gp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gross-profit growth
def f18rg_f18_revenue_growth_engine_gpg_126d_base_v010_signal(gp):
    b = _f18_growth(gp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue log-growth relative to its own trailing-year average (growth-trend gap)
def f18rg_f18_revenue_growth_engine_revlg_252d_base_v011_signal(revenue):
    lg = _f18_loggrowth(revenue, 252)
    b = lg - lg.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue log-growth de-trended vs its own half-year average (growth gap)
def f18rg_f18_revenue_growth_engine_revlg_126d_base_v012_signal(revenue):
    lg = _f18_loggrowth(revenue, 126)
    b = lg - lg.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d CAGR momentum: change in the annualized CAGR over a quarter (pace shift)
def f18rg_f18_revenue_growth_engine_cagr_252d_base_v013_signal(revenue):
    c = _f18_cagr(revenue, 252)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annualized CAGR proxy from 504d window, ranked within its own two-year history
def f18rg_f18_revenue_growth_engine_cagr_504d_base_v014_signal(revenue):
    c = _f18_cagr(revenue, 504)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annualized CAGR proxy from 126d window, ranked within its own two-year history
def f18rg_f18_revenue_growth_engine_cagr_126d_base_v015_signal(revenue):
    c = _f18_cagr(revenue, 126)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-revenue CAGR (252d) momentum: change in annualized FX-clean pace over a quarter
def f18rg_f18_revenue_growth_engine_cagrusd_252d_base_v016_signal(revenueusd):
    c = _f18_cagr(revenueusd, 252)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit annualized CAGR proxy (252d), z-scored vs its own two-year history
def f18rg_f18_revenue_growth_engine_cagrgp_252d_base_v017_signal(gp):
    c = _f18_cagr(gp, 252)
    b = _z(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential q/q revenue growth ranked within its own trailing-year distribution
def f18rg_f18_revenue_growth_engine_seqg_63d_base_v018_signal(revenue):
    g = _f18_seq_growth(revenue, 63)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential 21d revenue growth smoothed and de-meaned vs its quarterly average
def f18rg_f18_revenue_growth_engine_seqg_21d_base_v019_signal(revenue):
    g = _f18_seq_growth(revenue, 21)
    b = g.rolling(21, min_periods=10).mean() - g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential gross-profit growth (126d) de-meaned vs its own year average
def f18rg_f18_revenue_growth_engine_seqgpg_63d_base_v020_signal(gp):
    g = _f18_seq_growth(gp, 126)
    b = g - g.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth acceleration-as-level (63d)
def f18rg_f18_revenue_growth_engine_accel_63d_base_v021_signal(revenue):
    b = _f18_growth_accel(revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth acceleration-as-level (126d)
def f18rg_f18_revenue_growth_engine_accel_126d_base_v022_signal(revenue):
    b = _f18_growth_accel(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth acceleration-as-level (252d)
def f18rg_f18_revenue_growth_engine_accel_252d_base_v023_signal(revenue):
    b = _f18_growth_accel(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth acceleration-as-level (63d)
def f18rg_f18_revenue_growth_engine_accelgp_63d_base_v024_signal(gp):
    b = _f18_growth_accel(gp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability (252d): drift-to-noise of daily log changes, de-trended vs its own mean
def f18rg_f18_revenue_growth_engine_stab_252d_base_v025_signal(revenue):
    s = _f18_growth_stability(revenue, 252)
    b = s - s.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability (126d)
def f18rg_f18_revenue_growth_engine_stab_126d_base_v026_signal(revenue):
    b = _f18_growth_stability(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth stability (252d)
def f18rg_f18_revenue_growth_engine_stabgp_252d_base_v027_signal(gp):
    b = _f18_growth_stability(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth rank: 63d revenue growth percentile vs own 504d history
def f18rg_f18_revenue_growth_engine_grank_63d_base_v028_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth rank: 252d revenue growth percentile vs own 504d history
def f18rg_f18_revenue_growth_engine_grank_252d_base_v029_signal(revenue):
    g = _f18_growth(revenue, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth rank: gross-profit 252d growth percentile vs own 504d history
def f18rg_f18_revenue_growth_engine_grankgp_252d_base_v030_signal(gp):
    g = _f18_growth(gp, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth z-score: 63d revenue growth de-trended vs own 252d history
def f18rg_f18_revenue_growth_engine_gz_63d_base_v031_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth z-score: 126d revenue growth de-trended vs own 252d history
def f18rg_f18_revenue_growth_engine_gz_126d_base_v032_signal(revenue):
    g = _f18_growth(revenue, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth z-score (126d vs 252d history)
def f18rg_f18_revenue_growth_engine_gzgp_126d_base_v033_signal(gp):
    g = _f18_growth(gp, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality spread: gross-profit growth minus revenue growth (252d)
def f18rg_f18_revenue_growth_engine_gqspr_252d_base_v034_signal(gp, revenue):
    gg = _f18_growth(gp, 252)
    rg = _f18_growth(revenue, 252)
    b = gg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality spread (63d): gp growth minus revenue growth
def f18rg_f18_revenue_growth_engine_gqspr_63d_base_v035_signal(gp, revenue):
    gg = _f18_growth(gp, 63)
    rg = _f18_growth(revenue, 63)
    b = gg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth term-structure: short (63d) minus long (252d) revenue growth
def f18rg_f18_revenue_growth_engine_gterm_63v252_base_v036_signal(revenue):
    s = _f18_growth(revenue, 63)
    l = _f18_growth(revenue, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth term-structure ratio: 126d growth over 252d growth
def f18rg_f18_revenue_growth_engine_gtermr_126v252_base_v037_signal(revenue):
    s = _f18_growth(revenue, 126)
    l = _f18_growth(revenue, 252)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-vs-reported growth divergence (FX / mix signal), 252d
def f18rg_f18_revenue_growth_engine_fxdiv_252d_base_v038_signal(revenueusd, revenue):
    gu = _f18_growth(revenueusd, 252)
    gr = _f18_growth(revenue, 252)
    b = gu - gr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth dispersion: std of 63d revenue growth over the last year
def f18rg_f18_revenue_growth_engine_gdisp_252d_base_v039_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth dispersion: std of 21d revenue growth over a half-year
def f18rg_f18_revenue_growth_engine_gdisp_126d_base_v040_signal(revenue):
    g = _f18_growth(revenue, 21)
    b = _std(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed (EMA) 63d revenue growth (persistent trend pace)
def f18rg_f18_revenue_growth_engine_gema_63d_base_v041_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth displacement: 63d growth minus its own slow EMA
def f18rg_f18_revenue_growth_engine_gdisp_ema_base_v042_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = g - g.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR spread: short-window CAGR (126d) minus long-window CAGR (504d)
def f18rg_f18_revenue_growth_engine_cagrspr_base_v043_signal(revenue):
    s = _f18_cagr(revenue, 126)
    l = _f18_cagr(revenue, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit CAGR spread (126d vs 504d)
def f18rg_f18_revenue_growth_engine_cagrgpspr_base_v044_signal(gp):
    s = _f18_cagr(gp, 126)
    l = _f18_cagr(gp, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted growth: 252d revenue growth divided by its 252d dispersion
def f18rg_f18_revenue_growth_engine_radjg_252d_base_v045_signal(revenue):
    g = _f18_growth(revenue, 252)
    disp = _std(_f18_growth(revenue, 63), 252)
    b = g / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude compression of 252d revenue growth (tame outliers)
def f18rg_f18_revenue_growth_engine_gsignmag_252d_base_v046_signal(revenue):
    g = _f18_growth(revenue, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded growth-vs-trend: tanh of 63d growth minus its trailing-year median growth
def f18rg_f18_revenue_growth_engine_gtanh_63d_base_v047_signal(revenue):
    g = _f18_growth(revenue, 63)
    med = g.rolling(252, min_periods=126).median()
    b = np.tanh(8.0 * (g - med))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of USD-revenue growth (63d)
def f18rg_f18_revenue_growth_engine_accelusd_63d_base_v048_signal(revenueusd):
    b = _f18_growth_accel(revenueusd, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth consistency: fraction of last year with positive 21d growth
def f18rg_f18_revenue_growth_engine_gconsist_252d_base_v049_signal(revenue):
    g = _f18_growth(revenue, 21)
    pos = (g > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth consistency (63d positive fraction over a year)
def f18rg_f18_revenue_growth_engine_gpconsist_252d_base_v050_signal(gp):
    g = _f18_growth(gp, 63)
    pos = (g > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth breadth: 63d growth weighted by its consistency over the year
def f18rg_f18_revenue_growth_engine_gbreadth_base_v051_signal(revenue):
    g = _f18_growth(revenue, 63)
    consist = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    b = g * consist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-level position: where current log-revenue sits in its own 504d range (trend maturity)
def f18rg_f18_revenue_growth_engine_lglvl_252d_base_v052_signal(revenue):
    lg = np.log(revenue.replace(0, np.nan))
    hi = lg.rolling(504, min_periods=252).max()
    lo = lg.rolling(504, min_periods=252).min()
    b = (lg - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth rank (USD revenue, 126d growth vs 504d history)
def f18rg_f18_revenue_growth_engine_grankusd_126d_base_v053_signal(revenueusd):
    g = _f18_growth(revenueusd, 126)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration rank: rank of 63d acceleration vs 504d history
def f18rg_f18_revenue_growth_engine_accrank_63d_base_v054_signal(revenue):
    a = _f18_growth_accel(revenue, 63)
    b = _rank(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit-to-revenue compounding ratio over a half-year (mix-shift of growth)
def f18rg_f18_revenue_growth_engine_compgap_base_v055_signal(gp, revenue):
    cg = (gp / gp.shift(126).replace(0, np.nan))
    cr = (revenue / revenue.shift(126).replace(0, np.nan))
    b = cg / cr.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit vs revenue growth ratio (operating-leverage of growth, 126d)
def f18rg_f18_revenue_growth_engine_gpleverage_126d_base_v056_signal(gp, revenue):
    gg = _f18_growth(gp, 126)
    rg = _f18_growth(revenue, 126)
    b = gg / rg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth z-spread: revenue growth z minus gross-profit growth z (63d/252d)
def f18rg_f18_revenue_growth_engine_gzspr_base_v057_signal(revenue, gp):
    rz = _z(_f18_growth(revenue, 63), 252)
    gz = _z(_f18_growth(gp, 63), 252)
    b = rz - gz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth drawdown: 63d growth relative to its trailing-year peak growth
def f18rg_f18_revenue_growth_engine_gdd_252d_base_v058_signal(revenue):
    g = _f18_growth(revenue, 63)
    peak = g.rolling(252, min_periods=126).max()
    b = g - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth recovery: 63d growth relative to its trailing-year trough growth
def f18rg_f18_revenue_growth_engine_grec_252d_base_v059_signal(revenue):
    g = _f18_growth(revenue, 63)
    trough = g.rolling(252, min_periods=126).min()
    b = g - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth position in range: where current 63d growth sits in its 252d range
def f18rg_f18_revenue_growth_engine_gpos_252d_base_v060_signal(revenue):
    g = _f18_growth(revenue, 63)
    hi = g.rolling(252, min_periods=126).max()
    lo = g.rolling(252, min_periods=126).min()
    b = (g - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD growth stability (252d drift-to-noise)
def f18rg_f18_revenue_growth_engine_stabusd_252d_base_v061_signal(revenueusd):
    b = _f18_growth_stability(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-of-growth: change of 126d growth over a quarter, smoothed
def f18rg_f18_revenue_growth_engine_g2_126d_base_v062_signal(revenue):
    g = _f18_growth(revenue, 126)
    b = (g - g.shift(63)).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth momentum: 126d gp-growth change over a quarter
def f18rg_f18_revenue_growth_engine_gpmom_126d_base_v063_signal(gp):
    g = _f18_growth(gp, 126)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level vs its own 252d trailing mean (scale-detrended growth proxy)
def f18rg_f18_revenue_growth_engine_lvlmean_252d_base_v064_signal(revenue):
    b = revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit level vs its own 252d trailing mean
def f18rg_f18_revenue_growth_engine_gplvlmean_252d_base_v065_signal(gp):
    b = gp / _mean(gp, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-year dispersion of YoY growth: how variable the YoY growth rate has been
def f18rg_f18_revenue_growth_engine_gyoy2_base_v066_signal(revenue):
    g = _f18_growth(revenue, 252)
    b = _std(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs gross-profit growth co-movement (interaction product, 126d)
def f18rg_f18_revenue_growth_engine_ginteract_126d_base_v067_signal(revenue, gp):
    rg = _f18_growth(revenue, 126)
    gg = _f18_growth(gp, 126)
    b = np.sign(rg) * np.sqrt((rg.abs() * gg.abs()).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth streak: consecutive months of positive 21d revenue growth (capped)
def f18rg_f18_revenue_growth_engine_gstreak_base_v068_signal(revenue):
    g = _f18_growth(revenue, 21)
    pos = (g > 0).astype(float)
    grp = (pos != pos.shift(1)).cumsum()
    streak = pos.groupby(grp).cumsum()
    b = (streak * pos).clip(upper=126) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR risk-adjusted: 504d CAGR over half-year dispersion of 21d growth (Sharpe-like growth)
def f18rg_f18_revenue_growth_engine_cagradj_252d_base_v069_signal(revenue):
    c = _f18_cagr(revenue, 504)
    disp = _std(_f18_growth(revenue, 21), 126)
    b = c / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth rank de-meaned (504d) times sign (regime tilt)
def f18rg_f18_revenue_growth_engine_gpranktilt_base_v070_signal(gp):
    g = _f18_growth(gp, 126)
    r = _rank(g, 504)
    b = r * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window growth dispersion: std across 63/126/252d revenue growth
def f18rg_f18_revenue_growth_engine_gmultidisp_base_v071_signal(revenue):
    g1 = _f18_growth(revenue, 63)
    g2 = _f18_growth(revenue, 126)
    g3 = _f18_growth(revenue, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annualized-pace disagreement: rank of (126d-annualized growth minus 504d CAGR)
def f18rg_f18_revenue_growth_engine_gmultispr_base_v072_signal(revenue):
    near = (1.0 + _f18_growth(revenue, 126)).clip(lower=1e-9) ** 2 - 1.0
    longp = _f18_cagr(revenue, 504)
    b = _rank(near - longp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-CAGR risk-adjusted (504d window)
def f18rg_f18_revenue_growth_engine_cagrusdadj_504d_base_v073_signal(revenueusd):
    c = _f18_cagr(revenueusd, 504)
    disp = _std(_f18_growth(revenueusd, 63), 252)
    b = c / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth-acceleration sign-magnitude (126d, compressed)
def f18rg_f18_revenue_growth_engine_accelsm_126d_base_v074_signal(gp):
    a = _f18_growth_accel(gp, 126)
    b = np.sign(a) * (a.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite: stability x rank of 252d growth (quality of growth)
def f18rg_f18_revenue_growth_engine_durable_base_v075_signal(revenue):
    stab = _f18_growth_stability(revenue, 252)
    rnk = _rank(_f18_growth(revenue, 252), 504)
    b = np.tanh(stab) * rnk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18rg_f18_revenue_growth_engine_revg_21d_base_v001_signal,
    f18rg_f18_revenue_growth_engine_revg_63d_base_v002_signal,
    f18rg_f18_revenue_growth_engine_revg_126d_base_v003_signal,
    f18rg_f18_revenue_growth_engine_revg_252d_base_v004_signal,
    f18rg_f18_revenue_growth_engine_revg_504d_base_v005_signal,
    f18rg_f18_revenue_growth_engine_revusdg_63d_base_v006_signal,
    f18rg_f18_revenue_growth_engine_revusdg_252d_base_v007_signal,
    f18rg_f18_revenue_growth_engine_gpg_252d_base_v008_signal,
    f18rg_f18_revenue_growth_engine_gpg_63d_base_v009_signal,
    f18rg_f18_revenue_growth_engine_gpg_126d_base_v010_signal,
    f18rg_f18_revenue_growth_engine_revlg_252d_base_v011_signal,
    f18rg_f18_revenue_growth_engine_revlg_126d_base_v012_signal,
    f18rg_f18_revenue_growth_engine_cagr_252d_base_v013_signal,
    f18rg_f18_revenue_growth_engine_cagr_504d_base_v014_signal,
    f18rg_f18_revenue_growth_engine_cagr_126d_base_v015_signal,
    f18rg_f18_revenue_growth_engine_cagrusd_252d_base_v016_signal,
    f18rg_f18_revenue_growth_engine_cagrgp_252d_base_v017_signal,
    f18rg_f18_revenue_growth_engine_seqg_63d_base_v018_signal,
    f18rg_f18_revenue_growth_engine_seqg_21d_base_v019_signal,
    f18rg_f18_revenue_growth_engine_seqgpg_63d_base_v020_signal,
    f18rg_f18_revenue_growth_engine_accel_63d_base_v021_signal,
    f18rg_f18_revenue_growth_engine_accel_126d_base_v022_signal,
    f18rg_f18_revenue_growth_engine_accel_252d_base_v023_signal,
    f18rg_f18_revenue_growth_engine_accelgp_63d_base_v024_signal,
    f18rg_f18_revenue_growth_engine_stab_252d_base_v025_signal,
    f18rg_f18_revenue_growth_engine_stab_126d_base_v026_signal,
    f18rg_f18_revenue_growth_engine_stabgp_252d_base_v027_signal,
    f18rg_f18_revenue_growth_engine_grank_63d_base_v028_signal,
    f18rg_f18_revenue_growth_engine_grank_252d_base_v029_signal,
    f18rg_f18_revenue_growth_engine_grankgp_252d_base_v030_signal,
    f18rg_f18_revenue_growth_engine_gz_63d_base_v031_signal,
    f18rg_f18_revenue_growth_engine_gz_126d_base_v032_signal,
    f18rg_f18_revenue_growth_engine_gzgp_126d_base_v033_signal,
    f18rg_f18_revenue_growth_engine_gqspr_252d_base_v034_signal,
    f18rg_f18_revenue_growth_engine_gqspr_63d_base_v035_signal,
    f18rg_f18_revenue_growth_engine_gterm_63v252_base_v036_signal,
    f18rg_f18_revenue_growth_engine_gtermr_126v252_base_v037_signal,
    f18rg_f18_revenue_growth_engine_fxdiv_252d_base_v038_signal,
    f18rg_f18_revenue_growth_engine_gdisp_252d_base_v039_signal,
    f18rg_f18_revenue_growth_engine_gdisp_126d_base_v040_signal,
    f18rg_f18_revenue_growth_engine_gema_63d_base_v041_signal,
    f18rg_f18_revenue_growth_engine_gdisp_ema_base_v042_signal,
    f18rg_f18_revenue_growth_engine_cagrspr_base_v043_signal,
    f18rg_f18_revenue_growth_engine_cagrgpspr_base_v044_signal,
    f18rg_f18_revenue_growth_engine_radjg_252d_base_v045_signal,
    f18rg_f18_revenue_growth_engine_gsignmag_252d_base_v046_signal,
    f18rg_f18_revenue_growth_engine_gtanh_63d_base_v047_signal,
    f18rg_f18_revenue_growth_engine_accelusd_63d_base_v048_signal,
    f18rg_f18_revenue_growth_engine_gconsist_252d_base_v049_signal,
    f18rg_f18_revenue_growth_engine_gpconsist_252d_base_v050_signal,
    f18rg_f18_revenue_growth_engine_gbreadth_base_v051_signal,
    f18rg_f18_revenue_growth_engine_lglvl_252d_base_v052_signal,
    f18rg_f18_revenue_growth_engine_grankusd_126d_base_v053_signal,
    f18rg_f18_revenue_growth_engine_accrank_63d_base_v054_signal,
    f18rg_f18_revenue_growth_engine_compgap_base_v055_signal,
    f18rg_f18_revenue_growth_engine_gpleverage_126d_base_v056_signal,
    f18rg_f18_revenue_growth_engine_gzspr_base_v057_signal,
    f18rg_f18_revenue_growth_engine_gdd_252d_base_v058_signal,
    f18rg_f18_revenue_growth_engine_grec_252d_base_v059_signal,
    f18rg_f18_revenue_growth_engine_gpos_252d_base_v060_signal,
    f18rg_f18_revenue_growth_engine_stabusd_252d_base_v061_signal,
    f18rg_f18_revenue_growth_engine_g2_126d_base_v062_signal,
    f18rg_f18_revenue_growth_engine_gpmom_126d_base_v063_signal,
    f18rg_f18_revenue_growth_engine_lvlmean_252d_base_v064_signal,
    f18rg_f18_revenue_growth_engine_gplvlmean_252d_base_v065_signal,
    f18rg_f18_revenue_growth_engine_gyoy2_base_v066_signal,
    f18rg_f18_revenue_growth_engine_ginteract_126d_base_v067_signal,
    f18rg_f18_revenue_growth_engine_gstreak_base_v068_signal,
    f18rg_f18_revenue_growth_engine_cagradj_252d_base_v069_signal,
    f18rg_f18_revenue_growth_engine_gpranktilt_base_v070_signal,
    f18rg_f18_revenue_growth_engine_gmultidisp_base_v071_signal,
    f18rg_f18_revenue_growth_engine_gmultispr_base_v072_signal,
    f18rg_f18_revenue_growth_engine_cagrusdadj_504d_base_v073_signal,
    f18rg_f18_revenue_growth_engine_accelsm_126d_base_v074_signal,
    f18rg_f18_revenue_growth_engine_durable_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_REVENUE_GROWTH_ENGINE_REGISTRY_001_075 = REGISTRY


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

    print("OK f18_revenue_growth_engine_base_001_075_claude: %d features pass" % n_features)
