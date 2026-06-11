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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _f49_payout_sustain(ncfdiv, fcf):
    return ncfdiv.abs() / fcf.replace(0, np.nan)


def _f49_div_coverage_fcf(fcf, ncfdiv):
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f49_div_coverage_ocf(ncfo, ncfdiv):
    return ncfo / ncfdiv.abs().replace(0, np.nan)


def _f49_pref_drag(prefdivis, netinc):
    return prefdivis.abs() / netinc.abs().replace(0, np.nan)


def _f49_payout_earn(ncfdiv, netinc):
    return ncfdiv.abs() / netinc.replace(0, np.nan)


def f49pr_f49_capital_return_payout_psust_21d_slope_v001_signal(ncfdiv, fcf):
    b = _f49_payout_sustain(ncfdiv, fcf)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_psust_63d_slope_v002_signal(ncfdiv, fcf):
    b = _f49_payout_sustain(ncfdiv, fcf)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_psust_126d_slope_v003_signal(ncfdiv, fcf):
    b = _f49_payout_sustain(ncfdiv, fcf)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsfcfps_21d_slope_v004_signal(dps, fcfps):
    b = (dps / fcfps.replace(0, np.nan))
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsfcfps_126d_slope_v005_signal(dps, fcfps):
    b = (dps / fcfps.replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsfcfps_252d_slope_v006_signal(dps, fcfps):
    b = (dps / fcfps.replace(0, np.nan))
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covfcf_63d_slope_v007_signal(fcf, ncfo, ncfdiv):
    cfcf = _f49_div_coverage_fcf(fcf, ncfdiv)
    cocf = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = (cfcf + cocf) / 2.0
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covfcf_126d_slope_v008_signal(fcf, ncfo, ncfdiv):
    cfcf = _f49_div_coverage_fcf(fcf, ncfdiv)
    cocf = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = (cfcf + cocf) / 2.0
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covfcf_252d_slope_v009_signal(fcf, ncfo, ncfdiv):
    cfcf = _f49_div_coverage_fcf(fcf, ncfdiv)
    cocf = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = (cfcf + cocf) / 2.0
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covocf_21d_slope_v010_signal(ncfo, ncfdiv):
    b = _f49_div_coverage_ocf(ncfo, ncfdiv)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covocf_63d_slope_v011_signal(ncfo, ncfdiv):
    b = _f49_div_coverage_ocf(ncfo, ncfdiv)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covocf_126d_slope_v012_signal(ncfo, ncfdiv):
    b = _f49_div_coverage_ocf(ncfo, ncfdiv)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divyield_21d_slope_v013_signal(divyield):
    b = divyield
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divyield_126d_slope_v014_signal(divyield):
    b = divyield
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divyield_252d_slope_v015_signal(divyield):
    b = divyield
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payoutratio_63d_slope_v016_signal(payoutratio):
    b = payoutratio
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payoutratio_126d_slope_v017_signal(payoutratio):
    b = payoutratio
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payoutratio_252d_slope_v018_signal(payoutratio):
    b = payoutratio
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefdrag_21d_slope_v019_signal(prefdivis, netinc):
    b = _f49_pref_drag(prefdivis, netinc)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefdrag_63d_slope_v020_signal(prefdivis, netinc):
    b = _f49_pref_drag(prefdivis, netinc)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefdrag_126d_slope_v021_signal(prefdivis, netinc):
    b = _f49_pref_drag(prefdivis, netinc)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payearn_21d_slope_v022_signal(ncfdiv, netinc):
    b = _f49_payout_earn(ncfdiv, netinc)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payearn_126d_slope_v023_signal(ncfdiv, netinc):
    b = _f49_payout_earn(ncfdiv, netinc)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payearn_252d_slope_v024_signal(ncfdiv, netinc):
    b = _f49_payout_earn(ncfdiv, netinc)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_fcfyield_63d_slope_v025_signal(fcf, marketcap):
    b = _rank(fcf / marketcap.replace(0, np.nan), 252)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_fcfyield_126d_slope_v026_signal(fcf, marketcap):
    b = _rank(fcf / marketcap.replace(0, np.nan), 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_fcfyield_252d_slope_v027_signal(fcf, marketcap):
    b = _rank(fcf / marketcap.replace(0, np.nan), 252)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dps_21d_slope_v028_signal(dps):
    b = dps
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dps_63d_slope_v029_signal(dps):
    b = dps
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dps_126d_slope_v030_signal(dps):
    b = dps
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epspayout_21d_slope_v031_signal(dps, eps):
    b = (dps / eps.replace(0, np.nan))
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epspayout_126d_slope_v032_signal(dps, eps):
    b = (dps / eps.replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epspayout_252d_slope_v033_signal(dps, eps):
    b = (dps / eps.replace(0, np.nan))
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epsfcfblend_63d_slope_v034_signal(eps, fcfps, dps):
    b = (0.5 * eps + 0.5 * fcfps) / dps.replace(0, np.nan)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epsfcfblend_126d_slope_v035_signal(eps, fcfps, dps):
    b = (0.5 * eps + 0.5 * fcfps) / dps.replace(0, np.nan)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epsfcfblend_252d_slope_v036_signal(eps, fcfps, dps):
    b = (0.5 * eps + 0.5 * fcfps) / dps.replace(0, np.nan)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_cryield_21d_slope_v037_signal(ncfdiv, prefdivis, marketcap):
    b = ((ncfdiv.abs() + prefdivis.abs()) / marketcap.replace(0, np.nan))
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_cryield_63d_slope_v038_signal(ncfdiv, prefdivis, marketcap):
    b = ((ncfdiv.abs() + prefdivis.abs()) / marketcap.replace(0, np.nan))
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_cryield_126d_slope_v039_signal(ncfdiv, prefdivis, marketcap):
    b = ((ncfdiv.abs() + prefdivis.abs()) / marketcap.replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsyield_21d_slope_v040_signal(dps, eps, fcfps):
    b = dps / (eps.abs() + fcfps.abs()).replace(0, np.nan)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsyield_126d_slope_v041_signal(dps, eps, fcfps):
    b = dps / (eps.abs() + fcfps.abs()).replace(0, np.nan)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsyield_252d_slope_v042_signal(dps, eps, fcfps):
    b = dps / (eps.abs() + fcfps.abs()).replace(0, np.nan)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefshare_63d_slope_v043_signal(prefdivis, ncfdiv):
    b = (prefdivis.abs() / (prefdivis.abs() + ncfdiv.abs()).replace(0, np.nan))
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefshare_126d_slope_v044_signal(prefdivis, ncfdiv):
    b = (prefdivis.abs() / (prefdivis.abs() + ncfdiv.abs()).replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefshare_252d_slope_v045_signal(prefdivis, ncfdiv):
    b = (prefdivis.abs() / (prefdivis.abs() + ncfdiv.abs()).replace(0, np.nan))
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_earncov_21d_slope_v046_signal(netinc, ncfdiv):
    b = (netinc / ncfdiv.abs().replace(0, np.nan))
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_earncov_63d_slope_v047_signal(netinc, ncfdiv):
    b = (netinc / ncfdiv.abs().replace(0, np.nan))
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_earncov_126d_slope_v048_signal(netinc, ncfdiv):
    b = (netinc / ncfdiv.abs().replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dyz_21d_slope_v049_signal(divyield):
    b = _z(divyield, 252)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dyz_126d_slope_v050_signal(divyield):
    b = _z(divyield, 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dyz_252d_slope_v051_signal(divyield):
    b = _z(divyield, 252)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prz_63d_slope_v052_signal(payoutratio):
    b = _z(payoutratio, 252)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prz_126d_slope_v053_signal(payoutratio):
    b = _z(payoutratio, 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prz_252d_slope_v054_signal(payoutratio):
    b = _z(payoutratio, 252)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_psbuffer_21d_slope_v055_signal(fcfps, dps):
    b = (fcfps - dps) / fcfps.abs().replace(0, np.nan)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_psbuffer_63d_slope_v056_signal(fcfps, dps):
    b = (fcfps - dps) / fcfps.abs().replace(0, np.nan)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_psbuffer_126d_slope_v057_signal(fcfps, dps):
    b = (fcfps - dps) / fcfps.abs().replace(0, np.nan)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefcap_21d_slope_v058_signal(prefdivis, marketcap, fcfps):
    b = (prefdivis.abs() / marketcap.replace(0, np.nan)) * fcfps
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefcap_126d_slope_v059_signal(prefdivis, marketcap, fcfps):
    b = (prefdivis.abs() / marketcap.replace(0, np.nan)) * fcfps
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefcap_252d_slope_v060_signal(prefdivis, marketcap, fcfps):
    b = (prefdivis.abs() / marketcap.replace(0, np.nan)) * fcfps
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_ocfclaim_63d_slope_v061_signal(ncfdiv, prefdivis, ncfo):
    b = ((ncfdiv.abs() + prefdivis.abs()) / ncfo.replace(0, np.nan))
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_ocfclaim_126d_slope_v062_signal(ncfdiv, prefdivis, ncfo):
    b = ((ncfdiv.abs() + prefdivis.abs()) / ncfo.replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_ocfclaim_252d_slope_v063_signal(ncfdiv, prefdivis, ncfo):
    b = ((ncfdiv.abs() + prefdivis.abs()) / ncfo.replace(0, np.nan))
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsxyield_21d_slope_v064_signal(dps, divyield):
    b = dps * divyield
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsxyield_63d_slope_v065_signal(dps, divyield):
    b = dps * divyield
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsxyield_126d_slope_v066_signal(dps, divyield):
    b = dps * divyield
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_impliedey_21d_slope_v067_signal(divyield, payoutratio):
    b = (divyield / payoutratio.replace(0, np.nan))
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_impliedey_126d_slope_v068_signal(divyield, payoutratio):
    b = (divyield / payoutratio.replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_impliedey_252d_slope_v069_signal(divyield, payoutratio):
    b = (divyield / payoutratio.replace(0, np.nan))
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dyrangepos_63d_slope_v070_signal(divyield):
    hi = divyield.rolling(504, min_periods=126).max()
    lo = divyield.rolling(504, min_periods=126).min()
    b = (divyield - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dyrangepos_126d_slope_v071_signal(divyield):
    hi = divyield.rolling(504, min_periods=126).max()
    lo = divyield.rolling(504, min_periods=126).min()
    b = (divyield - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dyrangepos_252d_slope_v072_signal(divyield):
    hi = divyield.rolling(504, min_periods=126).max()
    lo = divyield.rolling(504, min_periods=126).min()
    b = (divyield - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prrangepos_21d_slope_v073_signal(payoutratio):
    hi = payoutratio.rolling(504, min_periods=126).max()
    lo = payoutratio.rolling(504, min_periods=126).min()
    b = (payoutratio - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prrangepos_63d_slope_v074_signal(payoutratio):
    hi = payoutratio.rolling(504, min_periods=126).max()
    lo = payoutratio.rolling(504, min_periods=126).min()
    b = (payoutratio - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prrangepos_126d_slope_v075_signal(payoutratio):
    hi = payoutratio.rolling(504, min_periods=126).max()
    lo = payoutratio.rolling(504, min_periods=126).min()
    b = (payoutratio - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefmc_21d_slope_v076_signal(prefdivis, marketcap):
    b = (prefdivis.abs() / marketcap.replace(0, np.nan))
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefmc_126d_slope_v077_signal(prefdivis, marketcap):
    b = (prefdivis.abs() / marketcap.replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefmc_252d_slope_v078_signal(prefdivis, marketcap):
    b = (prefdivis.abs() / marketcap.replace(0, np.nan))
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covspread_63d_slope_v079_signal(fcf, ncfo, ncfdiv):
    cfcf = _f49_div_coverage_fcf(fcf, ncfdiv)
    cocf = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = cocf - cfcf
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covspread_126d_slope_v080_signal(fcf, ncfo, ncfdiv):
    cfcf = _f49_div_coverage_fcf(fcf, ncfdiv)
    cocf = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = cocf - cfcf
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covspread_252d_slope_v081_signal(fcf, ncfo, ncfdiv):
    cfcf = _f49_div_coverage_fcf(fcf, ncfdiv)
    cocf = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = cocf - cfcf
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_capexcov_21d_slope_v082_signal(ncfo, fcf, ncfdiv):
    capex = (ncfo - fcf)
    b = capex / (capex.abs() + ncfdiv.abs()).replace(0, np.nan)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_capexcov_63d_slope_v083_signal(ncfo, fcf, ncfdiv):
    capex = (ncfo - fcf)
    b = capex / (capex.abs() + ncfdiv.abs()).replace(0, np.nan)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_capexcov_126d_slope_v084_signal(ncfo, fcf, ncfdiv):
    capex = (ncfo - fcf)
    b = capex / (capex.abs() + ncfdiv.abs()).replace(0, np.nan)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_nimc_21d_slope_v085_signal(netinc, marketcap):
    b = _z(netinc / marketcap.replace(0, np.nan), 252)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_nimc_126d_slope_v086_signal(netinc, marketcap):
    b = _z(netinc / marketcap.replace(0, np.nan), 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_nimc_252d_slope_v087_signal(netinc, marketcap):
    b = _z(netinc / marketcap.replace(0, np.nan), 252)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsxfcfps_63d_slope_v088_signal(fcfps, dps):
    b = np.sign(fcfps - dps) * (fcfps - dps).abs() ** 0.5
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsxfcfps_126d_slope_v089_signal(fcfps, dps):
    b = np.sign(fcfps - dps) * (fcfps - dps).abs() ** 0.5
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsxfcfps_252d_slope_v090_signal(fcfps, dps):
    b = np.sign(fcfps - dps) * (fcfps - dps).abs() ** 0.5
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divyieldxpr_21d_slope_v091_signal(divyield, payoutratio):
    b = divyield * payoutratio
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divyieldxpr_63d_slope_v092_signal(divyield, payoutratio):
    b = divyield * payoutratio
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divyieldxpr_126d_slope_v093_signal(divyield, payoutratio):
    b = divyield * payoutratio
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covconvex_21d_slope_v094_signal(ncfo, ncfdiv):
    cov = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = np.sign(cov - 1.0) * (cov - 1.0) ** 2
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covconvex_126d_slope_v095_signal(ncfo, ncfdiv):
    cov = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = np.sign(cov - 1.0) * (cov - 1.0) ** 2
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covconvex_252d_slope_v096_signal(ncfo, ncfdiv):
    cov = _f49_div_coverage_ocf(ncfo, ncfdiv)
    b = np.sign(cov - 1.0) * (cov - 1.0) ** 2
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsanchor_63d_slope_v097_signal(dps):
    anchor = dps.rolling(252, min_periods=63).mean()
    b = np.log(dps.replace(0, np.nan) / anchor.replace(0, np.nan))
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsanchor_126d_slope_v098_signal(dps):
    anchor = dps.rolling(252, min_periods=63).mean()
    b = np.log(dps.replace(0, np.nan) / anchor.replace(0, np.nan))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsanchor_252d_slope_v099_signal(dps):
    anchor = dps.rolling(252, min_periods=63).mean()
    b = np.log(dps.replace(0, np.nan) / anchor.replace(0, np.nan))
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsmom_21d_slope_v100_signal(dps, fcfps):
    b = (dps.pct_change(63) - fcfps.pct_change(63))
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsmom_63d_slope_v101_signal(dps, fcfps):
    b = (dps.pct_change(63) - fcfps.pct_change(63))
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsmom_126d_slope_v102_signal(dps, fcfps):
    b = (dps.pct_change(63) - fcfps.pct_change(63))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefadj_21d_slope_v103_signal(ncfdiv, prefdivis, netinc):
    avail = netinc - prefdivis.abs()
    b = ncfdiv.abs() / avail.replace(0, np.nan)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefadj_126d_slope_v104_signal(ncfdiv, prefdivis, netinc):
    avail = netinc - prefdivis.abs()
    b = ncfdiv.abs() / avail.replace(0, np.nan)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefadj_252d_slope_v105_signal(ncfdiv, prefdivis, netinc):
    avail = netinc - prefdivis.abs()
    b = ncfdiv.abs() / avail.replace(0, np.nan)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dycross_63d_slope_v106_signal(divyield):
    short = divyield.rolling(63, min_periods=21).mean()
    long = divyield.rolling(252, min_periods=63).mean()
    b = short / long.replace(0, np.nan) - 1.0
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dycross_126d_slope_v107_signal(divyield):
    short = divyield.rolling(63, min_periods=21).mean()
    long = divyield.rolling(252, min_periods=63).mean()
    b = short / long.replace(0, np.nan) - 1.0
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dycross_252d_slope_v108_signal(divyield):
    short = divyield.rolling(63, min_periods=21).mean()
    long = divyield.rolling(252, min_periods=63).mean()
    b = short / long.replace(0, np.nan) - 1.0
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_psustz_21d_slope_v109_signal(ncfdiv, fcf):
    b = _z(_f49_payout_sustain(ncfdiv, fcf), 252)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_psustz_63d_slope_v110_signal(ncfdiv, fcf):
    b = _z(_f49_payout_sustain(ncfdiv, fcf), 252)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_psustz_126d_slope_v111_signal(ncfdiv, fcf):
    b = _z(_f49_payout_sustain(ncfdiv, fcf), 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covdef_21d_slope_v112_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    med = cov.rolling(504, min_periods=126).median()
    b = (med - cov)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covdef_126d_slope_v113_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    med = cov.rolling(504, min_periods=126).median()
    b = (med - cov)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covdef_252d_slope_v114_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    med = cov.rolling(504, min_periods=126).median()
    b = (med - cov)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prxcovdef_63d_slope_v115_signal(payoutratio, ncfo, ncfdiv):
    cov = _f49_div_coverage_ocf(ncfo, ncfdiv)
    deficit = (cov.rolling(252, min_periods=63).median() - cov)
    b = payoutratio * deficit
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prxcovdef_126d_slope_v116_signal(payoutratio, ncfo, ncfdiv):
    cov = _f49_div_coverage_ocf(ncfo, ncfdiv)
    deficit = (cov.rolling(252, min_periods=63).median() - cov)
    b = payoutratio * deficit
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prxcovdef_252d_slope_v117_signal(payoutratio, ncfo, ncfdiv):
    cov = _f49_div_coverage_ocf(ncfo, ncfdiv)
    deficit = (cov.rolling(252, min_periods=63).median() - cov)
    b = payoutratio * deficit
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_ncfodps_21d_slope_v118_signal(ncfo, dps):
    b = ncfo.pct_change(63) * dps
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_ncfodps_63d_slope_v119_signal(ncfo, dps):
    b = ncfo.pct_change(63) * dps
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_ncfodps_126d_slope_v120_signal(ncfo, dps):
    b = ncfo.pct_change(63) * dps
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divnorm_21d_slope_v121_signal(ncfdiv):
    avg = ncfdiv.abs().rolling(504, min_periods=126).mean()
    b = ncfdiv.abs() / avg.replace(0, np.nan) - 1.0
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divnorm_126d_slope_v122_signal(ncfdiv):
    avg = ncfdiv.abs().rolling(504, min_periods=126).mean()
    b = ncfdiv.abs() / avg.replace(0, np.nan) - 1.0
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divnorm_252d_slope_v123_signal(ncfdiv):
    avg = ncfdiv.abs().rolling(504, min_periods=126).mean()
    b = ncfdiv.abs() / avg.replace(0, np.nan) - 1.0
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dylonganchor_63d_slope_v124_signal(divyield):
    anchor = divyield.rolling(504, min_periods=126).mean()
    b = divyield / anchor.replace(0, np.nan) - 1.0
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dylonganchor_126d_slope_v125_signal(divyield):
    anchor = divyield.rolling(504, min_periods=126).mean()
    b = divyield / anchor.replace(0, np.nan) - 1.0
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dylonganchor_252d_slope_v126_signal(divyield):
    anchor = divyield.rolling(504, min_periods=126).mean()
    b = divyield / anchor.replace(0, np.nan) - 1.0
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefdragz_21d_slope_v127_signal(prefdivis, netinc):
    b = _z(_f49_pref_drag(prefdivis, netinc), 252)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefdragz_63d_slope_v128_signal(prefdivis, netinc):
    b = _z(_f49_pref_drag(prefdivis, netinc), 252)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prefdragz_126d_slope_v129_signal(prefdivis, netinc):
    b = _z(_f49_pref_drag(prefdivis, netinc), 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covsource_21d_slope_v130_signal(netinc, fcf, ncfdiv):
    ecov = netinc / ncfdiv.abs().replace(0, np.nan)
    fcov = _f49_div_coverage_fcf(fcf, ncfdiv)
    b = ecov - fcov
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covsource_126d_slope_v131_signal(netinc, fcf, ncfdiv):
    ecov = netinc / ncfdiv.abs().replace(0, np.nan)
    fcov = _f49_div_coverage_fcf(fcf, ncfdiv)
    b = ecov - fcov
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_covsource_252d_slope_v132_signal(netinc, fcf, ncfdiv):
    ecov = netinc / ncfdiv.abs().replace(0, np.nan)
    fcov = _f49_div_coverage_fcf(fcf, ncfdiv)
    b = ecov - fcov
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prcovstress_63d_slope_v133_signal(payoutratio, fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    b = payoutratio / (1.0 + cov.clip(lower=0))
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prcovstress_126d_slope_v134_signal(payoutratio, fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    b = payoutratio / (1.0 + cov.clip(lower=0))
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_prcovstress_252d_slope_v135_signal(payoutratio, fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    b = payoutratio / (1.0 + cov.clip(lower=0))
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_fcfpsz_21d_slope_v136_signal(fcfps):
    b = _z(fcfps, 252)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_fcfpsz_63d_slope_v137_signal(fcfps):
    b = _z(fcfps, 252)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_fcfpsz_126d_slope_v138_signal(fcfps):
    b = _z(fcfps, 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epscushz_21d_slope_v139_signal(eps, dps):
    b = _z(eps / dps.replace(0, np.nan), 252)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epscushz_126d_slope_v140_signal(eps, dps):
    b = _z(eps / dps.replace(0, np.nan), 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_epscushz_252d_slope_v141_signal(eps, dps):
    b = _z(eps / dps.replace(0, np.nan), 252)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payearnz_63d_slope_v142_signal(ncfdiv, netinc):
    b = _z(_f49_payout_earn(ncfdiv, netinc), 252)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payearnz_126d_slope_v143_signal(ncfdiv, netinc):
    b = _z(_f49_payout_earn(ncfdiv, netinc), 252)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_payearnz_252d_slope_v144_signal(ncfdiv, netinc):
    b = _z(_f49_payout_earn(ncfdiv, netinc), 252)
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsrangepos_21d_slope_v145_signal(dps):
    hi = dps.rolling(504, min_periods=126).max()
    lo = dps.rolling(504, min_periods=126).min()
    b = (dps - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsrangepos_63d_slope_v146_signal(dps):
    hi = dps.rolling(504, min_periods=126).max()
    lo = dps.rolling(504, min_periods=126).min()
    b = (dps - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(31, min_periods=max(2, 31 // 2)).mean()
    d = bsm - bsm.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_dpsrangepos_126d_slope_v147_signal(dps):
    hi = dps.rolling(504, min_periods=126).max()
    lo = dps.rolling(504, min_periods=126).min()
    b = (dps - lo) / (hi - lo).replace(0, np.nan)
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divcoverstreak_21d_slope_v148_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    rising = (cov > cov.shift(63)).astype(float)
    b = rising.groupby((rising == 0).cumsum()).cumsum()
    bsm = b.rolling(10, min_periods=max(2, 10 // 2)).mean()
    d = bsm - bsm.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divcoverstreak_126d_slope_v149_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    rising = (cov > cov.shift(63)).astype(float)
    b = rising.groupby((rising == 0).cumsum()).cumsum()
    bsm = b.rolling(63, min_periods=max(2, 63 // 2)).mean()
    d = bsm - bsm.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f49pr_f49_capital_return_payout_divcoverstreak_252d_slope_v150_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    rising = (cov > cov.shift(63)).astype(float)
    b = rising.groupby((rising == 0).cumsum()).cumsum()
    bsm = b.rolling(126, min_periods=max(2, 126 // 2)).mean()
    d = bsm - bsm.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f49pr_f49_capital_return_payout_psust_21d_slope_v001_signal,
    f49pr_f49_capital_return_payout_psust_63d_slope_v002_signal,
    f49pr_f49_capital_return_payout_psust_126d_slope_v003_signal,
    f49pr_f49_capital_return_payout_dpsfcfps_21d_slope_v004_signal,
    f49pr_f49_capital_return_payout_dpsfcfps_126d_slope_v005_signal,
    f49pr_f49_capital_return_payout_dpsfcfps_252d_slope_v006_signal,
    f49pr_f49_capital_return_payout_covfcf_63d_slope_v007_signal,
    f49pr_f49_capital_return_payout_covfcf_126d_slope_v008_signal,
    f49pr_f49_capital_return_payout_covfcf_252d_slope_v009_signal,
    f49pr_f49_capital_return_payout_covocf_21d_slope_v010_signal,
    f49pr_f49_capital_return_payout_covocf_63d_slope_v011_signal,
    f49pr_f49_capital_return_payout_covocf_126d_slope_v012_signal,
    f49pr_f49_capital_return_payout_divyield_21d_slope_v013_signal,
    f49pr_f49_capital_return_payout_divyield_126d_slope_v014_signal,
    f49pr_f49_capital_return_payout_divyield_252d_slope_v015_signal,
    f49pr_f49_capital_return_payout_payoutratio_63d_slope_v016_signal,
    f49pr_f49_capital_return_payout_payoutratio_126d_slope_v017_signal,
    f49pr_f49_capital_return_payout_payoutratio_252d_slope_v018_signal,
    f49pr_f49_capital_return_payout_prefdrag_21d_slope_v019_signal,
    f49pr_f49_capital_return_payout_prefdrag_63d_slope_v020_signal,
    f49pr_f49_capital_return_payout_prefdrag_126d_slope_v021_signal,
    f49pr_f49_capital_return_payout_payearn_21d_slope_v022_signal,
    f49pr_f49_capital_return_payout_payearn_126d_slope_v023_signal,
    f49pr_f49_capital_return_payout_payearn_252d_slope_v024_signal,
    f49pr_f49_capital_return_payout_fcfyield_63d_slope_v025_signal,
    f49pr_f49_capital_return_payout_fcfyield_126d_slope_v026_signal,
    f49pr_f49_capital_return_payout_fcfyield_252d_slope_v027_signal,
    f49pr_f49_capital_return_payout_dps_21d_slope_v028_signal,
    f49pr_f49_capital_return_payout_dps_63d_slope_v029_signal,
    f49pr_f49_capital_return_payout_dps_126d_slope_v030_signal,
    f49pr_f49_capital_return_payout_epspayout_21d_slope_v031_signal,
    f49pr_f49_capital_return_payout_epspayout_126d_slope_v032_signal,
    f49pr_f49_capital_return_payout_epspayout_252d_slope_v033_signal,
    f49pr_f49_capital_return_payout_epsfcfblend_63d_slope_v034_signal,
    f49pr_f49_capital_return_payout_epsfcfblend_126d_slope_v035_signal,
    f49pr_f49_capital_return_payout_epsfcfblend_252d_slope_v036_signal,
    f49pr_f49_capital_return_payout_cryield_21d_slope_v037_signal,
    f49pr_f49_capital_return_payout_cryield_63d_slope_v038_signal,
    f49pr_f49_capital_return_payout_cryield_126d_slope_v039_signal,
    f49pr_f49_capital_return_payout_dpsyield_21d_slope_v040_signal,
    f49pr_f49_capital_return_payout_dpsyield_126d_slope_v041_signal,
    f49pr_f49_capital_return_payout_dpsyield_252d_slope_v042_signal,
    f49pr_f49_capital_return_payout_prefshare_63d_slope_v043_signal,
    f49pr_f49_capital_return_payout_prefshare_126d_slope_v044_signal,
    f49pr_f49_capital_return_payout_prefshare_252d_slope_v045_signal,
    f49pr_f49_capital_return_payout_earncov_21d_slope_v046_signal,
    f49pr_f49_capital_return_payout_earncov_63d_slope_v047_signal,
    f49pr_f49_capital_return_payout_earncov_126d_slope_v048_signal,
    f49pr_f49_capital_return_payout_dyz_21d_slope_v049_signal,
    f49pr_f49_capital_return_payout_dyz_126d_slope_v050_signal,
    f49pr_f49_capital_return_payout_dyz_252d_slope_v051_signal,
    f49pr_f49_capital_return_payout_prz_63d_slope_v052_signal,
    f49pr_f49_capital_return_payout_prz_126d_slope_v053_signal,
    f49pr_f49_capital_return_payout_prz_252d_slope_v054_signal,
    f49pr_f49_capital_return_payout_psbuffer_21d_slope_v055_signal,
    f49pr_f49_capital_return_payout_psbuffer_63d_slope_v056_signal,
    f49pr_f49_capital_return_payout_psbuffer_126d_slope_v057_signal,
    f49pr_f49_capital_return_payout_prefcap_21d_slope_v058_signal,
    f49pr_f49_capital_return_payout_prefcap_126d_slope_v059_signal,
    f49pr_f49_capital_return_payout_prefcap_252d_slope_v060_signal,
    f49pr_f49_capital_return_payout_ocfclaim_63d_slope_v061_signal,
    f49pr_f49_capital_return_payout_ocfclaim_126d_slope_v062_signal,
    f49pr_f49_capital_return_payout_ocfclaim_252d_slope_v063_signal,
    f49pr_f49_capital_return_payout_dpsxyield_21d_slope_v064_signal,
    f49pr_f49_capital_return_payout_dpsxyield_63d_slope_v065_signal,
    f49pr_f49_capital_return_payout_dpsxyield_126d_slope_v066_signal,
    f49pr_f49_capital_return_payout_impliedey_21d_slope_v067_signal,
    f49pr_f49_capital_return_payout_impliedey_126d_slope_v068_signal,
    f49pr_f49_capital_return_payout_impliedey_252d_slope_v069_signal,
    f49pr_f49_capital_return_payout_dyrangepos_63d_slope_v070_signal,
    f49pr_f49_capital_return_payout_dyrangepos_126d_slope_v071_signal,
    f49pr_f49_capital_return_payout_dyrangepos_252d_slope_v072_signal,
    f49pr_f49_capital_return_payout_prrangepos_21d_slope_v073_signal,
    f49pr_f49_capital_return_payout_prrangepos_63d_slope_v074_signal,
    f49pr_f49_capital_return_payout_prrangepos_126d_slope_v075_signal,
    f49pr_f49_capital_return_payout_prefmc_21d_slope_v076_signal,
    f49pr_f49_capital_return_payout_prefmc_126d_slope_v077_signal,
    f49pr_f49_capital_return_payout_prefmc_252d_slope_v078_signal,
    f49pr_f49_capital_return_payout_covspread_63d_slope_v079_signal,
    f49pr_f49_capital_return_payout_covspread_126d_slope_v080_signal,
    f49pr_f49_capital_return_payout_covspread_252d_slope_v081_signal,
    f49pr_f49_capital_return_payout_capexcov_21d_slope_v082_signal,
    f49pr_f49_capital_return_payout_capexcov_63d_slope_v083_signal,
    f49pr_f49_capital_return_payout_capexcov_126d_slope_v084_signal,
    f49pr_f49_capital_return_payout_nimc_21d_slope_v085_signal,
    f49pr_f49_capital_return_payout_nimc_126d_slope_v086_signal,
    f49pr_f49_capital_return_payout_nimc_252d_slope_v087_signal,
    f49pr_f49_capital_return_payout_dpsxfcfps_63d_slope_v088_signal,
    f49pr_f49_capital_return_payout_dpsxfcfps_126d_slope_v089_signal,
    f49pr_f49_capital_return_payout_dpsxfcfps_252d_slope_v090_signal,
    f49pr_f49_capital_return_payout_divyieldxpr_21d_slope_v091_signal,
    f49pr_f49_capital_return_payout_divyieldxpr_63d_slope_v092_signal,
    f49pr_f49_capital_return_payout_divyieldxpr_126d_slope_v093_signal,
    f49pr_f49_capital_return_payout_covconvex_21d_slope_v094_signal,
    f49pr_f49_capital_return_payout_covconvex_126d_slope_v095_signal,
    f49pr_f49_capital_return_payout_covconvex_252d_slope_v096_signal,
    f49pr_f49_capital_return_payout_dpsanchor_63d_slope_v097_signal,
    f49pr_f49_capital_return_payout_dpsanchor_126d_slope_v098_signal,
    f49pr_f49_capital_return_payout_dpsanchor_252d_slope_v099_signal,
    f49pr_f49_capital_return_payout_dpsmom_21d_slope_v100_signal,
    f49pr_f49_capital_return_payout_dpsmom_63d_slope_v101_signal,
    f49pr_f49_capital_return_payout_dpsmom_126d_slope_v102_signal,
    f49pr_f49_capital_return_payout_prefadj_21d_slope_v103_signal,
    f49pr_f49_capital_return_payout_prefadj_126d_slope_v104_signal,
    f49pr_f49_capital_return_payout_prefadj_252d_slope_v105_signal,
    f49pr_f49_capital_return_payout_dycross_63d_slope_v106_signal,
    f49pr_f49_capital_return_payout_dycross_126d_slope_v107_signal,
    f49pr_f49_capital_return_payout_dycross_252d_slope_v108_signal,
    f49pr_f49_capital_return_payout_psustz_21d_slope_v109_signal,
    f49pr_f49_capital_return_payout_psustz_63d_slope_v110_signal,
    f49pr_f49_capital_return_payout_psustz_126d_slope_v111_signal,
    f49pr_f49_capital_return_payout_covdef_21d_slope_v112_signal,
    f49pr_f49_capital_return_payout_covdef_126d_slope_v113_signal,
    f49pr_f49_capital_return_payout_covdef_252d_slope_v114_signal,
    f49pr_f49_capital_return_payout_prxcovdef_63d_slope_v115_signal,
    f49pr_f49_capital_return_payout_prxcovdef_126d_slope_v116_signal,
    f49pr_f49_capital_return_payout_prxcovdef_252d_slope_v117_signal,
    f49pr_f49_capital_return_payout_ncfodps_21d_slope_v118_signal,
    f49pr_f49_capital_return_payout_ncfodps_63d_slope_v119_signal,
    f49pr_f49_capital_return_payout_ncfodps_126d_slope_v120_signal,
    f49pr_f49_capital_return_payout_divnorm_21d_slope_v121_signal,
    f49pr_f49_capital_return_payout_divnorm_126d_slope_v122_signal,
    f49pr_f49_capital_return_payout_divnorm_252d_slope_v123_signal,
    f49pr_f49_capital_return_payout_dylonganchor_63d_slope_v124_signal,
    f49pr_f49_capital_return_payout_dylonganchor_126d_slope_v125_signal,
    f49pr_f49_capital_return_payout_dylonganchor_252d_slope_v126_signal,
    f49pr_f49_capital_return_payout_prefdragz_21d_slope_v127_signal,
    f49pr_f49_capital_return_payout_prefdragz_63d_slope_v128_signal,
    f49pr_f49_capital_return_payout_prefdragz_126d_slope_v129_signal,
    f49pr_f49_capital_return_payout_covsource_21d_slope_v130_signal,
    f49pr_f49_capital_return_payout_covsource_126d_slope_v131_signal,
    f49pr_f49_capital_return_payout_covsource_252d_slope_v132_signal,
    f49pr_f49_capital_return_payout_prcovstress_63d_slope_v133_signal,
    f49pr_f49_capital_return_payout_prcovstress_126d_slope_v134_signal,
    f49pr_f49_capital_return_payout_prcovstress_252d_slope_v135_signal,
    f49pr_f49_capital_return_payout_fcfpsz_21d_slope_v136_signal,
    f49pr_f49_capital_return_payout_fcfpsz_63d_slope_v137_signal,
    f49pr_f49_capital_return_payout_fcfpsz_126d_slope_v138_signal,
    f49pr_f49_capital_return_payout_epscushz_21d_slope_v139_signal,
    f49pr_f49_capital_return_payout_epscushz_126d_slope_v140_signal,
    f49pr_f49_capital_return_payout_epscushz_252d_slope_v141_signal,
    f49pr_f49_capital_return_payout_payearnz_63d_slope_v142_signal,
    f49pr_f49_capital_return_payout_payearnz_126d_slope_v143_signal,
    f49pr_f49_capital_return_payout_payearnz_252d_slope_v144_signal,
    f49pr_f49_capital_return_payout_dpsrangepos_21d_slope_v145_signal,
    f49pr_f49_capital_return_payout_dpsrangepos_63d_slope_v146_signal,
    f49pr_f49_capital_return_payout_dpsrangepos_126d_slope_v147_signal,
    f49pr_f49_capital_return_payout_divcoverstreak_21d_slope_v148_signal,
    f49pr_f49_capital_return_payout_divcoverstreak_126d_slope_v149_signal,
    f49pr_f49_capital_return_payout_divcoverstreak_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_CAPITAL_RETURN_PAYOUT_REGISTRY_SLOPE_001_150 = REGISTRY

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

    dps = _fund(1, base=1.0, drift=0.01, vol=0.05).rename("dps")
    divyield = _fund(2, base=0.03, drift=0.0, vol=0.06).rename("divyield")
    payoutratio = _fund(3, base=0.5, drift=0.0, vol=0.07).rename("payoutratio")
    ncfdiv = _fund(4, base=5e7, drift=0.005, vol=0.07).rename("ncfdiv")
    prefdivis = _fund(5, base=5e6, drift=0.0, vol=0.07).rename("prefdivis")
    fcf = _fund(6, base=1.2e8, drift=0.0, vol=0.10, allow_neg=True).rename("fcf")
    ncfo = _fund(7, base=2e8, drift=0.0, vol=0.09, allow_neg=True).rename("ncfo")
    fcfps = _fund(8, base=2.0, drift=0.0, vol=0.10, allow_neg=True).rename("fcfps")
    eps = _fund(9, base=2.5, drift=0.0, vol=0.10, allow_neg=True).rename("eps")
    netinc = _fund(10, base=1.5e8, drift=0.0, vol=0.10, allow_neg=True).rename("netinc")
    marketcap = _fund(11, base=2e9, drift=0.0, vol=0.06).rename("marketcap")

    cols = {"dps": dps, "divyield": divyield, "payoutratio": payoutratio,
            "ncfdiv": ncfdiv, "prefdivis": prefdivis, "fcf": fcf, "ncfo": ncfo,
            "fcfps": fcfps, "eps": eps, "netinc": netinc, "marketcap": marketcap}

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
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f49_capital_return_payout_2nd_derivatives_001_150_claude: %d features pass" % n_features)
