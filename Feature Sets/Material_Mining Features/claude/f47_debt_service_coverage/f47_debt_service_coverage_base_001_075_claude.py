import inspect
import numpy as np
import pandas as pd

# ============================================================
# f47_debt_service_coverage  —  DEBT-SERVICE COVERAGE (flow burden)
# FUNDAMENTAL family. Every feature consumes >= 1 fundamental column from:
#   intexp, ebit, ebitda, ncfo, fcf, debt, debtc, debtnc, cashneq, prefdivis
# Axis = FLOW / SERVICE burden via interest expense (intexp). Distinct from
# debt-STOCK families (f31_debt_cycle_trajectory, f22_balance_sheet_survival).
# The killer for levered miners: coverage collapsing at the cycle trough.
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


# ===== folder domain primitives (debt-service / interest coverage) =====
def _f47_int_cov_ebit(ebit, intexp):
    # classic interest coverage: EBIT / interest expense
    return ebit / intexp.replace(0, np.nan)


def _f47_int_cov_ebitda(ebitda, intexp):
    # EBITDA interest coverage (cash earnings burden)
    return ebitda / intexp.replace(0, np.nan)


def _f47_cash_cov_ncfo(ncfo, intexp):
    # cash-flow interest coverage: operating cash flow / interest
    return ncfo / intexp.replace(0, np.nan)


def _f47_cash_cov_fcf(fcf, intexp):
    # free-cash-flow interest coverage
    return fcf / intexp.replace(0, np.nan)


def _f47_cost_of_debt(intexp, debt):
    # effective cost of debt: interest expense / total debt
    return intexp / debt.replace(0, np.nan)


def _f47_fixed_charge(intexp, prefdivis, ncfo):
    # total fixed-charge burden on operating cash: (interest + pref divs) / ncfo
    return (intexp + prefdivis) / ncfo.replace(0, np.nan)


def _f47_maturity_wall(debtc, cashneq, fcf):
    # near-term maturity wall: current debt vs liquidity available to service it
    return debtc / (cashneq + fcf).replace(0, np.nan)


def _f47_runway_months(cashneq, intexp):
    # months-of-coverage runway: cash / monthly interest burden
    return cashneq / (intexp / 12.0).replace(0, np.nan)


# ============================================================
# --- Block A: seed interest-coverage primitives (levels) ---

# EBIT interest coverage (classic), smoothed over a quarter
def f47ds_f47_debt_service_coverage_ebitcov_63d_base_v001_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT interest coverage z-scored vs its own 252d history (de-trended level)
def f47ds_f47_debt_service_coverage_ebitcovz_252d_base_v002_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA interest coverage level (cash earnings burden)
def f47ds_f47_debt_service_coverage_ebitdacov_63d_base_v003_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA interest coverage percentile-ranked vs its own 252d history
def f47ds_f47_debt_service_coverage_ebitdacovrank_252d_base_v004_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash-flow interest coverage (ncfo / intexp)
def f47ds_f47_debt_service_coverage_ncfocov_63d_base_v005_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash-flow coverage z-scored vs own 252d history
def f47ds_f47_debt_service_coverage_ncfocovz_252d_base_v006_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-flow interest coverage (fcf / intexp) — the harshest test
def f47ds_f47_debt_service_coverage_fcfcov_63d_base_v007_signal(fcf, intexp):
    c = _f47_cash_cov_fcf(fcf, intexp)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-flow coverage percentile-ranked vs own 252d history
def f47ds_f47_debt_service_coverage_fcfcovrank_252d_base_v008_signal(fcf, intexp):
    c = _f47_cash_cov_fcf(fcf, intexp)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block B: YoY change in coverage (compression flags) ---

# YoY change in EBIT interest coverage (compression: negative = deteriorating)
def f47ds_f47_debt_service_coverage_ebitcovyoy_252d_base_v009_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    cs = _mean(c, 21)
    b = cs - cs.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YoY log-ratio of EBITDA coverage (proportional compression)
def f47ds_f47_debt_service_coverage_ebitdacovyoy_252d_base_v010_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp).clip(lower=0.01)
    cs = _mean(c, 21)
    b = np.log(cs.replace(0, np.nan) / cs.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# binary coverage-compression flag: EBITDA coverage below where it was a year ago
def f47ds_f47_debt_service_coverage_compflag_252d_base_v011_signal(ebitda, intexp):
    c = _mean(_f47_int_cov_ebitda(ebitda, intexp), 21)
    comp = (c < c.shift(252)).astype(float)
    # weight the flag by how deep the compression runs
    depth = (c.shift(252) - c).clip(lower=0) / c.shift(252).abs().replace(0, np.nan)
    b = comp + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarter-over-quarter change in ncfo coverage (near-term compression)
def f47ds_f47_debt_service_coverage_ncfocovqoq_63d_base_v012_signal(ncfo, intexp):
    c = _mean(_f47_cash_cov_ncfo(ncfo, intexp), 21)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year change in fcf coverage scaled by its own dispersion (compression z)
def f47ds_f47_debt_service_coverage_fcfcovchgz_126d_base_v013_signal(fcf, intexp):
    c = _mean(_f47_cash_cov_fcf(fcf, intexp), 21)
    chg = c - c.shift(126)
    sd = _std(c, 252)
    b = chg / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block C: coverage at trough vs trailing peak ---

# current EBITDA coverage relative to its trailing 504d peak (trough erosion)
def f47ds_f47_debt_service_coverage_covvspeak_504d_base_v014_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    pk = _rmax(c, 504)
    b = c / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA itself at trough vs its trailing 504d peak, normalized by interest burden
def f47ds_f47_debt_service_coverage_ebitdatrough_504d_base_v015_signal(ebitda, intexp):
    pk = _rmax(ebitda, 504)
    erosion = (pk - ebitda) / pk.abs().replace(0, np.nan)
    burden = intexp / pk.abs().replace(0, np.nan)
    b = erosion * (1.0 + burden)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage drawdown: current EBIT coverage vs 252d peak coverage (gap)
def f47ds_f47_debt_service_coverage_covdd_252d_base_v016_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    pk = _rmax(c, 252)
    b = c / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trough coverage: current ncfo coverage vs trailing 252d MIN (rebound headroom)
def f47ds_f47_debt_service_coverage_covtroughgap_252d_base_v017_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    tr = _rmin(c, 252)
    b = c - tr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block D: effective cost of debt and its rise ---

# effective cost of debt (intexp / debt), level
def f47ds_f47_debt_service_coverage_costdebt_63d_base_v018_signal(intexp, debt):
    c = _f47_cost_of_debt(intexp, debt)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rise in effective cost of debt over a year (refi/rate-shock pressure)
def f47ds_f47_debt_service_coverage_costdebtyoy_252d_base_v019_signal(intexp, debt):
    c = _mean(_f47_cost_of_debt(intexp, debt), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost of debt z-scored vs own 252d history (abnormal funding cost)
def f47ds_f47_debt_service_coverage_costdebtz_252d_base_v020_signal(intexp, debt):
    c = _f47_cost_of_debt(intexp, debt)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost of debt measured on long-term debt only (debtnc) — structural funding cost
def f47ds_f47_debt_service_coverage_costdebtnc_63d_base_v021_signal(intexp, debtnc):
    c = intexp / debtnc.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block E: fixed-charge burden ---

# total fixed-charge burden against free cash flow (interest+pref)/fcf
def f47ds_f47_debt_service_coverage_fixedchg_63d_base_v022_signal(intexp, prefdivis, fcf):
    c = (intexp + prefdivis) / fcf.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-charge burden on operating cash, percentile-ranked vs own 504d history
def f47ds_f47_debt_service_coverage_fixedchgz_252d_base_v023_signal(intexp, prefdivis, ncfo):
    c = _f47_fixed_charge(intexp, prefdivis, ncfo)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-dividend share of total fixed charges (capital-structure drag)
def f47ds_f47_debt_service_coverage_prefshare_63d_base_v024_signal(prefdivis, intexp):
    c = prefdivis / (prefdivis + intexp).replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pref-dividend-to-interest burden ratio z-scored (capital-structure fixed-charge mix)
def f47ds_f47_debt_service_coverage_fixedchgcov_63d_base_v025_signal(prefdivis, intexp):
    c = prefdivis / intexp.replace(0, np.nan)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block F: near-term maturity wall ---

# maturity wall: current debt vs cash+fcf liquidity (>1 = cannot self-fund)
def f47ds_f47_debt_service_coverage_matwall_63d_base_v026_signal(debtc, cashneq, fcf):
    c = _f47_maturity_wall(debtc, cashneq, fcf)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity wall z-scored vs own 252d history (escalating refi pressure)
def f47ds_f47_debt_service_coverage_matwallz_252d_base_v027_signal(debtc, cashneq, fcf):
    c = _f47_maturity_wall(debtc, cashneq, fcf)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-debt share of total debt (front-loaded maturity profile)
def f47ds_f47_debt_service_coverage_curdebtshare_63d_base_v028_signal(debtc, debt):
    c = debtc / debt.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current debt vs cash only (no fcf cushion) — liquidity-only wall
def f47ds_f47_debt_service_coverage_matwallcash_63d_base_v029_signal(debtc, cashneq):
    c = debtc / cashneq.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block G: months-of-coverage runway ---

# months of interest runway from cash (cash / monthly interest)
def f47ds_f47_debt_service_coverage_runway_63d_base_v030_signal(cashneq, intexp):
    c = _f47_runway_months(cashneq, intexp)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest-burn share of total liquidity buffer: intexp / (cashneq + fcf), ranked
def f47ds_f47_debt_service_coverage_runwaynet_63d_base_v031_signal(cashneq, intexp, fcf):
    # what fraction of the combined liquidity buffer one year of interest consumes
    c = intexp / (cashneq + fcf).replace(0, np.nan)
    b = _rank(_mean(c, 21), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YoY change in runway (shortening cushion = distress acceleration)
def f47ds_f47_debt_service_coverage_runwayyoy_252d_base_v032_signal(cashneq, intexp):
    c = _mean(_f47_runway_months(cashneq, intexp), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block H: negative-coverage persistence counts ---

# fraction of last year EBIT coverage sat below its own 504d median (weak-cover time)
def f47ds_f47_debt_service_coverage_negcovfrac_252d_base_v033_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    thr = c.rolling(504, min_periods=126).median()
    under = (c < thr).astype(float)
    depth = (thr - c).clip(lower=0) / thr.abs().replace(0, np.nan)
    b = under.rolling(252, min_periods=126).mean() + depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-day streak with fcf coverage below its 252d median (chronic shortfall)
def f47ds_f47_debt_service_coverage_negcovstreak_base_v034_signal(fcf, intexp):
    c = _f47_cash_cov_fcf(fcf, intexp)
    thr = c.rolling(252, min_periods=63).median()
    under = (c < thr).astype(float)
    grp = (under == 0).cumsum()
    streak = under.groupby(grp).cumsum()
    b = streak / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of distinct compression entries (coverage dropping below its 30th pctile) over a year
def f47ds_f47_debt_service_coverage_compentries_252d_base_v035_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    thr = c.rolling(504, min_periods=126).quantile(0.30)
    under = (c < thr).astype(float)
    entries = ((under == 1) & (under.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 5.0 * (thr - c).clip(lower=0).rolling(63, min_periods=21).mean() / c.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted time operating-cash coverage sat in its weakest tercile over the year
def f47ds_f47_debt_service_coverage_negncfofrac_252d_base_v036_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    thr = c.rolling(504, min_periods=126).quantile(0.3333)
    weak = (c < thr).astype(float)
    b = weak.rolling(252, min_periods=126).mean() + (thr - c).clip(lower=0).rolling(63, min_periods=21).mean() / thr.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block I: cross-metric coverage spreads / diversifiers ---

# accrual quality of cover: ratio of cash (ncfo) coverage to EBIT coverage
def f47ds_f47_debt_service_coverage_accrualgap_63d_base_v037_signal(ebit, ncfo, intexp):
    # intexp cancels: this is ncfo/ebit, the cash-conversion quality of earnings cover
    ce = _f47_int_cov_ebit(ebit, intexp)
    cc = _f47_cash_cov_ncfo(ncfo, intexp)
    b = _mean(cc / ce.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-vs-EBIT coverage spread (D&A cushion in coverage)
def f47ds_f47_debt_service_coverage_dacushion_63d_base_v038_signal(ebitda, ebit, intexp):
    b = _mean((ebitda - ebit) / intexp.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion of coverage: fcf/ncfo capex drag, z-scored vs own history
def f47ds_f47_debt_service_coverage_capexdrag_63d_base_v039_signal(fcf, ncfo, intexp):
    # intexp present per family rule; ratio = (fcf/intexp)/(ncfo/intexp) = fcf/ncfo
    cf = _f47_cash_cov_fcf(fcf, intexp)
    cn = _f47_cash_cov_ncfo(ncfo, intexp)
    b = _z(cf / cn.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long coverage divergence: 21d EBITDA cov vs 252d EBITDA cov
def f47ds_f47_debt_service_coverage_shortlongdiv_base_v040_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    b = _mean(c, 21) - _mean(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block J: interest-burden intensity (intexp scaled by cash earnings) ---

# interest burden as share of EBITDA (inverse coverage, bounded distress)
def f47ds_f47_debt_service_coverage_intburden_63d_base_v041_signal(intexp, ebitda):
    c = intexp / ebitda.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden as share of operating cash (intexp / ncfo)
def f47ds_f47_debt_service_coverage_intncfoburden_63d_base_v042_signal(intexp, ncfo):
    c = intexp / ncfo.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YoY rise in interest burden vs EBITDA (worsening service drag)
def f47ds_f47_debt_service_coverage_intburdenyoy_252d_base_v043_signal(intexp, ebitda):
    c = _mean(intexp / ebitda.replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden percentile-ranked vs own 504d history (extreme funding stress)
def f47ds_f47_debt_service_coverage_intburdenrank_504d_base_v044_signal(intexp, ebitda):
    c = intexp / ebitda.replace(0, np.nan)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block K: combined distress interactions ---

# coverage-collapse score: low EBITDA coverage AND rising cost of debt together
def f47ds_f47_debt_service_coverage_collapse_252d_base_v045_signal(ebitda, intexp, debt):
    covz = _z(_f47_int_cov_ebitda(ebitda, intexp), 252)
    costz = _z(_f47_cost_of_debt(intexp, debt), 252)
    b = costz - covz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-adjusted coverage: standardized coverage net of standardized wall pressure
def f47ds_f47_debt_service_coverage_liqadjcov_63d_base_v046_signal(ncfo, intexp, debtc, cashneq):
    covz = _z(_f47_cash_cov_ncfo(ncfo, intexp), 252)
    wallz = _z(debtc / cashneq.replace(0, np.nan), 252)
    b = covz - wallz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# prefunding adequacy vs full near-term stack, YoY change (liquidity build/erosion)
def f47ds_f47_debt_service_coverage_prefund_63d_base_v047_signal(cashneq, intexp, prefdivis, debtc):
    c = _mean(cashneq / (intexp + prefdivis + debtc).replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity erosion of coverage: share of total near-term service that is principal
def f47ds_f47_debt_service_coverage_dscr_63d_base_v048_signal(intexp, debtc):
    # debtc / (intexp + debtc): how principal-heavy the near-term service stack is
    c = debtc / (intexp + debtc).replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSCR z-scored vs own 252d history (escalating service stress)
def f47ds_f47_debt_service_coverage_dscrz_252d_base_v049_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block L: more diversified facets ---

# coverage volatility: dispersion of EBITDA coverage over 252d (instability)
def f47ds_f47_debt_service_coverage_covvol_252d_base_v050_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    b = _std(c, 252) / _mean(c, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# curvature of EBIT coverage path: 2nd-difference of quarterly coverage (convexity)
def f47ds_f47_debt_service_coverage_covsignmag_63d_base_v051_signal(ebit, intexp):
    c = _mean(_f47_int_cov_ebit(ebit, intexp), 63)
    curv = c - 2.0 * c.shift(63) + c.shift(126)
    b = np.sign(curv) * (curv.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed coverage compression momentum (bounded month-over-month)
def f47ds_f47_debt_service_coverage_covtanh_21d_base_v052_signal(ebitda, intexp):
    c = _mean(_f47_int_cov_ebitda(ebitda, intexp), 21)
    chg = c - c.shift(21)
    b = np.tanh(chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage smoothed by EMA minus its slow EMA (coverage displacement)
def f47ds_f47_debt_service_coverage_covdisp_base_v053_signal(ncfo, intexp):
    c = _f47_cash_cov_ncfo(ncfo, intexp)
    b = c.ewm(span=42, min_periods=21).mean() - c.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current coverage from its trailing-peak in std units (stress z)
def f47ds_f47_debt_service_coverage_peakdistz_252d_base_v054_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    pk = _rmax(c, 252)
    sd = _std(c, 252)
    b = (c - pk) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage burn rate: log-slope of EBITDA coverage over a half-year
def f47ds_f47_debt_service_coverage_covburn_126d_base_v055_signal(ebitda, intexp):
    c = _mean(_f47_int_cov_ebitda(ebitda, intexp).clip(lower=0.01), 21)
    b = np.log(c.replace(0, np.nan) / c.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-charge runway acceleration: 2nd difference of cash/(interest+pref) runway
def f47ds_f47_debt_service_coverage_fcrunwayyoy_252d_base_v056_signal(cashneq, intexp, prefdivis):
    c = _mean(cashneq / (intexp + prefdivis).replace(0, np.nan), 21)
    d1 = c - c.shift(126)
    b = d1 - d1.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YoY change in short-term liquidity coverage of current debt (cushion build/erosion)
def f47ds_f47_debt_service_coverage_liqcover_63d_base_v057_signal(cashneq, fcf, debtc):
    c = _mean((cashneq + fcf) / debtc.replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of debt that is long-term (term-structure cushion)
def f47ds_f47_debt_service_coverage_ltdebtshare_63d_base_v058_signal(debtnc, debt):
    c = debtnc / debt.replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-burden coverage gap (ncfo-fcf)/intexp, YoY change (intensifying capex drag)
def f47ds_f47_debt_service_coverage_capexgapz_252d_base_v059_signal(ncfo, fcf, intexp):
    g = _mean((ncfo - fcf) / intexp.replace(0, np.nan), 21)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jaws of distress: interest-expense growth outpacing operating-cash growth, vs debt growth
def f47ds_f47_debt_service_coverage_jaws_252d_base_v060_signal(intexp, ncfo, debt):
    ig = np.log(intexp.replace(0, np.nan) / intexp.shift(252).replace(0, np.nan))
    ng = np.log(ncfo.clip(lower=0.01) / ncfo.clip(lower=0.01).shift(252))
    dg = np.log(debt.replace(0, np.nan) / debt.shift(252).replace(0, np.nan))
    # interest rising faster than cash, beyond what debt growth alone explains (rate effect)
    b = (ig - ng) - dg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block M: regime / count diversifiers ---

# count of quarters where coverage fell vs prior quarter over the last 2 years
def f47ds_f47_debt_service_coverage_declqtrs_504d_base_v061_signal(ebitda, intexp):
    c = _mean(_f47_int_cov_ebitda(ebitda, intexp), 21)
    decl = (c < c.shift(63)).astype(float)
    b = decl.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime distance: how far current cost of debt sits above its 504d median
def f47ds_f47_debt_service_coverage_costregime_504d_base_v062_signal(intexp, debt):
    c = _f47_cost_of_debt(intexp, debt)
    med = c.rolling(504, min_periods=126).median()
    b = c / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distressed-coverage regime persistence (EBITDA cov below its 40th pctile sustained)
def f47ds_f47_debt_service_coverage_distregime_252d_base_v063_signal(ebitda, intexp):
    c = _f47_int_cov_ebitda(ebitda, intexp)
    thr = c.rolling(504, min_periods=126).quantile(0.40)
    flag = (c < thr).astype(float)
    persist = flag.rolling(63, min_periods=21).mean()
    b = persist + 0.5 * (thr - c).clip(lower=0) / thr.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity-wall rising regime: fraction of year debtc/cash climbed vs a quarter ago
def f47ds_f47_debt_service_coverage_wallregime_252d_base_v064_signal(debtc, cashneq):
    r = _mean(debtc / cashneq.replace(0, np.nan), 21)
    rising = (r > r.shift(63)).astype(float)
    b = rising.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block N: ratio short/long & interaction facets ---

# fast/slow coverage ratio (recent cover relative to structural cover)
def f47ds_f47_debt_service_coverage_fastslow_base_v065_signal(ebit, intexp):
    c = _f47_int_cov_ebit(ebit, intexp)
    b = _mean(c, 21) / _mean(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-weighted maturity wall: wall pressure amplified when coverage is weak
def f47ds_f47_debt_service_coverage_wallcovint_63d_base_v066_signal(debtc, cashneq, fcf, ebitda, intexp):
    wall = _f47_maturity_wall(debtc, cashneq, fcf)
    cov = _f47_int_cov_ebitda(ebitda, intexp)
    b = _mean(wall / (1.0 + cov.clip(lower=0)), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash fixed-charge coverage: fcf vs (interest + pref divs), z-scored
def f47ds_f47_debt_service_coverage_netcap_63d_base_v067_signal(fcf, intexp, prefdivis):
    c = fcf / (intexp + prefdivis).replace(0, np.nan)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt service capacity YoY change (capacity erosion)
def f47ds_f47_debt_service_coverage_netcapyoy_252d_base_v068_signal(ncfo, intexp, prefdivis, debt):
    c = _mean((ncfo - intexp - prefdivis) / debt.replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest-to-cash burn ratio, z-scored vs own 252d history (abnormal buffer drain)
def f47ds_f47_debt_service_coverage_intvscash_63d_base_v069_signal(intexp, cashneq):
    c = intexp / cashneq.replace(0, np.nan)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum percentile of fcf coverage: rank of its quarter-over-quarter change
def f47ds_f47_debt_service_coverage_cushrank_252d_base_v070_signal(fcf, intexp):
    c = _mean(_f47_cash_cov_fcf(fcf, intexp), 21)
    chg = c - c.shift(63)
    b = _rank(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block O: final diversifiers ---

# coverage acceleration sign over a quarter (turning point in service stress)
def f47ds_f47_debt_service_coverage_covaccel_63d_base_v071_signal(ebitda, intexp):
    c = _mean(_f47_int_cov_ebitda(ebitda, intexp), 21)
    d1 = c - c.shift(63)
    d2 = d1 - d1.shift(63)
    b = np.tanh(d2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest-adjusted leverage trend: net debt / (ncfo-interest) repay-years, YoY change
def f47ds_f47_debt_service_coverage_debtebitda_63d_base_v072_signal(debt, cashneq, ncfo, intexp):
    net_debt = (debt - cashneq)
    c = _mean(net_debt / (ncfo - intexp).replace(0, np.nan), 21)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined survival-of-service: harmonic blend of coverage z and runway z (weakest-link)
def f47ds_f47_debt_service_coverage_weaklink_63d_base_v073_signal(ebitda, intexp, cashneq):
    covz = _z(_f47_int_cov_ebitda(ebitda, intexp), 252)
    runz = _z(_f47_runway_months(cashneq, intexp), 252)
    # penalize the weaker of the two standardized buffers (distress when either is low)
    b = -(np.exp(-covz) + np.exp(-runz))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest cover dispersion across the three earnings bases (ebit/ebitda/ncfo)
def f47ds_f47_debt_service_coverage_covdisp_multi_base_v074_signal(ebit, ebitda, ncfo, intexp):
    c1 = _f47_int_cov_ebit(ebit, intexp)
    c2 = _f47_int_cov_ebitda(ebitda, intexp)
    c3 = _f47_cash_cov_ncfo(ncfo, intexp)
    b = pd.concat([c1, c2, c3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-charge burden minus its own slow trend (acute fixed-charge shock)
def f47ds_f47_debt_service_coverage_fixedchgshock_base_v075_signal(intexp, prefdivis, ncfo):
    c = _f47_fixed_charge(intexp, prefdivis, ncfo)
    b = c - c.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47ds_f47_debt_service_coverage_ebitcov_63d_base_v001_signal,
    f47ds_f47_debt_service_coverage_ebitcovz_252d_base_v002_signal,
    f47ds_f47_debt_service_coverage_ebitdacov_63d_base_v003_signal,
    f47ds_f47_debt_service_coverage_ebitdacovrank_252d_base_v004_signal,
    f47ds_f47_debt_service_coverage_ncfocov_63d_base_v005_signal,
    f47ds_f47_debt_service_coverage_ncfocovz_252d_base_v006_signal,
    f47ds_f47_debt_service_coverage_fcfcov_63d_base_v007_signal,
    f47ds_f47_debt_service_coverage_fcfcovrank_252d_base_v008_signal,
    f47ds_f47_debt_service_coverage_ebitcovyoy_252d_base_v009_signal,
    f47ds_f47_debt_service_coverage_ebitdacovyoy_252d_base_v010_signal,
    f47ds_f47_debt_service_coverage_compflag_252d_base_v011_signal,
    f47ds_f47_debt_service_coverage_ncfocovqoq_63d_base_v012_signal,
    f47ds_f47_debt_service_coverage_fcfcovchgz_126d_base_v013_signal,
    f47ds_f47_debt_service_coverage_covvspeak_504d_base_v014_signal,
    f47ds_f47_debt_service_coverage_ebitdatrough_504d_base_v015_signal,
    f47ds_f47_debt_service_coverage_covdd_252d_base_v016_signal,
    f47ds_f47_debt_service_coverage_covtroughgap_252d_base_v017_signal,
    f47ds_f47_debt_service_coverage_costdebt_63d_base_v018_signal,
    f47ds_f47_debt_service_coverage_costdebtyoy_252d_base_v019_signal,
    f47ds_f47_debt_service_coverage_costdebtz_252d_base_v020_signal,
    f47ds_f47_debt_service_coverage_costdebtnc_63d_base_v021_signal,
    f47ds_f47_debt_service_coverage_fixedchg_63d_base_v022_signal,
    f47ds_f47_debt_service_coverage_fixedchgz_252d_base_v023_signal,
    f47ds_f47_debt_service_coverage_prefshare_63d_base_v024_signal,
    f47ds_f47_debt_service_coverage_fixedchgcov_63d_base_v025_signal,
    f47ds_f47_debt_service_coverage_matwall_63d_base_v026_signal,
    f47ds_f47_debt_service_coverage_matwallz_252d_base_v027_signal,
    f47ds_f47_debt_service_coverage_curdebtshare_63d_base_v028_signal,
    f47ds_f47_debt_service_coverage_matwallcash_63d_base_v029_signal,
    f47ds_f47_debt_service_coverage_runway_63d_base_v030_signal,
    f47ds_f47_debt_service_coverage_runwaynet_63d_base_v031_signal,
    f47ds_f47_debt_service_coverage_runwayyoy_252d_base_v032_signal,
    f47ds_f47_debt_service_coverage_negcovfrac_252d_base_v033_signal,
    f47ds_f47_debt_service_coverage_negcovstreak_base_v034_signal,
    f47ds_f47_debt_service_coverage_compentries_252d_base_v035_signal,
    f47ds_f47_debt_service_coverage_negncfofrac_252d_base_v036_signal,
    f47ds_f47_debt_service_coverage_accrualgap_63d_base_v037_signal,
    f47ds_f47_debt_service_coverage_dacushion_63d_base_v038_signal,
    f47ds_f47_debt_service_coverage_capexdrag_63d_base_v039_signal,
    f47ds_f47_debt_service_coverage_shortlongdiv_base_v040_signal,
    f47ds_f47_debt_service_coverage_intburden_63d_base_v041_signal,
    f47ds_f47_debt_service_coverage_intncfoburden_63d_base_v042_signal,
    f47ds_f47_debt_service_coverage_intburdenyoy_252d_base_v043_signal,
    f47ds_f47_debt_service_coverage_intburdenrank_504d_base_v044_signal,
    f47ds_f47_debt_service_coverage_collapse_252d_base_v045_signal,
    f47ds_f47_debt_service_coverage_liqadjcov_63d_base_v046_signal,
    f47ds_f47_debt_service_coverage_prefund_63d_base_v047_signal,
    f47ds_f47_debt_service_coverage_dscr_63d_base_v048_signal,
    f47ds_f47_debt_service_coverage_dscrz_252d_base_v049_signal,
    f47ds_f47_debt_service_coverage_covvol_252d_base_v050_signal,
    f47ds_f47_debt_service_coverage_covsignmag_63d_base_v051_signal,
    f47ds_f47_debt_service_coverage_covtanh_21d_base_v052_signal,
    f47ds_f47_debt_service_coverage_covdisp_base_v053_signal,
    f47ds_f47_debt_service_coverage_peakdistz_252d_base_v054_signal,
    f47ds_f47_debt_service_coverage_covburn_126d_base_v055_signal,
    f47ds_f47_debt_service_coverage_fcrunwayyoy_252d_base_v056_signal,
    f47ds_f47_debt_service_coverage_liqcover_63d_base_v057_signal,
    f47ds_f47_debt_service_coverage_ltdebtshare_63d_base_v058_signal,
    f47ds_f47_debt_service_coverage_capexgapz_252d_base_v059_signal,
    f47ds_f47_debt_service_coverage_jaws_252d_base_v060_signal,
    f47ds_f47_debt_service_coverage_declqtrs_504d_base_v061_signal,
    f47ds_f47_debt_service_coverage_costregime_504d_base_v062_signal,
    f47ds_f47_debt_service_coverage_distregime_252d_base_v063_signal,
    f47ds_f47_debt_service_coverage_wallregime_252d_base_v064_signal,
    f47ds_f47_debt_service_coverage_fastslow_base_v065_signal,
    f47ds_f47_debt_service_coverage_wallcovint_63d_base_v066_signal,
    f47ds_f47_debt_service_coverage_netcap_63d_base_v067_signal,
    f47ds_f47_debt_service_coverage_netcapyoy_252d_base_v068_signal,
    f47ds_f47_debt_service_coverage_intvscash_63d_base_v069_signal,
    f47ds_f47_debt_service_coverage_cushrank_252d_base_v070_signal,
    f47ds_f47_debt_service_coverage_covaccel_63d_base_v071_signal,
    f47ds_f47_debt_service_coverage_debtebitda_63d_base_v072_signal,
    f47ds_f47_debt_service_coverage_weaklink_63d_base_v073_signal,
    f47ds_f47_debt_service_coverage_covdisp_multi_base_v074_signal,
    f47ds_f47_debt_service_coverage_fixedchgshock_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_DEBT_SERVICE_COVERAGE_REGISTRY_001_075 = REGISTRY


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

    print("OK f47_debt_service_coverage_base_001_075_claude: %d features pass" % n_features)
