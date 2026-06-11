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
    # OLS slope of s vs time over window w, per-step
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
    # log growth of an earnings-power level over window w
    return np.log(s.replace(0, np.nan).abs()) - np.log(s.shift(w).replace(0, np.nan).abs())


def _f26_roc(s, w):
    # simple rate of change over window w (handles sign)
    base = s.shift(w)
    return (s - base) / base.abs().replace(0, np.nan)


def _f26_stability(s, w):
    # inverse coefficient of variation of period-over-period changes (stability)
    chg = s - s.shift(21)
    m = chg.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = chg.rolling(w, min_periods=max(2, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f26_posstreak(s, w):
    # rolling fraction of window where the level is positive (earnings positive streak)
    pos = (s > 0).astype(float)
    return pos.rolling(w, min_periods=max(1, w // 2)).mean()


def _f26_accel_level(s, w):
    # acceleration-as-level: recent growth minus prior growth, as a standing level
    g_now = _f26_growth(s, w)
    g_prev = _f26_growth(s.shift(w), w)
    return g_now - g_prev


def _f26_eps_spread(eps, epsdil):
    # diluted-vs-basic dilution drag (basic minus diluted)
    return (eps - epsdil) / eps.abs().replace(0, np.nan)


def _f26_eps_recon(netinc, shareswa):
    # reconstructed eps from net income over weighted avg shares
    return netinc / shareswa.replace(0, np.nan)


# ============================================================
# --- EPS GROWTH block ---

# eps log growth over a quarter (sequential earnings-power growth)
def f26ep_f26_earnings_power_trajectory_epsg_63d_base_v001_signal(eps):
    b = _f26_growth(eps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps log growth over a year (annual earnings-power growth)
def f26ep_f26_earnings_power_trajectory_epsg_252d_base_v002_signal(eps):
    b = _f26_growth(eps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps log growth over two years (durable growth)
def f26ep_f26_earnings_power_trajectory_epsg_504d_base_v003_signal(eps):
    b = _f26_growth(eps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual eps growth, z-scored vs its own 252d history (de-trended growth)
def f26ep_f26_earnings_power_trajectory_epsgz_252d_base_v004_signal(eps):
    g = _f26_growth(eps, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual eps growth, percentile-ranked vs its own 504d history
def f26ep_f26_earnings_power_trajectory_epsgrank_252d_base_v005_signal(eps):
    g = _f26_growth(eps, 252)
    b = g.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- NET INCOME GROWTH block ---

# net income log growth over a year (earnings power scale-up)
def f26ep_f26_earnings_power_trajectory_nig_252d_base_v006_signal(netinc):
    b = _f26_growth(netinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income log growth over a quarter
def f26ep_f26_earnings_power_trajectory_nig_63d_base_v007_signal(netinc):
    b = _f26_growth(netinc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth over two years, smoothed (durable profit growth)
def f26ep_f26_earnings_power_trajectory_nig_504d_base_v008_signal(netinc):
    g = _f26_growth(netinc, 504)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common net income growth over a year (common-shareholder earnings power)
def f26ep_f26_earnings_power_trajectory_ncmng_252d_base_v009_signal(netinccmn):
    b = _f26_growth(netinccmn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common net income growth percentile-ranked vs own history
def f26ep_f26_earnings_power_trajectory_ncmngrank_252d_base_v010_signal(netinccmn):
    g = _f26_growth(netinccmn, 252)
    b = g.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EARNINGS STABILITY block ---

# stability of net-income changes over a year (signal/noise of profit path)
def f26ep_f26_earnings_power_trajectory_nistab_252d_base_v011_signal(netinc):
    b = _f26_stability(netinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stability of eps changes over two years
def f26ep_f26_earnings_power_trajectory_epsstab_504d_base_v012_signal(eps):
    b = _f26_stability(eps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps dispersion: std of quarterly eps changes normalized by eps level (volatility of EPS)
def f26ep_f26_earnings_power_trajectory_epsdisp_252d_base_v013_signal(eps):
    chg = eps - eps.shift(63)
    sd = chg.rolling(252, min_periods=126).std()
    b = sd / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income dispersion (inverse stability), ranked vs own history
def f26ep_f26_earnings_power_trajectory_nidisp_252d_base_v014_signal(netinc):
    chg = netinc - netinc.shift(63)
    sd = chg.rolling(252, min_periods=126).std()
    norm = sd / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = norm.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EPS ACCELERATION-AS-LEVEL block ---

# eps acceleration as a standing level (quarter growth now vs prior quarter)
def f26ep_f26_earnings_power_trajectory_epsacc_63d_base_v015_signal(eps):
    b = _f26_accel_level(eps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps acceleration over a year
def f26ep_f26_earnings_power_trajectory_epsacc_252d_base_v016_signal(eps):
    b = _f26_accel_level(eps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income acceleration as a standing level (year over year)
def f26ep_f26_earnings_power_trajectory_niacc_252d_base_v017_signal(netinc):
    b = _f26_accel_level(netinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps acceleration z-scored vs own history (de-trended inflection)
def f26ep_f26_earnings_power_trajectory_epsaccz_252d_base_v018_signal(eps):
    a = _f26_accel_level(eps, 252)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DILUTED-VS-BASIC SPREAD block ---

# basic-minus-diluted eps spread (dilution drag level)
def f26ep_f26_earnings_power_trajectory_epsspr_base_v019_signal(eps, epsdil):
    b = _f26_eps_spread(eps, epsdil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drag smoothed over a quarter (persistent overhang)
def f26ep_f26_earnings_power_trajectory_epssprsm_63d_base_v020_signal(eps, epsdil):
    sp = _f26_eps_spread(eps, epsdil)
    b = sp.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in dilution drag over a year (worsening/easing dilution)
def f26ep_f26_earnings_power_trajectory_epssprchg_252d_base_v021_signal(eps, epsdil):
    sp = _f26_eps_spread(eps, epsdil)
    b = sp - sp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-eps growth minus basic-eps growth (dilution-adjusted growth gap)
def f26ep_f26_earnings_power_trajectory_dilgrgap_252d_base_v022_signal(eps, epsdil):
    gb = _f26_growth(eps, 252)
    gd = _f26_growth(epsdil, 252)
    b = gd - gb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EARNINGS POSITIVE STREAK block ---

# fraction of the last year with positive net income (earnings positive streak)
def f26ep_f26_earnings_power_trajectory_nistreak_252d_base_v023_signal(netinc):
    b = _f26_posstreak(netinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last two years with positive eps
def f26ep_f26_earnings_power_trajectory_epsstreak_504d_base_v024_signal(eps):
    b = _f26_posstreak(eps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-earnings persistence quality: streak fraction weighted by recency within the year
def f26ep_f26_earnings_power_trajectory_nirun_252d_base_v025_signal(netinc):
    pos = (netinc > 0).astype(float)
    w = 252
    wt = np.linspace(0.5, 1.5, w)
    wt = wt / wt.sum()

    def _wfrac(a):
        return float(np.dot(a, wt))

    b = pos.rolling(w, min_periods=w).apply(_wfrac, raw=True)
    # contrast recency-weighted positivity against flat positivity -> emphasis on RECENT turn
    flat = pos.rolling(w, min_periods=w).mean()
    b = (b - flat) + 0.6 * np.tanh(2.0 * netinc / netinc.abs().rolling(63, min_periods=21).mean().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EARNINGS INFLECTION block ---

# earnings inflection: net income now vs its trailing mean, sign-scaled (turn off low base)
def f26ep_f26_earnings_power_trajectory_niinflect_252d_base_v026_signal(netinc):
    m = _mean(netinc, 252)
    b = (netinc - m) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps inflection vs trailing half-year mean (recent earnings turn)
def f26ep_f26_earnings_power_trajectory_epsinflect_126d_base_v027_signal(eps):
    m = _mean(eps, 126)
    b = (eps - m) / eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# loss-narrowing slope: OLS slope of net income when below zero (improving losses)
def f26ep_f26_earnings_power_trajectory_lossnar_252d_base_v028_signal(netinc):
    sl = _slope(netinc, 252)
    scale = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = sl / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RECONSTRUCTED EPS / SHARES interaction block ---

# reconstructed eps (netinc / shareswa) growth z-scored vs its own history (de-trended per-share)
def f26ep_f26_earnings_power_trajectory_reconepsg_252d_base_v029_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    g = _f26_growth(re, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reported eps vs reconstructed eps gap (accrual/share-base reconciliation)
def f26ep_f26_earnings_power_trajectory_epsrecongap_base_v030_signal(eps, netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    b = (eps - re) / eps.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share earnings power level z-scored vs own two-year history
def f26ep_f26_earnings_power_trajectory_reconepsz_504d_base_v031_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    b = _z(re, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional growth-flavored, kept structurally distinct ---

# eps half-year growth minus year growth (growth deceleration spread)
def f26ep_f26_earnings_power_trajectory_epsgdecel_base_v032_signal(eps):
    g126 = _f26_growth(eps, 126)
    g252 = _f26_growth(eps, 252)
    b = 2.0 * g126 - g252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income roc (signed simple rate) over a quarter, smoothed
def f26ep_f26_earnings_power_trajectory_niroc_63d_base_v033_signal(netinc):
    r = _f26_roc(netinc, 63)
    b = r.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps roc over a year, percentile-ranked vs own history
def f26ep_f26_earnings_power_trajectory_epsrocrank_252d_base_v034_signal(eps):
    r = _f26_roc(eps, 252)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income growth minus eps growth (share-count contribution to per-share growth)
def f26ep_f26_earnings_power_trajectory_nivsepsg_252d_base_v035_signal(netinc, eps):
    gn = _f26_growth(netinc, 252)
    ge = _f26_growth(eps, 252)
    b = gn - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common-vs-total net income share (preferred drag on common earnings)
def f26ep_f26_earnings_power_trajectory_cmnshare_base_v036_signal(netinccmn, netinc):
    b = netinccmn / netinc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in common-vs-total share over a year (shifting preferred burden)
def f26ep_f26_earnings_power_trajectory_cmnsharechg_252d_base_v037_signal(netinccmn, netinc):
    sh = netinccmn / netinc.replace(0, np.nan)
    b = sh - sh.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings power level trend: OLS slope of eps scaled by level (per-share trajectory)
def f26ep_f26_earnings_power_trajectory_epsslope_252d_base_v038_signal(eps):
    sl = _slope(eps, 252)
    scale = eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = sl / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income trend slope over two years, scaled by level
def f26ep_f26_earnings_power_trajectory_nislope_504d_base_v039_signal(netinc):
    sl = _slope(netinc, 504)
    scale = netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    b = sl / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps trend strength: slope-to-dispersion ratio (trend quality)
def f26ep_f26_earnings_power_trajectory_epstrendq_252d_base_v040_signal(eps):
    sl = _slope(eps, 252)
    sd = (eps - eps.shift(21)).rolling(252, min_periods=126).std()
    b = sl / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps drawdown from its trailing 252d peak (earnings-power drawdown)
def f26ep_f26_earnings_power_trajectory_epsdd_252d_base_v041_signal(eps):
    pk = _rmax(eps, 252)
    b = eps / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income recovery off trailing 252d trough (earnings rebound)
def f26ep_f26_earnings_power_trajectory_nirecov_252d_base_v042_signal(netinc):
    tr = _rmin(netinc, 252)
    b = (netinc - tr) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps range position within its 252d high-low (where current earnings sit)
def f26ep_f26_earnings_power_trajectory_epsrngpos_252d_base_v043_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    b = (eps - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps range position over two years (long earnings-power position)
def f26ep_f26_earnings_power_trajectory_dilrngpos_504d_base_v044_signal(epsdil):
    hi = _rmax(epsdil, 504)
    lo = _rmin(epsdil, 504)
    b = (epsdil - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-curvature: difference of quarterly eps growth across the year (acceleration of growth)
def f26ep_f26_earnings_power_trajectory_epsgyoy_base_v045_signal(eps):
    g_recent = _f26_growth(eps, 63)
    g_old = _f26_growth(eps.shift(189), 63)
    b = g_recent - g_old
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income level percentile vs its two-year history (where current profit ranks)
def f26ep_f26_earnings_power_trajectory_nilevelz_504d_base_v046_signal(netinc):
    b = netinc.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps growth over a year (diluted earnings-power growth)
def f26ep_f26_earnings_power_trajectory_dilg_252d_base_v047_signal(epsdil):
    b = _f26_growth(epsdil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps acceleration as level
def f26ep_f26_earnings_power_trajectory_dilacc_252d_base_v048_signal(epsdil):
    b = _f26_accel_level(epsdil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common net income stability over two years
def f26ep_f26_earnings_power_trajectory_ncmnstab_504d_base_v049_signal(netinccmn):
    b = _f26_stability(netinccmn, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings hit-rate: fraction of quarters with positive sequential eps change
def f26ep_f26_earnings_power_trajectory_epshit_252d_base_v050_signal(eps):
    up = (eps - eps.shift(63) > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income hit-rate over two years (consistency of profit growth)
def f26ep_f26_earnings_power_trajectory_nihit_504d_base_v051_signal(netinc):
    up = (netinc - netinc.shift(63) > 0).astype(float)
    b = up.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth risk-adjusted by its own dispersion (growth Sharpe)
def f26ep_f26_earnings_power_trajectory_epsgsharpe_252d_base_v052_signal(eps):
    g = _f26_growth(eps, 63)
    m = g.rolling(252, min_periods=126).mean()
    sd = g.rolling(252, min_periods=126).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-and-magnitude of eps growth (asymmetric emphasis on direction)
def f26ep_f26_earnings_power_trajectory_epsgsignmag_252d_base_v053_signal(eps):
    g = _f26_growth(eps, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth tanh-squashed (bounded growth signal)
def f26ep_f26_earnings_power_trajectory_nigtanh_252d_base_v054_signal(netinc):
    g = _f26_growth(netinc, 252)
    b = np.tanh(2.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth interacted with positive streak (durable + growing)
def f26ep_f26_earnings_power_trajectory_epsgxstreak_252d_base_v055_signal(eps):
    g = _f26_growth(eps, 252)
    st = _f26_posstreak(eps, 252)
    b = g * st
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income inflection interacted with stability (clean turn)
def f26ep_f26_earnings_power_trajectory_niinflxstab_252d_base_v056_signal(netinc):
    m = _mean(netinc, 252)
    infl = (netinc - m) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    stab = _f26_stability(netinc, 252)
    b = infl * np.tanh(stab)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted eps growth (diluted growth scaled by basic-minus-diluted spread)
def f26ep_f26_earnings_power_trajectory_dilgadj_252d_base_v057_signal(eps, epsdil):
    gd = _f26_growth(epsdil, 252)
    sp = _f26_eps_spread(eps, epsdil)
    b = gd * (1.0 - sp.clip(-1, 1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-tilt of earnings power: share-count growth gated by whether earnings are positive
def f26ep_f26_earnings_power_trajectory_epsvsshares_252d_base_v058_signal(eps, shareswa):
    gs = _f26_growth(shareswa, 252)
    earn_sign = np.tanh(eps / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    # issuance into strength vs issuance into weakness
    b = gs * earn_sign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-boost share of per-share earnings growth: share-shrinkage contribution vs eps growth
def f26ep_f26_earnings_power_trajectory_organiceps_252d_base_v059_signal(eps, shareswa):
    ge = _f26_growth(eps, 252)
    gs = _f26_growth(shareswa, 252)
    # fraction of eps growth attributable to share-count change (signed share contribution / total)
    b = (-gs) / (ge.abs() + gs.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base drag on the earnings trajectory: total-profit trend minus per-share trend
def f26ep_f26_earnings_power_trajectory_reconslope_504d_base_v060_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    sl_ni = _slope(netinc, 504) / netinc.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    sl_re = _slope(re, 504) / re.abs().rolling(504, min_periods=252).mean().replace(0, np.nan)
    b = sl_ni - sl_re
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps acceleration ranked vs own history (relative inflection)
def f26ep_f26_earnings_power_trajectory_epsaccrank_252d_base_v061_signal(eps):
    a = _f26_accel_level(eps, 252)
    b = a.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income underwater intensity: fraction of year below peak weighted by depth-below-peak
def f26ep_f26_earnings_power_trajectory_nidddur_252d_base_v062_signal(netinc):
    pk = _rmax(netinc, 252)
    scale = netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    underdepth = ((pk - netinc) / scale).clip(lower=0)
    b = underdepth.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps quartile-of-range change over a year (climbing within earnings band)
def f26ep_f26_earnings_power_trajectory_epsrngchg_252d_base_v063_signal(eps):
    hi = _rmax(eps, 252)
    lo = _rmin(eps, 252)
    rp = (eps - lo) / (hi - lo).replace(0, np.nan)
    b = rp - rp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common net income inflection vs trailing mean
def f26ep_f26_earnings_power_trajectory_ncmninflect_252d_base_v064_signal(netinccmn):
    m = _mean(netinccmn, 252)
    b = (netinccmn - m) / netinccmn.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted eps stability over a year
def f26ep_f26_earnings_power_trajectory_dilstab_252d_base_v065_signal(epsdil):
    b = _f26_stability(epsdil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps positive-streak change over a year (improving/deteriorating consistency)
def f26ep_f26_earnings_power_trajectory_epsstreakchg_252d_base_v066_signal(eps):
    st = _f26_posstreak(eps, 252)
    b = st - st.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income coefficient of variation (raw earnings volatility, inverse stability)
def f26ep_f26_earnings_power_trajectory_nicv_252d_base_v067_signal(netinc):
    sd = _std(netinc, 252)
    m = netinc.abs().rolling(252, min_periods=126).mean()
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps two-year growth minus net income two-year growth (per-share leakage)
def f26ep_f26_earnings_power_trajectory_epsnileak_504d_base_v068_signal(eps, netinc):
    ge = _f26_growth(eps, 504)
    gn = _f26_growth(netinc, 504)
    b = ge - gn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic growth spread, ranked vs history (dilution-trend regime)
def f26ep_f26_earnings_power_trajectory_dilgaprank_252d_base_v069_signal(eps, epsdil):
    gb = _f26_growth(eps, 252)
    gd = _f26_growth(epsdil, 252)
    gap = gd - gb
    b = gap.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings power trend consistency: sign-agreement of eps growth over a year
def f26ep_f26_earnings_power_trajectory_epsgsign_252d_base_v070_signal(eps):
    g = _f26_growth(eps, 21)
    sgn = np.sign(g)
    b = sgn.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income exponentially-weighted growth (recency-weighted profit trajectory)
def f26ep_f26_earnings_power_trajectory_niewmg_252d_base_v071_signal(netinc):
    g = _f26_growth(netinc, 63)
    b = g.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps inflection acceleration: change in eps-vs-mean gap over a quarter
def f26ep_f26_earnings_power_trajectory_epsinflacc_126d_base_v072_signal(eps):
    m = _mean(eps, 126)
    gap = (eps - m) / eps.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# common net income growth risk-adjusted by dispersion
def f26ep_f26_earnings_power_trajectory_ncmngsharpe_252d_base_v073_signal(netinccmn):
    g = _f26_growth(netinccmn, 63)
    m = g.rolling(252, min_periods=126).mean()
    sd = g.rolling(252, min_periods=126).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share earnings power drawdown over two years (reconstructed eps)
def f26ep_f26_earnings_power_trajectory_recondd_504d_base_v074_signal(netinc, shareswa):
    re = _f26_eps_recon(netinc, shareswa)
    pk = _rmax(re, 504)
    b = re / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite earnings-power: year eps growth x positive streak x stability sign
def f26ep_f26_earnings_power_trajectory_epcomposite_252d_base_v075_signal(eps):
    g = _f26_growth(eps, 252)
    st = _f26_posstreak(eps, 252)
    stab = _f26_stability(eps, 252)
    b = g * st * np.sign(stab)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ep_f26_earnings_power_trajectory_epsg_63d_base_v001_signal,
    f26ep_f26_earnings_power_trajectory_epsg_252d_base_v002_signal,
    f26ep_f26_earnings_power_trajectory_epsg_504d_base_v003_signal,
    f26ep_f26_earnings_power_trajectory_epsgz_252d_base_v004_signal,
    f26ep_f26_earnings_power_trajectory_epsgrank_252d_base_v005_signal,
    f26ep_f26_earnings_power_trajectory_nig_252d_base_v006_signal,
    f26ep_f26_earnings_power_trajectory_nig_63d_base_v007_signal,
    f26ep_f26_earnings_power_trajectory_nig_504d_base_v008_signal,
    f26ep_f26_earnings_power_trajectory_ncmng_252d_base_v009_signal,
    f26ep_f26_earnings_power_trajectory_ncmngrank_252d_base_v010_signal,
    f26ep_f26_earnings_power_trajectory_nistab_252d_base_v011_signal,
    f26ep_f26_earnings_power_trajectory_epsstab_504d_base_v012_signal,
    f26ep_f26_earnings_power_trajectory_epsdisp_252d_base_v013_signal,
    f26ep_f26_earnings_power_trajectory_nidisp_252d_base_v014_signal,
    f26ep_f26_earnings_power_trajectory_epsacc_63d_base_v015_signal,
    f26ep_f26_earnings_power_trajectory_epsacc_252d_base_v016_signal,
    f26ep_f26_earnings_power_trajectory_niacc_252d_base_v017_signal,
    f26ep_f26_earnings_power_trajectory_epsaccz_252d_base_v018_signal,
    f26ep_f26_earnings_power_trajectory_epsspr_base_v019_signal,
    f26ep_f26_earnings_power_trajectory_epssprsm_63d_base_v020_signal,
    f26ep_f26_earnings_power_trajectory_epssprchg_252d_base_v021_signal,
    f26ep_f26_earnings_power_trajectory_dilgrgap_252d_base_v022_signal,
    f26ep_f26_earnings_power_trajectory_nistreak_252d_base_v023_signal,
    f26ep_f26_earnings_power_trajectory_epsstreak_504d_base_v024_signal,
    f26ep_f26_earnings_power_trajectory_nirun_252d_base_v025_signal,
    f26ep_f26_earnings_power_trajectory_niinflect_252d_base_v026_signal,
    f26ep_f26_earnings_power_trajectory_epsinflect_126d_base_v027_signal,
    f26ep_f26_earnings_power_trajectory_lossnar_252d_base_v028_signal,
    f26ep_f26_earnings_power_trajectory_reconepsg_252d_base_v029_signal,
    f26ep_f26_earnings_power_trajectory_epsrecongap_base_v030_signal,
    f26ep_f26_earnings_power_trajectory_reconepsz_504d_base_v031_signal,
    f26ep_f26_earnings_power_trajectory_epsgdecel_base_v032_signal,
    f26ep_f26_earnings_power_trajectory_niroc_63d_base_v033_signal,
    f26ep_f26_earnings_power_trajectory_epsrocrank_252d_base_v034_signal,
    f26ep_f26_earnings_power_trajectory_nivsepsg_252d_base_v035_signal,
    f26ep_f26_earnings_power_trajectory_cmnshare_base_v036_signal,
    f26ep_f26_earnings_power_trajectory_cmnsharechg_252d_base_v037_signal,
    f26ep_f26_earnings_power_trajectory_epsslope_252d_base_v038_signal,
    f26ep_f26_earnings_power_trajectory_nislope_504d_base_v039_signal,
    f26ep_f26_earnings_power_trajectory_epstrendq_252d_base_v040_signal,
    f26ep_f26_earnings_power_trajectory_epsdd_252d_base_v041_signal,
    f26ep_f26_earnings_power_trajectory_nirecov_252d_base_v042_signal,
    f26ep_f26_earnings_power_trajectory_epsrngpos_252d_base_v043_signal,
    f26ep_f26_earnings_power_trajectory_dilrngpos_504d_base_v044_signal,
    f26ep_f26_earnings_power_trajectory_epsgyoy_base_v045_signal,
    f26ep_f26_earnings_power_trajectory_nilevelz_504d_base_v046_signal,
    f26ep_f26_earnings_power_trajectory_dilg_252d_base_v047_signal,
    f26ep_f26_earnings_power_trajectory_dilacc_252d_base_v048_signal,
    f26ep_f26_earnings_power_trajectory_ncmnstab_504d_base_v049_signal,
    f26ep_f26_earnings_power_trajectory_epshit_252d_base_v050_signal,
    f26ep_f26_earnings_power_trajectory_nihit_504d_base_v051_signal,
    f26ep_f26_earnings_power_trajectory_epsgsharpe_252d_base_v052_signal,
    f26ep_f26_earnings_power_trajectory_epsgsignmag_252d_base_v053_signal,
    f26ep_f26_earnings_power_trajectory_nigtanh_252d_base_v054_signal,
    f26ep_f26_earnings_power_trajectory_epsgxstreak_252d_base_v055_signal,
    f26ep_f26_earnings_power_trajectory_niinflxstab_252d_base_v056_signal,
    f26ep_f26_earnings_power_trajectory_dilgadj_252d_base_v057_signal,
    f26ep_f26_earnings_power_trajectory_epsvsshares_252d_base_v058_signal,
    f26ep_f26_earnings_power_trajectory_organiceps_252d_base_v059_signal,
    f26ep_f26_earnings_power_trajectory_reconslope_504d_base_v060_signal,
    f26ep_f26_earnings_power_trajectory_epsaccrank_252d_base_v061_signal,
    f26ep_f26_earnings_power_trajectory_nidddur_252d_base_v062_signal,
    f26ep_f26_earnings_power_trajectory_epsrngchg_252d_base_v063_signal,
    f26ep_f26_earnings_power_trajectory_ncmninflect_252d_base_v064_signal,
    f26ep_f26_earnings_power_trajectory_dilstab_252d_base_v065_signal,
    f26ep_f26_earnings_power_trajectory_epsstreakchg_252d_base_v066_signal,
    f26ep_f26_earnings_power_trajectory_nicv_252d_base_v067_signal,
    f26ep_f26_earnings_power_trajectory_epsnileak_504d_base_v068_signal,
    f26ep_f26_earnings_power_trajectory_dilgaprank_252d_base_v069_signal,
    f26ep_f26_earnings_power_trajectory_epsgsign_252d_base_v070_signal,
    f26ep_f26_earnings_power_trajectory_niewmg_252d_base_v071_signal,
    f26ep_f26_earnings_power_trajectory_epsinflacc_126d_base_v072_signal,
    f26ep_f26_earnings_power_trajectory_ncmngsharpe_252d_base_v073_signal,
    f26ep_f26_earnings_power_trajectory_recondd_504d_base_v074_signal,
    f26ep_f26_earnings_power_trajectory_epcomposite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_EARNINGS_POWER_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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

    print("OK f26_earnings_power_trajectory_base_001_075_claude: %d features pass" % n_features)
