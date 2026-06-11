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


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (cash runway / burn) =====
def _f18_burn_opex(opex, ncfo):
    # cash burn = operating spend not covered by operating cash flow
    return (opex - ncfo).clip(lower=0.0)


def _f18_burn_capex(ncfo, capex):
    # cash burn = negative free cash flow proxy = -(ncfo) + capex
    return (-ncfo + capex).clip(lower=0.0)


def _f18_runway_opex(cashneq, opex, ncfo):
    # quarters of cash at the opex-based burn rate
    burn = (opex - ncfo).clip(lower=0.0)
    return cashneq / burn.replace(0, np.nan)


def _f18_runway_capex(cashneq, ncfo, capex):
    burn = (-ncfo + capex).clip(lower=0.0)
    return cashneq / burn.replace(0, np.nan)


def _f18_months_of_cash(cashneq, opex, ncfo):
    # opex/ncfo are quarterly-ish flows; months = runway_quarters * 3
    burn = (opex - ncfo).clip(lower=0.0)
    return 3.0 * cashneq / burn.replace(0, np.nan)


def _f18_coverage(ncfo, opex):
    # operating cash flow coverage of operating spend
    return ncfo / opex.replace(0, np.nan)


# ============================================================
# --- RUNWAY LEVELS (opex-based) ---
# opex-based cash runway (quarters of cash), log-compressed level
def f18cr_f18_cash_runway_burn_runwayopex_63d_base_v001_signal(cashneq, opex, ncfo):
    r = _f18_runway_opex(cashneq, opex, ncfo)
    b = np.log1p(r.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-based runway smoothed over a quarter (persistent runway level)
def f18cr_f18_cash_runway_burn_runwayopexsm_63d_base_v002_signal(cashneq, opex, ncfo):
    r = _f18_runway_opex(cashneq, opex, ncfo)
    b = np.log1p(r.clip(lower=0)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# months-of-cash at opex burn (capped tail) — survival horizon
def f18cr_f18_cash_runway_burn_monthscash_21d_base_v003_signal(cashneq, opex, ncfo):
    m = _f18_months_of_cash(cashneq, opex, ncfo)
    b = m.clip(upper=120.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-based cash runway (free-cash-flow burn), log-compressed
def f18cr_f18_cash_runway_burn_runwaycapex_63d_base_v004_signal(cashneq, ncfo, capex):
    r = _f18_runway_capex(cashneq, ncfo, capex)
    b = np.log1p(r.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-based runway smoothed over a quarter
def f18cr_f18_cash_runway_burn_runwaycapexsm_63d_base_v005_signal(cashneq, ncfo, capex):
    r = _f18_runway_capex(cashneq, ncfo, capex)
    b = np.log1p(r.clip(lower=0)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between opex-runway and capex-runway (which burn definition bites)
def f18cr_f18_cash_runway_burn_runwayspread_63d_base_v006_signal(cashneq, opex, ncfo, capex):
    ro = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    rc = np.log1p(_f18_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    b = ro - rc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RUNWAY Z / RANK ---
# opex-runway z-scored vs its own 252d history (de-trended distress level)
def f18cr_f18_cash_runway_burn_runwayopexz_252d_base_v007_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-runway z-scored vs its own 126d history
def f18cr_f18_cash_runway_burn_runwaycapexz_126d_base_v008_signal(cashneq, ncfo, capex):
    r = np.log1p(_f18_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-runway percentile-rank vs its own 504d history (where in distress band)
def f18cr_f18_cash_runway_burn_runwayopexrank_504d_base_v009_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# months-of-cash percentile-rank vs 252d history
def f18cr_f18_cash_runway_burn_monthsrank_252d_base_v010_signal(cashneq, opex, ncfo):
    m = _f18_months_of_cash(cashneq, opex, ncfo)
    b = _rank(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BURN RATE LEVELS ---
# opex-based burn rate scaled by cash (inverse runway = depletion rate)
def f18cr_f18_cash_runway_burn_depletion_63d_base_v011_signal(cashneq, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    b = burn / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-based depletion rate (fcf-burn over cash)
def f18cr_f18_cash_runway_burn_depletioncapex_63d_base_v012_signal(cashneq, ncfo, capex):
    burn = _f18_burn_capex(ncfo, capex)
    b = burn / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex burn relative to its own trailing-year norm (burn surprise, de-trended)
def f18cr_f18_cash_runway_burn_burnlevel_21d_base_v013_signal(opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    norm = burn.rolling(252, min_periods=126).mean()
    b = burn / norm.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn rate as a fraction of opex (how much spend is uncovered)
def f18cr_f18_cash_runway_burn_burnfrac_63d_base_v014_signal(opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    b = burn / opex.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depletion-rate z-scored vs 252d (de-trended burn intensity)
def f18cr_f18_cash_runway_burn_depletionz_252d_base_v015_signal(cashneq, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    d = burn / cashneq.replace(0, np.nan)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COVERAGE ---
# operating-cash-flow coverage of opex (>=1 = self-funding)
def f18cr_f18_cash_runway_burn_coverage_63d_base_v016_signal(ncfo, opex):
    b = _f18_coverage(ncfo, opex).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-gap momentum: change in (1 - ncfo/opex) over a quarter (gap widening)
def f18cr_f18_cash_runway_burn_covgap_63d_base_v017_signal(ncfo, opex):
    gap = (1.0 - _f18_coverage(ncfo, opex)).clip(lower=-2.0, upper=2.0)
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage z-scored vs 126d history (coverage regime shift)
def f18cr_f18_cash_runway_burn_coveragez_126d_base_v018_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    b = _z(cov, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-burn coverage z-scored vs 126d (coverage regime extremity)
def f18cr_f18_cash_runway_burn_cashburncov_63d_base_v019_signal(cashneq, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    cov = np.log1p((cashneq / burn.replace(0, np.nan)).clip(lower=0))
    b = _z(cov, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RUNWAY TREND / SLOPE-LIKE (base-level changes, not derivative file) ---
# opex-runway trend over a quarter (improving/deteriorating survival)
def f18cr_f18_cash_runway_burn_runwaytrend_63d_base_v020_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-runway year-over-year change (cyclical survival shift)
def f18cr_f18_cash_runway_burn_runwayyoy_252d_base_v021_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depletion-rate trend over a quarter (burn accelerating in level terms)
def f18cr_f18_cash_runway_burn_depletiontrend_63d_base_v022_signal(cashneq, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    d = burn / cashneq.replace(0, np.nan)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend over half a year (path toward self-funding)
def f18cr_f18_cash_runway_burn_covtrend_126d_base_v023_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    b = cov - cov.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CASH BALANCE DYNAMICS ---
# cash balance log-trend over a quarter (treasury drawdown/build)
def f18cr_f18_cash_runway_burn_cashtrend_63d_base_v024_signal(cashneq):
    lc = np.log(cashneq.replace(0, np.nan))
    b = lc - lc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash drawdown from its trailing 252d peak (treasury underwater depth)
def f18cr_f18_cash_runway_burn_cashdd_252d_base_v025_signal(cashneq):
    peak = _rmax(cashneq, 252)
    b = cashneq / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash balance z-scored vs 252d history (treasury level regime)
def f18cr_f18_cash_runway_burn_cashz_252d_base_v026_signal(cashneq):
    b = _z(np.log(cashneq.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash percentile-rank vs 504d history (treasury percentile)
def f18cr_f18_cash_runway_burn_cashrank_504d_base_v027_signal(cashneq):
    b = _rank(cashneq, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year cash sat below its own 252d median (chronic low-cash)
def f18cr_f18_cash_runway_burn_lowcashtime_252d_base_v028_signal(cashneq):
    med = cashneq.rolling(252, min_periods=126).median()
    below = (cashneq < med).astype(float)
    b = below.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BURN STREAKS / COUNTS (regime-friendly) ---
# fraction of last year spent burning cash (opex burn > 0)
def f18cr_f18_cash_runway_burn_burntime_252d_base_v029_signal(opex, ncfo):
    burning = (_f18_burn_opex(opex, ncfo) > 0).astype(float)
    b = burning.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of fresh entries into burn regime over the last year (burn-onset tally)
def f18cr_f18_cash_runway_burn_burnonset_252d_base_v030_signal(ncfo, capex):
    burning = (_f18_burn_capex(ncfo, capex) > 0).astype(float)
    entries = ((burning == 1) & (burning.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 0.3 * burning.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# negative-ncfo prevalence blended with avg shortfall depth (cash-burn quarters)
def f18cr_f18_cash_runway_burn_negncfotime_252d_base_v031_signal(ncfo, opex):
    neg = (ncfo < 0).astype(float)
    frac = neg.rolling(252, min_periods=126).mean()
    depth = (-ncfo / opex.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 0.5 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-intensity instability: dispersion of uncovered-spend share over a quarter
def f18cr_f18_cash_runway_burn_burnintensity_63d_base_v032_signal(opex, ncfo):
    frac = _f18_burn_opex(opex, ncfo) / opex.replace(0, np.nan)
    b = frac.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FINANCING-FUNDED BURN (ncff) ---
# financing inflow relative to operating burn (raises plugging the hole)
def f18cr_f18_cash_runway_burn_finfundburn_63d_base_v033_signal(ncff, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    b = ncff / burn.replace(0, np.nan)
    b = b.clip(lower=-5.0, upper=5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing coverage of capex-burn, smoothed (external-finance dependence)
def f18cr_f18_cash_runway_burn_findepcapex_63d_base_v034_signal(ncff, ncfo, capex):
    burn = _f18_burn_capex(ncfo, capex)
    cov = ncff / burn.replace(0, np.nan)
    b = cov.clip(lower=-5.0, upper=5.0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap rate: (ncfo - opex) / cash, smoothed (operating cash gen vs spend)
def f18cr_f18_cash_runway_burn_selffundgap_63d_base_v035_signal(cashneq, opex, ncfo):
    net = ncfo - opex
    b = (net / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence z: ncff scaled by opex, z-scored vs 252d
def f18cr_f18_cash_runway_burn_finz_252d_base_v036_signal(ncff, opex):
    r = ncff / opex.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-runway extension: how much a year of raises lengthens runway vs cash alone
def f18cr_f18_cash_runway_burn_runwaywithfin_63d_base_v037_signal(cashneq, ncff):
    raise_yr = ncff.clip(lower=0).rolling(252, min_periods=126).mean() * 4.0
    b = (raise_yr / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RATIOS SHORT/LONG (term structure of burn) ---
# short-vs-long burn ratio: 63d avg burn over 252d avg burn (burn ramp)
def f18cr_f18_cash_runway_burn_burntermratio_base_v038_signal(opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    short = burn.rolling(63, min_periods=21).mean()
    long = burn.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long runway ratio (recent runway vs structural runway)
def f18cr_f18_cash_runway_burn_runwaytermratio_base_v039_signal(cashneq, opex, ncfo):
    r = _f18_runway_opex(cashneq, opex, ncfo)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = np.log1p(short.clip(lower=0)) - np.log1p(long.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long cash ratio (recent treasury vs structural treasury)
def f18cr_f18_cash_runway_burn_cashtermratio_base_v040_signal(cashneq):
    short = cashneq.rolling(63, min_periods=21).mean()
    long = cashneq.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISPERSION / VOLATILITY of burn ---
# burn-rate volatility over a half-year (erratic vs steady burn)
def f18cr_f18_cash_runway_burn_burnvol_126d_base_v041_signal(cashneq, opex, ncfo):
    d = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = d.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of cash balance over a year (treasury instability)
def f18cr_f18_cash_runway_burn_cashcv_252d_base_v042_signal(cashneq):
    m = _mean(cashneq, 252)
    sd = _std(cashneq, 252)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage dispersion over a year (volatility of self-funding ability)
def f18cr_f18_cash_runway_burn_covvol_252d_base_v043_signal(ncfo, opex):
    cov = _f18_coverage(ncfo, opex)
    b = cov.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIGN x MAGNITUDE forms ---
# signed root of coverage gap (compressed distance to break-even)
def f18cr_f18_cash_runway_burn_covgapsignmag_63d_base_v044_signal(ncfo, opex):
    gap = (1.0 - _f18_coverage(ncfo, opex))
    b = np.sign(gap) * (gap.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed depletion-rate momentum (bounded burn-intensity change over a month)
def f18cr_f18_cash_runway_burn_depletiontanh_63d_base_v045_signal(cashneq, opex, ncfo):
    d = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    chg = d - d.shift(21)
    b = np.tanh(40.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-flow margin relative to opex, de-trended vs its 126d norm
def f18cr_f18_cash_runway_burn_fcfsignlog_21d_base_v046_signal(ncfo, capex, opex):
    fcfm = (ncfo - capex) / opex.replace(0, np.nan)
    b = fcfm - fcfm.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTERACTIONS ---
# distress interaction: depletion x log-burn-over-cash (compound going-to-zero)
def f18cr_f18_cash_runway_burn_distressX_63d_base_v047_signal(cashneq, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    depl = burn / cashneq.replace(0, np.nan)
    b = depl * np.log1p((burn / cashneq.replace(0, np.nan)).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn x cash-drawdown interaction (burning while treasury bleeding)
def f18cr_f18_cash_runway_burn_burnXcashdd_252d_base_v048_signal(cashneq, opex, ncfo):
    burnfrac = _f18_burn_opex(opex, ncfo) / opex.replace(0, np.nan)
    peak = _rmax(cashneq, 252)
    cashdd = (1.0 - cashneq / peak.replace(0, np.nan)).clip(lower=0)
    b = burnfrac * cashdd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity relative to cash (development drain on treasury)
def f18cr_f18_cash_runway_burn_capexdrain_63d_base_v049_signal(cashneq, capex):
    b = (capex / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex vs operating cash flow (growth-spend funded by operations?)
def f18cr_f18_cash_runway_burn_capexvsncfo_63d_base_v050_signal(capex, ncfo):
    b = (capex / ncfo.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MORE RUNWAY VARIANTS (windows/normalizations) ---
# opex-runway smoothed over a half year (structural survival)
def f18cr_f18_cash_runway_burn_runwayopexsm_126d_base_v051_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-runway percentile-rank vs 252d history
def f18cr_f18_cash_runway_burn_runwaycapexrank_252d_base_v052_signal(cashneq, ncfo, capex):
    r = np.log1p(_f18_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway displacement: opex-runway minus its slow EMA (acute vs chronic)
def f18cr_f18_cash_runway_burn_runwaydisp_63d_base_v053_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# months-of-cash EMA-smoothed level
def f18cr_f18_cash_runway_burn_monthsema_63d_base_v054_signal(cashneq, opex, ncfo):
    m = _f18_months_of_cash(cashneq, opex, ncfo).clip(upper=120.0)
    b = m.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# critical-runway pressure: time under 4q-cash blended with how far below the line
def f18cr_f18_cash_runway_burn_critruntime_252d_base_v055_signal(cashneq, opex, ncfo):
    r = _f18_runway_opex(cashneq, opex, ncfo)
    crit = (r < 4.0).astype(float)
    frac = crit.rolling(252, min_periods=126).mean()
    shortfall = (4.0 - r.clip(upper=4.0)).rolling(63, min_periods=21).mean()
    b = frac + 0.25 * shortfall
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BURN ACCELERATION-LIKE (base-level second differences) ---
# burn level second difference (accel of absolute burn, base form)
def f18cr_f18_cash_runway_burn_burnaccel_63d_base_v056_signal(opex, ncfo):
    burn = np.log1p(_f18_burn_opex(opex, ncfo))
    d1 = burn - burn.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depletion-rate acceleration (base second difference)
def f18cr_f18_cash_runway_burn_deplaccel_42d_base_v057_signal(cashneq, opex, ncfo):
    d = _f18_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    d1 = d - d.shift(42)
    b = d1 - d1.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# runway curvature: opex-runway minus average of its lead/lag (concavity, base)
def f18cr_f18_cash_runway_burn_runwaycurv_63d_base_v058_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = r - 0.5 * (r.shift(63) + r.shift(-63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- NCFF / FINANCING REGIME ---
# financing-reliance regime: time raising blended with avg raise magnitude vs opex
def f18cr_f18_cash_runway_burn_finposttime_252d_base_v059_signal(ncff, opex):
    pos = (ncff > 0).astype(float)
    frac = pos.rolling(252, min_periods=126).mean()
    mag = (ncff.clip(lower=0) / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = frac + 0.3 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing volatility over a year (lumpy capital raises)
def f18cr_f18_cash_runway_burn_finvol_252d_base_v060_signal(ncff, opex):
    r = ncff / opex.replace(0, np.nan)
    b = r.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn streak: period ncff covers opex-burn, plus intensity
def f18cr_f18_cash_runway_burn_finfundstreak_base_v061_signal(ncff, opex, ncfo):
    burn = _f18_burn_opex(opex, ncfo)
    covered = ((ncff >= burn) & (burn > 0)).astype(float)
    b = covered.rolling(126, min_periods=42).mean() + 0.2 * np.tanh(ncff / opex.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE RUNWAY DISTANCE ---
# years-to-zero-cash: cash relative to typical annual opex burn
def f18cr_f18_cash_runway_burn_yearstozero_base_v062_signal(cashneq, opex, ncfo):
    annual_burn = _f18_burn_opex(opex, ncfo).rolling(252, min_periods=126).mean() * 4.0
    b = np.log1p((cashneq / annual_burn.replace(0, np.nan)).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# worst-case runway: cash over peak burn seen in last year
def f18cr_f18_cash_runway_burn_worstcaserun_252d_base_v063_signal(cashneq, opex, ncfo):
    peak_burn = _rmax(_f18_burn_opex(opex, ncfo), 252)
    b = np.log1p((cashneq / peak_burn.replace(0, np.nan)).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-runway drawdown from its 252d peak (loss of FCF-survival cushion)
def f18cr_f18_cash_runway_burn_bestcaserun_252d_base_v064_signal(cashneq, ncfo, capex):
    r = np.log1p(_f18_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COVERAGE / BURN CROSS FORMS ---
# coverage minus financing dependence (true operating self-sufficiency)
def f18cr_f18_cash_runway_burn_selfsuffic_63d_base_v065_signal(ncfo, opex, ncff):
    cov = _f18_coverage(ncfo, opex)
    findep = (ncff / opex.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    b = (cov - findep).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo-to-cash yield (operating cash generation per dollar of treasury)
def f18cr_f18_cash_runway_burn_ncfocashyield_63d_base_v066_signal(ncfo, cashneq):
    b = (ncfo / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-to-cash turn (treasury turns over how fast on spend)
def f18cr_f18_cash_runway_burn_opexcashturn_63d_base_v067_signal(opex, cashneq):
    b = (opex / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RANK / Z VARIANTS OF BURN ---
# burn-fraction percentile-rank vs 252d (chronic burn-share percentile)
def f18cr_f18_cash_runway_burn_burnfracrank_252d_base_v068_signal(opex, ncfo):
    frac = _f18_burn_opex(opex, ncfo) / opex.replace(0, np.nan)
    b = _rank(frac, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-burn term ratio: recent 63d fcf-burn vs structural 252d fcf-burn
def f18cr_f18_cash_runway_burn_capexburnz_126d_base_v069_signal(ncfo, capex):
    burn = _f18_burn_capex(ncfo, capex)
    short = burn.rolling(63, min_periods=21).mean()
    long = burn.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-yield (ncfo/cash) z-scored vs 252d
def f18cr_f18_cash_runway_burn_cashyieldz_252d_base_v070_signal(ncfo, cashneq):
    r = ncfo / cashneq.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DRAWDOWN / EXTREME RUNWAY ---
# runway drawdown from its trailing 252d peak (loss of survival cushion)
def f18cr_f18_cash_runway_burn_runwaydd_252d_base_v071_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# min runway over last half year (worst survival point recently)
def f18cr_f18_cash_runway_burn_minrunway_126d_base_v072_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _rmin(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread of runway across short/medium/long windows (runway disagreement)
def f18cr_f18_cash_runway_burn_runwaydisp_multi_base_v073_signal(cashneq, opex, ncfo):
    r = np.log1p(_f18_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    a = r.rolling(63, min_periods=21).mean()
    b2 = r.rolling(126, min_periods=63).mean()
    c = r.rolling(252, min_periods=126).mean()
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-vs-cash divergence: burn ramp minus treasury depletion (compounding pressure)
def f18cr_f18_cash_runway_burn_burnmomnorm_63d_base_v074_signal(cashneq, opex, ncfo):
    lb = np.log1p(_f18_burn_opex(opex, ncfo))
    lc = np.log(cashneq.replace(0, np.nan))
    burn_ramp = lb - lb.shift(21)
    cash_chg = lc - lc.shift(63)
    b = burn_ramp + cash_chg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite distress: cash-drawdown x burn-intensity x weak-coverage rank blend
def f18cr_f18_cash_runway_burn_distresscomposite_base_v075_signal(cashneq, opex, ncfo):
    peak = _rmax(cashneq, 252)
    cashdd = (1.0 - cashneq / peak.replace(0, np.nan)).clip(lower=0)
    burnfrac = (_f18_burn_opex(opex, ncfo) / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    covrank = _rank(_f18_coverage(ncfo, opex), 252)
    b = cashdd + burnfrac - covrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18cr_f18_cash_runway_burn_runwayopex_63d_base_v001_signal,
    f18cr_f18_cash_runway_burn_runwayopexsm_63d_base_v002_signal,
    f18cr_f18_cash_runway_burn_monthscash_21d_base_v003_signal,
    f18cr_f18_cash_runway_burn_runwaycapex_63d_base_v004_signal,
    f18cr_f18_cash_runway_burn_runwaycapexsm_63d_base_v005_signal,
    f18cr_f18_cash_runway_burn_runwayspread_63d_base_v006_signal,
    f18cr_f18_cash_runway_burn_runwayopexz_252d_base_v007_signal,
    f18cr_f18_cash_runway_burn_runwaycapexz_126d_base_v008_signal,
    f18cr_f18_cash_runway_burn_runwayopexrank_504d_base_v009_signal,
    f18cr_f18_cash_runway_burn_monthsrank_252d_base_v010_signal,
    f18cr_f18_cash_runway_burn_depletion_63d_base_v011_signal,
    f18cr_f18_cash_runway_burn_depletioncapex_63d_base_v012_signal,
    f18cr_f18_cash_runway_burn_burnlevel_21d_base_v013_signal,
    f18cr_f18_cash_runway_burn_burnfrac_63d_base_v014_signal,
    f18cr_f18_cash_runway_burn_depletionz_252d_base_v015_signal,
    f18cr_f18_cash_runway_burn_coverage_63d_base_v016_signal,
    f18cr_f18_cash_runway_burn_covgap_63d_base_v017_signal,
    f18cr_f18_cash_runway_burn_coveragez_126d_base_v018_signal,
    f18cr_f18_cash_runway_burn_cashburncov_63d_base_v019_signal,
    f18cr_f18_cash_runway_burn_runwaytrend_63d_base_v020_signal,
    f18cr_f18_cash_runway_burn_runwayyoy_252d_base_v021_signal,
    f18cr_f18_cash_runway_burn_depletiontrend_63d_base_v022_signal,
    f18cr_f18_cash_runway_burn_covtrend_126d_base_v023_signal,
    f18cr_f18_cash_runway_burn_cashtrend_63d_base_v024_signal,
    f18cr_f18_cash_runway_burn_cashdd_252d_base_v025_signal,
    f18cr_f18_cash_runway_burn_cashz_252d_base_v026_signal,
    f18cr_f18_cash_runway_burn_cashrank_504d_base_v027_signal,
    f18cr_f18_cash_runway_burn_lowcashtime_252d_base_v028_signal,
    f18cr_f18_cash_runway_burn_burntime_252d_base_v029_signal,
    f18cr_f18_cash_runway_burn_burnonset_252d_base_v030_signal,
    f18cr_f18_cash_runway_burn_negncfotime_252d_base_v031_signal,
    f18cr_f18_cash_runway_burn_burnintensity_63d_base_v032_signal,
    f18cr_f18_cash_runway_burn_finfundburn_63d_base_v033_signal,
    f18cr_f18_cash_runway_burn_findepcapex_63d_base_v034_signal,
    f18cr_f18_cash_runway_burn_selffundgap_63d_base_v035_signal,
    f18cr_f18_cash_runway_burn_finz_252d_base_v036_signal,
    f18cr_f18_cash_runway_burn_runwaywithfin_63d_base_v037_signal,
    f18cr_f18_cash_runway_burn_burntermratio_base_v038_signal,
    f18cr_f18_cash_runway_burn_runwaytermratio_base_v039_signal,
    f18cr_f18_cash_runway_burn_cashtermratio_base_v040_signal,
    f18cr_f18_cash_runway_burn_burnvol_126d_base_v041_signal,
    f18cr_f18_cash_runway_burn_cashcv_252d_base_v042_signal,
    f18cr_f18_cash_runway_burn_covvol_252d_base_v043_signal,
    f18cr_f18_cash_runway_burn_covgapsignmag_63d_base_v044_signal,
    f18cr_f18_cash_runway_burn_depletiontanh_63d_base_v045_signal,
    f18cr_f18_cash_runway_burn_fcfsignlog_21d_base_v046_signal,
    f18cr_f18_cash_runway_burn_distressX_63d_base_v047_signal,
    f18cr_f18_cash_runway_burn_burnXcashdd_252d_base_v048_signal,
    f18cr_f18_cash_runway_burn_capexdrain_63d_base_v049_signal,
    f18cr_f18_cash_runway_burn_capexvsncfo_63d_base_v050_signal,
    f18cr_f18_cash_runway_burn_runwayopexsm_126d_base_v051_signal,
    f18cr_f18_cash_runway_burn_runwaycapexrank_252d_base_v052_signal,
    f18cr_f18_cash_runway_burn_runwaydisp_63d_base_v053_signal,
    f18cr_f18_cash_runway_burn_monthsema_63d_base_v054_signal,
    f18cr_f18_cash_runway_burn_critruntime_252d_base_v055_signal,
    f18cr_f18_cash_runway_burn_burnaccel_63d_base_v056_signal,
    f18cr_f18_cash_runway_burn_deplaccel_42d_base_v057_signal,
    f18cr_f18_cash_runway_burn_runwaycurv_63d_base_v058_signal,
    f18cr_f18_cash_runway_burn_finposttime_252d_base_v059_signal,
    f18cr_f18_cash_runway_burn_finvol_252d_base_v060_signal,
    f18cr_f18_cash_runway_burn_finfundstreak_base_v061_signal,
    f18cr_f18_cash_runway_burn_yearstozero_base_v062_signal,
    f18cr_f18_cash_runway_burn_worstcaserun_252d_base_v063_signal,
    f18cr_f18_cash_runway_burn_bestcaserun_252d_base_v064_signal,
    f18cr_f18_cash_runway_burn_selfsuffic_63d_base_v065_signal,
    f18cr_f18_cash_runway_burn_ncfocashyield_63d_base_v066_signal,
    f18cr_f18_cash_runway_burn_opexcashturn_63d_base_v067_signal,
    f18cr_f18_cash_runway_burn_burnfracrank_252d_base_v068_signal,
    f18cr_f18_cash_runway_burn_capexburnz_126d_base_v069_signal,
    f18cr_f18_cash_runway_burn_cashyieldz_252d_base_v070_signal,
    f18cr_f18_cash_runway_burn_runwaydd_252d_base_v071_signal,
    f18cr_f18_cash_runway_burn_minrunway_126d_base_v072_signal,
    f18cr_f18_cash_runway_burn_runwaydisp_multi_base_v073_signal,
    f18cr_f18_cash_runway_burn_burnmomnorm_63d_base_v074_signal,
    f18cr_f18_cash_runway_burn_distresscomposite_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_CASH_RUNWAY_BURN_REGISTRY_001_075 = REGISTRY


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

    # ncfo swings widely around opex so burn/coverage regimes flip on/off
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

    print("OK f18_cash_runway_burn_base_001_075_claude: %d features pass" % n_features)
