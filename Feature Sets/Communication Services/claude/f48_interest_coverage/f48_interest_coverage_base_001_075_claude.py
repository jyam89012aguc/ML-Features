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
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (interest coverage / debt-service flow) =====
def _f48ic_cover(flow, intexp):
    # generic coverage ratio: a flow divided by the (positive, small) interest expense
    return flow / intexp.replace(0, np.nan)


def _f48ic_burden(intexp, base):
    # interest burden: interest expense as a fraction of a flow/stock base
    return intexp / base.replace(0, np.nan)


def _f48ic_eff_cost(intexp, debt):
    # effective cost of debt: interest expense per unit of debt outstanding
    return intexp / debt.replace(0, np.nan)


def _f48ic_breach(flow, intexp, thr):
    # coverage-breach indicator: coverage below a threshold (1.0 == cannot service)
    cov = flow / intexp.replace(0, np.nan)
    return (cov < thr).astype(float)


def _f48ic_logcover(flow, intexp):
    # log of a positive-shifted coverage, robust to scale (flow may be negative)
    cov = flow / intexp.replace(0, np.nan)
    return np.sign(cov) * np.log1p(cov.abs())


def _f48ic_relbreach(flow, intexp, w, zthr):
    # de-trended distress flag: coverage has fallen >|zthr| std below its own w-day norm
    # (coverage dipped well below where it usually sits) -> robust to trending levels
    cov = flow / intexp.replace(0, np.nan)
    m = cov.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = cov.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    z = (cov - m) / sd
    return (z < zthr).astype(float)


# ============================================================
# === EBIT interest coverage (classic times-interest-earned) family ===

# EBIT / interest expense — classic times-interest-earned, level
def f48ic_f48_interest_coverage_ebitcov_63d_base_v001_signal(ebit, intexp):
    b = _f48ic_cover(ebit, intexp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT coverage z-scored vs its own 252d history (de-trended coverage level)
def f48ic_f48_interest_coverage_ebitcovz_252d_base_v002_signal(ebit, intexp):
    cov = _f48ic_cover(ebit, intexp)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT coverage percentile-ranked vs its own 504d history
def f48ic_f48_interest_coverage_ebitcovrank_504d_base_v003_signal(ebit, intexp):
    cov = _f48ic_cover(ebit, intexp)
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude compressed EBIT coverage (robust to scale / negative EBIT)
def f48ic_f48_interest_coverage_ebitlogcov_126d_base_v004_signal(ebit, intexp):
    b = _f48ic_logcover(_mean(ebit, 126), intexp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed EBIT coverage minus its slow EMA (coverage displacement)
def f48ic_f48_interest_coverage_ebitcovdisp_126d_base_v005_signal(ebit, intexp):
    cov = _f48ic_cover(_mean(ebit, 63), _mean(intexp, 63))
    b = cov - cov.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === EBITDA interest coverage family ===

# EBITDA / interest expense — cash-proxy coverage, level
def f48ic_f48_interest_coverage_ebitdacov_63d_base_v006_signal(ebitda, intexp):
    b = _f48ic_cover(ebitda, intexp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage z-scored vs 252d history
def f48ic_f48_interest_coverage_ebitdacovz_252d_base_v007_signal(ebitda, intexp):
    cov = _f48ic_cover(ebitda, intexp)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage percentile-ranked vs 504d history
def f48ic_f48_interest_coverage_ebitdacovrank_504d_base_v008_signal(ebitda, intexp):
    cov = _f48ic_cover(ebitda, intexp)
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage log-compressed on smoothed inputs
def f48ic_f48_interest_coverage_ebitdalogcov_126d_base_v009_signal(ebitda, intexp):
    b = _f48ic_logcover(_mean(ebitda, 126), _mean(intexp, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# the EBITDA-to-EBIT coverage wedge (D&A cushion above EBIT servicing capacity)
def f48ic_f48_interest_coverage_dacushion_126d_base_v010_signal(ebitda, ebit, intexp):
    wedge = (ebitda - ebit) / intexp.replace(0, np.nan)
    b = _mean(wedge, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === cash-flow based coverage (FCF / ncfo) family ===

# FCF / interest expense — free-cash-flow servicing capacity
def f48ic_f48_interest_coverage_fcfcov_63d_base_v011_signal(fcf, intexp):
    b = _f48ic_cover(fcf, intexp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage z-scored vs 252d history
def f48ic_f48_interest_coverage_fcfcovz_252d_base_v012_signal(fcf, intexp):
    cov = _f48ic_cover(fcf, intexp)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage log-compressed on smoothed inputs (FCF often negative for this cohort)
def f48ic_f48_interest_coverage_fcflogcov_126d_base_v013_signal(fcf, intexp):
    b = _f48ic_logcover(_mean(fcf, 126), _mean(intexp, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash flow / interest expense — cash interest coverage
def f48ic_f48_interest_coverage_ncfocov_63d_base_v014_signal(ncfo, intexp):
    b = _f48ic_cover(ncfo, intexp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage z-scored vs 252d history
def f48ic_f48_interest_coverage_ncfocovz_252d_base_v015_signal(ncfo, intexp):
    cov = _f48ic_cover(ncfo, intexp)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage percentile-ranked vs 504d history
def f48ic_f48_interest_coverage_ncfocovrank_504d_base_v016_signal(ncfo, intexp):
    cov = _f48ic_cover(ncfo, intexp)
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between cash coverage (ncfo) and accrual coverage (ebit) — quality of coverage
def f48ic_f48_interest_coverage_cashaccrualspr_126d_base_v017_signal(ncfo, ebit, intexp):
    cash = _f48ic_cover(_mean(ncfo, 63), _mean(intexp, 63))
    accr = _f48ic_cover(_mean(ebit, 63), _mean(intexp, 63))
    b = _f48ic_logcover_spread(cash, accr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def _f48ic_logcover_spread(a, b):
    fa = np.sign(a) * np.log1p(a.abs())
    fb = np.sign(b) * np.log1p(b.abs())
    return fa - fb


# spread between FCF coverage and EBITDA coverage — cash conversion of servicing capacity
def f48ic_f48_interest_coverage_fcfvsebitdacov_126d_base_v018_signal(fcf, ebitda, intexp):
    fc = _f48ic_cover(_mean(fcf, 63), _mean(intexp, 63))
    ec = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    b = _f48ic_logcover_spread(fc, ec)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === interest burden on revenue/flows family (intexp as a drag) ===

# instability of the EBITDA interest burden (volatility of intexp/ebitda servicing drag)
def f48ic_f48_interest_coverage_intburden_ebitda_126d_base_v019_signal(intexp, ebitda):
    drag = intexp / ebitda.replace(0, np.nan)
    b = _std(drag, 126) / _mean(drag, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash servicing drag deviation: intexp/ncfo relative to its own 252d structural level
def f48ic_f48_interest_coverage_intburden_ncfo_126d_base_v020_signal(intexp, ncfo):
    drag = intexp / ncfo.replace(0, np.nan)
    b = _mean(drag, 63) - _mean(drag, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden acceleration: z-scored quarter-over-quarter change in intexp/ebitda drag
def f48ic_f48_interest_coverage_intburdz_252d_base_v021_signal(intexp, ebitda):
    drag = intexp / ebitda.replace(0, np.nan)
    chg = _mean(drag, 21) - _mean(drag, 21).shift(63)
    b = _z(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in EBIT interest burden vs a quarter ago, ranked (drag-momentum regime)
def f48ic_f48_interest_coverage_intburdrank_504d_base_v022_signal(intexp, ebit):
    drag = intexp / ebit.replace(0, np.nan)
    chg = _mean(drag, 21) - _mean(drag, 21).shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === effective cost of debt family (intexp / debt) ===

# effective cost of debt: interest expense per unit of total debt, level
def f48ic_f48_interest_coverage_effcost_63d_base_v023_signal(intexp, debt):
    b = _f48ic_eff_cost(_mean(intexp, 63), _mean(debt, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective cost of debt z-scored vs 252d history (re-pricing pressure)
def f48ic_f48_interest_coverage_effcostz_252d_base_v024_signal(intexp, debt):
    ec = _f48ic_eff_cost(intexp, debt)
    b = _z(ec, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rise in effective cost of debt: current cost vs cost a year ago (refinancing at higher rates)
def f48ic_f48_interest_coverage_effcostrise_252d_base_v025_signal(intexp, debt):
    ec = _f48ic_eff_cost(_mean(intexp, 63), _mean(debt, 63))
    b = ec - ec.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective cost of debt percentile-ranked vs 504d history
def f48ic_f48_interest_coverage_effcostrank_504d_base_v026_signal(intexp, debt):
    ec = _f48ic_eff_cost(intexp, debt)
    b = _rank(ec, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective cost of current (near-term) debt: intexp per unit of current debt
def f48ic_f48_interest_coverage_effcostc_126d_base_v027_signal(intexp, debtc):
    b = _f48ic_eff_cost(_mean(intexp, 126), _mean(debtc, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === maturity-wall / near-term debt-service family (debtc) ===

# near-term maturity wall vs operating cash flow, percentile-ranked vs 504d history (rollover-risk regime)
def f48ic_f48_interest_coverage_maturwall_126d_base_v028_signal(debtc, ncfo):
    wall = _mean(debtc, 63) / _mean(ncfo, 63).replace(0, np.nan)
    b = _rank(wall, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity-wall acceleration: how fast the current-debt/ncfo wall is building, ranked
def f48ic_f48_interest_coverage_debtservwall_126d_base_v029_signal(debtc, intexp, ncfo):
    wall = (debtc + intexp) / ncfo.replace(0, np.nan)
    chg = _mean(wall, 21) - _mean(wall, 21).shift(126)
    b = _rank(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-debt servicing coverage volatility: instability of ncfo/(current debt + interest)
def f48ic_f48_interest_coverage_debtservcov_126d_base_v030_signal(ncfo, debtc, intexp):
    serv = debtc + intexp
    cov = ncfo / serv.replace(0, np.nan)
    b = _std(cov, 252) / _mean(cov, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity wall z-scored vs 252d (worsening near-term refinancing pressure)
def f48ic_f48_interest_coverage_maturwallz_252d_base_v031_signal(debtc, ncfo):
    wall = debtc / ncfo.replace(0, np.nan)
    b = _z(wall, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# near-term wall build vs interest: change in debtc relative to interest run-rate (refi pressure)
def f48ic_f48_interest_coverage_wallintratio_126d_base_v032_signal(debtc, intexp):
    chg = _mean(debtc, 21) - _mean(debtc, 21).shift(126)
    b = chg / _mean(intexp, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === net debt issuance vs interest burden family (ncfdebt) ===

# net debt issuance relative to interest expense (financing the interest, ponzi-ish)
def f48ic_f48_interest_coverage_issvsint_126d_base_v033_signal(ncfdebt, intexp):
    r = ncfdebt / intexp.replace(0, np.nan)
    b = _mean(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt issuance vs operating cash flow shortfall against interest
def f48ic_f48_interest_coverage_issgapint_126d_base_v034_signal(ncfdebt, ncfo, intexp):
    shortfall = intexp - ncfo
    r = ncfdebt / shortfall.replace(0, np.nan)
    b = _mean(np.sign(r) * np.log1p(r.abs()), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt issuance z-scored vs 252d (issuance surge regime)
def f48ic_f48_interest_coverage_issz_252d_base_v035_signal(ncfdebt, intexp):
    r = ncfdebt / intexp.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign of net issuance interacted with interest burden (leveraging into a high-burden regime)
def f48ic_f48_interest_coverage_issburdmix_126d_base_v036_signal(ncfdebt, intexp, ebitda):
    iss_sign = np.sign(_mean(ncfdebt, 63))
    burden = _mean(intexp / ebitda.replace(0, np.nan), 63)
    b = iss_sign * burden
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === coverage trajectory / slope-as-level family (still base, single value) ===

# EBIT coverage trajectory: year-over-year change in coverage level
def f48ic_f48_interest_coverage_ebitcovyoy_252d_base_v037_signal(ebit, intexp):
    cov = _f48ic_cover(_mean(ebit, 63), _mean(intexp, 63))
    b = cov - cov.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage trajectory: quarter-over-quarter change in coverage
def f48ic_f48_interest_coverage_ebitdacovqoq_63d_base_v038_signal(ebitda, intexp):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    b = cov - cov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage trajectory: half-year change in cash coverage
def f48ic_f48_interest_coverage_ncfocovh_126d_base_v039_signal(ncfo, intexp):
    cov = _f48ic_cover(_mean(ncfo, 63), _mean(intexp, 63))
    b = cov - cov.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage trajectory normalized by its own dispersion (standardized momentum)
def f48ic_f48_interest_coverage_fcfcovmomn_252d_base_v040_signal(fcf, intexp):
    cov = _f48ic_cover(_mean(fcf, 63), _mean(intexp, 63))
    chg = cov - cov.shift(126)
    b = chg / _std(cov, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === coverage-breach / distress flag family ===

# fraction of last year EBIT coverage sat in the lower fifth of its own 504d range (distress dwell)
def f48ic_f48_interest_coverage_ebitbreach_252d_base_v041_signal(ebit, intexp):
    breach = _f48ic_relbreach(ebit, intexp, 252, -0.75)
    b = breach.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thin-cushion dwell: distance of EBITDA coverage below its own 252d median, clipped
def f48ic_f48_interest_coverage_ebitdathin_252d_base_v042_signal(ebitda, intexp):
    cov = _f48ic_cover(ebitda, intexp)
    med = cov.rolling(252, min_periods=126).median()
    shortfall = (med - cov).clip(lower=0)
    b = shortfall.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year cash coverage sat in the lower quartile of its own 504d range
def f48ic_f48_interest_coverage_ncfoneg_252d_base_v043_signal(ncfo, intexp):
    breach = _f48ic_relbreach(ncfo, intexp, 252, -0.50)
    b = breach.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest recent streak of FCF coverage in its own lower-fifth distress zone, normalized
def f48ic_f48_interest_coverage_fcfbreachstreak_252d_base_v044_signal(fcf, intexp):
    breach = _f48ic_relbreach(fcf, intexp, 252, -0.60)
    grp = (breach == 0).cumsum()
    streak = breach.groupby(grp).cumsum()
    b = streak.rolling(252, min_periods=63).max() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of distinct EBIT distress-zone entries over the last year, plus depth below median
def f48ic_f48_interest_coverage_ebitbreachent_252d_base_v045_signal(ebit, intexp):
    breach = _f48ic_relbreach(ebit, intexp, 252, -0.50)
    entries = ((breach == 1) & (breach.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=126).sum()
    cov = _f48ic_cover(ebit, intexp)
    med = cov.rolling(252, min_periods=126).median()
    depth = (med - cov).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === dispersion / volatility of coverage family ===

# volatility of EBITDA coverage over 252d (instability of servicing capacity)
def f48ic_f48_interest_coverage_ebitdacovvol_252d_base_v046_signal(ebitda, intexp):
    cov = _f48ic_cover(ebitda, intexp)
    b = _std(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient-of-variation of ncfo coverage (risk-adjusted cash coverage)
def f48ic_f48_interest_coverage_ncfocovcv_252d_base_v047_signal(ncfo, intexp):
    cov = _f48ic_cover(ncfo, intexp)
    b = _std(cov, 252) / _mean(cov, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of effective cost of debt (rate-environment instability)
def f48ic_f48_interest_coverage_effcostvol_252d_base_v048_signal(intexp, debt):
    ec = _f48ic_eff_cost(intexp, debt)
    b = _std(ec, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === cross-flow coverage interactions ===

# minimum coverage across EBIT / EBITDA / ncfo / fcf (weakest-link servicing capacity)
def f48ic_f48_interest_coverage_mincover_126d_base_v049_signal(ebit, ebitda, ncfo, fcf, intexp):
    ie = intexp.replace(0, np.nan)
    c1 = _mean(ebit, 63) / ie
    c2 = _mean(ebitda, 63) / ie
    c3 = _mean(ncfo, 63) / ie
    c4 = _mean(fcf, 63) / ie
    stacked = pd.concat([c1, c2, c3, c4], axis=1)
    rng = stacked.max(axis=1) - stacked.min(axis=1)
    b = _z(rng, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of coverage across the four flows (disagreement of servicing measures)
def f48ic_f48_interest_coverage_coverdisp_126d_base_v050_signal(ebit, ebitda, ncfo, fcf, intexp):
    ie = _mean(intexp, 63).replace(0, np.nan)
    c1 = _mean(ebit, 63) / ie
    c2 = _mean(ebitda, 63) / ie
    c3 = _mean(ncfo, 63) / ie
    c4 = _mean(fcf, 63) / ie
    b = pd.concat([c1, c2, c3, c4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === debt-weighted coverage (stock x flow servicing) ===

# debt-service coverage gap: full-service shortfall vs ncfo, normalized by interest expense
def f48ic_f48_interest_coverage_dscr_126d_base_v051_signal(ncfo, intexp, debtc):
    service = intexp + debtc
    gap = service - ncfo
    b = _mean(gap, 126) / _mean(intexp, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA debt-service coverage ratio (interest + current debt), ranked
def f48ic_f48_interest_coverage_dscrebitda_504d_base_v052_signal(ebitda, intexp, debtc):
    service = intexp + debtc
    dscr = ebitda / service.replace(0, np.nan)
    b = _rank(dscr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-implied leverage from servicing: ratio of EBITDA-burden to financing-cost, ranked
# (high => earnings base is small relative to the debt the rate is charged on)
def f48ic_f48_interest_coverage_burdvscost_126d_base_v053_signal(intexp, ebitda, debt):
    burden = intexp / ebitda.replace(0, np.nan)
    cost = intexp / debt.replace(0, np.nan)
    ratio = _mean(burden, 63) / _mean(cost, 63).replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === longer-window / leverage-of-coverage variants ===

# EBIT coverage measured on 252d-smoothed flows (structural coverage level)
def f48ic_f48_interest_coverage_ebitcovstruc_252d_base_v054_signal(ebit, intexp):
    b = _mean(ebit, 252) / _mean(intexp, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage measured on 504d-smoothed flows (multi-year structural coverage)
def f48ic_f48_interest_coverage_ebitdacovstruc_504d_base_v055_signal(ebitda, intexp):
    b = _mean(ebitda, 504) / _mean(intexp, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long EBITDA coverage spread (deteriorating/improving vs structural)
def f48ic_f48_interest_coverage_covspr_63v252_base_v056_signal(ebitda, intexp):
    short = _mean(ebitda, 63) / _mean(intexp, 63).replace(0, np.nan)
    long = _mean(ebitda, 252) / _mean(intexp, 252).replace(0, np.nan)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage short-vs-long ratio (cash-coverage regime shift)
def f48ic_f48_interest_coverage_ncfocovspr_63v252_base_v057_signal(ncfo, intexp):
    short = _mean(ncfo, 63) / _mean(intexp, 63).replace(0, np.nan)
    long = _mean(ncfo, 252) / _mean(intexp, 252).replace(0, np.nan)
    b = _f48ic_logcover_spread(short, long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === interest expense growth / dynamics family ===

# interest-expense growth rate (rising debt-service cost), year-over-year log change
def f48ic_f48_interest_coverage_intgrowth_252d_base_v058_signal(intexp):
    s = _mean(intexp, 63)
    b = np.log(s.replace(0, np.nan) / s.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest-expense growth outpacing EBITDA growth (servicing cost rising faster than earnings)
def f48ic_f48_interest_coverage_intvsebitdagro_252d_base_v059_signal(intexp, ebitda):
    ig = np.log(_mean(intexp, 63).replace(0, np.nan) / _mean(intexp, 63).shift(252).replace(0, np.nan))
    eg = np.log(_mean(ebitda, 63).abs().replace(0, np.nan) / _mean(ebitda, 63).abs().shift(252).replace(0, np.nan))
    b = ig - eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of interest expense relative to its own trend (z of growth)
def f48ic_f48_interest_coverage_intgrowthz_252d_base_v060_signal(intexp):
    s = _mean(intexp, 63)
    g = np.log(s.replace(0, np.nan) / s.shift(63).replace(0, np.nan))
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === debt-to-flow servicing burden (stock vs flow) ===

# debt/ncfo repayment-years trajectory: change in years-to-repay vs a year ago (worsening burden)
def f48ic_f48_interest_coverage_debtncfo_252d_base_v061_signal(debt, ncfo):
    r = _mean(debt, 63) / _mean(ncfo, 63).replace(0, np.nan)
    rc = np.sign(r) * np.log1p(r.abs())
    b = rc - rc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to EBITDA but expressed through interest-burden lens (net leverage proxy)
def f48ic_f48_interest_coverage_debtebitdaint_252d_base_v062_signal(debt, ebitda, intexp):
    lev = debt / ebitda.replace(0, np.nan)
    burden = intexp / ebitda.replace(0, np.nan)
    b = _z(_mean(lev, 126), 252) - _z(_mean(burden, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === FCF-after-interest / discretionary cash family ===

# discretionary servicing buffer trajectory: change in (fcf-intexp)/intexp vs a year ago
def f48ic_f48_interest_coverage_fcfafterint_126d_base_v063_signal(fcf, intexp):
    buffer = (fcf - intexp) / intexp.replace(0, np.nan)
    sm = _mean(buffer, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging-capacity momentum: change in (ncfo-intexp)/debt vs a year ago (improving payoff power)
def f48ic_f48_interest_coverage_delevcap_252d_base_v064_signal(ncfo, intexp, debt):
    after = ncfo - intexp
    cap = _mean(after, 63) / _mean(debt, 63).replace(0, np.nan)
    b = cap - cap.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# post-servicing EBITDA margin headroom: (ebitda-intexp)/ebitda vs its 252d minimum (cushion)
def f48ic_f48_interest_coverage_ebitdaafterint_126d_base_v065_signal(ebitda, intexp):
    share = (ebitda - intexp) / ebitda.replace(0, np.nan)
    sm = _mean(share, 63)
    b = sm - _rmin(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === tanh-bounded / regime-distance variants ===

# bounded EBIT coverage (squashed times-interest-earned for stable scaling)
def f48ic_f48_interest_coverage_ebitcovtanh_126d_base_v066_signal(ebit, intexp):
    cov = _f48ic_cover(_mean(ebit, 63), _mean(intexp, 63))
    b = np.tanh(0.25 * cov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of EBITDA coverage from the conventional 3x investment-grade-ish threshold
def f48ic_f48_interest_coverage_covdist3x_126d_base_v067_signal(ebitda, intexp):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    b = np.tanh(0.5 * (cov - 3.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded effective cost of debt deviation from its own structural level
def f48ic_f48_interest_coverage_effcostdevtanh_252d_base_v068_signal(intexp, debt):
    ec = _f48ic_eff_cost(intexp, debt)
    dev = ec - _mean(ec, 252)
    b = np.tanh(20.0 * dev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === composite / weighted servicing-stress score ===

# composite servicing stress: high burden + rising cost + thin coverage
def f48ic_f48_interest_coverage_stress_252d_base_v069_signal(intexp, ebitda, debt):
    burden = _z(intexp / ebitda.replace(0, np.nan), 252)
    cost = _z(intexp / debt.replace(0, np.nan), 252)
    cov = _z(ebitda / intexp.replace(0, np.nan), 252)
    b = burden + cost - cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-servicing stress: rising maturity wall and falling cash coverage combined
def f48ic_f48_interest_coverage_cashstress_252d_base_v070_signal(debtc, ncfo, intexp):
    wall = _z(debtc / ncfo.replace(0, np.nan), 252)
    cov = _z(ncfo / intexp.replace(0, np.nan), 252)
    b = wall - cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance-funded interest: issuance covering the interest gap, ranked regime
def f48ic_f48_interest_coverage_issfundint_504d_base_v071_signal(ncfdebt, intexp, ncfo):
    gap = (intexp - ncfo).clip(lower=0)
    funded = ncfdebt / (gap + intexp.abs()).replace(0, np.nan)
    b = _rank(funded, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === remaining distinct facets ===

# interest expense relative to its own 252d max (how stretched current servicing cost is)
def f48ic_f48_interest_coverage_intstretch_252d_base_v072_signal(intexp):
    s = _mean(intexp, 21)
    b = s / _rmax(s, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage headroom: EBITDA coverage minus its trailing 252d minimum (cushion above worst)
def f48ic_f48_interest_coverage_covheadroom_252d_base_v073_signal(ebitda, intexp):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    b = cov - _rmin(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of debt that is current weighted by interest burden (refinancing-at-risk intensity)
def f48ic_f48_interest_coverage_currdebtburd_126d_base_v074_signal(debtc, debt, intexp, ebitda):
    curr_share = debtc / debt.replace(0, np.nan)
    burden = intexp / ebitda.replace(0, np.nan)
    b = _mean(curr_share, 126) * _mean(burden, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# twin-distress persistence: both EBIT and FCF coverage in their own lower-third zones
def f48ic_f48_interest_coverage_twindistress_252d_base_v075_signal(ebit, fcf, intexp):
    eb_low = _f48ic_relbreach(ebit, intexp, 252, -0.40)
    fc_low = _f48ic_relbreach(fcf, intexp, 252, -0.40)
    both = eb_low * fc_low
    b = both.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48ic_f48_interest_coverage_ebitcov_63d_base_v001_signal,
    f48ic_f48_interest_coverage_ebitcovz_252d_base_v002_signal,
    f48ic_f48_interest_coverage_ebitcovrank_504d_base_v003_signal,
    f48ic_f48_interest_coverage_ebitlogcov_126d_base_v004_signal,
    f48ic_f48_interest_coverage_ebitcovdisp_126d_base_v005_signal,
    f48ic_f48_interest_coverage_ebitdacov_63d_base_v006_signal,
    f48ic_f48_interest_coverage_ebitdacovz_252d_base_v007_signal,
    f48ic_f48_interest_coverage_ebitdacovrank_504d_base_v008_signal,
    f48ic_f48_interest_coverage_ebitdalogcov_126d_base_v009_signal,
    f48ic_f48_interest_coverage_dacushion_126d_base_v010_signal,
    f48ic_f48_interest_coverage_fcfcov_63d_base_v011_signal,
    f48ic_f48_interest_coverage_fcfcovz_252d_base_v012_signal,
    f48ic_f48_interest_coverage_fcflogcov_126d_base_v013_signal,
    f48ic_f48_interest_coverage_ncfocov_63d_base_v014_signal,
    f48ic_f48_interest_coverage_ncfocovz_252d_base_v015_signal,
    f48ic_f48_interest_coverage_ncfocovrank_504d_base_v016_signal,
    f48ic_f48_interest_coverage_cashaccrualspr_126d_base_v017_signal,
    f48ic_f48_interest_coverage_fcfvsebitdacov_126d_base_v018_signal,
    f48ic_f48_interest_coverage_intburden_ebitda_126d_base_v019_signal,
    f48ic_f48_interest_coverage_intburden_ncfo_126d_base_v020_signal,
    f48ic_f48_interest_coverage_intburdz_252d_base_v021_signal,
    f48ic_f48_interest_coverage_intburdrank_504d_base_v022_signal,
    f48ic_f48_interest_coverage_effcost_63d_base_v023_signal,
    f48ic_f48_interest_coverage_effcostz_252d_base_v024_signal,
    f48ic_f48_interest_coverage_effcostrise_252d_base_v025_signal,
    f48ic_f48_interest_coverage_effcostrank_504d_base_v026_signal,
    f48ic_f48_interest_coverage_effcostc_126d_base_v027_signal,
    f48ic_f48_interest_coverage_maturwall_126d_base_v028_signal,
    f48ic_f48_interest_coverage_debtservwall_126d_base_v029_signal,
    f48ic_f48_interest_coverage_debtservcov_126d_base_v030_signal,
    f48ic_f48_interest_coverage_maturwallz_252d_base_v031_signal,
    f48ic_f48_interest_coverage_wallintratio_126d_base_v032_signal,
    f48ic_f48_interest_coverage_issvsint_126d_base_v033_signal,
    f48ic_f48_interest_coverage_issgapint_126d_base_v034_signal,
    f48ic_f48_interest_coverage_issz_252d_base_v035_signal,
    f48ic_f48_interest_coverage_issburdmix_126d_base_v036_signal,
    f48ic_f48_interest_coverage_ebitcovyoy_252d_base_v037_signal,
    f48ic_f48_interest_coverage_ebitdacovqoq_63d_base_v038_signal,
    f48ic_f48_interest_coverage_ncfocovh_126d_base_v039_signal,
    f48ic_f48_interest_coverage_fcfcovmomn_252d_base_v040_signal,
    f48ic_f48_interest_coverage_ebitbreach_252d_base_v041_signal,
    f48ic_f48_interest_coverage_ebitdathin_252d_base_v042_signal,
    f48ic_f48_interest_coverage_ncfoneg_252d_base_v043_signal,
    f48ic_f48_interest_coverage_fcfbreachstreak_252d_base_v044_signal,
    f48ic_f48_interest_coverage_ebitbreachent_252d_base_v045_signal,
    f48ic_f48_interest_coverage_ebitdacovvol_252d_base_v046_signal,
    f48ic_f48_interest_coverage_ncfocovcv_252d_base_v047_signal,
    f48ic_f48_interest_coverage_effcostvol_252d_base_v048_signal,
    f48ic_f48_interest_coverage_mincover_126d_base_v049_signal,
    f48ic_f48_interest_coverage_coverdisp_126d_base_v050_signal,
    f48ic_f48_interest_coverage_dscr_126d_base_v051_signal,
    f48ic_f48_interest_coverage_dscrebitda_504d_base_v052_signal,
    f48ic_f48_interest_coverage_burdvscost_126d_base_v053_signal,
    f48ic_f48_interest_coverage_ebitcovstruc_252d_base_v054_signal,
    f48ic_f48_interest_coverage_ebitdacovstruc_504d_base_v055_signal,
    f48ic_f48_interest_coverage_covspr_63v252_base_v056_signal,
    f48ic_f48_interest_coverage_ncfocovspr_63v252_base_v057_signal,
    f48ic_f48_interest_coverage_intgrowth_252d_base_v058_signal,
    f48ic_f48_interest_coverage_intvsebitdagro_252d_base_v059_signal,
    f48ic_f48_interest_coverage_intgrowthz_252d_base_v060_signal,
    f48ic_f48_interest_coverage_debtncfo_252d_base_v061_signal,
    f48ic_f48_interest_coverage_debtebitdaint_252d_base_v062_signal,
    f48ic_f48_interest_coverage_fcfafterint_126d_base_v063_signal,
    f48ic_f48_interest_coverage_delevcap_252d_base_v064_signal,
    f48ic_f48_interest_coverage_ebitdaafterint_126d_base_v065_signal,
    f48ic_f48_interest_coverage_ebitcovtanh_126d_base_v066_signal,
    f48ic_f48_interest_coverage_covdist3x_126d_base_v067_signal,
    f48ic_f48_interest_coverage_effcostdevtanh_252d_base_v068_signal,
    f48ic_f48_interest_coverage_stress_252d_base_v069_signal,
    f48ic_f48_interest_coverage_cashstress_252d_base_v070_signal,
    f48ic_f48_interest_coverage_issfundint_504d_base_v071_signal,
    f48ic_f48_interest_coverage_intstretch_252d_base_v072_signal,
    f48ic_f48_interest_coverage_covheadroom_252d_base_v073_signal,
    f48ic_f48_interest_coverage_currdebtburd_126d_base_v074_signal,
    f48ic_f48_interest_coverage_twindistress_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_INTEREST_COVERAGE_REGISTRY_001_075 = REGISTRY


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
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis",
        "netincdis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
        "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    intexp = _fund(101, base=8e6, drift=0.02, vol=0.05).rename("intexp")
    ebit = _fund(102, base=4e7, drift=0.02, vol=0.09, allow_neg=True).rename("ebit")
    ebitda = _fund(103, base=7e7, drift=0.02, vol=0.08, allow_neg=True).rename("ebitda")
    ncfo = _fund(104, base=6e7, drift=0.02, vol=0.09, allow_neg=True).rename("ncfo")
    fcf = _fund(105, base=3e7, drift=0.02, vol=0.11, allow_neg=True).rename("fcf")
    debt = _fund(106, base=5e8, drift=0.025, vol=0.05).rename("debt")
    debtc = _fund(107, base=9e7, drift=0.025, vol=0.07).rename("debtc")
    ncfdebt = _fund(108, base=2e7, drift=0.0, vol=0.13, allow_neg=True).rename("ncfdebt")

    cols = {
        "intexp": intexp, "ebit": ebit, "ebitda": ebitda, "ncfo": ncfo,
        "fcf": fcf, "debt": debt, "debtc": debtc, "ncfdebt": ncfdebt,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
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

    print("OK f48_interest_coverage_base_001_075_claude: %d features pass" % n_features)
