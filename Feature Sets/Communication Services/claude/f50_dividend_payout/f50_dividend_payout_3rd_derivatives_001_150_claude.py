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


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (dividend & payout sustainability) =====
def _f50_payer(dps):
    return (dps > 0).astype(float)


def _f50_growth(s, w):
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _f50_fcf_cover(fcf, ncfdiv):
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f50_pref_overhang(prefdivis, netinccmn):
    return prefdivis / netinccmn.replace(0, np.nan)


def _f50_payout_earn(ncfdiv, netinccmn):
    return ncfdiv.abs() / netinccmn.replace(0, np.nan)



# ============================================================

def f50dp_f50_dividend_payout_divyield_21d_jerk_v001_signal(divyield):
    u = divyield
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpslevel_63d_jerk_v002_signal(dps):
    u = np.log1p(dps.clip(lower=0))
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_payoutratio_126d_jerk_v003_signal(payoutratio):
    u = payoutratio
    base = _mean(u, 126)
    d1 = base - base.shift(126)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_fcfcover_252d_jerk_v004_signal(fcf, ncfdiv):
    u = _f50_fcf_cover(fcf, ncfdiv)
    base = _mean(u, 21)
    d1 = base - base.shift(252)
    d = d1 - d1.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v005_signal(prefdivis, netinccmn):
    u = _f50_pref_overhang(prefdivis, netinccmn)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_cashpayout_63d_jerk_v006_signal(ncfdiv, netinccmn):
    u = np.tanh(_f50_payout_earn(ncfdiv, netinccmn))
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpseps_126d_jerk_v007_signal(dps, eps):
    u = dps / eps.replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(126)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscover_252d_jerk_v008_signal(eps, dps):
    u = eps / dps.replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(252)
    d = d1 - d1.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divfcf_21d_jerk_v009_signal(ncfdiv, fcf):
    u = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldtrap_63d_jerk_v010_signal(divyield, payoutratio):
    u = divyield * payoutratio.clip(lower=0)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_earncover_126d_jerk_v011_signal(netinccmn, ncfdiv):
    u = netinccmn / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(126)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefdrag_252d_jerk_v012_signal(prefdivis, ncfdiv):
    u = prefdivis / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(252)
    d = d1 - d1.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divcashlvl_21d_jerk_v013_signal(ncfdiv):
    u = np.log1p(ncfdiv.abs())
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldquality_63d_jerk_v014_signal(divyield, payoutratio):
    u = divyield / payoutratio.clip(lower=0.01)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_totdistr_126d_jerk_v015_signal(ncfdiv, prefdivis, netinccmn):
    u = (ncfdiv.abs() + prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(126)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscushion_252d_jerk_v016_signal(eps, dps):
    u = (eps - dps) / eps.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(252)
    d = d1 - d1.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preffcf_21d_jerk_v017_signal(prefdivis, fcf):
    u = prefdivis / fcf.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_commonavail_63d_jerk_v018_signal(netinccmn, prefdivis):
    u = (netinccmn - prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_coversafety_126d_jerk_v019_signal(fcf, ncfdiv):
    u = np.tanh(_f50_fcf_cover(fcf, ncfdiv) - 1.0)
    base = _mean(u, 21)
    d1 = base - base.shift(126)
    d = d1 - d1.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preflevel_252d_jerk_v020_signal(prefdivis):
    u = np.log1p(prefdivis.clip(lower=0))
    base = _mean(u, 63)
    d1 = base - base.shift(252)
    d = d1 - d1.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divyield_21d_jerk_v021_signal(divyield):
    u = divyield
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpslevel_21d_jerk_v022_signal(dps):
    u = np.log1p(dps.clip(lower=0))
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_payoutratio_21d_jerk_v023_signal(payoutratio):
    u = payoutratio
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_fcfcover_21d_jerk_v024_signal(fcf, ncfdiv):
    u = _f50_fcf_cover(fcf, ncfdiv)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v025_signal(prefdivis, netinccmn):
    u = _f50_pref_overhang(prefdivis, netinccmn)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_cashpayout_21d_jerk_v026_signal(ncfdiv, netinccmn):
    u = np.tanh(_f50_payout_earn(ncfdiv, netinccmn))
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpseps_21d_jerk_v027_signal(dps, eps):
    u = dps / eps.replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscover_21d_jerk_v028_signal(eps, dps):
    u = eps / dps.replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divfcf_21d_jerk_v029_signal(ncfdiv, fcf):
    u = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldtrap_21d_jerk_v030_signal(divyield, payoutratio):
    u = divyield * payoutratio.clip(lower=0)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_earncover_21d_jerk_v031_signal(netinccmn, ncfdiv):
    u = netinccmn / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefdrag_21d_jerk_v032_signal(prefdivis, ncfdiv):
    u = prefdivis / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divcashlvl_21d_jerk_v033_signal(ncfdiv):
    u = np.log1p(ncfdiv.abs())
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldquality_21d_jerk_v034_signal(divyield, payoutratio):
    u = divyield / payoutratio.clip(lower=0.01)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_totdistr_21d_jerk_v035_signal(ncfdiv, prefdivis, netinccmn):
    u = (ncfdiv.abs() + prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscushion_21d_jerk_v036_signal(eps, dps):
    u = (eps - dps) / eps.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preffcf_21d_jerk_v037_signal(prefdivis, fcf):
    u = prefdivis / fcf.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_commonavail_21d_jerk_v038_signal(netinccmn, prefdivis):
    u = (netinccmn - prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_coversafety_21d_jerk_v039_signal(fcf, ncfdiv):
    u = np.tanh(_f50_fcf_cover(fcf, ncfdiv) - 1.0)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preflevel_21d_jerk_v040_signal(prefdivis):
    u = np.log1p(prefdivis.clip(lower=0))
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divyield_21d_jerk_v041_signal(divyield):
    u = divyield
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpslevel_21d_jerk_v042_signal(dps):
    u = np.log1p(dps.clip(lower=0))
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_payoutratio_21d_jerk_v043_signal(payoutratio):
    u = payoutratio
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_fcfcover_21d_jerk_v044_signal(fcf, ncfdiv):
    u = _f50_fcf_cover(fcf, ncfdiv)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v045_signal(prefdivis, netinccmn):
    u = _f50_pref_overhang(prefdivis, netinccmn)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_cashpayout_21d_jerk_v046_signal(ncfdiv, netinccmn):
    u = np.tanh(_f50_payout_earn(ncfdiv, netinccmn))
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpseps_21d_jerk_v047_signal(dps, eps):
    u = dps / eps.replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscover_21d_jerk_v048_signal(eps, dps):
    u = eps / dps.replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divfcf_21d_jerk_v049_signal(ncfdiv, fcf):
    u = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldtrap_21d_jerk_v050_signal(divyield, payoutratio):
    u = divyield * payoutratio.clip(lower=0)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_earncover_21d_jerk_v051_signal(netinccmn, ncfdiv):
    u = netinccmn / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefdrag_21d_jerk_v052_signal(prefdivis, ncfdiv):
    u = prefdivis / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divcashlvl_21d_jerk_v053_signal(ncfdiv):
    u = np.log1p(ncfdiv.abs())
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldquality_21d_jerk_v054_signal(divyield, payoutratio):
    u = divyield / payoutratio.clip(lower=0.01)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_totdistr_21d_jerk_v055_signal(ncfdiv, prefdivis, netinccmn):
    u = (ncfdiv.abs() + prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscushion_21d_jerk_v056_signal(eps, dps):
    u = (eps - dps) / eps.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preffcf_21d_jerk_v057_signal(prefdivis, fcf):
    u = prefdivis / fcf.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_commonavail_21d_jerk_v058_signal(netinccmn, prefdivis):
    u = (netinccmn - prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_coversafety_21d_jerk_v059_signal(fcf, ncfdiv):
    u = np.tanh(_f50_fcf_cover(fcf, ncfdiv) - 1.0)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preflevel_21d_jerk_v060_signal(prefdivis):
    u = np.log1p(prefdivis.clip(lower=0))
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divyield_21d_jerk_v061_signal(divyield):
    u = divyield
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpslevel_21d_jerk_v062_signal(dps):
    u = np.log1p(dps.clip(lower=0))
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_payoutratio_21d_jerk_v063_signal(payoutratio):
    u = payoutratio
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_fcfcover_21d_jerk_v064_signal(fcf, ncfdiv):
    u = _f50_fcf_cover(fcf, ncfdiv)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v065_signal(prefdivis, netinccmn):
    u = _f50_pref_overhang(prefdivis, netinccmn)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_cashpayout_21d_jerk_v066_signal(ncfdiv, netinccmn):
    u = np.tanh(_f50_payout_earn(ncfdiv, netinccmn))
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpseps_21d_jerk_v067_signal(dps, eps):
    u = dps / eps.replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscover_21d_jerk_v068_signal(eps, dps):
    u = eps / dps.replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divfcf_21d_jerk_v069_signal(ncfdiv, fcf):
    u = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldtrap_21d_jerk_v070_signal(divyield, payoutratio):
    u = divyield * payoutratio.clip(lower=0)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_earncover_21d_jerk_v071_signal(netinccmn, ncfdiv):
    u = netinccmn / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefdrag_21d_jerk_v072_signal(prefdivis, ncfdiv):
    u = prefdivis / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divcashlvl_21d_jerk_v073_signal(ncfdiv):
    u = np.log1p(ncfdiv.abs())
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldquality_21d_jerk_v074_signal(divyield, payoutratio):
    u = divyield / payoutratio.clip(lower=0.01)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_totdistr_21d_jerk_v075_signal(ncfdiv, prefdivis, netinccmn):
    u = (ncfdiv.abs() + prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscushion_21d_jerk_v076_signal(eps, dps):
    u = (eps - dps) / eps.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preffcf_21d_jerk_v077_signal(prefdivis, fcf):
    u = prefdivis / fcf.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_commonavail_21d_jerk_v078_signal(netinccmn, prefdivis):
    u = (netinccmn - prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_coversafety_21d_jerk_v079_signal(fcf, ncfdiv):
    u = np.tanh(_f50_fcf_cover(fcf, ncfdiv) - 1.0)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preflevel_21d_jerk_v080_signal(prefdivis):
    u = np.log1p(prefdivis.clip(lower=0))
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divyield_21d_jerk_v081_signal(divyield):
    u = divyield
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpslevel_21d_jerk_v082_signal(dps):
    u = np.log1p(dps.clip(lower=0))
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_payoutratio_21d_jerk_v083_signal(payoutratio):
    u = payoutratio
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_fcfcover_21d_jerk_v084_signal(fcf, ncfdiv):
    u = _f50_fcf_cover(fcf, ncfdiv)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v085_signal(prefdivis, netinccmn):
    u = _f50_pref_overhang(prefdivis, netinccmn)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_cashpayout_21d_jerk_v086_signal(ncfdiv, netinccmn):
    u = np.tanh(_f50_payout_earn(ncfdiv, netinccmn))
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpseps_21d_jerk_v087_signal(dps, eps):
    u = dps / eps.replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscover_21d_jerk_v088_signal(eps, dps):
    u = eps / dps.replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divfcf_21d_jerk_v089_signal(ncfdiv, fcf):
    u = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldtrap_21d_jerk_v090_signal(divyield, payoutratio):
    u = divyield * payoutratio.clip(lower=0)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_earncover_21d_jerk_v091_signal(netinccmn, ncfdiv):
    u = netinccmn / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefdrag_21d_jerk_v092_signal(prefdivis, ncfdiv):
    u = prefdivis / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divcashlvl_252d_jerk_v093_signal(ncfdiv):
    u = np.log1p(ncfdiv.abs())
    base = _mean(u, 21)
    d1 = base - base.shift(252)
    d = d1 - d1.shift(126)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldquality_21d_jerk_v094_signal(divyield, payoutratio):
    u = divyield / payoutratio.clip(lower=0.01)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_totdistr_21d_jerk_v095_signal(ncfdiv, prefdivis, netinccmn):
    u = (ncfdiv.abs() + prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscushion_21d_jerk_v096_signal(eps, dps):
    u = (eps - dps) / eps.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preffcf_21d_jerk_v097_signal(prefdivis, fcf):
    u = prefdivis / fcf.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_commonavail_21d_jerk_v098_signal(netinccmn, prefdivis):
    u = (netinccmn - prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_coversafety_21d_jerk_v099_signal(fcf, ncfdiv):
    u = np.tanh(_f50_fcf_cover(fcf, ncfdiv) - 1.0)
    base = _mean(u, 21)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preflevel_21d_jerk_v100_signal(prefdivis):
    u = np.log1p(prefdivis.clip(lower=0))
    base = _mean(u, 63)
    d1 = base - base.shift(21)
    d = d1 - d1.shift(10)
    result = _z(d, 126).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divyield_63d_jerk_v101_signal(divyield):
    u = divyield
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpslevel_63d_jerk_v102_signal(dps):
    u = np.log1p(dps.clip(lower=0))
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_payoutratio_63d_jerk_v103_signal(payoutratio):
    u = payoutratio
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_fcfcover_63d_jerk_v104_signal(fcf, ncfdiv):
    u = _f50_fcf_cover(fcf, ncfdiv)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefoverhang_63d_jerk_v105_signal(prefdivis, netinccmn):
    u = _f50_pref_overhang(prefdivis, netinccmn)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_cashpayout_63d_jerk_v106_signal(ncfdiv, netinccmn):
    u = np.tanh(_f50_payout_earn(ncfdiv, netinccmn))
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpseps_63d_jerk_v107_signal(dps, eps):
    u = dps / eps.replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscover_63d_jerk_v108_signal(eps, dps):
    u = eps / dps.replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divfcf_63d_jerk_v109_signal(ncfdiv, fcf):
    u = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldtrap_63d_jerk_v110_signal(divyield, payoutratio):
    u = divyield * payoutratio.clip(lower=0)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_earncover_252d_jerk_v111_signal(netinccmn, ncfdiv):
    u = netinccmn / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(252)
    d = d1 - d1.shift(126)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefdrag_63d_jerk_v112_signal(prefdivis, ncfdiv):
    u = prefdivis / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divcashlvl_63d_jerk_v113_signal(ncfdiv):
    u = np.log1p(ncfdiv.abs())
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldquality_63d_jerk_v114_signal(divyield, payoutratio):
    u = divyield / payoutratio.clip(lower=0.01)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_totdistr_63d_jerk_v115_signal(ncfdiv, prefdivis, netinccmn):
    u = (ncfdiv.abs() + prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscushion_63d_jerk_v116_signal(eps, dps):
    u = (eps - dps) / eps.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preffcf_63d_jerk_v117_signal(prefdivis, fcf):
    u = prefdivis / fcf.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_commonavail_63d_jerk_v118_signal(netinccmn, prefdivis):
    u = (netinccmn - prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_coversafety_63d_jerk_v119_signal(fcf, ncfdiv):
    u = np.tanh(_f50_fcf_cover(fcf, ncfdiv) - 1.0)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preflevel_63d_jerk_v120_signal(prefdivis):
    u = np.log1p(prefdivis.clip(lower=0))
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divyield_63d_jerk_v121_signal(divyield):
    u = divyield
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpslevel_63d_jerk_v122_signal(dps):
    u = np.log1p(dps.clip(lower=0))
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_payoutratio_63d_jerk_v123_signal(payoutratio):
    u = payoutratio
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_fcfcover_63d_jerk_v124_signal(fcf, ncfdiv):
    u = _f50_fcf_cover(fcf, ncfdiv)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefoverhang_63d_jerk_v125_signal(prefdivis, netinccmn):
    u = _f50_pref_overhang(prefdivis, netinccmn)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_cashpayout_63d_jerk_v126_signal(ncfdiv, netinccmn):
    u = np.tanh(_f50_payout_earn(ncfdiv, netinccmn))
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpseps_63d_jerk_v127_signal(dps, eps):
    u = dps / eps.replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscover_63d_jerk_v128_signal(eps, dps):
    u = eps / dps.replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divfcf_63d_jerk_v129_signal(ncfdiv, fcf):
    u = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldtrap_63d_jerk_v130_signal(divyield, payoutratio):
    u = divyield * payoutratio.clip(lower=0)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_earncover_63d_jerk_v131_signal(netinccmn, ncfdiv):
    u = netinccmn / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefdrag_63d_jerk_v132_signal(prefdivis, ncfdiv):
    u = prefdivis / ncfdiv.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divcashlvl_63d_jerk_v133_signal(ncfdiv):
    u = np.log1p(ncfdiv.abs())
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldquality_63d_jerk_v134_signal(divyield, payoutratio):
    u = divyield / payoutratio.clip(lower=0.01)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_totdistr_63d_jerk_v135_signal(ncfdiv, prefdivis, netinccmn):
    u = (ncfdiv.abs() + prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscushion_63d_jerk_v136_signal(eps, dps):
    u = (eps - dps) / eps.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preffcf_63d_jerk_v137_signal(prefdivis, fcf):
    u = prefdivis / fcf.abs().replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_commonavail_63d_jerk_v138_signal(netinccmn, prefdivis):
    u = (netinccmn - prefdivis) / netinccmn.abs().replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_coversafety_63d_jerk_v139_signal(fcf, ncfdiv):
    u = np.tanh(_f50_fcf_cover(fcf, ncfdiv) - 1.0)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 126).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_preflevel_63d_jerk_v140_signal(prefdivis):
    u = np.log1p(prefdivis.clip(lower=0))
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.tanh(d / (_std(d, 252).replace(0, np.nan)))
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divyield_63d_jerk_v141_signal(divyield):
    u = divyield
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpslevel_63d_jerk_v142_signal(dps):
    u = np.log1p(dps.clip(lower=0))
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_payoutratio_63d_jerk_v143_signal(payoutratio):
    u = payoutratio
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_fcfcover_63d_jerk_v144_signal(fcf, ncfdiv):
    u = _f50_fcf_cover(fcf, ncfdiv)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_prefoverhang_63d_jerk_v145_signal(prefdivis, netinccmn):
    u = _f50_pref_overhang(prefdivis, netinccmn)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_cashpayout_63d_jerk_v146_signal(ncfdiv, netinccmn):
    u = np.tanh(_f50_payout_earn(ncfdiv, netinccmn))
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_dpseps_63d_jerk_v147_signal(dps, eps):
    u = dps / eps.replace(0, np.nan)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_epscover_63d_jerk_v148_signal(eps, dps):
    u = eps / dps.replace(0, np.nan)
    base = _mean(u, 63)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_divfcf_63d_jerk_v149_signal(ncfdiv, fcf):
    u = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    base = _mean(u, 126)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 252).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f50dp_f50_dividend_payout_yieldtrap_63d_jerk_v150_signal(divyield, payoutratio):
    u = divyield * payoutratio.clip(lower=0)
    base = _mean(u, 21)
    d1 = base - base.shift(63)
    d = d1 - d1.shift(31)
    result = np.sign(d) * (d.abs() / _std(d, 126).replace(0, np.nan)) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50dp_f50_dividend_payout_divyield_21d_jerk_v001_signal,
    f50dp_f50_dividend_payout_dpslevel_63d_jerk_v002_signal,
    f50dp_f50_dividend_payout_payoutratio_126d_jerk_v003_signal,
    f50dp_f50_dividend_payout_fcfcover_252d_jerk_v004_signal,
    f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v005_signal,
    f50dp_f50_dividend_payout_cashpayout_63d_jerk_v006_signal,
    f50dp_f50_dividend_payout_dpseps_126d_jerk_v007_signal,
    f50dp_f50_dividend_payout_epscover_252d_jerk_v008_signal,
    f50dp_f50_dividend_payout_divfcf_21d_jerk_v009_signal,
    f50dp_f50_dividend_payout_yieldtrap_63d_jerk_v010_signal,
    f50dp_f50_dividend_payout_earncover_126d_jerk_v011_signal,
    f50dp_f50_dividend_payout_prefdrag_252d_jerk_v012_signal,
    f50dp_f50_dividend_payout_divcashlvl_21d_jerk_v013_signal,
    f50dp_f50_dividend_payout_yieldquality_63d_jerk_v014_signal,
    f50dp_f50_dividend_payout_totdistr_126d_jerk_v015_signal,
    f50dp_f50_dividend_payout_epscushion_252d_jerk_v016_signal,
    f50dp_f50_dividend_payout_preffcf_21d_jerk_v017_signal,
    f50dp_f50_dividend_payout_commonavail_63d_jerk_v018_signal,
    f50dp_f50_dividend_payout_coversafety_126d_jerk_v019_signal,
    f50dp_f50_dividend_payout_preflevel_252d_jerk_v020_signal,
    f50dp_f50_dividend_payout_divyield_21d_jerk_v021_signal,
    f50dp_f50_dividend_payout_dpslevel_21d_jerk_v022_signal,
    f50dp_f50_dividend_payout_payoutratio_21d_jerk_v023_signal,
    f50dp_f50_dividend_payout_fcfcover_21d_jerk_v024_signal,
    f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v025_signal,
    f50dp_f50_dividend_payout_cashpayout_21d_jerk_v026_signal,
    f50dp_f50_dividend_payout_dpseps_21d_jerk_v027_signal,
    f50dp_f50_dividend_payout_epscover_21d_jerk_v028_signal,
    f50dp_f50_dividend_payout_divfcf_21d_jerk_v029_signal,
    f50dp_f50_dividend_payout_yieldtrap_21d_jerk_v030_signal,
    f50dp_f50_dividend_payout_earncover_21d_jerk_v031_signal,
    f50dp_f50_dividend_payout_prefdrag_21d_jerk_v032_signal,
    f50dp_f50_dividend_payout_divcashlvl_21d_jerk_v033_signal,
    f50dp_f50_dividend_payout_yieldquality_21d_jerk_v034_signal,
    f50dp_f50_dividend_payout_totdistr_21d_jerk_v035_signal,
    f50dp_f50_dividend_payout_epscushion_21d_jerk_v036_signal,
    f50dp_f50_dividend_payout_preffcf_21d_jerk_v037_signal,
    f50dp_f50_dividend_payout_commonavail_21d_jerk_v038_signal,
    f50dp_f50_dividend_payout_coversafety_21d_jerk_v039_signal,
    f50dp_f50_dividend_payout_preflevel_21d_jerk_v040_signal,
    f50dp_f50_dividend_payout_divyield_21d_jerk_v041_signal,
    f50dp_f50_dividend_payout_dpslevel_21d_jerk_v042_signal,
    f50dp_f50_dividend_payout_payoutratio_21d_jerk_v043_signal,
    f50dp_f50_dividend_payout_fcfcover_21d_jerk_v044_signal,
    f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v045_signal,
    f50dp_f50_dividend_payout_cashpayout_21d_jerk_v046_signal,
    f50dp_f50_dividend_payout_dpseps_21d_jerk_v047_signal,
    f50dp_f50_dividend_payout_epscover_21d_jerk_v048_signal,
    f50dp_f50_dividend_payout_divfcf_21d_jerk_v049_signal,
    f50dp_f50_dividend_payout_yieldtrap_21d_jerk_v050_signal,
    f50dp_f50_dividend_payout_earncover_21d_jerk_v051_signal,
    f50dp_f50_dividend_payout_prefdrag_21d_jerk_v052_signal,
    f50dp_f50_dividend_payout_divcashlvl_21d_jerk_v053_signal,
    f50dp_f50_dividend_payout_yieldquality_21d_jerk_v054_signal,
    f50dp_f50_dividend_payout_totdistr_21d_jerk_v055_signal,
    f50dp_f50_dividend_payout_epscushion_21d_jerk_v056_signal,
    f50dp_f50_dividend_payout_preffcf_21d_jerk_v057_signal,
    f50dp_f50_dividend_payout_commonavail_21d_jerk_v058_signal,
    f50dp_f50_dividend_payout_coversafety_21d_jerk_v059_signal,
    f50dp_f50_dividend_payout_preflevel_21d_jerk_v060_signal,
    f50dp_f50_dividend_payout_divyield_21d_jerk_v061_signal,
    f50dp_f50_dividend_payout_dpslevel_21d_jerk_v062_signal,
    f50dp_f50_dividend_payout_payoutratio_21d_jerk_v063_signal,
    f50dp_f50_dividend_payout_fcfcover_21d_jerk_v064_signal,
    f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v065_signal,
    f50dp_f50_dividend_payout_cashpayout_21d_jerk_v066_signal,
    f50dp_f50_dividend_payout_dpseps_21d_jerk_v067_signal,
    f50dp_f50_dividend_payout_epscover_21d_jerk_v068_signal,
    f50dp_f50_dividend_payout_divfcf_21d_jerk_v069_signal,
    f50dp_f50_dividend_payout_yieldtrap_21d_jerk_v070_signal,
    f50dp_f50_dividend_payout_earncover_21d_jerk_v071_signal,
    f50dp_f50_dividend_payout_prefdrag_21d_jerk_v072_signal,
    f50dp_f50_dividend_payout_divcashlvl_21d_jerk_v073_signal,
    f50dp_f50_dividend_payout_yieldquality_21d_jerk_v074_signal,
    f50dp_f50_dividend_payout_totdistr_21d_jerk_v075_signal,
    f50dp_f50_dividend_payout_epscushion_21d_jerk_v076_signal,
    f50dp_f50_dividend_payout_preffcf_21d_jerk_v077_signal,
    f50dp_f50_dividend_payout_commonavail_21d_jerk_v078_signal,
    f50dp_f50_dividend_payout_coversafety_21d_jerk_v079_signal,
    f50dp_f50_dividend_payout_preflevel_21d_jerk_v080_signal,
    f50dp_f50_dividend_payout_divyield_21d_jerk_v081_signal,
    f50dp_f50_dividend_payout_dpslevel_21d_jerk_v082_signal,
    f50dp_f50_dividend_payout_payoutratio_21d_jerk_v083_signal,
    f50dp_f50_dividend_payout_fcfcover_21d_jerk_v084_signal,
    f50dp_f50_dividend_payout_prefoverhang_21d_jerk_v085_signal,
    f50dp_f50_dividend_payout_cashpayout_21d_jerk_v086_signal,
    f50dp_f50_dividend_payout_dpseps_21d_jerk_v087_signal,
    f50dp_f50_dividend_payout_epscover_21d_jerk_v088_signal,
    f50dp_f50_dividend_payout_divfcf_21d_jerk_v089_signal,
    f50dp_f50_dividend_payout_yieldtrap_21d_jerk_v090_signal,
    f50dp_f50_dividend_payout_earncover_21d_jerk_v091_signal,
    f50dp_f50_dividend_payout_prefdrag_21d_jerk_v092_signal,
    f50dp_f50_dividend_payout_divcashlvl_252d_jerk_v093_signal,
    f50dp_f50_dividend_payout_yieldquality_21d_jerk_v094_signal,
    f50dp_f50_dividend_payout_totdistr_21d_jerk_v095_signal,
    f50dp_f50_dividend_payout_epscushion_21d_jerk_v096_signal,
    f50dp_f50_dividend_payout_preffcf_21d_jerk_v097_signal,
    f50dp_f50_dividend_payout_commonavail_21d_jerk_v098_signal,
    f50dp_f50_dividend_payout_coversafety_21d_jerk_v099_signal,
    f50dp_f50_dividend_payout_preflevel_21d_jerk_v100_signal,
    f50dp_f50_dividend_payout_divyield_63d_jerk_v101_signal,
    f50dp_f50_dividend_payout_dpslevel_63d_jerk_v102_signal,
    f50dp_f50_dividend_payout_payoutratio_63d_jerk_v103_signal,
    f50dp_f50_dividend_payout_fcfcover_63d_jerk_v104_signal,
    f50dp_f50_dividend_payout_prefoverhang_63d_jerk_v105_signal,
    f50dp_f50_dividend_payout_cashpayout_63d_jerk_v106_signal,
    f50dp_f50_dividend_payout_dpseps_63d_jerk_v107_signal,
    f50dp_f50_dividend_payout_epscover_63d_jerk_v108_signal,
    f50dp_f50_dividend_payout_divfcf_63d_jerk_v109_signal,
    f50dp_f50_dividend_payout_yieldtrap_63d_jerk_v110_signal,
    f50dp_f50_dividend_payout_earncover_252d_jerk_v111_signal,
    f50dp_f50_dividend_payout_prefdrag_63d_jerk_v112_signal,
    f50dp_f50_dividend_payout_divcashlvl_63d_jerk_v113_signal,
    f50dp_f50_dividend_payout_yieldquality_63d_jerk_v114_signal,
    f50dp_f50_dividend_payout_totdistr_63d_jerk_v115_signal,
    f50dp_f50_dividend_payout_epscushion_63d_jerk_v116_signal,
    f50dp_f50_dividend_payout_preffcf_63d_jerk_v117_signal,
    f50dp_f50_dividend_payout_commonavail_63d_jerk_v118_signal,
    f50dp_f50_dividend_payout_coversafety_63d_jerk_v119_signal,
    f50dp_f50_dividend_payout_preflevel_63d_jerk_v120_signal,
    f50dp_f50_dividend_payout_divyield_63d_jerk_v121_signal,
    f50dp_f50_dividend_payout_dpslevel_63d_jerk_v122_signal,
    f50dp_f50_dividend_payout_payoutratio_63d_jerk_v123_signal,
    f50dp_f50_dividend_payout_fcfcover_63d_jerk_v124_signal,
    f50dp_f50_dividend_payout_prefoverhang_63d_jerk_v125_signal,
    f50dp_f50_dividend_payout_cashpayout_63d_jerk_v126_signal,
    f50dp_f50_dividend_payout_dpseps_63d_jerk_v127_signal,
    f50dp_f50_dividend_payout_epscover_63d_jerk_v128_signal,
    f50dp_f50_dividend_payout_divfcf_63d_jerk_v129_signal,
    f50dp_f50_dividend_payout_yieldtrap_63d_jerk_v130_signal,
    f50dp_f50_dividend_payout_earncover_63d_jerk_v131_signal,
    f50dp_f50_dividend_payout_prefdrag_63d_jerk_v132_signal,
    f50dp_f50_dividend_payout_divcashlvl_63d_jerk_v133_signal,
    f50dp_f50_dividend_payout_yieldquality_63d_jerk_v134_signal,
    f50dp_f50_dividend_payout_totdistr_63d_jerk_v135_signal,
    f50dp_f50_dividend_payout_epscushion_63d_jerk_v136_signal,
    f50dp_f50_dividend_payout_preffcf_63d_jerk_v137_signal,
    f50dp_f50_dividend_payout_commonavail_63d_jerk_v138_signal,
    f50dp_f50_dividend_payout_coversafety_63d_jerk_v139_signal,
    f50dp_f50_dividend_payout_preflevel_63d_jerk_v140_signal,
    f50dp_f50_dividend_payout_divyield_63d_jerk_v141_signal,
    f50dp_f50_dividend_payout_dpslevel_63d_jerk_v142_signal,
    f50dp_f50_dividend_payout_payoutratio_63d_jerk_v143_signal,
    f50dp_f50_dividend_payout_fcfcover_63d_jerk_v144_signal,
    f50dp_f50_dividend_payout_prefoverhang_63d_jerk_v145_signal,
    f50dp_f50_dividend_payout_cashpayout_63d_jerk_v146_signal,
    f50dp_f50_dividend_payout_dpseps_63d_jerk_v147_signal,
    f50dp_f50_dividend_payout_epscover_63d_jerk_v148_signal,
    f50dp_f50_dividend_payout_divfcf_63d_jerk_v149_signal,
    f50dp_f50_dividend_payout_yieldtrap_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_DIVIDEND_PAYOUT_REGISTRY_001_150 = REGISTRY


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

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False, noise=0.0,
              cycle=0.0, cyc_period=378):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if cycle > 0:
            phase = g.uniform(0, 2 * np.pi)
            s = s + base * cycle * np.sin(2 * np.pi * np.arange(n) / cyc_period + phase)
        if noise > 0:
            s = s * (1.0 + g.normal(0.0, noise, n))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    dps = _fund(201, base=0.6, drift=0.02, vol=0.10, allow_neg=True, noise=0.03,
                cycle=0.8, cyc_period=340).clip(lower=0.0).rename("dps")
    divyield = _fund(202, base=0.03, drift=0.005, vol=0.12, noise=0.05,
                     cycle=0.30, cyc_period=300).clip(lower=0.0).rename("divyield")
    payoutratio = _fund(203, base=0.7, drift=0.01, vol=0.16, noise=0.06,
                        cycle=0.9, cyc_period=410).clip(lower=0.0).rename("payoutratio")
    ncfdiv = (-_fund(204, base=4e7, drift=0.02, vol=0.10, noise=0.04,
                     cycle=0.3, cyc_period=370)).rename("ncfdiv")
    prefdivis = _fund(205, base=6e6, drift=0.01, vol=0.12, noise=0.05,
                      cycle=0.4, cyc_period=440).clip(lower=0.0).rename("prefdivis")
    fcf = _fund(206, base=1.0e8, drift=0.0, vol=0.16, allow_neg=True, noise=0.05,
                cycle=0.9, cyc_period=470).rename("fcf")
    netinccmn = _fund(207, base=9e7, drift=0.0, vol=0.15, allow_neg=True, noise=0.05,
                      cycle=0.9, cyc_period=410).rename("netinccmn")
    eps = _fund(208, base=1.4, drift=0.0, vol=0.15, allow_neg=True, noise=0.05,
                cycle=0.9, cyc_period=380).rename("eps")

    cols = {"dps": dps, "divyield": divyield, "payoutratio": payoutratio,
            "ncfdiv": ncfdiv, "prefdivis": prefdivis, "fcf": fcf,
            "netinccmn": netinccmn, "eps": eps}

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

    print("OK f50_dividend_payout_3rd_derivatives_001_150_claude.py: %d features pass" % n_features)
