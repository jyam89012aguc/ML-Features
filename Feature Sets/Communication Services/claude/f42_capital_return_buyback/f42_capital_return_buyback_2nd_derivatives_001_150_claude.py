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



def f42rb_f42_capital_return_buyback_byyield_slope_v001_signal(ncfcommon, marketcap):  # slope deriv of v001 w=21d
    b = _f42_buyback_yield(ncfcommon, marketcap)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byyieldsm_slope_v002_signal(ncfcommon, marketcap):  # slope deriv of v002 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by.rolling(63, min_periods=21).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byyieldz_slope_v003_signal(ncfcommon, marketcap):  # slope deriv of v003 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _z(by, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byyieldrank_slope_v004_signal(ncfcommon, marketcap):  # slope deriv of v004 w=63d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _rank(by, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshflow_slope_v005_signal(ncfcommon, marketcap):  # slope deriv of v005 w=42d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = nsf - nsf.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_issyield_slope_v006_signal(ncfcommon, marketcap):  # slope deriv of v006 w=21d
    b = _f42_issuance(ncfcommon) / marketcap.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_buybackbias_slope_v007_signal(ncfcommon):  # slope deriv of v007 w=21d
    net = (-ncfcommon).rolling(63, min_periods=21).sum()
    gross = ncfcommon.abs().rolling(63, min_periods=21).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divyield_slope_v008_signal(ncfdiv, marketcap):  # slope deriv of v008 w=21d
    b = _f42_div_yield(ncfdiv, marketcap)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divyieldz_slope_v009_signal(ncfdiv, marketcap):  # slope deriv of v009 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _z(dy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divyieldrank_slope_v010_signal(ncfdiv, marketcap):  # slope deriv of v010 w=63d
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _rank(dy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_totyield_slope_v011_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v011 w=21d
    b = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_totyieldsm_slope_v012_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v012 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_totyieldz_slope_v013_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v013 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _z(ty, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_returnmix_slope_v014_signal(ncfcommon, ncfdiv):  # slope deriv of v014 w=21d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    b = (bb - dv) / (bb + dv).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divcover_slope_v015_signal(ncfdiv, fcf):  # slope deriv of v015 w=21d
    b = _f42_div_cover(ncfdiv, fcf)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divcoversm_slope_v016_signal(ncfdiv, fcf):  # slope deriv of v016 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divcoverz_slope_v017_signal(ncfdiv, fcf):  # slope deriv of v017 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _z(cov, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divpayout_slope_v018_signal(ncfdiv, fcf):  # slope deriv of v018 w=21d
    b = ncfdiv.abs() / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfpayout_slope_v019_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v019 w=21d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = ret / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retcover_slope_v020_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v020 w=21d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    b = fcf / ret
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcf_slope_v021_signal(ncfcommon, fcf):  # slope deriv of v021 w=21d
    b = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbocf_slope_v022_signal(ncfcommon, ncfo):  # slope deriv of v022 w=21d
    b = _f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divocf_slope_v023_signal(ncfdiv, ncfo):  # slope deriv of v023 w=21d
    b = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retocf_slope_v024_signal(ncfcommon, ncfdiv, ncfo):  # slope deriv of v024 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = ncfo.clip(lower=0) / ret
    b = cov - cov.rolling(252, min_periods=84).median()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpslevel_slope_v025_signal(dps):  # slope deriv of v025 w=21d
    fast = dps.ewm(span=42, min_periods=21).mean()
    slow = dps.ewm(span=189, min_periods=63).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsgrow_slope_v026_signal(dps):  # slope deriv of v026 w=42d
    b = dps / dps.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsz_slope_v027_signal(dps):  # slope deriv of v027 w=42d
    b = _z(dps, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpshikefreq_slope_v028_signal(dps):  # slope deriv of v028 w=42d
    up = (dps > dps.shift(21)).astype(float)
    b = up.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpscut_slope_v029_signal(dps):  # slope deriv of v029 w=42d
    peak = dps.rolling(252, min_periods=84).max()
    b = dps / peak.replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divreliance_slope_v030_signal(ncfdiv, ncfcommon, marketcap):  # slope deriv of v030 w=21d
    dy = _f42_div_yield(ncfdiv, marketcap)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).replace(0, np.nan)
    share = dy / ty
    b = _slope(share, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byaccel_slope_v031_signal(ncfcommon, marketcap):  # slope deriv of v031 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by - by.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tymom_slope_v032_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v032 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty - ty.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dymom_slope_v033_signal(ncfdiv, marketcap):  # slope deriv of v033 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = dy - dy.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfyield_slope_v034_signal(fcf, marketcap):  # slope deriv of v034 w=21d
    b = fcf / marketcap.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfyieldz_slope_v035_signal(fcf, marketcap):  # slope deriv of v035 w=42d
    fy = fcf / marketcap.replace(0, np.nan)
    b = _z(fy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_surplus_slope_v036_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v036 w=42d
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    b = surplus - surplus.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfconv_slope_v037_signal(fcf, ncfo):  # slope deriv of v037 w=42d
    conv = fcf / ncfo.replace(0, np.nan)
    b = _z(conv, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_overpay_slope_v038_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v038 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    gap = ty - fy
    b = gap - gap.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_sustdepth_slope_v039_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v039 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    margin = (fcf - ret) / ret.replace(0, np.nan)
    b = _z(margin, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbpersist_slope_v040_signal(ncfcommon):  # slope deriv of v040 w=42d
    isbb = (-ncfcommon > 0).astype(float)
    b = isbb.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covregime_slope_v041_signal(ncfdiv, fcf):  # slope deriv of v041 w=63d
    cov = _f42_div_cover(ncfdiv, fcf)
    med = cov.rolling(504, min_periods=126).median()
    ok = (cov > med).astype(float)
    b = ok.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_selffund_slope_v042_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v042 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    margin = np.tanh((fcf - ret) / ret.replace(0, np.nan))
    b = margin.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tiltyield_slope_v043_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v043 w=21d
    b = (_f42_buyback(ncfcommon) - ncfdiv.abs()) / marketcap.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bydisp_slope_v044_signal(ncfcommon, marketcap):  # slope deriv of v044 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _std(by, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dystable_slope_v045_signal(ncfdiv, marketcap):  # slope deriv of v045 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    m = _mean(dy, 252)
    sd = _std(dy, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tysmooth_slope_v046_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v046 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = -_std(ty, 126) / _mean(ty, 126).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbocfz_slope_v047_signal(ncfcommon, ncfo):  # slope deriv of v047 w=42d
    r = _f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_hikefund_slope_v048_signal(dps, fcf):  # slope deriv of v048 w=42d
    dg = dps / dps.shift(252).replace(0, np.nan) - 1.0
    fg = fcf / fcf.shift(252).replace(0, np.nan) - 1.0
    b = dg - fg
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byfcfratio_slope_v049_signal(ncfcommon, fcf, marketcap):  # slope deriv of v049 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = (fcf / marketcap.replace(0, np.nan)).replace(0, np.nan)
    b = _z(by / fy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_mixmom_slope_v050_signal(ncfcommon, ncfdiv):  # slope deriv of v050 w=42d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _z(mix, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tyrank_slope_v051_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v051 w=63d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _rank(ty, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbperdiv_slope_v052_signal(ncfcommon, ncfdiv):  # slope deriv of v052 w=42d
    bb_sum = _f42_buyback(ncfcommon).rolling(252, min_periods=84).sum()
    dv_sum = ncfdiv.abs().rolling(252, min_periods=84).sum()
    b = np.log((bb_sum + 1.0) / (dv_sum + 1.0).replace(0, np.nan))
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbheadroom_slope_v053_signal(fcf, ncfdiv, marketcap):  # slope deriv of v053 w=63d
    fy = fcf / marketcap.replace(0, np.nan)
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _rank(fy - dy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_burdenz_slope_v054_signal(ncfcommon, ncfdiv, ncfo):  # slope deriv of v054 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    r = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covtrend_slope_v055_signal(ncfdiv, fcf):  # slope deriv of v055 w=21d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _slope(cov, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bytrend_slope_v056_signal(ncfcommon, marketcap):  # slope deriv of v056 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _slope(by, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_distribrank_slope_v057_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v057 w=63d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _rank(ty - fy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_incomequal_slope_v058_signal(ncfdiv, fcf, marketcap):  # slope deriv of v058 w=21d
    dy = _f42_div_yield(ncfdiv, marketcap)
    cov = _f42_div_cover(ncfdiv, fcf).clip(lower=0)
    b = dy * np.tanh(cov)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbqual_slope_v059_signal(ncfcommon, fcf, marketcap):  # slope deriv of v059 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fund = (fcf / _f42_buyback(ncfcommon).replace(0, np.nan)).clip(0, 3)
    b = by * fund
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retscore_slope_v060_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v060 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret).clip(lower=0)
    b = ty * np.tanh(cov)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dilregime_slope_v061_signal(ncfcommon):  # slope deriv of v061 w=42d
    iss = ncfcommon.clip(lower=0)
    disp = _std(iss, 252) / (_mean(iss, 252).replace(0, np.nan))
    b = disp
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_payeridentity_slope_v062_signal(dps, ncfdiv, marketcap):  # slope deriv of v062 w=42d
    dg = (dps / dps.shift(63).replace(0, np.nan) - 1.0)
    dvy = _f42_div_yield(ncfdiv, marketcap)
    b = dg.rolling(252, min_periods=84).corr(dvy)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_intensz_slope_v063_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v063 w=63d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _z(ty, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbstress_slope_v064_signal(ncfcommon, fcf, marketcap):  # slope deriv of v064 w=21d
    bb = _f42_buyback(ncfcommon)
    shortfall = (bb - fcf.clip(lower=0)) / bb.replace(0, np.nan)
    b = np.tanh(shortfall)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_incomevsbb_slope_v065_signal(dps, ncfcommon, marketcap):  # slope deriv of v065 w=21d
    dg = (dps / dps.shift(126).replace(0, np.nan) - 1.0).clip(lower=0)
    by = _f42_buyback_yield(ncfcommon, marketcap).rolling(63, min_periods=21).mean()
    b = np.tanh(dg) - np.tanh(80.0 * by)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divocfz_slope_v066_signal(ncfdiv, ncfo):  # slope deriv of v066 w=42d
    r = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_warchest_slope_v067_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v067 w=42d
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(63, min_periods=21).mean()
    b = _z(sm, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_payoutgrow_slope_v068_signal(ncfcommon, ncfdiv):  # slope deriv of v068 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = ret / ret.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbtiming_slope_v069_signal(ncfcommon, fcf, marketcap):  # slope deriv of v069 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = by * np.sign(fy) * np.sqrt(fy.abs())
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covimprove_slope_v070_signal(ncfdiv, fcf):  # slope deriv of v070 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov - cov.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshdisp_slope_v071_signal(ncfcommon, marketcap):  # slope deriv of v071 w=42d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = nsf.ewm(span=63, min_periods=21).mean() - nsf.ewm(span=252, min_periods=63).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_cyclicality_slope_v072_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v072 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = ty.rolling(252, min_periods=84).corr(fy)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dyfcfshare_slope_v073_signal(ncfdiv, ncfo):  # slope deriv of v073 w=42d
    dg = ncfdiv.abs() / ncfdiv.abs().shift(252).replace(0, np.nan) - 1.0
    og = ncfo / ncfo.shift(252).replace(0, np.nan) - 1.0
    b = dg - og
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbsignmag_slope_v074_signal(ncfcommon, marketcap):  # slope deriv of v074 w=42d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    typ = nsf.rolling(252, min_periods=84).mean()
    b = np.sign(nsf) * np.sqrt(nsf.abs()) - np.sign(typ) * np.sqrt(typ.abs())
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_durability_slope_v075_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v075 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret)
    mincov = cov.rolling(252, min_periods=84).min().clip(lower=0)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty * np.tanh(mincov)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byyieldyr_slope_v076_signal(ncfcommon, marketcap):  # slope deriv of v076 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byaccel2_slope_v077_signal(ncfcommon, marketcap):  # slope deriv of v077 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap).rolling(63, min_periods=21).mean()
    b = by - by.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bycurv_slope_v078_signal(ncfcommon, marketcap):  # slope deriv of v078 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    d = by - by.shift(63)
    b = d - d.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbcumyield_slope_v079_signal(ncfcommon):  # slope deriv of v079 w=42d
    bb = _f42_buyback(ncfcommon).rolling(252, min_periods=84).sum()
    b = bb / bb.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_byskew_slope_v080_signal(ncfcommon, marketcap):  # slope deriv of v080 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    typ = by.rolling(252, min_periods=84).median()
    b = np.sqrt(by) - np.sqrt(typ.clip(lower=0))
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divyieldyr_slope_v081_signal(ncfdiv, marketcap):  # slope deriv of v081 w=63d
    dy = _f42_div_yield(ncfdiv, marketcap).rolling(252, min_periods=84).mean()
    b = _z(dy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dyaccel_slope_v082_signal(ncfdiv, marketcap):  # slope deriv of v082 w=21d
    dy = _f42_div_yield(ncfdiv, marketcap).rolling(63, min_periods=21).mean()
    b = dy - dy.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dycurv_slope_v083_signal(ncfdiv, marketcap):  # slope deriv of v083 w=21d
    dy = _f42_div_yield(ncfdiv, marketcap)
    d = dy - dy.shift(63)
    b = d - d.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divcumyield_slope_v084_signal(ncfdiv, marketcap):  # slope deriv of v084 w=42d
    dv = ncfdiv.abs().rolling(252, min_periods=84).sum()
    cy = dv / (marketcap * 4.0).replace(0, np.nan)
    b = _z(cy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dydisp_slope_v085_signal(ncfdiv, marketcap):  # slope deriv of v085 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _std(dy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tyyrz_slope_v086_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v086 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(252, min_periods=84).mean()
    b = ty / ty.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tyaccel_slope_v087_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v087 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    d = ty - ty.shift(63)
    b = d - d.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tycumyield_slope_v088_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v088 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).rolling(252, min_periods=84).sum()
    b = ret / (marketcap * 4.0).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tydisp_slope_v089_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v089 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _std(ty, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_mixsm_slope_v090_signal(ncfcommon, ncfdiv):  # slope deriv of v090 w=21d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = mix.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_mixdisp_slope_v091_signal(ncfcommon, ncfdiv):  # slope deriv of v091 w=42d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _std(mix, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_mixrank_slope_v092_signal(ncfcommon, ncfdiv):  # slope deriv of v092 w=63d
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _rank(mix, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covmin_slope_v093_signal(ncfdiv, fcf):  # slope deriv of v093 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov.rolling(252, min_periods=84).min()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covdisp_slope_v094_signal(ncfdiv, fcf):  # slope deriv of v094 w=42d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _std(cov, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covrank_slope_v095_signal(ncfdiv, fcf):  # slope deriv of v095 w=63d
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _rank(cov, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covaccel_slope_v096_signal(ncfdiv, fcf):  # slope deriv of v096 w=21d
    cov = _f42_div_cover(ncfdiv, fcf)
    sl = _slope(cov, 126)
    b = sl - sl.shift(63)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retcovmin_slope_v097_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v097 w=21d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret).rolling(63, min_periods=21).mean()
    b = cov - cov.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfpayoutsm_slope_v098_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v098 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    pr = (ret / fcf.clip(lower=0).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = pr - pr.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfpayoutrank_slope_v099_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v099 w=63d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    pr = ret / fcf.clip(lower=0).replace(0, np.nan)
    b = _rank(pr, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcfsm_slope_v100_signal(ncfcommon, fcf):  # slope deriv of v100 w=21d
    r = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    b = r.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbocfz2_slope_v101_signal(ncfcommon, ncfo):  # slope deriv of v101 w=42d
    r = (_f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = r - r.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divocfsm_slope_v102_signal(ncfdiv, ncfo):  # slope deriv of v102 w=42d
    r = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    b = r.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retocfrank_slope_v103_signal(ncfcommon, ncfdiv, ncfo):  # slope deriv of v103 w=63d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    r = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsaccel_slope_v104_signal(dps):  # slope deriv of v104 w=21d
    g = dps / dps.shift(126).replace(0, np.nan) - 1.0
    b = g - g.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsslope_slope_v105_signal(dps):  # slope deriv of v105 w=42d
    sm = dps.rolling(63, min_periods=21).mean()
    b = _slope(sm, 252) / sm.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsrank_slope_v106_signal(dps):  # slope deriv of v106 w=63d
    b = _rank(dps, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsdisp_slope_v107_signal(dps):  # slope deriv of v107 w=42d
    b = _std(dps, 252) / _mean(dps, 252).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsstag_slope_v108_signal(dps):  # slope deriv of v108 w=42d
    chg = (dps / dps.shift(21).replace(0, np.nan) - 1.0).abs()
    b = -chg.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_dpsvsdiv_slope_v109_signal(dps, ncfdiv):  # slope deriv of v109 w=21d
    dg = dps / dps.shift(126).replace(0, np.nan) - 1.0
    cg = ncfdiv.abs() / ncfdiv.abs().shift(126).replace(0, np.nan) - 1.0
    b = dg - cg
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfyieldyr_slope_v110_signal(fcf, marketcap):  # slope deriv of v110 w=63d
    fy = (fcf / marketcap.replace(0, np.nan)).rolling(252, min_periods=84).mean()
    b = _z(fy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfymom_slope_v111_signal(fcf, marketcap):  # slope deriv of v111 w=21d
    fy = fcf / marketcap.replace(0, np.nan)
    b = fy - fy.shift(126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfyrank_slope_v112_signal(fcf, marketcap):  # slope deriv of v112 w=63d
    fy = fcf / marketcap.replace(0, np.nan)
    b = _rank(fy, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfydisp_slope_v113_signal(fcf, marketcap):  # slope deriv of v113 w=42d
    fy = fcf / marketcap.replace(0, np.nan)
    b = _std(fy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_surplusrank_slope_v114_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v114 w=42d
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(126, min_periods=42).mean()
    b = sm - sm.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_surplussm_slope_v115_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v115 w=42d
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(63, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=84).median()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_overpayrank_slope_v116_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v116 w=21d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    ratio = ret / fcf.clip(lower=0).replace(0, np.nan)
    b = np.tanh(ratio.rolling(63, min_periods=21).mean() - 1.0)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_overpaystreak_slope_v117_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v117 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _std(ty - fy, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfconvyr_slope_v118_signal(fcf, ncfo):  # slope deriv of v118 w=63d
    conv = (fcf / ncfo.replace(0, np.nan)).rolling(252, min_periods=84).mean()
    b = _z(conv, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_fcfconvdisp_slope_v119_signal(fcf, ncfo):  # slope deriv of v119 w=42d
    conv = fcf / ncfo.replace(0, np.nan)
    b = _std(conv, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcfcorr_slope_v120_signal(ncfcommon, fcf):  # slope deriv of v120 w=42d
    bb = _f42_buyback(ncfcommon)
    b = bb.rolling(252, min_periods=84).corr(fcf)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divfcfcorr_slope_v121_signal(ncfdiv, fcf):  # slope deriv of v121 w=42d
    b = ncfdiv.abs().rolling(252, min_periods=84).corr(fcf)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_channelcorr_slope_v122_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v122 w=42d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = by.rolling(252, min_periods=84).corr(dy)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_distribgrow_slope_v123_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v123 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _slope(ty, 126) - _slope(fy, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcfinter_slope_v124_signal(ncfcommon, fcf, marketcap):  # slope deriv of v124 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = (fcf / marketcap.replace(0, np.nan)).clip(lower=0)
    b = by * fy
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_incomequalyr_slope_v125_signal(ncfdiv, fcf, marketcap):  # slope deriv of v125 w=42d
    dy = _f42_div_yield(ncfdiv, marketcap)
    cov = _f42_div_cover(ncfdiv, fcf).clip(lower=0)
    raw = dy * np.tanh(cov)
    b = raw.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbtimerank_slope_v126_signal(ncfcommon, fcf, marketcap):  # slope deriv of v126 w=63d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fyr = _rank(fcf / marketcap.replace(0, np.nan), 504)
    b = by * fyr
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retconsist_slope_v127_signal(ncfcommon, ncfdiv):  # slope deriv of v127 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = -_std(ret, 252) / _mean(ret, 252).replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_payoutaccel_slope_v128_signal(ncfcommon, ncfdiv):  # slope deriv of v128 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    g = ret / ret.shift(252).replace(0, np.nan) - 1.0
    b = g - g.shift(126)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbfcfmom_slope_v129_signal(ncfcommon, fcf):  # slope deriv of v129 w=42d
    r = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divsharesm_slope_v130_signal(ncfcommon, ncfdiv):  # slope deriv of v130 w=21d
    dv = ncfdiv.abs()
    ret = (_f42_buyback(ncfcommon) + dv).replace(0, np.nan)
    share = dv / ret
    b = share.ewm(span=42, min_periods=21).mean() - share.ewm(span=189, min_periods=63).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshz_slope_v131_signal(ncfcommon, marketcap):  # slope deriv of v131 w=63d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _z(nsf, 504)
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshslope_slope_v132_signal(ncfcommon, marketcap):  # slope deriv of v132 w=21d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _slope(nsf, 126)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_netshrank_slope_v133_signal(ncfcommon, marketcap):  # slope deriv of v133 w=42d
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _std(nsf, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_capactlumpy_slope_v134_signal(ncfcommon):  # slope deriv of v134 w=42d
    iss = ncfcommon.clip(lower=0)
    bb = (-ncfcommon).clip(lower=0)
    b = _std(iss, 252) - _std(bb, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_extfundsm_slope_v135_signal(ncfcommon, fcf):  # slope deriv of v135 w=21d
    bb = _f42_buyback(ncfcommon)
    shortfall = np.tanh((bb - fcf.clip(lower=0)) / bb.replace(0, np.nan))
    b = shortfall.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_durablereturn_slope_v136_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v136 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    mincov = (fcf / ret).rolling(252, min_periods=84).min().clip(lower=0)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(126, min_periods=42).mean()
    b = ty * np.tanh(mincov)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_safetydist_slope_v137_signal(ncfdiv, fcf):  # slope deriv of v137 w=21d
    cov = _f42_div_cover(ncfdiv, fcf)
    g = cov - 1.0
    b = np.sign(g) * np.sqrt(g.abs())
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_backedyield_slope_v138_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v138 w=21d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    backed = pd.concat([ret, fcf.clip(lower=0)], axis=1).min(axis=1)
    b = backed / marketcap.replace(0, np.nan)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_unbacked_slope_v139_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v139 w=21d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    unb = (ret - fcf.clip(lower=0)).clip(lower=0) / ret.replace(0, np.nan)
    b = unb
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_tiltz_slope_v140_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v140 w=42d
    tilt = (_f42_buyback(ncfcommon) - ncfdiv.abs()) / marketcap.replace(0, np.nan)
    b = _z(tilt, 252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_safetycomp_slope_v141_signal(ncfcommon, ncfdiv, ncfo):  # slope deriv of v141 w=10d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    ocfcov = np.tanh(ncfo.clip(lower=0) / ret - 1.0)
    bb = _f42_buyback(ncfcommon)
    bbshare = np.tanh(bb / ret - 0.5)
    b = ocfcov - bbshare
    result = b
    _d1 = (result - result.shift(10)) / 10.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_annualcover_slope_v142_signal(ncfcommon, ncfdiv, fcf):  # slope deriv of v142 w=42d
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).rolling(252, min_periods=84).sum()
    cash = fcf.rolling(252, min_periods=84).sum()
    cov = cash / ret.replace(0, np.nan)
    b = cov - cov.shift(126)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_channelratio_slope_v143_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v143 w=21d
    by = _f42_buyback_yield(ncfcommon, marketcap)
    dy = _f42_div_yield(ncfdiv, marketcap).replace(0, np.nan)
    r = np.log((by + 1e-6) / (dy + 1e-6))
    b = r.rolling(126, min_periods=42).mean()
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_divgrow_slope_v144_signal(ncfdiv):  # slope deriv of v144 w=42d
    dv = ncfdiv.abs()
    b = dv / dv.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_bbgrow_slope_v145_signal(ncfcommon):  # slope deriv of v145 w=42d
    bb = _f42_buyback(ncfcommon)
    bb_sm = bb.rolling(63, min_periods=21).mean()
    b = bb_sm / bb_sm.shift(252).replace(0, np.nan) - 1.0
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_ocfgrow_slope_v146_signal(ncfo, marketcap):  # slope deriv of v146 w=42d
    fy = ncfo / marketcap.replace(0, np.nan)
    b = fy - fy.shift(252)
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_ocfcushion_slope_v147_signal(ncfcommon, ncfdiv, ncfo):  # slope deriv of v147 w=42d
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    burden = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = 1.0 - burden.rolling(252, min_periods=84).max()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_retbias_slope_v148_signal(ncfcommon, ncfdiv, marketcap):  # slope deriv of v148 w=42d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    divshare = dv / (bb + dv).replace(0, np.nan)
    raw = (ty * divshare).rolling(63, min_periods=21).mean()
    b = raw - raw.rolling(252, min_periods=84).mean()
    result = b
    _d1 = (result - result.shift(42)) / 42.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_covregdist_slope_v149_signal(ncfdiv, fcf):  # slope deriv of v149 w=63d
    cov = _f42_div_cover(ncfdiv, fcf)
    med = cov.rolling(504, min_periods=126).median()
    g = cov - med
    b = np.sign(g) * np.sqrt(g.abs())
    result = b
    _d1 = (result - result.shift(63)) / 63.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

def f42rb_f42_capital_return_buyback_crscore_slope_v150_signal(ncfcommon, ncfdiv, fcf, marketcap):  # slope deriv of v150 w=21d
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(63, min_periods=21).mean()
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = np.tanh((fcf / ret).clip(lower=0))
    bb = _f42_buyback(ncfcommon)
    tilt = bb / ret
    b = ty * cov * (0.5 + tilt)
    result = b
    _d1 = (result - result.shift(21)) / 21.0
    result = _d1
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f42rb_f42_capital_return_buyback_byyield_slope_v001_signal,
    f42rb_f42_capital_return_buyback_byyieldsm_slope_v002_signal,
    f42rb_f42_capital_return_buyback_byyieldz_slope_v003_signal,
    f42rb_f42_capital_return_buyback_byyieldrank_slope_v004_signal,
    f42rb_f42_capital_return_buyback_netshflow_slope_v005_signal,
    f42rb_f42_capital_return_buyback_issyield_slope_v006_signal,
    f42rb_f42_capital_return_buyback_buybackbias_slope_v007_signal,
    f42rb_f42_capital_return_buyback_divyield_slope_v008_signal,
    f42rb_f42_capital_return_buyback_divyieldz_slope_v009_signal,
    f42rb_f42_capital_return_buyback_divyieldrank_slope_v010_signal,
    f42rb_f42_capital_return_buyback_totyield_slope_v011_signal,
    f42rb_f42_capital_return_buyback_totyieldsm_slope_v012_signal,
    f42rb_f42_capital_return_buyback_totyieldz_slope_v013_signal,
    f42rb_f42_capital_return_buyback_returnmix_slope_v014_signal,
    f42rb_f42_capital_return_buyback_divcover_slope_v015_signal,
    f42rb_f42_capital_return_buyback_divcoversm_slope_v016_signal,
    f42rb_f42_capital_return_buyback_divcoverz_slope_v017_signal,
    f42rb_f42_capital_return_buyback_divpayout_slope_v018_signal,
    f42rb_f42_capital_return_buyback_fcfpayout_slope_v019_signal,
    f42rb_f42_capital_return_buyback_retcover_slope_v020_signal,
    f42rb_f42_capital_return_buyback_bbfcf_slope_v021_signal,
    f42rb_f42_capital_return_buyback_bbocf_slope_v022_signal,
    f42rb_f42_capital_return_buyback_divocf_slope_v023_signal,
    f42rb_f42_capital_return_buyback_retocf_slope_v024_signal,
    f42rb_f42_capital_return_buyback_dpslevel_slope_v025_signal,
    f42rb_f42_capital_return_buyback_dpsgrow_slope_v026_signal,
    f42rb_f42_capital_return_buyback_dpsz_slope_v027_signal,
    f42rb_f42_capital_return_buyback_dpshikefreq_slope_v028_signal,
    f42rb_f42_capital_return_buyback_dpscut_slope_v029_signal,
    f42rb_f42_capital_return_buyback_divreliance_slope_v030_signal,
    f42rb_f42_capital_return_buyback_byaccel_slope_v031_signal,
    f42rb_f42_capital_return_buyback_tymom_slope_v032_signal,
    f42rb_f42_capital_return_buyback_dymom_slope_v033_signal,
    f42rb_f42_capital_return_buyback_fcfyield_slope_v034_signal,
    f42rb_f42_capital_return_buyback_fcfyieldz_slope_v035_signal,
    f42rb_f42_capital_return_buyback_surplus_slope_v036_signal,
    f42rb_f42_capital_return_buyback_fcfconv_slope_v037_signal,
    f42rb_f42_capital_return_buyback_overpay_slope_v038_signal,
    f42rb_f42_capital_return_buyback_sustdepth_slope_v039_signal,
    f42rb_f42_capital_return_buyback_bbpersist_slope_v040_signal,
    f42rb_f42_capital_return_buyback_covregime_slope_v041_signal,
    f42rb_f42_capital_return_buyback_selffund_slope_v042_signal,
    f42rb_f42_capital_return_buyback_tiltyield_slope_v043_signal,
    f42rb_f42_capital_return_buyback_bydisp_slope_v044_signal,
    f42rb_f42_capital_return_buyback_dystable_slope_v045_signal,
    f42rb_f42_capital_return_buyback_tysmooth_slope_v046_signal,
    f42rb_f42_capital_return_buyback_bbocfz_slope_v047_signal,
    f42rb_f42_capital_return_buyback_hikefund_slope_v048_signal,
    f42rb_f42_capital_return_buyback_byfcfratio_slope_v049_signal,
    f42rb_f42_capital_return_buyback_mixmom_slope_v050_signal,
    f42rb_f42_capital_return_buyback_tyrank_slope_v051_signal,
    f42rb_f42_capital_return_buyback_bbperdiv_slope_v052_signal,
    f42rb_f42_capital_return_buyback_bbheadroom_slope_v053_signal,
    f42rb_f42_capital_return_buyback_burdenz_slope_v054_signal,
    f42rb_f42_capital_return_buyback_covtrend_slope_v055_signal,
    f42rb_f42_capital_return_buyback_bytrend_slope_v056_signal,
    f42rb_f42_capital_return_buyback_distribrank_slope_v057_signal,
    f42rb_f42_capital_return_buyback_incomequal_slope_v058_signal,
    f42rb_f42_capital_return_buyback_bbqual_slope_v059_signal,
    f42rb_f42_capital_return_buyback_retscore_slope_v060_signal,
    f42rb_f42_capital_return_buyback_dilregime_slope_v061_signal,
    f42rb_f42_capital_return_buyback_payeridentity_slope_v062_signal,
    f42rb_f42_capital_return_buyback_intensz_slope_v063_signal,
    f42rb_f42_capital_return_buyback_bbstress_slope_v064_signal,
    f42rb_f42_capital_return_buyback_incomevsbb_slope_v065_signal,
    f42rb_f42_capital_return_buyback_divocfz_slope_v066_signal,
    f42rb_f42_capital_return_buyback_warchest_slope_v067_signal,
    f42rb_f42_capital_return_buyback_payoutgrow_slope_v068_signal,
    f42rb_f42_capital_return_buyback_bbtiming_slope_v069_signal,
    f42rb_f42_capital_return_buyback_covimprove_slope_v070_signal,
    f42rb_f42_capital_return_buyback_netshdisp_slope_v071_signal,
    f42rb_f42_capital_return_buyback_cyclicality_slope_v072_signal,
    f42rb_f42_capital_return_buyback_dyfcfshare_slope_v073_signal,
    f42rb_f42_capital_return_buyback_bbsignmag_slope_v074_signal,
    f42rb_f42_capital_return_buyback_durability_slope_v075_signal,
    f42rb_f42_capital_return_buyback_byyieldyr_slope_v076_signal,
    f42rb_f42_capital_return_buyback_byaccel2_slope_v077_signal,
    f42rb_f42_capital_return_buyback_bycurv_slope_v078_signal,
    f42rb_f42_capital_return_buyback_bbcumyield_slope_v079_signal,
    f42rb_f42_capital_return_buyback_byskew_slope_v080_signal,
    f42rb_f42_capital_return_buyback_divyieldyr_slope_v081_signal,
    f42rb_f42_capital_return_buyback_dyaccel_slope_v082_signal,
    f42rb_f42_capital_return_buyback_dycurv_slope_v083_signal,
    f42rb_f42_capital_return_buyback_divcumyield_slope_v084_signal,
    f42rb_f42_capital_return_buyback_dydisp_slope_v085_signal,
    f42rb_f42_capital_return_buyback_tyyrz_slope_v086_signal,
    f42rb_f42_capital_return_buyback_tyaccel_slope_v087_signal,
    f42rb_f42_capital_return_buyback_tycumyield_slope_v088_signal,
    f42rb_f42_capital_return_buyback_tydisp_slope_v089_signal,
    f42rb_f42_capital_return_buyback_mixsm_slope_v090_signal,
    f42rb_f42_capital_return_buyback_mixdisp_slope_v091_signal,
    f42rb_f42_capital_return_buyback_mixrank_slope_v092_signal,
    f42rb_f42_capital_return_buyback_covmin_slope_v093_signal,
    f42rb_f42_capital_return_buyback_covdisp_slope_v094_signal,
    f42rb_f42_capital_return_buyback_covrank_slope_v095_signal,
    f42rb_f42_capital_return_buyback_covaccel_slope_v096_signal,
    f42rb_f42_capital_return_buyback_retcovmin_slope_v097_signal,
    f42rb_f42_capital_return_buyback_fcfpayoutsm_slope_v098_signal,
    f42rb_f42_capital_return_buyback_fcfpayoutrank_slope_v099_signal,
    f42rb_f42_capital_return_buyback_bbfcfsm_slope_v100_signal,
    f42rb_f42_capital_return_buyback_bbocfz2_slope_v101_signal,
    f42rb_f42_capital_return_buyback_divocfsm_slope_v102_signal,
    f42rb_f42_capital_return_buyback_retocfrank_slope_v103_signal,
    f42rb_f42_capital_return_buyback_dpsaccel_slope_v104_signal,
    f42rb_f42_capital_return_buyback_dpsslope_slope_v105_signal,
    f42rb_f42_capital_return_buyback_dpsrank_slope_v106_signal,
    f42rb_f42_capital_return_buyback_dpsdisp_slope_v107_signal,
    f42rb_f42_capital_return_buyback_dpsstag_slope_v108_signal,
    f42rb_f42_capital_return_buyback_dpsvsdiv_slope_v109_signal,
    f42rb_f42_capital_return_buyback_fcfyieldyr_slope_v110_signal,
    f42rb_f42_capital_return_buyback_fcfymom_slope_v111_signal,
    f42rb_f42_capital_return_buyback_fcfyrank_slope_v112_signal,
    f42rb_f42_capital_return_buyback_fcfydisp_slope_v113_signal,
    f42rb_f42_capital_return_buyback_surplusrank_slope_v114_signal,
    f42rb_f42_capital_return_buyback_surplussm_slope_v115_signal,
    f42rb_f42_capital_return_buyback_overpayrank_slope_v116_signal,
    f42rb_f42_capital_return_buyback_overpaystreak_slope_v117_signal,
    f42rb_f42_capital_return_buyback_fcfconvyr_slope_v118_signal,
    f42rb_f42_capital_return_buyback_fcfconvdisp_slope_v119_signal,
    f42rb_f42_capital_return_buyback_bbfcfcorr_slope_v120_signal,
    f42rb_f42_capital_return_buyback_divfcfcorr_slope_v121_signal,
    f42rb_f42_capital_return_buyback_channelcorr_slope_v122_signal,
    f42rb_f42_capital_return_buyback_distribgrow_slope_v123_signal,
    f42rb_f42_capital_return_buyback_bbfcfinter_slope_v124_signal,
    f42rb_f42_capital_return_buyback_incomequalyr_slope_v125_signal,
    f42rb_f42_capital_return_buyback_bbtimerank_slope_v126_signal,
    f42rb_f42_capital_return_buyback_retconsist_slope_v127_signal,
    f42rb_f42_capital_return_buyback_payoutaccel_slope_v128_signal,
    f42rb_f42_capital_return_buyback_bbfcfmom_slope_v129_signal,
    f42rb_f42_capital_return_buyback_divsharesm_slope_v130_signal,
    f42rb_f42_capital_return_buyback_netshz_slope_v131_signal,
    f42rb_f42_capital_return_buyback_netshslope_slope_v132_signal,
    f42rb_f42_capital_return_buyback_netshrank_slope_v133_signal,
    f42rb_f42_capital_return_buyback_capactlumpy_slope_v134_signal,
    f42rb_f42_capital_return_buyback_extfundsm_slope_v135_signal,
    f42rb_f42_capital_return_buyback_durablereturn_slope_v136_signal,
    f42rb_f42_capital_return_buyback_safetydist_slope_v137_signal,
    f42rb_f42_capital_return_buyback_backedyield_slope_v138_signal,
    f42rb_f42_capital_return_buyback_unbacked_slope_v139_signal,
    f42rb_f42_capital_return_buyback_tiltz_slope_v140_signal,
    f42rb_f42_capital_return_buyback_safetycomp_slope_v141_signal,
    f42rb_f42_capital_return_buyback_annualcover_slope_v142_signal,
    f42rb_f42_capital_return_buyback_channelratio_slope_v143_signal,
    f42rb_f42_capital_return_buyback_divgrow_slope_v144_signal,
    f42rb_f42_capital_return_buyback_bbgrow_slope_v145_signal,
    f42rb_f42_capital_return_buyback_ocfgrow_slope_v146_signal,
    f42rb_f42_capital_return_buyback_ocfcushion_slope_v147_signal,
    f42rb_f42_capital_return_buyback_retbias_slope_v148_signal,
    f42rb_f42_capital_return_buyback_covregdist_slope_v149_signal,
    f42rb_f42_capital_return_buyback_crscore_slope_v150_signal,
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

    print("OK f42_capital_return_buyback_2nd_derivatives_001_150_claude: %d features pass" % n_features)
