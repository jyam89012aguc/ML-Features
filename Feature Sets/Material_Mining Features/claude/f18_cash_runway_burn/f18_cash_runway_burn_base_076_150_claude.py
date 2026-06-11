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


# ===== folder domain primitives (cash runway / burn) =====
def _f18_burn_opex(opex, ncfo):
    return (opex - ncfo).clip(lower=0.0)


def _f18_burn_capex(ncfo, capex):
    return (-ncfo + capex).clip(lower=0.0)


def _f18_runway_opex(cashneq, opex, ncfo):
    burn = (opex - ncfo).clip(lower=0.0)
    return cashneq / burn.replace(0, np.nan)


def _f18_runway_capex(cashneq, ncfo, capex):
    burn = (-ncfo + capex).clip(lower=0.0)
    return cashneq / burn.replace(0, np.nan)


def _f18_coverage(ncfo, opex):
    return ncfo / opex.replace(0, np.nan)


# ============================================================
# --- RUNWAY at wider windows / new normalizations ---
# opex-runway ranked vs 252d, scaled by recent depletion (distress percentile)
def f18cr_f18_cash_runway_burn_runwaypctdepl_252d_base_v076_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-runway minus its 252d median (level vs structural median runway)
def f18cr_f18_cash_runway_burn_runwaymeddev_252d_base_v077_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    med = r.rolling(252, min_periods=126).median()
    b = r - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-runway smoothed over a half year (structural FCF survival)
def f18cr_f18_cash_runway_burn_runwaycapexsm_126d_base_v078_signal(cashneq, ncfo, capex):
    r = np.log1p(_f18_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    b = r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-runway displacement vs slow EMA (acute FCF squeeze)
def f18cr_f18_cash_runway_burn_runwaycapexdisp_base_v079_signal(cashneq, ncfo, capex):
    r = np.log1p(_f18_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# months-of-cash vs 504d median (long-horizon survival deviation)
def f18cr_f18_cash_runway_burn_monthsmeddev_504d_base_v080_signal(cashneq, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    m = (3.0 * cashneq / burn.replace(0, np.nan)).clip(upper=120.0)
    med = m.rolling(504, min_periods=252).median()
    b = m - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BURN composition: opex vs capex burn balance ---
# which burn dominates: opex-burn share of total (opex + capex) burn
def f18cr_f18_cash_runway_burn_burnmix_63d_base_v081_signal(opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    b = (bo / (bo + bc).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total burn (opex + capex) over cash, log-compressed (combined depletion)
def f18cr_f18_cash_runway_burn_totalburncash_63d_base_v082_signal(cashneq, opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    b = np.log1p(((bo + bc) / cashneq.replace(0, np.nan)).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined-burn runway: cash over total opex+capex burn (all-in survival)
def f18cr_f18_cash_runway_burn_allinrunway_63d_base_v083_signal(cashneq, opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    r = cashneq / (bo + bc).replace(0, np.nan)
    b = np.log1p(r.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-in runway trend over a quarter (combined survival momentum)
def f18cr_f18_cash_runway_burn_allinrunwaytrend_base_v084_signal(cashneq, opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    r = np.log1p((cashneq / (bo + bc).replace(0, np.nan)).clip(lower=0))
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CASH-FLOW LEVEL / TREND FACETS ---
# operating cash margin: ncfo / opex relative to its 252d norm (de-trended self-funding)
def f18cr_f18_cash_runway_burn_ocfmargindev_252d_base_v085_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    b = cov - cov.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash-flow level z-scored vs 252d (cash-generation regime)
def f18cr_f18_cash_runway_burn_ncfoz_252d_base_v086_signal(ncfo, opex):
    r = ncfo / opex.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo year-over-year change scaled by opex (operating-cash improvement)
def f18cr_f18_cash_runway_burn_ncfoyoy_252d_base_v087_signal(ncfo, opex):
    r = ncfo / opex.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash yield (ncfo/cash) percentile-rank vs 504d (cash-gen percentile)
def f18cr_f18_cash_runway_burn_ncforank_504d_base_v088_signal(ncfo, cashneq):
    r = ncfo / cashneq.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CASH BALANCE FACETS (further) ---
# cash balance log-trend over a half year (slower treasury direction)
def f18cr_f18_cash_runway_burn_cashtrend_126d_base_v089_signal(cashneq):
    lc = np.log(cashneq.replace(0, np.nan))
    b = lc - lc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash drawdown from 504d peak (deep treasury underwater)
def f18cr_f18_cash_runway_burn_cashdd_504d_base_v090_signal(cashneq):
    peak = _rmax(cashneq, 504)
    b = cashneq / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash recovery off its 504d trough (treasury rebuild multiple)
def f18cr_f18_cash_runway_burn_cashrecov_504d_base_v091_signal(cashneq):
    trough = _rmin(cashneq, 504)
    b = cashneq / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash range-position momentum: change over a quarter (treasury band shift)
def f18cr_f18_cash_runway_burn_cashrngpos_252d_base_v092_signal(cashneq):
    hi = _rmax(cashneq, 252)
    lo = _rmin(cashneq, 252)
    rp = (cashneq - lo) / (hi - lo).replace(0, np.nan)
    b = rp - rp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coefficient of variation over a half year (short-run treasury instability)
def f18cr_f18_cash_runway_burn_cashcv_126d_base_v093_signal(cashneq):
    m = _mean(cashneq, 126)
    sd = _std(cashneq, 126)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DEPLETION FACETS at other windows ---
# depletion-momentum percentile-rank vs 504d (burn-acceleration percentile)
def f18cr_f18_cash_runway_burn_deplrank_504d_base_v094_signal(cashneq, opex, ncfo):
    d = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    dm = d - d.shift(63)
    b = _rank(dm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-depletion percentile-rank vs 252d (FCF-burn pressure percentile)
def f18cr_f18_cash_runway_burn_capexdeplrank_252d_base_v095_signal(cashneq, ncfo, capex):
    d = _f18_burn_capex(ncfo, capex) / cashneq.replace(0, np.nan)
    b = _rank(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depletion-rate displacement vs slow EMA (acute burn vs chronic burn)
def f18cr_f18_cash_runway_burn_depldisp_63d_base_v096_signal(cashneq, opex, ncfo):
    d = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = d - d.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COVERAGE FACETS at other windows ---
# coverage smoothed over a half year (structural self-funding level)
def f18cr_f18_cash_runway_burn_coveragesm_126d_base_v097_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    b = cov.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage percentile-rank vs 504d (self-funding percentile)
def f18cr_f18_cash_runway_burn_coveragerank_504d_base_v098_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year coverage exceeded break-even (self-funding-time)
def f18cr_f18_cash_runway_burn_selffundtime_252d_base_v099_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    ok = (cov >= 1.0).astype(float)
    frac = ok.rolling(252, min_periods=126).mean()
    surplus = (cov - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 0.3 * surplus
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FINANCING (ncff) FACETS ---
# financing inflow relative to total burn (external-funding share of burn)
def f18cr_f18_cash_runway_burn_finshareburn_63d_base_v100_signal(ncff, opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    b = (ncff / (bo + bc).replace(0, np.nan)).clip(lower=-5.0, upper=5.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow scaled by cash (treasury top-up rate from raises)
def f18cr_f18_cash_runway_burn_fintopup_63d_base_v101_signal(ncff, cashneq):
    b = (ncff / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing momentum: change in ncff/opex over a quarter (raise acceleration)
def f18cr_f18_cash_runway_burn_finmom_63d_base_v102_signal(ncff, opex):
    r = ncff / opex.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing percentile-rank vs 504d (raise-intensity percentile)
def f18cr_f18_cash_runway_burn_finrank_504d_base_v103_signal(ncff, opex):
    r = ncff / opex.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence regime: time financing exceeded operating burn
def f18cr_f18_cash_runway_burn_findeptime_252d_base_v104_signal(ncff, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    rel = ((ncff >= burn) & (burn > 0)).astype(float)
    frac = rel.rolling(252, min_periods=126).mean()
    ratio = (ncff / burn.replace(0, np.nan)).clip(lower=0, upper=5.0).rolling(63, min_periods=21).mean()
    b = frac + 0.2 * ratio
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CAPEX FACETS ---
# capex intensity relative to opex (development-vs-operating spend mix)
def f18cr_f18_cash_runway_burn_capexopexmix_63d_base_v105_signal(capex, opex):
    b = (capex / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex trend over a half year (development-spend ramp)
def f18cr_f18_cash_runway_burn_capextrend_126d_base_v106_signal(capex):
    lc = np.log(capex.replace(0, np.nan))
    b = lc - lc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex z-scored vs 252d (development-spend regime)
def f18cr_f18_cash_runway_burn_capexz_252d_base_v107_signal(capex, cashneq):
    r = capex / cashneq.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex drawdown from 252d peak (development cutback signal)
def f18cr_f18_cash_runway_burn_capexcut_252d_base_v108_signal(capex):
    peak = _rmax(capex, 252)
    b = capex / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIGN x MAGNITUDE / BOUNDED FACETS ---
# tanh-squashed coverage gap (bounded distance to self-funding)
def f18cr_f18_cash_runway_burn_covgaptanh_63d_base_v109_signal(ncfo, opex):
    gap = 1.0 - _f18_coverage(ncfo, opex)
    b = np.tanh(2.0 * gap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-root depletion rate (compressed burn intensity)
def f18cr_f18_cash_runway_burn_deplsignroot_63d_base_v110_signal(cashneq, opex, ncfo):
    d = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh of all-in burn over cash (bounded combined depletion)
def f18cr_f18_cash_runway_burn_allinburntanh_63d_base_v111_signal(cashneq, opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    d = (bo + bc) / cashneq.replace(0, np.nan)
    b = np.tanh(5.0 * d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTERACTIONS / COMPOSITES ---
# burn intensity x cash-rank (high burn while low treasury = acute risk)
def f18cr_f18_cash_runway_burn_burnXlowcash_252d_base_v112_signal(cashneq, opex, ncfo):
    burnfrac = (_f18_burn_opex(opex, ncfo) / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    cashlow = 0.5 - _rank(cashneq, 252)
    b = burnfrac * cashlow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex drain x weak coverage (developing while not self-funding)
def f18cr_f18_cash_runway_burn_capexXweakcov_63d_base_v113_signal(cashneq, capex, ncfo, opex):
    drain = (capex / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    weakcov = (1.0 - _f18_coverage(ncfo, opex)).clip(lower=0)
    b = drain * weakcov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance x burn (raising into a burn = dilution pressure proxy)
def f18cr_f18_cash_runway_burn_finXburn_63d_base_v114_signal(ncff, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    finrel = (ncff.clip(lower=0) / opex.replace(0, np.nan))
    b = (finrel * (burn / opex.replace(0, np.nan))).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISPERSION / VOL FACETS ---
# opex-runway volatility over a year (erratic survival horizon)
def f18cr_f18_cash_runway_burn_runwayvol_252d_base_v115_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = r.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo volatility over a year scaled by opex (operating-cash instability)
def f18cr_f18_cash_runway_burn_ncfovol_252d_base_v116_signal(ncfo, opex):
    r = ncfo / opex.replace(0, np.nan)
    b = r.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-in depletion volatility over a half year (combined burn instability)
def f18cr_f18_cash_runway_burn_allindeplvol_126d_base_v117_signal(cashneq, opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    d = (bo + bc) / cashneq.replace(0, np.nan)
    b = d.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TERM-STRUCTURE / SHORT-LONG FACETS ---
# coverage term ratio: 63d coverage vs 252d coverage (self-funding momentum)
def f18cr_f18_cash_runway_burn_covtermratio_base_v118_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    short = cov.rolling(63, min_periods=21).mean()
    long = cov.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex term ratio: 63d capex/cash vs 252d capex/cash (capex acceleration)
def f18cr_f18_cash_runway_burn_capextermratio_base_v119_signal(capex, cashneq):
    r = capex / cashneq.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncff term ratio: 63d vs 252d financing intensity (raise-cadence shift)
def f18cr_f18_cash_runway_burn_fintermratio_base_v120_signal(ncff, opex):
    r = ncff / opex.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DRAWDOWN / EXTREME RUNWAY FACETS ---
# max depletion over last half year (worst burn-pressure point)
def f18cr_f18_cash_runway_burn_maxdepl_126d_base_v121_signal(cashneq, opex, ncfo):
    d = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = _rmax(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway drawdown from 504d peak (long-horizon survival cushion loss)
def f18cr_f18_cash_runway_burn_runwaydd_504d_base_v122_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    peak = _rmax(r, 504)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 504d runway sat below 2 quarters of cash (deep-distress time)
def f18cr_f18_cash_runway_burn_deepcrittime_504d_base_v123_signal(cashneq, opex, ncfo):
    r = _f18_runway_opex(cashneq, opex, ncfo)
    crit = (r < 2.0).astype(float)
    frac = crit.rolling(504, min_periods=252).mean()
    shortfall = (2.0 - r.clip(upper=2.0)).rolling(63, min_periods=21).mean()
    b = frac + 0.5 * shortfall
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MULTI-WINDOW DISPERSION / DISAGREEMENT ---
# coverage disagreement across 63/126/252 windows (self-funding regime instability)
def f18cr_f18_cash_runway_burn_covdisp_multi_base_v124_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    a = cov.rolling(63, min_periods=21).mean()
    b2 = cov.rolling(126, min_periods=63).mean()
    c = cov.rolling(252, min_periods=126).mean()
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-trend disagreement across windows (treasury direction instability)
def f18cr_f18_cash_runway_burn_cashtrenddisp_base_v125_signal(cashneq):
    lc = np.log(cashneq.replace(0, np.nan))
    t1 = lc - lc.shift(21)
    t2 = lc - lc.shift(63)
    t3 = lc - lc.shift(126)
    b = pd.concat([t1, t2, t3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RUNWAY MOMENTUM / ACCELERATION (base-level) ---
# opex-runway momentum: trend now vs trend a quarter ago (base second-order)
def f18cr_f18_cash_runway_burn_runwaymom_63d_base_v126_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    t = r - r.shift(63)
    b = t - t.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage acceleration (base second difference of coverage)
def f18cr_f18_cash_runway_burn_covaccel_42d_base_v127_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    d1 = cov - cov.shift(42)
    b = d1 - d1.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash log-trend acceleration (treasury depletion accelerating, base)
def f18cr_f18_cash_runway_burn_cashaccel_63d_base_v128_signal(cashneq):
    lc = np.log(cashneq.replace(0, np.nan))
    d1 = lc - lc.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BURN-STREAK / REGIME FACETS ---
# longest recent burn streak proxy: avg burn-on over a quarter weighted by depth
def f18cr_f18_cash_runway_burn_burnstreak_63d_base_v129_signal(opex, ncfo):
    burning = (_f18_burn_opex(opex, ncfo) > 0).astype(float)
    streak = burning.rolling(63, min_periods=21).mean()
    depth = (_f18_burn_opex(opex, ncfo) / opex.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = streak * (1.0 + depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-burn regime time: fraction of last year FCF was negative, plus onset count
def f18cr_f18_cash_runway_burn_capexburntime_252d_base_v130_signal(ncfo, capex):
    burning = (_f18_burn_capex(ncfo, capex) > 0).astype(float)
    frac = burning.rolling(252, min_periods=126).mean()
    entries = ((burning == 1) & (burning.shift(1) == 0)).astype(float)
    onset = entries.rolling(252, min_periods=126).sum()
    b = frac + 0.1 * onset
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of fresh self-funding entries over a year (turning cash-flow positive)
def f18cr_f18_cash_runway_burn_turnpositive_252d_base_v131_signal(ncfo, opex):
    ok = (_f18_coverage(ncfo, opex) >= 1.0).astype(float)
    entries = ((ok == 1) & (ok.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 0.3 * ok.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RATIO / YIELD FACETS ---
# burn-to-financing ratio (how much of burn financing must cover)
def f18cr_f18_cash_runway_burn_burnvsfin_63d_base_v132_signal(opex, ncfo, ncff):
    burn = _f18_burn_opex(opex, ncfo)
    b = (burn / ncff.clip(lower=1.0)).clip(upper=20.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-to-burn ratio (development spend as share of operating burn)
def f18cr_f18_cash_runway_burn_capexvsburn_63d_base_v133_signal(capex, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    b = (capex / burn.replace(0, np.nan)).clip(upper=20.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-flow over cash yield (FCF generation per treasury dollar)
def f18cr_f18_cash_runway_burn_fcfcashyield_63d_base_v134_signal(ncfo, capex, cashneq):
    fcf = ncfo - capex
    b = (fcf / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CROSS-SECTIONAL-STYLE Z / RANK FACETS (further) ---
# all-in runway z-scored vs 252d (combined survival regime)
def f18cr_f18_cash_runway_burn_allinrunwayz_252d_base_v135_signal(cashneq, opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    r = np.log1p((cashneq / (bo + bc).replace(0, np.nan)).clip(lower=0))
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-mix z-scored vs 252d (shift toward opex- vs capex-driven burn)
def f18cr_f18_cash_runway_burn_burnmixz_252d_base_v136_signal(opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    mix = bo / (bo + bc).replace(0, np.nan)
    b = _z(mix, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-share-of-burn percentile-rank vs 252d (external-funding percentile)
def f18cr_f18_cash_runway_burn_finsharerank_252d_base_v137_signal(ncff, opex, ncfo, capex):
    bo = _f18_burn_opex(opex, ncfo)
    bc = _f18_burn_capex(ncfo, capex)
    share = (ncff / (bo + bc).replace(0, np.nan)).clip(lower=-5.0, upper=5.0)
    b = _rank(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LONG-WINDOW STRUCTURAL FACETS ---
# 504d structural runway level (long-horizon survival baseline)
def f18cr_f18_cash_runway_burn_runwaystruct_504d_base_v138_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = r.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d structural coverage (long-horizon self-funding baseline)
def f18cr_f18_cash_runway_burn_covstruct_504d_base_v139_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    b = cov.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d structural depletion (long-horizon burn-pressure baseline)
def f18cr_f18_cash_runway_burn_deplstruct_504d_base_v140_signal(cashneq, opex, ncfo):
    d = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = d.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FURTHER DISTINCT COMPOSITES ---
# survival buffer: runway level minus financing dependence (true cushion)
def f18cr_f18_cash_runway_burn_survbuffer_63d_base_v141_signal(cashneq, opex, ncfo, ncff):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    findep = (ncff.clip(lower=0) / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = r - findep
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zombie proxy: burning AND raising AND low cash-rank (graveyard distance)
def f18cr_f18_cash_runway_burn_zombieproxy_252d_base_v142_signal(cashneq, opex, ncfo, ncff):
    burning = (_f18_burn_opex(opex, ncfo) > 0).astype(float)
    raising = (ncff > 0).astype(float)
    lowcash = (0.5 - _rank(cashneq, 252)).clip(lower=0)
    b = (burning * raising).rolling(126, min_periods=63).mean() + lowcash
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway-to-burn-vol ratio (survival horizon per unit of burn instability)
def f18cr_f18_cash_runway_burn_runwayperburnvol_base_v143_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    burn = _f18_burn_opex(opex, ncfo)
    bv = (burn / cashneq.replace(0, np.nan)).rolling(126, min_periods=63).std()
    b = r / bv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-burn coverage gap to a 1-year survival floor (distance to safety)
def f18cr_f18_cash_runway_burn_safetyfloor_63d_base_v144_signal(cashneq, opex, ncfo):
    r = _f18_runway_opex(cashneq, opex, ncfo)
    b = np.tanh(0.5 * (r - 4.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo-to-capex coverage (operations funding development vs needing finance)
def f18cr_f18_cash_runway_burn_ncfocapexcov_63d_base_v145_signal(ncfo, capex):
    b = (ncfo / capex.replace(0, np.nan)).clip(lower=-10.0, upper=10.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn fraction of cash plus capex drain (total treasury pressure rate)
def f18cr_f18_cash_runway_burn_treasurypressure_63d_base_v146_signal(cashneq, opex, ncfo, capex):
    burnrate = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    capexrate = capex / cashneq.replace(0, np.nan)
    b = (burnrate + 0.5 * capexrate).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn coverage trend (is financing keeping up with burn?)
def f18cr_f18_cash_runway_burn_finkeepup_126d_base_v147_signal(ncff, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    cov = (ncff / burn.replace(0, np.nan)).clip(lower=-5.0, upper=5.0)
    b = cov - cov.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-gap signed-root momentum (compressed self-funding deterioration)
def f18cr_f18_cash_runway_burn_covgaprootmom_63d_base_v148_signal(ncfo, opex):
    gap = 1.0 - _f18_coverage(ncfo, opex)
    sr = np.sign(gap) * (gap.abs() ** 0.5)
    b = sr - sr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-runway-rank minus opex-coverage-rank (FCF survival vs operating self-funding)
def f18cr_f18_cash_runway_burn_survvsburn_252d_base_v149_signal(cashneq, ncfo, capex, opex):
    r = np.log1p(_f18_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    cov = _f18_coverage(ncfo, opex)
    b = _rank(r, 252) - _rank(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-in survival composite: structural runway minus burn-vol minus fin-reliance
def f18cr_f18_cash_runway_burn_survcomposite_base_v150_signal(cashneq, opex, ncfo, ncff):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0)).rolling(126, min_periods=63).mean()
    burn = _f18_burn_opex(opex, ncfo)
    bv = (burn / cashneq.replace(0, np.nan)).rolling(126, min_periods=63).std()
    finrel = (ncff.clip(lower=0) / opex.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b = _z(r, 252) - _z(bv, 252) - _z(finrel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18cr_f18_cash_runway_burn_runwaypctdepl_252d_base_v076_signal,
    f18cr_f18_cash_runway_burn_runwaymeddev_252d_base_v077_signal,
    f18cr_f18_cash_runway_burn_runwaycapexsm_126d_base_v078_signal,
    f18cr_f18_cash_runway_burn_runwaycapexdisp_base_v079_signal,
    f18cr_f18_cash_runway_burn_monthsmeddev_504d_base_v080_signal,
    f18cr_f18_cash_runway_burn_burnmix_63d_base_v081_signal,
    f18cr_f18_cash_runway_burn_totalburncash_63d_base_v082_signal,
    f18cr_f18_cash_runway_burn_allinrunway_63d_base_v083_signal,
    f18cr_f18_cash_runway_burn_allinrunwaytrend_base_v084_signal,
    f18cr_f18_cash_runway_burn_ocfmargindev_252d_base_v085_signal,
    f18cr_f18_cash_runway_burn_ncfoz_252d_base_v086_signal,
    f18cr_f18_cash_runway_burn_ncfoyoy_252d_base_v087_signal,
    f18cr_f18_cash_runway_burn_ncforank_504d_base_v088_signal,
    f18cr_f18_cash_runway_burn_cashtrend_126d_base_v089_signal,
    f18cr_f18_cash_runway_burn_cashdd_504d_base_v090_signal,
    f18cr_f18_cash_runway_burn_cashrecov_504d_base_v091_signal,
    f18cr_f18_cash_runway_burn_cashrngpos_252d_base_v092_signal,
    f18cr_f18_cash_runway_burn_cashcv_126d_base_v093_signal,
    f18cr_f18_cash_runway_burn_deplrank_504d_base_v094_signal,
    f18cr_f18_cash_runway_burn_capexdeplrank_252d_base_v095_signal,
    f18cr_f18_cash_runway_burn_depldisp_63d_base_v096_signal,
    f18cr_f18_cash_runway_burn_coveragesm_126d_base_v097_signal,
    f18cr_f18_cash_runway_burn_coveragerank_504d_base_v098_signal,
    f18cr_f18_cash_runway_burn_selffundtime_252d_base_v099_signal,
    f18cr_f18_cash_runway_burn_finshareburn_63d_base_v100_signal,
    f18cr_f18_cash_runway_burn_fintopup_63d_base_v101_signal,
    f18cr_f18_cash_runway_burn_finmom_63d_base_v102_signal,
    f18cr_f18_cash_runway_burn_finrank_504d_base_v103_signal,
    f18cr_f18_cash_runway_burn_findeptime_252d_base_v104_signal,
    f18cr_f18_cash_runway_burn_capexopexmix_63d_base_v105_signal,
    f18cr_f18_cash_runway_burn_capextrend_126d_base_v106_signal,
    f18cr_f18_cash_runway_burn_capexz_252d_base_v107_signal,
    f18cr_f18_cash_runway_burn_capexcut_252d_base_v108_signal,
    f18cr_f18_cash_runway_burn_covgaptanh_63d_base_v109_signal,
    f18cr_f18_cash_runway_burn_deplsignroot_63d_base_v110_signal,
    f18cr_f18_cash_runway_burn_allinburntanh_63d_base_v111_signal,
    f18cr_f18_cash_runway_burn_burnXlowcash_252d_base_v112_signal,
    f18cr_f18_cash_runway_burn_capexXweakcov_63d_base_v113_signal,
    f18cr_f18_cash_runway_burn_finXburn_63d_base_v114_signal,
    f18cr_f18_cash_runway_burn_runwayvol_252d_base_v115_signal,
    f18cr_f18_cash_runway_burn_ncfovol_252d_base_v116_signal,
    f18cr_f18_cash_runway_burn_allindeplvol_126d_base_v117_signal,
    f18cr_f18_cash_runway_burn_covtermratio_base_v118_signal,
    f18cr_f18_cash_runway_burn_capextermratio_base_v119_signal,
    f18cr_f18_cash_runway_burn_fintermratio_base_v120_signal,
    f18cr_f18_cash_runway_burn_maxdepl_126d_base_v121_signal,
    f18cr_f18_cash_runway_burn_runwaydd_504d_base_v122_signal,
    f18cr_f18_cash_runway_burn_deepcrittime_504d_base_v123_signal,
    f18cr_f18_cash_runway_burn_covdisp_multi_base_v124_signal,
    f18cr_f18_cash_runway_burn_cashtrenddisp_base_v125_signal,
    f18cr_f18_cash_runway_burn_runwaymom_63d_base_v126_signal,
    f18cr_f18_cash_runway_burn_covaccel_42d_base_v127_signal,
    f18cr_f18_cash_runway_burn_cashaccel_63d_base_v128_signal,
    f18cr_f18_cash_runway_burn_burnstreak_63d_base_v129_signal,
    f18cr_f18_cash_runway_burn_capexburntime_252d_base_v130_signal,
    f18cr_f18_cash_runway_burn_turnpositive_252d_base_v131_signal,
    f18cr_f18_cash_runway_burn_burnvsfin_63d_base_v132_signal,
    f18cr_f18_cash_runway_burn_capexvsburn_63d_base_v133_signal,
    f18cr_f18_cash_runway_burn_fcfcashyield_63d_base_v134_signal,
    f18cr_f18_cash_runway_burn_allinrunwayz_252d_base_v135_signal,
    f18cr_f18_cash_runway_burn_burnmixz_252d_base_v136_signal,
    f18cr_f18_cash_runway_burn_finsharerank_252d_base_v137_signal,
    f18cr_f18_cash_runway_burn_runwaystruct_504d_base_v138_signal,
    f18cr_f18_cash_runway_burn_covstruct_504d_base_v139_signal,
    f18cr_f18_cash_runway_burn_deplstruct_504d_base_v140_signal,
    f18cr_f18_cash_runway_burn_survbuffer_63d_base_v141_signal,
    f18cr_f18_cash_runway_burn_zombieproxy_252d_base_v142_signal,
    f18cr_f18_cash_runway_burn_runwayperburnvol_base_v143_signal,
    f18cr_f18_cash_runway_burn_safetyfloor_63d_base_v144_signal,
    f18cr_f18_cash_runway_burn_ncfocapexcov_63d_base_v145_signal,
    f18cr_f18_cash_runway_burn_treasurypressure_63d_base_v146_signal,
    f18cr_f18_cash_runway_burn_finkeepup_126d_base_v147_signal,
    f18cr_f18_cash_runway_burn_covgaprootmom_63d_base_v148_signal,
    f18cr_f18_cash_runway_burn_survvsburn_252d_base_v149_signal,
    f18cr_f18_cash_runway_burn_survcomposite_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_CASH_RUNWAY_BURN_REGISTRY_076_150 = REGISTRY


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

    cashneq = _fund(1801, base=1.2e8, drift=-0.02, vol=0.10).rename("cashneq")
    ncfo = _fund(1802, base=1.1e8, drift=-0.01, vol=0.22, allow_neg=True).rename("ncfo")
    opex = _fund(1803, base=5e7, drift=0.01, vol=0.07).rename("opex")
    capex = _fund(1804, base=6e7, drift=0.01, vol=0.18).rename("capex")
    ncff = _fund(1805, base=3e7, drift=0.0, vol=0.25, allow_neg=True).rename("ncff")

    cols = {"cashneq": cashneq, "ncfo": ncfo, "opex": opex,
            "capex": capex, "ncff": ncff}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("cashneq", "ncfo", "opex", "capex", "ncff")
                   for c in meta["inputs"]), name
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

    print("OK f18_cash_runway_burn_base_076_150_claude: %d features pass" % n_features)
