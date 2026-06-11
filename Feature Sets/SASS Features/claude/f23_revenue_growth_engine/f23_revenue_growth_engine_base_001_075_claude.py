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
    # pct_change of the revenue series over window w (revenue growth)
    return rev / rev.shift(w).replace(0, np.nan) - 1.0


def _f23_log_growth(rev, w):
    return np.log(rev.replace(0, np.nan) / rev.shift(w).replace(0, np.nan))


def _f23_cagr(rev, w, periods_per_year=252.0):
    # CAGR proxy: annualized compound growth over window w
    r = rev / rev.shift(w).replace(0, np.nan)
    return r.clip(lower=1e-9) ** (periods_per_year / float(w)) - 1.0


def _f23_growth_std(rev, w, gw):
    # dispersion (stability) of the gw-day growth over a window w
    g = _f23_growth(rev, gw)
    return g.rolling(w, min_periods=max(1, w // 2)).std()


def _f23_seq_growth(rev, w):
    # sequential growth: this window's growth vs the immediately prior window
    g = _f23_growth(rev, w)
    return g - g.shift(w)


# ============================================================
# revenue growth over 21d (monthly) — raw level
def f23rg_f23_revenue_growth_engine_grw_21d_base_v001_signal(revenue):
    b = _f23_growth(revenue, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth over 63d (quarterly)
def f23rg_f23_revenue_growth_engine_grw_63d_base_v002_signal(revenue):
    b = _f23_growth(revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth over 126d (half year)
def f23rg_f23_revenue_growth_engine_grw_126d_base_v003_signal(revenue):
    b = _f23_growth(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth over 252d (year-over-year)
def f23rg_f23_revenue_growth_engine_grw_252d_base_v004_signal(revenue):
    b = _f23_growth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth over 504d (two-year)
def f23rg_f23_revenue_growth_engine_grw_504d_base_v005_signal(revenue):
    b = _f23_growth(revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log revenue growth over 252d (USD-denominated series)
def f23rg_f23_revenue_growth_engine_lgrw_252d_base_v006_signal(revenueusd):
    b = _f23_log_growth(revenueusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR term-structure: annualized 504d rate minus annualized 252d rate (durability)
def f23rg_f23_revenue_growth_engine_cagr_252d_base_v007_signal(revenue):
    c_long = _f23_cagr(revenue, 504)
    c_short = _f23_cagr(revenue, 252)
    b = c_long - c_short
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# robust CAGR: annualized MEDIAN monthly log-growth over 252d (typical-pace rate)
def f23rg_f23_revenue_growth_engine_cagr_504d_base_v008_signal(revenue):
    # median (not mean) of trailing monthly log-growths -> robust typical growth pace,
    # structurally distinct from any endpoint-ratio CAGR on a stepped series
    mlg = np.log(revenue.replace(0, np.nan)).diff(21)
    med = mlg.rolling(252, min_periods=126).median()
    b = np.exp(med * (252.0 / 21.0)) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR proxy over 1260d annualized (five-year compound, distinct exponent)
def f23rg_f23_revenue_growth_engine_cagr_1260d_base_v009_signal(revenueusd):
    b = _f23_cagr(revenueusd, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability: std of 21d growth over a 252d window (lower = steadier)
def f23rg_f23_revenue_growth_engine_gstd_252d_base_v010_signal(revenue):
    b = _f23_growth_std(revenue, 252, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability: std of 63d growth over a 504d window
def f23rg_f23_revenue_growth_engine_gstd_504d_base_v011_signal(revenue):
    b = _f23_growth_std(revenue, 504, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-to-volatility ratio (information-ratio of growth) over 252d
def f23rg_f23_revenue_growth_engine_girr_252d_base_v012_signal(revenue):
    g = _f23_growth(revenue, 63)
    mu = g.rolling(252, min_periods=126).mean()
    sd = g.rolling(252, min_periods=126).std()
    b = mu / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential growth: 63d growth minus the prior 63d growth (acceleration as level)
def f23rg_f23_revenue_growth_engine_seq_63d_base_v013_signal(revenue):
    b = _f23_seq_growth(revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential growth over 126d windows
def f23rg_f23_revenue_growth_engine_seq_126d_base_v014_signal(revenue):
    b = _f23_seq_growth(revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth vs prior year (ratio): this year's growth FACTOR over last year's, ranked
def f23rg_f23_revenue_growth_engine_gvprior_252d_base_v015_signal(revenue):
    g = _f23_growth(revenue, 252)
    ratio = (1.0 + g) / (1.0 + g.shift(252)).replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth rank vs its own 504d history (percentile of current 63d growth)
def f23rg_f23_revenue_growth_engine_grank_63d_base_v016_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth rank vs its own 252d history (percentile of current 252d growth)
def f23rg_f23_revenue_growth_engine_grank_252d_base_v017_signal(revenueusd):
    g = _f23_growth(revenueusd, 252)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth z-score: 63d growth z-scored vs its own 252d history (de-trended)
def f23rg_f23_revenue_growth_engine_gz_63d_base_v018_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth consistency: fraction of last year with positive 21d sequential change
def f23rg_f23_revenue_growth_engine_gcons_252d_base_v019_signal(revenue):
    up = (revenue.diff(21) > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth streak: length of the consecutive-positive-21d-change run, capped & scaled
def f23rg_f23_revenue_growth_engine_gstreak_base_v020_signal(revenue):
    up = (revenue.diff(21) > 0).astype(float)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    b = (streak.clip(upper=252)) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long growth spread: 63d growth minus 252d growth (acceleration as level)
def f23rg_f23_revenue_growth_engine_gspread_63v252_base_v021_signal(revenue):
    s = _f23_growth(revenue, 63)
    l = _f23_growth(revenue, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long growth spread: 126d growth minus 504d growth
def f23rg_f23_revenue_growth_engine_gspread_126v504_base_v022_signal(revenueusd):
    s = _f23_growth(revenueusd, 126)
    l = _f23_growth(revenueusd, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth dispersion across windows (21/63/126/252) — disagreement of horizons
def f23rg_f23_revenue_growth_engine_gdisp_multi_base_v023_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    g4 = _f23_growth(revenue, 252)
    b = pd.concat([g1, g2, g3, g4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth range across windows: max minus min growth across horizons
def f23rg_f23_revenue_growth_engine_grange_multi_base_v024_signal(revenue):
    g1 = _f23_growth(revenue, 63)
    g2 = _f23_growth(revenue, 126)
    g3 = _f23_growth(revenue, 252)
    g4 = _f23_growth(revenue, 504)
    stacked = pd.concat([g1, g2, g3, g4], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed growth directionality: EWMA(21d growth) / EWMA(|21d growth|) in [-1,1]
def f23rg_f23_revenue_growth_engine_gsmooth_63d_base_v025_signal(revenue):
    g = _f23_growth(revenue, 21)
    num = g.ewm(span=126, min_periods=63).mean()
    den = g.abs().ewm(span=126, min_periods=63).mean()
    b = num / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth displacement: 63d growth minus its own slow EWMA (growth surprise)
def f23rg_f23_revenue_growth_engine_gdisp_63d_base_v026_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = g - g.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed monthly growth acceleration (bounded change in 21d growth over a month)
def f23rg_f23_revenue_growth_engine_gacctanh_63d_base_v027_signal(revenue):
    g = _f23_growth(revenue, 21)
    chg = g - g.shift(21)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of 252d growth (compressed growth level)
def f23rg_f23_revenue_growth_engine_gsignmag_252d_base_v028_signal(revenueusd):
    g = _f23_growth(revenueusd, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth smoothness: 1 minus normalized path roughness of log-revenue over 252d
def f23rg_f23_revenue_growth_engine_gqual_252d_base_v029_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    step = lr.diff(21)
    rough = step.diff(21).abs().rolling(252, min_periods=126).mean()
    scale = step.abs().rolling(252, min_periods=126).mean()
    b = 1.0 - rough / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# level-vs-trend extremity: revenue/252d-mean gap percentile-ranked vs its 504d history
def f23rg_f23_revenue_growth_engine_levtrend_252d_base_v030_signal(revenue):
    mn = _mean(revenue, 252)
    gap = revenue / mn.replace(0, np.nan) - 1.0
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level vs its own 504d trailing mean
def f23rg_f23_revenue_growth_engine_levtrend_504d_base_v031_signal(revenueusd):
    mn = _mean(revenueusd, 504)
    b = revenueusd / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue at a new trailing-252d high? proximity of current revenue to its 252d max
def f23rg_f23_revenue_growth_engine_revhi_252d_base_v032_signal(revenue):
    hi = _rmax(revenue, 252)
    b = revenue / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue trough recovery: current revenue vs its 504d minimum (off-the-bottom growth)
def f23rg_f23_revenue_growth_engine_revrecov_504d_base_v033_signal(revenueusd):
    lo = _rmin(revenueusd, 504)
    b = revenueusd / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth curvature ratio: 63d growth ratio relative to the prior 63d growth ratio
def f23rg_f23_revenue_growth_engine_gcurv_63d_base_v034_signal(revenue):
    r = revenue / revenue.shift(63).replace(0, np.nan)
    # ratio-of-ratios (multiplicative acceleration), de-trended vs its 252d mean
    rr = r / r.shift(63).replace(0, np.nan)
    b = rr - rr.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-medium pace ratio: 21d growth relative to 63d growth (impulse vs trend)
def f23rg_f23_revenue_growth_engine_gcurv_21d_base_v035_signal(revenue):
    g21 = _f23_growth(revenue, 21)
    g63 = _f23_growth(revenue, 63)
    # annualize both to comparable rates, take the gap (recent impulse vs trend pace)
    b = 3.0 * g21 - g63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year quarter accel: latest-quarter growth vs the same quarter a year ago
def f23rg_f23_revenue_growth_engine_ghalf_base_v036_signal(revenue):
    recent = revenue / revenue.shift(63).replace(0, np.nan)
    yago = revenue.shift(252) / revenue.shift(315).replace(0, np.nan)
    b = recent / yago.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth percentile-rank of the 126d growth vs its own 504d history
def f23rg_f23_revenue_growth_engine_grank_126d_base_v037_signal(revenue):
    g = _f23_growth(revenue, 126)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR proxy z-scored vs own history (durable growth de-trended)
def f23rg_f23_revenue_growth_engine_cagrz_252d_base_v038_signal(revenue):
    c = _f23_cagr(revenue, 252)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability rank: std-of-growth ranked (low rank = steadiest grower)
def f23rg_f23_revenue_growth_engine_gstabrank_base_v039_signal(revenue):
    sd = _f23_growth_std(revenue, 252, 21)
    b = _rank(sd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of growth (dispersion / |mean|) over 252d
def f23rg_f23_revenue_growth_engine_gcv_252d_base_v040_signal(revenue):
    g = _f23_growth(revenue, 63)
    mu = g.rolling(252, min_periods=126).mean()
    sd = g.rolling(252, min_periods=126).std()
    b = sd / mu.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth breadth: fraction of last year where 63d growth exceeds its 252d median
def f23rg_f23_revenue_growth_engine_gbreadth_base_v041_signal(revenue):
    g = _f23_growth(revenue, 63)
    med = g.rolling(252, min_periods=126).median()
    above = (g > med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth momentum: change in 252d growth over a quarter
def f23rg_f23_revenue_growth_engine_gmom_252d_base_v042_signal(revenueusd):
    g = _f23_growth(revenueusd, 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth momentum (short): change in 63d growth over a month
def f23rg_f23_revenue_growth_engine_gmom_63d_base_v043_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = g - g.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth range width: spread between trailing-252d max and min of the 126d growth
def f23rg_f23_revenue_growth_engine_gvprior_126d_base_v044_signal(revenue):
    g = _f23_growth(revenue, 126)
    peak = g.rolling(252, min_periods=126).max()
    trough = g.rolling(252, min_periods=126).min()
    b = peak - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth: 252d growth gated by whether growth is also accelerating (seq sign)
def f23rg_f23_revenue_growth_engine_gdurable_base_v045_signal(revenue):
    g252 = _f23_growth(revenue, 252)
    seq = _f23_seq_growth(revenue, 63)
    accel = np.tanh(10.0 * seq)  # in (-1,1): +1 accelerating, -1 decelerating
    b = g252 * accel
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth skew across horizons (asymmetry of the growth term-structure)
def f23rg_f23_revenue_growth_engine_gskew_multi_base_v046_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    g4 = _f23_growth(revenue, 252)
    g5 = _f23_growth(revenue, 504)
    stacked = pd.concat([g1, g2, g3, g4, g5], axis=1)
    mean = stacked.mean(axis=1)
    med = stacked.median(axis=1)
    sd = stacked.std(axis=1)
    b = (mean - med) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend t-stat: log-revenue regression slope over 126d divided by its residual SE
def f23rg_f23_revenue_growth_engine_gslope_126d_base_v047_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    w = 126

    def _tstat(a):
        nn = len(a)
        x = np.arange(nn, dtype=float)
        xm = x.mean()
        d = x - xm
        den = (d * d).sum()
        if den == 0:
            return np.nan
        slope = (d * (a - a.mean())).sum() / den
        resid = a - (a.mean() + slope * d)
        sse = (resid * resid).sum()
        if nn <= 2 or sse <= 0:
            return np.nan
        se = (sse / (nn - 2)) ** 0.5 / (den ** 0.5)
        if se == 0:
            return np.nan
        return slope / se

    b = lr.rolling(w, min_periods=63).apply(_tstat, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue level percentile vs its own 504d history (where in its range)
def f23rg_f23_revenue_growth_engine_levrank_504d_base_v048_signal(revenueusd):
    b = _rank(revenueusd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth drawdown: current 252d growth vs its trailing-252d peak growth
def f23rg_f23_revenue_growth_engine_gdd_252d_base_v049_signal(revenue):
    g = _f23_growth(revenue, 252)
    peak = g.rolling(252, min_periods=126).max()
    b = g - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth recovery off trough: current 63d growth vs its trailing-252d min growth
def f23rg_f23_revenue_growth_engine_grecov_63d_base_v050_signal(revenue):
    g = _f23_growth(revenue, 63)
    trough = g.rolling(252, min_periods=126).min()
    b = g - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-year stacked growth: compound of two consecutive 252d growths (durability)
def f23rg_f23_revenue_growth_engine_gstack_504d_base_v051_signal(revenueusd):
    r1 = revenueusd / revenueusd.shift(252).replace(0, np.nan)
    r2 = revenueusd.shift(252) / revenueusd.shift(504).replace(0, np.nan)
    b = (r1 * r2) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth inflection: sign x magnitude of the change in 126d growth vs a year ago
def f23rg_f23_revenue_growth_engine_ginflect_63d_base_v052_signal(revenue):
    g = _f23_growth(revenue, 126)
    d = g - g.shift(252)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-of-growth: 21d change of the 63d growth, smoothed (sustained acceleration)
def f23rg_f23_revenue_growth_engine_gog_base_v053_signal(revenue):
    g = _f23_growth(revenue, 63)
    acc = g - g.shift(21)
    b = acc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside growth semi-deviation: dispersion of only positive growth excursions
def f23rg_f23_revenue_growth_engine_gupsd_252d_base_v054_signal(revenue):
    g = _f23_growth(revenue, 63)
    med = g.rolling(252, min_periods=126).median()
    excess = (g - med).clip(lower=0)
    b = (excess ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside growth semi-deviation: dispersion of only negative growth excursions
def f23rg_f23_revenue_growth_engine_gdnsd_252d_base_v055_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    med = g.rolling(252, min_periods=126).median()
    shortfall = (med - g).clip(lower=0)
    b = (shortfall ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-vs-trend gap: 63d growth minus its 504d-window mean (anomaly)
def f23rg_f23_revenue_growth_engine_gtrendgap_base_v056_signal(revenue):
    g = _f23_growth(revenue, 63)
    b = g - g.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration ratio: 21d growth over 126d-average 21d growth (relative pace)
def f23rg_f23_revenue_growth_engine_gpace_21d_base_v057_signal(revenue):
    g = _f23_growth(revenue, 21)
    avg = g.rolling(126, min_periods=63).mean()
    b = g / avg.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR regime rank: where the current 252d CAGR sits within its own 504d distribution
def f23rg_f23_revenue_growth_engine_cagrspread_base_v058_signal(revenue):
    c_short = _f23_cagr(revenue, 252)
    b = _rank(c_short, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth hit-rate of beating last quarter (sequential-positive frequency)
def f23rg_f23_revenue_growth_engine_seqhit_base_v059_signal(revenue):
    seq = _f23_seq_growth(revenue, 63)
    hit = (seq > 0).astype(float)
    b = hit.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth choppiness: rate of sign-flips in monthly revenue changes (smooth vs choppy)
def f23rg_f23_revenue_growth_engine_gchop_base_v060_signal(revenue):
    sgn = np.sign(revenue.diff(21))
    flips = (sgn != sgn.shift(21)).astype(float)
    b = flips.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-horizon growth composite: short-weighted blend of 21/63/126/252 growth
def f23rg_f23_revenue_growth_engine_gblend_base_v061_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    g4 = _f23_growth(revenue, 252)
    b = 0.4 * g1 + 0.3 * g2 + 0.2 * g3 + 0.1 * g4
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth persistence: rolling autocorrelation of 21d growth at lag 21 over 252d
def f23rg_f23_revenue_growth_engine_gautocorr_base_v062_signal(revenue):
    g = _f23_growth(revenue, 21)
    gl = g.shift(21)
    b = g.rolling(252, min_periods=126).corr(gl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 63d-growth USD vs domestic series spread (currency / mix tilt)
def f23rg_f23_revenue_growth_engine_fxgap_63d_base_v063_signal(revenue, revenueusd):
    g_loc = _f23_growth(revenue, 63)
    g_usd = _f23_growth(revenueusd, 63)
    b = g_usd - g_loc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 252d-growth USD vs domestic spread (long-horizon currency tilt)
def f23rg_f23_revenue_growth_engine_fxgap_252d_base_v064_signal(revenue, revenueusd):
    g_loc = _f23_growth(revenue, 252)
    g_usd = _f23_growth(revenueusd, 252)
    b = g_usd - g_loc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth surprise z: latest 21d growth z-scored vs trailing 126d growth distribution
def f23rg_f23_revenue_growth_engine_gsurprise_21d_base_v065_signal(revenue):
    g = _f23_growth(revenue, 21)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# staleness of expansion: trading days since revenue last set a trailing-252d high
def f23rg_f23_revenue_growth_engine_newhifreq_base_v066_signal(revenue):
    w = 252

    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = revenue.rolling(w, min_periods=126).apply(_dsh, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth concavity: is growth decelerating? second diff of 126d growth
def f23rg_f23_revenue_growth_engine_gconcav_126d_base_v067_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    b = g - 2.0 * g.shift(63) + g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth efficiency ratio: net log-growth over sum of absolute monthly log-moves
def f23rg_f23_revenue_growth_engine_geff_252d_base_v068_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    net = (lr - lr.shift(252)).abs()
    path = lr.diff(21).abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth tilt: rank of current revenue level minus rank of 252d-ago level
def f23rg_f23_revenue_growth_engine_levranktilt_base_v069_signal(revenueusd):
    r_now = _rank(revenueusd, 504)
    b = r_now - r_now.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth quality blended with stability rank (high-growth, steady-grower score)
def f23rg_f23_revenue_growth_engine_gqualrank_base_v070_signal(revenue):
    g = _f23_growth(revenue, 252)
    g_rank = _rank(g, 504)
    sd = _f23_growth_std(revenue, 252, 21)
    stab_rank = _rank(sd, 504)
    b = g_rank - stab_rank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth diffusion: tanh-weighted net agreement of horizons (21/63/126/252/504)
def f23rg_f23_revenue_growth_engine_gewslope_base_v071_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    g4 = _f23_growth(revenue, 252)
    g5 = _f23_growth(revenue, 504)
    # annualize each to a comparable rate, then squash and average (continuous)
    a1 = np.tanh(g1 * 12.0)
    a2 = np.tanh(g2 * 4.0)
    a3 = np.tanh(g3 * 2.0)
    a4 = np.tanh(g4 * 1.0)
    a5 = np.tanh(g5 * 0.5)
    stacked = pd.concat([a1, a2, a3, a4, a5], axis=1)
    # horizon disagreement: low when all horizons agree on direction/strength
    b = stacked.std(axis=1) * np.sign(stacked.mean(axis=1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth dispersion change: is the growth path getting more volatile over time?
def f23rg_f23_revenue_growth_engine_gdispchg_base_v072_signal(revenue):
    sd = _f23_growth_std(revenue, 126, 21)
    b = sd - sd.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue compound vs simple growth gap (volatility drag on growth path)
def f23rg_f23_revenue_growth_engine_gdrag_base_v073_signal(revenueusd):
    simple = _f23_growth(revenueusd, 252)
    compound = np.exp(np.log(revenueusd.replace(0, np.nan)).diff(21).rolling(
        252, min_periods=126).sum()) - 1.0
    b = simple - compound
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth streak intensity: signed run-length of sequential-growth direction
def f23rg_f23_revenue_growth_engine_seqstreak_base_v074_signal(revenue):
    seq = _f23_seq_growth(revenue, 63)
    sgn = np.sign(seq)
    grp = (sgn != sgn.shift(1)).cumsum()
    run = sgn.groupby(grp).cumcount() + 1
    b = (sgn * run.clip(upper=63)) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted level: revenue z-score scaled by its 252d CAGR (size-of-grower)
def f23rg_f23_revenue_growth_engine_gradjlev_base_v075_signal(revenue):
    c = _f23_cagr(revenue, 252)
    lev_z = _z(np.log(revenue.replace(0, np.nan)), 504)
    b = lev_z * np.sign(c) * (c.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23rg_f23_revenue_growth_engine_grw_21d_base_v001_signal,
    f23rg_f23_revenue_growth_engine_grw_63d_base_v002_signal,
    f23rg_f23_revenue_growth_engine_grw_126d_base_v003_signal,
    f23rg_f23_revenue_growth_engine_grw_252d_base_v004_signal,
    f23rg_f23_revenue_growth_engine_grw_504d_base_v005_signal,
    f23rg_f23_revenue_growth_engine_lgrw_252d_base_v006_signal,
    f23rg_f23_revenue_growth_engine_cagr_252d_base_v007_signal,
    f23rg_f23_revenue_growth_engine_cagr_504d_base_v008_signal,
    f23rg_f23_revenue_growth_engine_cagr_1260d_base_v009_signal,
    f23rg_f23_revenue_growth_engine_gstd_252d_base_v010_signal,
    f23rg_f23_revenue_growth_engine_gstd_504d_base_v011_signal,
    f23rg_f23_revenue_growth_engine_girr_252d_base_v012_signal,
    f23rg_f23_revenue_growth_engine_seq_63d_base_v013_signal,
    f23rg_f23_revenue_growth_engine_seq_126d_base_v014_signal,
    f23rg_f23_revenue_growth_engine_gvprior_252d_base_v015_signal,
    f23rg_f23_revenue_growth_engine_grank_63d_base_v016_signal,
    f23rg_f23_revenue_growth_engine_grank_252d_base_v017_signal,
    f23rg_f23_revenue_growth_engine_gz_63d_base_v018_signal,
    f23rg_f23_revenue_growth_engine_gcons_252d_base_v019_signal,
    f23rg_f23_revenue_growth_engine_gstreak_base_v020_signal,
    f23rg_f23_revenue_growth_engine_gspread_63v252_base_v021_signal,
    f23rg_f23_revenue_growth_engine_gspread_126v504_base_v022_signal,
    f23rg_f23_revenue_growth_engine_gdisp_multi_base_v023_signal,
    f23rg_f23_revenue_growth_engine_grange_multi_base_v024_signal,
    f23rg_f23_revenue_growth_engine_gsmooth_63d_base_v025_signal,
    f23rg_f23_revenue_growth_engine_gdisp_63d_base_v026_signal,
    f23rg_f23_revenue_growth_engine_gacctanh_63d_base_v027_signal,
    f23rg_f23_revenue_growth_engine_gsignmag_252d_base_v028_signal,
    f23rg_f23_revenue_growth_engine_gqual_252d_base_v029_signal,
    f23rg_f23_revenue_growth_engine_levtrend_252d_base_v030_signal,
    f23rg_f23_revenue_growth_engine_levtrend_504d_base_v031_signal,
    f23rg_f23_revenue_growth_engine_revhi_252d_base_v032_signal,
    f23rg_f23_revenue_growth_engine_revrecov_504d_base_v033_signal,
    f23rg_f23_revenue_growth_engine_gcurv_63d_base_v034_signal,
    f23rg_f23_revenue_growth_engine_gcurv_21d_base_v035_signal,
    f23rg_f23_revenue_growth_engine_ghalf_base_v036_signal,
    f23rg_f23_revenue_growth_engine_grank_126d_base_v037_signal,
    f23rg_f23_revenue_growth_engine_cagrz_252d_base_v038_signal,
    f23rg_f23_revenue_growth_engine_gstabrank_base_v039_signal,
    f23rg_f23_revenue_growth_engine_gcv_252d_base_v040_signal,
    f23rg_f23_revenue_growth_engine_gbreadth_base_v041_signal,
    f23rg_f23_revenue_growth_engine_gmom_252d_base_v042_signal,
    f23rg_f23_revenue_growth_engine_gmom_63d_base_v043_signal,
    f23rg_f23_revenue_growth_engine_gvprior_126d_base_v044_signal,
    f23rg_f23_revenue_growth_engine_gdurable_base_v045_signal,
    f23rg_f23_revenue_growth_engine_gskew_multi_base_v046_signal,
    f23rg_f23_revenue_growth_engine_gslope_126d_base_v047_signal,
    f23rg_f23_revenue_growth_engine_levrank_504d_base_v048_signal,
    f23rg_f23_revenue_growth_engine_gdd_252d_base_v049_signal,
    f23rg_f23_revenue_growth_engine_grecov_63d_base_v050_signal,
    f23rg_f23_revenue_growth_engine_gstack_504d_base_v051_signal,
    f23rg_f23_revenue_growth_engine_ginflect_63d_base_v052_signal,
    f23rg_f23_revenue_growth_engine_gog_base_v053_signal,
    f23rg_f23_revenue_growth_engine_gupsd_252d_base_v054_signal,
    f23rg_f23_revenue_growth_engine_gdnsd_252d_base_v055_signal,
    f23rg_f23_revenue_growth_engine_gtrendgap_base_v056_signal,
    f23rg_f23_revenue_growth_engine_gpace_21d_base_v057_signal,
    f23rg_f23_revenue_growth_engine_cagrspread_base_v058_signal,
    f23rg_f23_revenue_growth_engine_seqhit_base_v059_signal,
    f23rg_f23_revenue_growth_engine_gchop_base_v060_signal,
    f23rg_f23_revenue_growth_engine_gblend_base_v061_signal,
    f23rg_f23_revenue_growth_engine_gautocorr_base_v062_signal,
    f23rg_f23_revenue_growth_engine_fxgap_63d_base_v063_signal,
    f23rg_f23_revenue_growth_engine_fxgap_252d_base_v064_signal,
    f23rg_f23_revenue_growth_engine_gsurprise_21d_base_v065_signal,
    f23rg_f23_revenue_growth_engine_newhifreq_base_v066_signal,
    f23rg_f23_revenue_growth_engine_gconcav_126d_base_v067_signal,
    f23rg_f23_revenue_growth_engine_geff_252d_base_v068_signal,
    f23rg_f23_revenue_growth_engine_levranktilt_base_v069_signal,
    f23rg_f23_revenue_growth_engine_gqualrank_base_v070_signal,
    f23rg_f23_revenue_growth_engine_gewslope_base_v071_signal,
    f23rg_f23_revenue_growth_engine_gdispchg_base_v072_signal,
    f23rg_f23_revenue_growth_engine_gdrag_base_v073_signal,
    f23rg_f23_revenue_growth_engine_seqstreak_base_v074_signal,
    f23rg_f23_revenue_growth_engine_gradjlev_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_REVENUE_GROWTH_ENGINE_REGISTRY_001_075 = REGISTRY


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

    print("OK f23_revenue_growth_engine_base_001_075_claude: %d features pass" % n_features)
