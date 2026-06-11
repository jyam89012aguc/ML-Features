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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (revenue growth engine) =====
def _f23_growth(rev, w):
    return rev / rev.shift(w).replace(0, np.nan) - 1.0


def _f23_log_growth(rev, w):
    return np.log(rev.replace(0, np.nan) / rev.shift(w).replace(0, np.nan))


def _f23_cagr(rev, w, periods_per_year=252.0):
    r = rev / rev.shift(w).replace(0, np.nan)
    return r.clip(lower=1e-9) ** (periods_per_year / float(w)) - 1.0


def _f23_growth_std(rev, w, gw):
    g = _f23_growth(rev, gw)
    return g.rolling(w, min_periods=max(1, w // 2)).std()


def _f23_seq_growth(rev, w):
    g = _f23_growth(rev, w)
    return g - g.shift(w)


def _f23_slope(s, w):
    def _f(a):
        x = np.arange(len(a), dtype=float)
        d = x - x.mean()
        den = (d * d).sum()
        if den == 0:
            return np.nan
        return (d * (a - a.mean())).sum() / den
    return s.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


# ============================================================
# trailing-126d log-growth (half-year compounding), USD series
def f23rg_f23_revenue_growth_engine_lgrw_126d_base_v076_signal(revenueusd):
    b = _f23_log_growth(revenueusd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing-504d log-growth (two-year compounding)
def f23rg_f23_revenue_growth_engine_lgrw_504d_base_v077_signal(revenue):
    b = _f23_log_growth(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d growth z-scored vs its own 252d distribution (monthly surprise, long window)
def f23rg_f23_revenue_growth_engine_gz_21d_base_v078_signal(revenue):
    g = _f23_growth(revenue, 21)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d growth z-scored vs its own 504d distribution (de-trended medium growth)
def f23rg_f23_revenue_growth_engine_gz_126d_base_v079_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth rank of the 21d growth vs its own 252d history (percentile placement)
def f23rg_f23_revenue_growth_engine_grank_21d_base_v080_signal(revenue):
    g = _f23_growth(revenue, 21)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth rank of the 504d growth vs its own 504d history
def f23rg_f23_revenue_growth_engine_grank_504d_base_v081_signal(revenueusd):
    g = _f23_growth(revenueusd, 504)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 63d-growth series over 126d (is the growth rate itself trending up?)
def f23rg_f23_revenue_growth_engine_gtrendslope_base_v082_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = _f23_slope(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 21d-growth series over 252d (long-run drift of the growth rate)
def f23rg_f23_revenue_growth_engine_gtrendslope_long_base_v083_signal(revenue):
    g = _f23_growth(revenue, 21)
    b = _f23_slope(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability: std of 126d growth over a 504d window (medium-horizon steadiness)
def f23rg_f23_revenue_growth_engine_gstd126_504d_base_v084_signal(revenue):
    b = _f23_growth_std(revenue, 504, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability short window: std of 21d growth over 126d
def f23rg_f23_revenue_growth_engine_gstd21_126d_base_v085_signal(revenueusd):
    b = _f23_growth_std(revenueusd, 126, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inverse-volatility-weighted growth: 252d growth divided by 252d growth-vol (Sharpe)
def f23rg_f23_revenue_growth_engine_gsharpe_252d_base_v086_signal(revenueusd):
    g = _f23_growth(revenueusd, 252)
    sd = _f23_growth_std(revenueusd, 252, 21)
    b = g / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-vol normalized 63d growth (risk-adjusted quarterly growth)
def f23rg_f23_revenue_growth_engine_gsharpe_63d_base_v087_signal(revenue):
    g = _f23_growth(revenue, 63)
    sd = _f23_growth_std(revenue, 126, 21)
    b = g / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential growth at 21d (month-over-month acceleration as level)
def f23rg_f23_revenue_growth_engine_seq_21d_base_v088_signal(revenue):
    b = _f23_seq_growth(revenue, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential growth at 252d (year-over-year acceleration)
def f23rg_f23_revenue_growth_engine_seq_252d_base_v089_signal(revenueusd):
    b = _f23_seq_growth(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration ratio: 63d growth over its value a quarter ago (multiplicative)
def f23rg_f23_revenue_growth_engine_gaccratio_63d_base_v090_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = (1.0 + g) / (1.0 + g.shift(63)).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration ratio at 126d horizon
def f23rg_f23_revenue_growth_engine_gaccratio_126d_base_v091_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    b = (1.0 + g) / (1.0 + g.shift(126)).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth consistency at 63d horizon: fraction of last year with positive 63d growth
def f23rg_f23_revenue_growth_engine_gcons63_base_v092_signal(revenue):
    g = _f23_growth(revenue, 63)
    pos = (g > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth consistency: fraction of last year 21d growth beats its trailing 252d mean
def f23rg_f23_revenue_growth_engine_gconsmean_base_v093_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    mu = g.rolling(252, min_periods=126).mean()
    above = (g > mu).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-growth streak (consecutive months of positive 63d growth), scaled
def f23rg_f23_revenue_growth_engine_posstreak_base_v094_signal(revenue):
    g = _f23_growth(revenue, 63)
    up = (g > 0).astype(float)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    b = streak.clip(upper=252) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration streak intensity: signed run-length x magnitude of sequential growth
def f23rg_f23_revenue_growth_engine_accstreak_base_v095_signal(revenue):
    seq = _f23_seq_growth(revenue, 21)
    up = (seq > 0).astype(float)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    mag = seq.abs().rolling(63, min_periods=21).mean()
    b = (streak.clip(upper=189) / 189.0) * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth percentile gap: rank of 63d growth minus rank of 252d growth (rotation)
def f23rg_f23_revenue_growth_engine_grankgap_base_v096_signal(revenue):
    r_short = _rank(_f23_growth(revenue, 63), 504)
    r_long = _rank(_f23_growth(revenue, 252), 504)
    b = r_short - r_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window growth dispersion across 63/126/252/504 (long-horizon disagreement)
def f23rg_f23_revenue_growth_engine_gdisp_long_base_v097_signal(revenueusd):
    g1 = _f23_growth(revenueusd, 63)
    g2 = _f23_growth(revenueusd, 126)
    g3 = _f23_growth(revenueusd, 252)
    g4 = _f23_growth(revenueusd, 504)
    b = pd.concat([g1, g2, g3, g4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth coefficient-of-variation at the 126d/504d configuration (stability ratio)
def f23rg_f23_revenue_growth_engine_gcv_504d_base_v098_signal(revenue):
    g = _f23_growth(revenue, 126)
    mu = g.rolling(504, min_periods=252).mean()
    sd = g.rolling(504, min_periods=252).std()
    b = sd / mu.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth EWMA crossover: fast EWMA of 21d growth minus slow EWMA (momentum of growth)
def f23rg_f23_revenue_growth_engine_gcross_base_v099_signal(revenue):
    g = _f23_growth(revenue, 21)
    fast = g.ewm(span=42, min_periods=21).mean()
    slow = g.ewm(span=189, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth displacement at 126d: 126d growth minus its slow EWMA (medium surprise)
def f23rg_f23_revenue_growth_engine_gdisp_126d_base_v100_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    b = g - g.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of the 63d growth (compressed quarterly growth level)
def f23rg_f23_revenue_growth_engine_gsignmag_63d_base_v101_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of the sequential 126d growth (compressed accel level)
def f23rg_f23_revenue_growth_engine_seqsignmag_126d_base_v102_signal(revenueusd):
    seq = _f23_seq_growth(revenueusd, 126)
    b = np.sign(seq) * (seq.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded 252d growth level (saturating growth signal)
def f23rg_f23_revenue_growth_engine_gtanh_252d_base_v103_signal(revenue):
    g = _f23_growth(revenue, 252)
    b = np.tanh(2.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level vs its trailing-126d EWMA (short-trend stretch)
def f23rg_f23_revenue_growth_engine_levstretch_126d_base_v104_signal(revenue):
    ema = revenue.ewm(span=126, min_periods=63).mean()
    b = revenue / ema.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level z-score vs its own 252d window (where revenue sits in its range)
def f23rg_f23_revenue_growth_engine_levz_252d_base_v105_signal(revenueusd):
    b = _z(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs its trailing-252d high (expansion proximity), ranked over 504d
def f23rg_f23_revenue_growth_engine_revhirank_base_v106_signal(revenue):
    hi = _rmax(revenue, 252)
    prox = revenue / hi.replace(0, np.nan)
    b = _rank(prox, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue contraction depth: drawdown of revenue from its trailing-504d peak
def f23rg_f23_revenue_growth_engine_revdd_504d_base_v107_signal(revenueusd):
    hi = _rmax(revenueusd, 504)
    b = revenueusd / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue recovery off 252d trough scaled by time since that trough (rebound rate)
def f23rg_f23_revenue_growth_engine_revrebound_base_v108_signal(revenue):
    w = 252
    lo = _rmin(revenue, w)
    rec = revenue / lo.replace(0, np.nan) - 1.0

    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))

    dsl = revenue.rolling(w, min_periods=126).apply(_dsl, raw=True).replace(0, np.nan)
    b = rec / dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth curvature: second difference of the 63d-growth series (jerk-as-level)
def f23rg_f23_revenue_growth_engine_gcurv2_base_v109_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = g - 2.0 * g.shift(63) + g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth jerk ratio: change in sequential growth normalized by growth dispersion
def f23rg_f23_revenue_growth_engine_gjerknorm_base_v110_signal(revenueusd):
    seq = _f23_seq_growth(revenueusd, 63)
    jerk = seq - seq.shift(63)
    sd = _f23_growth_std(revenueusd, 252, 63)
    b = jerk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth half-life proxy: ratio of recent-half growth to full-year growth
def f23rg_f23_revenue_growth_engine_gfrontload_base_v111_signal(revenue):
    g_half = _f23_log_growth(revenue, 126)
    g_full = _f23_log_growth(revenue, 252)
    b = g_half / g_full.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth back-load: ratio of older-half growth to full-year growth (deceleration sign)
def f23rg_f23_revenue_growth_engine_gbackload_base_v112_signal(revenueusd):
    g_old = _f23_log_growth(revenueusd, 252) - _f23_log_growth(revenueusd, 126)
    g_full = _f23_log_growth(revenueusd, 252)
    b = g_old / g_full.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year growth of the growth rate (second-order YoY change)
def f23rg_f23_revenue_growth_engine_gyoy2_base_v113_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = g.shift(0) - 2.0 * g.shift(126) + g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth breadth across both series: avg of USD-growth-rank and domestic-growth-rank
def f23rg_f23_revenue_growth_engine_dualgrank_base_v114_signal(revenue, revenueusd):
    r1 = _rank(_f23_growth(revenue, 252), 504)
    r2 = _rank(_f23_growth(revenueusd, 252), 504)
    b = 0.5 * (r1 + r2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# currency-mix drift: ratio of USD revenue level to domestic revenue level, de-trended
def f23rg_f23_revenue_growth_engine_fxmixdrift_base_v115_signal(revenue, revenueusd):
    ratio = revenueusd / revenue.replace(0, np.nan)
    b = ratio / ratio.rolling(252, min_periods=126).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-vs-domestic growth divergence streak (consecutive months USD outgrows domestic)
def f23rg_f23_revenue_growth_engine_fxdivstreak_base_v116_signal(revenue, revenueusd):
    diff = _f23_growth(revenueusd, 63) - _f23_growth(revenue, 63)
    up = (diff > 0).astype(float)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    b = streak.clip(upper=126) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth efficiency over 126d: net log-growth over absolute monthly path length
def f23rg_f23_revenue_growth_engine_geff_126d_base_v117_signal(revenueusd):
    lr = np.log(revenueusd.replace(0, np.nan))
    net = (lr - lr.shift(126)).abs()
    path = lr.diff(21).abs().rolling(126, min_periods=63).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth path smoothness: net 252d move signed, divided by total path (directional ER)
def f23rg_f23_revenue_growth_engine_dirER_252d_base_v118_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    net = lr - lr.shift(252)
    path = lr.diff(21).abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth drawdown depth: current 63d growth vs its trailing-504d peak growth
def f23rg_f23_revenue_growth_engine_gdd_63d_base_v119_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    peak = g.rolling(504, min_periods=252).max()
    b = g - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth recovery: current 126d growth vs its trailing-504d trough growth
def f23rg_f23_revenue_growth_engine_grecov_126d_base_v120_signal(revenue):
    g = _f23_growth(revenue, 126)
    trough = g.rolling(504, min_periods=252).min()
    b = g - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR over 756d (three-year annualized compound growth)
def f23rg_f23_revenue_growth_engine_cagr_756d_base_v121_signal(revenueusd):
    b = _f23_cagr(revenueusd, 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR robust median: annualized median quarterly log-growth over 504d
def f23rg_f23_revenue_growth_engine_cagrmed_504d_base_v122_signal(revenue):
    qlg = np.log(revenue.replace(0, np.nan)).diff(63)
    med = qlg.rolling(504, min_periods=252).median()
    b = np.exp(med * (252.0 / 63.0)) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration regime: sign of growth slope x magnitude of growth (regime tag)
def f23rg_f23_revenue_growth_engine_gregime_base_v123_signal(revenue):
    g = _f23_growth(revenue, 63)
    slope = _f23_slope(g, 126)
    b = np.sign(slope) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside growth capture: avg of positive 21d growths over 252d (expansion intensity)
def f23rg_f23_revenue_growth_engine_gupcap_base_v124_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    up = g.clip(lower=0)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside growth capture: avg of negative 21d growths over 252d (contraction intensity)
def f23rg_f23_revenue_growth_engine_gdncap_base_v125_signal(revenue):
    g = _f23_growth(revenue, 21)
    dn = g.clip(upper=0)
    b = dn.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth Omega: ratio of summed positive 21d growths to summed negative ones (log)
def f23rg_f23_revenue_growth_engine_gasym_base_v126_signal(revenue):
    g = _f23_growth(revenue, 21)
    up = g.clip(lower=0).rolling(252, min_periods=126).sum()
    dn = (-g.clip(upper=0)).rolling(252, min_periods=126).sum()
    b = np.log((up + 1e-9) / (dn + 1e-9))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 63d growth relative to its 252d-window median (excess-pace level)
def f23rg_f23_revenue_growth_engine_gexcess_base_v127_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    med = g.rolling(252, min_periods=126).median()
    b = g - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth quartile width: 75th minus 25th percentile of 21d growth over 252d (IQR)
def f23rg_f23_revenue_growth_engine_giqr_base_v128_signal(revenue):
    g = _f23_growth(revenue, 21)
    q75 = g.rolling(252, min_periods=126).quantile(0.75)
    q25 = g.rolling(252, min_periods=126).quantile(0.25)
    b = q75 - q25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth tail: 95th percentile of 21d growth over 252d (best-month pace)
def f23rg_f23_revenue_growth_engine_gtail95_base_v129_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    b = g.rolling(252, min_periods=126).quantile(0.95)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth left-tail: 5th percentile of 21d growth over 252d (worst-month pace)
def f23rg_f23_revenue_growth_engine_gtail05_base_v130_signal(revenue):
    g = _f23_growth(revenue, 21)
    b = g.rolling(252, min_periods=126).quantile(0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth median over 252d (robust central growth pace), 63d growth distribution
def f23rg_f23_revenue_growth_engine_gmed_252d_base_v131_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    b = g.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth trend vs level interaction: growth slope times current growth level
def f23rg_f23_revenue_growth_engine_gtrendlev_base_v132_signal(revenue):
    g = _f23_growth(revenue, 63)
    slope = _f23_slope(g, 126)
    b = slope * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration via log-revenue regression slope change (curvature of slope)
def f23rg_f23_revenue_growth_engine_slopechg_base_v133_signal(revenueusd):
    lr = np.log(revenueusd.replace(0, np.nan))
    slope = _f23_slope(lr, 126)
    b = slope - slope.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth persistence: rolling autocorrelation of 63d growth at lag 63 over 504d
def f23rg_f23_revenue_growth_engine_gautocorr63_base_v134_signal(revenue):
    g = _f23_growth(revenue, 63)
    gl = g.shift(63)
    b = g.rolling(504, min_periods=252).corr(gl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth Hurst-like: ratio of 252d net move range to summed 21d move dispersion
def f23rg_f23_revenue_growth_engine_grs_base_v135_signal(revenueusd):
    lr = np.log(revenueusd.replace(0, np.nan))
    step = lr.diff(21)
    rng = (lr.rolling(252, min_periods=126).max()
           - lr.rolling(252, min_periods=126).min())
    sd = step.rolling(252, min_periods=126).std()
    b = rng / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion intensity: time-weighted proximity to the trailing-126d revenue high
def f23rg_f23_revenue_growth_engine_newhi126_base_v136_signal(revenue):
    hi = revenue.rolling(126, min_periods=63).max()
    prox = revenue / hi.replace(0, np.nan)
    # how persistently revenue hugs its 126d high, averaged over the last year
    b = prox.rolling(252, min_periods=126).mean() * (1.0 + prox)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# contraction frequency: fraction of last year with negative 63d growth
def f23rg_f23_revenue_growth_engine_contracfreq_base_v137_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    neg = (g < 0).astype(float)
    b = neg.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration breadth: net fraction of horizons accelerating (seq>0)
def f23rg_f23_revenue_growth_engine_accbreadth_base_v138_signal(revenue):
    s1 = _f23_seq_growth(revenue, 21)
    s2 = _f23_seq_growth(revenue, 63)
    s3 = _f23_seq_growth(revenue, 126)
    a1 = np.tanh(s1 * 10.0)
    a2 = np.tanh(s2 * 6.0)
    a3 = np.tanh(s3 * 4.0)
    b = (a1 + a2 + a3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth quality composite: growth rank minus dispersion rank minus contraction rank
def f23rg_f23_revenue_growth_engine_gquality_base_v139_signal(revenue):
    g_rank = _rank(_f23_growth(revenue, 252), 504)
    disp_rank = _rank(_f23_growth_std(revenue, 252, 21), 504)
    g63 = _f23_growth(revenue, 63)
    contr_rank = _rank((g63 < 0).astype(float).rolling(252, min_periods=126).mean(), 504)
    b = g_rank - 0.5 * disp_rank - 0.5 * contr_rank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-acceleration ratio: 63d log-revenue slope relative to its 252d slope (fade)
def f23rg_f23_revenue_growth_engine_levslopegap_base_v140_signal(revenueusd):
    lr = np.log(revenueusd.replace(0, np.nan))
    s_short = _f23_slope(lr, 63)
    s_long = _f23_slope(lr, 252)
    b = s_short / s_long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarterly-growth dispersion: cross-quarter spread of the last 4 QoQ growth ratios
def f23rg_f23_revenue_growth_engine_qoqratio_base_v141_signal(revenue):
    q = revenue / revenue.shift(63).replace(0, np.nan)
    stacked = pd.concat([q, q.shift(63), q.shift(126), q.shift(189)], axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion change: 252d growth-std now minus a year ago (regime shift)
def f23rg_f23_revenue_growth_engine_dispshift_base_v142_signal(revenueusd):
    sd = _f23_growth_std(revenueusd, 252, 21)
    b = sd - sd.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed growth surprise: EWMA of (21d growth minus its 252d mean)
def f23rg_f23_revenue_growth_engine_gsurpsm_base_v143_signal(revenue):
    g = _f23_growth(revenue, 21)
    surprise = g - g.rolling(252, min_periods=126).mean()
    b = surprise.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth convexity: is the growth rate itself decelerating? curvature of 126d growth
def f23rg_f23_revenue_growth_engine_gconvex_base_v144_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    b = -(g - 2.0 * g.shift(63) + g.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level rank tilt over 126d: rank now minus rank 126d ago (medium tilt)
def f23rg_f23_revenue_growth_engine_levtilt126_base_v145_signal(revenue):
    r = _rank(revenue, 504)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability z: 252d growth-std z-scored vs its own 504d history (vol regime)
def f23rg_f23_revenue_growth_engine_gstabz_base_v146_signal(revenueusd):
    sd = _f23_growth_std(revenueusd, 252, 21)
    b = _z(sd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compound-vs-simple gap at 504d (two-year volatility drag on the growth path)
def f23rg_f23_revenue_growth_engine_gdrag504_base_v147_signal(revenue):
    simple = _f23_growth(revenue, 504)
    compound = np.exp(np.log(revenue.replace(0, np.nan)).diff(21).rolling(
        504, min_periods=252).sum()) - 1.0
    b = simple - compound
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth impulse: latest 21d growth minus the EWMA growth, scaled by growth-vol
def f23rg_f23_revenue_growth_engine_gimpulse_base_v148_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g.ewm(span=126, min_periods=63).mean()
    sd = g.rolling(252, min_periods=126).std()
    b = (g - base) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-grower score: high 252d growth AND low growth dispersion (product of ranks)
def f23rg_f23_revenue_growth_engine_durscore_base_v149_signal(revenue):
    g_rank = _rank(_f23_growth(revenue, 252), 504) + 0.5
    stab_rank = 0.5 - _rank(_f23_growth_std(revenue, 252, 21), 504)
    b = g_rank * stab_rank - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-vs-prior-trough: 504d growth relative to the lowest 504d growth in 504d
def f23rg_f23_revenue_growth_engine_g504recov_base_v150_signal(revenueusd):
    g = _f23_growth(revenueusd, 504)
    trough = g.rolling(504, min_periods=252).min()
    peak = g.rolling(504, min_periods=252).max()
    b = (g - trough) / (peak - trough).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23rg_f23_revenue_growth_engine_lgrw_126d_base_v076_signal,
    f23rg_f23_revenue_growth_engine_lgrw_504d_base_v077_signal,
    f23rg_f23_revenue_growth_engine_gz_21d_base_v078_signal,
    f23rg_f23_revenue_growth_engine_gz_126d_base_v079_signal,
    f23rg_f23_revenue_growth_engine_grank_21d_base_v080_signal,
    f23rg_f23_revenue_growth_engine_grank_504d_base_v081_signal,
    f23rg_f23_revenue_growth_engine_gtrendslope_base_v082_signal,
    f23rg_f23_revenue_growth_engine_gtrendslope_long_base_v083_signal,
    f23rg_f23_revenue_growth_engine_gstd126_504d_base_v084_signal,
    f23rg_f23_revenue_growth_engine_gstd21_126d_base_v085_signal,
    f23rg_f23_revenue_growth_engine_gsharpe_252d_base_v086_signal,
    f23rg_f23_revenue_growth_engine_gsharpe_63d_base_v087_signal,
    f23rg_f23_revenue_growth_engine_seq_21d_base_v088_signal,
    f23rg_f23_revenue_growth_engine_seq_252d_base_v089_signal,
    f23rg_f23_revenue_growth_engine_gaccratio_63d_base_v090_signal,
    f23rg_f23_revenue_growth_engine_gaccratio_126d_base_v091_signal,
    f23rg_f23_revenue_growth_engine_gcons63_base_v092_signal,
    f23rg_f23_revenue_growth_engine_gconsmean_base_v093_signal,
    f23rg_f23_revenue_growth_engine_posstreak_base_v094_signal,
    f23rg_f23_revenue_growth_engine_accstreak_base_v095_signal,
    f23rg_f23_revenue_growth_engine_grankgap_base_v096_signal,
    f23rg_f23_revenue_growth_engine_gdisp_long_base_v097_signal,
    f23rg_f23_revenue_growth_engine_gcv_504d_base_v098_signal,
    f23rg_f23_revenue_growth_engine_gcross_base_v099_signal,
    f23rg_f23_revenue_growth_engine_gdisp_126d_base_v100_signal,
    f23rg_f23_revenue_growth_engine_gsignmag_63d_base_v101_signal,
    f23rg_f23_revenue_growth_engine_seqsignmag_126d_base_v102_signal,
    f23rg_f23_revenue_growth_engine_gtanh_252d_base_v103_signal,
    f23rg_f23_revenue_growth_engine_levstretch_126d_base_v104_signal,
    f23rg_f23_revenue_growth_engine_levz_252d_base_v105_signal,
    f23rg_f23_revenue_growth_engine_revhirank_base_v106_signal,
    f23rg_f23_revenue_growth_engine_revdd_504d_base_v107_signal,
    f23rg_f23_revenue_growth_engine_revrebound_base_v108_signal,
    f23rg_f23_revenue_growth_engine_gcurv2_base_v109_signal,
    f23rg_f23_revenue_growth_engine_gjerknorm_base_v110_signal,
    f23rg_f23_revenue_growth_engine_gfrontload_base_v111_signal,
    f23rg_f23_revenue_growth_engine_gbackload_base_v112_signal,
    f23rg_f23_revenue_growth_engine_gyoy2_base_v113_signal,
    f23rg_f23_revenue_growth_engine_dualgrank_base_v114_signal,
    f23rg_f23_revenue_growth_engine_fxmixdrift_base_v115_signal,
    f23rg_f23_revenue_growth_engine_fxdivstreak_base_v116_signal,
    f23rg_f23_revenue_growth_engine_geff_126d_base_v117_signal,
    f23rg_f23_revenue_growth_engine_dirER_252d_base_v118_signal,
    f23rg_f23_revenue_growth_engine_gdd_63d_base_v119_signal,
    f23rg_f23_revenue_growth_engine_grecov_126d_base_v120_signal,
    f23rg_f23_revenue_growth_engine_cagr_756d_base_v121_signal,
    f23rg_f23_revenue_growth_engine_cagrmed_504d_base_v122_signal,
    f23rg_f23_revenue_growth_engine_gregime_base_v123_signal,
    f23rg_f23_revenue_growth_engine_gupcap_base_v124_signal,
    f23rg_f23_revenue_growth_engine_gdncap_base_v125_signal,
    f23rg_f23_revenue_growth_engine_gasym_base_v126_signal,
    f23rg_f23_revenue_growth_engine_gexcess_base_v127_signal,
    f23rg_f23_revenue_growth_engine_giqr_base_v128_signal,
    f23rg_f23_revenue_growth_engine_gtail95_base_v129_signal,
    f23rg_f23_revenue_growth_engine_gtail05_base_v130_signal,
    f23rg_f23_revenue_growth_engine_gmed_252d_base_v131_signal,
    f23rg_f23_revenue_growth_engine_gtrendlev_base_v132_signal,
    f23rg_f23_revenue_growth_engine_slopechg_base_v133_signal,
    f23rg_f23_revenue_growth_engine_gautocorr63_base_v134_signal,
    f23rg_f23_revenue_growth_engine_grs_base_v135_signal,
    f23rg_f23_revenue_growth_engine_newhi126_base_v136_signal,
    f23rg_f23_revenue_growth_engine_contracfreq_base_v137_signal,
    f23rg_f23_revenue_growth_engine_accbreadth_base_v138_signal,
    f23rg_f23_revenue_growth_engine_gquality_base_v139_signal,
    f23rg_f23_revenue_growth_engine_levslopegap_base_v140_signal,
    f23rg_f23_revenue_growth_engine_qoqratio_base_v141_signal,
    f23rg_f23_revenue_growth_engine_dispshift_base_v142_signal,
    f23rg_f23_revenue_growth_engine_gsurpsm_base_v143_signal,
    f23rg_f23_revenue_growth_engine_gconvex_base_v144_signal,
    f23rg_f23_revenue_growth_engine_levtilt126_base_v145_signal,
    f23rg_f23_revenue_growth_engine_gstabz_base_v146_signal,
    f23rg_f23_revenue_growth_engine_gdrag504_base_v147_signal,
    f23rg_f23_revenue_growth_engine_gimpulse_base_v148_signal,
    f23rg_f23_revenue_growth_engine_durscore_base_v149_signal,
    f23rg_f23_revenue_growth_engine_g504recov_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_REVENUE_GROWTH_ENGINE_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(101, base=8e7, drift=0.025, vol=0.06, n=n).rename("revenue")
    revenueusd = _fund(102, base=1.0e8, drift=0.022, vol=0.07, n=n).rename("revenueusd")

    cols = {"revenue": revenue, "revenueusd": revenueusd}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f23_revenue_growth_engine_base_076_150_claude: %d features pass" % n_features)
