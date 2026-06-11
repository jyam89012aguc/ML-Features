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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    def _f(a):
        k = len(a)
        idx = np.arange(k, dtype=float)
        idx = idx - idx.mean()
        denom = (idx * idx).sum()
        if denom == 0:
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (hypergrowth signature: growth x margin x reinvestment) =====
def _f31_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f31_pct_growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f31_gross_margin(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f31_rnd_intensity(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f31_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f31_rule40(rev_growth, ocf_margin):
    return rev_growth + ocf_margin


def _f31_margin_expansion(margin, w):
    return margin - margin.shift(w)


# ============================================================
# sequential (quarterly) revenue growth x gross-margin level
def f31hg_f31_hypergrowth_signature_seqgrth_63d_base_v076_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    m = _f31_gross_margin(gp, revenue)
    b = g * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sequential gp growth x reported grossmargin
def f31hg_f31_hypergrowth_signature_seqgpgrth_63d_base_v077_signal(gp, grossmargin):
    g = _f31_growth(gp, 63)
    b = g * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR proxy (annualized 504d growth) x gross margin level
def f31hg_f31_hypergrowth_signature_cagrmargin_504d_base_v078_signal(revenue, gp):
    cagr = (1.0 + _f31_pct_growth(revenue, 504)).clip(lower=0.01) ** 0.5 - 1.0
    m = _f31_gross_margin(gp, revenue)
    b = cagr * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CAGR proxy x cash-margin (Rule-of-40 with compounded growth)
def f31hg_f31_hypergrowth_signature_cagrrule40_504d_base_v079_signal(revenue, ncfo):
    cagr = (1.0 + _f31_pct_growth(revenue, 504)).clip(lower=0.01) ** 0.5 - 1.0
    om = _f31_ocf_margin(ncfo, revenue)
    b = cagr + om
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-acceleration (short vs long growth) x margin (re-acceleration signature)
def f31hg_f31_hypergrowth_signature_reaccel_252d_base_v080_signal(revenue, gp):
    gs = _f31_growth(revenue, 63)
    gl = _f31_growth(revenue, 252) * (63.0 / 252.0)
    m = _f31_gross_margin(gp, revenue)
    b = (gs - gl) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-acceleration x cash-margin (ramping R&D backed by cash)
def f31hg_f31_hypergrowth_signature_reinvaccel_252d_base_v081_signal(rnd, revenue, ncfo):
    ri = _f31_rnd_intensity(rnd, revenue)
    accel = ri - 2.0 * ri.shift(126) + ri.shift(252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = accel * (1.0 + om)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory (slope) x revenue growth (expanding-margin grower)
def f31hg_f31_hypergrowth_signature_margslope_126d_base_v082_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    sl = _slope(m, 126)
    g = _f31_growth(revenue, 126)
    b = sl * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 slope (improving cash-growth profile)
def f31hg_f31_hypergrowth_signature_rule40slope_126d_base_v083_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = _slope(g + om, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth slope (R&D-backed acceleration over time)
def f31hg_f31_hypergrowth_signature_reinvslope_126d_base_v084_signal(revenue, rnd):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = _slope(g * ri, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin spread between two horizons (short minus long, margin-weighted gap)
def f31hg_f31_hypergrowth_signature_gmspread_252v504_base_v085_signal(revenue, gp):
    m = _f31_gross_margin(gp, revenue)
    gs = _f31_growth(revenue, 126)
    gl = _f31_growth(revenue, 504) * (126.0 / 504.0)
    b = (gs - gl) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 spread between two horizons
def f31hg_f31_hypergrowth_signature_r40spread_252v504_base_v086_signal(revenue, ncfo):
    om = _f31_ocf_margin(ncfo, revenue)
    s = _f31_pct_growth(revenue, 252) + om
    l = _f31_pct_growth(revenue, 504) + om
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable composite: revenue growth x margin, dispersion-penalized (consistency)
def f31hg_f31_hypergrowth_signature_consistgm_252d_base_v087_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    m = _f31_gross_margin(gp, revenue)
    gm = g * m
    b = _mean(gm, 252) - 1.5 * _std(gm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 consistency (downside-penalized cash-growth)
def f31hg_f31_hypergrowth_signature_r40consist_252d_base_v088_signal(revenue, ncfo):
    g = _f31_growth(revenue, 63)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    downside = r40.where(r40 < _mean(r40, 252)).rolling(252, min_periods=63).std()
    b = _mean(r40, 252) - downside
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin hit-rate: fraction of months both growth>0 and margin rising
def f31hg_f31_hypergrowth_signature_gmhit_252d_base_v089_signal(revenue, gp):
    g = _f31_growth(revenue, 21)
    m = _f31_gross_margin(gp, revenue)
    dm = m - m.shift(21)
    both = ((g > 0) & (dm > 0)).astype(float)
    b = both.rolling(252, min_periods=126).mean() + 0.2 * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment hit-rate: fraction R&D-intensity rising while revenue grows
def f31hg_f31_hypergrowth_signature_reinvhit_252d_base_v090_signal(rnd, revenue):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(21)
    g = _f31_growth(revenue, 21)
    both = ((g > 0) & (dri > 0)).astype(float)
    b = both.rolling(252, min_periods=126).mean() + 0.3 * ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-weighted growth asymmetry: upside growth vol minus downside, x margin
def f31hg_f31_hypergrowth_signature_grthasym_252d_base_v091_signal(revenue, gp):
    g = _f31_growth(revenue, 21)
    up = g.where(g > 0).rolling(252, min_periods=63).std()
    dn = g.where(g < 0).rolling(252, min_periods=63).std()
    m = _f31_gross_margin(gp, revenue)
    b = (up - dn) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin asymmetry x revenue growth (cash-stability of fast growers)
def f31hg_f31_hypergrowth_signature_cashasym_252d_base_v092_signal(ncfo, revenue):
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(21)
    up = dom.where(dom > 0).rolling(252, min_periods=63).std()
    dn = dom.where(dom < 0).rolling(252, min_periods=63).std()
    g = _f31_growth(revenue, 126)
    b = (dn - up) * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triad rank: average of growth-rank, margin-rank, reinvestment-rank
def f31hg_f31_hypergrowth_signature_triadrank_252d_base_v093_signal(revenue, gp, rnd):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = (_rank(g, 504) + _rank(m, 504) + _rank(ri, 504)) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 rank percentile (relative hypergrowth standing)
def f31hg_f31_hypergrowth_signature_r40rank_252d_base_v094_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = _rank(g + om, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion x reinvestment-rank (efficient reinvestment lifting margins)
def f31hg_f31_hypergrowth_signature_effreinv_252d_base_v095_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = dm * (_rank(ri, 504) + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite log-score: log of (growth+1) plus log of (margin) plus log of (1+cash-margin)
def f31hg_f31_hypergrowth_signature_logscore_252d_base_v096_signal(revenue, gp, ncfo):
    g = (1.0 + _f31_pct_growth(revenue, 252)).clip(lower=0.05)
    m = _f31_gross_margin(gp, revenue).clip(lower=0.01)
    om = (1.0 + _f31_ocf_margin(ncfo, revenue)).clip(lower=0.05)
    b = np.log(g) + np.log(m) + np.log(om)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality momentum: change in (growth x cash-conversion) over a quarter
def f31hg_f31_hypergrowth_signature_gqmom_252d_base_v097_signal(revenue, ncfo, gp):
    g = _f31_growth(revenue, 252)
    cc = ncfo / gp.replace(0, np.nan)
    gq = g * cc
    b = gq - gq.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth momentum (acceleration of R&D-backed growth)
def f31hg_f31_hypergrowth_signature_reinvmom_252d_base_v098_signal(revenue, rnd):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    rg = g * ri
    b = rg - rg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-defended growth: growth x margin minus penalty for margin volatility
def f31hg_f31_hypergrowth_signature_margdefend_252d_base_v099_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    mvol = _std(m, 252)
    b = g * m - 20.0 * g.abs() * mvol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-defended Rule-of-40: rule-of-40 minus its own volatility (stable-cash growers)
def f31hg_f31_hypergrowth_signature_r40defend_252d_base_v100_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    b = r40 - 1.5 * _std(r40, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x margin x reinvestment-coverage by cash (full self-funded hypergrowth)
def f31hg_f31_hypergrowth_signature_selfgrow_252d_base_v101_signal(revenue, gp, rnd, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    cov = (ncfo - rnd) / revenue.replace(0, np.nan)
    b = g * m * (1.0 + cov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-after-RnD margin x revenue growth (growth funded after reinvestment)
def f31hg_f31_hypergrowth_signature_fcfreinv_252d_base_v102_signal(ncfo, rnd, revenue):
    fcfar = (ncfo - rnd) / revenue.replace(0, np.nan)
    g = _f31_growth(revenue, 252)
    b = fcfar * (1.0 + 2.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin level x reinvestment-funded growth-rank (quality + funded-growth)
def f31hg_f31_hypergrowth_signature_qualfunded_252d_base_v103_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = m * _rank(g * ri, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth: minimum of (rev-growth, gp-growth, ocf-growth) weighted by margin
def f31hg_f31_hypergrowth_signature_minall_252d_base_v104_signal(revenue, gp, ncfo):
    rg = _f31_growth(revenue, 252)
    gg = _f31_growth(gp, 252)
    og = _f31_growth(ncfo.abs() + 1.0, 252)
    m = _f31_gross_margin(gp, revenue)
    b = pd.concat([rg, gg, og], axis=1).min(axis=1) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin product EMA crossover (fast vs slow signature)
def f31hg_f31_hypergrowth_signature_gmcross_252d_base_v105_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    gm = g * m
    b = gm.ewm(span=21, min_periods=10).mean() - gm.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 EMA crossover (cash-growth regime change)
def f31hg_f31_hypergrowth_signature_r40cross_252d_base_v106_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    b = r40.ewm(span=21, min_periods=10).mean() - r40.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion convexity x growth: reward accelerating margin under growth
def f31hg_f31_hypergrowth_signature_margconvex_252d_base_v107_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    accel = m - 2.0 * m.shift(126) + m.shift(252)
    g = _f31_growth(revenue, 252)
    b = accel * (1.0 + 3.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-intensity z x revenue-growth z (standardized reinvest-growth interaction)
def f31hg_f31_hypergrowth_signature_zreinv_252d_base_v108_signal(rnd, revenue):
    ri = _f31_rnd_intensity(rnd, revenue)
    g = _f31_growth(revenue, 252)
    b = _z(ri, 252) * _z(g, 252) + 0.3 * _z(ri, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin z x margin-expansion z (standardized cash + improving-margin)
def f31hg_f31_hypergrowth_signature_zcashmarg_252d_base_v109_signal(ncfo, revenue, gp):
    om = _f31_ocf_margin(ncfo, revenue)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    b = _z(om, 252) * _z(dm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-z product: growth-z x margin-z x cash-margin-z (rare-triple signature)
def f31hg_f31_hypergrowth_signature_triplez_252d_base_v110_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    b = _z(g, 252) * _z(m, 252) + _z(g, 252) * _z(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-rate-of-gross-profit-per-RnD (R&D productivity growth) x margin
def f31hg_f31_hypergrowth_signature_rndprod_252d_base_v111_signal(gp, rnd, revenue):
    prod = gp / rnd.replace(0, np.nan)
    gprod = _f31_growth(prod, 252)
    m = _f31_gross_margin(gp, revenue)
    b = gprod * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-RnD growth (sales productivity of R&D) x cash-margin
def f31hg_f31_hypergrowth_signature_salesprod_252d_base_v112_signal(revenue, rnd, ncfo):
    prod = revenue / rnd.replace(0, np.nan)
    gprod = _f31_growth(prod, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = gprod * (1.0 + om)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin product, ranked then EMA-smoothed (durable relative hypergrowth)
def f31hg_f31_hypergrowth_signature_gmrankema_252d_base_v113_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    r = _rank(g * m, 504)
    b = r.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-of-reinvestment Rule-of-40, ranked (sustainable rule-of-40, heavy reinvest penalty)
def f31hg_f31_hypergrowth_signature_r40netrank_252d_base_v114_signal(revenue, ncfo, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = _rank(g + om - 4.0 * ri, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-momentum gated by growth-momentum (co-improving regime)
def f31hg_f31_hypergrowth_signature_comprove_252d_base_v115_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    dm = m - m.shift(63)
    g = _f31_growth(revenue, 252)
    dg = g - g.shift(63)
    b = np.sign(dg) * dm.abs() + np.sign(dm) * dg.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion stability premium x growth (reliable-cash growers; stability-led)
def f31hg_f31_hypergrowth_signature_ccstab_252d_base_v116_signal(ncfo, gp, revenue):
    cc = ncfo / gp.replace(0, np.nan)
    stab = 1.0 / (1.0 + 5.0 * _std(cc, 126))
    g = _f31_growth(revenue, 252)
    ccdev = cc - _mean(cc, 252)
    b = stab * np.sign(g) + ccdev * np.tanh(3.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# organic vs funded growth: reinvestment-trend dominant, margin-growth as modifier
def f31hg_f31_hypergrowth_signature_organic_252d_base_v117_signal(revenue, gp, rnd):
    g = _f31_growth(revenue, 126)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(126)
    b = -dri + 0.5 * g * m - 3.0 * dri * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth, smoothed and differenced (impulse signature)
def f31hg_f31_hypergrowth_signature_reinvimp_252d_base_v118_signal(revenue, rnd):
    g = _f31_growth(revenue, 126)
    ri = _f31_rnd_intensity(rnd, revenue)
    rg = (g * ri).ewm(span=42, min_periods=21).mean()
    b = rg - rg.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-quality: margin level x positive-growth-streak fraction
def f31hg_f31_hypergrowth_signature_growstreak_252d_base_v119_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    streak = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    m = _f31_gross_margin(gp, revenue)
    b = streak * m + 0.1 * _mean(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-cash-flow streak (cash-durability led) modulated by growth
def f31hg_f31_hypergrowth_signature_cashstreak_252d_base_v120_signal(ncfo, revenue):
    pos = (ncfo > 0).astype(float).rolling(252, min_periods=126).mean()
    g = _f31_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = pos * (1.0 + g) + (om - _mean(om, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin product times reinvestment-momentum (reinvestment-accel led)
def f31hg_f31_hypergrowth_signature_fundedaccel_252d_base_v121_signal(revenue, gp, rnd):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(126)
    b = dri * (1.0 + np.tanh(5.0 * g)) + g * m * dri * 10.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log gross-profit-dollar growth x cash-margin level (profit-dollar cash composite)
def f31hg_f31_hypergrowth_signature_gpdollar_252d_base_v122_signal(gp, ncfo, revenue):
    gg = _f31_growth(gp, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = gg * (om - _mean(om, 252)) + 0.3 * gg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 with margin tiebreaker (growth+cash, margin used to scale)
def f31hg_f31_hypergrowth_signature_r40margin_252d_base_v123_signal(revenue, ncfo, gp):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    m = _f31_gross_margin(gp, revenue)
    b = (g + om) * (0.5 + m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion-rate per unit growth (margin leverage of growth)
def f31hg_f31_hypergrowth_signature_marglev_252d_base_v124_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    g = _f31_pct_growth(revenue, 252).replace(0, np.nan)
    b = np.tanh(dm / g.abs().clip(lower=0.02)) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-to-growth efficiency, smoothed (durable growth-per-RnD)
def f31hg_f31_hypergrowth_signature_growperreinv_252d_base_v125_signal(revenue, rnd):
    g = _f31_pct_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue).replace(0, np.nan)
    eff = g / ri
    b = eff.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin trajectory x margin trajectory (twin improving margins)
def f31hg_f31_hypergrowth_signature_twinmargin_252d_base_v126_signal(ncfo, revenue, gp):
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    b = dom * m + dm * (0.5 + om)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin product Sharpe over the year (risk-adjusted hypergrowth)
def f31hg_f31_hypergrowth_signature_gmsharpe_252d_base_v127_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    m = _f31_gross_margin(gp, revenue)
    gm = g * m
    b = _mean(gm, 252) / _std(gm, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite triad-min (weakest of growth/margin/reinvest ranks) - balanced quality
def f31hg_f31_hypergrowth_signature_triadmin_252d_base_v128_signal(revenue, gp, rnd):
    g = _rank(_f31_growth(revenue, 252), 504)
    m = _rank(_f31_gross_margin(gp, revenue), 504)
    ri = _rank(_f31_rnd_intensity(rnd, revenue), 504)
    b = pd.concat([g, m, ri], axis=1).min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth gated by cash-margin sign (cash-positive growth regime; cash-sign led)
def f31hg_f31_hypergrowth_signature_cashposgrow_252d_base_v129_signal(revenue, ncfo, gp):
    g = _f31_growth(revenue, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    m = _f31_gross_margin(gp, revenue)
    gate = np.tanh(10.0 * om)
    b = gate * np.tanh(5.0 * g) + 0.3 * gate * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment ramp x margin expansion (investing into margin gains)
def f31hg_f31_hypergrowth_signature_investmargin_252d_base_v130_signal(rnd, revenue, gp):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    b = np.sign(dri) * dm.abs() + dri * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite: CAGR x cash-margin DEVIATION (long cash-surprise growth)
def f31hg_f31_hypergrowth_signature_longdur_504d_base_v131_signal(revenue, gp, ncfo):
    cagr = (1.0 + _f31_pct_growth(revenue, 504)).clip(lower=0.01) ** 0.5 - 1.0
    om = _f31_ocf_margin(ncfo, revenue)
    omdev = om - _mean(om, 252)
    m = _f31_gross_margin(gp, revenue)
    b = cagr * omdev + 0.2 * cagr * np.sign(m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin product year-over-year change, normalized by its own dispersion
def f31hg_f31_hypergrowth_signature_gmyoy_252d_base_v132_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    gm = g * m
    chg = gm - gm.shift(252)
    b = chg / (1.0 + _std(gm, 252)) + 0.5 * np.sign(chg) * (m - _mean(m, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 minus rolling-min (resilience above worst rule-of-40)
def f31hg_f31_hypergrowth_signature_r40resil_252d_base_v133_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    b = r40 - r40.rolling(504, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin level x growth-percentile, EMA-smoothed (durable high-margin growers)
def f31hg_f31_hypergrowth_signature_hmgrow_252d_base_v134_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    g = _f31_growth(revenue, 252)
    raw = m * (_rank(g, 504) + 0.5)
    b = raw.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth divided by margin volatility (clean funded growth)
def f31hg_f31_hypergrowth_signature_cleanfunded_252d_base_v135_signal(revenue, rnd, gp):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    m = _f31_gross_margin(gp, revenue)
    mvol = _std(m, 252)
    b = (g * ri) / (1.0 + 25.0 * mvol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-burn penalty on growth (burn-led: penalize fast growth that burns cash)
def f31hg_f31_hypergrowth_signature_cashefficient_252d_base_v136_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    burn = (-om).clip(lower=0)
    b = -burn * (1.0 + g.abs()) - 0.3 * _std(om, 126) * np.sign(m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-growth x rnd-intensity-rank (profit growth backed by reinvestment standing)
def f31hg_f31_hypergrowth_signature_gpreinvrank_252d_base_v137_signal(gp, rnd, revenue):
    gg = _f31_growth(gp, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = gg * (_rank(ri, 504) + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite slope of the triad-sum (improving overall hypergrowth profile)
def f31hg_f31_hypergrowth_signature_triadslope_126d_base_v138_signal(revenue, gp, rnd):
    g = _f31_pct_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = _slope(g + m + ri, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smooth-cash hypergrowth: cash-margin level penalized by its own volatility, growth-scaled
def f31hg_f31_hypergrowth_signature_smoothcash_252d_base_v139_signal(revenue, ncfo):
    g = _f31_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    omvol = _std(om, 126)
    smoothcash = om / (1.0 + 8.0 * omvol)
    b = smoothcash * (1.0 + 2.0 * g) - 0.5 * omvol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion x cash-margin-expansion product (twin-margin acceleration)
def f31hg_f31_hypergrowth_signature_twinexp_252d_base_v140_signal(gp, revenue, ncfo):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(126)
    b = np.sign(dm) * np.sign(dom) * (dm.abs() * dom.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality composite: rule-of-40 times margin times reinvestment-discipline
def f31hg_f31_hypergrowth_signature_discipline_252d_base_v141_signal(revenue, ncfo, gp, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    disc = 1.0 / (1.0 + _std(ri, 252) * 30.0)
    b = (g + om) * m * disc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-revenue-growth x log-gross-profit-growth interaction (compounding twin growth)
def f31hg_f31_hypergrowth_signature_twingrow_252d_base_v142_signal(revenue, gp):
    rg = _f31_growth(revenue, 252)
    gg = _f31_growth(gp, 252)
    m = _f31_gross_margin(gp, revenue)
    b = rg * gg * np.sign(m) + 0.1 * (rg + gg) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity x margin-level, z-scored interaction (quality reinvestor)
def f31hg_f31_hypergrowth_signature_qualreinv_252d_base_v143_signal(rnd, revenue, gp):
    ri = _f31_rnd_intensity(rnd, revenue)
    m = _f31_gross_margin(gp, revenue)
    b = _z(ri, 252) * _z(m, 252) + 0.2 * _z(ri * m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 percentile minus reinvestment-intensity percentile (lean efficient growth)
def f31hg_f31_hypergrowth_signature_leangrow_252d_base_v144_signal(revenue, ncfo, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = _rank(g + om, 504) - _rank(ri, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-clean surprise: cash-margin surprise weighted by growth-margin level
def f31hg_f31_hypergrowth_signature_cleansurp_252d_base_v145_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    omsurp = om - om.ewm(span=126, min_periods=63).mean()
    b = omsurp * (1.0 + 3.0 * g * m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon growth consensus x margin (sign-agreement across 126/252/504 growth)
def f31hg_f31_hypergrowth_signature_consensus_252d_base_v146_signal(revenue, gp):
    g1 = _f31_growth(revenue, 126)
    g2 = _f31_growth(revenue, 252) * 0.5
    g3 = _f31_growth(revenue, 504) * 0.25
    consensus = (np.sign(g1) + np.sign(g2) + np.sign(g3))
    m = _f31_gross_margin(gp, revenue)
    mdev = m - _mean(m, 252)
    b = consensus * (m + 5.0 * mdev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin-improvement x reinvestment-intensity (cash funding rising R&D)
def f31hg_f31_hypergrowth_signature_cashfundsrnd_252d_base_v147_signal(ncfo, revenue, rnd):
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(126)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = dom * ri + 0.5 * np.sign(dom) * ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth score: weighted z of growth, margin, margin-expansion, cash, minus reinvest-vol
def f31hg_f31_hypergrowth_signature_durscore_252d_base_v148_signal(revenue, gp, ncfo, rnd):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = _z(g, 504) + 0.7 * _z(m, 504) + 0.7 * _z(dm, 504) + 0.5 * _z(om, 504) - 0.3 * _z(_std(ri, 126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin product x cash-conversion-rank (cash-validated hypergrowth)
def f31hg_f31_hypergrowth_signature_ccvalid_252d_base_v149_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    cc = ncfo / gp.replace(0, np.nan)
    b = g * m * (_rank(cc, 504) + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full integrated signature: rule-of-40-net-rank x margin-trajectory x growth-stability
def f31hg_f31_hypergrowth_signature_integfull_252d_base_v150_signal(revenue, ncfo, rnd, gp):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    gstab = _f31_growth(revenue, 63)
    stab = 1.0 / (1.0 + 10.0 * _std(gstab, 252))
    b = _rank(g + om - ri, 504) * (1.0 + 5.0 * dm) * stab
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31hg_f31_hypergrowth_signature_seqgrth_63d_base_v076_signal,
    f31hg_f31_hypergrowth_signature_seqgpgrth_63d_base_v077_signal,
    f31hg_f31_hypergrowth_signature_cagrmargin_504d_base_v078_signal,
    f31hg_f31_hypergrowth_signature_cagrrule40_504d_base_v079_signal,
    f31hg_f31_hypergrowth_signature_reaccel_252d_base_v080_signal,
    f31hg_f31_hypergrowth_signature_reinvaccel_252d_base_v081_signal,
    f31hg_f31_hypergrowth_signature_margslope_126d_base_v082_signal,
    f31hg_f31_hypergrowth_signature_rule40slope_126d_base_v083_signal,
    f31hg_f31_hypergrowth_signature_reinvslope_126d_base_v084_signal,
    f31hg_f31_hypergrowth_signature_gmspread_252v504_base_v085_signal,
    f31hg_f31_hypergrowth_signature_r40spread_252v504_base_v086_signal,
    f31hg_f31_hypergrowth_signature_consistgm_252d_base_v087_signal,
    f31hg_f31_hypergrowth_signature_r40consist_252d_base_v088_signal,
    f31hg_f31_hypergrowth_signature_gmhit_252d_base_v089_signal,
    f31hg_f31_hypergrowth_signature_reinvhit_252d_base_v090_signal,
    f31hg_f31_hypergrowth_signature_grthasym_252d_base_v091_signal,
    f31hg_f31_hypergrowth_signature_cashasym_252d_base_v092_signal,
    f31hg_f31_hypergrowth_signature_triadrank_252d_base_v093_signal,
    f31hg_f31_hypergrowth_signature_r40rank_252d_base_v094_signal,
    f31hg_f31_hypergrowth_signature_effreinv_252d_base_v095_signal,
    f31hg_f31_hypergrowth_signature_logscore_252d_base_v096_signal,
    f31hg_f31_hypergrowth_signature_gqmom_252d_base_v097_signal,
    f31hg_f31_hypergrowth_signature_reinvmom_252d_base_v098_signal,
    f31hg_f31_hypergrowth_signature_margdefend_252d_base_v099_signal,
    f31hg_f31_hypergrowth_signature_r40defend_252d_base_v100_signal,
    f31hg_f31_hypergrowth_signature_selfgrow_252d_base_v101_signal,
    f31hg_f31_hypergrowth_signature_fcfreinv_252d_base_v102_signal,
    f31hg_f31_hypergrowth_signature_qualfunded_252d_base_v103_signal,
    f31hg_f31_hypergrowth_signature_minall_252d_base_v104_signal,
    f31hg_f31_hypergrowth_signature_gmcross_252d_base_v105_signal,
    f31hg_f31_hypergrowth_signature_r40cross_252d_base_v106_signal,
    f31hg_f31_hypergrowth_signature_margconvex_252d_base_v107_signal,
    f31hg_f31_hypergrowth_signature_zreinv_252d_base_v108_signal,
    f31hg_f31_hypergrowth_signature_zcashmarg_252d_base_v109_signal,
    f31hg_f31_hypergrowth_signature_triplez_252d_base_v110_signal,
    f31hg_f31_hypergrowth_signature_rndprod_252d_base_v111_signal,
    f31hg_f31_hypergrowth_signature_salesprod_252d_base_v112_signal,
    f31hg_f31_hypergrowth_signature_gmrankema_252d_base_v113_signal,
    f31hg_f31_hypergrowth_signature_r40netrank_252d_base_v114_signal,
    f31hg_f31_hypergrowth_signature_comprove_252d_base_v115_signal,
    f31hg_f31_hypergrowth_signature_ccstab_252d_base_v116_signal,
    f31hg_f31_hypergrowth_signature_organic_252d_base_v117_signal,
    f31hg_f31_hypergrowth_signature_reinvimp_252d_base_v118_signal,
    f31hg_f31_hypergrowth_signature_growstreak_252d_base_v119_signal,
    f31hg_f31_hypergrowth_signature_cashstreak_252d_base_v120_signal,
    f31hg_f31_hypergrowth_signature_fundedaccel_252d_base_v121_signal,
    f31hg_f31_hypergrowth_signature_gpdollar_252d_base_v122_signal,
    f31hg_f31_hypergrowth_signature_r40margin_252d_base_v123_signal,
    f31hg_f31_hypergrowth_signature_marglev_252d_base_v124_signal,
    f31hg_f31_hypergrowth_signature_growperreinv_252d_base_v125_signal,
    f31hg_f31_hypergrowth_signature_twinmargin_252d_base_v126_signal,
    f31hg_f31_hypergrowth_signature_gmsharpe_252d_base_v127_signal,
    f31hg_f31_hypergrowth_signature_triadmin_252d_base_v128_signal,
    f31hg_f31_hypergrowth_signature_cashposgrow_252d_base_v129_signal,
    f31hg_f31_hypergrowth_signature_investmargin_252d_base_v130_signal,
    f31hg_f31_hypergrowth_signature_longdur_504d_base_v131_signal,
    f31hg_f31_hypergrowth_signature_gmyoy_252d_base_v132_signal,
    f31hg_f31_hypergrowth_signature_r40resil_252d_base_v133_signal,
    f31hg_f31_hypergrowth_signature_hmgrow_252d_base_v134_signal,
    f31hg_f31_hypergrowth_signature_cleanfunded_252d_base_v135_signal,
    f31hg_f31_hypergrowth_signature_cashefficient_252d_base_v136_signal,
    f31hg_f31_hypergrowth_signature_gpreinvrank_252d_base_v137_signal,
    f31hg_f31_hypergrowth_signature_triadslope_126d_base_v138_signal,
    f31hg_f31_hypergrowth_signature_smoothcash_252d_base_v139_signal,
    f31hg_f31_hypergrowth_signature_twinexp_252d_base_v140_signal,
    f31hg_f31_hypergrowth_signature_discipline_252d_base_v141_signal,
    f31hg_f31_hypergrowth_signature_twingrow_252d_base_v142_signal,
    f31hg_f31_hypergrowth_signature_qualreinv_252d_base_v143_signal,
    f31hg_f31_hypergrowth_signature_leangrow_252d_base_v144_signal,
    f31hg_f31_hypergrowth_signature_cleansurp_252d_base_v145_signal,
    f31hg_f31_hypergrowth_signature_consensus_252d_base_v146_signal,
    f31hg_f31_hypergrowth_signature_cashfundsrnd_252d_base_v147_signal,
    f31hg_f31_hypergrowth_signature_durscore_252d_base_v148_signal,
    f31hg_f31_hypergrowth_signature_ccvalid_252d_base_v149_signal,
    f31hg_f31_hypergrowth_signature_integfull_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_HYPERGROWTH_SIGNATURE_REGISTRY_076_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(101, n, base=1e9, drift=0.05, vol=0.06).rename("revenue")
    gp = (_fund(102, n, base=4e8, drift=0.045, vol=0.10)).rename("gp")
    rnd = (_fund(103, n, base=1.2e8, drift=0.035, vol=0.12)).rename("rnd")
    ncfo = _fund(104, n, base=2.5e8, drift=0.025, vol=0.16, allow_neg=True).rename("ncfo")
    grossmargin = _fund(105, n, base=0.45, drift=0.0, vol=0.05).clip(0.05, 0.95).rename("grossmargin")

    cols = {"revenue": revenue, "gp": gp, "rnd": rnd, "ncfo": ncfo,
            "grossmargin": grossmargin}

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

    print("OK f31_hypergrowth_signature_base_076_150_claude: %d features pass" % n_features)
