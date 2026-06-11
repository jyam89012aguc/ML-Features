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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # ordinary-least-squares slope over a rolling window
    x = np.arange(w)
    xm = x.mean()
    denom = ((x - xm) ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return ((x - xm) * (a - a.mean())).sum() / denom
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (cash burn / runway) =====
def _f31_burn_opex(opex, ncfo):
    return (opex - ncfo).clip(lower=0)


def _f31_burn_fcf(ncfo, capex):
    return (-ncfo - capex).clip(lower=0)


def _f31_runway_opex(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    return cashneq / burn.replace(0, np.nan) * 12.0


def _f31_runway_fcf(cashneq, ncfo, capex):
    burn = _f31_burn_fcf(ncfo, capex)
    return cashneq / burn.replace(0, np.nan) * 12.0


def _f31_coverage(ncfo, opex):
    return ncfo / opex.replace(0, np.nan)


def _f31_logwarp(s):
    return np.sign(s) * np.log1p(s.abs())


# ============================================================
# --- alternate-window runway levels ---
# opex-runway level over a half-year window
def f31cr_f31_cash_burn_runway_runway126_126d_base_v076_signal(cashneq, opex, ncfo):
    b = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    result = b.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-runway level smoothed over a year
def f31cr_f31_cash_burn_runway_runwayfcf126_base_v077_signal(cashneq, ncfo, capex):
    b = _f31_runway_fcf(cashneq, ncfo, capex).clip(upper=120.0)
    result = b.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# harmonic-mean-style blended runway (penalizes whichever burn is worse)
def f31cr_f31_cash_burn_runway_runwayblend_252d_base_v078_signal(cashneq, opex, ncfo, capex):
    ro = _f31_runway_opex(cashneq, opex, ncfo).clip(1, 120)
    rf = _f31_runway_fcf(cashneq, ncfo, capex).clip(1, 120)
    blend = 2.0 / (1.0 / ro + 1.0 / rf)
    result = _mean(blend, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- OLS slope of runway (trend strength, distinct from simple diff) ---
# 126d OLS slope of opex-runway (months per day deterioration/improvement)
def f31cr_f31_cash_burn_runway_runwayols_126d_base_v079_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    result = _slope(rw, 126) * 21.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d OLS slope of cash balance (log) — cash trajectory steepness
def f31cr_f31_cash_burn_runway_cashols_63d_base_v080_signal(cashneq):
    lc = np.log(cashneq.replace(0, np.nan))
    result = _slope(lc, 63) * 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d OLS slope of coverage (self-funding trend)
def f31cr_f31_cash_burn_runway_coverols_126d_base_v081_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    result = _slope(cov, 126) * 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn multiple style (cash burned per period vs cash) ---
# free-cash burn as a multiple of trailing-quarter average burn (spike detector)
def f31cr_f31_cash_burn_runway_burnspike_63d_base_v082_signal(ncfo, capex):
    burn = _f31_burn_fcf(ncfo, capex)
    avg = _mean(burn, 252)
    result = burn / avg.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# opex-burn spike vs trailing year average
def f31cr_f31_cash_burn_runway_burnspikeopx_base_v083_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    avg = _mean(burn, 252)
    result = burn / avg.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash adequacy vs burn run-rate (months) ranked differently ---
# stress-runway haircut: how much worst-case burn shortens runway vs current burn (ratio)
def f31cr_f31_cash_burn_runway_stressrunway_252d_base_v084_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    worst = _rmax(burn, 252)
    haircut = burn / worst.replace(0, np.nan)
    result = _mean(haircut, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# optimistic-runway uplift: best-case burn vs current burn (upside potential ratio)
def f31cr_f31_cash_burn_runway_optrunway_252d_base_v085_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    best = _rmin(burn, 252)
    uplift = best / burn.replace(0, np.nan)
    result = _rank(uplift, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# stress-vs-optimistic runway gap (sensitivity of runway to burn level)
def f31cr_f31_cash_burn_runway_runwaysens_252d_base_v086_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    worst = _rmax(burn, 252)
    best = _rmin(burn, 252)
    span = (worst - best) / _mean(burn, 252).replace(0, np.nan)
    result = _mean(span, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage regime durations / counts ---
# coverage interquartile spread over trailing year (range of self-funding outcomes)
def f31cr_f31_cash_burn_runway_halfcover_252d_base_v087_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    q75 = cov.rolling(252, min_periods=126).quantile(0.75)
    q25 = cov.rolling(252, min_periods=126).quantile(0.25)
    result = q75 - q25
    return result.replace([np.inf, -np.inf], np.nan)


# best coverage achieved in trailing year minus current (room to break-even)
def f31cr_f31_cash_burn_runway_coverroom_252d_base_v088_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    best = _rmax(cov, 252)
    result = best - cov
    return result.replace([np.inf, -np.inf], np.nan)


# how far current coverage sits above its trailing-year worst (resilience)
def f31cr_f31_cash_burn_runway_coverfloor_252d_base_v089_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    worst = _rmin(cov, 252)
    result = cov - worst
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash drawdown dynamics ---
# longest consecutive cash-decline streak (months) over the last year, normalized
def f31cr_f31_cash_burn_runway_cashdeclstreak_base_v090_signal(cashneq):
    down = (cashneq < cashneq.shift(1)).astype(float)
    grp = (down == 0).cumsum()
    streak = down.groupby(grp).cumcount() + 1
    streak = streak.where(down == 1, 0.0)
    result = streak.rolling(252, min_periods=126).max() / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash trough proximity: current cash vs its trailing 504d minimum
def f31cr_f31_cash_burn_runway_cashtrough_504d_base_v091_signal(cashneq):
    lo = _rmin(cashneq, 504)
    result = cashneq / lo.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# time since the trailing-year cash trough (staleness of the cash low)
def f31cr_f31_cash_burn_runway_cashrebuild_252d_base_v092_signal(cashneq):
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    result = cashneq.rolling(252, min_periods=126).apply(_dsl, raw=True)
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn composition (opex vs fcf burn mix) ---
# share of total burn that is capex-driven vs operating (investment intensity of drain)
def f31cr_f31_cash_burn_runway_capexshare_252d_base_v093_signal(opex, ncfo, capex):
    opburn = _f31_burn_opex(opex, ncfo)
    capx = capex.abs()
    result = _mean(capx / (opburn + capx).replace(0, np.nan), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex as a fraction of operating cash flow (reinvestment claim on cash gen)
def f31cr_f31_cash_burn_runway_capexocf_126d_base_v094_signal(capex, ncfo):
    result = _mean(capex.abs() / ncfo.abs().replace(0, np.nan), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth (content/platform spend trajectory)
def f31cr_f31_cash_burn_runway_capexgro_126d_base_v095_signal(capex):
    lc = np.log(capex.abs().replace(0, np.nan))
    result = lc - lc.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- financing-reliance facets (ncff) ---
# financing inflow as a share of total cash inflows (ncff vs ncfo magnitude)
def f31cr_f31_cash_burn_runway_finshare_252d_base_v096_signal(ncff, ncfo):
    pos_fin = ncff.clip(lower=0)
    pos_ops = ncfo.clip(lower=0)
    result = _mean(pos_fin / (pos_fin + pos_ops + 1.0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# financing volatility (lumpy capital raises)
def f31cr_f31_cash_burn_runway_finvol_252d_base_v097_signal(ncff):
    result = _std(_f31_logwarp(ncff), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year financing ran above its own trailing-year median (heavy-raise regime)
def f31cr_f31_cash_burn_runway_findays_252d_base_v098_signal(ncff):
    med = ncff.rolling(252, min_periods=126).median()
    heavy = (ncff > med).astype(float)
    result = heavy.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow trend (is the firm leaning more on external capital)
def f31cr_f31_cash_burn_runway_fintrend_126d_base_v099_signal(ncff):
    lw = _f31_logwarp(ncff)
    result = lw.ewm(span=63, min_periods=21).mean() - lw.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway-deterioration interaction features ---
# burn intensity rising while runway short (compounding-risk interaction)
def f31cr_f31_cash_burn_runway_compound_126d_base_v100_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    intens = burn / cashneq.replace(0, np.nan)
    rising = (intens - intens.shift(63)).clip(lower=0)
    rw = _f31_runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=1.0)).clip(upper=1.0)
    result = _mean(rising * short * 100.0, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# cash-decline x coverage-shortfall (draining and not self-funding)
def f31cr_f31_cash_burn_runway_drainfund_252d_base_v101_signal(cashneq, ncfo, opex):
    drain = (-(cashneq / cashneq.shift(63) - 1.0)).clip(lower=0)
    gap = (1.0 - _f31_coverage(ncfo, opex)).clip(lower=0)
    result = _mean(drain * gap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- log-level / sign-magnitude facets ---
# signed log of free-cash flow before capex netting (ncfo magnitude character)
def f31cr_f31_cash_burn_runway_ocflog_252d_base_v102_signal(ncfo):
    result = _mean(_f31_logwarp(ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage dispersion: rolling std of coverage (erratic self-funding magnitude)
def f31cr_f31_cash_burn_runway_coverwarp_252d_base_v103_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    sd = _std(cov, 126)
    result = _rank(sd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway z facets at alternate windows ---
# opex-runway z vs own 126d history (faster de-trend)
def f31cr_f31_cash_burn_runway_runwayz126_base_v104_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    result = _z(rw, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# cash balance z vs own 504d history (slow cash de-trend)
def f31cr_f31_cash_burn_runway_cashz504_base_v105_signal(cashneq):
    result = _z(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway acceleration / jerk-as-level ---
# coverage curvature: is coverage decline itself accelerating (level facet)
def f31cr_f31_cash_burn_runway_covercurv_base_v106_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    result = cov - 2.0 * cov.shift(63) + cov.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# burn intensity curvature (acceleration of the cash-drain rate)
def f31cr_f31_cash_burn_runway_burncurv_base_v107_signal(cashneq, opex, ncfo):
    intens = _f31_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    result = intens - 2.0 * intens.shift(63) + intens.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-window runway agreement ---
# multi-horizon runway-trend consensus, magnitude-weighted across 21/63/126 horizons
def f31cr_f31_cash_burn_runway_runwayagree_base_v108_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    r1 = (rw - rw.shift(21)) / 21.0
    r2 = (rw - rw.shift(63)) / 63.0
    r3 = (rw - rw.shift(126)) / 126.0
    consensus = (np.tanh(r1) + np.tanh(r2) + np.tanh(r3)) / 3.0
    result = consensus.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage breakeven distance smoothed and ranked ---
# distance to break-even coverage, percentile-ranked vs own 504d history
def f31cr_f31_cash_burn_runway_breakevenrank_base_v109_signal(ncfo, opex):
    dist = _f31_coverage(ncfo, opex) - 1.0
    result = _rank(dist, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# --- net cash flow (ops + financing) vs cash ---
# total external+internal cash generation relative to balance (net funding rate)
def f31cr_f31_cash_burn_runway_netfund_252d_base_v110_signal(cashneq, ncfo, ncff):
    netflow = ncfo + ncff
    result = _mean(netflow / (cashneq.abs() + 1.0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding ratio trend: change in operating-share-of-cash-sources over a year
def f31cr_f31_cash_burn_runway_selfratio_252d_base_v111_signal(ncfo, ncff):
    pos_ops = ncfo.clip(lower=0)
    total = pos_ops + ncff.clip(lower=0) + 1.0
    ratio = pos_ops / total
    result = ratio.ewm(span=63, min_periods=21).mean() - ratio.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway level normalized by burn volatility (quality of runway) ---
# runway divided by its own instability (high & stable runway scores best)
def f31cr_f31_cash_burn_runway_runwaystable_252d_base_v112_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    mn = _mean(rw, 252)
    sd = _std(rw, 252)
    result = mn / (sd + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# --- count of burn-acceleration episodes ---
# number of quarters in the last year where burn rose vs prior quarter (count)
def f31cr_f31_cash_burn_runway_burnupcount_base_v113_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    up = (burn > burn.shift(63)).astype(float)
    result = up.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash-vs-opex scale (size-of-cushion in operating-cost terms) ---
# months-of-opex cushion z-scored vs own 252d history (de-trended gross cushion)
def f31cr_f31_cash_burn_runway_cashopexmo_252d_base_v114_signal(cashneq, opex):
    months = (cashneq / opex.replace(0, np.nan) * 12.0).clip(upper=120.0)
    result = _z(months, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# change in months-of-opex cushion over a year (cushion erosion)
def f31cr_f31_cash_burn_runway_cushionyoy_base_v115_signal(cashneq, opex):
    months = cashneq / opex.replace(0, np.nan) * 12.0
    result = months - months.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage-weighted runway (combined survival quality, alt to file1 quality) ---
# runway scaled by how close coverage is to break-even (near-self-funding extends life)
def f31cr_f31_cash_burn_runway_covrunway_252d_base_v116_signal(cashneq, opex, ncfo):
    rw = np.log1p(_f31_runway_opex(cashneq, opex, ncfo).clip(lower=0, upper=120.0))
    prox = (1.0 - (1.0 - _f31_coverage(ncfo, opex)).clip(0, 1))
    result = _mean(rw * prox, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn per capex (operating drain relative to investment), ranked ---
# operating-burn to capex ratio percentile (survival-spend vs growth-spend balance)
def f31cr_f31_cash_burn_runway_burncapexrank_base_v117_signal(opex, ncfo, capex):
    ratio = _f31_burn_opex(opex, ncfo) / (capex.abs() + 1.0)
    result = _rank(np.log1p(ratio), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# --- financing-adjusted runway change ---
# change in financing-buffered months-of-cash over a half-year
def f31cr_f31_cash_burn_runway_bufrunwaychg_base_v118_signal(cashneq, ncff, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo).replace(0, np.nan)
    buffered = (cashneq + ncff.clip(lower=0)) / burn * 12.0
    buffered = buffered.clip(upper=240.0)
    result = buffered - buffered.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash drain volatility (erratic balance moves) ---
# volatility of quarter-over-quarter cash changes (unpredictable burn)
def f31cr_f31_cash_burn_runway_cashchgvol_252d_base_v119_signal(cashneq):
    chg = cashneq.pct_change(63)
    result = _std(chg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway floor breach severity ---
# deepest single-quarter runway drop in the last year (worst deterioration shock)
def f31cr_f31_cash_burn_runway_worstdrop_252d_base_v120_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    drop = (rw - rw.shift(63))
    result = drop.rolling(252, min_periods=126).min()
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage improvement durability ---
# fraction of last year coverage stayed above its own 252d median (durable funding)
def f31cr_f31_cash_burn_runway_coverdurable_base_v121_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    med = cov.rolling(252, min_periods=126).median()
    above = (cov > med).astype(float)
    result = above.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn magnitude relative to opex scale, smoothed ---
# operating-burn as a fraction of opex, slow-EMA (structural unprofitability)
def f31cr_f31_cash_burn_runway_burnopexfrac_base_v122_signal(opex, ncfo):
    frac = _f31_burn_opex(opex, ncfo) / opex.replace(0, np.nan)
    result = frac.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash sufficiency probability proxy (logit of runway) ---
# runway survival-probability momentum: change in logistic(runway-12) over a quarter
def f31cr_f31_cash_burn_runway_runwaylogit_base_v123_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    p = 1.0 / (1.0 + np.exp(-(rw - 12.0) / 6.0))
    sm = p.ewm(span=42, min_periods=21).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- free-cash burn coverage by cash, change facet ---
# change in cash-to-fcf-burn coverage over a half-year (deteriorating fcf cushion)
def f31cr_f31_cash_burn_runway_fcfcoverchg_base_v124_signal(cashneq, ncfo, capex):
    cov = cashneq / _f31_burn_fcf(ncfo, capex).replace(0, np.nan)
    cov = np.log1p(cov.clip(lower=0, upper=240.0))
    result = cov - cov.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway dispersion across burn definitions ---
# capex-drag widening: change in the (opex-runway minus fcf-runway) gap over a half-year
def f31cr_f31_cash_burn_runway_runwaydefdisp_base_v125_signal(cashneq, opex, ncfo, capex):
    ro = _f31_runway_opex(cashneq, opex, ncfo).clip(lower=1, upper=120.0)
    rf = _f31_runway_fcf(cashneq, ncfo, capex).clip(lower=0, upper=120.0)
    gap = (ro - rf).clip(upper=120.0)
    sm = gap.ewm(span=42, min_periods=21).mean()
    result = sm - sm.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash burn-down annual fraction ---
# fraction of cash consumed over the trailing year (annual burn-down rate)
def f31cr_f31_cash_burn_runway_burndown_252d_base_v126_signal(cashneq):
    prior = cashneq.shift(252)
    result = (prior - cashneq) / prior.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating-cash margin level (alt to coverage) ---
# ncfo-to-total-spend trend: change in cash-gen vs total outlay over a half-year
def f31cr_f31_cash_burn_runway_ocftotal_252d_base_v127_signal(ncfo, opex, capex):
    total = opex + capex.abs()
    ratio = ncfo / total.replace(0, np.nan)
    sm = ratio.ewm(span=63, min_periods=21).mean()
    result = sm - sm.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway trend stability (consistency of improvement) ---
# fraction of last year runway change was non-negative (steady-not-deteriorating)
def f31cr_f31_cash_burn_runway_runwaysteady_base_v128_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    stable = (rw >= rw.shift(21)).astype(float)
    result = stable.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- financing-to-burn coverage (lifeline adequacy) ---
# can financing inflows cover the operating burn? ratio capped, ranked
def f31cr_f31_cash_burn_runway_finadequacy_base_v129_signal(ncff, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    ratio = ncff.clip(lower=0) / (burn + 1.0)
    result = _rank(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# --- combined drain index ---
# net cash drain trend: change in (burn - financing)/cash drain rate over a half-year
def f31cr_f31_cash_burn_runway_netdrainrank_base_v130_signal(cashneq, opex, ncfo, ncff):
    net = _f31_burn_opex(opex, ncfo) - ncff.clip(lower=0)
    rate = net / (cashneq.abs() + 1.0)
    sm = rate.ewm(span=63, min_periods=21).mean()
    result = sm - sm.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway vs cash-cushion divergence ---
# burn-adjusted runway minus gross opex-cushion (how much burn shortens cash life)
def f31cr_f31_cash_burn_runway_runwaycushdiv_base_v131_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=240.0)
    cushion = (cashneq / opex.replace(0, np.nan) * 12.0).clip(upper=240.0)
    result = _mean((cushion - rw).clip(lower=0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- ncfo trough recovery momentum ---
# operating-cash improvement vs its trailing-year worst, smoothed (turnaround)
def f31cr_f31_cash_burn_runway_ocfturn_252d_base_v132_signal(ncfo):
    worst = _rmin(ncfo, 252)
    span = (_rmax(ncfo, 252) - worst).replace(0, np.nan)
    pos = (ncfo - worst) / span
    result = pos.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn intensity rank momentum ---
# change in burn-intensity percentile over a quarter (regime shift in drain rate)
def f31cr_f31_cash_burn_runway_burnrankmom_base_v133_signal(cashneq, opex, ncfo):
    intens = _f31_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    r = _rank(intens, 504)
    result = r - r.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage and cash co-movement (quality of cash generation) ---
# correlation-style sign product of ncfo-change and cash-change (cash tracks ops)
def f31cr_f31_cash_burn_runway_cashopslink_base_v134_signal(cashneq, ncfo):
    do = np.sign(ncfo - ncfo.shift(21))
    dc = np.sign(cashneq - cashneq.shift(21))
    result = (do * dc).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway half-life proxy ---
# runway decay rate: quarterly relative decline as a share of current runway (hazard proxy)
def f31cr_f31_cash_burn_runway_halflife_base_v135_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(lower=1, upper=120.0)
    decay = (rw.shift(63) - rw).clip(lower=0) / rw
    result = _mean(decay, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn seasonality / lumpiness ---
# max-minus-min burn within trailing year relative to mean (burn lumpiness)
def f31cr_f31_cash_burn_runway_burnlumpy_252d_base_v136_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    rng = _rmax(burn, 252) - _rmin(burn, 252)
    result = rng / _mean(burn, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash adequacy vs financing dependence interaction ---
# short runway AND high financing reliance (dilution-dependent survival flag)
def f31cr_f31_cash_burn_runway_dilutiondep_base_v137_signal(cashneq, opex, ncfo, ncff):
    rw = _f31_runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=2.0)).clip(upper=0.5)
    finrel = (ncff.clip(lower=0) / (cashneq.abs() + 1.0)).clip(upper=1.0)
    result = _mean(short * finrel * 10.0, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway percentile vs longer history ---
# opex-runway percentile vs own 252d history (medium-horizon rank)
def f31cr_f31_cash_burn_runway_runwayrank252_base_v138_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo)
    result = _rank(rw, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- operating burn acceleration sign streak ---
# consecutive quarters of worsening coverage (deterioration persistence)
def f31cr_f31_cash_burn_runway_coverworsen_base_v139_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    worse = (cov < cov.shift(21)).astype(float)
    grp = (worse == 0).cumsum()
    streak = worse.groupby(grp).cumcount() + 1
    streak = streak.where(worse == 1, 0.0)
    result = streak.rolling(252, min_periods=126).mean() / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash-flow self-sufficiency composite ---
# fully-self-funded streak: longest run of (ncfo>capex) months in last year, normalized
def f31cr_f31_cash_burn_runway_fullyfunded_base_v140_signal(ncfo, capex):
    funded = ((ncfo - capex.abs()) > 0).astype(float)
    grp = (funded == 0).cumsum()
    streak = funded.groupby(grp).cumcount() + 1
    streak = streak.where(funded == 1, 0.0)
    result = streak.rolling(252, min_periods=126).max() / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway momentum normalized by level (relative deterioration) ---
# quarterly runway change as a fraction of current runway (relative burn-down)
def f31cr_f31_cash_burn_runway_relrunwaychg_base_v141_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(lower=1, upper=120.0)
    result = (rw - rw.shift(63)) / rw
    return result.replace([np.inf, -np.inf], np.nan)


# --- financing burst detector ---
# financing-burst intensity: excess of financing above 1.25x its trailing median, smoothed
def f31cr_f31_cash_burn_runway_finburst_base_v142_signal(ncff):
    pos = ncff.clip(lower=0)
    med = pos.rolling(252, min_periods=126).median()
    excess = (pos - 1.25 * med).clip(lower=0) / (med + 1.0)
    result = excess.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash-runway in stress vs base, ratio ---
# stress runway (worst burn) as a fraction of base runway (downside sensitivity ratio)
def f31cr_f31_cash_burn_runway_stressratio_base_v143_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    base_rw = cashneq / _mean(burn, 252).replace(0, np.nan)
    stress_rw = cashneq / _rmax(burn, 252).replace(0, np.nan)
    result = _mean(stress_rw / base_rw.replace(0, np.nan), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage-zero crossings (profitability flicker) ---
# coverage sign-flip instability, magnitude-weighted by the size of each zero-crossing
def f31cr_f31_cash_burn_runway_coverflip_base_v144_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    sign = np.sign(cov)
    flip = (sign != sign.shift(1)).astype(float)
    weighted = flip * cov.abs()
    result = weighted.rolling(252, min_periods=126).sum() / (cov.abs().rolling(252, min_periods=126).mean() + 1e-9)
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn-adjusted cash growth (is cash outpacing burn) ---
# cash growth minus burn growth (is the cushion winning the race), smoothed
def f31cr_f31_cash_burn_runway_cashvsburn_base_v145_signal(cashneq, opex, ncfo):
    cg = np.log(cashneq.replace(0, np.nan) / cashneq.shift(126).replace(0, np.nan))
    burn = _f31_burn_opex(opex, ncfo)
    bg = np.log1p(burn) - np.log1p(burn.shift(126))
    result = (cg - bg).ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway entropy / regime persistence ---
# runway trend efficiency: net runway move over total path traveled (directional purity)
def f31cr_f31_cash_burn_runway_runwaypersist_base_v146_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    net = (rw - rw.shift(126)).abs()
    path = rw.diff().abs().rolling(126, min_periods=63).sum()
    result = net / path.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# --- capex-burn coverage by operating cash ---
# share of capex funded by operating cash flow (vs financed), smoothed
def f31cr_f31_cash_burn_runway_capexfunded_base_v147_signal(ncfo, capex):
    funded = (ncfo.clip(lower=0)) / (capex.abs() + 1.0)
    result = funded.ewm(span=63, min_periods=21).mean().clip(upper=10.0)
    return result.replace([np.inf, -np.inf], np.nan)


# --- net burn yoy acceleration ---
# year-over-year change in operating-burn-to-cash ratio (structural drain shift)
def f31cr_f31_cash_burn_runway_drainyoy_base_v148_signal(cashneq, opex, ncfo):
    rate = _f31_burn_opex(opex, ncfo) / (cashneq.abs() + 1.0)
    result = rate - rate.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway downside semi-deviation ---
# downside dispersion of runway changes (only deteriorations count)
def f31cr_f31_cash_burn_runway_runwaydownside_base_v149_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    chg = rw.diff()
    down = chg.where(chg < 0, 0.0)
    result = np.sqrt((down ** 2).rolling(252, min_periods=126).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite cash-life resilience score ---
# blend: high runway, positive coverage trend, low financing reliance (resilience)
def f31cr_f31_cash_burn_runway_resilience_base_v150_signal(cashneq, opex, ncfo, ncff):
    rw = np.log1p(_f31_runway_opex(cashneq, opex, ncfo).clip(lower=0, upper=120.0))
    cov_trend = (_f31_coverage(ncfo, opex) - _f31_coverage(ncfo, opex).shift(126))
    finrel = (ncff.clip(lower=0) / (cashneq.abs() + 1.0))
    raw = rw + 5.0 * cov_trend - 3.0 * finrel
    result = _mean(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31cr_f31_cash_burn_runway_runway126_126d_base_v076_signal,
    f31cr_f31_cash_burn_runway_runwayfcf126_base_v077_signal,
    f31cr_f31_cash_burn_runway_runwayblend_252d_base_v078_signal,
    f31cr_f31_cash_burn_runway_runwayols_126d_base_v079_signal,
    f31cr_f31_cash_burn_runway_cashols_63d_base_v080_signal,
    f31cr_f31_cash_burn_runway_coverols_126d_base_v081_signal,
    f31cr_f31_cash_burn_runway_burnspike_63d_base_v082_signal,
    f31cr_f31_cash_burn_runway_burnspikeopx_base_v083_signal,
    f31cr_f31_cash_burn_runway_stressrunway_252d_base_v084_signal,
    f31cr_f31_cash_burn_runway_optrunway_252d_base_v085_signal,
    f31cr_f31_cash_burn_runway_runwaysens_252d_base_v086_signal,
    f31cr_f31_cash_burn_runway_halfcover_252d_base_v087_signal,
    f31cr_f31_cash_burn_runway_coverroom_252d_base_v088_signal,
    f31cr_f31_cash_burn_runway_coverfloor_252d_base_v089_signal,
    f31cr_f31_cash_burn_runway_cashdeclstreak_base_v090_signal,
    f31cr_f31_cash_burn_runway_cashtrough_504d_base_v091_signal,
    f31cr_f31_cash_burn_runway_cashrebuild_252d_base_v092_signal,
    f31cr_f31_cash_burn_runway_capexshare_252d_base_v093_signal,
    f31cr_f31_cash_burn_runway_capexocf_126d_base_v094_signal,
    f31cr_f31_cash_burn_runway_capexgro_126d_base_v095_signal,
    f31cr_f31_cash_burn_runway_finshare_252d_base_v096_signal,
    f31cr_f31_cash_burn_runway_finvol_252d_base_v097_signal,
    f31cr_f31_cash_burn_runway_findays_252d_base_v098_signal,
    f31cr_f31_cash_burn_runway_fintrend_126d_base_v099_signal,
    f31cr_f31_cash_burn_runway_compound_126d_base_v100_signal,
    f31cr_f31_cash_burn_runway_drainfund_252d_base_v101_signal,
    f31cr_f31_cash_burn_runway_ocflog_252d_base_v102_signal,
    f31cr_f31_cash_burn_runway_coverwarp_252d_base_v103_signal,
    f31cr_f31_cash_burn_runway_runwayz126_base_v104_signal,
    f31cr_f31_cash_burn_runway_cashz504_base_v105_signal,
    f31cr_f31_cash_burn_runway_covercurv_base_v106_signal,
    f31cr_f31_cash_burn_runway_burncurv_base_v107_signal,
    f31cr_f31_cash_burn_runway_runwayagree_base_v108_signal,
    f31cr_f31_cash_burn_runway_breakevenrank_base_v109_signal,
    f31cr_f31_cash_burn_runway_netfund_252d_base_v110_signal,
    f31cr_f31_cash_burn_runway_selfratio_252d_base_v111_signal,
    f31cr_f31_cash_burn_runway_runwaystable_252d_base_v112_signal,
    f31cr_f31_cash_burn_runway_burnupcount_base_v113_signal,
    f31cr_f31_cash_burn_runway_cashopexmo_252d_base_v114_signal,
    f31cr_f31_cash_burn_runway_cushionyoy_base_v115_signal,
    f31cr_f31_cash_burn_runway_covrunway_252d_base_v116_signal,
    f31cr_f31_cash_burn_runway_burncapexrank_base_v117_signal,
    f31cr_f31_cash_burn_runway_bufrunwaychg_base_v118_signal,
    f31cr_f31_cash_burn_runway_cashchgvol_252d_base_v119_signal,
    f31cr_f31_cash_burn_runway_worstdrop_252d_base_v120_signal,
    f31cr_f31_cash_burn_runway_coverdurable_base_v121_signal,
    f31cr_f31_cash_burn_runway_burnopexfrac_base_v122_signal,
    f31cr_f31_cash_burn_runway_runwaylogit_base_v123_signal,
    f31cr_f31_cash_burn_runway_fcfcoverchg_base_v124_signal,
    f31cr_f31_cash_burn_runway_runwaydefdisp_base_v125_signal,
    f31cr_f31_cash_burn_runway_burndown_252d_base_v126_signal,
    f31cr_f31_cash_burn_runway_ocftotal_252d_base_v127_signal,
    f31cr_f31_cash_burn_runway_runwaysteady_base_v128_signal,
    f31cr_f31_cash_burn_runway_finadequacy_base_v129_signal,
    f31cr_f31_cash_burn_runway_netdrainrank_base_v130_signal,
    f31cr_f31_cash_burn_runway_runwaycushdiv_base_v131_signal,
    f31cr_f31_cash_burn_runway_ocfturn_252d_base_v132_signal,
    f31cr_f31_cash_burn_runway_burnrankmom_base_v133_signal,
    f31cr_f31_cash_burn_runway_cashopslink_base_v134_signal,
    f31cr_f31_cash_burn_runway_halflife_base_v135_signal,
    f31cr_f31_cash_burn_runway_burnlumpy_252d_base_v136_signal,
    f31cr_f31_cash_burn_runway_dilutiondep_base_v137_signal,
    f31cr_f31_cash_burn_runway_runwayrank252_base_v138_signal,
    f31cr_f31_cash_burn_runway_coverworsen_base_v139_signal,
    f31cr_f31_cash_burn_runway_fullyfunded_base_v140_signal,
    f31cr_f31_cash_burn_runway_relrunwaychg_base_v141_signal,
    f31cr_f31_cash_burn_runway_finburst_base_v142_signal,
    f31cr_f31_cash_burn_runway_stressratio_base_v143_signal,
    f31cr_f31_cash_burn_runway_coverflip_base_v144_signal,
    f31cr_f31_cash_burn_runway_cashvsburn_base_v145_signal,
    f31cr_f31_cash_burn_runway_runwaypersist_base_v146_signal,
    f31cr_f31_cash_burn_runway_capexfunded_base_v147_signal,
    f31cr_f31_cash_burn_runway_drainyoy_base_v148_signal,
    f31cr_f31_cash_burn_runway_runwaydownside_base_v149_signal,
    f31cr_f31_cash_burn_runway_resilience_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_CASH_BURN_RUNWAY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
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

    cashneq = _fund(101, base=2e8, drift=-0.02, vol=0.07).rename("cashneq")
    opex = _fund(102, base=1.0e8, drift=0.01, vol=0.06).rename("opex")
    capex = _fund(103, base=2e7, drift=0.02, vol=0.08).rename("capex")
    ncfo = _fund(104, base=1.6e8, drift=-0.13, vol=0.32, allow_neg=True).rename("ncfo")
    ncff = _fund(105, base=6e7, drift=0.01, vol=0.20, allow_neg=True).rename("ncff")

    cols = {"cashneq": cashneq, "opex": opex, "capex": capex,
            "ncfo": ncfo, "ncff": ncff}

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

    print("OK f31_cash_burn_runway_base_076_150_claude: %d features pass" % n_features)
