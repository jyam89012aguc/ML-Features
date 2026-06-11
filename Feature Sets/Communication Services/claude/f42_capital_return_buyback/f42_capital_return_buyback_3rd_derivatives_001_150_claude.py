import inspect
import numpy as np
import pandas as pd

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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (capital return / buyback) =====
def _f42_buyback(ncfcommon):
    return (-ncfcommon).clip(lower=0)


def _f42_issuance(ncfcommon):
    return ncfcommon.clip(lower=0)


def _f42_buyback_yield(ncfcommon, marketcap):
    return _f42_buyback(ncfcommon) / marketcap.replace(0, np.nan)


def _f42_div_yield(ncfdiv, marketcap):
    return ncfdiv.abs() / marketcap.replace(0, np.nan)


def _f42_total_yield(ncfcommon, ncfdiv, marketcap):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    return ret / marketcap.replace(0, np.nan)


def _f42_div_cover(ncfdiv, fcf):
    return fcf / ncfdiv.abs().replace(0, np.nan)



def f42rb_f42_capital_return_buyback_byyield_jerk_v001_signal(ncfcommon, marketcap):  # jerk deriv of v001 w=21d
    b = _f42_buyback_yield(ncfcommon, marketcap)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byyieldsm_jerk_v002_signal(ncfcommon, marketcap):  # jerk deriv of v002 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by.rolling(63, min_periods=21).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byyieldz_jerk_v003_signal(ncfcommon, marketcap):  # jerk deriv of v003 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _z(by, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byyieldrank_jerk_v004_signal(ncfcommon, marketcap):  # jerk deriv of v004 w=63d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _rank(by, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshflow_jerk_v005_signal(ncfcommon, marketcap):  # jerk deriv of v005 w=42d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = nsf - nsf.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_issyield_jerk_v006_signal(ncfcommon, marketcap):  # jerk deriv of v006 w=21d
    b = _f42_issuance(ncfcommon) / marketcap.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_buybackbias_jerk_v007_signal(ncfcommon):  # jerk deriv of v007 w=21d
    net = (-ncfcommon).rolling(63, min_periods=21).sum()
    gross = ncfcommon.abs().rolling(63, min_periods=21).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divyield_jerk_v008_signal(ncfdiv, marketcap):  # jerk deriv of v008 w=21d
    b = _f42_div_yield(ncfdiv, marketcap)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divyieldz_jerk_v009_signal(ncfdiv, marketcap):  # jerk deriv of v009 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _z(dy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divyieldrank_jerk_v010_signal(ncfdiv, marketcap):  # jerk deriv of v010 w=63d
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _rank(dy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_totyield_jerk_v011_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v011 w=21d
    b = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_totyieldsm_jerk_v012_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v012 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_totyieldz_jerk_v013_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v013 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _z(ty, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_returnmix_jerk_v014_signal(ncfcommon, ncfdiv):  # jerk deriv of v014 w=21d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    b = (bb - dv) / (bb + dv).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divcover_jerk_v015_signal(ncfdiv, fcf):  # jerk deriv of v015 w=21d
    b = _f42_div_cover(ncfdiv, fcf)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divcoversm_jerk_v016_signal(ncfdiv, fcf):  # jerk deriv of v016 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divcoverz_jerk_v017_signal(ncfdiv, fcf):  # jerk deriv of v017 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _z(cov, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divpayout_jerk_v018_signal(ncfdiv, fcf):  # jerk deriv of v018 w=21d
    b = ncfdiv.abs() / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfpayout_jerk_v019_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v019 w=21d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = ret / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retcover_jerk_v020_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v020 w=21d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    b = fcf / ret
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcf_jerk_v021_signal(ncfcommon, fcf):  # jerk deriv of v021 w=21d
    b = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbocf_jerk_v022_signal(ncfcommon, ncfo):  # jerk deriv of v022 w=21d
    b = _f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divocf_jerk_v023_signal(ncfdiv, ncfo):  # jerk deriv of v023 w=21d
    b = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retocf_jerk_v024_signal(ncfcommon, ncfdiv, ncfo):  # jerk deriv of v024 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = ncfo.clip(lower=0) / ret
    b = cov - cov.rolling(252, min_periods=84).median()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpslevel_jerk_v025_signal(dps):  # jerk deriv of v025 w=21d
    fast = dps.ewm(span=42, min_periods=21).mean()
    slow = dps.ewm(span=189, min_periods=63).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsgrow_jerk_v026_signal(dps):  # jerk deriv of v026 w=42d
    b = dps / dps.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsz_jerk_v027_signal(dps):  # jerk deriv of v027 w=42d
    b = _z(dps, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpshikefreq_jerk_v028_signal(dps):  # jerk deriv of v028 w=42d
    up = (dps > dps.shift(21)).astype(float)
    b = up.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpscut_jerk_v029_signal(dps):  # jerk deriv of v029 w=42d
    peak = dps.rolling(252, min_periods=84).max()
    b = dps / peak.replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divreliance_jerk_v030_signal(ncfdiv, ncfcommon, marketcap):  # jerk deriv of v030 w=21d
    dy = _f42_div_yield(ncfdiv, marketcap)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).replace(0, np.nan)
    share = dy / ty
    b = _slope(share, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byaccel_jerk_v031_signal(ncfcommon, marketcap):  # jerk deriv of v031 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by - by.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tymom_jerk_v032_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v032 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty - ty.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dymom_jerk_v033_signal(ncfdiv, marketcap):  # jerk deriv of v033 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = dy - dy.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfyield_jerk_v034_signal(fcf, marketcap):  # jerk deriv of v034 w=21d
    b = fcf / marketcap.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfyieldz_jerk_v035_signal(fcf, marketcap):  # jerk deriv of v035 w=42d
    fy = fcf / marketcap.replace(0, np.nan)
    b = _z(fy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_surplus_jerk_v036_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v036 w=42d
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    b = surplus - surplus.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfconv_jerk_v037_signal(fcf, ncfo):  # jerk deriv of v037 w=42d
    conv = fcf / ncfo.replace(0, np.nan)
    b = _z(conv, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_overpay_jerk_v038_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v038 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    gap = ty - fy
    b = gap - gap.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_sustdepth_jerk_v039_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v039 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    margin = (fcf - ret) / ret.replace(0, np.nan)
    b = _z(margin, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbpersist_jerk_v040_signal(ncfcommon):  # jerk deriv of v040 w=42d
    isbb = (-ncfcommon > 0).astype(float)
    b = isbb.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covregime_jerk_v041_signal(ncfdiv, fcf):  # jerk deriv of v041 w=63d
    cov = _f42_div_cover(ncfdiv, fcf)
    med = cov.rolling(504, min_periods=126).median()
    ok = (cov > med).astype(float)
    b = ok.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_selffund_jerk_v042_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v042 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    margin = np.tanh((fcf - ret) / ret.replace(0, np.nan))
    b = margin.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tiltyield_jerk_v043_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v043 w=21d
    b = (_f42_buyback(ncfcommon) - ncfdiv.abs()) / marketcap.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bydisp_jerk_v044_signal(ncfcommon, marketcap):  # jerk deriv of v044 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _std(by, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dystable_jerk_v045_signal(ncfdiv, marketcap):  # jerk deriv of v045 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    m = _mean(dy, 252)
    sd = _std(dy, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tysmooth_jerk_v046_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v046 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = -_std(ty, 126) / _mean(ty, 126).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbocfz_jerk_v047_signal(ncfcommon, ncfo):  # jerk deriv of v047 w=42d
    r = _f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_hikefund_jerk_v048_signal(dps, fcf):  # jerk deriv of v048 w=42d
    dg = dps / dps.shift(252).replace(0, np.nan) - 1.0
    fg = fcf / fcf.shift(252).replace(0, np.nan) - 1.0
    b = dg - fg
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byfcfratio_jerk_v049_signal(ncfcommon, fcf, marketcap):  # jerk deriv of v049 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = (fcf / marketcap.replace(0, np.nan)).replace(0, np.nan)
    b = _z(by / fy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_mixmom_jerk_v050_signal(ncfcommon, ncfdiv):  # jerk deriv of v050 w=42d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _z(mix, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tyrank_jerk_v051_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v051 w=63d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _rank(ty, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbperdiv_jerk_v052_signal(ncfcommon, ncfdiv):  # jerk deriv of v052 w=42d
    bb_sum = _f42_buyback(ncfcommon).rolling(252, min_periods=84).sum()
    dv_sum = ncfdiv.abs().rolling(252, min_periods=84).sum()
    b = np.log((bb_sum + 1.0) / (dv_sum + 1.0).replace(0, np.nan))
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbheadroom_jerk_v053_signal(fcf, ncfdiv, marketcap):  # jerk deriv of v053 w=63d
    fy = fcf / marketcap.replace(0, np.nan)
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _rank(fy - dy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_burdenz_jerk_v054_signal(ncfcommon, ncfdiv, ncfo):  # jerk deriv of v054 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    r = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covtrend_jerk_v055_signal(ncfdiv, fcf):  # jerk deriv of v055 w=21d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _slope(cov, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bytrend_jerk_v056_signal(ncfcommon, marketcap):  # jerk deriv of v056 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _slope(by, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_distribrank_jerk_v057_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v057 w=63d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _rank(ty - fy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_incomequal_jerk_v058_signal(ncfdiv, fcf, marketcap):  # jerk deriv of v058 w=21d
    dy = _f42_div_yield(ncfdiv, marketcap)
    cov = _f42_div_cover(ncfdiv, fcf).clip(lower=0)
    b = dy * np.tanh(cov)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbqual_jerk_v059_signal(ncfcommon, fcf, marketcap):  # jerk deriv of v059 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fund = (fcf / _f42_buyback(ncfcommon).replace(0, np.nan)).clip(0, 3)
    b = by * fund
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retscore_jerk_v060_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v060 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret).clip(lower=0)
    b = ty * np.tanh(cov)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dilregime_jerk_v061_signal(ncfcommon):  # jerk deriv of v061 w=42d
    iss = ncfcommon.clip(lower=0)
    disp = _std(iss, 252) / (_mean(iss, 252).replace(0, np.nan))
    b = disp
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_payeridentity_jerk_v062_signal(dps, ncfdiv, marketcap):  # jerk deriv of v062 w=42d
    dg = (dps / dps.shift(63).replace(0, np.nan) - 1.0)
    dvy = _f42_div_yield(ncfdiv, marketcap)
    b = dg.rolling(252, min_periods=84).corr(dvy)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_intensz_jerk_v063_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v063 w=63d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _z(ty, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbstress_jerk_v064_signal(ncfcommon, fcf, marketcap):  # jerk deriv of v064 w=21d
    bb = _f42_buyback(ncfcommon)
    shortfall = (bb - fcf.clip(lower=0)) / bb.replace(0, np.nan)
    b = np.tanh(shortfall)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_incomevsbb_jerk_v065_signal(dps, ncfcommon, marketcap):  # jerk deriv of v065 w=21d
    dg = (dps / dps.shift(126).replace(0, np.nan) - 1.0).clip(lower=0)
    by = _f42_buyback_yield(ncfcommon, marketcap).rolling(63, min_periods=21).mean()
    b = np.tanh(dg) - np.tanh(80.0 * by)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divocfz_jerk_v066_signal(ncfdiv, ncfo):  # jerk deriv of v066 w=42d
    r = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_warchest_jerk_v067_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v067 w=42d
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(63, min_periods=21).mean()
    b = _z(sm, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_payoutgrow_jerk_v068_signal(ncfcommon, ncfdiv):  # jerk deriv of v068 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = ret / ret.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbtiming_jerk_v069_signal(ncfcommon, fcf, marketcap):  # jerk deriv of v069 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = by * np.sign(fy) * np.sqrt(fy.abs())
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covimprove_jerk_v070_signal(ncfdiv, fcf):  # jerk deriv of v070 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov - cov.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshdisp_jerk_v071_signal(ncfcommon, marketcap):  # jerk deriv of v071 w=42d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = nsf.ewm(span=63, min_periods=21).mean() - nsf.ewm(span=252, min_periods=63).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_cyclicality_jerk_v072_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v072 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = ty.rolling(252, min_periods=84).corr(fy)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dyfcfshare_jerk_v073_signal(ncfdiv, ncfo):  # jerk deriv of v073 w=42d
    dg = ncfdiv.abs() / ncfdiv.abs().shift(252).replace(0, np.nan) - 1.0
    og = ncfo / ncfo.shift(252).replace(0, np.nan) - 1.0
    b = dg - og
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbsignmag_jerk_v074_signal(ncfcommon, marketcap):  # jerk deriv of v074 w=42d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    typ = nsf.rolling(252, min_periods=84).mean()
    b = np.sign(nsf) * np.sqrt(nsf.abs()) - np.sign(typ) * np.sqrt(typ.abs())
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_durability_jerk_v075_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v075 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret)
    mincov = cov.rolling(252, min_periods=84).min().clip(lower=0)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty * np.tanh(mincov)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byyieldyr_jerk_v076_signal(ncfcommon, marketcap):  # jerk deriv of v076 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byaccel2_jerk_v077_signal(ncfcommon, marketcap):  # jerk deriv of v077 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap).rolling(63, min_periods=21).mean()
    b = by - by.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bycurv_jerk_v078_signal(ncfcommon, marketcap):  # jerk deriv of v078 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    d = by - by.shift(63)
    b = d - d.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbcumyield_jerk_v079_signal(ncfcommon):  # jerk deriv of v079 w=42d
    bb = _f42_buyback(ncfcommon).rolling(252, min_periods=84).sum()
    b = bb / bb.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byskew_jerk_v080_signal(ncfcommon, marketcap):  # jerk deriv of v080 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    typ = by.rolling(252, min_periods=84).median()
    b = np.sqrt(by) - np.sqrt(typ.clip(lower=0))
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divyieldyr_jerk_v081_signal(ncfdiv, marketcap):  # jerk deriv of v081 w=63d
    dy = _f42_div_yield(ncfdiv, marketcap).rolling(252, min_periods=84).mean()
    b = _z(dy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dyaccel_jerk_v082_signal(ncfdiv, marketcap):  # jerk deriv of v082 w=21d
    dy = _f42_div_yield(ncfdiv, marketcap).rolling(63, min_periods=21).mean()
    b = dy - dy.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dycurv_jerk_v083_signal(ncfdiv, marketcap):  # jerk deriv of v083 w=21d
    dy = _f42_div_yield(ncfdiv, marketcap)
    d = dy - dy.shift(63)
    b = d - d.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divcumyield_jerk_v084_signal(ncfdiv, marketcap):  # jerk deriv of v084 w=42d
    dv = ncfdiv.abs().rolling(252, min_periods=84).sum()
    cy = dv / (marketcap * 4.0).replace(0, np.nan)
    b = _z(cy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dydisp_jerk_v085_signal(ncfdiv, marketcap):  # jerk deriv of v085 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _std(dy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tyyrz_jerk_v086_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v086 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(252, min_periods=84).mean()
    b = ty / ty.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tyaccel_jerk_v087_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v087 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    d = ty - ty.shift(63)
    b = d - d.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tycumyield_jerk_v088_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v088 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).rolling(252, min_periods=84).sum()
    b = ret / (marketcap * 4.0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tydisp_jerk_v089_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v089 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _std(ty, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_mixsm_jerk_v090_signal(ncfcommon, ncfdiv):  # jerk deriv of v090 w=21d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = mix.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_mixdisp_jerk_v091_signal(ncfcommon, ncfdiv):  # jerk deriv of v091 w=42d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _std(mix, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_mixrank_jerk_v092_signal(ncfcommon, ncfdiv):  # jerk deriv of v092 w=63d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _rank(mix, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covmin_jerk_v093_signal(ncfdiv, fcf):  # jerk deriv of v093 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov.rolling(252, min_periods=84).min()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covdisp_jerk_v094_signal(ncfdiv, fcf):  # jerk deriv of v094 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _std(cov, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covrank_jerk_v095_signal(ncfdiv, fcf):  # jerk deriv of v095 w=63d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _rank(cov, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covaccel_jerk_v096_signal(ncfdiv, fcf):  # jerk deriv of v096 w=21d
    cov = _f42_div_cover(ncfdiv, fcf)
    sl = _slope(cov, 126)
    b = sl - sl.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retcovmin_jerk_v097_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v097 w=21d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret).rolling(63, min_periods=21).mean()
    b = cov - cov.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfpayoutsm_jerk_v098_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v098 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    pr = (ret / fcf.clip(lower=0).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = pr - pr.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfpayoutrank_jerk_v099_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v099 w=63d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    pr = ret / fcf.clip(lower=0).replace(0, np.nan)
    b = _rank(pr, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcfsm_jerk_v100_signal(ncfcommon, fcf):  # jerk deriv of v100 w=21d
    r = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    b = r.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbocfz2_jerk_v101_signal(ncfcommon, ncfo):  # jerk deriv of v101 w=42d
    r = (_f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = r - r.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divocfsm_jerk_v102_signal(ncfdiv, ncfo):  # jerk deriv of v102 w=42d
    r = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    b = r.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retocfrank_jerk_v103_signal(ncfcommon, ncfdiv, ncfo):  # jerk deriv of v103 w=63d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    r = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsaccel_jerk_v104_signal(dps):  # jerk deriv of v104 w=21d
    g = dps / dps.shift(126).replace(0, np.nan) - 1.0
    b = g - g.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsslope_jerk_v105_signal(dps):  # jerk deriv of v105 w=42d
    sm = dps.rolling(63, min_periods=21).mean()
    b = _slope(sm, 252) / sm.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsrank_jerk_v106_signal(dps):  # jerk deriv of v106 w=63d
    b = _rank(dps, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsdisp_jerk_v107_signal(dps):  # jerk deriv of v107 w=42d
    b = _std(dps, 252) / _mean(dps, 252).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsstag_jerk_v108_signal(dps):  # jerk deriv of v108 w=42d
    chg = (dps / dps.shift(21).replace(0, np.nan) - 1.0).abs()
    b = -chg.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsvsdiv_jerk_v109_signal(dps, ncfdiv):  # jerk deriv of v109 w=21d
    dg = dps / dps.shift(126).replace(0, np.nan) - 1.0
    cg = ncfdiv.abs() / ncfdiv.abs().shift(126).replace(0, np.nan) - 1.0
    b = dg - cg
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfyieldyr_jerk_v110_signal(fcf, marketcap):  # jerk deriv of v110 w=63d
    fy = (fcf / marketcap.replace(0, np.nan)).rolling(252, min_periods=84).mean()
    b = _z(fy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfymom_jerk_v111_signal(fcf, marketcap):  # jerk deriv of v111 w=21d
    fy = fcf / marketcap.replace(0, np.nan)
    b = fy - fy.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfyrank_jerk_v112_signal(fcf, marketcap):  # jerk deriv of v112 w=63d
    fy = fcf / marketcap.replace(0, np.nan)
    b = _rank(fy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfydisp_jerk_v113_signal(fcf, marketcap):  # jerk deriv of v113 w=42d
    fy = fcf / marketcap.replace(0, np.nan)
    b = _std(fy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_surplusrank_jerk_v114_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v114 w=42d
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(126, min_periods=42).mean()
    b = sm - sm.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_surplussm_jerk_v115_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v115 w=42d
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(63, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=84).median()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_overpayrank_jerk_v116_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v116 w=21d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    ratio = ret / fcf.clip(lower=0).replace(0, np.nan)
    b = np.tanh(ratio.rolling(63, min_periods=21).mean() - 1.0)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_overpaystreak_jerk_v117_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v117 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _std(ty - fy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfconvyr_jerk_v118_signal(fcf, ncfo):  # jerk deriv of v118 w=63d
    conv = (fcf / ncfo.replace(0, np.nan)).rolling(252, min_periods=84).mean()
    b = _z(conv, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfconvdisp_jerk_v119_signal(fcf, ncfo):  # jerk deriv of v119 w=42d
    conv = fcf / ncfo.replace(0, np.nan)
    b = _std(conv, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcfcorr_jerk_v120_signal(ncfcommon, fcf):  # jerk deriv of v120 w=42d
    bb = _f42_buyback(ncfcommon)
    b = bb.rolling(252, min_periods=84).corr(fcf)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divfcfcorr_jerk_v121_signal(ncfdiv, fcf):  # jerk deriv of v121 w=42d
    b = ncfdiv.abs().rolling(252, min_periods=84).corr(fcf)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_channelcorr_jerk_v122_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v122 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = by.rolling(252, min_periods=84).corr(dy)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_distribgrow_jerk_v123_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v123 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _slope(ty, 126) - _slope(fy, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcfinter_jerk_v124_signal(ncfcommon, fcf, marketcap):  # jerk deriv of v124 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = (fcf / marketcap.replace(0, np.nan)).clip(lower=0)
    b = by * fy
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_incomequalyr_jerk_v125_signal(ncfdiv, fcf, marketcap):  # jerk deriv of v125 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    cov = _f42_div_cover(ncfdiv, fcf).clip(lower=0)
    raw = dy * np.tanh(cov)
    b = raw.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbtimerank_jerk_v126_signal(ncfcommon, fcf, marketcap):  # jerk deriv of v126 w=63d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fyr = _rank(fcf / marketcap.replace(0, np.nan), 504)
    b = by * fyr
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retconsist_jerk_v127_signal(ncfcommon, ncfdiv):  # jerk deriv of v127 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = -_std(ret, 252) / _mean(ret, 252).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_payoutaccel_jerk_v128_signal(ncfcommon, ncfdiv):  # jerk deriv of v128 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    g = ret / ret.shift(252).replace(0, np.nan) - 1.0
    b = g - g.shift(126)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcfmom_jerk_v129_signal(ncfcommon, fcf):  # jerk deriv of v129 w=42d
    r = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divsharesm_jerk_v130_signal(ncfcommon, ncfdiv):  # jerk deriv of v130 w=21d
    dv = ncfdiv.abs()
    ret = (_f42_buyback(ncfcommon) + dv).replace(0, np.nan)
    share = dv / ret
    b = share.ewm(span=42, min_periods=21).mean() - share.ewm(span=189, min_periods=63).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshz_jerk_v131_signal(ncfcommon, marketcap):  # jerk deriv of v131 w=63d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _z(nsf, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshslope_jerk_v132_signal(ncfcommon, marketcap):  # jerk deriv of v132 w=21d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _slope(nsf, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshrank_jerk_v133_signal(ncfcommon, marketcap):  # jerk deriv of v133 w=42d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _std(nsf, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_capactlumpy_jerk_v134_signal(ncfcommon):  # jerk deriv of v134 w=42d
    iss = ncfcommon.clip(lower=0)
    bb = (-ncfcommon).clip(lower=0)
    b = _std(iss, 252) - _std(bb, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_extfundsm_jerk_v135_signal(ncfcommon, fcf):  # jerk deriv of v135 w=21d
    bb = _f42_buyback(ncfcommon)
    shortfall = np.tanh((bb - fcf.clip(lower=0)) / bb.replace(0, np.nan))
    b = shortfall.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_durablereturn_jerk_v136_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v136 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    mincov = (fcf / ret).rolling(252, min_periods=84).min().clip(lower=0)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(126, min_periods=42).mean()
    b = ty * np.tanh(mincov)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_safetydist_jerk_v137_signal(ncfdiv, fcf):  # jerk deriv of v137 w=21d
    cov = _f42_div_cover(ncfdiv, fcf)
    g = cov - 1.0
    b = np.sign(g) * np.sqrt(g.abs())
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_backedyield_jerk_v138_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v138 w=21d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    backed = pd.concat([ret, fcf.clip(lower=0)], axis=1).min(axis=1)
    b = backed / marketcap.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_unbacked_jerk_v139_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v139 w=21d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    unb = (ret - fcf.clip(lower=0)).clip(lower=0) / ret.replace(0, np.nan)
    b = unb
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tiltz_jerk_v140_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v140 w=42d
    tilt = (_f42_buyback(ncfcommon) - ncfdiv.abs()) / marketcap.replace(0, np.nan)
    b = _z(tilt, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_safetycomp_jerk_v141_signal(ncfcommon, ncfdiv, ncfo):  # jerk deriv of v141 w=10d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    ocfcov = np.tanh(ncfo.clip(lower=0) / ret - 1.0)
    bb = _f42_buyback(ncfcommon)
    bbshare = np.tanh(bb / ret - 0.5)
    b = ocfcov - bbshare
    result = b
    _d1 = (result - result.shift(10)) / 10.0
    result = (_d1 - _d1.shift(10)) / 10.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_annualcover_jerk_v142_signal(ncfcommon, ncfdiv, fcf):  # jerk deriv of v142 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).rolling(252, min_periods=84).sum()
    cash = fcf.rolling(252, min_periods=84).sum()
    cov = cash / ret.replace(0, np.nan)
    b = cov - cov.shift(126)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_channelratio_jerk_v143_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v143 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    dy = _f42_div_yield(ncfdiv, marketcap).replace(0, np.nan)
    r = np.log((by + 1e-6) / (dy + 1e-6))
    b = r.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divgrow_jerk_v144_signal(ncfdiv):  # jerk deriv of v144 w=42d
    dv = ncfdiv.abs()
    b = dv / dv.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbgrow_jerk_v145_signal(ncfcommon):  # jerk deriv of v145 w=42d
    bb = _f42_buyback(ncfcommon)
    bb_sm = bb.rolling(63, min_periods=21).mean()
    b = bb_sm / bb_sm.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_ocfgrow_jerk_v146_signal(ncfo, marketcap):  # jerk deriv of v146 w=42d
    fy = ncfo / marketcap.replace(0, np.nan)
    b = fy - fy.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_ocfcushion_jerk_v147_signal(ncfcommon, ncfdiv, ncfo):  # jerk deriv of v147 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    burden = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = 1.0 - burden.rolling(252, min_periods=84).max()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retbias_jerk_v148_signal(ncfcommon, ncfdiv, marketcap):  # jerk deriv of v148 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    divshare = dv / (bb + dv).replace(0, np.nan)
    raw = (ty * divshare).rolling(63, min_periods=21).mean()
    b = raw - raw.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covregdist_jerk_v149_signal(ncfdiv, fcf):  # jerk deriv of v149 w=63d
    cov = _f42_div_cover(ncfdiv, fcf)
    med = cov.rolling(504, min_periods=126).median()
    g = cov - med
    b = np.sign(g) * np.sqrt(g.abs())
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_crscore_jerk_v150_signal(ncfcommon, ncfdiv, fcf, marketcap):  # jerk deriv of v150 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(63, min_periods=21).mean()
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = np.tanh((fcf / ret).clip(lower=0))
    bb = _f42_buyback(ncfcommon)
    tilt = bb / ret
    b = ty * cov * (0.5 + tilt)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f42rb_f42_capital_return_buyback_byyield_jerk_v001_signal,
    f42rb_f42_capital_return_buyback_byyieldsm_jerk_v002_signal,
    f42rb_f42_capital_return_buyback_byyieldz_jerk_v003_signal,
    f42rb_f42_capital_return_buyback_byyieldrank_jerk_v004_signal,
    f42rb_f42_capital_return_buyback_netshflow_jerk_v005_signal,
    f42rb_f42_capital_return_buyback_issyield_jerk_v006_signal,
    f42rb_f42_capital_return_buyback_buybackbias_jerk_v007_signal,
    f42rb_f42_capital_return_buyback_divyield_jerk_v008_signal,
    f42rb_f42_capital_return_buyback_divyieldz_jerk_v009_signal,
    f42rb_f42_capital_return_buyback_divyieldrank_jerk_v010_signal,
    f42rb_f42_capital_return_buyback_totyield_jerk_v011_signal,
    f42rb_f42_capital_return_buyback_totyieldsm_jerk_v012_signal,
    f42rb_f42_capital_return_buyback_totyieldz_jerk_v013_signal,
    f42rb_f42_capital_return_buyback_returnmix_jerk_v014_signal,
    f42rb_f42_capital_return_buyback_divcover_jerk_v015_signal,
    f42rb_f42_capital_return_buyback_divcoversm_jerk_v016_signal,
    f42rb_f42_capital_return_buyback_divcoverz_jerk_v017_signal,
    f42rb_f42_capital_return_buyback_divpayout_jerk_v018_signal,
    f42rb_f42_capital_return_buyback_fcfpayout_jerk_v019_signal,
    f42rb_f42_capital_return_buyback_retcover_jerk_v020_signal,
    f42rb_f42_capital_return_buyback_bbfcf_jerk_v021_signal,
    f42rb_f42_capital_return_buyback_bbocf_jerk_v022_signal,
    f42rb_f42_capital_return_buyback_divocf_jerk_v023_signal,
    f42rb_f42_capital_return_buyback_retocf_jerk_v024_signal,
    f42rb_f42_capital_return_buyback_dpslevel_jerk_v025_signal,
    f42rb_f42_capital_return_buyback_dpsgrow_jerk_v026_signal,
    f42rb_f42_capital_return_buyback_dpsz_jerk_v027_signal,
    f42rb_f42_capital_return_buyback_dpshikefreq_jerk_v028_signal,
    f42rb_f42_capital_return_buyback_dpscut_jerk_v029_signal,
    f42rb_f42_capital_return_buyback_divreliance_jerk_v030_signal,
    f42rb_f42_capital_return_buyback_byaccel_jerk_v031_signal,
    f42rb_f42_capital_return_buyback_tymom_jerk_v032_signal,
    f42rb_f42_capital_return_buyback_dymom_jerk_v033_signal,
    f42rb_f42_capital_return_buyback_fcfyield_jerk_v034_signal,
    f42rb_f42_capital_return_buyback_fcfyieldz_jerk_v035_signal,
    f42rb_f42_capital_return_buyback_surplus_jerk_v036_signal,
    f42rb_f42_capital_return_buyback_fcfconv_jerk_v037_signal,
    f42rb_f42_capital_return_buyback_overpay_jerk_v038_signal,
    f42rb_f42_capital_return_buyback_sustdepth_jerk_v039_signal,
    f42rb_f42_capital_return_buyback_bbpersist_jerk_v040_signal,
    f42rb_f42_capital_return_buyback_covregime_jerk_v041_signal,
    f42rb_f42_capital_return_buyback_selffund_jerk_v042_signal,
    f42rb_f42_capital_return_buyback_tiltyield_jerk_v043_signal,
    f42rb_f42_capital_return_buyback_bydisp_jerk_v044_signal,
    f42rb_f42_capital_return_buyback_dystable_jerk_v045_signal,
    f42rb_f42_capital_return_buyback_tysmooth_jerk_v046_signal,
    f42rb_f42_capital_return_buyback_bbocfz_jerk_v047_signal,
    f42rb_f42_capital_return_buyback_hikefund_jerk_v048_signal,
    f42rb_f42_capital_return_buyback_byfcfratio_jerk_v049_signal,
    f42rb_f42_capital_return_buyback_mixmom_jerk_v050_signal,
    f42rb_f42_capital_return_buyback_tyrank_jerk_v051_signal,
    f42rb_f42_capital_return_buyback_bbperdiv_jerk_v052_signal,
    f42rb_f42_capital_return_buyback_bbheadroom_jerk_v053_signal,
    f42rb_f42_capital_return_buyback_burdenz_jerk_v054_signal,
    f42rb_f42_capital_return_buyback_covtrend_jerk_v055_signal,
    f42rb_f42_capital_return_buyback_bytrend_jerk_v056_signal,
    f42rb_f42_capital_return_buyback_distribrank_jerk_v057_signal,
    f42rb_f42_capital_return_buyback_incomequal_jerk_v058_signal,
    f42rb_f42_capital_return_buyback_bbqual_jerk_v059_signal,
    f42rb_f42_capital_return_buyback_retscore_jerk_v060_signal,
    f42rb_f42_capital_return_buyback_dilregime_jerk_v061_signal,
    f42rb_f42_capital_return_buyback_payeridentity_jerk_v062_signal,
    f42rb_f42_capital_return_buyback_intensz_jerk_v063_signal,
    f42rb_f42_capital_return_buyback_bbstress_jerk_v064_signal,
    f42rb_f42_capital_return_buyback_incomevsbb_jerk_v065_signal,
    f42rb_f42_capital_return_buyback_divocfz_jerk_v066_signal,
    f42rb_f42_capital_return_buyback_warchest_jerk_v067_signal,
    f42rb_f42_capital_return_buyback_payoutgrow_jerk_v068_signal,
    f42rb_f42_capital_return_buyback_bbtiming_jerk_v069_signal,
    f42rb_f42_capital_return_buyback_covimprove_jerk_v070_signal,
    f42rb_f42_capital_return_buyback_netshdisp_jerk_v071_signal,
    f42rb_f42_capital_return_buyback_cyclicality_jerk_v072_signal,
    f42rb_f42_capital_return_buyback_dyfcfshare_jerk_v073_signal,
    f42rb_f42_capital_return_buyback_bbsignmag_jerk_v074_signal,
    f42rb_f42_capital_return_buyback_durability_jerk_v075_signal,
    f42rb_f42_capital_return_buyback_byyieldyr_jerk_v076_signal,
    f42rb_f42_capital_return_buyback_byaccel2_jerk_v077_signal,
    f42rb_f42_capital_return_buyback_bycurv_jerk_v078_signal,
    f42rb_f42_capital_return_buyback_bbcumyield_jerk_v079_signal,
    f42rb_f42_capital_return_buyback_byskew_jerk_v080_signal,
    f42rb_f42_capital_return_buyback_divyieldyr_jerk_v081_signal,
    f42rb_f42_capital_return_buyback_dyaccel_jerk_v082_signal,
    f42rb_f42_capital_return_buyback_dycurv_jerk_v083_signal,
    f42rb_f42_capital_return_buyback_divcumyield_jerk_v084_signal,
    f42rb_f42_capital_return_buyback_dydisp_jerk_v085_signal,
    f42rb_f42_capital_return_buyback_tyyrz_jerk_v086_signal,
    f42rb_f42_capital_return_buyback_tyaccel_jerk_v087_signal,
    f42rb_f42_capital_return_buyback_tycumyield_jerk_v088_signal,
    f42rb_f42_capital_return_buyback_tydisp_jerk_v089_signal,
    f42rb_f42_capital_return_buyback_mixsm_jerk_v090_signal,
    f42rb_f42_capital_return_buyback_mixdisp_jerk_v091_signal,
    f42rb_f42_capital_return_buyback_mixrank_jerk_v092_signal,
    f42rb_f42_capital_return_buyback_covmin_jerk_v093_signal,
    f42rb_f42_capital_return_buyback_covdisp_jerk_v094_signal,
    f42rb_f42_capital_return_buyback_covrank_jerk_v095_signal,
    f42rb_f42_capital_return_buyback_covaccel_jerk_v096_signal,
    f42rb_f42_capital_return_buyback_retcovmin_jerk_v097_signal,
    f42rb_f42_capital_return_buyback_fcfpayoutsm_jerk_v098_signal,
    f42rb_f42_capital_return_buyback_fcfpayoutrank_jerk_v099_signal,
    f42rb_f42_capital_return_buyback_bbfcfsm_jerk_v100_signal,
    f42rb_f42_capital_return_buyback_bbocfz2_jerk_v101_signal,
    f42rb_f42_capital_return_buyback_divocfsm_jerk_v102_signal,
    f42rb_f42_capital_return_buyback_retocfrank_jerk_v103_signal,
    f42rb_f42_capital_return_buyback_dpsaccel_jerk_v104_signal,
    f42rb_f42_capital_return_buyback_dpsslope_jerk_v105_signal,
    f42rb_f42_capital_return_buyback_dpsrank_jerk_v106_signal,
    f42rb_f42_capital_return_buyback_dpsdisp_jerk_v107_signal,
    f42rb_f42_capital_return_buyback_dpsstag_jerk_v108_signal,
    f42rb_f42_capital_return_buyback_dpsvsdiv_jerk_v109_signal,
    f42rb_f42_capital_return_buyback_fcfyieldyr_jerk_v110_signal,
    f42rb_f42_capital_return_buyback_fcfymom_jerk_v111_signal,
    f42rb_f42_capital_return_buyback_fcfyrank_jerk_v112_signal,
    f42rb_f42_capital_return_buyback_fcfydisp_jerk_v113_signal,
    f42rb_f42_capital_return_buyback_surplusrank_jerk_v114_signal,
    f42rb_f42_capital_return_buyback_surplussm_jerk_v115_signal,
    f42rb_f42_capital_return_buyback_overpayrank_jerk_v116_signal,
    f42rb_f42_capital_return_buyback_overpaystreak_jerk_v117_signal,
    f42rb_f42_capital_return_buyback_fcfconvyr_jerk_v118_signal,
    f42rb_f42_capital_return_buyback_fcfconvdisp_jerk_v119_signal,
    f42rb_f42_capital_return_buyback_bbfcfcorr_jerk_v120_signal,
    f42rb_f42_capital_return_buyback_divfcfcorr_jerk_v121_signal,
    f42rb_f42_capital_return_buyback_channelcorr_jerk_v122_signal,
    f42rb_f42_capital_return_buyback_distribgrow_jerk_v123_signal,
    f42rb_f42_capital_return_buyback_bbfcfinter_jerk_v124_signal,
    f42rb_f42_capital_return_buyback_incomequalyr_jerk_v125_signal,
    f42rb_f42_capital_return_buyback_bbtimerank_jerk_v126_signal,
    f42rb_f42_capital_return_buyback_retconsist_jerk_v127_signal,
    f42rb_f42_capital_return_buyback_payoutaccel_jerk_v128_signal,
    f42rb_f42_capital_return_buyback_bbfcfmom_jerk_v129_signal,
    f42rb_f42_capital_return_buyback_divsharesm_jerk_v130_signal,
    f42rb_f42_capital_return_buyback_netshz_jerk_v131_signal,
    f42rb_f42_capital_return_buyback_netshslope_jerk_v132_signal,
    f42rb_f42_capital_return_buyback_netshrank_jerk_v133_signal,
    f42rb_f42_capital_return_buyback_capactlumpy_jerk_v134_signal,
    f42rb_f42_capital_return_buyback_extfundsm_jerk_v135_signal,
    f42rb_f42_capital_return_buyback_durablereturn_jerk_v136_signal,
    f42rb_f42_capital_return_buyback_safetydist_jerk_v137_signal,
    f42rb_f42_capital_return_buyback_backedyield_jerk_v138_signal,
    f42rb_f42_capital_return_buyback_unbacked_jerk_v139_signal,
    f42rb_f42_capital_return_buyback_tiltz_jerk_v140_signal,
    f42rb_f42_capital_return_buyback_safetycomp_jerk_v141_signal,
    f42rb_f42_capital_return_buyback_annualcover_jerk_v142_signal,
    f42rb_f42_capital_return_buyback_channelratio_jerk_v143_signal,
    f42rb_f42_capital_return_buyback_divgrow_jerk_v144_signal,
    f42rb_f42_capital_return_buyback_bbgrow_jerk_v145_signal,
    f42rb_f42_capital_return_buyback_ocfgrow_jerk_v146_signal,
    f42rb_f42_capital_return_buyback_ocfcushion_jerk_v147_signal,
    f42rb_f42_capital_return_buyback_retbias_jerk_v148_signal,
    f42rb_f42_capital_return_buyback_covregdist_jerk_v149_signal,
    f42rb_f42_capital_return_buyback_crscore_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_CAPITAL_RETURN_BUYBACK_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    s = s * (1.0 + g.normal(0.0, 0.04, n))
    if allow_neg:
        s = s - base * 0.6
    return pd.Series(s, name=None)


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
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    _bb_mag = _fund(101, base=7e7, drift=0.005, vol=0.18)
    _iss_mag = _fund(111, base=6.5e7, drift=-0.01, vol=0.30)
    ncfcommon = (_iss_mag - _bb_mag).rename("ncfcommon")
    ncfdiv = _fund(102, base=6e7, drift=0.02, vol=0.11).rename("ncfdiv")
    dps = _fund(103, base=0.4, drift=0.015, vol=0.05).rename("dps")
    fcf = _fund(104, base=1.2e8, drift=0.025, vol=0.1, allow_neg=True).rename("fcf")
    ncfo = _fund(105, base=1.6e8, drift=0.025, vol=0.09, allow_neg=True).rename("ncfo")
    marketcap = _fund(106, base=2.5e9, drift=0.02, vol=0.06).rename("marketcap")

    cols = {"ncfcommon": ncfcommon, "ncfdiv": ncfdiv, "dps": dps,
            "fcf": fcf, "ncfo": ncfo, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f42_capital_return_buyback_3rd_derivatives_001_150_claude: %d features pass" % n_features)
