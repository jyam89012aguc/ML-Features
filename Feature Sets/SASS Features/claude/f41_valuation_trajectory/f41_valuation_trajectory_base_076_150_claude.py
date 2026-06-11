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


def _slope(s, w):
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        x = x - x.mean()
        denom = (x ** 2).sum()
        if denom == 0.0:
            return np.nan
        return float(np.dot(x, a) / denom)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives =====
def _f41_logmult(m):
    return np.log(m.replace(0, np.nan).clip(lower=1e-9))


def _f41_rerate(m, w):
    lm = _f41_logmult(m)
    return lm - lm.shift(w)


def _f41_revgap(m, w):
    lm = _f41_logmult(m)
    return lm - lm.rolling(w, min_periods=max(2, w // 2)).mean()


def _f41_halflife_decay(m, span):
    lm = _f41_logmult(m)
    return lm - lm.ewm(span=span, min_periods=max(2, span // 3)).mean()


# ============================================================
# --- EMA-trend (re-rating regime) on each multiple ---
def f41vj_f41_valuation_trajectory_peematrend_63d_base_v076_signal(pe):
    lm = _f41_logmult(pe)
    fast = lm.ewm(span=21, min_periods=10).mean()
    slow = lm.ewm(span=84, min_periods=28).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbematrend_63d_base_v077_signal(pb):
    lm = _f41_logmult(pb)
    fast = lm.ewm(span=21, min_periods=10).mean()
    slow = lm.ewm(span=84, min_periods=28).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebematrend_63d_base_v078_signal(evebitda):
    lm = _f41_logmult(evebitda)
    fast = lm.ewm(span=21, min_periods=10).mean()
    slow = lm.ewm(span=84, min_periods=28).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- decay-displacement (price-multiple vs its half-life memory) ---
def f41vj_f41_valuation_trajectory_pedecay_base_v079_signal(pe):
    b = _f41_halflife_decay(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psdecay_base_v080_signal(ps):
    b = _f41_halflife_decay(ps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating over 504d (multi-year compression/expansion) ---
def f41vj_f41_valuation_trajectory_pererate_504d_base_v081_signal(pe):
    b = _f41_rerate(pe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrerate_504d_base_v082_signal(evebitda):
    b = _f41_rerate(evebitda, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrerate_504d_base_v083_signal(ps):
    b = _f41_rerate(ps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 504d valuation z (long-history extremity) ---
def f41vj_f41_valuation_trajectory_pezhist_504d_base_v084_signal(pe):
    b = _z(pe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebzhist_504d_base_v085_signal(evebitda):
    b = _z(evebitda, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating direction × magnitude over 252d, vol-scaled (risk-adj re-rating) ---
def f41vj_f41_valuation_trajectory_pererateadj_252d_base_v086_signal(pe):
    r = _f41_rerate(pe, 252)
    vol = _std(_f41_logmult(pe).diff(), 252) * np.sqrt(252.0)
    b = r / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrerateadj_252d_base_v087_signal(evebitda):
    r = _f41_rerate(evebitda, 252)
    vol = _std(_f41_logmult(evebitda).diff(), 252) * np.sqrt(252.0)
    b = r / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrerateadj_252d_base_v088_signal(ps):
    r = _f41_rerate(ps, 252)
    vol = _std(_f41_logmult(ps).diff(), 252) * np.sqrt(252.0)
    b = r / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple efficiency ratio (net re-rating / total path traveled) ---
def f41vj_f41_valuation_trajectory_peeff_126d_base_v089_signal(pe):
    lm = _f41_logmult(pe)
    net = (lm - lm.shift(126)).abs()
    path = lm.diff().abs().rolling(126, min_periods=63).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebeff_126d_base_v090_signal(evebitda):
    lm = _f41_logmult(evebitda)
    net = (lm - lm.shift(126)).abs()
    path = lm.diff().abs().rolling(126, min_periods=63).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pseff_252d_base_v091_signal(ps):
    lm = _f41_logmult(ps)
    net = (lm - lm.shift(252)).abs()
    path = lm.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- distance of current multiple below own 504d max in vol units (de-rating depth) ---
def f41vj_f41_valuation_trajectory_pederatedepth_504d_base_v092_signal(pe):
    lm = _f41_logmult(pe)
    hi = _rmax(lm, 504)
    vol = _std(lm.diff(), 126) * np.sqrt(126.0)
    b = (lm - hi) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebderatedepth_504d_base_v093_signal(evebitda):
    lm = _f41_logmult(evebitda)
    hi = _rmax(lm, 504)
    vol = _std(lm.diff(), 126) * np.sqrt(126.0)
    b = (lm - hi) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating skewness (asymmetry of multiple changes) ---
def f41vj_f41_valuation_trajectory_peskew_252d_base_v094_signal(pe):
    chg = _f41_logmult(pe).diff()
    b = chg.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psskew_252d_base_v095_signal(ps):
    chg = _f41_logmult(ps).diff()
    b = chg.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- upside vs downside re-rating semivariance ratio ---
def f41vj_f41_valuation_trajectory_pesemiratio_252d_base_v096_signal(pe):
    chg = _f41_logmult(pe).diff()
    up = chg.clip(lower=0).rolling(252, min_periods=126).std()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).std()
    b = up / dn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebsemiratio_252d_base_v097_signal(evebitda):
    chg = _f41_logmult(evebitda).diff()
    up = chg.clip(lower=0).rolling(252, min_periods=126).std()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).std()
    b = up / dn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple autocorrelation of changes (re-rating persistence) ---
def f41vj_f41_valuation_trajectory_peautocorr_126d_base_v098_signal(pe):
    chg = _f41_logmult(pe).diff()

    def _ac(a):
        a0 = a[:-1]
        a1 = a[1:]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return float(np.corrcoef(a0, a1)[0, 1])

    b = chg.rolling(126, min_periods=63).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psautocorr_126d_base_v099_signal(ps):
    chg = _f41_logmult(ps).diff()

    def _ac(a):
        a0 = a[:-1]
        a1 = a[1:]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return float(np.corrcoef(a0, a1)[0, 1])

    b = chg.rolling(126, min_periods=63).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- variance ratio of re-rating (trending vs mean-reverting multiple) ---
def f41vj_f41_valuation_trajectory_pevarratio_base_v100_signal(pe):
    lm = _f41_logmult(pe)
    v1 = _std(lm.diff(), 252) ** 2
    v5 = _std(lm.diff(5), 252) ** 2 / 5.0
    b = v5 / v1.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebvarratio_base_v101_signal(evebitda):
    lm = _f41_logmult(evebitda)
    v1 = _std(lm.diff(), 252) ** 2
    v5 = _std(lm.diff(5), 252) ** 2 / 5.0
    b = v5 / v1.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV trend vs EV/EBITDA trend divergence (denominator-driven re-rating) ---
def f41vj_f41_valuation_trajectory_evdenomdiv_252d_base_v102_signal(ev, evebitda):
    re = _f41_rerate(ev, 252)
    rm = _f41_rerate(evebitda, 252)
    b = re - rm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evdenomdiv_126d_base_v103_signal(ev, evebitda):
    re = _f41_rerate(ev, 126)
    rm = _f41_rerate(evebitda, 126)
    b = re - rm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- marketcap vs ps re-rating divergence (cap growth vs sales-multiple) ---
def f41vj_f41_valuation_trajectory_mcappsdiv_252d_base_v104_signal(marketcap, ps):
    rm = _f41_rerate(marketcap, 252)
    rp = _f41_rerate(ps, 252)
    b = rm - rp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- valuation composite z across multiples (blended richness level) ---
def f41vj_f41_valuation_trajectory_blendz_252d_base_v105_signal(pe, pb, ps, evebitda):
    b = pd.concat(
        [_z(pe, 252), _z(pb, 252), _z(ps, 252), _z(evebitda, 252)], axis=1
    ).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blended re-rating momentum (avg compression across multiples over a quarter) ---
def f41vj_f41_valuation_trajectory_blendmom_63d_base_v106_signal(pe, pb, ps, evebitda):
    b = pd.concat(
        [
            _f41_rerate(pe, 63),
            _f41_rerate(pb, 63),
            _f41_rerate(ps, 63),
            _f41_rerate(evebitda, 63),
        ],
        axis=1,
    ).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating range expansion vs contraction (vol regime of multiple) ---
def f41vj_f41_valuation_trajectory_pevolregime_base_v107_signal(pe):
    chg = _f41_logmult(pe).diff()
    short = _std(chg, 21)
    long = _std(chg, 126)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebvolregime_base_v108_signal(evebitda):
    chg = _f41_logmult(evebitda).diff()
    short = _std(chg, 21)
    long = _std(chg, 126)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple band-position z (where in 252d range, standardized) ---
def f41vj_f41_valuation_trajectory_pebandz_252d_base_v109_signal(pe):
    hi = _rmax(pe, 252)
    lo = _rmin(pe, 252)
    pos = (pe - lo) / (hi - lo).replace(0, np.nan)
    b = _z(pos, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psbandz_252d_base_v110_signal(ps):
    hi = _rmax(ps, 252)
    lo = _rmin(ps, 252)
    pos = (ps - lo) / (hi - lo).replace(0, np.nan)
    b = _z(pos, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating slope of slope (curvature) on EV/EBITDA ---
def f41vj_f41_valuation_trajectory_evebcurv_252d_base_v111_signal(evebitda):
    lm = _f41_logmult(evebitda)
    sl = _slope(lm, 126)
    b = _slope(sl, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mean-reversion gap half-life weighted (recent-weighted cheapness) ---
def f41vj_f41_valuation_trajectory_pbcompresshvar_base_v112_signal(pb):
    # heteroskedastic compression: 21d re-rating divided by its 252d realized vol band
    r = _f41_rerate(pb, 21)
    band = _std(_f41_logmult(pb).diff(), 252) * np.sqrt(21.0)
    b = r / band.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebgaprangepos_base_v113_signal(evebitda):
    # where the current reversion gap sits within its own 252d gap range
    g = _f41_revgap(evebitda, 126)
    hi = _rmax(g, 252)
    lo = _rmin(g, 252)
    b = (g - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating reversal: 252d level vs 63d recent direction (snapback) ---
def f41vj_f41_valuation_trajectory_pesnapback_base_v114_signal(pe):
    longgap = _f41_revgap(pe, 504)
    recent = _f41_rerate(pe, 21)
    b = -np.sign(longgap) * recent
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebsnapback_base_v115_signal(evebitda):
    longgap = _f41_revgap(evebitda, 504)
    recent = _f41_rerate(evebitda, 21)
    b = -np.sign(longgap) * recent
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple drawdown from peak (de-rating drawdown) ---
def f41vj_f41_valuation_trajectory_pevaldd_504d_base_v116_signal(pe):
    hi = _rmax(pe, 504)
    b = pe / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psvaldd_504d_base_v117_signal(ps):
    hi = _rmax(ps, 504)
    b = ps / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple recovery from trough (re-rating off cheap floor) ---
def f41vj_f41_valuation_trajectory_pevshape_504d_base_v118_signal(pe):
    # V-shape balance of the valuation path: recovery-off-trough vs drawdown-from-peak
    lo = _rmin(pe, 504)
    hi = _rmax(pe, 504)
    rec = (pe - lo) / lo.replace(0, np.nan)
    dd = (hi - pe) / hi.replace(0, np.nan)
    b = (rec - dd) / (rec + dd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebvshape_504d_base_v119_signal(evebitda):
    # V-shape balance of the valuation path: recovery-off-trough vs drawdown-from-peak
    lo = _rmin(evebitda, 504)
    hi = _rmax(evebitda, 504)
    rec = (evebitda - lo) / lo.replace(0, np.nan)
    dd = (hi - evebitda) / hi.replace(0, np.nan)
    b = (rec - dd) / (rec + dd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating consistency: fraction of quarters with positive YoY re-rating ---
def f41vj_f41_valuation_trajectory_pererateyoy_base_v120_signal(pe):
    yoy = _f41_rerate(pe, 252)
    b = (yoy > 0).astype(float).rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrerateyoyavg_base_v121_signal(evebitda):
    # smoothed YoY re-rating: trailing average of the 252d log re-rating
    yoy = _f41_rerate(evebitda, 252)
    b = yoy.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV premium trajectory rank (enterprise premium percentile drift) ---
def f41vj_f41_valuation_trajectory_evpremrank_504d_base_v122_signal(ev, marketcap):
    prem = _f41_logmult(ev) - _f41_logmult(marketcap)
    b = _rank(prem, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- log re-rating gap between pe and evebitda (equity vs enterprise re-rating) ---
def f41vj_f41_valuation_trajectory_peeveb_rerdiv_252d_base_v123_signal(pe, evebitda):
    b = _f41_rerate(pe, 252) - _f41_rerate(evebitda, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbps_rerdiv_252d_base_v124_signal(pb, ps):
    b = _f41_rerate(pb, 252) - _f41_rerate(ps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating impulse: today's jump vs trailing typical jump (z of daily change) ---
def f41vj_f41_valuation_trajectory_peimpulse_base_v125_signal(pe):
    chg = _f41_logmult(pe).diff()
    b = _z(chg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebimpulse_base_v126_signal(evebitda):
    chg = _f41_logmult(evebitda).diff()
    b = _z(chg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- compression streak depth (how deep below recent typical the multiple sits) ---
def f41vj_f41_valuation_trajectory_pscompressdepth_base_v127_signal(ps):
    lm = _f41_logmult(ps)
    below = (lm.rolling(126, min_periods=63).mean() - lm).clip(lower=0)
    b = below.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebexpandheight_base_v128_signal(evebitda):
    lm = _f41_logmult(evebitda)
    above = (lm - lm.rolling(126, min_periods=63).mean()).clip(lower=0)
    b = above.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating breadth (cross-multiple) over a year, magnitude-weighted ---
def f41vj_f41_valuation_trajectory_blendbreadthyr_base_v129_signal(pe, pb, ps, evebitda):
    # magnitude-weighted cross-multiple re-rating breadth (continuous tanh of each)
    s = (
        np.tanh(4.0 * _f41_rerate(pe, 252))
        + np.tanh(4.0 * _f41_rerate(pb, 252))
        + np.tanh(4.0 * _f41_rerate(ps, 252))
        + np.tanh(4.0 * _f41_rerate(evebitda, 252))
    )
    b = s / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- marketcap-vs-ev structural re-rating (equity share of enterprise drift) ---
def f41vj_f41_valuation_trajectory_eqshare_252d_base_v130_signal(marketcap, ev):
    share = marketcap / ev.replace(0, np.nan)
    b = share - share.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_eqsharez_base_v131_signal(marketcap, ev):
    share = marketcap / ev.replace(0, np.nan)
    b = _z(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple kurtosis of changes (fat-tailed re-rating shocks) ---
def f41vj_f41_valuation_trajectory_pekurt_252d_base_v132_signal(pe):
    chg = _f41_logmult(pe).diff()
    b = chg.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating momentum minus reversion gap (trend vs value tension) ---
def f41vj_f41_valuation_trajectory_petension_base_v133_signal(pe):
    # trend-vs-value tension as a ratio of momentum to reversion-gap magnitude
    mom = _f41_rerate(pe, 126)
    gap = _f41_revgap(pe, 252)
    b = mom / (gap.abs() + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebtension_base_v134_signal(evebitda):
    mom = _f41_rerate(evebitda, 63)
    gap = _f41_revgap(evebitda, 504)
    b = mom + gap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple slope over 504d (long-horizon structural re-rating drift) ---
def f41vj_f41_valuation_trajectory_pbslope_504d_base_v135_signal(pb):
    b = _slope(_f41_logmult(pb), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psslope_504d_base_v136_signal(ps):
    b = _slope(_f41_logmult(ps), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating acceleration of EV premium (premium curvature) ---
def f41vj_f41_valuation_trajectory_evpremaccel_base_v137_signal(ev, marketcap):
    prem = _f41_logmult(ev) - _f41_logmult(marketcap)
    recent = prem - prem.shift(126)
    older = prem.shift(126) - prem.shift(252)
    b = recent - older
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- valuation rank velocity on PB (cheapness percentile drift) ---
def f41vj_f41_valuation_trajectory_pbrankvel_504d_base_v138_signal(pb):
    rk = _rank(pb, 504)
    b = rk - rk.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_psrankvel_504d_base_v139_signal(ps):
    rk = _rank(ps, 504)
    b = rk - rk.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating dispersion across multiples over a quarter (regime disagreement) ---
def f41vj_f41_valuation_trajectory_blenddisp63_base_v140_signal(pe, pb, ps, evebitda):
    b = pd.concat(
        [
            _f41_rerate(pe, 63),
            _f41_rerate(pb, 63),
            _f41_rerate(ps, 63),
            _f41_rerate(evebitda, 63),
        ],
        axis=1,
    ).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV/EBITDA gap relative to PB gap (enterprise vs book re-rating tilt) ---
def f41vj_f41_valuation_trajectory_evebpbtilt_base_v141_signal(evebitda, pb):
    b = _f41_revgap(evebitda, 252) - _f41_revgap(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- compression half-life vs full-history gap (recency-weighted reversion) ---
def f41vj_f41_valuation_trajectory_perecencygap_base_v142_signal(pe):
    fast = _f41_halflife_decay(pe, 42)
    slow = _f41_revgap(pe, 252)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- valuation z momentum (change in 252d z over a quarter) ---
def f41vj_f41_valuation_trajectory_pszmom_base_v143_signal(ps):
    z = _z(ps, 252)
    b = z - z.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebzmom_base_v144_signal(evebitda):
    z = _z(evebitda, 252)
    b = z - z.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- marketcap drawdown-from-peak (cap de-rating drawdown) ---
def f41vj_f41_valuation_trajectory_mcapdd_504d_base_v145_signal(marketcap):
    hi = _rmax(marketcap, 504)
    b = _f41_logmult(marketcap) - _f41_logmult(hi)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- re-rating Sharpe-like (252d rerate over its own dispersion path) ---
def f41vj_f41_valuation_trajectory_pererange252_base_v146_signal(pe):
    # log span of the multiple over a year (re-rating amplitude), de-trended by its mean
    lm = _f41_logmult(pe)
    span = _rmax(lm, 252) - _rmin(lm, 252)
    b = span - span.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evebrerange252_base_v147_signal(evebitda):
    # log span of the multiple over a year (re-rating amplitude), de-trended by its mean
    lm = _f41_logmult(evebitda)
    span = _rmax(lm, 252) - _rmin(lm, 252)
    b = span - span.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite cheapness improvement: blended rank velocity across multiples ---
def f41vj_f41_valuation_trajectory_blendrankvel_base_v148_signal(pe, pb, ps, evebitda):
    rk = pd.concat(
        [_rank(pe, 504), _rank(pb, 504), _rank(ps, 504), _rank(evebitda, 504)], axis=1
    ).mean(axis=1)
    b = rk - rk.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV trend over 504d normalized by marketcap trend (deleveraging re-rating) ---
def f41vj_f41_valuation_trajectory_evmcapdiv504_base_v149_signal(ev, marketcap):
    re = _f41_rerate(ev, 504)
    rm = _f41_rerate(marketcap, 504)
    b = re - rm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple tension composite: blended (momentum + reversion) signed score ---
def f41vj_f41_valuation_trajectory_blendtension_base_v150_signal(pe, ps, evebitda):
    t1 = _f41_rerate(pe, 63) + _f41_revgap(pe, 504)
    t2 = _f41_rerate(ps, 63) + _f41_revgap(ps, 504)
    t3 = _f41_rerate(evebitda, 63) + _f41_revgap(evebitda, 504)
    b = pd.concat([t1, t2, t3], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41vj_f41_valuation_trajectory_peematrend_63d_base_v076_signal,
    f41vj_f41_valuation_trajectory_pbematrend_63d_base_v077_signal,
    f41vj_f41_valuation_trajectory_evebematrend_63d_base_v078_signal,
    f41vj_f41_valuation_trajectory_pedecay_base_v079_signal,
    f41vj_f41_valuation_trajectory_psdecay_base_v080_signal,
    f41vj_f41_valuation_trajectory_pererate_504d_base_v081_signal,
    f41vj_f41_valuation_trajectory_evebrerate_504d_base_v082_signal,
    f41vj_f41_valuation_trajectory_psrerate_504d_base_v083_signal,
    f41vj_f41_valuation_trajectory_pezhist_504d_base_v084_signal,
    f41vj_f41_valuation_trajectory_evebzhist_504d_base_v085_signal,
    f41vj_f41_valuation_trajectory_pererateadj_252d_base_v086_signal,
    f41vj_f41_valuation_trajectory_evebrerateadj_252d_base_v087_signal,
    f41vj_f41_valuation_trajectory_psrerateadj_252d_base_v088_signal,
    f41vj_f41_valuation_trajectory_peeff_126d_base_v089_signal,
    f41vj_f41_valuation_trajectory_evebeff_126d_base_v090_signal,
    f41vj_f41_valuation_trajectory_pseff_252d_base_v091_signal,
    f41vj_f41_valuation_trajectory_pederatedepth_504d_base_v092_signal,
    f41vj_f41_valuation_trajectory_evebderatedepth_504d_base_v093_signal,
    f41vj_f41_valuation_trajectory_peskew_252d_base_v094_signal,
    f41vj_f41_valuation_trajectory_psskew_252d_base_v095_signal,
    f41vj_f41_valuation_trajectory_pesemiratio_252d_base_v096_signal,
    f41vj_f41_valuation_trajectory_evebsemiratio_252d_base_v097_signal,
    f41vj_f41_valuation_trajectory_peautocorr_126d_base_v098_signal,
    f41vj_f41_valuation_trajectory_psautocorr_126d_base_v099_signal,
    f41vj_f41_valuation_trajectory_pevarratio_base_v100_signal,
    f41vj_f41_valuation_trajectory_evebvarratio_base_v101_signal,
    f41vj_f41_valuation_trajectory_evdenomdiv_252d_base_v102_signal,
    f41vj_f41_valuation_trajectory_evdenomdiv_126d_base_v103_signal,
    f41vj_f41_valuation_trajectory_mcappsdiv_252d_base_v104_signal,
    f41vj_f41_valuation_trajectory_blendz_252d_base_v105_signal,
    f41vj_f41_valuation_trajectory_blendmom_63d_base_v106_signal,
    f41vj_f41_valuation_trajectory_pevolregime_base_v107_signal,
    f41vj_f41_valuation_trajectory_evebvolregime_base_v108_signal,
    f41vj_f41_valuation_trajectory_pebandz_252d_base_v109_signal,
    f41vj_f41_valuation_trajectory_psbandz_252d_base_v110_signal,
    f41vj_f41_valuation_trajectory_evebcurv_252d_base_v111_signal,
    f41vj_f41_valuation_trajectory_pbcompresshvar_base_v112_signal,
    f41vj_f41_valuation_trajectory_evebgaprangepos_base_v113_signal,
    f41vj_f41_valuation_trajectory_pesnapback_base_v114_signal,
    f41vj_f41_valuation_trajectory_evebsnapback_base_v115_signal,
    f41vj_f41_valuation_trajectory_pevaldd_504d_base_v116_signal,
    f41vj_f41_valuation_trajectory_psvaldd_504d_base_v117_signal,
    f41vj_f41_valuation_trajectory_pevshape_504d_base_v118_signal,
    f41vj_f41_valuation_trajectory_evebvshape_504d_base_v119_signal,
    f41vj_f41_valuation_trajectory_pererateyoy_base_v120_signal,
    f41vj_f41_valuation_trajectory_evebrerateyoyavg_base_v121_signal,
    f41vj_f41_valuation_trajectory_evpremrank_504d_base_v122_signal,
    f41vj_f41_valuation_trajectory_peeveb_rerdiv_252d_base_v123_signal,
    f41vj_f41_valuation_trajectory_pbps_rerdiv_252d_base_v124_signal,
    f41vj_f41_valuation_trajectory_peimpulse_base_v125_signal,
    f41vj_f41_valuation_trajectory_evebimpulse_base_v126_signal,
    f41vj_f41_valuation_trajectory_pscompressdepth_base_v127_signal,
    f41vj_f41_valuation_trajectory_evebexpandheight_base_v128_signal,
    f41vj_f41_valuation_trajectory_blendbreadthyr_base_v129_signal,
    f41vj_f41_valuation_trajectory_eqshare_252d_base_v130_signal,
    f41vj_f41_valuation_trajectory_eqsharez_base_v131_signal,
    f41vj_f41_valuation_trajectory_pekurt_252d_base_v132_signal,
    f41vj_f41_valuation_trajectory_petension_base_v133_signal,
    f41vj_f41_valuation_trajectory_evebtension_base_v134_signal,
    f41vj_f41_valuation_trajectory_pbslope_504d_base_v135_signal,
    f41vj_f41_valuation_trajectory_psslope_504d_base_v136_signal,
    f41vj_f41_valuation_trajectory_evpremaccel_base_v137_signal,
    f41vj_f41_valuation_trajectory_pbrankvel_504d_base_v138_signal,
    f41vj_f41_valuation_trajectory_psrankvel_504d_base_v139_signal,
    f41vj_f41_valuation_trajectory_blenddisp63_base_v140_signal,
    f41vj_f41_valuation_trajectory_evebpbtilt_base_v141_signal,
    f41vj_f41_valuation_trajectory_perecencygap_base_v142_signal,
    f41vj_f41_valuation_trajectory_pszmom_base_v143_signal,
    f41vj_f41_valuation_trajectory_evebzmom_base_v144_signal,
    f41vj_f41_valuation_trajectory_mcapdd_504d_base_v145_signal,
    f41vj_f41_valuation_trajectory_pererange252_base_v146_signal,
    f41vj_f41_valuation_trajectory_evebrerange252_base_v147_signal,
    f41vj_f41_valuation_trajectory_blendrankvel_base_v148_signal,
    f41vj_f41_valuation_trajectory_evmcapdiv504_base_v149_signal,
    f41vj_f41_valuation_trajectory_blendtension_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_VALUATION_TRAJECTORY_REGISTRY_076_150 = REGISTRY


def _build_synth():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    pe = _fund(101, base=18.0, drift=0.03, vol=0.06).rename("pe")
    pb = _fund(102, base=2.5, drift=0.02, vol=0.05).rename("pb")
    ps = _fund(103, base=3.0, drift=0.025, vol=0.055).rename("ps")
    evebitda = _fund(104, base=11.0, drift=0.028, vol=0.05).rename("evebitda")
    ev = _fund(105, base=5e9, drift=0.03, vol=0.05).rename("ev")
    marketcap = _fund(106, base=4e9, drift=0.028, vol=0.05).rename("marketcap")
    return {
        "pe": pe, "pb": pb, "ps": ps,
        "evebitda": evebitda, "ev": ev, "marketcap": marketcap,
    }


if __name__ == "__main__":
    cols = _build_synth()

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

    print("OK f41_valuation_trajectory_base_076_150_claude: %d features pass" % n_features)
