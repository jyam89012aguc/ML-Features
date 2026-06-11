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
    return flow / intexp.replace(0, np.nan)


def _f48ic_eff_cost(intexp, debt):
    return intexp / debt.replace(0, np.nan)


def _f48ic_logcover(flow, intexp):
    cov = flow / intexp.replace(0, np.nan)
    return np.sign(cov) * np.log1p(cov.abs())


def _f48ic_lcspread(a, b):
    fa = np.sign(a) * np.log1p(a.abs())
    fb = np.sign(b) * np.log1p(b.abs())
    return fa - fb


def _f48ic_distress(flow, intexp, w, zthr):
    cov = flow / intexp.replace(0, np.nan)
    m = cov.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = cov.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    z = (cov - m) / sd
    return (z < zthr).astype(float)


# ============================================================
# === EBIT/EBITDA coverage — additional facets ===

# EBIT coverage smoothed over a half-year (structural earnings servicing capacity)
def f48ic_f48_interest_coverage_ebitcovh_126d_base_v076_signal(ebit, intexp):
    b = _mean(ebit, 126) / _mean(intexp, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT coverage headroom above its trailing 252d minimum (cushion vs worst recent)
def f48ic_f48_interest_coverage_ebitcovhead_252d_base_v077_signal(ebit, intexp):
    cov = _f48ic_cover(_mean(ebit, 63), _mean(intexp, 63))
    b = cov - _rmin(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage distance below its trailing 252d maximum (erosion from best)
def f48ic_f48_interest_coverage_ebitdacoverode_252d_base_v078_signal(ebitda, intexp):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    b = cov - _rmax(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded EBITDA coverage distance from a 4x comfort threshold (regime distance)
def f48ic_f48_interest_coverage_ebitdadist4x_126d_base_v079_signal(ebitda, intexp):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    b = np.tanh(0.4 * (cov - 4.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT coverage range (max-min) over 252d, normalized by its mean (coverage instability)
def f48ic_f48_interest_coverage_ebitcovrng_252d_base_v080_signal(ebit, intexp):
    cov = _f48ic_cover(ebit, intexp)
    rng = _rmax(cov, 252) - _rmin(cov, 252)
    b = rng / _mean(cov, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === cash coverage — additional facets ===

# FCF coverage smoothed over a half-year (structural free-cash servicing capacity)
def f48ic_f48_interest_coverage_fcfcovh_126d_base_v081_signal(fcf, intexp):
    b = _mean(fcf, 126) / _mean(intexp, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage smoothed over a half-year, log-compressed
def f48ic_f48_interest_coverage_ncfocovh_126d_base_v082_signal(ncfo, intexp):
    b = _f48ic_logcover(_mean(ncfo, 126), _mean(intexp, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage percentile-ranked vs its own 504d history (relative free-cash servicing)
def f48ic_f48_interest_coverage_fcfcovrank_504d_base_v083_signal(fcf, intexp):
    cov = _f48ic_cover(_mean(fcf, 63), _mean(intexp, 63))
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage volatility (instability of free-cash servicing capacity)
def f48ic_f48_interest_coverage_fcfcovvol_252d_base_v084_signal(fcf, intexp):
    cov = _f48ic_cover(fcf, intexp)
    b = _std(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex conversion of servicing capacity: free-cash coverage as a share of cash coverage
# (fcf/ncfo expressed through the interest-coverage lens; low => capex eats servicing capacity)
def f48ic_f48_interest_coverage_capexdrag_126d_base_v085_signal(ncfo, fcf, intexp):
    nc = _f48ic_cover(_mean(ncfo, 63), _mean(intexp, 63))
    fc = _f48ic_cover(_mean(fcf, 63), _mean(intexp, 63))
    ratio = fc / nc.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === interest burden on flows — additional facets ===

# interest burden on FCF trajectory: half-year change in intexp/fcf free-cash drag
def f48ic_f48_interest_coverage_intburdfcf_126d_base_v086_signal(intexp, fcf):
    drag = intexp / fcf.replace(0, np.nan)
    lc = np.sign(_mean(drag, 21)) * np.log1p(_mean(drag, 21).abs())
    b = lc - lc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden on EBIT volatility (instability of accrual-earnings servicing drag)
def f48ic_f48_interest_coverage_intburdebit_126d_base_v087_signal(intexp, ebit):
    drag = intexp / ebit.replace(0, np.nan)
    b = _std(drag, 126) / _mean(drag, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden on ncfo z-scored vs 252d (cash-drag regime extremity)
def f48ic_f48_interest_coverage_intburdncfoz_252d_base_v088_signal(intexp, ncfo):
    drag = intexp / ncfo.replace(0, np.nan)
    b = _z(drag, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden on EBITDA trajectory: half-year change (rising/falling drag)
def f48ic_f48_interest_coverage_intburdtraj_126d_base_v089_signal(intexp, ebitda):
    drag = _mean(intexp / ebitda.replace(0, np.nan), 21)
    b = drag - drag.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === effective cost of debt — additional facets ===

# effective cost on non-current/total debt, smoothed over a year (structural rate)
def f48ic_f48_interest_coverage_effcoststruc_252d_base_v090_signal(intexp, debt):
    b = _mean(intexp, 252) / _mean(debt, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective-cost momentum normalized by its dispersion (standardized re-pricing speed)
def f48ic_f48_interest_coverage_effcostmomn_252d_base_v091_signal(intexp, debt):
    ec = _f48ic_eff_cost(_mean(intexp, 63), _mean(debt, 63))
    chg = ec - ec.shift(126)
    b = chg / _std(ec, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective cost on current debt vs on total debt (term-structure of financing cost)
def f48ic_f48_interest_coverage_costtermspr_126d_base_v092_signal(intexp, debtc, debt):
    cost_c = intexp / debtc.replace(0, np.nan)
    cost_t = intexp / debt.replace(0, np.nan)
    b = _mean(cost_c, 126) - _mean(cost_t, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective cost distance above its 252d minimum (rate cushion gone)
def f48ic_f48_interest_coverage_effcosthead_252d_base_v093_signal(intexp, debt):
    ec = _f48ic_eff_cost(_mean(intexp, 21), _mean(debt, 21))
    b = ec - _rmin(ec, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === maturity wall / near-term refinancing — additional facets ===

# current-debt share of total debt (refinancing concentration in the near term)
def f48ic_f48_interest_coverage_currshare_126d_base_v094_signal(debtc, debt):
    share = debtc / debt.replace(0, np.nan)
    b = _mean(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-debt share trajectory: change vs a year ago (maturity wall building up front)
def f48ic_f48_interest_coverage_currsharetraj_252d_base_v095_signal(debtc, debt):
    share = _mean(debtc / debt.replace(0, np.nan), 63)
    b = share - share.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity wall against FCF, z-deviation from its own 252d structural level (free-cash rollover stress)
def f48ic_f48_interest_coverage_wallfcf_126d_base_v096_signal(debtc, fcf):
    wall = debtc / fcf.replace(0, np.nan)
    lc = np.sign(wall) * np.log1p(wall.abs())
    b = _z(lc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity wall against EBITDA (earnings rollover capacity), ranked
def f48ic_f48_interest_coverage_wallebitda_504d_base_v097_signal(debtc, ebitda):
    wall = _mean(debtc, 63) / _mean(ebitda, 63).replace(0, np.nan)
    b = _rank(wall, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full near-term service (interest + current debt) against EBITDA, distance from comfort
def f48ic_f48_interest_coverage_servebitda_126d_base_v098_signal(intexp, debtc, ebitda):
    service = intexp + debtc
    cov = _mean(ebitda, 63) / service.replace(0, np.nan)
    b = np.tanh(0.5 * (cov - 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === net debt issuance / financing — additional facets ===

# net debt issuance relative to operating cash flow (external funding reliance)
def f48ic_f48_interest_coverage_issncfo_126d_base_v099_signal(ncfdebt, ncfo):
    r = ncfdebt / ncfo.replace(0, np.nan)
    b = _mean(np.sign(r) * np.log1p(r.abs()), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt issuance relative to interest expense, ranked (issuance-funding regime)
def f48ic_f48_interest_coverage_issintrank_504d_base_v100_signal(ncfdebt, intexp):
    r = _mean(ncfdebt, 63) / _mean(intexp, 63).replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year net issuance ran below its own norm while interest burden ran above its norm
# (pulling back on new debt precisely when servicing drag is elevated -> defensive deleveraging)
def f48ic_f48_interest_coverage_repayburden_252d_base_v101_signal(ncfdebt, intexp, ebitda):
    iss = _mean(ncfdebt, 21)
    low_iss = (iss < _mean(ncfdebt, 252)).astype(float)
    burd = intexp / ebitda.replace(0, np.nan)
    high_burd = (burd > _mean(burd, 252)).astype(float)
    both = low_iss * high_burd
    b = both.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt issuance volatility relative to interest (financing-policy instability)
def f48ic_f48_interest_coverage_issvol_252d_base_v102_signal(ncfdebt, intexp):
    r = ncfdebt / intexp.replace(0, np.nan)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === coverage trajectory / momentum — additional facets ===

# EBIT coverage standardized momentum over a half-year (de-noised trajectory)
def f48ic_f48_interest_coverage_ebitcovmomn_126d_base_v103_signal(ebit, intexp):
    cov = _f48ic_cover(_mean(ebit, 63), _mean(intexp, 63))
    chg = cov - cov.shift(63)
    b = chg / _std(cov, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage year-over-year log change (structural servicing growth)
def f48ic_f48_interest_coverage_ebitdacovyoy_252d_base_v104_signal(ebitda, intexp):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    b = _f48ic_lcspread(cov, cov.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage acceleration: recent quarterly change minus prior quarterly change
def f48ic_f48_interest_coverage_ncfocovaccel_126d_base_v105_signal(ncfo, intexp):
    cov = _f48ic_cover(_mean(ncfo, 63), _mean(intexp, 63))
    chg = cov - cov.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage trajectory ranked (improving/deteriorating free-cash servicing regime)
def f48ic_f48_interest_coverage_fcfcovtrajrank_504d_base_v106_signal(fcf, intexp):
    cov = _f48ic_cover(_mean(fcf, 63), _mean(intexp, 63))
    chg = cov - cov.shift(126)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === distress / breach — additional facets ===

# fraction of last year EBITDA coverage dwelt in its own lower-fifth distress zone
def f48ic_f48_interest_coverage_ebitdadistress_252d_base_v107_signal(ebitda, intexp):
    d = _f48ic_distress(ebitda, intexp, 252, -0.75)
    b = d.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest ncfo-coverage distress streak over a year, normalized (persistent cash distress)
def f48ic_f48_interest_coverage_ncfostreak_252d_base_v108_signal(ncfo, intexp):
    d = _f48ic_distress(ncfo, intexp, 252, -0.60)
    grp = (d == 0).cumsum()
    streak = d.groupby(grp).cumsum()
    b = streak.rolling(252, min_periods=63).max() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depth of EBIT coverage below its own 252d median (continuous distress intensity)
def f48ic_f48_interest_coverage_ebitdepth_126d_base_v109_signal(ebit, intexp):
    cov = _f48ic_cover(ebit, intexp)
    med = cov.rolling(252, min_periods=126).median()
    shortfall = (med - cov).clip(lower=0)
    b = shortfall.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of FCF-coverage distress entries over a year plus mean depth (recurring free-cash stress)
def f48ic_f48_interest_coverage_fcfentries_252d_base_v110_signal(fcf, intexp):
    d = _f48ic_distress(fcf, intexp, 252, -0.50)
    entries = ((d == 1) & (d.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=126).sum()
    cov = _f48ic_cover(fcf, intexp)
    med = cov.rolling(252, min_periods=126).median()
    depth = (med - cov).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === cross-flow / composite — additional facets ===

# median coverage across the four flows (central servicing tendency), log-compressed
def f48ic_f48_interest_coverage_medcover_126d_base_v111_signal(ebit, ebitda, ncfo, fcf, intexp):
    ie = _mean(intexp, 63).replace(0, np.nan)
    c1 = _mean(ebit, 63) / ie
    c2 = _mean(ebitda, 63) / ie
    c3 = _mean(ncfo, 63) / ie
    c4 = _mean(fcf, 63) / ie
    med = pd.concat([c1, c2, c3, c4], axis=1).median(axis=1)
    b = np.sign(med) * np.log1p(med.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of flows whose coverage exceeds 2x (breadth of comfortable servicing)
def f48ic_f48_interest_coverage_coverbreadth_126d_base_v112_signal(ebit, ebitda, ncfo, fcf, intexp):
    ie = _mean(intexp, 63).replace(0, np.nan)
    cnt = ((_mean(ebit, 63) / ie) > 2.0).astype(float)
    cnt = cnt + ((_mean(ebitda, 63) / ie) > 2.0).astype(float)
    cnt = cnt + ((_mean(ncfo, 63) / ie) > 2.0).astype(float)
    cnt = cnt + ((_mean(fcf, 63) / ie) > 2.0).astype(float)
    b = _mean(cnt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-accrual coverage agreement (sign concordance of ncfo and ebit coverage trajectories)
def f48ic_f48_interest_coverage_signconcord_126d_base_v113_signal(ncfo, ebit, intexp):
    nc = _f48ic_cover(_mean(ncfo, 63), _mean(intexp, 63))
    ec = _f48ic_cover(_mean(ebit, 63), _mean(intexp, 63))
    agree = np.sign(nc - nc.shift(63)) * np.sign(ec - ec.shift(63))
    b = _mean(agree, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === debt-service coverage (DSCR) variants ===

# DSCR on FCF trajectory: change in free-cash/(interest+current debt) vs a year ago
def f48ic_f48_interest_coverage_dscrfcf_126d_base_v114_signal(fcf, intexp, debtc):
    service = intexp + debtc
    dscr = _mean(fcf, 63) / service.replace(0, np.nan)
    lc = np.sign(dscr) * np.log1p(dscr.abs())
    b = lc - lc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSCR gap on EBITDA: full-service shortfall vs ebitda, normalized by interest
def f48ic_f48_interest_coverage_dscrgapebitda_126d_base_v115_signal(ebitda, intexp, debtc):
    service = intexp + debtc
    gap = service - ebitda
    b = _mean(gap, 126) / _mean(intexp, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSCR trajectory: change in ncfo/(interest+current debt) vs a year ago
def f48ic_f48_interest_coverage_dscrtraj_252d_base_v116_signal(ncfo, intexp, debtc):
    service = intexp + debtc
    dscr = _mean(ncfo, 63) / service.replace(0, np.nan)
    b = dscr - dscr.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === stock-vs-flow leverage through servicing lens ===

# debt relative to EBITDA (gross leverage), log-compressed level
def f48ic_f48_interest_coverage_debtebitda_252d_base_v117_signal(debt, ebitda):
    r = _mean(debt, 126) / _mean(ebitda, 126).replace(0, np.nan)
    b = np.sign(r) * np.log1p(r.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to FCF (years to repay from free cash), ranked
def f48ic_f48_interest_coverage_debtfcf_504d_base_v118_signal(debt, fcf):
    r = _mean(debt, 126) / _mean(fcf, 126).replace(0, np.nan)
    b = _rank(np.sign(r) * np.log1p(r.abs()), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-service intensity trajectory: change in (interest+current debt)/total debt vs a year ago
def f48ic_f48_interest_coverage_servintensity_126d_base_v119_signal(intexp, debtc, debt):
    intensity = _mean((intexp + debtc) / debt.replace(0, np.nan), 21)
    b = intensity - intensity.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === discretionary-cash-after-service ===

# operating cash after full service relative to interest (true discretionary buffer)
def f48ic_f48_interest_coverage_afterservbuf_126d_base_v120_signal(ncfo, intexp, debtc):
    after = ncfo - intexp - debtc
    b = _mean(after, 126) / _mean(intexp, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-after-interest to debt, standardized momentum (de-noised change in pay-down capacity)
def f48ic_f48_interest_coverage_ebitdaafterdebt_252d_base_v121_signal(ebitda, intexp, debt):
    after = ebitda - intexp
    r = _mean(after, 63) / _mean(debt, 63).replace(0, np.nan)
    chg = r - r.shift(126)
    b = chg / _std(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT interest-share trajectory: change in intexp/(|ebit|+intexp) vs a year ago (rising claim)
def f48ic_f48_interest_coverage_intshareebit_126d_base_v122_signal(intexp, ebit):
    share = _mean(intexp / (ebit.abs() + intexp).replace(0, np.nan), 21)
    b = share - share.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === bounded / regime-distance — additional facets ===

# bounded ncfo coverage deviation from its own structural level (squashed cash-coverage swing)
def f48ic_f48_interest_coverage_ncfocovtanh_126d_base_v123_signal(ncfo, intexp):
    cov = _f48ic_cover(_mean(ncfo, 63), _mean(intexp, 63))
    b = np.tanh(0.3 * (cov - _mean(cov, 252)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded effective-cost rise vs a year ago (squashed re-pricing shock)
def f48ic_f48_interest_coverage_costrisetanh_252d_base_v124_signal(intexp, debt):
    ec = _f48ic_eff_cost(_mean(intexp, 63), _mean(debt, 63))
    b = np.tanh(40.0 * (ec - ec.shift(252)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded FCF coverage deviation from its own trailing median (squashed free-cash servicing swing)
def f48ic_f48_interest_coverage_fcfshorttanh_126d_base_v125_signal(fcf, intexp):
    cov = _f48ic_cover(_mean(fcf, 63), _mean(intexp, 63))
    med = cov.rolling(252, min_periods=126).median()
    b = np.tanh(0.5 * (cov - med))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === interest-expense dynamics — additional facets ===

# interest-expense quarter-over-quarter growth, standardized (servicing-cost acceleration)
def f48ic_f48_interest_coverage_intgrowq_126d_base_v126_signal(intexp):
    s = _mean(intexp, 21)
    g = np.log(s.replace(0, np.nan) / s.shift(63).replace(0, np.nan))
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest expense relative to its own 252d mean (run-rate stretch)
def f48ic_f48_interest_coverage_intstretch_252d_base_v127_signal(intexp):
    s = _mean(intexp, 21)
    b = s / _mean(intexp, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rate-vs-balance divergence, standardized: how much interest growth outran debt growth (z)
def f48ic_f48_interest_coverage_ratevsbalance_252d_base_v128_signal(intexp, debt):
    ig = np.log(_mean(intexp, 63).replace(0, np.nan) / _mean(intexp, 63).shift(126).replace(0, np.nan))
    dg = np.log(_mean(debt, 63).replace(0, np.nan) / _mean(debt, 63).shift(126).replace(0, np.nan))
    b = _z(ig - dg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === composite servicing-stress — additional facets ===

# composite cash-servicing stress: rising burden + rising cost + falling cash coverage
def f48ic_f48_interest_coverage_cashstress2_252d_base_v129_signal(intexp, ncfo, debt):
    burden = _z(intexp / ncfo.replace(0, np.nan), 252)
    cost = _z(intexp / debt.replace(0, np.nan), 252)
    cov = _z(ncfo / intexp.replace(0, np.nan), 252)
    b = burden + cost - cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# refinancing-stress score: near-term wall up + effective cost up (rollover at higher rates)
def f48ic_f48_interest_coverage_refistress_252d_base_v130_signal(debtc, ncfo, intexp, debt):
    wall = _z(debtc / ncfo.replace(0, np.nan), 252)
    cost = _z(intexp / debt.replace(0, np.nan), 252)
    b = wall + cost
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-quality-of-coverage stress: accrual coverage strong but cash coverage weak
def f48ic_f48_interest_coverage_qualstress_252d_base_v131_signal(ebit, ncfo, intexp):
    accr = _z(ebit / intexp.replace(0, np.nan), 252)
    cash = _z(ncfo / intexp.replace(0, np.nan), 252)
    b = accr - cash
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === longer-window structural variants ===

# EBIT coverage structural level over 504d (multi-year times-interest-earned)
def f48ic_f48_interest_coverage_ebitcovstruc_504d_base_v132_signal(ebit, intexp):
    b = _mean(ebit, 504) / _mean(intexp, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo coverage drawdown vs its 504d structural peak (multi-year cash-servicing erosion)
def f48ic_f48_interest_coverage_ncfocovstruc_504d_base_v133_signal(ncfo, intexp):
    cov = _f48ic_cover(_mean(ncfo, 63), _mean(intexp, 63))
    peak = _rmax(cov, 504)
    b = cov / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long FCF coverage ratio, percentile-ranked (free-cash regime-shift extremity)
def f48ic_f48_interest_coverage_fcfcovspr_63v252_base_v134_signal(fcf, intexp):
    short = _mean(fcf, 63) / _mean(intexp, 63).replace(0, np.nan)
    long = _mean(fcf, 252) / _mean(intexp, 252).replace(0, np.nan)
    ratio = short / long.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long effective cost of debt spread (recent re-pricing vs structural rate)
def f48ic_f48_interest_coverage_costspr_63v252_base_v135_signal(intexp, debt):
    short = _mean(intexp, 63) / _mean(debt, 63).replace(0, np.nan)
    long = _mean(intexp, 252) / _mean(debt, 252).replace(0, np.nan)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === remaining diversified facets ===

# coverage convexity: how far EBITDA coverage sits in the convex (squared) upper tail vs median
def f48ic_f48_interest_coverage_covconvex_252d_base_v136_signal(ebitda, intexp):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    med = cov.rolling(252, min_periods=126).median()
    dev = cov - med
    b = np.sign(dev) * (dev ** 2) / (med.abs() + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest-burden breadth: count of flows where intexp exceeds 30% of the flow (broad drag)
def f48ic_f48_interest_coverage_burdbreadth_126d_base_v137_signal(ebit, ebitda, ncfo, fcf, intexp):
    ie = _mean(intexp, 63)
    cnt = (ie > 0.30 * _mean(ebit, 63).abs()).astype(float)
    cnt = cnt + (ie > 0.30 * _mean(ebitda, 63).abs()).astype(float)
    cnt = cnt + (ie > 0.30 * _mean(ncfo, 63).abs()).astype(float)
    cnt = cnt + (ie > 0.30 * _mean(fcf, 63).abs()).astype(float)
    b = _mean(cnt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance funded coverage gap: issuance bridging (interest - ncfo), z-scored trajectory
def f48ic_f48_interest_coverage_issbridge_504d_base_v138_signal(ncfdebt, intexp, ncfo):
    gap = (intexp - ncfo).clip(lower=0)
    bridge = _mean(ncfdebt, 63) / (_mean(gap, 63) + _mean(intexp, 63)).replace(0, np.nan)
    b = _z(bridge - bridge.shift(126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity-wall stress relative to cash buffer after interest, percentile-ranked (rollover-squeeze regime)
def f48ic_f48_interest_coverage_wallsqueeze_126d_base_v139_signal(debtc, ncfo, intexp):
    buffer = (ncfo - intexp)
    squeeze = _mean(debtc, 63) / _mean(buffer, 63).replace(0, np.nan)
    lc = np.sign(squeeze) * np.log1p(squeeze.abs())
    b = _rank(lc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage drawdown: current EBITDA coverage vs its trailing 504d peak (servicing erosion)
def f48ic_f48_interest_coverage_covdrawdown_504d_base_v140_signal(ebitda, intexp):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    peak = _rmax(cov, 504)
    b = cov / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year ncfo covered at least interest plus half the near-term maturity wall
# (partial self-funding of debt service from operations)
def f48ic_f48_interest_coverage_selffund_252d_base_v141_signal(ncfo, intexp, debtc):
    covered = (ncfo >= (intexp + 0.5 * debtc)).astype(float)
    b = covered.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT coverage skewness proxy: (mean - median)/std over 252d (asymmetry of servicing capacity)
def f48ic_f48_interest_coverage_covskew_252d_base_v142_signal(ebit, intexp):
    cov = _f48ic_cover(ebit, intexp)
    m = _mean(cov, 252)
    med = cov.rolling(252, min_periods=126).median()
    b = (m - med) / _std(cov, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rising-cost & shrinking-coverage interaction (z of cost times z of inverse coverage)
def f48ic_f48_interest_coverage_costcovmix_252d_base_v143_signal(intexp, debt, ebitda):
    cost_z = _z(_f48ic_eff_cost(intexp, debt), 252)
    cov_z = _z(_f48ic_cover(ebitda, intexp), 252)
    b = cost_z * (-cov_z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net leverage-of-servicing: (interest + current debt) growth vs EBITDA growth divergence
def f48ic_f48_interest_coverage_servgrowdiv_252d_base_v144_signal(intexp, debtc, ebitda):
    serv = _mean(intexp + debtc, 63)
    sg = np.log(serv.replace(0, np.nan) / serv.shift(252).replace(0, np.nan))
    eg = np.log(_mean(ebitda, 63).abs().replace(0, np.nan) / _mean(ebitda, 63).abs().shift(252).replace(0, np.nan))
    b = _rank(sg - eg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage persistence: fraction of last year EBITDA coverage stayed above its own median
def f48ic_f48_interest_coverage_covpersist_252d_base_v145_signal(ebitda, intexp):
    cov = _f48ic_cover(ebitda, intexp)
    med = cov.rolling(504, min_periods=252).median()
    above = (cov >= med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest coverage vs effective cost interaction (coverage per unit of financing rate)
def f48ic_f48_interest_coverage_covpercost_252d_base_v146_signal(ebitda, intexp, debt):
    cov = _f48ic_cover(_mean(ebitda, 63), _mean(intexp, 63))
    cost = _f48ic_eff_cost(_mean(intexp, 63), _mean(debt, 63))
    b = cov * cost
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash buffer after full service relative to debt (organic deleveraging power)
def f48ic_f48_interest_coverage_organicdelev_252d_base_v147_signal(fcf, intexp, debtc, debt):
    after = fcf - intexp - debtc
    b = _mean(after, 126) / _mean(debt, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# instability of the FCF interest burden (volatility of intexp/fcf free-cash drag)
def f48ic_f48_interest_coverage_intburdfcftraj_126d_base_v148_signal(intexp, fcf):
    drag = intexp / fcf.replace(0, np.nan)
    lc = np.sign(drag) * np.log1p(drag.abs())
    b = _std(lc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage agreement breadth: dispersion of coverage trajectories across the four flows
def f48ic_f48_interest_coverage_trajdisp_126d_base_v149_signal(ebit, ebitda, ncfo, fcf, intexp):
    ie = _mean(intexp, 63).replace(0, np.nan)
    t1 = (_mean(ebit, 63) / ie).diff(63)
    t2 = (_mean(ebitda, 63) / ie).diff(63)
    t3 = (_mean(ncfo, 63) / ie).diff(63)
    t4 = (_mean(fcf, 63) / ie).diff(63)
    b = pd.concat([t1, t2, t3, t4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined servicing-fragility: thin coverage AND high near-term wall AND rising cost (z-sum)
def f48ic_f48_interest_coverage_fragility_252d_base_v150_signal(ebitda, intexp, debtc, ncfo, debt):
    thin = -_z(_f48ic_cover(ebitda, intexp), 252)
    wall = _z(debtc / ncfo.replace(0, np.nan), 252)
    cost = _z(intexp / debt.replace(0, np.nan), 252)
    b = (thin + wall + cost) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48ic_f48_interest_coverage_ebitcovh_126d_base_v076_signal,
    f48ic_f48_interest_coverage_ebitcovhead_252d_base_v077_signal,
    f48ic_f48_interest_coverage_ebitdacoverode_252d_base_v078_signal,
    f48ic_f48_interest_coverage_ebitdadist4x_126d_base_v079_signal,
    f48ic_f48_interest_coverage_ebitcovrng_252d_base_v080_signal,
    f48ic_f48_interest_coverage_fcfcovh_126d_base_v081_signal,
    f48ic_f48_interest_coverage_ncfocovh_126d_base_v082_signal,
    f48ic_f48_interest_coverage_fcfcovrank_504d_base_v083_signal,
    f48ic_f48_interest_coverage_fcfcovvol_252d_base_v084_signal,
    f48ic_f48_interest_coverage_capexdrag_126d_base_v085_signal,
    f48ic_f48_interest_coverage_intburdfcf_126d_base_v086_signal,
    f48ic_f48_interest_coverage_intburdebit_126d_base_v087_signal,
    f48ic_f48_interest_coverage_intburdncfoz_252d_base_v088_signal,
    f48ic_f48_interest_coverage_intburdtraj_126d_base_v089_signal,
    f48ic_f48_interest_coverage_effcoststruc_252d_base_v090_signal,
    f48ic_f48_interest_coverage_effcostmomn_252d_base_v091_signal,
    f48ic_f48_interest_coverage_costtermspr_126d_base_v092_signal,
    f48ic_f48_interest_coverage_effcosthead_252d_base_v093_signal,
    f48ic_f48_interest_coverage_currshare_126d_base_v094_signal,
    f48ic_f48_interest_coverage_currsharetraj_252d_base_v095_signal,
    f48ic_f48_interest_coverage_wallfcf_126d_base_v096_signal,
    f48ic_f48_interest_coverage_wallebitda_504d_base_v097_signal,
    f48ic_f48_interest_coverage_servebitda_126d_base_v098_signal,
    f48ic_f48_interest_coverage_issncfo_126d_base_v099_signal,
    f48ic_f48_interest_coverage_issintrank_504d_base_v100_signal,
    f48ic_f48_interest_coverage_repayburden_252d_base_v101_signal,
    f48ic_f48_interest_coverage_issvol_252d_base_v102_signal,
    f48ic_f48_interest_coverage_ebitcovmomn_126d_base_v103_signal,
    f48ic_f48_interest_coverage_ebitdacovyoy_252d_base_v104_signal,
    f48ic_f48_interest_coverage_ncfocovaccel_126d_base_v105_signal,
    f48ic_f48_interest_coverage_fcfcovtrajrank_504d_base_v106_signal,
    f48ic_f48_interest_coverage_ebitdadistress_252d_base_v107_signal,
    f48ic_f48_interest_coverage_ncfostreak_252d_base_v108_signal,
    f48ic_f48_interest_coverage_ebitdepth_126d_base_v109_signal,
    f48ic_f48_interest_coverage_fcfentries_252d_base_v110_signal,
    f48ic_f48_interest_coverage_medcover_126d_base_v111_signal,
    f48ic_f48_interest_coverage_coverbreadth_126d_base_v112_signal,
    f48ic_f48_interest_coverage_signconcord_126d_base_v113_signal,
    f48ic_f48_interest_coverage_dscrfcf_126d_base_v114_signal,
    f48ic_f48_interest_coverage_dscrgapebitda_126d_base_v115_signal,
    f48ic_f48_interest_coverage_dscrtraj_252d_base_v116_signal,
    f48ic_f48_interest_coverage_debtebitda_252d_base_v117_signal,
    f48ic_f48_interest_coverage_debtfcf_504d_base_v118_signal,
    f48ic_f48_interest_coverage_servintensity_126d_base_v119_signal,
    f48ic_f48_interest_coverage_afterservbuf_126d_base_v120_signal,
    f48ic_f48_interest_coverage_ebitdaafterdebt_252d_base_v121_signal,
    f48ic_f48_interest_coverage_intshareebit_126d_base_v122_signal,
    f48ic_f48_interest_coverage_ncfocovtanh_126d_base_v123_signal,
    f48ic_f48_interest_coverage_costrisetanh_252d_base_v124_signal,
    f48ic_f48_interest_coverage_fcfshorttanh_126d_base_v125_signal,
    f48ic_f48_interest_coverage_intgrowq_126d_base_v126_signal,
    f48ic_f48_interest_coverage_intstretch_252d_base_v127_signal,
    f48ic_f48_interest_coverage_ratevsbalance_252d_base_v128_signal,
    f48ic_f48_interest_coverage_cashstress2_252d_base_v129_signal,
    f48ic_f48_interest_coverage_refistress_252d_base_v130_signal,
    f48ic_f48_interest_coverage_qualstress_252d_base_v131_signal,
    f48ic_f48_interest_coverage_ebitcovstruc_504d_base_v132_signal,
    f48ic_f48_interest_coverage_ncfocovstruc_504d_base_v133_signal,
    f48ic_f48_interest_coverage_fcfcovspr_63v252_base_v134_signal,
    f48ic_f48_interest_coverage_costspr_63v252_base_v135_signal,
    f48ic_f48_interest_coverage_covconvex_252d_base_v136_signal,
    f48ic_f48_interest_coverage_burdbreadth_126d_base_v137_signal,
    f48ic_f48_interest_coverage_issbridge_504d_base_v138_signal,
    f48ic_f48_interest_coverage_wallsqueeze_126d_base_v139_signal,
    f48ic_f48_interest_coverage_covdrawdown_504d_base_v140_signal,
    f48ic_f48_interest_coverage_selffund_252d_base_v141_signal,
    f48ic_f48_interest_coverage_covskew_252d_base_v142_signal,
    f48ic_f48_interest_coverage_costcovmix_252d_base_v143_signal,
    f48ic_f48_interest_coverage_servgrowdiv_252d_base_v144_signal,
    f48ic_f48_interest_coverage_covpersist_252d_base_v145_signal,
    f48ic_f48_interest_coverage_covpercost_252d_base_v146_signal,
    f48ic_f48_interest_coverage_organicdelev_252d_base_v147_signal,
    f48ic_f48_interest_coverage_intburdfcftraj_126d_base_v148_signal,
    f48ic_f48_interest_coverage_trajdisp_126d_base_v149_signal,
    f48ic_f48_interest_coverage_fragility_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_INTEREST_COVERAGE_REGISTRY_076_150 = REGISTRY


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

    print("OK f48_interest_coverage_base_076_150_claude: %d features pass" % n_features)
