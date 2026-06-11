import inspect
import numpy as np
import pandas as pd

# ============================================================
# f47_debt_service_coverage  —  DEBT-SERVICE COVERAGE (flow burden)  [076-150]
# FUNDAMENTAL family. Every feature consumes >= 1 fundamental column from:
#   intexp, ebit, ebitda, ncfo, fcf, debt, debtc, debtnc, cashneq, prefdivis
# Flow/service-burden axis via interest expense. Distinct from debt-STOCK families.
# ============================================================

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
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _med(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).median()


# ===== folder domain primitives (debt-service / interest coverage) =====
def _f47_int_cov_ebit(ebit, intexp):
    return ebit / intexp.replace(0, np.nan)


def _f47_int_cov_ebitda(ebitda, intexp):
    return ebitda / intexp.replace(0, np.nan)


def _f47_cash_cov_ncfo(ncfo, intexp):
    return ncfo / intexp.replace(0, np.nan)


def _f47_cash_cov_fcf(fcf, intexp):
    return fcf / intexp.replace(0, np.nan)


def _f47_cost_of_debt(intexp, debt):
    return intexp / debt.replace(0, np.nan)


def _f47_maturity_wall(debtc, cashneq, fcf):
    return debtc / (cashneq + fcf).replace(0, np.nan)


def _f47_runway_months(cashneq, intexp):
    return cashneq / (intexp / 12.0).replace(0, np.nan)


# ============================================================
# --- Block A: alternate-window coverage levels & smooths ---

# EBIT interest coverage, half-year smoothed (slower structural cover)
def f47ds_f47_debt_service_coverage_ebitcov_126d_base_v076_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    b = _mean(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage EMA minus slow EMA (coverage trend displacement)
def f47ds_f47_debt_service_coverage_ebitdacovema_base_v077_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    b = c.ewm(span=21, min_periods=10).mean() - c.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage monthly level (fast cash cover)
def f47ds_f47_debt_service_coverage_ncfocov_21d_base_v078_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    b = _mean(c, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf coverage, half-year smoothed and z-scored (structural cash cover)
def f47ds_f47_debt_service_coverage_fcfcovz_126d_base_v079_signal(fcf, intexp):
    c = _mean(_f47_cash_cov_fcf(fcf, intexp), 126)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT coverage percentile rank over 504d (long-horizon cover percentile)
def f47ds_f47_debt_service_coverage_ebitcovrank_504d_base_v080_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block B: coverage momentum / change at varied horizons ---

# monthly change in EBITDA coverage (fast compression)
def f47ds_f47_debt_service_coverage_ebitdacovchg_21d_base_v081_signal(ebitda, intexp):
    c = _mean(_f47_int_cov_ebitda(ebitda, intexp), 21)
    b = c - c.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarterly change in EBIT coverage scaled by its own dispersion
def f47ds_f47_debt_service_coverage_ebitcovchgz_63d_base_v082_signal(ebit, intexp):
    c = _mean(_f47_int_cov_ebit(ebit, intexp), 21)
    chg = c - c.shift(63)
    b = chg / _std(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year log-momentum of ncfo coverage (proportional cash-cover trend)
def f47ds_f47_debt_service_coverage_ncfocovmom_126d_base_v083_signal(ncfo, intexp):
    c = _mean(_f47_cash_cov_ncfo(ncfo, intexp).clip(lower=0.01), 21)
    b = np.log(c.replace(0, np.nan) / c.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of fcf coverage (2nd diff over quarters)
def f47ds_f47_debt_service_coverage_fcfcovaccel_base_v084_signal(fcf, intexp):
    c = _mean(_f47_cash_cov_fcf(fcf, intexp), 21)
    d1 = c - c.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block C: cost-of-debt facets ---

# cost of debt half-year smoothed (structural funding cost)
def f47ds_f47_debt_service_coverage_costdebt_126d_base_v085_signal(intexp, debt):
    c = _f47_cost_of_debt(intexp, debt)
    b = _mean(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost of debt percentile rank over 504d (funding-cost regime percentile)
def f47ds_f47_debt_service_coverage_costdebtrank_504d_base_v086_signal(intexp, debt):
    c = _f47_cost_of_debt(intexp, debt)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-debt spread: cost on long-term debt minus blended cost (term premium)
def f47ds_f47_debt_service_coverage_costtermspread_base_v087_signal(intexp, debt, debtnc):
    blended = intexp / debt.replace(0, np.nan)
    longc = intexp / debtnc.replace(0, np.nan)
    b = _mean(longc - blended, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarter-over-quarter rise in cost of debt (near-term refi shock)
def f47ds_f47_debt_service_coverage_costdebtqoq_63d_base_v088_signal(intexp, debt):
    c = _mean(_f47_cost_of_debt(intexp, debt), 21)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied marginal cost of debt: change in interest vs change in debt
def f47ds_f47_debt_service_coverage_marginalcost_base_v089_signal(intexp, debt):
    di = intexp - intexp.shift(252)
    dd = (debt - debt.shift(252))
    b = di / dd.replace(0, np.nan)
    b = b.clip(lower=-1.0, upper=2.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block D: fixed-charge & pref facets ---

# preferred-dividend drag share of total fixed charges, percentile-ranked (cap-structure mix)
def f47ds_f47_debt_service_coverage_fccncfo_63d_base_v090_signal(prefdivis, intexp):
    c = prefdivis / (prefdivis + intexp).replace(0, np.nan)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-charge coverage by fcf, percentile ranked (harsh fixed-charge cover percentile)
def f47ds_f47_debt_service_coverage_fccfcfrank_252d_base_v091_signal(fcf, intexp, prefdivis):
    c = fcf / (intexp + prefdivis).replace(0, np.nan)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pref-dividend burden relative to EBITDA (preferred drag on cash earnings)
def f47ds_f47_debt_service_coverage_prefebitda_63d_base_v092_signal(prefdivis, ebitda):
    c = prefdivis / ebitda.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-charge coverage YoY deterioration (ncfo-based fixed cover change)
def f47ds_f47_debt_service_coverage_fccyoy_252d_base_v093_signal(ncfo, intexp, prefdivis):
    c = _mean(ncfo / (intexp + prefdivis).replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block E: maturity-wall facets ---

# maturity wall half-year smoothed (structural refi pressure)
def f47ds_f47_debt_service_coverage_matwall_126d_base_v094_signal(debtc, cashneq, fcf):
    c = _f47_maturity_wall(debtc, cashneq, fcf)
    b = _mean(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity-wall percentile rank over 504d (refi-pressure regime percentile)
def f47ds_f47_debt_service_coverage_matwallrank_504d_base_v095_signal(debtc, cashneq, fcf):
    c = _f47_maturity_wall(debtc, cashneq, fcf)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity wall YoY change (escalating/easing wall)
def f47ds_f47_debt_service_coverage_matwallyoy_252d_base_v096_signal(debtc, cashneq, fcf):
    c = _mean(_f47_maturity_wall(debtc, cashneq, fcf), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current debt covered by one year of fcf, YoY change (organic-repay capacity trend)
def f47ds_f47_debt_service_coverage_curdebtfcf_63d_base_v097_signal(debtc, fcf):
    c = _mean(fcf / debtc.replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block F: runway facets ---

# interest runway from cash, half-year smoothed (structural runway)
def f47ds_f47_debt_service_coverage_runway_126d_base_v098_signal(cashneq, intexp):
    c = _f47_runway_months(cashneq, intexp)
    b = _mean(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest runway percentile rank over 504d
def f47ds_f47_debt_service_coverage_runwayrank_504d_base_v099_signal(cashneq, intexp):
    c = _f47_runway_months(cashneq, intexp)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway including fcf vs interest (months of combined liquidity per interest)
def f47ds_f47_debt_service_coverage_runwayfcf_63d_base_v100_signal(cashneq, fcf, intexp):
    c = (cashneq + fcf.clip(lower=0)) / (intexp / 12.0).replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block G: distress counts / regimes (self-relative thresholds) ---

# weighted time EBIT coverage sat below its 504d 30th percentile (chronic weak cover)
def f47ds_f47_debt_service_coverage_weakcovtime_252d_base_v101_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    thr = c.rolling(504, min_periods=126).quantile(0.30)
    weak = (c < thr).astype(float)
    b = weak.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of cost-of-debt spikes above 504d 70th pctile over the year (rate-shock tally)
def f47ds_f47_debt_service_coverage_costspikes_252d_base_v102_signal(intexp, debt):
    c = _f47_cost_of_debt(intexp, debt)
    thr = c.rolling(504, min_periods=126).quantile(0.70)
    hot = (c > thr).astype(float)
    entries = ((hot == 1) & (hot.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 5.0 * (c - thr).clip(lower=0).rolling(63, min_periods=21).mean() / c.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-day streak with EBITDA coverage below its 252d median (sustained stress)
def f47ds_f47_debt_service_coverage_covstreak_base_v103_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    thr = c.rolling(252, min_periods=63).median()
    under = (c < thr).astype(float)
    grp = (under == 0).cumsum()
    streak = under.groupby(grp).cumsum()
    b = streak / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year maturity wall sat above its own 504d median (sustained refi regime)
def f47ds_f47_debt_service_coverage_wallhotregime_252d_base_v104_signal(debtc, cashneq, fcf):
    c = _f47_maturity_wall(debtc, cashneq, fcf)
    thr = c.rolling(504, min_periods=126).median()
    hot = (c > thr).astype(float)
    b = hot.rolling(252, min_periods=126).mean() + (c - thr).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block H: peak/trough coverage facets ---

# current EBIT coverage vs trailing 252d peak coverage (erosion ratio)
def f47ds_f47_debt_service_coverage_ebitcovvspeak_252d_base_v105_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    pk = _rmax(c, 252)
    b = c / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage vs trailing 504d peak (deep trough erosion)
def f47ds_f47_debt_service_coverage_ncfocovvspeak_504d_base_v106_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    pk = _rmax(c, 504)
    b = c / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage rebound: current EBITDA coverage above its trailing 252d trough
def f47ds_f47_debt_service_coverage_covrebound_252d_base_v107_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    tr = _rmin(c, 252)
    b = (c - tr) / tr.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf coverage drawdown from 504d peak in std units (cash-cover stress z)
def f47ds_f47_debt_service_coverage_fcfpeakz_504d_base_v108_signal(fcf, intexp):
    c = _f47_cash_cov_fcf(fcf, intexp)
    pk = _rmax(c, 504)
    sd = _std(c, 252)
    b = (c - pk) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block I: interest-burden (inverse coverage) facets ---

# interest burden on EBIT (intexp/ebit), monthly level
def f47ds_f47_debt_service_coverage_intebitburden_21d_base_v109_signal(intexp, ebit):
    c = intexp / ebit.replace(0, np.nan)
    b = _mean(c, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden on fcf (intexp/fcf), half-year smoothed
def f47ds_f47_debt_service_coverage_intfcfburden_126d_base_v110_signal(intexp, fcf):
    c = intexp / fcf.replace(0, np.nan)
    b = _mean(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden on ncfo z-scored (abnormal cash-burden episodes)
def f47ds_f47_debt_service_coverage_intncfoburdenz_252d_base_v111_signal(intexp, ncfo):
    c = intexp / ncfo.replace(0, np.nan)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YoY rise in interest burden on EBIT (worsening earnings-side service drag)
def f47ds_f47_debt_service_coverage_intebitburdenyoy_base_v112_signal(intexp, ebit):
    c = _mean(intexp / ebit.replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block J: cross-metric spreads / dispersions ---

# EBITDA-vs-ncfo coverage spread (cash-vs-accrual cover gap), z-scored
def f47ds_f47_debt_service_coverage_ebitdancfogapz_base_v113_signal(ebitda, ncfo, intexp):
    g = (ebitda - ncfo) / intexp.replace(0, np.nan)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of EBIT/EBITDA/fcf coverages (multi-metric cover disagreement)
def f47ds_f47_debt_service_coverage_covdisp3_base_v114_signal(ebit, ebitda, fcf, intexp):
    c1 = _f47_int_cov_ebit(ebit, intexp)
    c2 = _f47_int_cov_ebitda(ebitda, intexp)
    c3 = _f47_cash_cov_fcf(fcf, intexp)
    b = pd.concat([c1, c2, c3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weakest-cover view: which earnings base is the binding constraint, z-scored gap to mean
def f47ds_f47_debt_service_coverage_mincov_63d_base_v115_signal(ebit, ebitda, ncfo, fcf, intexp):
    c1 = _f47_int_cov_ebit(ebit, intexp)
    c2 = _f47_int_cov_ebitda(ebitda, intexp)
    c3 = _f47_cash_cov_ncfo(ncfo, intexp)
    c4 = _f47_cash_cov_fcf(fcf, intexp)
    stk = pd.concat([c1, c2, c3, c4], axis=1)
    # how far the weakest cover sits below the average cover (binding-constraint depth)
    gap = stk.mean(axis=1) - stk.min(axis=1)
    b = _z(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range of coverages (max-min spread) relative to mean coverage (relative dispersion)
def f47ds_f47_debt_service_coverage_covreldisp_base_v116_signal(ebit, ebitda, ncfo, intexp):
    c1 = _f47_int_cov_ebit(ebit, intexp)
    c2 = _f47_int_cov_ebitda(ebitda, intexp)
    c3 = _f47_cash_cov_ncfo(ncfo, intexp)
    stk = pd.concat([c1, c2, c3], axis=1)
    b = (stk.max(axis=1) - stk.min(axis=1)) / stk.mean(axis=1).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block K: liquidity / balance interactions (flow-burden tinted) ---

# liquidity-to-interest buffer: (cashneq+debtnc headroom) — cash vs annual interest, ranked
def f47ds_f47_debt_service_coverage_cashintrank_252d_base_v117_signal(cashneq, intexp):
    c = cashneq / intexp.replace(0, np.nan)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net liquidity after current maturities, scaled by interest (post-wall runway)
def f47ds_f47_debt_service_coverage_postwallrun_63d_base_v118_signal(cashneq, debtc, intexp):
    net_liq = (cashneq - debtc)
    c = net_liq / intexp.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest as share of cash earnings plus cash buffer (total drain intensity), ranked
def f47ds_f47_debt_service_coverage_draintensity_63d_base_v119_signal(intexp, ncfo, cashneq):
    c = intexp / (ncfo.clip(lower=0) + cashneq).replace(0, np.nan)
    b = _rank(_mean(c, 21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash buffer to total debt (stock-light liquidity ratio), z-scored
def f47ds_f47_debt_service_coverage_cashdebtz_252d_base_v120_signal(cashneq, debt, intexp):
    # interest included per family rule to tint as service buffer
    c = cashneq / (debt + intexp).replace(0, np.nan)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block L: combined distress scores ---

# coverage-collapse score using EBIT: low cover z combined with rising burden z
def f47ds_f47_debt_service_coverage_ebitcollapse_base_v121_signal(ebit, intexp, ncfo):
    covz = _z(_f47_int_cov_ebit(ebit, intexp), 252)
    burdz = _z(intexp / ncfo.replace(0, np.nan), 252)
    b = burdz - covz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-trigger distress: weak EBITDA cover, high wall, low runway (additive z)
def f47ds_f47_debt_service_coverage_triple_base_v122_signal(ebitda, intexp, debtc, cashneq, fcf):
    covz = _z(_f47_int_cov_ebitda(ebitda, intexp), 252)
    wallz = _z(_f47_maturity_wall(debtc, cashneq, fcf), 252)
    runz = _z(_f47_runway_months(cashneq, intexp), 252)
    b = wallz - covz - runz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rate-stress gap: EBITDA-on-debt earnings yield minus effective cost of debt (net carry)
def f47ds_f47_debt_service_coverage_ratestressed_63d_base_v123_signal(ebitda, intexp, debt):
    earnyield = ebitda / debt.replace(0, np.nan)
    cost = _f47_cost_of_debt(intexp, debt)
    b = _mean(earnyield - cost, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival service margin: (ncfo - interest - pref) over cash buffer (months of cushion)
def f47ds_f47_debt_service_coverage_survmargin_63d_base_v124_signal(ncfo, intexp, prefdivis, cashneq):
    resid = ncfo - intexp - prefdivis
    c = resid / cashneq.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block M: sign-magnitude / bounded transforms ---

# sign-magnitude of fcf coverage cushion above breakeven (bounded distress, smoothed)
def f47ds_f47_debt_service_coverage_fcfcushsm_63d_base_v125_signal(fcf, intexp):
    c = _f47_cash_cov_fcf(fcf, intexp) - 1.0
    sm = np.sign(c) * (c.abs() ** 0.5)
    b = _mean(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed ncfo-coverage compression momentum (bounded quarterly)
def f47ds_f47_debt_service_coverage_ncfocovtanh_63d_base_v126_signal(ncfo, intexp):
    c = _mean(_f47_cash_cov_ncfo(ncfo, intexp), 21)
    chg = c - c.shift(63)
    b = np.tanh(chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log of EBIT coverage (compressed scale level)
def f47ds_f47_debt_service_coverage_logebitcov_63d_base_v127_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    b = _mean(np.log(c.clip(lower=0.01)), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh of cost-of-debt deviation from its median (bounded funding-cost shock)
def f47ds_f47_debt_service_coverage_costtanh_base_v128_signal(intexp, debt):
    c = _f47_cost_of_debt(intexp, debt)
    dev = c - _med(c, 504)
    b = np.tanh(50.0 * dev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block N: volatility / stability of coverage ---

# coefficient of variation of EBIT coverage over 252d (cover instability)
def f47ds_f47_debt_service_coverage_ebitcovcv_252d_base_v129_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    b = _std(c, 252) / _mean(c, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized volatility of fcf coverage (raw dispersion of cash cover)
def f47ds_f47_debt_service_coverage_fcfcovvol_126d_base_v130_signal(fcf, intexp):
    c = _f47_cash_cov_fcf(fcf, intexp)
    b = _std(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation of EBITDA coverage (only adverse cover swings)
def f47ds_f47_debt_service_coverage_covdownvol_252d_base_v131_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    chg = c.diff()
    down = chg.clip(upper=0.0)
    b = (down ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage stability ratio: short-window std over long-window std (vol regime shift)
def f47ds_f47_debt_service_coverage_covvolratio_base_v132_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    b = _std(c, 63) / _std(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block O: term-structure & mix facets ---

# share of interest implicitly on short-term debt (front-end funding exposure)
def f47ds_f47_debt_service_coverage_stintshare_63d_base_v133_signal(debtc, debt, intexp):
    # debtc/debt scaled by overall interest level -> front-end interest intensity proxy
    c = (debtc / debt.replace(0, np.nan)) * (intexp / debt.replace(0, np.nan))
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt coverage by operating cash net of interest, YoY change (term-cover trend)
def f47ds_f47_debt_service_coverage_ltdebtcov_63d_base_v134_signal(ncfo, debtnc, intexp):
    c = _mean((ncfo - intexp) / debtnc.replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-vs-noncurrent debt service tilt z (refi-front-loading regime)
def f47ds_f47_debt_service_coverage_debttiltz_252d_base_v135_signal(debtc, debtnc, intexp):
    tilt = debtc / debtnc.replace(0, np.nan)
    # tint with interest to keep it a service-burden feature
    tilt = tilt * (1.0 + intexp / (debtc + debtnc).replace(0, np.nan))
    b = _z(tilt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block P: more momentum/regime diversifiers ---

# fraction of year EBITDA coverage declined vs prior month (chronic-compression density)
def f47ds_f47_debt_service_coverage_compdensity_252d_base_v136_signal(ebitda, intexp):
    c = _mean(_f47_int_cov_ebitda(ebitda, intexp), 21)
    decl = (c < c.shift(21)).astype(float)
    b = decl.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-debt above its 252d mean by how many std (funding-cost extremity)
def f47ds_f47_debt_service_coverage_costextremez_base_v137_signal(intexp, debt):
    c = _f47_cost_of_debt(intexp, debt)
    b = _z(c, 252).clip(lower=0.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast/slow ncfo coverage ratio (recent cash cover vs structural cash cover)
def f47ds_f47_debt_service_coverage_ncfofastslow_base_v138_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    b = _mean(c, 21) / _mean(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-trend slope sign persistence (sustained improving/worsening cover)
def f47ds_f47_debt_service_coverage_trendpersist_base_v139_signal(ebit, intexp):
    c = _mean(_f47_int_cov_ebit(ebit, intexp), 21)
    up = (c.diff() > 0).astype(float)
    b = up.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block Q: final blended diversifiers ---

# interest coverage gap to a 3.0 investment-grade-ish target, normalized & ranked
def f47ds_f47_debt_service_coverage_igtargetrank_252d_base_v140_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    gap = (c - 3.0)
    b = _rank(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow service coverage net of pref over total fixed obligations, YoY change
def f47ds_f47_debt_service_coverage_netfixedcov_63d_base_v141_signal(ncfo, prefdivis, intexp, debtc):
    c = _mean((ncfo - prefdivis) / (intexp + debtc).replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# product of coverage weakness and wall pressure (compound distress, bounded)
def f47ds_f47_debt_service_coverage_compounddistress_base_v142_signal(ebitda, intexp, debtc, cashneq, fcf):
    weak = (-_z(_f47_int_cov_ebitda(ebitda, intexp), 252)).clip(lower=0)
    wall = _z(_f47_maturity_wall(debtc, cashneq, fcf), 252).clip(lower=0)
    b = np.tanh(weak * wall)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest expense intensity vs total liquidity+earnings capacity (burn fraction)
def f47ds_f47_debt_service_coverage_burnfraction_63d_base_v143_signal(intexp, cashneq, ebitda):
    c = intexp / (cashneq + ebitda.clip(lower=0)).replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash net carry vs funding cost: (ncfo/debt) minus effective cost, z-scored
def f47ds_f47_debt_service_coverage_netspread_63d_base_v144_signal(ncfo, intexp, debt):
    cashyield = ncfo / debt.replace(0, np.nan)
    cost = _f47_cost_of_debt(intexp, debt)
    b = _z(cashyield - cost, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year change in months-of-runway (cushion build/erosion, mid-horizon)
def f47ds_f47_debt_service_coverage_runwaychg_126d_base_v145_signal(cashneq, intexp):
    c = _mean(_f47_runway_months(cashneq, intexp), 21)
    b = c - c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage convexity: 2nd difference of EBITDA coverage (turning-point curvature)
def f47ds_f47_debt_service_coverage_covcurv_base_v146_signal(ebitda, intexp):
    c = _mean(_f47_int_cov_ebitda(ebitda, intexp), 21)
    b = c - 2.0 * c.shift(63) + c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-charge burden EMA displacement (acute fixed-charge shock vs trend)
def f47ds_f47_debt_service_coverage_fcburdendisp_base_v147_signal(intexp, prefdivis, fcf):
    c = (intexp + prefdivis) / fcf.replace(0, np.nan)
    b = c.ewm(span=42, min_periods=21).mean() - c.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-service coverage ratio (ncfo / (interest+current debt)) z-scored, mid-horizon
def f47ds_f47_debt_service_coverage_dscrz126_base_v148_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    b = _z(_mean(c, 21), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth of strong coverage: fraction of earnings bases covering >2x interest
def f47ds_f47_debt_service_coverage_strongbreadth_63d_base_v149_signal(ebit, ebitda, ncfo, fcf, intexp):
    c1 = (_f47_int_cov_ebit(ebit, intexp) > 2.0).astype(float)
    c2 = (_f47_int_cov_ebitda(ebitda, intexp) > 2.0).astype(float)
    c3 = (_f47_cash_cov_ncfo(ncfo, intexp) > 2.0).astype(float)
    c4 = (_f47_cash_cov_fcf(fcf, intexp) > 2.0).astype(float)
    breadth = (c1 + c2 + c3 + c4) / 4.0
    b = _mean(breadth, 63) + 0.1 * _z(_f47_int_cov_ebitda(ebitda, intexp), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-in service-burden index: sum of standardized burden facets (composite stress)
def f47ds_f47_debt_service_coverage_burdenindex_base_v150_signal(intexp, ebitda, ncfo, debtc, cashneq):
    b1 = _z(intexp / ebitda.replace(0, np.nan), 252)
    b2 = _z(intexp / ncfo.replace(0, np.nan), 252)
    b3 = _z(debtc / cashneq.replace(0, np.nan), 252)
    b = (b1 + b2 + b3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47ds_f47_debt_service_coverage_ebitcov_126d_base_v076_signal,
    f47ds_f47_debt_service_coverage_ebitdacovema_base_v077_signal,
    f47ds_f47_debt_service_coverage_ncfocov_21d_base_v078_signal,
    f47ds_f47_debt_service_coverage_fcfcovz_126d_base_v079_signal,
    f47ds_f47_debt_service_coverage_ebitcovrank_504d_base_v080_signal,
    f47ds_f47_debt_service_coverage_ebitdacovchg_21d_base_v081_signal,
    f47ds_f47_debt_service_coverage_ebitcovchgz_63d_base_v082_signal,
    f47ds_f47_debt_service_coverage_ncfocovmom_126d_base_v083_signal,
    f47ds_f47_debt_service_coverage_fcfcovaccel_base_v084_signal,
    f47ds_f47_debt_service_coverage_costdebt_126d_base_v085_signal,
    f47ds_f47_debt_service_coverage_costdebtrank_504d_base_v086_signal,
    f47ds_f47_debt_service_coverage_costtermspread_base_v087_signal,
    f47ds_f47_debt_service_coverage_costdebtqoq_63d_base_v088_signal,
    f47ds_f47_debt_service_coverage_marginalcost_base_v089_signal,
    f47ds_f47_debt_service_coverage_fccncfo_63d_base_v090_signal,
    f47ds_f47_debt_service_coverage_fccfcfrank_252d_base_v091_signal,
    f47ds_f47_debt_service_coverage_prefebitda_63d_base_v092_signal,
    f47ds_f47_debt_service_coverage_fccyoy_252d_base_v093_signal,
    f47ds_f47_debt_service_coverage_matwall_126d_base_v094_signal,
    f47ds_f47_debt_service_coverage_matwallrank_504d_base_v095_signal,
    f47ds_f47_debt_service_coverage_matwallyoy_252d_base_v096_signal,
    f47ds_f47_debt_service_coverage_curdebtfcf_63d_base_v097_signal,
    f47ds_f47_debt_service_coverage_runway_126d_base_v098_signal,
    f47ds_f47_debt_service_coverage_runwayrank_504d_base_v099_signal,
    f47ds_f47_debt_service_coverage_runwayfcf_63d_base_v100_signal,
    f47ds_f47_debt_service_coverage_weakcovtime_252d_base_v101_signal,
    f47ds_f47_debt_service_coverage_costspikes_252d_base_v102_signal,
    f47ds_f47_debt_service_coverage_covstreak_base_v103_signal,
    f47ds_f47_debt_service_coverage_wallhotregime_252d_base_v104_signal,
    f47ds_f47_debt_service_coverage_ebitcovvspeak_252d_base_v105_signal,
    f47ds_f47_debt_service_coverage_ncfocovvspeak_504d_base_v106_signal,
    f47ds_f47_debt_service_coverage_covrebound_252d_base_v107_signal,
    f47ds_f47_debt_service_coverage_fcfpeakz_504d_base_v108_signal,
    f47ds_f47_debt_service_coverage_intebitburden_21d_base_v109_signal,
    f47ds_f47_debt_service_coverage_intfcfburden_126d_base_v110_signal,
    f47ds_f47_debt_service_coverage_intncfoburdenz_252d_base_v111_signal,
    f47ds_f47_debt_service_coverage_intebitburdenyoy_base_v112_signal,
    f47ds_f47_debt_service_coverage_ebitdancfogapz_base_v113_signal,
    f47ds_f47_debt_service_coverage_covdisp3_base_v114_signal,
    f47ds_f47_debt_service_coverage_mincov_63d_base_v115_signal,
    f47ds_f47_debt_service_coverage_covreldisp_base_v116_signal,
    f47ds_f47_debt_service_coverage_cashintrank_252d_base_v117_signal,
    f47ds_f47_debt_service_coverage_postwallrun_63d_base_v118_signal,
    f47ds_f47_debt_service_coverage_draintensity_63d_base_v119_signal,
    f47ds_f47_debt_service_coverage_cashdebtz_252d_base_v120_signal,
    f47ds_f47_debt_service_coverage_ebitcollapse_base_v121_signal,
    f47ds_f47_debt_service_coverage_triple_base_v122_signal,
    f47ds_f47_debt_service_coverage_ratestressed_63d_base_v123_signal,
    f47ds_f47_debt_service_coverage_survmargin_63d_base_v124_signal,
    f47ds_f47_debt_service_coverage_fcfcushsm_63d_base_v125_signal,
    f47ds_f47_debt_service_coverage_ncfocovtanh_63d_base_v126_signal,
    f47ds_f47_debt_service_coverage_logebitcov_63d_base_v127_signal,
    f47ds_f47_debt_service_coverage_costtanh_base_v128_signal,
    f47ds_f47_debt_service_coverage_ebitcovcv_252d_base_v129_signal,
    f47ds_f47_debt_service_coverage_fcfcovvol_126d_base_v130_signal,
    f47ds_f47_debt_service_coverage_covdownvol_252d_base_v131_signal,
    f47ds_f47_debt_service_coverage_covvolratio_base_v132_signal,
    f47ds_f47_debt_service_coverage_stintshare_63d_base_v133_signal,
    f47ds_f47_debt_service_coverage_ltdebtcov_63d_base_v134_signal,
    f47ds_f47_debt_service_coverage_debttiltz_252d_base_v135_signal,
    f47ds_f47_debt_service_coverage_compdensity_252d_base_v136_signal,
    f47ds_f47_debt_service_coverage_costextremez_base_v137_signal,
    f47ds_f47_debt_service_coverage_ncfofastslow_base_v138_signal,
    f47ds_f47_debt_service_coverage_trendpersist_base_v139_signal,
    f47ds_f47_debt_service_coverage_igtargetrank_252d_base_v140_signal,
    f47ds_f47_debt_service_coverage_netfixedcov_63d_base_v141_signal,
    f47ds_f47_debt_service_coverage_compounddistress_base_v142_signal,
    f47ds_f47_debt_service_coverage_burnfraction_63d_base_v143_signal,
    f47ds_f47_debt_service_coverage_netspread_63d_base_v144_signal,
    f47ds_f47_debt_service_coverage_runwaychg_126d_base_v145_signal,
    f47ds_f47_debt_service_coverage_covcurv_base_v146_signal,
    f47ds_f47_debt_service_coverage_fcburdendisp_base_v147_signal,
    f47ds_f47_debt_service_coverage_dscrz126_base_v148_signal,
    f47ds_f47_debt_service_coverage_strongbreadth_63d_base_v149_signal,
    f47ds_f47_debt_service_coverage_burdenindex_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_DEBT_SERVICE_COVERAGE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    intexp = _fund(101, base=8e6, drift=0.01, vol=0.06).rename("intexp")
    ebit = _fund(102, base=6e7, drift=0.0, vol=0.10, allow_neg=True).rename("ebit")
    ebitda = _fund(103, base=1.1e8, drift=0.0, vol=0.09, allow_neg=True).rename("ebitda")
    ncfo = _fund(104, base=9e7, drift=0.0, vol=0.11, allow_neg=True).rename("ncfo")
    fcf = _fund(105, base=5e7, drift=0.0, vol=0.13, allow_neg=True).rename("fcf")
    debt = _fund(106, base=4e8, drift=0.005, vol=0.05).rename("debt")
    debtc = _fund(107, base=9e7, drift=0.005, vol=0.07).rename("debtc")
    debtnc = _fund(108, base=3.1e8, drift=0.004, vol=0.05).rename("debtnc")
    cashneq = _fund(109, base=1.2e8, drift=0.0, vol=0.10).rename("cashneq")
    prefdivis = _fund(110, base=3e6, drift=0.0, vol=0.05).rename("prefdivis")

    cols = {"intexp": intexp, "ebit": ebit, "ebitda": ebitda, "ncfo": ncfo,
            "fcf": fcf, "debt": debt, "debtc": debtc, "debtnc": debtnc,
            "cashneq": cashneq, "prefdivis": prefdivis}

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

    print("OK f47_debt_service_coverage_base_076_150_claude: %d features pass" % n_features)
