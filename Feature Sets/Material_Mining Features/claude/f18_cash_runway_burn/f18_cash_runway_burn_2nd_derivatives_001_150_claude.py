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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (cash runway / burn) =====
def _burn_opex(opex, ncfo):
    return (opex - ncfo).clip(lower=0.0)


def _burn_capex(ncfo, capex):
    return (-ncfo + capex).clip(lower=0.0)


def _runway_opex(cashneq, opex, ncfo):
    burn = (opex - ncfo).clip(lower=0.0)
    return cashneq / burn.replace(0, np.nan)


def _runway_capex(cashneq, ncfo, capex):
    burn = (-ncfo + capex).clip(lower=0.0)
    return cashneq / burn.replace(0, np.nan)


def _coverage(ncfo, opex):
    return ncfo / opex.replace(0, np.nan)


# ============================================================
# Each feature: build a cash-runway/burn base series inline, then take its
# 1st math derivative (slope) over a window matched to the base window.

# slope of log opex-runway (survival-horizon velocity), 21d
def f18cr_f18_cash_runway_burn_runwayopex_21d_slope_v001_signal(cashneq, opex, ncfo):
    base = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log opex-runway, 63d (slower survival velocity)
def f18cr_f18_cash_runway_burn_runwayopex_63d_slope_v002_signal(cashneq, opex, ncfo):
    base = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log capex-runway, 21d (FCF-survival velocity)
def f18cr_f18_cash_runway_burn_runwaycapex_21d_slope_v003_signal(cashneq, ncfo, capex):
    base = np.log1p(_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log capex-runway, 63d
def f18cr_f18_cash_runway_burn_runwaycapex_63d_slope_v004_signal(cashneq, ncfo, capex):
    base = np.log1p(_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of months-of-cash, 21d (survival-months velocity)
def f18cr_f18_cash_runway_burn_monthscash_21d_slope_v005_signal(cashneq, opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    base = (3.0 * cashneq / burn.replace(0, np.nan)).clip(upper=120.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depletion rate (burn/cash), 21d (burn-pressure velocity)
def f18cr_f18_cash_runway_burn_depletion_21d_slope_v006_signal(cashneq, opex, ncfo):
    base = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depletion rate, 63d
def f18cr_f18_cash_runway_burn_depletion_63d_slope_v007_signal(cashneq, opex, ncfo):
    base = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-depletion (fcf-burn/cash), 21d
def f18cr_f18_cash_runway_burn_depletioncapex_21d_slope_v008_signal(cashneq, ncfo, capex):
    base = _burn_capex(ncfo, capex) / cashneq.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage (ncfo/opex), 21d (self-funding velocity)
def f18cr_f18_cash_runway_burn_coverage_21d_slope_v009_signal(ncfo, opex):
    base = _coverage(ncfo, opex)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage, 63d
def f18cr_f18_cash_runway_burn_coverage_63d_slope_v010_signal(ncfo, opex):
    base = _coverage(ncfo, opex)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn fraction (burn/opex), 21d (uncovered-spend velocity)
def f18cr_f18_cash_runway_burn_burnfrac_21d_slope_v011_signal(opex, ncfo):
    base = _burn_opex(opex, ncfo) / opex.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-burn-to-opex-burn ratio, 21d (which burn channel dominates)
def f18cr_f18_cash_runway_burn_burnlevel_21d_slope_v012_signal(opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    base = (bc / bo.replace(0, np.nan)).clip(upper=20.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex burn as fraction of capex (uncovered-development share), 21d
def f18cr_f18_cash_runway_burn_capexburn_21d_slope_v013_signal(ncfo, capex):
    base = _burn_capex(ncfo, capex) / capex.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log cash balance, 21d (treasury depletion velocity)
def f18cr_f18_cash_runway_burn_cash_21d_slope_v014_signal(cashneq):
    base = np.log(cashneq.replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log cash balance, 63d
def f18cr_f18_cash_runway_burn_cash_63d_slope_v015_signal(cashneq):
    base = np.log(cashneq.replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash drawdown from 252d peak, 21d (treasury bleeding velocity)
def f18cr_f18_cash_runway_burn_cashdd_21d_slope_v016_signal(cashneq):
    peak = _rmax(cashneq, 252)
    base = cashneq / peak.replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash z-score, 21d (treasury-regime velocity)
def f18cr_f18_cash_runway_burn_cashz_21d_slope_v017_signal(cashneq):
    base = _z(np.log(cashneq.replace(0, np.nan)), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash percentile-rank, 21d (treasury-percentile velocity)
def f18cr_f18_cash_runway_burn_cashrank_21d_slope_v018_signal(cashneq):
    base = _rank(cashneq, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex-runway z-score, 21d (distress-regime velocity)
def f18cr_f18_cash_runway_burn_runwayz_21d_slope_v019_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    base = _z(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex-runway percentile-rank, 63d
def f18cr_f18_cash_runway_burn_runwayrank_63d_slope_v020_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    base = _rank(r, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage z-score, 21d
def f18cr_f18_cash_runway_burn_covz_21d_slope_v021_signal(ncfo, opex):
    base = _z(_coverage(ncfo, opex), 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage-gap dispersion over a quarter, 21d (self-funding instability)
def f18cr_f18_cash_runway_burn_covgap_21d_slope_v022_signal(ncfo, opex):
    gap = (1.0 - _coverage(ncfo, opex)).clip(lower=-2.0, upper=2.0)
    base = gap.rolling(63, min_periods=21).std()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of smoothed opex-runway, 63d (structural survival velocity)
def f18cr_f18_cash_runway_burn_runwaysm_63d_slope_v023_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    base = r.rolling(63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of all-in runway (cash over total burn), 21d
def f18cr_f18_cash_runway_burn_allinrunway_21d_slope_v024_signal(cashneq, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    base = np.log1p((cashneq / (bo + bc).replace(0, np.nan)).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of total-burn-over-cash, 63d (combined depletion velocity)
def f18cr_f18_cash_runway_burn_totalburn_63d_slope_v025_signal(cashneq, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    base = np.log1p(((bo + bc) / cashneq.replace(0, np.nan)).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-mix (opex share of total burn), 21d
def f18cr_f18_cash_runway_burn_burnmix_21d_slope_v026_signal(opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    base = bo / (bo + bc).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing/opex intensity, 21d (raise-cadence velocity)
def f18cr_f18_cash_runway_burn_fin_21d_slope_v027_signal(ncff, opex):
    base = ncff / opex.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing/cash top-up rate, 63d
def f18cr_f18_cash_runway_burn_fintopup_63d_slope_v028_signal(ncff, cashneq):
    base = (ncff / cashneq.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing-share-of-burn, 21d
def f18cr_f18_cash_runway_burn_finshare_21d_slope_v029_signal(ncff, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    base = (ncff / (bo + bc).replace(0, np.nan)).clip(lower=-5.0, upper=5.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex/cash drain, 21d (development-drain velocity)
def f18cr_f18_cash_runway_burn_capexdrain_21d_slope_v030_signal(cashneq, capex):
    base = capex / cashneq.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex/opex mix, 63d
def f18cr_f18_cash_runway_burn_capexopex_63d_slope_v031_signal(capex, opex):
    base = (capex / opex.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log capex level, 21d
def f18cr_f18_cash_runway_burn_capexlvl_21d_slope_v032_signal(capex):
    base = np.log(capex.replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of free-cash-flow margin (fcf/opex), 21d
def f18cr_f18_cash_runway_burn_fcfmargin_21d_slope_v033_signal(ncfo, capex, opex):
    base = (ncfo - capex) / opex.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo/cash yield, 21d
def f18cr_f18_cash_runway_burn_ncfoyield_21d_slope_v034_signal(ncfo, cashneq):
    base = ncfo / cashneq.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex/cash turn, 63d
def f18cr_f18_cash_runway_burn_opexturn_63d_slope_v035_signal(opex, cashneq):
    base = (opex / cashneq.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-burn coverage (log cash/burn) z, 21d
def f18cr_f18_cash_runway_burn_cashburncovz_21d_slope_v036_signal(cashneq, opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    cov = np.log1p((cashneq / burn.replace(0, np.nan)).clip(lower=0))
    base = _z(cov, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-coverage-vol ratio (runway per burn instability), 21d
def f18cr_f18_cash_runway_burn_runwaydisp_21d_slope_v037_signal(cashneq, opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    bv = (burn / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).std()
    base = bv
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn term ratio (short/long burn), 63d
def f18cr_f18_cash_runway_burn_burnterm_63d_slope_v038_signal(opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    short = burn.rolling(63, min_periods=21).mean()
    long = burn.rolling(252, min_periods=126).mean()
    base = short / long.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage term spread (short-long), 21d
def f18cr_f18_cash_runway_burn_covterm_21d_slope_v039_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    short = cov.rolling(63, min_periods=21).mean()
    long = cov.rolling(252, min_periods=126).mean()
    base = short - long
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-rate volatility, 63d (burn-instability velocity)
def f18cr_f18_cash_runway_burn_burnvol_63d_slope_v040_signal(cashneq, opex, ncfo):
    d = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    base = d.rolling(126, min_periods=63).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash coefficient-of-variation, 63d
def f18cr_f18_cash_runway_burn_cashcv_63d_slope_v041_signal(cashneq):
    m = _mean(cashneq, 126)
    sd = _std(cashneq, 126)
    base = sd / m.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage volatility, 63d
def f18cr_f18_cash_runway_burn_covvol_63d_slope_v042_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = cov.rolling(252, min_periods=126).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tanh-squashed depletion, 21d
def f18cr_f18_cash_runway_burn_depltanh_21d_slope_v043_signal(cashneq, opex, ncfo):
    d = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    base = np.tanh(8.0 * d)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of signed-root coverage gap, 21d
def f18cr_f18_cash_runway_burn_covgaproot_21d_slope_v044_signal(ncfo, opex):
    gap = 1.0 - _coverage(ncfo, opex)
    base = np.sign(gap) * (gap.abs() ** 0.5)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of distress interaction (depl x log burn/cash), 21d
def f18cr_f18_cash_runway_burn_distressX_21d_slope_v045_signal(cashneq, opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    depl = burn / cashneq.replace(0, np.nan)
    base = depl * np.log1p((burn / cashneq.replace(0, np.nan)).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-drain x weak-coverage interaction, 21d
def f18cr_f18_cash_runway_burn_capexXcov_21d_slope_v046_signal(cashneq, capex, ncfo, opex):
    drain = capex / cashneq.replace(0, np.nan)
    weakcov = (1.0 - _coverage(ncfo, opex)).clip(lower=0)
    base = drain * weakcov
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing-dependence buffer alone (fin reliance level), 21d
def f18cr_f18_cash_runway_burn_survbuffer_21d_slope_v047_signal(opex, ncff):
    findep = (ncff.clip(lower=0) / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    base = findep
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-burn coverage to year-floor (tanh), 21d
def f18cr_f18_cash_runway_burn_safetyfloor_21d_slope_v048_signal(cashneq, opex, ncfo):
    r = _runway_opex(cashneq, opex, ncfo)
    base = np.tanh(0.5 * (r - 4.0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo z-score, 21d
def f18cr_f18_cash_runway_burn_ncfoz_21d_slope_v049_signal(ncfo, opex):
    base = _z(ncfo / opex.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex/cash z-score, 21d
def f18cr_f18_cash_runway_burn_capexz_21d_slope_v050_signal(capex, cashneq):
    base = _z(capex / cashneq.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log opex-runway, 5d (fast survival velocity)
def f18cr_f18_cash_runway_burn_runwayopex_5d_slope_v051_signal(cashneq, opex, ncfo):
    base = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depletion rate, 5d
def f18cr_f18_cash_runway_burn_depletion_5d_slope_v052_signal(cashneq, opex, ncfo):
    base = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage, 5d
def f18cr_f18_cash_runway_burn_coverage_5d_slope_v053_signal(ncfo, opex):
    base = _coverage(ncfo, opex)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log cash, 5d
def f18cr_f18_cash_runway_burn_cash_5d_slope_v054_signal(cashneq):
    base = np.log(cashneq.replace(0, np.nan))
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-runway z, 63d
def f18cr_f18_cash_runway_burn_runwaycapexz_63d_slope_v055_signal(cashneq, ncfo, capex):
    r = np.log1p(_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    base = _z(r, 126)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of all-in depletion volatility, 63d
def f18cr_f18_cash_runway_burn_allindeplvol_63d_slope_v056_signal(cashneq, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    d = (bo + bc) / cashneq.replace(0, np.nan)
    base = d.rolling(126, min_periods=63).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of treasury pressure (burn+0.5capex)/cash, 21d
def f18cr_f18_cash_runway_burn_treaspress_21d_slope_v057_signal(cashneq, opex, ncfo, capex):
    burnrate = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    capexrate = capex / cashneq.replace(0, np.nan)
    base = (burnrate + 0.5 * capexrate).rolling(21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo-to-capex coverage, 21d
def f18cr_f18_cash_runway_burn_ncfocapex_21d_slope_v058_signal(ncfo, capex):
    base = (ncfo / capex.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fcf/cash yield, 21d
def f18cr_f18_cash_runway_burn_fcfyield_21d_slope_v059_signal(ncfo, capex, cashneq):
    base = (ncfo - capex) / cashneq.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash drawdown from 504d peak, 63d
def f18cr_f18_cash_runway_burn_cashdd504_63d_slope_v060_signal(cashneq):
    peak = _rmax(cashneq, 504)
    base = cashneq / peak.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash recovery off 504d trough, 63d
def f18cr_f18_cash_runway_burn_cashrecov_63d_slope_v061_signal(cashneq):
    trough = _rmin(cashneq, 504)
    base = cashneq / trough.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex-vs-capex runway spread, 21d (which burn channel sets survival)
def f18cr_f18_cash_runway_burn_runwaymeddev_21d_slope_v062_signal(cashneq, opex, ncfo, capex):
    ro = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    rc = np.log1p(_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    base = ro - rc
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage median-deviation, 21d
def f18cr_f18_cash_runway_burn_covdev_21d_slope_v063_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = cov - cov.rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo year-over-year change, 63d
def f18cr_f18_cash_runway_burn_ncfoyoy_63d_slope_v064_signal(ncfo, opex):
    r = ncfo / opex.replace(0, np.nan)
    base = r - r.shift(252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex cutback (capex vs 252d peak), 21d
def f18cr_f18_cash_runway_burn_capexcut_21d_slope_v065_signal(capex):
    peak = _rmax(capex, 252)
    base = capex / peak.replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing percentile-rank, 63d
def f18cr_f18_cash_runway_burn_finrank_63d_slope_v066_signal(ncff, opex):
    base = _rank(ncff / opex.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing momentum (ncff/opex chg), 21d
def f18cr_f18_cash_runway_burn_finmom_21d_slope_v067_signal(ncff, opex):
    r = ncff / opex.replace(0, np.nan)
    base = r - r.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-vs-financing ratio, 63d
def f18cr_f18_cash_runway_burn_burnvsfin_63d_slope_v068_signal(opex, ncfo, ncff):
    burn = _burn_opex(opex, ncfo)
    base = (burn / ncff.clip(lower=1.0)).clip(upper=20.0).rolling(21, min_periods=10).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex share of total spend (capex/(capex+opex)), 21d
def f18cr_f18_cash_runway_burn_capexvsburn_21d_slope_v069_signal(capex, opex):
    base = capex / (capex + opex).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of structural runway (504d mean), 63d
def f18cr_f18_cash_runway_burn_runwaystruct_63d_slope_v070_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    base = r.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of structural coverage (504d mean), 63d
def f18cr_f18_cash_runway_burn_covstruct_63d_slope_v071_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    base = cov.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of all-in runway z, 21d
def f18cr_f18_cash_runway_burn_allinrunwayz_21d_slope_v072_signal(cashneq, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    r = np.log1p((cashneq / (bo + bc).replace(0, np.nan)).clip(lower=0))
    base = _z(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-mix z, 21d
def f18cr_f18_cash_runway_burn_burnmixz_21d_slope_v073_signal(opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    mix = bo / (bo + bc).replace(0, np.nan)
    base = _z(mix, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of safety-runway worst-case (cash/peak-burn), 21d
def f18cr_f18_cash_runway_burn_worstcase_21d_slope_v074_signal(cashneq, opex, ncfo):
    peak_burn = _rmax(_burn_opex(opex, ncfo), 252)
    base = np.log1p((cashneq / peak_burn.replace(0, np.nan)).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of years-to-zero (cash/annual-burn), 63d
def f18cr_f18_cash_runway_burn_yearstozero_63d_slope_v075_signal(cashneq, opex, ncfo):
    annual = _burn_opex(opex, ncfo).rolling(252, min_periods=126).mean() * 4.0
    base = np.log1p((cashneq / annual.replace(0, np.nan)).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex-runway, 126d (very slow survival drift)
def f18cr_f18_cash_runway_burn_runwayopex_126d_slope_v076_signal(cashneq, opex, ncfo):
    base = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depletion rate, 126d
def f18cr_f18_cash_runway_burn_depletion_126d_slope_v077_signal(cashneq, opex, ncfo):
    base = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage, 126d
def f18cr_f18_cash_runway_burn_coverage_126d_slope_v078_signal(ncfo, opex):
    base = _coverage(ncfo, opex)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log cash, 126d
def f18cr_f18_cash_runway_burn_cash_126d_slope_v079_signal(cashneq):
    base = np.log(cashneq.replace(0, np.nan))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-runway, 126d
def f18cr_f18_cash_runway_burn_runwaycapex_126d_slope_v080_signal(cashneq, ncfo, capex):
    base = np.log1p(_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage percentile-rank (252d), 21d (self-funding-percentile velocity)
def f18cr_f18_cash_runway_burn_covsm_21d_slope_v081_signal(ncfo, opex):
    base = _rank(_coverage(ncfo, opex), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depletion percentile-rank (252d), 21d (burn-pressure-percentile velocity)
def f18cr_f18_cash_runway_burn_deplsm_21d_slope_v082_signal(cashneq, opex, ncfo):
    d = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    base = _rank(d, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex burn surprise (burn/norm-1), 21d
def f18cr_f18_cash_runway_burn_burnsurprise_21d_slope_v083_signal(opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    norm = burn.rolling(252, min_periods=126).mean()
    base = burn / norm.replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fcf margin de-trended, 21d
def f18cr_f18_cash_runway_burn_fcfmargindev_21d_slope_v084_signal(ncfo, capex, opex):
    fcfm = (ncfo - capex) / opex.replace(0, np.nan)
    base = fcfm - fcfm.rolling(126, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex term ratio (short/long capex/cash), 63d
def f18cr_f18_cash_runway_burn_capexterm_63d_slope_v085_signal(capex, cashneq):
    r = capex / cashneq.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    base = short / long.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing term spread (short-long), 21d
def f18cr_f18_cash_runway_burn_finterm_21d_slope_v086_signal(ncff, opex):
    r = ncff / opex.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    base = short - long
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of max-depletion (126d), 63d
def f18cr_f18_cash_runway_burn_maxdepl_63d_slope_v087_signal(cashneq, opex, ncfo):
    d = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    base = _rmax(d, 126)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of min-runway (126d), 63d
def f18cr_f18_cash_runway_burn_minrunway_63d_slope_v088_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    base = _rmin(r, 126)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of runway drawdown (252d), 21d
def f18cr_f18_cash_runway_burn_runwaydd_21d_slope_v089_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    base = r - _rmax(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-runway drawdown (252d), 21d
def f18cr_f18_cash_runway_burn_capexrunwaydd_21d_slope_v090_signal(cashneq, ncfo, capex):
    r = np.log1p(_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    base = r - _rmax(r, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex/cash drain smoothed, 63d
def f18cr_f18_cash_runway_burn_capexdrain_63d_slope_v091_signal(cashneq, capex):
    base = (capex / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo/cash yield z, 21d
def f18cr_f18_cash_runway_burn_ncfoyieldz_21d_slope_v092_signal(ncfo, cashneq):
    base = _z(ncfo / cashneq.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of all-in burn tanh, 21d
def f18cr_f18_cash_runway_burn_allinburntanh_21d_slope_v093_signal(cashneq, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    d = (bo + bc) / cashneq.replace(0, np.nan)
    base = np.tanh(5.0 * d)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of signed-root depletion, 21d
def f18cr_f18_cash_runway_burn_deplsignroot_21d_slope_v094_signal(cashneq, opex, ncfo):
    d = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    base = np.sign(d) * (d.abs() ** 0.5)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage-gap tanh, 21d
def f18cr_f18_cash_runway_burn_covgaptanh_21d_slope_v095_signal(ncfo, opex):
    gap = 1.0 - _coverage(ncfo, opex)
    base = np.tanh(2.0 * gap)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn x low-cash interaction, 21d
def f18cr_f18_cash_runway_burn_burnXlowcash_21d_slope_v096_signal(cashneq, opex, ncfo):
    burnfrac = (_burn_opex(opex, ncfo) / opex.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    cashlow = 0.5 - _rank(cashneq, 252)
    base = burnfrac * cashlow
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing x burn interaction, 21d
def f18cr_f18_cash_runway_burn_finXburn_21d_slope_v097_signal(ncff, opex, ncfo):
    finrel = ncff.clip(lower=0) / opex.replace(0, np.nan)
    burn = _burn_opex(opex, ncfo)
    base = (finrel * (burn / opex.replace(0, np.nan))).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of self-funding gap rate ((ncfo-opex)/cash), 21d
def f18cr_f18_cash_runway_burn_selffundgap_21d_slope_v098_signal(cashneq, opex, ncfo):
    base = ((ncfo - opex) / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing-runway extension, 63d
def f18cr_f18_cash_runway_burn_finrunway_63d_slope_v099_signal(cashneq, ncff):
    raise_yr = ncff.clip(lower=0).rolling(252, min_periods=126).mean() * 4.0
    base = (raise_yr / cashneq.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of runway-per-burn-vol ratio, 63d
def f18cr_f18_cash_runway_burn_runwayperbv_63d_slope_v100_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    burn = _burn_opex(opex, ncfo)
    bv = (burn / cashneq.replace(0, np.nan)).rolling(126, min_periods=63).std()
    base = r / bv.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of months-of-cash EMA, 21d
def f18cr_f18_cash_runway_burn_monthsema_21d_slope_v101_signal(cashneq, opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    m = (3.0 * cashneq / burn.replace(0, np.nan)).clip(upper=120.0)
    base = m.ewm(span=63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex/cash turn z, 21d
def f18cr_f18_cash_runway_burn_opexturnz_21d_slope_v102_signal(opex, cashneq):
    base = _z(opex / cashneq.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-burn term ratio (short/long fcf-burn), 63d
def f18cr_f18_cash_runway_burn_capexburnz_63d_slope_v103_signal(ncfo, capex):
    burn = _burn_capex(ncfo, capex)
    short = burn.rolling(63, min_periods=21).mean()
    long = burn.rolling(252, min_periods=126).mean()
    base = short / long.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-trend (63d) itself, 21d
def f18cr_f18_cash_runway_burn_cashtrend_21d_slope_v104_signal(cashneq):
    lc = np.log(cashneq.replace(0, np.nan))
    base = lc - lc.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage gap quarter-change, 21d
def f18cr_f18_cash_runway_burn_covgapchg_21d_slope_v105_signal(ncfo, opex):
    gap = (1.0 - _coverage(ncfo, opex)).clip(lower=-2.0, upper=2.0)
    base = gap - gap.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of total-burn-over-cash, 21d
def f18cr_f18_cash_runway_burn_totalburn_21d_slope_v106_signal(cashneq, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    base = (bo + bc) / cashneq.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex/opex mix z, 21d
def f18cr_f18_cash_runway_burn_capexopexz_21d_slope_v107_signal(capex, opex):
    base = _z(capex / opex.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing-keepup (ncff/burn change), 63d
def f18cr_f18_cash_runway_burn_finkeepup_63d_slope_v108_signal(ncff, opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    cov = (ncff / burn.replace(0, np.nan)).clip(lower=-5.0, upper=5.0)
    base = cov - cov.shift(126)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo-capex coverage smoothed, 63d
def f18cr_f18_cash_runway_burn_ncfocapexsm_63d_slope_v109_signal(ncfo, capex):
    base = (ncfo / capex.replace(0, np.nan)).clip(lower=-10.0, upper=10.0).rolling(63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash range position (252d), 21d
def f18cr_f18_cash_runway_burn_cashrngpos_21d_slope_v110_signal(cashneq):
    hi = _rmax(cashneq, 252)
    lo = _rmin(cashneq, 252)
    base = (cashneq - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of all-in runway trend, 21d
def f18cr_f18_cash_runway_burn_allinrunwaytrend_21d_slope_v111_signal(cashneq, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    r = np.log1p((cashneq / (bo + bc).replace(0, np.nan)).clip(lower=0))
    base = r - r.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of survival composite (z runway - z burnvol - z finrel), 21d
def f18cr_f18_cash_runway_burn_survcomposite_21d_slope_v112_signal(cashneq, opex, ncfo, ncff):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0)).rolling(126, min_periods=63).mean()
    burn = _burn_opex(opex, ncfo)
    bv = (burn / cashneq.replace(0, np.nan)).rolling(126, min_periods=63).std()
    finrel = (ncff.clip(lower=0) / opex.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    base = _z(r, 252) - _z(bv, 252) - _z(finrel, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of zombie proxy, 21d
def f18cr_f18_cash_runway_burn_zombie_21d_slope_v113_signal(cashneq, opex, ncfo, ncff):
    burning = (_burn_opex(opex, ncfo) > 0).astype(float)
    raising = (ncff > 0).astype(float)
    lowcash = (0.5 - _rank(cashneq, 252)).clip(lower=0)
    base = (burning * raising).rolling(126, min_periods=63).mean() + lowcash
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of self-funding-time, 63d
def f18cr_f18_cash_runway_burn_selffundtime_63d_slope_v114_signal(ncfo, opex):
    cov = _coverage(ncfo, opex)
    ok = (cov >= 1.0).astype(float)
    frac = ok.rolling(252, min_periods=126).mean()
    surplus = (cov - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    base = frac + 0.3 * surplus
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing-dependence-time, 63d
def f18cr_f18_cash_runway_burn_findeptime_63d_slope_v115_signal(ncff, opex, ncfo):
    burn = _burn_opex(opex, ncfo)
    rel = ((ncff >= burn) & (burn > 0)).astype(float)
    frac = rel.rolling(252, min_periods=126).mean()
    ratio = (ncff / burn.replace(0, np.nan)).clip(lower=0, upper=5.0).rolling(63, min_periods=21).mean()
    base = frac + 0.2 * ratio
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of critical-runway-time, 63d
def f18cr_f18_cash_runway_burn_crittime_63d_slope_v116_signal(cashneq, opex, ncfo):
    r = _runway_opex(cashneq, opex, ncfo)
    crit = (r < 4.0).astype(float)
    frac = crit.rolling(252, min_periods=126).mean()
    shortfall = (4.0 - r.clip(upper=4.0)).rolling(63, min_periods=21).mean()
    base = frac + 0.25 * shortfall
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of negative-ncfo-time, 63d
def f18cr_f18_cash_runway_burn_negncfotime_63d_slope_v117_signal(ncfo, opex):
    neg = (ncfo < 0).astype(float)
    frac = neg.rolling(252, min_periods=126).mean()
    depth = (-ncfo / opex.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    base = frac + 0.5 * depth
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-burn regime time (fraction FCF negative), 63d
def f18cr_f18_cash_runway_burn_burntime_63d_slope_v118_signal(ncfo, capex):
    burning = (_burn_capex(ncfo, capex) > 0).astype(float)
    base = burning.rolling(252, min_periods=126).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex-runway, 42d (intermediate survival velocity)
def f18cr_f18_cash_runway_burn_runwayopex_42d_slope_v119_signal(cashneq, opex, ncfo):
    base = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage, 42d
def f18cr_f18_cash_runway_burn_coverage_42d_slope_v120_signal(ncfo, opex):
    base = _coverage(ncfo, opex)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depletion rate, 42d
def f18cr_f18_cash_runway_burn_depletion_42d_slope_v121_signal(cashneq, opex, ncfo):
    base = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log cash, 42d
def f18cr_f18_cash_runway_burn_cash_42d_slope_v122_signal(cashneq):
    base = np.log(cashneq.replace(0, np.nan))
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-depletion, 63d
def f18cr_f18_cash_runway_burn_capexdepl_63d_slope_v123_signal(cashneq, ncfo, capex):
    base = _burn_capex(ncfo, capex) / cashneq.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo/cash yield, 42d
def f18cr_f18_cash_runway_burn_ncfoopex_42d_slope_v124_signal(ncfo, cashneq):
    base = ncfo / cashneq.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex/cash, 42d
def f18cr_f18_cash_runway_burn_capexcash_42d_slope_v125_signal(capex, cashneq):
    base = capex / cashneq.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing/opex, 42d
def f18cr_f18_cash_runway_burn_finopex_42d_slope_v126_signal(ncff, opex):
    base = ncff / opex.replace(0, np.nan)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-fraction dispersion (uncovered-share instability), 63d
def f18cr_f18_cash_runway_burn_burnfrac_63d_slope_v127_signal(opex, ncfo):
    frac = _burn_opex(opex, ncfo) / opex.replace(0, np.nan)
    base = frac.rolling(126, min_periods=63).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fcf margin, 63d
def f18cr_f18_cash_runway_burn_fcfmargin_63d_slope_v128_signal(ncfo, capex, opex):
    base = (ncfo - capex) / opex.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of opex-runway smoothed (126d), 63d
def f18cr_f18_cash_runway_burn_runwaysm126_63d_slope_v129_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    base = r.rolling(126, min_periods=63).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-runway smoothed (126d), 63d
def f18cr_f18_cash_runway_burn_capexrunwaysm_63d_slope_v130_signal(cashneq, ncfo, capex):
    r = np.log1p(_runway_capex(cashneq, ncfo, capex).clip(lower=0))
    base = r.rolling(126, min_periods=63).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-to-opex-burn ratio, 63d (burn-channel-dominance velocity)
def f18cr_f18_cash_runway_burn_burnlevel_63d_slope_v131_signal(opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    base = (bc / bo.replace(0, np.nan)).clip(upper=20.0).rolling(21, min_periods=10).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash percentile-rank (252d), 63d (treasury-percentile drift)
def f18cr_f18_cash_runway_burn_cashtrend21_63d_slope_v132_signal(cashneq):
    base = _rank(cashneq, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo yield rank, 63d
def f18cr_f18_cash_runway_burn_ncfoyieldrank_63d_slope_v133_signal(ncfo, cashneq):
    base = _rank(ncfo / cashneq.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage rank, 63d
def f18cr_f18_cash_runway_burn_covrank_63d_slope_v134_signal(ncfo, opex):
    base = _rank(_coverage(ncfo, opex), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-depletion rank, 63d
def f18cr_f18_cash_runway_burn_capexdeplrank_63d_slope_v135_signal(cashneq, ncfo, capex):
    base = _rank(_burn_capex(ncfo, capex) / cashneq.replace(0, np.nan), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing-share-rank, 63d
def f18cr_f18_cash_runway_burn_finsharerank_63d_slope_v136_signal(ncff, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    share = (ncff / (bo + bc).replace(0, np.nan)).clip(lower=-5.0, upper=5.0)
    base = _rank(share, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of structural depletion (504d mean), 63d
def f18cr_f18_cash_runway_burn_deplstruct_63d_slope_v137_signal(cashneq, opex, ncfo):
    d = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    base = d.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash CV (252d), 63d
def f18cr_f18_cash_runway_burn_cashcv252_63d_slope_v138_signal(cashneq):
    m = _mean(cashneq, 252)
    sd = _std(cashneq, 252)
    base = sd / m.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo-yield (ncfo/cash) volatility (126d), 63d
def f18cr_f18_cash_runway_burn_ncfovol_63d_slope_v139_signal(ncfo, cashneq):
    r = ncfo / cashneq.replace(0, np.nan)
    base = r.rolling(126, min_periods=63).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of runway volatility (252d), 63d
def f18cr_f18_cash_runway_burn_runwayvol_63d_slope_v140_signal(cashneq, opex, ncfo):
    r = np.log1p(_runway_opex(cashneq, opex, ncfo).clip(lower=0))
    base = r.rolling(252, min_periods=126).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of treasury pressure smoothed, 63d
def f18cr_f18_cash_runway_burn_treaspress_63d_slope_v141_signal(cashneq, opex, ncfo, capex):
    burnrate = _burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)
    capexrate = capex / cashneq.replace(0, np.nan)
    base = (burnrate + 0.5 * capexrate).rolling(63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-vs-cash divergence, 21d
def f18cr_f18_cash_runway_burn_burnvscash_21d_slope_v142_signal(cashneq, opex, ncfo):
    lb = np.log1p(_burn_opex(opex, ncfo))
    lc = np.log(cashneq.replace(0, np.nan))
    base = (lb - lb.shift(21)) + (lc - lc.shift(63))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of fcf-cash yield (de-trended), 63d
def f18cr_f18_cash_runway_burn_fcfyielddev_63d_slope_v143_signal(ncfo, capex, cashneq):
    y = (ncfo - capex) / cashneq.replace(0, np.nan)
    base = y - y.rolling(126, min_periods=63).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex/opex mix, 21d
def f18cr_f18_cash_runway_burn_capexopex_21d_slope_v144_signal(capex, opex):
    base = capex / opex.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financing/cash top-up, 21d
def f18cr_f18_cash_runway_burn_fintopup_21d_slope_v145_signal(ncff, cashneq):
    base = ncff / cashneq.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of all-in runway, 63d
def f18cr_f18_cash_runway_burn_allinrunway_63d_slope_v146_signal(cashneq, opex, ncfo, capex):
    bo = _burn_opex(opex, ncfo)
    bc = _burn_capex(ncfo, capex)
    base = np.log1p((cashneq / (bo + bc).replace(0, np.nan)).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coverage gap signed-root, 63d
def f18cr_f18_cash_runway_burn_covgaproot_63d_slope_v147_signal(ncfo, opex):
    gap = 1.0 - _coverage(ncfo, opex)
    base = np.sign(gap) * (gap.abs() ** 0.5)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex cutback, 63d
def f18cr_f18_cash_runway_burn_capexcut_63d_slope_v148_signal(capex):
    peak = _rmax(capex, 252)
    base = capex / peak.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo z-score, 63d
def f18cr_f18_cash_runway_burn_ncfoz_63d_slope_v149_signal(ncfo, opex):
    base = _z(ncfo / opex.replace(0, np.nan), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of safety-floor tanh, 63d
def f18cr_f18_cash_runway_burn_safetyfloor_63d_slope_v150_signal(cashneq, opex, ncfo):
    r = _runway_opex(cashneq, opex, ncfo)
    base = np.tanh(0.5 * (r - 4.0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18cr_f18_cash_runway_burn_runwayopex_21d_slope_v001_signal,
    f18cr_f18_cash_runway_burn_runwayopex_63d_slope_v002_signal,
    f18cr_f18_cash_runway_burn_runwaycapex_21d_slope_v003_signal,
    f18cr_f18_cash_runway_burn_runwaycapex_63d_slope_v004_signal,
    f18cr_f18_cash_runway_burn_monthscash_21d_slope_v005_signal,
    f18cr_f18_cash_runway_burn_depletion_21d_slope_v006_signal,
    f18cr_f18_cash_runway_burn_depletion_63d_slope_v007_signal,
    f18cr_f18_cash_runway_burn_depletioncapex_21d_slope_v008_signal,
    f18cr_f18_cash_runway_burn_coverage_21d_slope_v009_signal,
    f18cr_f18_cash_runway_burn_coverage_63d_slope_v010_signal,
    f18cr_f18_cash_runway_burn_burnfrac_21d_slope_v011_signal,
    f18cr_f18_cash_runway_burn_burnlevel_21d_slope_v012_signal,
    f18cr_f18_cash_runway_burn_capexburn_21d_slope_v013_signal,
    f18cr_f18_cash_runway_burn_cash_21d_slope_v014_signal,
    f18cr_f18_cash_runway_burn_cash_63d_slope_v015_signal,
    f18cr_f18_cash_runway_burn_cashdd_21d_slope_v016_signal,
    f18cr_f18_cash_runway_burn_cashz_21d_slope_v017_signal,
    f18cr_f18_cash_runway_burn_cashrank_21d_slope_v018_signal,
    f18cr_f18_cash_runway_burn_runwayz_21d_slope_v019_signal,
    f18cr_f18_cash_runway_burn_runwayrank_63d_slope_v020_signal,
    f18cr_f18_cash_runway_burn_covz_21d_slope_v021_signal,
    f18cr_f18_cash_runway_burn_covgap_21d_slope_v022_signal,
    f18cr_f18_cash_runway_burn_runwaysm_63d_slope_v023_signal,
    f18cr_f18_cash_runway_burn_allinrunway_21d_slope_v024_signal,
    f18cr_f18_cash_runway_burn_totalburn_63d_slope_v025_signal,
    f18cr_f18_cash_runway_burn_burnmix_21d_slope_v026_signal,
    f18cr_f18_cash_runway_burn_fin_21d_slope_v027_signal,
    f18cr_f18_cash_runway_burn_fintopup_63d_slope_v028_signal,
    f18cr_f18_cash_runway_burn_finshare_21d_slope_v029_signal,
    f18cr_f18_cash_runway_burn_capexdrain_21d_slope_v030_signal,
    f18cr_f18_cash_runway_burn_capexopex_63d_slope_v031_signal,
    f18cr_f18_cash_runway_burn_capexlvl_21d_slope_v032_signal,
    f18cr_f18_cash_runway_burn_fcfmargin_21d_slope_v033_signal,
    f18cr_f18_cash_runway_burn_ncfoyield_21d_slope_v034_signal,
    f18cr_f18_cash_runway_burn_opexturn_63d_slope_v035_signal,
    f18cr_f18_cash_runway_burn_cashburncovz_21d_slope_v036_signal,
    f18cr_f18_cash_runway_burn_runwaydisp_21d_slope_v037_signal,
    f18cr_f18_cash_runway_burn_burnterm_63d_slope_v038_signal,
    f18cr_f18_cash_runway_burn_covterm_21d_slope_v039_signal,
    f18cr_f18_cash_runway_burn_burnvol_63d_slope_v040_signal,
    f18cr_f18_cash_runway_burn_cashcv_63d_slope_v041_signal,
    f18cr_f18_cash_runway_burn_covvol_63d_slope_v042_signal,
    f18cr_f18_cash_runway_burn_depltanh_21d_slope_v043_signal,
    f18cr_f18_cash_runway_burn_covgaproot_21d_slope_v044_signal,
    f18cr_f18_cash_runway_burn_distressX_21d_slope_v045_signal,
    f18cr_f18_cash_runway_burn_capexXcov_21d_slope_v046_signal,
    f18cr_f18_cash_runway_burn_survbuffer_21d_slope_v047_signal,
    f18cr_f18_cash_runway_burn_safetyfloor_21d_slope_v048_signal,
    f18cr_f18_cash_runway_burn_ncfoz_21d_slope_v049_signal,
    f18cr_f18_cash_runway_burn_capexz_21d_slope_v050_signal,
    f18cr_f18_cash_runway_burn_runwayopex_5d_slope_v051_signal,
    f18cr_f18_cash_runway_burn_depletion_5d_slope_v052_signal,
    f18cr_f18_cash_runway_burn_coverage_5d_slope_v053_signal,
    f18cr_f18_cash_runway_burn_cash_5d_slope_v054_signal,
    f18cr_f18_cash_runway_burn_runwaycapexz_63d_slope_v055_signal,
    f18cr_f18_cash_runway_burn_allindeplvol_63d_slope_v056_signal,
    f18cr_f18_cash_runway_burn_treaspress_21d_slope_v057_signal,
    f18cr_f18_cash_runway_burn_ncfocapex_21d_slope_v058_signal,
    f18cr_f18_cash_runway_burn_fcfyield_21d_slope_v059_signal,
    f18cr_f18_cash_runway_burn_cashdd504_63d_slope_v060_signal,
    f18cr_f18_cash_runway_burn_cashrecov_63d_slope_v061_signal,
    f18cr_f18_cash_runway_burn_runwaymeddev_21d_slope_v062_signal,
    f18cr_f18_cash_runway_burn_covdev_21d_slope_v063_signal,
    f18cr_f18_cash_runway_burn_ncfoyoy_63d_slope_v064_signal,
    f18cr_f18_cash_runway_burn_capexcut_21d_slope_v065_signal,
    f18cr_f18_cash_runway_burn_finrank_63d_slope_v066_signal,
    f18cr_f18_cash_runway_burn_finmom_21d_slope_v067_signal,
    f18cr_f18_cash_runway_burn_burnvsfin_63d_slope_v068_signal,
    f18cr_f18_cash_runway_burn_capexvsburn_21d_slope_v069_signal,
    f18cr_f18_cash_runway_burn_runwaystruct_63d_slope_v070_signal,
    f18cr_f18_cash_runway_burn_covstruct_63d_slope_v071_signal,
    f18cr_f18_cash_runway_burn_allinrunwayz_21d_slope_v072_signal,
    f18cr_f18_cash_runway_burn_burnmixz_21d_slope_v073_signal,
    f18cr_f18_cash_runway_burn_worstcase_21d_slope_v074_signal,
    f18cr_f18_cash_runway_burn_yearstozero_63d_slope_v075_signal,
    f18cr_f18_cash_runway_burn_runwayopex_126d_slope_v076_signal,
    f18cr_f18_cash_runway_burn_depletion_126d_slope_v077_signal,
    f18cr_f18_cash_runway_burn_coverage_126d_slope_v078_signal,
    f18cr_f18_cash_runway_burn_cash_126d_slope_v079_signal,
    f18cr_f18_cash_runway_burn_runwaycapex_126d_slope_v080_signal,
    f18cr_f18_cash_runway_burn_covsm_21d_slope_v081_signal,
    f18cr_f18_cash_runway_burn_deplsm_21d_slope_v082_signal,
    f18cr_f18_cash_runway_burn_burnsurprise_21d_slope_v083_signal,
    f18cr_f18_cash_runway_burn_fcfmargindev_21d_slope_v084_signal,
    f18cr_f18_cash_runway_burn_capexterm_63d_slope_v085_signal,
    f18cr_f18_cash_runway_burn_finterm_21d_slope_v086_signal,
    f18cr_f18_cash_runway_burn_maxdepl_63d_slope_v087_signal,
    f18cr_f18_cash_runway_burn_minrunway_63d_slope_v088_signal,
    f18cr_f18_cash_runway_burn_runwaydd_21d_slope_v089_signal,
    f18cr_f18_cash_runway_burn_capexrunwaydd_21d_slope_v090_signal,
    f18cr_f18_cash_runway_burn_capexdrain_63d_slope_v091_signal,
    f18cr_f18_cash_runway_burn_ncfoyieldz_21d_slope_v092_signal,
    f18cr_f18_cash_runway_burn_allinburntanh_21d_slope_v093_signal,
    f18cr_f18_cash_runway_burn_deplsignroot_21d_slope_v094_signal,
    f18cr_f18_cash_runway_burn_covgaptanh_21d_slope_v095_signal,
    f18cr_f18_cash_runway_burn_burnXlowcash_21d_slope_v096_signal,
    f18cr_f18_cash_runway_burn_finXburn_21d_slope_v097_signal,
    f18cr_f18_cash_runway_burn_selffundgap_21d_slope_v098_signal,
    f18cr_f18_cash_runway_burn_finrunway_63d_slope_v099_signal,
    f18cr_f18_cash_runway_burn_runwayperbv_63d_slope_v100_signal,
    f18cr_f18_cash_runway_burn_monthsema_21d_slope_v101_signal,
    f18cr_f18_cash_runway_burn_opexturnz_21d_slope_v102_signal,
    f18cr_f18_cash_runway_burn_capexburnz_63d_slope_v103_signal,
    f18cr_f18_cash_runway_burn_cashtrend_21d_slope_v104_signal,
    f18cr_f18_cash_runway_burn_covgapchg_21d_slope_v105_signal,
    f18cr_f18_cash_runway_burn_totalburn_21d_slope_v106_signal,
    f18cr_f18_cash_runway_burn_capexopexz_21d_slope_v107_signal,
    f18cr_f18_cash_runway_burn_finkeepup_63d_slope_v108_signal,
    f18cr_f18_cash_runway_burn_ncfocapexsm_63d_slope_v109_signal,
    f18cr_f18_cash_runway_burn_cashrngpos_21d_slope_v110_signal,
    f18cr_f18_cash_runway_burn_allinrunwaytrend_21d_slope_v111_signal,
    f18cr_f18_cash_runway_burn_survcomposite_21d_slope_v112_signal,
    f18cr_f18_cash_runway_burn_zombie_21d_slope_v113_signal,
    f18cr_f18_cash_runway_burn_selffundtime_63d_slope_v114_signal,
    f18cr_f18_cash_runway_burn_findeptime_63d_slope_v115_signal,
    f18cr_f18_cash_runway_burn_crittime_63d_slope_v116_signal,
    f18cr_f18_cash_runway_burn_negncfotime_63d_slope_v117_signal,
    f18cr_f18_cash_runway_burn_burntime_63d_slope_v118_signal,
    f18cr_f18_cash_runway_burn_runwayopex_42d_slope_v119_signal,
    f18cr_f18_cash_runway_burn_coverage_42d_slope_v120_signal,
    f18cr_f18_cash_runway_burn_depletion_42d_slope_v121_signal,
    f18cr_f18_cash_runway_burn_cash_42d_slope_v122_signal,
    f18cr_f18_cash_runway_burn_capexdepl_63d_slope_v123_signal,
    f18cr_f18_cash_runway_burn_ncfoopex_42d_slope_v124_signal,
    f18cr_f18_cash_runway_burn_capexcash_42d_slope_v125_signal,
    f18cr_f18_cash_runway_burn_finopex_42d_slope_v126_signal,
    f18cr_f18_cash_runway_burn_burnfrac_63d_slope_v127_signal,
    f18cr_f18_cash_runway_burn_fcfmargin_63d_slope_v128_signal,
    f18cr_f18_cash_runway_burn_runwaysm126_63d_slope_v129_signal,
    f18cr_f18_cash_runway_burn_capexrunwaysm_63d_slope_v130_signal,
    f18cr_f18_cash_runway_burn_burnlevel_63d_slope_v131_signal,
    f18cr_f18_cash_runway_burn_cashtrend21_63d_slope_v132_signal,
    f18cr_f18_cash_runway_burn_ncfoyieldrank_63d_slope_v133_signal,
    f18cr_f18_cash_runway_burn_covrank_63d_slope_v134_signal,
    f18cr_f18_cash_runway_burn_capexdeplrank_63d_slope_v135_signal,
    f18cr_f18_cash_runway_burn_finsharerank_63d_slope_v136_signal,
    f18cr_f18_cash_runway_burn_deplstruct_63d_slope_v137_signal,
    f18cr_f18_cash_runway_burn_cashcv252_63d_slope_v138_signal,
    f18cr_f18_cash_runway_burn_ncfovol_63d_slope_v139_signal,
    f18cr_f18_cash_runway_burn_runwayvol_63d_slope_v140_signal,
    f18cr_f18_cash_runway_burn_treaspress_63d_slope_v141_signal,
    f18cr_f18_cash_runway_burn_burnvscash_21d_slope_v142_signal,
    f18cr_f18_cash_runway_burn_fcfyielddev_63d_slope_v143_signal,
    f18cr_f18_cash_runway_burn_capexopex_21d_slope_v144_signal,
    f18cr_f18_cash_runway_burn_fintopup_21d_slope_v145_signal,
    f18cr_f18_cash_runway_burn_allinrunway_63d_slope_v146_signal,
    f18cr_f18_cash_runway_burn_covgaproot_63d_slope_v147_signal,
    f18cr_f18_cash_runway_burn_capexcut_63d_slope_v148_signal,
    f18cr_f18_cash_runway_burn_ncfoz_63d_slope_v149_signal,
    f18cr_f18_cash_runway_burn_safetyfloor_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_CASH_RUNWAY_BURN_REGISTRY_SLOPE_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f18_cash_runway_burn_2nd_derivatives_001_150_claude: %d features pass" % n_features)
