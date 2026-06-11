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


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float(np.dot(idx, a) / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== f24 profitability-inflection primitives =====
def _f24pi_signmag(s):
    return np.sign(s) * np.sqrt(np.abs(s))


def _f24pi_pos_share(s, w):
    # magnitude-weighted positive share over window (profit vs gross flow)
    pos = s.clip(lower=0).rolling(w, min_periods=max(1, w // 2)).sum()
    gross = s.abs().rolling(w, min_periods=max(1, w // 2)).sum()
    return pos / gross.replace(0, np.nan)


def _f24pi_loss_share(s, w):
    loss = (-s).clip(lower=0).rolling(w, min_periods=max(1, w // 2)).sum()
    gross = s.abs().rolling(w, min_periods=max(1, w // 2)).sum()
    return loss / gross.replace(0, np.nan)


def _f24pi_logclose(s, w):
    # log-repair of the |negative| gap toward zero over window w
    deficit = (-s).clip(lower=0)
    gap_now = deficit + 1.0
    gap_then = deficit.shift(w) + 1.0
    return np.log(gap_then / gap_now)


def _f24pi_cross_up(s):
    return ((s > 0) & (s.shift(1) <= 0)).astype(float)


def _f24pi_recency(s, span):
    pos = (s > 0).astype(float)
    return pos.ewm(span=span, min_periods=max(5, span // 3)).mean()


def _f24pi_inflect(s, w):
    # second difference of signed-sqrt level: profitability curvature
    sm = _f24pi_signmag(s)
    d = sm.diff(w)
    return d - d.shift(w)


# ============================================================
# --- netinc facets (file 2) ---

# net-income magnitude-weighted profit share over a half-year (profit dominance)
def f24pi_f24_profitability_inflection_niprofitshare_126d_base_v076_signal(netinc):
    b = _f24pi_pos_share(netinc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income log-loss-narrowing over a quarter (loss gap closing toward zero)
def f24pi_f24_profitability_inflection_nilogclose_63d_base_v077_signal(netinc):
    b = _f24pi_logclose(netinc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income profitability curvature (is the climb accelerating)
def f24pi_f24_profitability_inflection_niinflect_63d_base_v078_signal(netinc):
    b = _f24pi_inflect(netinc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income EW profit recency (fast) minus slow recency (regime shift)
def f24pi_f24_profitability_inflection_nirecencyspread_base_v079_signal(netinc):
    fast = _f24pi_recency(netinc, 42)
    slow = _f24pi_recency(netinc, 168)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income breakeven proximity: signed inverse-distance to zero (inflection zone)
def f24pi_f24_profitability_inflection_nibreakprox_252d_base_v080_signal(netinc):
    scale = netinc.abs().rolling(252, min_periods=126).median()
    b = np.tanh(netinc / scale.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income half-year slope normalized by year-vol (risk-adjusted profit climb)
def f24pi_f24_profitability_inflection_nislopevol_126d_base_v081_signal(netinc):
    sl = _slope(netinc, 126)
    vol = _std(netinc, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ebit facets ---

# ebit magnitude-weighted operating-profit share over a half-year
def f24pi_f24_profitability_inflection_ebitprofitshare_126d_base_v082_signal(ebit):
    b = _f24pi_pos_share(ebit, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit log-loss-narrowing over a quarter
def f24pi_f24_profitability_inflection_ebitlogclose_63d_base_v083_signal(ebit):
    b = _f24pi_logclose(ebit, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit operating-profit curvature (acceleration of operating climb)
def f24pi_f24_profitability_inflection_ebitinflect_63d_base_v084_signal(ebit):
    b = _f24pi_inflect(ebit, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit recency spread (fast vs slow operating-profit prevalence)
def f24pi_f24_profitability_inflection_ebitrecencyspread_base_v085_signal(ebit):
    fast = _f24pi_recency(ebit, 42)
    slow = _f24pi_recency(ebit, 168)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit breakeven proximity (tanh of operating profit vs own median scale)
def f24pi_f24_profitability_inflection_ebitbreakprox_252d_base_v086_signal(ebit):
    scale = ebit.abs().rolling(252, min_periods=126).median()
    b = np.tanh(ebit / scale.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit slope normalized by year-vol
def f24pi_f24_profitability_inflection_ebitslopevol_126d_base_v087_signal(ebit):
    sl = _slope(ebit, 126)
    vol = _std(ebit, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- opinc facets ---

# opinc magnitude-weighted profit share over a half-year
def f24pi_f24_profitability_inflection_opincprofitshare_126d_base_v088_signal(opinc):
    b = _f24pi_pos_share(opinc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc log-loss-narrowing over a quarter
def f24pi_f24_profitability_inflection_opinclogclose_63d_base_v089_signal(opinc):
    b = _f24pi_logclose(opinc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc curvature (acceleration of operating-income path)
def f24pi_f24_profitability_inflection_opincinflect_63d_base_v090_signal(opinc):
    b = _f24pi_inflect(opinc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc breakeven proximity
def f24pi_f24_profitability_inflection_opincbreakprox_252d_base_v091_signal(opinc):
    scale = opinc.abs().rolling(252, min_periods=126).median()
    b = np.tanh(opinc / scale.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc slope normalized by year-vol
def f24pi_f24_profitability_inflection_opincslopevol_126d_base_v092_signal(opinc):
    sl = _slope(opinc, 126)
    vol = _std(opinc, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ncfo facets ---

# ncfo magnitude-weighted cash-generation share over a half-year
def f24pi_f24_profitability_inflection_ncfogenshare_126d_base_v093_signal(ncfo):
    b = _f24pi_pos_share(ncfo, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo log-burn-narrowing over a quarter (cash burn closing toward zero)
def f24pi_f24_profitability_inflection_ncfologclose_63d_base_v094_signal(ncfo):
    b = _f24pi_logclose(ncfo, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo cash-flow curvature
def f24pi_f24_profitability_inflection_ncfoinflect_63d_base_v095_signal(ncfo):
    b = _f24pi_inflect(ncfo, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo recency spread (fast vs slow cash-generation prevalence)
def f24pi_f24_profitability_inflection_ncforecencyspread_base_v096_signal(ncfo):
    fast = _f24pi_recency(ncfo, 42)
    slow = _f24pi_recency(ncfo, 168)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo breakeven proximity
def f24pi_f24_profitability_inflection_ncfobreakprox_252d_base_v097_signal(ncfo):
    scale = ncfo.abs().rolling(252, min_periods=126).median()
    b = np.tanh(ncfo / scale.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo slope normalized by year-vol
def f24pi_f24_profitability_inflection_ncfoslopevol_126d_base_v098_signal(ncfo):
    sl = _slope(ncfo, 126)
    vol = _std(ncfo, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- eps facets ---

# eps upside/downside semivariance ratio over a half-year (per-share earnings asymmetry)
def f24pi_f24_profitability_inflection_epssemiratio_126d_base_v099_signal(eps):
    dev = eps - eps.rolling(126, min_periods=63).mean()
    up = dev.clip(lower=0).pow(2).rolling(126, min_periods=63).mean()
    dn = dev.clip(upper=0).pow(2).rolling(126, min_periods=63).mean()
    b = up / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps log-loss-narrowing over a quarter
def f24pi_f24_profitability_inflection_epslogclose_63d_base_v100_signal(eps):
    b = _f24pi_logclose(eps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps inflection curvature (per-share earnings acceleration)
def f24pi_f24_profitability_inflection_epsinflect_63d_base_v101_signal(eps):
    b = _f24pi_inflect(eps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps recency spread (fast vs slow positive-eps prevalence)
def f24pi_f24_profitability_inflection_epsrecencyspread_base_v102_signal(eps):
    fast = _f24pi_recency(eps, 42)
    slow = _f24pi_recency(eps, 168)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps in-window percentile rank (where current per-share earnings sit vs own year)
def f24pi_f24_profitability_inflection_epsqrank_252d_base_v103_signal(eps):
    b = eps.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share dilution wedge: eps year-rank minus netinc year-rank (per-share vs aggregate)
def f24pi_f24_profitability_inflection_epsVniwedge_252d_base_v104_signal(eps, netinc):
    re = eps.rolling(252, min_periods=126).rank(pct=True)
    rn = netinc.rolling(252, min_periods=126).rank(pct=True)
    b = re - rn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- retearn facets ---

# retained-earnings monotonicity: net signed-step share weighted by step magnitude
def f24pi_f24_profitability_inflection_retmonotone_252d_base_v105_signal(retearn):
    d = retearn.diff()
    up = (d > 0).astype(float).rolling(252, min_periods=126).mean()
    dn = (d < 0).astype(float).rolling(252, min_periods=126).mean()
    netstep = d.rolling(252, min_periods=126).sum()
    gross = d.abs().rolling(252, min_periods=126).sum()
    b = (up - dn) + netstep / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn deficit log-close over a year (accumulated-deficit repair pace)
def f24pi_f24_profitability_inflection_retlogclose_252d_base_v106_signal(retearn):
    b = _f24pi_logclose(retearn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn trajectory curvature (is deficit-repair accelerating)
def f24pi_f24_profitability_inflection_retinflect_126d_base_v107_signal(retearn):
    b = _f24pi_inflect(retearn, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn slope normalized by its own two-year vol
def f24pi_f24_profitability_inflection_retslopevol_252d_base_v108_signal(retearn):
    sl = _slope(retearn, 252)
    vol = _std(retearn, 504)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn breakeven proximity (distance of accumulated earnings to zero)
def f24pi_f24_profitability_inflection_retbreakprox_504d_base_v109_signal(retearn):
    scale = retearn.abs().rolling(504, min_periods=252).median()
    b = np.tanh(retearn / scale.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-metric facets ---

# accrual-vs-cash profit-share gap (netinc vs ncfo magnitude-weighted profit share)
def f24pi_f24_profitability_inflection_niVncfoshare_126d_base_v110_signal(netinc, ncfo):
    a = _f24pi_pos_share(netinc, 126)
    c = _f24pi_pos_share(ncfo, 126)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# below-the-line drag: ebit profit share minus netinc profit share
def f24pi_f24_profitability_inflection_ebitVnishare_126d_base_v111_signal(ebit, netinc):
    a = _f24pi_pos_share(ebit, 126)
    c = _f24pi_pos_share(netinc, 126)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating vs reported climb: opinc slope minus netinc slope (scaled)
def f24pi_f24_profitability_inflection_opincVnislope_126d_base_v112_signal(opinc, netinc):
    so = _slope(opinc, 126) / opinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    sn = _slope(netinc, 126) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = so - sn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-earnings inflection agreement: do ncfo and netinc curvatures agree in sign
def f24pi_f24_profitability_inflection_niNcfoinflectagree_base_v113_signal(netinc, ncfo):
    ci = _f24pi_inflect(netinc, 63)
    cc = _f24pi_inflect(ncfo, 63)
    agree = (np.sign(ci) == np.sign(cc)).astype(float)
    b = agree.rolling(126, min_periods=63).mean() - 0.5 + 0.1 * np.tanh(ci + cc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite path-to-profit climb: avg of scaled slopes across ni/ebit/opinc/ncfo
def f24pi_f24_profitability_inflection_compositeclimb_126d_base_v114_signal(netinc, ebit, opinc, ncfo):
    def sc(s):
        return _slope(s, 126) / s.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = (sc(netinc) + sc(ebit) + sc(opinc) + sc(ncfo)) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# profit-share dispersion across ni/ebit/opinc/ncfo (consistency of profitability)
def f24pi_f24_profitability_inflection_sharedispersion_126d_base_v115_signal(netinc, ebit, opinc, ncfo):
    a = _f24pi_pos_share(netinc, 126)
    c = _f24pi_pos_share(ebit, 126)
    d = _f24pi_pos_share(opinc, 126)
    e = _f24pi_pos_share(ncfo, 126)
    b = pd.concat([a, c, d, e], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps-vs-netinc climb divergence (per-share dilution-adjusted inflection gap)
def f24pi_f24_profitability_inflection_epsVniclimb_126d_base_v116_signal(eps, netinc):
    se = _slope(eps, 126) / eps.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    sn = _slope(netinc, 126) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = se - sn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net profit relative to accumulated deficit repair (current vs legacy interplay)
def f24pi_f24_profitability_inflection_niVretrepair_base_v117_signal(netinc, retearn):
    repair = _f24pi_logclose(retearn, 126)
    ni_sm = _f24pi_signmag(netinc)
    ni_tilt = ni_sm / ni_sm.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = np.tanh(ni_tilt) + np.tanh(5.0 * repair)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional distinct facets to fill out 150 ---

# net-income first-crossing maturity: cross-up count blended with profit-share level
def f24pi_f24_profitability_inflection_nicrossmature_252d_base_v118_signal(netinc):
    cnt = _f24pi_cross_up(netinc).rolling(252, min_periods=126).sum()
    share = _f24pi_pos_share(netinc, 252)
    b = cnt * 0.5 + share
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit profit-share trend (is operating-profit dominance improving over a quarter)
def f24pi_f24_profitability_inflection_ebitsharetrend_126d_base_v119_signal(ebit):
    sh = _f24pi_pos_share(ebit, 126)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc rank-position momentum: change over a quarter in where opinc ranks in its own year
def f24pi_f24_profitability_inflection_opincrankmom_252d_base_v120_signal(opinc):
    r = opinc.rolling(252, min_periods=126).rank(pct=True)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo rank-position momentum: quarter-change in cash-flow's percentile rank within its year
def f24pi_f24_profitability_inflection_ncforankmom_252d_base_v121_signal(ncfo):
    r = ncfo.rolling(252, min_periods=126).rank(pct=True)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps profit-share trend
def f24pi_f24_profitability_inflection_epssharetrend_126d_base_v122_signal(eps):
    sh = _f24pi_pos_share(eps, 126)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income level momentum: signed-sqrt net income now vs a half-year ago
def f24pi_f24_profitability_inflection_nilevelmom_126d_base_v123_signal(netinc):
    sm = _f24pi_signmag(netinc)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit level momentum: signed-sqrt ebit now vs a half-year ago
def f24pi_f24_profitability_inflection_ebitlevelmom_126d_base_v124_signal(ebit):
    sm = _f24pi_signmag(ebit)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps level momentum: signed-sqrt eps now vs a half-year ago
def f24pi_f24_profitability_inflection_epslevelmom_126d_base_v125_signal(eps):
    sm = _f24pi_signmag(eps)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income worst-loss relief: how far the trailing max net loss has receded
def f24pi_f24_profitability_inflection_niworstlossrelief_base_v126_signal(netinc):
    depth = (-netinc).clip(lower=0)
    worst = depth.rolling(252, min_periods=126).max()
    cur = depth.rolling(21, min_periods=10).mean()
    b = 1.0 - cur / worst.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit worst-loss relief: how far the trailing max operating-loss has receded
def f24pi_f24_profitability_inflection_ebitworstlossrelief_base_v127_signal(ebit):
    depth = (-ebit).clip(lower=0)
    worst = depth.rolling(252, min_periods=126).max()
    cur = depth.rolling(21, min_periods=10).mean()
    b = 1.0 - cur / worst.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo downside deviation: typical below-median shortfall of cash flow, own-scaled
def f24pi_f24_profitability_inflection_ncfodowndev_252d_base_v128_signal(ncfo):
    sm = _f24pi_signmag(ncfo)
    med = sm.rolling(252, min_periods=126).median()
    short = (sm - med).clip(upper=0)
    dd = short.pow(2).rolling(252, min_periods=126).mean().pow(0.5)
    scale = sm.abs().rolling(252, min_periods=126).mean()
    b = dd / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income profit-depth widening (avg profit magnitude growing over a half-year)
def f24pi_f24_profitability_inflection_niprofitdepthgrow_base_v129_signal(netinc):
    depth = netinc.clip(lower=0)
    sm = np.sqrt(depth)
    avg = sm.rolling(126, min_periods=63).mean()
    b = avg - avg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps profit-depth widening
def f24pi_f24_profitability_inflection_epsprofitdepthgrow_base_v130_signal(eps):
    depth = eps.clip(lower=0)
    sm = np.sqrt(depth)
    avg = sm.rolling(126, min_periods=63).mean()
    b = avg - avg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income vs ebit breakeven-proximity spread (which line is closer to flipping)
def f24pi_f24_profitability_inflection_niVebitprox_252d_base_v131_signal(netinc, ebit):
    sn = netinc.abs().rolling(252, min_periods=126).median()
    se = ebit.abs().rolling(252, min_periods=126).median()
    pn = np.tanh(netinc / sn.replace(0, np.nan))
    pe = np.tanh(ebit / se.replace(0, np.nan))
    b = pn - pe
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo vs opinc cash-backing breakeven spread
def f24pi_f24_profitability_inflection_ncfoVopincprox_252d_base_v132_signal(ncfo, opinc):
    sn = ncfo.abs().rolling(252, min_periods=126).median()
    so = opinc.abs().rolling(252, min_periods=126).median()
    pn = np.tanh(ncfo / sn.replace(0, np.nan))
    po = np.tanh(opinc / so.replace(0, np.nan))
    b = pn - po
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite breakeven proximity: mean tanh across the four profit lines
def f24pi_f24_profitability_inflection_compositeprox_252d_base_v133_signal(netinc, ebit, opinc, ncfo):
    def tp(s):
        sc = s.abs().rolling(252, min_periods=126).median()
        return np.tanh(s / sc.replace(0, np.nan))
    b = (tp(netinc) + tp(ebit) + tp(opinc) + tp(ncfo)) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income curvature over a half-year (slow acceleration of profit)
def f24pi_f24_profitability_inflection_niinflect_126d_base_v134_signal(netinc):
    b = _f24pi_inflect(netinc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps curvature over a half-year
def f24pi_f24_profitability_inflection_epsinflect_126d_base_v135_signal(eps):
    b = _f24pi_inflect(eps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo regime entropy: how mixed positive/negative cash quarters are over the year
def f24pi_f24_profitability_inflection_ncforegimeentropy_252d_base_v136_signal(ncfo):
    p = (ncfo > 0).astype(float).rolling(252, min_periods=126).mean()
    pc = p.clip(1e-6, 1.0 - 1e-6)
    b = -(pc * np.log(pc) + (1.0 - pc) * np.log(1.0 - pc))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit cross-up maturity (operating return-to-profit density + share level)
def f24pi_f24_profitability_inflection_ebitcrossmature_252d_base_v137_signal(ebit):
    cnt = _f24pi_cross_up(ebit).rolling(252, min_periods=126).sum()
    share = _f24pi_pos_share(ebit, 252)
    b = cnt * 0.5 + share
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps turning-point density: frequency of local direction reversals over the year
def f24pi_f24_profitability_inflection_epsturnpoint_252d_base_v138_signal(eps):
    d = eps.diff()
    turn = ((np.sign(d) != np.sign(d.shift(1))) & (d != 0) & (d.shift(1) != 0)).astype(float)
    b = turn.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income profit-share acceleration (second difference of the profit share)
def f24pi_f24_profitability_inflection_nishareaccel_126d_base_v139_signal(netinc):
    sh = _f24pi_pos_share(netinc, 126)
    d = sh.diff(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo cash-share acceleration
def f24pi_f24_profitability_inflection_ncfoshareaccel_126d_base_v140_signal(ncfo):
    sh = _f24pi_pos_share(ncfo, 126)
    d = sh.diff(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn surplus-share trend (accumulated surplus dominance improving)
def f24pi_f24_profitability_inflection_retsurpltrend_252d_base_v141_signal(retearn):
    sh = _f24pi_pos_share(retearn, 252)
    b = sh - sh.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retearn surplus-share acceleration (second difference of accumulated-surplus share)
def f24pi_f24_profitability_inflection_retsurplaccel_base_v142_signal(retearn):
    sh = _f24pi_pos_share(retearn, 252)
    d = sh.diff(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income relative climb vs cash climb (accrual-vs-cash inflection momentum)
def f24pi_f24_profitability_inflection_niVncfoclimb_126d_base_v143_signal(netinc, ncfo):
    sn = _slope(netinc, 126) / netinc.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    sc = _slope(ncfo, 126) / ncfo.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = sn - sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating profitability ladder: opinc share minus ebit share minus netinc share
def f24pi_f24_profitability_inflection_profitladder_126d_base_v144_signal(opinc, ebit, netinc):
    a = _f24pi_pos_share(opinc, 126)
    c = _f24pi_pos_share(ebit, 126)
    d = _f24pi_pos_share(netinc, 126)
    b = a - 0.5 * c - 0.5 * d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps short-horizon autocorrelation: persistence of per-share earnings changes
def f24pi_f24_profitability_inflection_epsautocorr_252d_base_v145_signal(eps):
    d = eps.diff()
    dl = d.shift(1)
    md = d.rolling(252, min_periods=126).mean()
    cov = ((d - md) * (dl - md)).rolling(252, min_periods=126).mean()
    var = ((d - md) ** 2).rolling(252, min_periods=126).mean()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# netinc breakeven-proximity momentum
def f24pi_f24_profitability_inflection_niproxmom_252d_base_v146_signal(netinc):
    scale = netinc.abs().rolling(252, min_periods=126).median()
    prox = np.tanh(netinc / scale.replace(0, np.nan))
    b = prox - prox.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo range compression: recent-quarter cash-flow span vs the full-year span
def f24pi_f24_profitability_inflection_ncforangecompress_252d_base_v147_signal(ncfo):
    r63 = ncfo.rolling(63, min_periods=21).max() - ncfo.rolling(63, min_periods=21).min()
    r252 = ncfo.rolling(252, min_periods=126).max() - ncfo.rolling(252, min_periods=126).min()
    b = r63 / r252.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit distribution kurtosis over the year (tail-heaviness of operating-profit prints)
def f24pi_f24_profitability_inflection_ebitkurt_252d_base_v148_signal(ebit):
    b = ebit.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# four-line profit recency average (consensus path-to-profit prevalence)
def f24pi_f24_profitability_inflection_consensusrecency_base_v149_signal(netinc, ebit, opinc, ncfo):
    b = (_f24pi_recency(netinc, 63) + _f24pi_recency(ebit, 63)
         + _f24pi_recency(opinc, 63) + _f24pi_recency(ncfo, 63)) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-profit composite: profit-share level minus loss-share, blended w/ retearn surplus
def f24pi_f24_profitability_inflection_durableprofit_base_v150_signal(netinc, ncfo, retearn):
    ni_net = _f24pi_pos_share(netinc, 252) - _f24pi_loss_share(netinc, 252)
    cf_net = _f24pi_pos_share(ncfo, 252) - _f24pi_loss_share(ncfo, 252)
    surpl = (retearn > 0).astype(float).rolling(252, min_periods=126).mean()
    b = 0.4 * ni_net + 0.4 * cf_net + 0.2 * (surpl - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24pi_f24_profitability_inflection_niprofitshare_126d_base_v076_signal,
    f24pi_f24_profitability_inflection_nilogclose_63d_base_v077_signal,
    f24pi_f24_profitability_inflection_niinflect_63d_base_v078_signal,
    f24pi_f24_profitability_inflection_nirecencyspread_base_v079_signal,
    f24pi_f24_profitability_inflection_nibreakprox_252d_base_v080_signal,
    f24pi_f24_profitability_inflection_nislopevol_126d_base_v081_signal,
    f24pi_f24_profitability_inflection_ebitprofitshare_126d_base_v082_signal,
    f24pi_f24_profitability_inflection_ebitlogclose_63d_base_v083_signal,
    f24pi_f24_profitability_inflection_ebitinflect_63d_base_v084_signal,
    f24pi_f24_profitability_inflection_ebitrecencyspread_base_v085_signal,
    f24pi_f24_profitability_inflection_ebitbreakprox_252d_base_v086_signal,
    f24pi_f24_profitability_inflection_ebitslopevol_126d_base_v087_signal,
    f24pi_f24_profitability_inflection_opincprofitshare_126d_base_v088_signal,
    f24pi_f24_profitability_inflection_opinclogclose_63d_base_v089_signal,
    f24pi_f24_profitability_inflection_opincinflect_63d_base_v090_signal,
    f24pi_f24_profitability_inflection_opincbreakprox_252d_base_v091_signal,
    f24pi_f24_profitability_inflection_opincslopevol_126d_base_v092_signal,
    f24pi_f24_profitability_inflection_ncfogenshare_126d_base_v093_signal,
    f24pi_f24_profitability_inflection_ncfologclose_63d_base_v094_signal,
    f24pi_f24_profitability_inflection_ncfoinflect_63d_base_v095_signal,
    f24pi_f24_profitability_inflection_ncforecencyspread_base_v096_signal,
    f24pi_f24_profitability_inflection_ncfobreakprox_252d_base_v097_signal,
    f24pi_f24_profitability_inflection_ncfoslopevol_126d_base_v098_signal,
    f24pi_f24_profitability_inflection_epssemiratio_126d_base_v099_signal,
    f24pi_f24_profitability_inflection_epslogclose_63d_base_v100_signal,
    f24pi_f24_profitability_inflection_epsinflect_63d_base_v101_signal,
    f24pi_f24_profitability_inflection_epsrecencyspread_base_v102_signal,
    f24pi_f24_profitability_inflection_epsqrank_252d_base_v103_signal,
    f24pi_f24_profitability_inflection_epsVniwedge_252d_base_v104_signal,
    f24pi_f24_profitability_inflection_retmonotone_252d_base_v105_signal,
    f24pi_f24_profitability_inflection_retlogclose_252d_base_v106_signal,
    f24pi_f24_profitability_inflection_retinflect_126d_base_v107_signal,
    f24pi_f24_profitability_inflection_retslopevol_252d_base_v108_signal,
    f24pi_f24_profitability_inflection_retbreakprox_504d_base_v109_signal,
    f24pi_f24_profitability_inflection_niVncfoshare_126d_base_v110_signal,
    f24pi_f24_profitability_inflection_ebitVnishare_126d_base_v111_signal,
    f24pi_f24_profitability_inflection_opincVnislope_126d_base_v112_signal,
    f24pi_f24_profitability_inflection_niNcfoinflectagree_base_v113_signal,
    f24pi_f24_profitability_inflection_compositeclimb_126d_base_v114_signal,
    f24pi_f24_profitability_inflection_sharedispersion_126d_base_v115_signal,
    f24pi_f24_profitability_inflection_epsVniclimb_126d_base_v116_signal,
    f24pi_f24_profitability_inflection_niVretrepair_base_v117_signal,
    f24pi_f24_profitability_inflection_nicrossmature_252d_base_v118_signal,
    f24pi_f24_profitability_inflection_ebitsharetrend_126d_base_v119_signal,
    f24pi_f24_profitability_inflection_opincrankmom_252d_base_v120_signal,
    f24pi_f24_profitability_inflection_ncforankmom_252d_base_v121_signal,
    f24pi_f24_profitability_inflection_epssharetrend_126d_base_v122_signal,
    f24pi_f24_profitability_inflection_nilevelmom_126d_base_v123_signal,
    f24pi_f24_profitability_inflection_ebitlevelmom_126d_base_v124_signal,
    f24pi_f24_profitability_inflection_epslevelmom_126d_base_v125_signal,
    f24pi_f24_profitability_inflection_niworstlossrelief_base_v126_signal,
    f24pi_f24_profitability_inflection_ebitworstlossrelief_base_v127_signal,
    f24pi_f24_profitability_inflection_ncfodowndev_252d_base_v128_signal,
    f24pi_f24_profitability_inflection_niprofitdepthgrow_base_v129_signal,
    f24pi_f24_profitability_inflection_epsprofitdepthgrow_base_v130_signal,
    f24pi_f24_profitability_inflection_niVebitprox_252d_base_v131_signal,
    f24pi_f24_profitability_inflection_ncfoVopincprox_252d_base_v132_signal,
    f24pi_f24_profitability_inflection_compositeprox_252d_base_v133_signal,
    f24pi_f24_profitability_inflection_niinflect_126d_base_v134_signal,
    f24pi_f24_profitability_inflection_epsinflect_126d_base_v135_signal,
    f24pi_f24_profitability_inflection_ncforegimeentropy_252d_base_v136_signal,
    f24pi_f24_profitability_inflection_ebitcrossmature_252d_base_v137_signal,
    f24pi_f24_profitability_inflection_epsturnpoint_252d_base_v138_signal,
    f24pi_f24_profitability_inflection_nishareaccel_126d_base_v139_signal,
    f24pi_f24_profitability_inflection_ncfoshareaccel_126d_base_v140_signal,
    f24pi_f24_profitability_inflection_retsurpltrend_252d_base_v141_signal,
    f24pi_f24_profitability_inflection_retsurplaccel_base_v142_signal,
    f24pi_f24_profitability_inflection_niVncfoclimb_126d_base_v143_signal,
    f24pi_f24_profitability_inflection_profitladder_126d_base_v144_signal,
    f24pi_f24_profitability_inflection_epsautocorr_252d_base_v145_signal,
    f24pi_f24_profitability_inflection_niproxmom_252d_base_v146_signal,
    f24pi_f24_profitability_inflection_ncforangecompress_252d_base_v147_signal,
    f24pi_f24_profitability_inflection_ebitkurt_252d_base_v148_signal,
    f24pi_f24_profitability_inflection_consensusrecency_base_v149_signal,
    f24pi_f24_profitability_inflection_durableprofit_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_PROFITABILITY_INFLECTION_REGISTRY_076_150 = REGISTRY


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

    def _swing(seed, base, amp, per, allow_neg=True):
        core = _fund(seed, base=base, drift=0.0, vol=0.10, allow_neg=allow_neg)
        g = np.random.default_rng(seed + 7000)
        t = np.arange(n, dtype=float)
        osc = np.sin(2.0 * np.pi * t / per + g.uniform(0, 6.28))
        noise = g.normal(0.0, 0.35, n)
        return pd.Series(core.values - base * 0.6 + amp * base * (osc + noise))

    netinc = _swing(101, base=8e7, amp=0.9, per=180).rename("netinc")
    ebit = _swing(102, base=9e7, amp=0.85, per=150).rename("ebit")
    opinc = _swing(103, base=9e7, amp=0.8, per=210).rename("opinc")
    ncfo = _swing(104, base=7e7, amp=1.0, per=130).rename("ncfo")
    eps = _swing(105, base=1.5, amp=0.95, per=160).rename("eps")
    retearn = _swing(106, base=2e8, amp=0.7, per=320).rename("retearn")

    cols = {"netinc": netinc, "ebit": ebit, "opinc": opinc, "ncfo": ncfo,
            "eps": eps, "retearn": retearn}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
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

    print("OK f24_profitability_inflection_base_076_150_claude: %d features pass" % n_features)
