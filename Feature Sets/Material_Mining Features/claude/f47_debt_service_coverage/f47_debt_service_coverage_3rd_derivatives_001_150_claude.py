import inspect
import numpy as np
import pandas as pd

# ============================================================
# f47_debt_service_coverage  -  3rd derivatives (JERK) 001-150
# Each feature = 2nd math derivative (acceleration / jerk) of a debt-service-coverage
# base signal. FUNDAMENTAL family: every feature consumes >= 1 fundamental column.
# Flow/service-burden axis via interest expense. Fully expanded inline defs only.
# ============================================================

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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



def f47ds_f47_debt_service_coverage_ebitcov_lvl_21d_jerk_v001_signal(ebit, intexp):
    c = ebit / intexp.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitdacov_vspeak_21d_jerk_v002_signal(ebitda, intexp):
    c = ebitda / intexp.replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ncfocov_vstrough_21d_jerk_v003_signal(ncfo, intexp):
    c = ncfo / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fcfcov_lvl_21d_jerk_v004_signal(fcf, intexp):
    c = fcf / intexp.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebt_vspeak_21d_jerk_v005_signal(intexp, debt):
    c = intexp / debt.replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebtnc_vstrough_21d_jerk_v006_signal(intexp, debtnc):
    c = intexp / debtnc.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_matwall_lvl_21d_jerk_v007_signal(debtc, cashneq, fcf):
    c = debtc / (cashneq + fcf).replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_runway_vspeak_21d_jerk_v008_signal(cashneq, intexp):
    c = cashneq / (intexp / 12.0).replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fixedchg_vstrough_21d_jerk_v009_signal(intexp, prefdivis, debtc):
    c = (intexp + prefdivis) / debtc.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dscr_lvl_21d_jerk_v010_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtfcf_vstrough_21d_jerk_v011_signal(fcf, intexp, debtc):
    c = (fcf - intexp) / debtc.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_netcap_vstrough_21d_jerk_v012_signal(ebit, intexp, prefdivis, debt):
    c = (ebit - intexp - prefdivis) / debt.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ltdebtcov_lvl_21d_jerk_v013_signal(ncfo, debtnc, intexp):
    c = (ncfo - intexp) / debtnc.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dacushion_vstrough_21d_jerk_v014_signal(ebitda, ebit, intexp):
    c = (ebitda - ebit) / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_accrualgap_vstrough_21d_jerk_v015_signal(ncfo, ebit, intexp):
    c = (ncfo - ebit) / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_capexgap_lvl_21d_jerk_v016_signal(ncfo, fcf, intexp):
    c = (ncfo - fcf) / intexp.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefebitda_vspeak_21d_jerk_v017_signal(prefdivis, ebitda):
    c = prefdivis / ebitda.replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtshare_vstrough_21d_jerk_v018_signal(debtc, debt):
    c = debtc / debt.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_intpref_lvl_21d_jerk_v019_signal(intexp, prefdivis):
    c = intexp / prefdivis.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_survmargin_vstrough_21d_jerk_v020_signal(ncfo, intexp, prefdivis, cashneq):
    c = (ncfo - intexp - prefdivis) / cashneq.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_burnfrac_vstrough_21d_jerk_v021_signal(intexp, cashneq, ebitda):
    c = intexp / (cashneq + ebitda.clip(lower=0)).replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefcov_lvl_21d_jerk_v022_signal(ncfo, prefdivis, intexp):
    c = (ncfo - intexp) / prefdivis.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_cashfixed_vspeak_21d_jerk_v023_signal(cashneq, intexp, prefdivis, debtc):
    c = cashneq / (intexp + prefdivis + debtc).replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitcov_vspeak_63d_jerk_v024_signal(ebit, intexp):
    c = ebit / intexp.replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitdacov_vstrough_63d_jerk_v025_signal(ebitda, intexp):
    c = ebitda / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ncfocov_lvl_63d_jerk_v026_signal(ncfo, intexp):
    c = ncfo / intexp.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fcfcov_vstrough_63d_jerk_v027_signal(fcf, intexp):
    c = fcf / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebt_vstrough_63d_jerk_v028_signal(intexp, debt):
    c = intexp / debt.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebtnc_lvl_63d_jerk_v029_signal(intexp, debtnc):
    c = intexp / debtnc.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_matwall_vspeak_63d_jerk_v030_signal(debtc, cashneq, fcf):
    c = debtc / (cashneq + fcf).replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_runway_vstrough_63d_jerk_v031_signal(cashneq, intexp):
    c = cashneq / (intexp / 12.0).replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fixedchg_lvl_63d_jerk_v032_signal(intexp, prefdivis, debtc):
    c = (intexp + prefdivis) / debtc.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dscr_vspeak_63d_jerk_v033_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtfcf_vstrough_63d_jerk_v034_signal(fcf, intexp, debtc):
    c = (fcf - intexp) / debtc.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_netcap_lvl_63d_jerk_v035_signal(ebit, intexp, prefdivis, debt):
    c = (ebit - intexp - prefdivis) / debt.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ltdebtcov_vstrough_63d_jerk_v036_signal(ncfo, debtnc, intexp):
    c = (ncfo - intexp) / debtnc.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dacushion_vstrough_63d_jerk_v037_signal(ebitda, ebit, intexp):
    c = (ebitda - ebit) / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_accrualgap_lvl_63d_jerk_v038_signal(ncfo, ebit, intexp):
    c = (ncfo - ebit) / intexp.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_capexgap_vstrough_63d_jerk_v039_signal(ncfo, fcf, intexp):
    c = (ncfo - fcf) / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefebitda_vstrough_63d_jerk_v040_signal(prefdivis, ebitda):
    c = prefdivis / ebitda.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtshare_lvl_63d_jerk_v041_signal(debtc, debt):
    c = debtc / debt.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_intpref_vspeak_63d_jerk_v042_signal(intexp, prefdivis):
    c = intexp / prefdivis.replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_survmargin_vstrough_63d_jerk_v043_signal(ncfo, intexp, prefdivis, cashneq):
    c = (ncfo - intexp - prefdivis) / cashneq.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_burnfrac_lvl_63d_jerk_v044_signal(intexp, cashneq, ebitda):
    c = intexp / (cashneq + ebitda.clip(lower=0)).replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefcov_vstrough_63d_jerk_v045_signal(ncfo, prefdivis, intexp):
    c = (ncfo - intexp) / prefdivis.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_cashfixed_vstrough_63d_jerk_v046_signal(cashneq, intexp, prefdivis, debtc):
    c = cashneq / (intexp + prefdivis + debtc).replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitcov_vstrough_126d_jerk_v047_signal(ebit, intexp):
    c = ebit / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitdacov_lvl_126d_jerk_v048_signal(ebitda, intexp):
    c = ebitda / intexp.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ncfocov_vstrough_126d_jerk_v049_signal(ncfo, intexp):
    c = ncfo / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fcfcov_vstrough_126d_jerk_v050_signal(fcf, intexp):
    c = fcf / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebt_lvl_126d_jerk_v051_signal(intexp, debt):
    c = intexp / debt.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebtnc_vspeak_126d_jerk_v052_signal(intexp, debtnc):
    c = intexp / debtnc.replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_matwall_vstrough_126d_jerk_v053_signal(debtc, cashneq, fcf):
    c = debtc / (cashneq + fcf).replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_runway_lvl_126d_jerk_v054_signal(cashneq, intexp):
    c = cashneq / (intexp / 12.0).replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fixedchg_vspeak_126d_jerk_v055_signal(intexp, prefdivis, debtc):
    c = (intexp + prefdivis) / debtc.replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dscr_vstrough_126d_jerk_v056_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtfcf_lvl_126d_jerk_v057_signal(fcf, intexp, debtc):
    c = (fcf - intexp) / debtc.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_netcap_vstrough_126d_jerk_v058_signal(ebit, intexp, prefdivis, debt):
    c = (ebit - intexp - prefdivis) / debt.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ltdebtcov_vstrough_126d_jerk_v059_signal(ncfo, debtnc, intexp):
    c = (ncfo - intexp) / debtnc.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dacushion_lvl_126d_jerk_v060_signal(ebitda, ebit, intexp):
    c = (ebitda - ebit) / intexp.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_accrualgap_vstrough_126d_jerk_v061_signal(ncfo, ebit, intexp):
    c = (ncfo - ebit) / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_capexgap_vstrough_126d_jerk_v062_signal(ncfo, fcf, intexp):
    c = (ncfo - fcf) / intexp.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefebitda_lvl_126d_jerk_v063_signal(prefdivis, ebitda):
    c = prefdivis / ebitda.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtshare_vspeak_126d_jerk_v064_signal(debtc, debt):
    c = debtc / debt.replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_intpref_vstrough_126d_jerk_v065_signal(intexp, prefdivis):
    c = intexp / prefdivis.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_survmargin_lvl_126d_jerk_v066_signal(ncfo, intexp, prefdivis, cashneq):
    c = (ncfo - intexp - prefdivis) / cashneq.replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_burnfrac_vspeak_126d_jerk_v067_signal(intexp, cashneq, ebitda):
    c = intexp / (cashneq + ebitda.clip(lower=0)).replace(0, np.nan)
    base = c / _rmax(c, 252).replace(0, np.nan)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefcov_vstrough_126d_jerk_v068_signal(ncfo, prefdivis, intexp):
    c = (ncfo - intexp) / prefdivis.replace(0, np.nan)
    base = c - _rmin(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_cashfixed_lvl_126d_jerk_v069_signal(cashneq, intexp, prefdivis, debtc):
    c = cashneq / (intexp + prefdivis + debtc).replace(0, np.nan)
    base = _mean(c, 21)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitcov_z_21d_jerk_v070_signal(ebit, intexp):
    c = ebit / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitdacov_z_21d_jerk_v071_signal(ebitda, intexp):
    c = ebitda / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ncfocov_z_21d_jerk_v072_signal(ncfo, intexp):
    c = ncfo / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fcfcov_z_21d_jerk_v073_signal(fcf, intexp):
    c = fcf / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebt_z_21d_jerk_v074_signal(intexp, debt):
    c = intexp / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebtnc_z_21d_jerk_v075_signal(intexp, debtnc):
    c = intexp / debtnc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_matwall_z_21d_jerk_v076_signal(debtc, cashneq, fcf):
    c = debtc / (cashneq + fcf).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_runway_z_21d_jerk_v077_signal(cashneq, intexp):
    c = cashneq / (intexp / 12.0).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fixedchg_z_21d_jerk_v078_signal(intexp, prefdivis, debtc):
    c = (intexp + prefdivis) / debtc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dscr_z_21d_jerk_v079_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtfcf_z_21d_jerk_v080_signal(fcf, intexp, debtc):
    c = (fcf - intexp) / debtc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_netcap_z_21d_jerk_v081_signal(ebit, intexp, prefdivis, debt):
    c = (ebit - intexp - prefdivis) / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ltdebtcov_z_21d_jerk_v082_signal(ncfo, debtnc, intexp):
    c = (ncfo - intexp) / debtnc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dacushion_z_21d_jerk_v083_signal(ebitda, ebit, intexp):
    c = (ebitda - ebit) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_accrualgap_z_21d_jerk_v084_signal(ncfo, ebit, intexp):
    c = (ncfo - ebit) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_capexgap_z_21d_jerk_v085_signal(ncfo, fcf, intexp):
    c = (ncfo - fcf) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefebitda_z_21d_jerk_v086_signal(prefdivis, ebitda):
    c = prefdivis / ebitda.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtshare_z_21d_jerk_v087_signal(debtc, debt):
    c = debtc / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_intpref_z_21d_jerk_v088_signal(intexp, prefdivis):
    c = intexp / prefdivis.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_survmargin_z_21d_jerk_v089_signal(ncfo, intexp, prefdivis, cashneq):
    c = (ncfo - intexp - prefdivis) / cashneq.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_burnfrac_z_21d_jerk_v090_signal(intexp, cashneq, ebitda):
    c = intexp / (cashneq + ebitda.clip(lower=0)).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefcov_z_21d_jerk_v091_signal(ncfo, prefdivis, intexp):
    c = (ncfo - intexp) / prefdivis.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_cashfixed_z_21d_jerk_v092_signal(cashneq, intexp, prefdivis, debtc):
    c = cashneq / (intexp + prefdivis + debtc).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(21)) / 21.0
    d = (d1 - d1.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitcov_z_63d_jerk_v093_signal(ebit, intexp):
    c = ebit / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitdacov_z_63d_jerk_v094_signal(ebitda, intexp):
    c = ebitda / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ncfocov_z_63d_jerk_v095_signal(ncfo, intexp):
    c = ncfo / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fcfcov_z_63d_jerk_v096_signal(fcf, intexp):
    c = fcf / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebt_z_63d_jerk_v097_signal(intexp, debt):
    c = intexp / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebtnc_z_63d_jerk_v098_signal(intexp, debtnc):
    c = intexp / debtnc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_matwall_z_63d_jerk_v099_signal(debtc, cashneq, fcf):
    c = debtc / (cashneq + fcf).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_runway_z_63d_jerk_v100_signal(cashneq, intexp):
    c = cashneq / (intexp / 12.0).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fixedchg_z_63d_jerk_v101_signal(intexp, prefdivis, debtc):
    c = (intexp + prefdivis) / debtc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dscr_z_63d_jerk_v102_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtfcf_z_63d_jerk_v103_signal(fcf, intexp, debtc):
    c = (fcf - intexp) / debtc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_netcap_z_63d_jerk_v104_signal(ebit, intexp, prefdivis, debt):
    c = (ebit - intexp - prefdivis) / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ltdebtcov_z_63d_jerk_v105_signal(ncfo, debtnc, intexp):
    c = (ncfo - intexp) / debtnc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dacushion_z_63d_jerk_v106_signal(ebitda, ebit, intexp):
    c = (ebitda - ebit) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_accrualgap_z_63d_jerk_v107_signal(ncfo, ebit, intexp):
    c = (ncfo - ebit) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_capexgap_z_63d_jerk_v108_signal(ncfo, fcf, intexp):
    c = (ncfo - fcf) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefebitda_z_63d_jerk_v109_signal(prefdivis, ebitda):
    c = prefdivis / ebitda.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtshare_z_63d_jerk_v110_signal(debtc, debt):
    c = debtc / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_intpref_z_63d_jerk_v111_signal(intexp, prefdivis):
    c = intexp / prefdivis.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_survmargin_z_63d_jerk_v112_signal(ncfo, intexp, prefdivis, cashneq):
    c = (ncfo - intexp - prefdivis) / cashneq.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_burnfrac_z_63d_jerk_v113_signal(intexp, cashneq, ebitda):
    c = intexp / (cashneq + ebitda.clip(lower=0)).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefcov_z_63d_jerk_v114_signal(ncfo, prefdivis, intexp):
    c = (ncfo - intexp) / prefdivis.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_cashfixed_z_63d_jerk_v115_signal(cashneq, intexp, prefdivis, debtc):
    c = cashneq / (intexp + prefdivis + debtc).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitcov_z_126d_jerk_v116_signal(ebit, intexp):
    c = ebit / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitdacov_z_126d_jerk_v117_signal(ebitda, intexp):
    c = ebitda / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ncfocov_z_126d_jerk_v118_signal(ncfo, intexp):
    c = ncfo / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fcfcov_z_126d_jerk_v119_signal(fcf, intexp):
    c = fcf / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebt_z_126d_jerk_v120_signal(intexp, debt):
    c = intexp / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebtnc_z_126d_jerk_v121_signal(intexp, debtnc):
    c = intexp / debtnc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_matwall_z_126d_jerk_v122_signal(debtc, cashneq, fcf):
    c = debtc / (cashneq + fcf).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_runway_z_126d_jerk_v123_signal(cashneq, intexp):
    c = cashneq / (intexp / 12.0).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fixedchg_z_126d_jerk_v124_signal(intexp, prefdivis, debtc):
    c = (intexp + prefdivis) / debtc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dscr_z_126d_jerk_v125_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtfcf_z_126d_jerk_v126_signal(fcf, intexp, debtc):
    c = (fcf - intexp) / debtc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_netcap_z_126d_jerk_v127_signal(ebit, intexp, prefdivis, debt):
    c = (ebit - intexp - prefdivis) / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ltdebtcov_z_126d_jerk_v128_signal(ncfo, debtnc, intexp):
    c = (ncfo - intexp) / debtnc.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dacushion_z_126d_jerk_v129_signal(ebitda, ebit, intexp):
    c = (ebitda - ebit) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_accrualgap_z_126d_jerk_v130_signal(ncfo, ebit, intexp):
    c = (ncfo - ebit) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_capexgap_z_126d_jerk_v131_signal(ncfo, fcf, intexp):
    c = (ncfo - fcf) / intexp.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefebitda_z_126d_jerk_v132_signal(prefdivis, ebitda):
    c = prefdivis / ebitda.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtshare_z_126d_jerk_v133_signal(debtc, debt):
    c = debtc / debt.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_intpref_z_126d_jerk_v134_signal(intexp, prefdivis):
    c = intexp / prefdivis.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_survmargin_z_126d_jerk_v135_signal(ncfo, intexp, prefdivis, cashneq):
    c = (ncfo - intexp - prefdivis) / cashneq.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_burnfrac_z_126d_jerk_v136_signal(intexp, cashneq, ebitda):
    c = intexp / (cashneq + ebitda.clip(lower=0)).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_prefcov_z_126d_jerk_v137_signal(ncfo, prefdivis, intexp):
    c = (ncfo - intexp) / prefdivis.replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_cashfixed_z_126d_jerk_v138_signal(cashneq, intexp, prefdivis, debtc):
    c = cashneq / (intexp + prefdivis + debtc).replace(0, np.nan)
    base = _z(c, 252)
    d1 = (base - base.shift(126)) / 126.0
    d = (d1 - d1.shift(126)) / 126.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitcov_cv_63d_jerk_v139_signal(ebit, intexp):
    c = ebit / intexp.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ebitdacov_cv_63d_jerk_v140_signal(ebitda, intexp):
    c = ebitda / intexp.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_ncfocov_cv_63d_jerk_v141_signal(ncfo, intexp):
    c = ncfo / intexp.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fcfcov_cv_63d_jerk_v142_signal(fcf, intexp):
    c = fcf / intexp.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebt_cv_63d_jerk_v143_signal(intexp, debt):
    c = intexp / debt.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_costdebtnc_cv_63d_jerk_v144_signal(intexp, debtnc):
    c = intexp / debtnc.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_matwall_cv_63d_jerk_v145_signal(debtc, cashneq, fcf):
    c = debtc / (cashneq + fcf).replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_runway_cv_63d_jerk_v146_signal(cashneq, intexp):
    c = cashneq / (intexp / 12.0).replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_fixedchg_cv_63d_jerk_v147_signal(intexp, prefdivis, debtc):
    c = (intexp + prefdivis) / debtc.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_dscr_cv_63d_jerk_v148_signal(ncfo, intexp, debtc):
    c = ncfo / (intexp + debtc).replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_curdebtfcf_cv_63d_jerk_v149_signal(fcf, intexp, debtc):
    c = (fcf - intexp) / debtc.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f47ds_f47_debt_service_coverage_netcap_cv_63d_jerk_v150_signal(ebit, intexp, prefdivis, debt):
    c = (ebit - intexp - prefdivis) / debt.replace(0, np.nan)
    base = _std(c, 126) / _mean(c, 126).abs().replace(0, np.nan)
    d1 = (base - base.shift(63)) / 63.0
    d = (d1 - d1.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47ds_f47_debt_service_coverage_ebitcov_lvl_21d_jerk_v001_signal,
    f47ds_f47_debt_service_coverage_ebitdacov_vspeak_21d_jerk_v002_signal,
    f47ds_f47_debt_service_coverage_ncfocov_vstrough_21d_jerk_v003_signal,
    f47ds_f47_debt_service_coverage_fcfcov_lvl_21d_jerk_v004_signal,
    f47ds_f47_debt_service_coverage_costdebt_vspeak_21d_jerk_v005_signal,
    f47ds_f47_debt_service_coverage_costdebtnc_vstrough_21d_jerk_v006_signal,
    f47ds_f47_debt_service_coverage_matwall_lvl_21d_jerk_v007_signal,
    f47ds_f47_debt_service_coverage_runway_vspeak_21d_jerk_v008_signal,
    f47ds_f47_debt_service_coverage_fixedchg_vstrough_21d_jerk_v009_signal,
    f47ds_f47_debt_service_coverage_dscr_lvl_21d_jerk_v010_signal,
    f47ds_f47_debt_service_coverage_curdebtfcf_vstrough_21d_jerk_v011_signal,
    f47ds_f47_debt_service_coverage_netcap_vstrough_21d_jerk_v012_signal,
    f47ds_f47_debt_service_coverage_ltdebtcov_lvl_21d_jerk_v013_signal,
    f47ds_f47_debt_service_coverage_dacushion_vstrough_21d_jerk_v014_signal,
    f47ds_f47_debt_service_coverage_accrualgap_vstrough_21d_jerk_v015_signal,
    f47ds_f47_debt_service_coverage_capexgap_lvl_21d_jerk_v016_signal,
    f47ds_f47_debt_service_coverage_prefebitda_vspeak_21d_jerk_v017_signal,
    f47ds_f47_debt_service_coverage_curdebtshare_vstrough_21d_jerk_v018_signal,
    f47ds_f47_debt_service_coverage_intpref_lvl_21d_jerk_v019_signal,
    f47ds_f47_debt_service_coverage_survmargin_vstrough_21d_jerk_v020_signal,
    f47ds_f47_debt_service_coverage_burnfrac_vstrough_21d_jerk_v021_signal,
    f47ds_f47_debt_service_coverage_prefcov_lvl_21d_jerk_v022_signal,
    f47ds_f47_debt_service_coverage_cashfixed_vspeak_21d_jerk_v023_signal,
    f47ds_f47_debt_service_coverage_ebitcov_vspeak_63d_jerk_v024_signal,
    f47ds_f47_debt_service_coverage_ebitdacov_vstrough_63d_jerk_v025_signal,
    f47ds_f47_debt_service_coverage_ncfocov_lvl_63d_jerk_v026_signal,
    f47ds_f47_debt_service_coverage_fcfcov_vstrough_63d_jerk_v027_signal,
    f47ds_f47_debt_service_coverage_costdebt_vstrough_63d_jerk_v028_signal,
    f47ds_f47_debt_service_coverage_costdebtnc_lvl_63d_jerk_v029_signal,
    f47ds_f47_debt_service_coverage_matwall_vspeak_63d_jerk_v030_signal,
    f47ds_f47_debt_service_coverage_runway_vstrough_63d_jerk_v031_signal,
    f47ds_f47_debt_service_coverage_fixedchg_lvl_63d_jerk_v032_signal,
    f47ds_f47_debt_service_coverage_dscr_vspeak_63d_jerk_v033_signal,
    f47ds_f47_debt_service_coverage_curdebtfcf_vstrough_63d_jerk_v034_signal,
    f47ds_f47_debt_service_coverage_netcap_lvl_63d_jerk_v035_signal,
    f47ds_f47_debt_service_coverage_ltdebtcov_vstrough_63d_jerk_v036_signal,
    f47ds_f47_debt_service_coverage_dacushion_vstrough_63d_jerk_v037_signal,
    f47ds_f47_debt_service_coverage_accrualgap_lvl_63d_jerk_v038_signal,
    f47ds_f47_debt_service_coverage_capexgap_vstrough_63d_jerk_v039_signal,
    f47ds_f47_debt_service_coverage_prefebitda_vstrough_63d_jerk_v040_signal,
    f47ds_f47_debt_service_coverage_curdebtshare_lvl_63d_jerk_v041_signal,
    f47ds_f47_debt_service_coverage_intpref_vspeak_63d_jerk_v042_signal,
    f47ds_f47_debt_service_coverage_survmargin_vstrough_63d_jerk_v043_signal,
    f47ds_f47_debt_service_coverage_burnfrac_lvl_63d_jerk_v044_signal,
    f47ds_f47_debt_service_coverage_prefcov_vstrough_63d_jerk_v045_signal,
    f47ds_f47_debt_service_coverage_cashfixed_vstrough_63d_jerk_v046_signal,
    f47ds_f47_debt_service_coverage_ebitcov_vstrough_126d_jerk_v047_signal,
    f47ds_f47_debt_service_coverage_ebitdacov_lvl_126d_jerk_v048_signal,
    f47ds_f47_debt_service_coverage_ncfocov_vstrough_126d_jerk_v049_signal,
    f47ds_f47_debt_service_coverage_fcfcov_vstrough_126d_jerk_v050_signal,
    f47ds_f47_debt_service_coverage_costdebt_lvl_126d_jerk_v051_signal,
    f47ds_f47_debt_service_coverage_costdebtnc_vspeak_126d_jerk_v052_signal,
    f47ds_f47_debt_service_coverage_matwall_vstrough_126d_jerk_v053_signal,
    f47ds_f47_debt_service_coverage_runway_lvl_126d_jerk_v054_signal,
    f47ds_f47_debt_service_coverage_fixedchg_vspeak_126d_jerk_v055_signal,
    f47ds_f47_debt_service_coverage_dscr_vstrough_126d_jerk_v056_signal,
    f47ds_f47_debt_service_coverage_curdebtfcf_lvl_126d_jerk_v057_signal,
    f47ds_f47_debt_service_coverage_netcap_vstrough_126d_jerk_v058_signal,
    f47ds_f47_debt_service_coverage_ltdebtcov_vstrough_126d_jerk_v059_signal,
    f47ds_f47_debt_service_coverage_dacushion_lvl_126d_jerk_v060_signal,
    f47ds_f47_debt_service_coverage_accrualgap_vstrough_126d_jerk_v061_signal,
    f47ds_f47_debt_service_coverage_capexgap_vstrough_126d_jerk_v062_signal,
    f47ds_f47_debt_service_coverage_prefebitda_lvl_126d_jerk_v063_signal,
    f47ds_f47_debt_service_coverage_curdebtshare_vspeak_126d_jerk_v064_signal,
    f47ds_f47_debt_service_coverage_intpref_vstrough_126d_jerk_v065_signal,
    f47ds_f47_debt_service_coverage_survmargin_lvl_126d_jerk_v066_signal,
    f47ds_f47_debt_service_coverage_burnfrac_vspeak_126d_jerk_v067_signal,
    f47ds_f47_debt_service_coverage_prefcov_vstrough_126d_jerk_v068_signal,
    f47ds_f47_debt_service_coverage_cashfixed_lvl_126d_jerk_v069_signal,
    f47ds_f47_debt_service_coverage_ebitcov_z_21d_jerk_v070_signal,
    f47ds_f47_debt_service_coverage_ebitdacov_z_21d_jerk_v071_signal,
    f47ds_f47_debt_service_coverage_ncfocov_z_21d_jerk_v072_signal,
    f47ds_f47_debt_service_coverage_fcfcov_z_21d_jerk_v073_signal,
    f47ds_f47_debt_service_coverage_costdebt_z_21d_jerk_v074_signal,
    f47ds_f47_debt_service_coverage_costdebtnc_z_21d_jerk_v075_signal,
    f47ds_f47_debt_service_coverage_matwall_z_21d_jerk_v076_signal,
    f47ds_f47_debt_service_coverage_runway_z_21d_jerk_v077_signal,
    f47ds_f47_debt_service_coverage_fixedchg_z_21d_jerk_v078_signal,
    f47ds_f47_debt_service_coverage_dscr_z_21d_jerk_v079_signal,
    f47ds_f47_debt_service_coverage_curdebtfcf_z_21d_jerk_v080_signal,
    f47ds_f47_debt_service_coverage_netcap_z_21d_jerk_v081_signal,
    f47ds_f47_debt_service_coverage_ltdebtcov_z_21d_jerk_v082_signal,
    f47ds_f47_debt_service_coverage_dacushion_z_21d_jerk_v083_signal,
    f47ds_f47_debt_service_coverage_accrualgap_z_21d_jerk_v084_signal,
    f47ds_f47_debt_service_coverage_capexgap_z_21d_jerk_v085_signal,
    f47ds_f47_debt_service_coverage_prefebitda_z_21d_jerk_v086_signal,
    f47ds_f47_debt_service_coverage_curdebtshare_z_21d_jerk_v087_signal,
    f47ds_f47_debt_service_coverage_intpref_z_21d_jerk_v088_signal,
    f47ds_f47_debt_service_coverage_survmargin_z_21d_jerk_v089_signal,
    f47ds_f47_debt_service_coverage_burnfrac_z_21d_jerk_v090_signal,
    f47ds_f47_debt_service_coverage_prefcov_z_21d_jerk_v091_signal,
    f47ds_f47_debt_service_coverage_cashfixed_z_21d_jerk_v092_signal,
    f47ds_f47_debt_service_coverage_ebitcov_z_63d_jerk_v093_signal,
    f47ds_f47_debt_service_coverage_ebitdacov_z_63d_jerk_v094_signal,
    f47ds_f47_debt_service_coverage_ncfocov_z_63d_jerk_v095_signal,
    f47ds_f47_debt_service_coverage_fcfcov_z_63d_jerk_v096_signal,
    f47ds_f47_debt_service_coverage_costdebt_z_63d_jerk_v097_signal,
    f47ds_f47_debt_service_coverage_costdebtnc_z_63d_jerk_v098_signal,
    f47ds_f47_debt_service_coverage_matwall_z_63d_jerk_v099_signal,
    f47ds_f47_debt_service_coverage_runway_z_63d_jerk_v100_signal,
    f47ds_f47_debt_service_coverage_fixedchg_z_63d_jerk_v101_signal,
    f47ds_f47_debt_service_coverage_dscr_z_63d_jerk_v102_signal,
    f47ds_f47_debt_service_coverage_curdebtfcf_z_63d_jerk_v103_signal,
    f47ds_f47_debt_service_coverage_netcap_z_63d_jerk_v104_signal,
    f47ds_f47_debt_service_coverage_ltdebtcov_z_63d_jerk_v105_signal,
    f47ds_f47_debt_service_coverage_dacushion_z_63d_jerk_v106_signal,
    f47ds_f47_debt_service_coverage_accrualgap_z_63d_jerk_v107_signal,
    f47ds_f47_debt_service_coverage_capexgap_z_63d_jerk_v108_signal,
    f47ds_f47_debt_service_coverage_prefebitda_z_63d_jerk_v109_signal,
    f47ds_f47_debt_service_coverage_curdebtshare_z_63d_jerk_v110_signal,
    f47ds_f47_debt_service_coverage_intpref_z_63d_jerk_v111_signal,
    f47ds_f47_debt_service_coverage_survmargin_z_63d_jerk_v112_signal,
    f47ds_f47_debt_service_coverage_burnfrac_z_63d_jerk_v113_signal,
    f47ds_f47_debt_service_coverage_prefcov_z_63d_jerk_v114_signal,
    f47ds_f47_debt_service_coverage_cashfixed_z_63d_jerk_v115_signal,
    f47ds_f47_debt_service_coverage_ebitcov_z_126d_jerk_v116_signal,
    f47ds_f47_debt_service_coverage_ebitdacov_z_126d_jerk_v117_signal,
    f47ds_f47_debt_service_coverage_ncfocov_z_126d_jerk_v118_signal,
    f47ds_f47_debt_service_coverage_fcfcov_z_126d_jerk_v119_signal,
    f47ds_f47_debt_service_coverage_costdebt_z_126d_jerk_v120_signal,
    f47ds_f47_debt_service_coverage_costdebtnc_z_126d_jerk_v121_signal,
    f47ds_f47_debt_service_coverage_matwall_z_126d_jerk_v122_signal,
    f47ds_f47_debt_service_coverage_runway_z_126d_jerk_v123_signal,
    f47ds_f47_debt_service_coverage_fixedchg_z_126d_jerk_v124_signal,
    f47ds_f47_debt_service_coverage_dscr_z_126d_jerk_v125_signal,
    f47ds_f47_debt_service_coverage_curdebtfcf_z_126d_jerk_v126_signal,
    f47ds_f47_debt_service_coverage_netcap_z_126d_jerk_v127_signal,
    f47ds_f47_debt_service_coverage_ltdebtcov_z_126d_jerk_v128_signal,
    f47ds_f47_debt_service_coverage_dacushion_z_126d_jerk_v129_signal,
    f47ds_f47_debt_service_coverage_accrualgap_z_126d_jerk_v130_signal,
    f47ds_f47_debt_service_coverage_capexgap_z_126d_jerk_v131_signal,
    f47ds_f47_debt_service_coverage_prefebitda_z_126d_jerk_v132_signal,
    f47ds_f47_debt_service_coverage_curdebtshare_z_126d_jerk_v133_signal,
    f47ds_f47_debt_service_coverage_intpref_z_126d_jerk_v134_signal,
    f47ds_f47_debt_service_coverage_survmargin_z_126d_jerk_v135_signal,
    f47ds_f47_debt_service_coverage_burnfrac_z_126d_jerk_v136_signal,
    f47ds_f47_debt_service_coverage_prefcov_z_126d_jerk_v137_signal,
    f47ds_f47_debt_service_coverage_cashfixed_z_126d_jerk_v138_signal,
    f47ds_f47_debt_service_coverage_ebitcov_cv_63d_jerk_v139_signal,
    f47ds_f47_debt_service_coverage_ebitdacov_cv_63d_jerk_v140_signal,
    f47ds_f47_debt_service_coverage_ncfocov_cv_63d_jerk_v141_signal,
    f47ds_f47_debt_service_coverage_fcfcov_cv_63d_jerk_v142_signal,
    f47ds_f47_debt_service_coverage_costdebt_cv_63d_jerk_v143_signal,
    f47ds_f47_debt_service_coverage_costdebtnc_cv_63d_jerk_v144_signal,
    f47ds_f47_debt_service_coverage_matwall_cv_63d_jerk_v145_signal,
    f47ds_f47_debt_service_coverage_runway_cv_63d_jerk_v146_signal,
    f47ds_f47_debt_service_coverage_fixedchg_cv_63d_jerk_v147_signal,
    f47ds_f47_debt_service_coverage_dscr_cv_63d_jerk_v148_signal,
    f47ds_f47_debt_service_coverage_curdebtfcf_cv_63d_jerk_v149_signal,
    f47ds_f47_debt_service_coverage_netcap_cv_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_DEBT_SERVICE_COVERAGE_REGISTRY_001_150 = REGISTRY


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

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            ix = ai.index.intersection(aj.index)
            if len(ix) < 30:
                continue
            cc = ai.loc[ix].corr(aj.loc[ix])
            if cc is None or np.isnan(cc):
                continue
            assert abs(cc) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, cc)

    print("OK f47_debt_service_coverage_3rd_derivatives_001_150_claude: %d features pass" % n_features)

