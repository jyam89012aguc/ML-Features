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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _roc(s, w):
    return s - s.shift(w)


# ===== folder domain primitives (dividend / payout policy) =====
def _f22_yield(divyield):
    return divyield


def _f22_payout(payoutratio):
    return payoutratio


def _f22_fcf_cover(ncfdiv, fcf):
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f22_div_to_netinc(ncfdiv, netinc):
    return ncfdiv.abs() / netinc.replace(0, np.nan)


def _f22_sustain(fcf, ncfdiv):
    return (fcf - ncfdiv.abs()) / fcf.abs().replace(0, np.nan)


def _f22_buffer(fcf, ncfdiv):
    return fcf - ncfdiv.abs()


def f22dp_f22_dividend_payout_policy_dyld_21d_slope_v001_signal(divyield):
    q = _mean(_f22_yield(divyield), 21)
    d1 = q - q.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyld_63d_slope_v002_signal(divyield):
    q = _mean(_f22_yield(divyield), 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyld_126d_slope_v003_signal(divyield):
    q = _mean(_f22_yield(divyield), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldz_252d_slope_v004_signal(divyield):
    q = _z(_f22_yield(divyield), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldz_126d_slope_v005_signal(divyield):
    q = _z(_f22_yield(divyield), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldrnk_504d_slope_v006_signal(divyield):
    q = _rank(_f22_yield(divyield), 504)
    d1 = q - q.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldmed_252d_slope_v007_signal(divyield):
    q = _f22_yield(divyield) - _f22_yield(divyield).rolling(252, min_periods=126).median()
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payout_63d_slope_v008_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payout_126d_slope_v009_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payoutz_252d_slope_v010_signal(payoutratio):
    q = _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payoutz_126d_slope_v011_signal(payoutratio):
    q = _z(_f22_payout(payoutratio), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payrnk_504d_slope_v012_signal(payoutratio):
    q = _rank(_f22_payout(payoutratio), 504)
    d1 = q - q.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paymed_252d_slope_v013_signal(payoutratio):
    q = _f22_payout(payoutratio) - _f22_payout(payoutratio).rolling(252, min_periods=126).median()
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paysq_63d_slope_v014_signal(payoutratio):
    q = _mean((_f22_payout(payoutratio) - 0.6) ** 2, 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcov_63d_slope_v015_signal(ncfdiv, fcf):
    q = _mean(_f22_fcf_cover(ncfdiv, fcf), 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcov_126d_slope_v016_signal(ncfdiv, fcf):
    q = _mean(_f22_fcf_cover(ncfdiv, fcf), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcovz_252d_slope_v017_signal(ncfdiv, fcf):
    q = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpspay_126d_slope_v018_signal(dps, payoutratio):
    q = _mean(dps * _f22_payout(payoutratio), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covrnk_504d_slope_v019_signal(ncfdiv, fcf):
    q = _rank(_f22_fcf_cover(ncfdiv, fcf), 504)
    d1 = q - q.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldni_252d_slope_v020_signal(divyield, netinc):
    q = _z(_f22_yield(divyield) * np.sign(netinc) * (netinc.abs() ** 0.25), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_divni_63d_slope_v021_signal(ncfdiv, netinc):
    q = _mean(_f22_div_to_netinc(ncfdiv, netinc), 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_diniz_252d_slope_v022_signal(ncfdiv, netinc):
    q = _z(_f22_div_to_netinc(ncfdiv, netinc), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dinirnk_504d_slope_v023_signal(ncfdiv, netinc):
    q = _rank(_f22_div_to_netinc(ncfdiv, netinc), 504)
    d1 = q - q.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_nicov_126d_slope_v024_signal(ncfdiv, netinc):
    q = _mean(np.tanh((netinc / ncfdiv.abs().replace(0, np.nan)) / 5.0), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dps_63d_slope_v025_signal(dps):
    q = _mean(dps, 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsz_252d_slope_v026_signal(dps):
    q = _z(dps, 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsrnk_504d_slope_v027_signal(dps):
    q = _rank(dps, 504)
    d1 = q - q.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsstr_252d_slope_v028_signal(dps):
    q = dps / _mean(dps, 252).replace(0, np.nan) - 1.0
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsdd_252d_slope_v029_signal(dps):
    q = dps / dps.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsmom_252d_slope_v030_signal(dps):
    q = _mean(dps / dps.shift(126).replace(0, np.nan) - 1.0, 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldpz_252d_slope_v031_signal(divyield, payoutratio):
    q = _z(_f22_yield(divyield), 252) - _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldrnk_252d_slope_v032_signal(divyield):
    q = _rank(_f22_yield(divyield), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufpay_63d_slope_v033_signal(fcf, ncfdiv, payoutratio):
    q = _mean(_f22_buffer(fcf, ncfdiv), 63) * _f22_payout(payoutratio)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufz_252d_slope_v034_signal(fcf, ncfdiv):
    q = _z(_f22_buffer(fcf, ncfdiv), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufni_63d_slope_v035_signal(fcf, ncfdiv, netinc):
    q = _mean(_f22_buffer(fcf, ncfdiv) / netinc.abs().replace(0, np.nan), 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldpay_63d_slope_v036_signal(divyield, payoutratio):
    q = _mean(_f22_yield(divyield) * _f22_payout(payoutratio), 63)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldperp_126d_slope_v037_signal(divyield, payoutratio):
    q = _mean(_f22_yield(divyield) / _f22_payout(payoutratio).replace(0, np.nan), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covmpay_252d_slope_v038_signal(ncfdiv, fcf, payoutratio):
    q = _z(_f22_fcf_cover(ncfdiv, fcf), 252) - _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_ylddisp_252d_slope_v039_signal(divyield):
    q = _std(_f22_yield(divyield), 252) / _mean(_f22_yield(divyield), 252).replace(0, np.nan)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paydisp_252d_slope_v040_signal(payoutratio):
    q = _std(_f22_payout(payoutratio), 252) / _mean(_f22_payout(payoutratio), 252).replace(0, np.nan)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covdisp_252d_slope_v041_signal(ncfdiv, fcf):
    q = _std(_f22_fcf_cover(ncfdiv, fcf), 252) / _mean(_f22_fcf_cover(ncfdiv, fcf), 252).abs().replace(0, np.nan)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_qualyld_126d_slope_v042_signal(divyield, ncfdiv, fcf):
    q = _z(_f22_yield(divyield), 126) - 0.5 * _z(_f22_fcf_cover(ncfdiv, fcf), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsyld_126d_slope_v043_signal(dps, divyield):
    q = _mean(dps * _f22_yield(divyield), 126)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_tension_252d_slope_v044_signal(divyield, payoutratio, ncfdiv, fcf):
    q = _z(_f22_yield(divyield), 252) + _z(_f22_payout(payoutratio), 252) - _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_incint_252d_slope_v045_signal(dps, divyield):
    q = _z(dps * _f22_yield(divyield), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paycov_252d_slope_v046_signal(payoutratio, ncfdiv, fcf):
    q = _mean(_f22_payout(payoutratio) / _f22_fcf_cover(ncfdiv, fcf).clip(lower=0.1), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufema_252d_slope_v047_signal(fcf, ncfdiv, netinc):
    q = ((fcf - ncfdiv.abs()) / netinc.abs().replace(0, np.nan)).ewm(span=126, min_periods=42).mean()
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_genros_252d_slope_v048_signal(dps, payoutratio, netinc):
    q = _z(dps * _f22_payout(payoutratio) / (netinc.abs().replace(0, np.nan) ** 0.25), 252)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldshrp_252d_slope_v049_signal(divyield):
    q = _mean(_f22_yield(divyield), 252) / _std(_f22_yield(divyield), 252).replace(0, np.nan)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paysh_252d_slope_v050_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 252) / _std(_f22_payout(payoutratio), 252).replace(0, np.nan)
    d1 = q - q.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyld_21d_slope_v051_signal(divyield):
    q = _mean(_f22_yield(divyield), 21)
    d1 = q - q.shift(7)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyld_63d_slope_v052_signal(divyield):
    q = _mean(_f22_yield(divyield), 63)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyld_126d_slope_v053_signal(divyield):
    q = _mean(_f22_yield(divyield), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldz_252d_slope_v054_signal(divyield):
    q = _z(_f22_yield(divyield), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldz_126d_slope_v055_signal(divyield):
    q = _z(_f22_yield(divyield), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldrnk_504d_slope_v056_signal(divyield):
    q = _rank(_f22_yield(divyield), 504)
    d1 = q - q.shift(168)
    result = d1 / (_std(q, 504).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldmed_252d_slope_v057_signal(divyield):
    q = _f22_yield(divyield) - _f22_yield(divyield).rolling(252, min_periods=126).median()
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payout_63d_slope_v058_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 63)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payout_126d_slope_v059_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payoutz_252d_slope_v060_signal(payoutratio):
    q = _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payoutz_126d_slope_v061_signal(payoutratio):
    q = _z(_f22_payout(payoutratio), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payrnk_504d_slope_v062_signal(payoutratio):
    q = _rank(_f22_payout(payoutratio), 504)
    d1 = q - q.shift(168)
    result = d1 / (_std(q, 504).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paymed_252d_slope_v063_signal(payoutratio):
    q = _f22_payout(payoutratio) - _f22_payout(payoutratio).rolling(252, min_periods=126).median()
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paysq_63d_slope_v064_signal(payoutratio):
    q = _mean((_f22_payout(payoutratio) - 0.6) ** 2, 63)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcov_63d_slope_v065_signal(ncfdiv, fcf):
    q = _mean(_f22_fcf_cover(ncfdiv, fcf), 63)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcov_126d_slope_v066_signal(ncfdiv, fcf):
    q = _mean(_f22_fcf_cover(ncfdiv, fcf), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcovz_252d_slope_v067_signal(ncfdiv, fcf):
    q = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpspay_126d_slope_v068_signal(dps, payoutratio):
    q = _mean(dps * _f22_payout(payoutratio), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covrnk_504d_slope_v069_signal(ncfdiv, fcf):
    q = _rank(_f22_fcf_cover(ncfdiv, fcf), 504)
    d1 = q - q.shift(168)
    result = d1 / (_std(q, 504).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldni_252d_slope_v070_signal(divyield, netinc):
    q = _z(_f22_yield(divyield) * np.sign(netinc) * (netinc.abs() ** 0.25), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_divni_63d_slope_v071_signal(ncfdiv, netinc):
    q = _mean(_f22_div_to_netinc(ncfdiv, netinc), 63)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_diniz_252d_slope_v072_signal(ncfdiv, netinc):
    q = _z(_f22_div_to_netinc(ncfdiv, netinc), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dinirnk_504d_slope_v073_signal(ncfdiv, netinc):
    q = _rank(_f22_div_to_netinc(ncfdiv, netinc), 504)
    d1 = q - q.shift(168)
    result = d1 / (_std(q, 504).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_nicov_126d_slope_v074_signal(ncfdiv, netinc):
    q = _mean(np.tanh((netinc / ncfdiv.abs().replace(0, np.nan)) / 5.0), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dps_63d_slope_v075_signal(dps):
    q = _mean(dps, 63)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsz_252d_slope_v076_signal(dps):
    q = _z(dps, 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsrnk_504d_slope_v077_signal(dps):
    q = _rank(dps, 504)
    d1 = q - q.shift(168)
    result = d1 / (_std(q, 504).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsstr_252d_slope_v078_signal(dps):
    q = dps / _mean(dps, 252).replace(0, np.nan) - 1.0
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsdd_252d_slope_v079_signal(dps):
    q = dps / dps.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsmom_252d_slope_v080_signal(dps):
    q = _mean(dps / dps.shift(126).replace(0, np.nan) - 1.0, 63)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldpz_252d_slope_v081_signal(divyield, payoutratio):
    q = _z(_f22_yield(divyield), 252) - _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldrnk_252d_slope_v082_signal(divyield):
    q = _rank(_f22_yield(divyield), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufpay_63d_slope_v083_signal(fcf, ncfdiv, payoutratio):
    q = _mean(_f22_buffer(fcf, ncfdiv), 63) * _f22_payout(payoutratio)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufz_252d_slope_v084_signal(fcf, ncfdiv):
    q = _z(_f22_buffer(fcf, ncfdiv), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufni_63d_slope_v085_signal(fcf, ncfdiv, netinc):
    q = _mean(_f22_buffer(fcf, ncfdiv) / netinc.abs().replace(0, np.nan), 63)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldpay_63d_slope_v086_signal(divyield, payoutratio):
    q = _mean(_f22_yield(divyield) * _f22_payout(payoutratio), 63)
    d1 = q - q.shift(21)
    result = d1 / (_std(q, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldperp_126d_slope_v087_signal(divyield, payoutratio):
    q = _mean(_f22_yield(divyield) / _f22_payout(payoutratio).replace(0, np.nan), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covmpay_252d_slope_v088_signal(ncfdiv, fcf, payoutratio):
    q = _z(_f22_fcf_cover(ncfdiv, fcf), 252) - _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_ylddisp_252d_slope_v089_signal(divyield):
    q = _std(_f22_yield(divyield), 252) / _mean(_f22_yield(divyield), 252).replace(0, np.nan)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paydisp_252d_slope_v090_signal(payoutratio):
    q = _std(_f22_payout(payoutratio), 252) / _mean(_f22_payout(payoutratio), 252).replace(0, np.nan)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covdisp_252d_slope_v091_signal(ncfdiv, fcf):
    q = _std(_f22_fcf_cover(ncfdiv, fcf), 252) / _mean(_f22_fcf_cover(ncfdiv, fcf), 252).abs().replace(0, np.nan)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_qualyld_126d_slope_v092_signal(divyield, ncfdiv, fcf):
    q = _z(_f22_yield(divyield), 126) - 0.5 * _z(_f22_fcf_cover(ncfdiv, fcf), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsyld_126d_slope_v093_signal(dps, divyield):
    q = _mean(dps * _f22_yield(divyield), 126)
    d1 = q - q.shift(42)
    result = d1 / (_std(q, 126).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_tension_252d_slope_v094_signal(divyield, payoutratio, ncfdiv, fcf):
    q = _z(_f22_yield(divyield), 252) + _z(_f22_payout(payoutratio), 252) - _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_incint_252d_slope_v095_signal(dps, divyield):
    q = _z(dps * _f22_yield(divyield), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paycov_252d_slope_v096_signal(payoutratio, ncfdiv, fcf):
    q = _mean(_f22_payout(payoutratio) / _f22_fcf_cover(ncfdiv, fcf).clip(lower=0.1), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufema_252d_slope_v097_signal(fcf, ncfdiv, netinc):
    q = ((fcf - ncfdiv.abs()) / netinc.abs().replace(0, np.nan)).ewm(span=126, min_periods=42).mean()
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_genros_252d_slope_v098_signal(dps, payoutratio, netinc):
    q = _z(dps * _f22_payout(payoutratio) / (netinc.abs().replace(0, np.nan) ** 0.25), 252)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldshrp_252d_slope_v099_signal(divyield):
    q = _mean(_f22_yield(divyield), 252) / _std(_f22_yield(divyield), 252).replace(0, np.nan)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paysh_252d_slope_v100_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 252) / _std(_f22_payout(payoutratio), 252).replace(0, np.nan)
    d1 = q - q.shift(84)
    result = d1 / (_std(q, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyld_21d_slope_v101_signal(divyield):
    q = _mean(_f22_yield(divyield), 21)
    d1 = q - q.shift(10)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyld_63d_slope_v102_signal(divyield):
    q = _mean(_f22_yield(divyield), 63)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyld_126d_slope_v103_signal(divyield):
    q = _mean(_f22_yield(divyield), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldz_252d_slope_v104_signal(divyield):
    q = _z(_f22_yield(divyield), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldz_126d_slope_v105_signal(divyield):
    q = _z(_f22_yield(divyield), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldrnk_504d_slope_v106_signal(divyield):
    q = _rank(_f22_yield(divyield), 504)
    d1 = q - q.shift(63)
    result = _rank(d1, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dyldmed_252d_slope_v107_signal(divyield):
    q = _f22_yield(divyield) - _f22_yield(divyield).rolling(252, min_periods=126).median()
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payout_63d_slope_v108_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 63)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payout_126d_slope_v109_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payoutz_252d_slope_v110_signal(payoutratio):
    q = _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payoutz_126d_slope_v111_signal(payoutratio):
    q = _z(_f22_payout(payoutratio), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_payrnk_504d_slope_v112_signal(payoutratio):
    q = _rank(_f22_payout(payoutratio), 504)
    d1 = q - q.shift(63)
    result = _rank(d1, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paymed_252d_slope_v113_signal(payoutratio):
    q = _f22_payout(payoutratio) - _f22_payout(payoutratio).rolling(252, min_periods=126).median()
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paysq_63d_slope_v114_signal(payoutratio):
    q = _mean((_f22_payout(payoutratio) - 0.6) ** 2, 63)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcov_63d_slope_v115_signal(ncfdiv, fcf):
    q = _mean(_f22_fcf_cover(ncfdiv, fcf), 63)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcov_126d_slope_v116_signal(ncfdiv, fcf):
    q = _mean(_f22_fcf_cover(ncfdiv, fcf), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_fcfcovz_252d_slope_v117_signal(ncfdiv, fcf):
    q = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpspay_126d_slope_v118_signal(dps, payoutratio):
    q = _mean(dps * _f22_payout(payoutratio), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covrnk_504d_slope_v119_signal(ncfdiv, fcf):
    q = _rank(_f22_fcf_cover(ncfdiv, fcf), 504)
    d1 = q - q.shift(63)
    result = _rank(d1, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldni_252d_slope_v120_signal(divyield, netinc):
    q = _z(_f22_yield(divyield) * np.sign(netinc) * (netinc.abs() ** 0.25), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_divni_63d_slope_v121_signal(ncfdiv, netinc):
    q = _mean(_f22_div_to_netinc(ncfdiv, netinc), 63)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_diniz_252d_slope_v122_signal(ncfdiv, netinc):
    q = _z(_f22_div_to_netinc(ncfdiv, netinc), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dinirnk_504d_slope_v123_signal(ncfdiv, netinc):
    q = _rank(_f22_div_to_netinc(ncfdiv, netinc), 504)
    d1 = q - q.shift(63)
    result = _rank(d1, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_nicov_126d_slope_v124_signal(ncfdiv, netinc):
    q = _mean(np.tanh((netinc / ncfdiv.abs().replace(0, np.nan)) / 5.0), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dps_63d_slope_v125_signal(dps):
    q = _mean(dps, 63)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsz_252d_slope_v126_signal(dps):
    q = _z(dps, 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsrnk_504d_slope_v127_signal(dps):
    q = _rank(dps, 504)
    d1 = q - q.shift(63)
    result = _rank(d1, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsstr_252d_slope_v128_signal(dps):
    q = dps / _mean(dps, 252).replace(0, np.nan) - 1.0
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsdd_252d_slope_v129_signal(dps):
    q = dps / dps.rolling(252, min_periods=126).max().replace(0, np.nan) - 1.0
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsmom_252d_slope_v130_signal(dps):
    q = _mean(dps / dps.shift(126).replace(0, np.nan) - 1.0, 63)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldpz_252d_slope_v131_signal(divyield, payoutratio):
    q = _z(_f22_yield(divyield), 252) - _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldrnk_252d_slope_v132_signal(divyield):
    q = _rank(_f22_yield(divyield), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufpay_63d_slope_v133_signal(fcf, ncfdiv, payoutratio):
    q = _mean(_f22_buffer(fcf, ncfdiv), 63) * _f22_payout(payoutratio)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufz_252d_slope_v134_signal(fcf, ncfdiv):
    q = _z(_f22_buffer(fcf, ncfdiv), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufni_63d_slope_v135_signal(fcf, ncfdiv, netinc):
    q = _mean(_f22_buffer(fcf, ncfdiv) / netinc.abs().replace(0, np.nan), 63)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldpay_63d_slope_v136_signal(divyield, payoutratio):
    q = _mean(_f22_yield(divyield) * _f22_payout(payoutratio), 63)
    d1 = q - q.shift(31)
    result = _rank(d1, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldperp_126d_slope_v137_signal(divyield, payoutratio):
    q = _mean(_f22_yield(divyield) / _f22_payout(payoutratio).replace(0, np.nan), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covmpay_252d_slope_v138_signal(ncfdiv, fcf, payoutratio):
    q = _z(_f22_fcf_cover(ncfdiv, fcf), 252) - _z(_f22_payout(payoutratio), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_ylddisp_252d_slope_v139_signal(divyield):
    q = _std(_f22_yield(divyield), 252) / _mean(_f22_yield(divyield), 252).replace(0, np.nan)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paydisp_252d_slope_v140_signal(payoutratio):
    q = _std(_f22_payout(payoutratio), 252) / _mean(_f22_payout(payoutratio), 252).replace(0, np.nan)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_covdisp_252d_slope_v141_signal(ncfdiv, fcf):
    q = _std(_f22_fcf_cover(ncfdiv, fcf), 252) / _mean(_f22_fcf_cover(ncfdiv, fcf), 252).abs().replace(0, np.nan)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_qualyld_126d_slope_v142_signal(divyield, ncfdiv, fcf):
    q = _z(_f22_yield(divyield), 126) - 0.5 * _z(_f22_fcf_cover(ncfdiv, fcf), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_dpsyld_126d_slope_v143_signal(dps, divyield):
    q = _mean(dps * _f22_yield(divyield), 126)
    d1 = q - q.shift(63)
    result = _rank(d1, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_tension_252d_slope_v144_signal(divyield, payoutratio, ncfdiv, fcf):
    q = _z(_f22_yield(divyield), 252) + _z(_f22_payout(payoutratio), 252) - _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_incint_252d_slope_v145_signal(dps, divyield):
    q = _z(dps * _f22_yield(divyield), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paycov_252d_slope_v146_signal(payoutratio, ncfdiv, fcf):
    q = _mean(_f22_payout(payoutratio) / _f22_fcf_cover(ncfdiv, fcf).clip(lower=0.1), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_bufema_252d_slope_v147_signal(fcf, ncfdiv, netinc):
    q = ((fcf - ncfdiv.abs()) / netinc.abs().replace(0, np.nan)).ewm(span=126, min_periods=42).mean()
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_genros_252d_slope_v148_signal(dps, payoutratio, netinc):
    q = _z(dps * _f22_payout(payoutratio) / (netinc.abs().replace(0, np.nan) ** 0.25), 252)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_yldshrp_252d_slope_v149_signal(divyield):
    q = _mean(_f22_yield(divyield), 252) / _std(_f22_yield(divyield), 252).replace(0, np.nan)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f22dp_f22_dividend_payout_policy_paysh_252d_slope_v150_signal(payoutratio):
    q = _mean(_f22_payout(payoutratio), 252) / _std(_f22_payout(payoutratio), 252).replace(0, np.nan)
    d1 = q - q.shift(63)
    result = _rank(d1, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f22dp_f22_dividend_payout_policy_dyld_21d_slope_v001_signal,
    f22dp_f22_dividend_payout_policy_dyld_63d_slope_v002_signal,
    f22dp_f22_dividend_payout_policy_dyld_126d_slope_v003_signal,
    f22dp_f22_dividend_payout_policy_dyldz_252d_slope_v004_signal,
    f22dp_f22_dividend_payout_policy_dyldz_126d_slope_v005_signal,
    f22dp_f22_dividend_payout_policy_dyldrnk_504d_slope_v006_signal,
    f22dp_f22_dividend_payout_policy_dyldmed_252d_slope_v007_signal,
    f22dp_f22_dividend_payout_policy_payout_63d_slope_v008_signal,
    f22dp_f22_dividend_payout_policy_payout_126d_slope_v009_signal,
    f22dp_f22_dividend_payout_policy_payoutz_252d_slope_v010_signal,
    f22dp_f22_dividend_payout_policy_payoutz_126d_slope_v011_signal,
    f22dp_f22_dividend_payout_policy_payrnk_504d_slope_v012_signal,
    f22dp_f22_dividend_payout_policy_paymed_252d_slope_v013_signal,
    f22dp_f22_dividend_payout_policy_paysq_63d_slope_v014_signal,
    f22dp_f22_dividend_payout_policy_fcfcov_63d_slope_v015_signal,
    f22dp_f22_dividend_payout_policy_fcfcov_126d_slope_v016_signal,
    f22dp_f22_dividend_payout_policy_fcfcovz_252d_slope_v017_signal,
    f22dp_f22_dividend_payout_policy_dpspay_126d_slope_v018_signal,
    f22dp_f22_dividend_payout_policy_covrnk_504d_slope_v019_signal,
    f22dp_f22_dividend_payout_policy_yldni_252d_slope_v020_signal,
    f22dp_f22_dividend_payout_policy_divni_63d_slope_v021_signal,
    f22dp_f22_dividend_payout_policy_diniz_252d_slope_v022_signal,
    f22dp_f22_dividend_payout_policy_dinirnk_504d_slope_v023_signal,
    f22dp_f22_dividend_payout_policy_nicov_126d_slope_v024_signal,
    f22dp_f22_dividend_payout_policy_dps_63d_slope_v025_signal,
    f22dp_f22_dividend_payout_policy_dpsz_252d_slope_v026_signal,
    f22dp_f22_dividend_payout_policy_dpsrnk_504d_slope_v027_signal,
    f22dp_f22_dividend_payout_policy_dpsstr_252d_slope_v028_signal,
    f22dp_f22_dividend_payout_policy_dpsdd_252d_slope_v029_signal,
    f22dp_f22_dividend_payout_policy_dpsmom_252d_slope_v030_signal,
    f22dp_f22_dividend_payout_policy_yldpz_252d_slope_v031_signal,
    f22dp_f22_dividend_payout_policy_yldrnk_252d_slope_v032_signal,
    f22dp_f22_dividend_payout_policy_bufpay_63d_slope_v033_signal,
    f22dp_f22_dividend_payout_policy_bufz_252d_slope_v034_signal,
    f22dp_f22_dividend_payout_policy_bufni_63d_slope_v035_signal,
    f22dp_f22_dividend_payout_policy_yldpay_63d_slope_v036_signal,
    f22dp_f22_dividend_payout_policy_yldperp_126d_slope_v037_signal,
    f22dp_f22_dividend_payout_policy_covmpay_252d_slope_v038_signal,
    f22dp_f22_dividend_payout_policy_ylddisp_252d_slope_v039_signal,
    f22dp_f22_dividend_payout_policy_paydisp_252d_slope_v040_signal,
    f22dp_f22_dividend_payout_policy_covdisp_252d_slope_v041_signal,
    f22dp_f22_dividend_payout_policy_qualyld_126d_slope_v042_signal,
    f22dp_f22_dividend_payout_policy_dpsyld_126d_slope_v043_signal,
    f22dp_f22_dividend_payout_policy_tension_252d_slope_v044_signal,
    f22dp_f22_dividend_payout_policy_incint_252d_slope_v045_signal,
    f22dp_f22_dividend_payout_policy_paycov_252d_slope_v046_signal,
    f22dp_f22_dividend_payout_policy_bufema_252d_slope_v047_signal,
    f22dp_f22_dividend_payout_policy_genros_252d_slope_v048_signal,
    f22dp_f22_dividend_payout_policy_yldshrp_252d_slope_v049_signal,
    f22dp_f22_dividend_payout_policy_paysh_252d_slope_v050_signal,
    f22dp_f22_dividend_payout_policy_dyld_21d_slope_v051_signal,
    f22dp_f22_dividend_payout_policy_dyld_63d_slope_v052_signal,
    f22dp_f22_dividend_payout_policy_dyld_126d_slope_v053_signal,
    f22dp_f22_dividend_payout_policy_dyldz_252d_slope_v054_signal,
    f22dp_f22_dividend_payout_policy_dyldz_126d_slope_v055_signal,
    f22dp_f22_dividend_payout_policy_dyldrnk_504d_slope_v056_signal,
    f22dp_f22_dividend_payout_policy_dyldmed_252d_slope_v057_signal,
    f22dp_f22_dividend_payout_policy_payout_63d_slope_v058_signal,
    f22dp_f22_dividend_payout_policy_payout_126d_slope_v059_signal,
    f22dp_f22_dividend_payout_policy_payoutz_252d_slope_v060_signal,
    f22dp_f22_dividend_payout_policy_payoutz_126d_slope_v061_signal,
    f22dp_f22_dividend_payout_policy_payrnk_504d_slope_v062_signal,
    f22dp_f22_dividend_payout_policy_paymed_252d_slope_v063_signal,
    f22dp_f22_dividend_payout_policy_paysq_63d_slope_v064_signal,
    f22dp_f22_dividend_payout_policy_fcfcov_63d_slope_v065_signal,
    f22dp_f22_dividend_payout_policy_fcfcov_126d_slope_v066_signal,
    f22dp_f22_dividend_payout_policy_fcfcovz_252d_slope_v067_signal,
    f22dp_f22_dividend_payout_policy_dpspay_126d_slope_v068_signal,
    f22dp_f22_dividend_payout_policy_covrnk_504d_slope_v069_signal,
    f22dp_f22_dividend_payout_policy_yldni_252d_slope_v070_signal,
    f22dp_f22_dividend_payout_policy_divni_63d_slope_v071_signal,
    f22dp_f22_dividend_payout_policy_diniz_252d_slope_v072_signal,
    f22dp_f22_dividend_payout_policy_dinirnk_504d_slope_v073_signal,
    f22dp_f22_dividend_payout_policy_nicov_126d_slope_v074_signal,
    f22dp_f22_dividend_payout_policy_dps_63d_slope_v075_signal,
    f22dp_f22_dividend_payout_policy_dpsz_252d_slope_v076_signal,
    f22dp_f22_dividend_payout_policy_dpsrnk_504d_slope_v077_signal,
    f22dp_f22_dividend_payout_policy_dpsstr_252d_slope_v078_signal,
    f22dp_f22_dividend_payout_policy_dpsdd_252d_slope_v079_signal,
    f22dp_f22_dividend_payout_policy_dpsmom_252d_slope_v080_signal,
    f22dp_f22_dividend_payout_policy_yldpz_252d_slope_v081_signal,
    f22dp_f22_dividend_payout_policy_yldrnk_252d_slope_v082_signal,
    f22dp_f22_dividend_payout_policy_bufpay_63d_slope_v083_signal,
    f22dp_f22_dividend_payout_policy_bufz_252d_slope_v084_signal,
    f22dp_f22_dividend_payout_policy_bufni_63d_slope_v085_signal,
    f22dp_f22_dividend_payout_policy_yldpay_63d_slope_v086_signal,
    f22dp_f22_dividend_payout_policy_yldperp_126d_slope_v087_signal,
    f22dp_f22_dividend_payout_policy_covmpay_252d_slope_v088_signal,
    f22dp_f22_dividend_payout_policy_ylddisp_252d_slope_v089_signal,
    f22dp_f22_dividend_payout_policy_paydisp_252d_slope_v090_signal,
    f22dp_f22_dividend_payout_policy_covdisp_252d_slope_v091_signal,
    f22dp_f22_dividend_payout_policy_qualyld_126d_slope_v092_signal,
    f22dp_f22_dividend_payout_policy_dpsyld_126d_slope_v093_signal,
    f22dp_f22_dividend_payout_policy_tension_252d_slope_v094_signal,
    f22dp_f22_dividend_payout_policy_incint_252d_slope_v095_signal,
    f22dp_f22_dividend_payout_policy_paycov_252d_slope_v096_signal,
    f22dp_f22_dividend_payout_policy_bufema_252d_slope_v097_signal,
    f22dp_f22_dividend_payout_policy_genros_252d_slope_v098_signal,
    f22dp_f22_dividend_payout_policy_yldshrp_252d_slope_v099_signal,
    f22dp_f22_dividend_payout_policy_paysh_252d_slope_v100_signal,
    f22dp_f22_dividend_payout_policy_dyld_21d_slope_v101_signal,
    f22dp_f22_dividend_payout_policy_dyld_63d_slope_v102_signal,
    f22dp_f22_dividend_payout_policy_dyld_126d_slope_v103_signal,
    f22dp_f22_dividend_payout_policy_dyldz_252d_slope_v104_signal,
    f22dp_f22_dividend_payout_policy_dyldz_126d_slope_v105_signal,
    f22dp_f22_dividend_payout_policy_dyldrnk_504d_slope_v106_signal,
    f22dp_f22_dividend_payout_policy_dyldmed_252d_slope_v107_signal,
    f22dp_f22_dividend_payout_policy_payout_63d_slope_v108_signal,
    f22dp_f22_dividend_payout_policy_payout_126d_slope_v109_signal,
    f22dp_f22_dividend_payout_policy_payoutz_252d_slope_v110_signal,
    f22dp_f22_dividend_payout_policy_payoutz_126d_slope_v111_signal,
    f22dp_f22_dividend_payout_policy_payrnk_504d_slope_v112_signal,
    f22dp_f22_dividend_payout_policy_paymed_252d_slope_v113_signal,
    f22dp_f22_dividend_payout_policy_paysq_63d_slope_v114_signal,
    f22dp_f22_dividend_payout_policy_fcfcov_63d_slope_v115_signal,
    f22dp_f22_dividend_payout_policy_fcfcov_126d_slope_v116_signal,
    f22dp_f22_dividend_payout_policy_fcfcovz_252d_slope_v117_signal,
    f22dp_f22_dividend_payout_policy_dpspay_126d_slope_v118_signal,
    f22dp_f22_dividend_payout_policy_covrnk_504d_slope_v119_signal,
    f22dp_f22_dividend_payout_policy_yldni_252d_slope_v120_signal,
    f22dp_f22_dividend_payout_policy_divni_63d_slope_v121_signal,
    f22dp_f22_dividend_payout_policy_diniz_252d_slope_v122_signal,
    f22dp_f22_dividend_payout_policy_dinirnk_504d_slope_v123_signal,
    f22dp_f22_dividend_payout_policy_nicov_126d_slope_v124_signal,
    f22dp_f22_dividend_payout_policy_dps_63d_slope_v125_signal,
    f22dp_f22_dividend_payout_policy_dpsz_252d_slope_v126_signal,
    f22dp_f22_dividend_payout_policy_dpsrnk_504d_slope_v127_signal,
    f22dp_f22_dividend_payout_policy_dpsstr_252d_slope_v128_signal,
    f22dp_f22_dividend_payout_policy_dpsdd_252d_slope_v129_signal,
    f22dp_f22_dividend_payout_policy_dpsmom_252d_slope_v130_signal,
    f22dp_f22_dividend_payout_policy_yldpz_252d_slope_v131_signal,
    f22dp_f22_dividend_payout_policy_yldrnk_252d_slope_v132_signal,
    f22dp_f22_dividend_payout_policy_bufpay_63d_slope_v133_signal,
    f22dp_f22_dividend_payout_policy_bufz_252d_slope_v134_signal,
    f22dp_f22_dividend_payout_policy_bufni_63d_slope_v135_signal,
    f22dp_f22_dividend_payout_policy_yldpay_63d_slope_v136_signal,
    f22dp_f22_dividend_payout_policy_yldperp_126d_slope_v137_signal,
    f22dp_f22_dividend_payout_policy_covmpay_252d_slope_v138_signal,
    f22dp_f22_dividend_payout_policy_ylddisp_252d_slope_v139_signal,
    f22dp_f22_dividend_payout_policy_paydisp_252d_slope_v140_signal,
    f22dp_f22_dividend_payout_policy_covdisp_252d_slope_v141_signal,
    f22dp_f22_dividend_payout_policy_qualyld_126d_slope_v142_signal,
    f22dp_f22_dividend_payout_policy_dpsyld_126d_slope_v143_signal,
    f22dp_f22_dividend_payout_policy_tension_252d_slope_v144_signal,
    f22dp_f22_dividend_payout_policy_incint_252d_slope_v145_signal,
    f22dp_f22_dividend_payout_policy_paycov_252d_slope_v146_signal,
    f22dp_f22_dividend_payout_policy_bufema_252d_slope_v147_signal,
    f22dp_f22_dividend_payout_policy_genros_252d_slope_v148_signal,
    f22dp_f22_dividend_payout_policy_yldshrp_252d_slope_v149_signal,
    f22dp_f22_dividend_payout_policy_paysh_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_DIVIDEND_PAYOUT_POLICY_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    dps = _fund(101, base=1.5, drift=0.01, vol=0.04).rename("dps")
    divyield = _fund(102, base=0.03, drift=0.005, vol=0.05).rename("divyield")
    payoutratio = _fund(103, base=0.95, drift=0.004, vol=0.14).rename("payoutratio")
    ncfdiv = _fund(104, base=4.5e8, drift=0.015, vol=0.12).rename("ncfdiv")
    netinc = _fund(105, base=5e8, drift=0.02, vol=0.10, allow_neg=True).rename("netinc")
    fcf = _fund(106, base=5e8, drift=0.02, vol=0.13, allow_neg=True).rename("fcf")

    cols = {"dps": dps, "divyield": divyield, "payoutratio": payoutratio,
            "ncfdiv": ncfdiv, "netinc": netinc, "fcf": fcf}

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f22_dividend_payout_policy_2nd_derivatives_001_150_claude: %d features pass" % n_features)
