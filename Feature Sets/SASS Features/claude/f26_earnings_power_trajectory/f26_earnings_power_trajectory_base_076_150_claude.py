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


def _slope(s, w):
    x = np.arange(w, dtype=float)
    xm = x.mean()
    xd = x - xm
    denom = (xd ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((xd * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (earnings power trajectory) =====
def _f26_growth(s, w):
    return np.log(s.replace(0, np.nan).abs()) - np.log(s.shift(w).replace(0, np.nan).abs())


def _f26_roc(s, w):
    base = s.shift(w)
    return (s - base) / base.abs().replace(0, np.nan)


def _f26_stability(s, w):
    chg = s - s.shift(21)
    m = chg.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = chg.rolling(w, min_periods=max(2, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f26_posstreak(s, w):
    pos = (s > 0).astype(float)
    return pos.rolling(w, min_periods=max(1, w // 2)).mean()


def _f26_accel_level(s, w):
    g_now = _f26_growth(s, w)
    g_prev = _f26_growth(s.shift(w), w)
    return g_now - g_prev


def _f26_eps_spread(eps, epsdil):
    return (eps - epsdil) / eps.abs().replace(0, np.nan)


def _f26_eps_recon(netinc, shareswa):
    return netinc / shareswa.replace(0, np.nan)


# ============================================================

# eps semi-deviation of downside growth (downside earnings volatility)
def f26ep_f26_earnings_power_trajectory_epsdownvol_252d_base_v076_signal(eps):
    g = _f26_growth(eps, 63)
    down = g.where(g < 0, 0.0)
    b = (down ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps upside/downside growth asymmetry (skew of earnings momentum)
def f26ep_f26_earnings_power_trajectory_epsasym_252d_base_v077_signal(eps):
    g = _f26_growth(eps, 63)
    up = g.where(g > 0, 0.0).rolling(252, min_periods=126).mean()
    dn = (-g.where(g < 0, 0.0)).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income downside semi-deviation over two years
def f26ep_f26_earnings_power_trajectory_nidownvol_504d_base_v078_signal(netinc):
    g = _f26_growth(netinc, 63)
    down = g.where(g < 0, 0.0)
    b = (down ** 2).rolling(504, min_periods=252).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth breadth: fraction of recent quarters with growth above its own median
def f26ep_f26_earnings_power_trajectory_epsbreadth_252d_base_v079_signal(eps):
    g = _f26_growth(eps, 63)
    med = g.rolling(252, min_periods=126).median()
    above = (g > med).astype(float)
    b = above.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic eps level ratio (structural dilution factor)
def f26ep_f26_earnings_power_trajectory_dilratio_base_v080_signal(eps, epsdil):
    b = epsdil / eps.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution ratio z-scored vs its own two-year history (de-trended dilution)
def f26ep_f26_earnings_power_trajectory_dilratioz_504d_base_v081_signal(eps, epsdil):
    r = epsdil / eps.replace(0, np.nan)
    b = _z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-spread slope over a year (dilution worsening trend)
def f26ep_f26_earnings_power_trajectory_dilsprslope_252d_base_v082_signal(eps, epsdil):
    sp = _f26_eps_spread(eps, epsdil)
    sl = _slope(sp, 252)
    b = sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings power momentum: eps growth minus its own one-year-lagged level smoothed
def f26ep_f26_earnings_power_trajectory_epsgmom_252d_base_v083_signal(eps):
    g = _f26_growth(eps, 63)
    b = g.ewm(span=42, min_periods=21).mean() - g.shift(126).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income momentum interacted with stability sign (quality-filtered momentum)
def f26ep_f26_earnings_power_trajectory_nigqual_252d_base_v084_signal(netinc):
    g = _f26_growth(netinc, 252)
    stab = _f26_stability(netinc, 252)
    b = g * (0.5 + 0.5 * np.tanh(stab))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common-earnings growth minus total-earnings growth (preferred-burden drift)
def f26ep_f26_earnings_power_trajectory_cmngap_252d_base_v085_signal(netinccmn, netinc):
    gc = _f26_growth(netinccmn, 252)
    gn = _f26_growth(netinc, 252)
    b = gc - gn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings power range width: eps high-low spread over a year normalized by mean (amplitude)
def f26ep_f26_earnings_power_trajectory_epsampl_252d_base_v086_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    m = eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = (hi - lo) / m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income amplitude over two years (profit-scale swing)
def f26ep_f26_earnings_power_trajectory_niampl_504d_base_v087_signal(netinc):
    hi = _rmax(netinc, 504)
    lo = _rmin(netinc, 504)
    m = netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    b = (hi - lo) / m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps acceleration over a quarter, smoothed (short-cycle inflection)
def f26ep_f26_earnings_power_trajectory_epsaccsm_63d_base_v088_signal(eps):
    a = _f26_accel_level(eps, 63)
    b = a.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income acceleration over a quarter ranked vs history
def f26ep_f26_earnings_power_trajectory_niaccrank_63d_base_v089_signal(netinc):
    a = _f26_accel_level(netinc, 63)
    b = a.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps trend convexity: 2nd difference of eps level scaled (curvature of earnings path)
def f26ep_f26_earnings_power_trajectory_epsconvex_126d_base_v090_signal(eps):
    d1 = eps - eps.shift(63)
    d2 = d1 - d1.shift(63)
    scale = eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = d2 / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income convexity over two years
def f26ep_f26_earnings_power_trajectory_niconvex_504d_base_v091_signal(netinc):
    d1 = netinc - netinc.shift(126)
    d2 = d1 - d1.shift(126)
    scale = netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    b = d2 / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps growth percentile-ranked vs own history
def f26ep_f26_earnings_power_trajectory_dilgrank_252d_base_v092_signal(epsdil):
    g = _f26_growth(epsdil, 252)
    b = g.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps inflection vs trailing mean
def f26ep_f26_earnings_power_trajectory_dilinflect_252d_base_v093_signal(epsdil):
    m = _mean(epsdil, 252)
    b = (epsdil - m) / epsdil.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings power consistency: share of last year where eps and netinc both grew (joint breadth)
def f26ep_f26_earnings_power_trajectory_jointgrow_252d_base_v094_signal(eps, netinc):
    eu = (eps - eps.shift(63) > 0)
    nu = (netinc - netinc.shift(63) > 0)
    both = (eu & nu).astype(float)
    b = both.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth dispersion across windows (term-structure of growth)
def f26ep_f26_earnings_power_trajectory_epsgterm_base_v095_signal(eps):
    g63 = _f26_growth(eps, 63)
    g126 = _f26_growth(eps, 126)
    g252 = _f26_growth(eps, 252)
    b = pd.concat([g63, g126, g252], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth term-structure slope (short minus long growth)
def f26ep_f26_earnings_power_trajectory_nigterm_base_v096_signal(netinc):
    gshort = _f26_growth(netinc, 63)
    glong = _f26_growth(netinc, 252)
    b = gshort - glong / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps surprise proxy: eps vs its EWMA-extrapolated expectation (earnings beat level)
def f26ep_f26_earnings_power_trajectory_epssurp_126d_base_v097_signal(eps):
    expect = eps.shift(63).ewm(span=63, min_periods=21).mean()
    b = (eps - expect) / eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income surprise proxy vs trailing expectation, ranked
def f26ep_f26_earnings_power_trajectory_nisurp_252d_base_v098_signal(netinc):
    expect = netinc.shift(63).ewm(span=63, min_periods=21).mean()
    surp = (netinc - expect) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = surp.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth autocorrelation (momentum persistence of earnings trajectory)
def f26ep_f26_earnings_power_trajectory_epsgautoc_252d_base_v099_signal(eps):
    g = _f26_growth(eps, 63)
    g_lag = g.shift(63)
    cov = (g - g.rolling(252, min_periods=126).mean()) * (g_lag - g_lag.rolling(252, min_periods=126).mean())
    num = cov.rolling(252, min_periods=126).mean()
    den = g.rolling(252, min_periods=126).std() * g_lag.rolling(252, min_periods=126).std()
    b = num / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic spread interacted with eps growth (dilution-adjusted momentum)
def f26ep_f26_earnings_power_trajectory_dilsprxg_252d_base_v100_signal(eps, epsdil):
    sp = _f26_eps_spread(eps, epsdil)
    g = _f26_growth(eps, 252)
    b = g - 2.0 * sp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings power level relative to its five-year-equivalent peak (long drawdown, eps)
def f26ep_f26_earnings_power_trajectory_epsdd_504d_base_v101_signal(eps):
    pk = _rmax(eps, 504)
    b = eps / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income recovery off two-year trough scaled (long earnings rebound)
def f26ep_f26_earnings_power_trajectory_nirecov_504d_base_v102_signal(netinc):
    tr = _rmin(netinc, 504)
    b = (netinc - tr) / netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common net income drawdown from trailing peak
def f26ep_f26_earnings_power_trajectory_ncmndd_252d_base_v103_signal(netinccmn):
    pk = _rmax(netinccmn, 252)
    b = netinccmn / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps quarter growth sign-consistency (run-quality of recent earnings)
def f26ep_f26_earnings_power_trajectory_epssignrun_126d_base_v104_signal(eps):
    g = _f26_growth(eps, 21)
    sgn = np.sign(g)
    b = sgn.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth-acceleration interacted with positive streak (durable inflection)
def f26ep_f26_earnings_power_trajectory_niaccxstreak_252d_base_v105_signal(netinc):
    a = _f26_accel_level(netinc, 252)
    st = _f26_posstreak(netinc, 252)
    b = a * st
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth minus diluted-eps growth, ranked (dilution-trend regime, basic vs diluted)
def f26ep_f26_earnings_power_trajectory_basicvsdil_252d_base_v106_signal(eps, epsdil):
    gb = _f26_growth(eps, 252)
    gd = _f26_growth(epsdil, 252)
    spread = gb - gd
    b = spread.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income trend-quality: slope-to-dispersion over two years
def f26ep_f26_earnings_power_trajectory_nitrendq_504d_base_v107_signal(netinc):
    sl = _slope(netinc, 504)
    sd = (netinc - netinc.shift(21)).rolling(504, min_periods=252).std()
    b = sl / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps level vs its 252d range midpoint, smoothed (earnings positioning)
def f26ep_f26_earnings_power_trajectory_epsmidpos_252d_base_v108_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    mid = (hi + lo) / 2.0
    raw = (eps - mid) / (hi - lo).replace(0, np.nan)
    b = raw.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reconstructed per-share earnings growth minus reported eps growth (accrual-share residual)
def f26ep_f26_earnings_power_trajectory_reconresid_252d_base_v109_signal(eps, netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    gr = _f26_growth(re, 252)
    ge = _f26_growth(eps, 252)
    b = gr - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reconstructed per-share earnings displacement from its own EWMA (per-share gap, mean-reverting)
def f26ep_f26_earnings_power_trajectory_reconrank_504d_base_v110_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    ewm = re.ewm(span=252, min_periods=126).mean()
    b = (re - ewm) / re.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth volatility-of-volatility (instability of earnings instability)
def f26ep_f26_earnings_power_trajectory_epsvov_252d_base_v111_signal(eps):
    g = _f26_growth(eps, 21)
    vol = g.rolling(63, min_periods=21).std()
    b = vol.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth tanh momentum minus lagged (bounded earnings acceleration)
def f26ep_f26_earnings_power_trajectory_nigtanhacc_252d_base_v112_signal(netinc):
    g = _f26_growth(netinc, 252)
    t = np.tanh(2.0 * g)
    b = t - t.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps positive-streak interacted with growth-sign breadth (consistency composite)
def f26ep_f26_earnings_power_trajectory_epsconsist_252d_base_v113_signal(eps):
    st = _f26_posstreak(eps, 252)
    g = _f26_growth(eps, 21)
    breadth = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    b = st * breadth - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common net income growth minus its lagged value (common-earnings acceleration)
def f26ep_f26_earnings_power_trajectory_ncmnacc_252d_base_v114_signal(netinccmn):
    b = _f26_accel_level(netinccmn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth vs net income growth correlation gap (per-share vs total divergence z)
def f26ep_f26_earnings_power_trajectory_epsnidiv_252d_base_v115_signal(eps, netinc):
    ge = _f26_growth(eps, 252)
    gn = _f26_growth(netinc, 252)
    b = _z(ge - gn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income half-year vs year growth gap (deceleration spread)
def f26ep_f26_earnings_power_trajectory_nidecel_base_v116_signal(netinc):
    g126 = _f26_growth(netinc, 126)
    g252 = _f26_growth(netinc, 252)
    b = 2.0 * g126 - g252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps level smoothed slope of log (compounded earnings-power growth rate)
def f26ep_f26_earnings_power_trajectory_epslogslope_252d_base_v117_signal(eps):
    le = np.log(eps.replace(0, np.nan).abs())
    b = _slope(le, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income log slope over two years (compounded profit growth rate)
def f26ep_f26_earnings_power_trajectory_nilogslope_504d_base_v118_signal(netinc):
    ln = np.log(netinc.replace(0, np.nan).abs())
    b = _slope(ln, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps drawdown over two years (diluted earnings-power decline)
def f26ep_f26_earnings_power_trajectory_dildd_504d_base_v119_signal(epsdil):
    pk = _rmax(epsdil, 504)
    b = epsdil / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth above zero-line persistence weighted by magnitude (sustained-growth depth)
def f26ep_f26_earnings_power_trajectory_epsgdepth_252d_base_v120_signal(eps):
    g = _f26_growth(eps, 63)
    pos_mag = g.clip(lower=0)
    b = pos_mag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income loss-magnitude persistence (depth of negative-earnings episodes)
def f26ep_f26_earnings_power_trajectory_nilossdepth_252d_base_v121_signal(netinc):
    scale = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    loss = (-netinc / scale).clip(lower=0)
    b = loss.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps vs diluted eps growth correlation-free spread, smoothed (clean dilution drift)
def f26ep_f26_earnings_power_trajectory_dildrift_252d_base_v122_signal(eps, epsdil):
    ratio = (eps - epsdil) / (eps.abs() + epsdil.abs()).replace(0, np.nan)
    b = ratio - ratio.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count-adjusted earnings power: netinc growth divided by share growth (efficiency of issuance)
def f26ep_f26_earnings_power_trajectory_issueeff_252d_base_v123_signal(netinc, shareswa):
    gn = _f26_growth(netinc, 252)
    gs = _f26_growth(shareswa, 252)
    b = gn - 3.0 * gs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth EWMA crossover (fast vs slow earnings momentum)
def f26ep_f26_earnings_power_trajectory_epsgcross_base_v124_signal(eps):
    g = _f26_growth(eps, 63)
    fast = g.ewm(span=21, min_periods=10).mean()
    slow = g.ewm(span=126, min_periods=42).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth EWMA crossover
def f26ep_f26_earnings_power_trajectory_nigcross_base_v125_signal(netinc):
    g = _f26_growth(netinc, 63)
    fast = g.ewm(span=21, min_periods=10).mean()
    slow = g.ewm(span=189, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps level z-scored over a quarter (short-horizon earnings extremity)
def f26ep_f26_earnings_power_trajectory_epsz_63d_base_v126_signal(eps):
    b = _z(eps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income level z-scored over a quarter
def f26ep_f26_earnings_power_trajectory_niz_63d_base_v127_signal(netinc):
    b = _z(netinc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps acceleration sign-and-magnitude (asymmetric inflection emphasis)
def f26ep_f26_earnings_power_trajectory_epsaccsignmag_252d_base_v128_signal(eps):
    a = _f26_accel_level(eps, 252)
    b = np.sign(a) * (a.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income inflection year-over-year change (turn relative to a year ago)
def f26ep_f26_earnings_power_trajectory_niinflyoy_252d_base_v129_signal(netinc):
    m = _mean(netinc, 126)
    infl = (netinc - m) / netinc.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = infl - infl.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-power Rule-of-quality: eps growth plus positive-streak premium
def f26ep_f26_earnings_power_trajectory_epsrule_252d_base_v130_signal(eps):
    g = _f26_growth(eps, 252)
    st = _f26_posstreak(eps, 252) - 0.5
    b = np.tanh(2.0 * g) + 0.5 * st
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps acceleration ranked vs history (relative diluted inflection)
def f26ep_f26_earnings_power_trajectory_dilaccrank_252d_base_v131_signal(epsdil):
    a = _f26_accel_level(epsdil, 252)
    b = a.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common net income stability ranked vs total net income stability (relative quality)
def f26ep_f26_earnings_power_trajectory_relstab_252d_base_v132_signal(netinccmn, netinc):
    sc = _f26_stability(netinccmn, 252)
    sn = _f26_stability(netinc, 252)
    b = np.tanh(sc) - np.tanh(sn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth interacted with low-dispersion premium (high-quality growth)
def f26ep_f26_earnings_power_trajectory_epsqualgrow_252d_base_v133_signal(eps):
    g = _f26_growth(eps, 252)
    disp = (eps - eps.shift(63)).rolling(252, min_periods=126).std()
    norm_disp = disp / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = g / (1.0 + norm_disp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income momentum reversal: current level vs its EWMA expectation, ranked (overshoot gap)
def f26ep_f26_earnings_power_trajectory_nigrev_252d_base_v134_signal(netinc):
    ewm = netinc.ewm(span=189, min_periods=63).mean()
    gap = (netinc - ewm) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = gap.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps level coefficient of variation over two years (long earnings volatility)
def f26ep_f26_earnings_power_trajectory_epscv_504d_base_v135_signal(eps):
    sd = _std(eps, 504)
    m = eps.abs().rolling(504, min_periods=252).mean()
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic spread change ranked (dilution regime shift)
def f26ep_f26_earnings_power_trajectory_dilsprchgrank_252d_base_v136_signal(eps, epsdil):
    sp = _f26_eps_spread(eps, epsdil)
    chg = sp - sp.shift(126)
    b = chg.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income positive-streak depth: positivity weighted by level magnitude
def f26ep_f26_earnings_power_trajectory_nistreakdepth_252d_base_v137_signal(netinc):
    scale = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    pos_mag = (netinc / scale).clip(lower=0)
    b = pos_mag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth vs share growth interaction (per-share-amplified earnings power)
def f26ep_f26_earnings_power_trajectory_epsshareint_252d_base_v138_signal(eps, shareswa):
    ge = _f26_growth(eps, 252)
    sl = _slope(shareswa, 252) / shareswa.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = ge * np.sign(-sl) * (1.0 + sl.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income trend acceleration: slope now vs slope a quarter ago
def f26ep_f26_earnings_power_trajectory_nislopeacc_252d_base_v139_signal(netinc):
    sl = _slope(netinc, 252) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps trend acceleration: slope now vs slope a quarter ago
def f26ep_f26_earnings_power_trajectory_epsslopeacc_252d_base_v140_signal(eps):
    sl = _slope(eps, 252) / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings power breadth across all four earnings measures (joint up-fraction)
def f26ep_f26_earnings_power_trajectory_quadbreadth_252d_base_v141_signal(netinc, netinccmn, eps, epsdil):
    u1 = (netinc - netinc.shift(63) > 0).astype(float)
    u2 = (netinccmn - netinccmn.shift(63) > 0).astype(float)
    u3 = (eps - eps.shift(63) > 0).astype(float)
    u4 = (epsdil - epsdil.shift(63) > 0).astype(float)
    score = (u1 + u2 + u3 + u4) / 4.0
    b = score.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps inflection minus net income inflection (per-share vs total turn divergence)
def f26ep_f26_earnings_power_trajectory_inflectdiv_252d_base_v142_signal(eps, netinc):
    me = _mean(eps, 252)
    ie = (eps - me) / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    mn = _mean(netinc, 252)
    inc = (netinc - mn) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = ie - inc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth scaled by inverse downside-vol (downside-risk-adjusted growth)
def f26ep_f26_earnings_power_trajectory_nigdownadj_252d_base_v143_signal(netinc):
    g = _f26_growth(netinc, 252)
    gq = _f26_growth(netinc, 63)
    down = gq.where(gq < 0, 0.0)
    dvol = (down ** 2).rolling(252, min_periods=126).mean() ** 0.5
    b = g / (0.05 + dvol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth diffusion: cumulative sign of monthly growth over the year (trend diffusion)
def f26ep_f26_earnings_power_trajectory_epsdiffusion_252d_base_v144_signal(eps):
    g = _f26_growth(eps, 21)
    sgn = np.sign(g)
    b = sgn.rolling(252, min_periods=126).sum() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps log slope over a year (diluted compounded growth rate)
def f26ep_f26_earnings_power_trajectory_dillogslope_252d_base_v145_signal(epsdil):
    ld = np.log(epsdil.replace(0, np.nan).abs())
    b = _slope(ld, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common-earnings level z minus total-earnings level z (relative scale divergence)
def f26ep_f26_earnings_power_trajectory_cmnzdiv_252d_base_v146_signal(netinccmn, netinc):
    zc = _z(netinccmn, 252)
    zn = _z(netinc, 252)
    b = zc - zn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps acceleration smoothed minus its own slow trend (clean inflection signal)
def f26ep_f26_earnings_power_trajectory_epsacctrend_252d_base_v147_signal(eps):
    a = _f26_accel_level(eps, 252)
    b = a.ewm(span=21, min_periods=10).mean() - a.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income recovery-vs-drawdown balance (earnings V-shape over a year)
def f26ep_f26_earnings_power_trajectory_nivshape_252d_base_v148_signal(netinc):
    pk = _rmax(netinc, 252)
    tr = _rmin(netinc, 252)
    scale = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    rec = (netinc - tr) / scale
    dd = (pk - netinc) / scale
    b = (rec - dd) / (rec + dd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth strength net of dilution-spread, tanh-bounded (clean per-share momentum)
def f26ep_f26_earnings_power_trajectory_epscleanmom_252d_base_v149_signal(eps, epsdil):
    gd = _f26_growth(epsdil, 252)
    sp = _f26_eps_spread(eps, epsdil)
    b = np.tanh(2.0 * gd) - np.tanh(4.0 * sp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full earnings-power composite: per-share growth x streak x trend-quality sign
def f26ep_f26_earnings_power_trajectory_epfullcomp_252d_base_v150_signal(eps, netinc):
    g = _f26_growth(eps, 252)
    st = _f26_posstreak(netinc, 252) - 0.5
    sl = _slope(netinc, 252) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = np.tanh(2.0 * g) * (1.0 + st) * np.sign(sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ep_f26_earnings_power_trajectory_epsdownvol_252d_base_v076_signal,
    f26ep_f26_earnings_power_trajectory_epsasym_252d_base_v077_signal,
    f26ep_f26_earnings_power_trajectory_nidownvol_504d_base_v078_signal,
    f26ep_f26_earnings_power_trajectory_epsbreadth_252d_base_v079_signal,
    f26ep_f26_earnings_power_trajectory_dilratio_base_v080_signal,
    f26ep_f26_earnings_power_trajectory_dilratioz_504d_base_v081_signal,
    f26ep_f26_earnings_power_trajectory_dilsprslope_252d_base_v082_signal,
    f26ep_f26_earnings_power_trajectory_epsgmom_252d_base_v083_signal,
    f26ep_f26_earnings_power_trajectory_nigqual_252d_base_v084_signal,
    f26ep_f26_earnings_power_trajectory_cmngap_252d_base_v085_signal,
    f26ep_f26_earnings_power_trajectory_epsampl_252d_base_v086_signal,
    f26ep_f26_earnings_power_trajectory_niampl_504d_base_v087_signal,
    f26ep_f26_earnings_power_trajectory_epsaccsm_63d_base_v088_signal,
    f26ep_f26_earnings_power_trajectory_niaccrank_63d_base_v089_signal,
    f26ep_f26_earnings_power_trajectory_epsconvex_126d_base_v090_signal,
    f26ep_f26_earnings_power_trajectory_niconvex_504d_base_v091_signal,
    f26ep_f26_earnings_power_trajectory_dilgrank_252d_base_v092_signal,
    f26ep_f26_earnings_power_trajectory_dilinflect_252d_base_v093_signal,
    f26ep_f26_earnings_power_trajectory_jointgrow_252d_base_v094_signal,
    f26ep_f26_earnings_power_trajectory_epsgterm_base_v095_signal,
    f26ep_f26_earnings_power_trajectory_nigterm_base_v096_signal,
    f26ep_f26_earnings_power_trajectory_epssurp_126d_base_v097_signal,
    f26ep_f26_earnings_power_trajectory_nisurp_252d_base_v098_signal,
    f26ep_f26_earnings_power_trajectory_epsgautoc_252d_base_v099_signal,
    f26ep_f26_earnings_power_trajectory_dilsprxg_252d_base_v100_signal,
    f26ep_f26_earnings_power_trajectory_epsdd_504d_base_v101_signal,
    f26ep_f26_earnings_power_trajectory_nirecov_504d_base_v102_signal,
    f26ep_f26_earnings_power_trajectory_ncmndd_252d_base_v103_signal,
    f26ep_f26_earnings_power_trajectory_epssignrun_126d_base_v104_signal,
    f26ep_f26_earnings_power_trajectory_niaccxstreak_252d_base_v105_signal,
    f26ep_f26_earnings_power_trajectory_basicvsdil_252d_base_v106_signal,
    f26ep_f26_earnings_power_trajectory_nitrendq_504d_base_v107_signal,
    f26ep_f26_earnings_power_trajectory_epsmidpos_252d_base_v108_signal,
    f26ep_f26_earnings_power_trajectory_reconresid_252d_base_v109_signal,
    f26ep_f26_earnings_power_trajectory_reconrank_504d_base_v110_signal,
    f26ep_f26_earnings_power_trajectory_epsvov_252d_base_v111_signal,
    f26ep_f26_earnings_power_trajectory_nigtanhacc_252d_base_v112_signal,
    f26ep_f26_earnings_power_trajectory_epsconsist_252d_base_v113_signal,
    f26ep_f26_earnings_power_trajectory_ncmnacc_252d_base_v114_signal,
    f26ep_f26_earnings_power_trajectory_epsnidiv_252d_base_v115_signal,
    f26ep_f26_earnings_power_trajectory_nidecel_base_v116_signal,
    f26ep_f26_earnings_power_trajectory_epslogslope_252d_base_v117_signal,
    f26ep_f26_earnings_power_trajectory_nilogslope_504d_base_v118_signal,
    f26ep_f26_earnings_power_trajectory_dildd_504d_base_v119_signal,
    f26ep_f26_earnings_power_trajectory_epsgdepth_252d_base_v120_signal,
    f26ep_f26_earnings_power_trajectory_nilossdepth_252d_base_v121_signal,
    f26ep_f26_earnings_power_trajectory_dildrift_252d_base_v122_signal,
    f26ep_f26_earnings_power_trajectory_issueeff_252d_base_v123_signal,
    f26ep_f26_earnings_power_trajectory_epsgcross_base_v124_signal,
    f26ep_f26_earnings_power_trajectory_nigcross_base_v125_signal,
    f26ep_f26_earnings_power_trajectory_epsz_63d_base_v126_signal,
    f26ep_f26_earnings_power_trajectory_niz_63d_base_v127_signal,
    f26ep_f26_earnings_power_trajectory_epsaccsignmag_252d_base_v128_signal,
    f26ep_f26_earnings_power_trajectory_niinflyoy_252d_base_v129_signal,
    f26ep_f26_earnings_power_trajectory_epsrule_252d_base_v130_signal,
    f26ep_f26_earnings_power_trajectory_dilaccrank_252d_base_v131_signal,
    f26ep_f26_earnings_power_trajectory_relstab_252d_base_v132_signal,
    f26ep_f26_earnings_power_trajectory_epsqualgrow_252d_base_v133_signal,
    f26ep_f26_earnings_power_trajectory_nigrev_252d_base_v134_signal,
    f26ep_f26_earnings_power_trajectory_epscv_504d_base_v135_signal,
    f26ep_f26_earnings_power_trajectory_dilsprchgrank_252d_base_v136_signal,
    f26ep_f26_earnings_power_trajectory_nistreakdepth_252d_base_v137_signal,
    f26ep_f26_earnings_power_trajectory_epsshareint_252d_base_v138_signal,
    f26ep_f26_earnings_power_trajectory_nislopeacc_252d_base_v139_signal,
    f26ep_f26_earnings_power_trajectory_epsslopeacc_252d_base_v140_signal,
    f26ep_f26_earnings_power_trajectory_quadbreadth_252d_base_v141_signal,
    f26ep_f26_earnings_power_trajectory_inflectdiv_252d_base_v142_signal,
    f26ep_f26_earnings_power_trajectory_nigdownadj_252d_base_v143_signal,
    f26ep_f26_earnings_power_trajectory_epsdiffusion_252d_base_v144_signal,
    f26ep_f26_earnings_power_trajectory_dillogslope_252d_base_v145_signal,
    f26ep_f26_earnings_power_trajectory_cmnzdiv_252d_base_v146_signal,
    f26ep_f26_earnings_power_trajectory_epsacctrend_252d_base_v147_signal,
    f26ep_f26_earnings_power_trajectory_nivshape_252d_base_v148_signal,
    f26ep_f26_earnings_power_trajectory_epscleanmom_252d_base_v149_signal,
    f26ep_f26_earnings_power_trajectory_epfullcomp_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_EARNINGS_POWER_TRAJECTORY_REGISTRY_076_150 = REGISTRY


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
    netinc = _fund(7, base=5e8, drift=0.0, vol=0.5, allow_neg=True, n=n).rename("netinc")
    netinccmn = _fund(8, base=4.6e8, drift=0.0, vol=0.5, allow_neg=True, n=n).rename("netinccmn")
    eps = _fund(3, base=3.0, drift=0.0, vol=0.5, allow_neg=True, n=n).rename("eps")
    epsdil = _fund(5, base=2.85, drift=0.0, vol=0.5, allow_neg=True, n=n).rename("epsdil")
    shareswa = _fund(11, base=2.0e8, drift=0.01, vol=0.08, allow_neg=False, n=n).rename("shareswa")

    cols = {"netinc": netinc, "netinccmn": netinccmn, "eps": eps,
            "epsdil": epsdil, "shareswa": shareswa}

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

    print("OK f26_earnings_power_trajectory_base_076_150_claude: %d features pass" % n_features)
