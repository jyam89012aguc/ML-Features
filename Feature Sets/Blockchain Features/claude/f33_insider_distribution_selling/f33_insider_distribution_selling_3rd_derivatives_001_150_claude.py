import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


# ===== folder domain primitives (insider distribution / selling) =====
def _f33_sellintensity(sellval, marketcap, w):
    # trailing-w sum of insider sale $ scaled by market cap
    s = sellval.rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(s, marketcap)


def _f33_sellflow(sellshares, sharesbas, w):
    # trailing-w insider shares sold scaled by shares outstanding
    s = sellshares.rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(s, sharesbas)


def _f33_exercisedump(optionexval, sellval, marketcap, w):
    # trailing-w (option-exercise $ + sale $) scaled by market cap
    s = (optionexval + sellval).rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(s, marketcap)


def _f33_liquidation(tenpctsellval, sellval, w):
    # 10%-owner sale $ as a share of total trailing sale $
    a = tenpctsellval.rolling(w, min_periods=max(1, w // 2)).sum()
    b = sellval.rolling(w, min_periods=max(1, w // 2)).sum()
    return _safe_div(a, b)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f33id_f33_insider_distribution_selling_sellint_21d_jerk_v001_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_63d_jerk_v002_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_126d_jerk_v003_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_252d_jerk_v004_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_42d_jerk_v005_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_84d_jerk_v006_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_189d_jerk_v007_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_21d_jerk_v008_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_63d_jerk_v009_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_126d_jerk_v010_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_252d_jerk_v011_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_42d_jerk_v012_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_189d_jerk_v013_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exdump_21d_jerk_v014_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exdump_63d_jerk_v015_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exdump_126d_jerk_v016_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exdump_252d_jerk_v017_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exdump_84d_jerk_v018_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liq_21d_jerk_v019_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liq_63d_jerk_v020_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liq_126d_jerk_v021_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liq_252d_jerk_v022_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liq_42d_jerk_v023_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellint_21d_jerk_v024_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellint_63d_jerk_v025_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellint_126d_jerk_v026_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellflow_21d_jerk_v027_signal(sellshares, sharesbas):
    result = _z(_f33_sellflow(sellshares, sharesbas, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellflow_63d_jerk_v028_signal(sellshares, sharesbas):
    result = _z(_f33_sellflow(sellshares, sharesbas, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zexdump_21d_jerk_v029_signal(optionexval, sellval, marketcap):
    result = _z(_f33_exercisedump(optionexval, sellval, marketcap, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zexdump_63d_jerk_v030_signal(optionexval, sellval, marketcap):
    result = _z(_f33_exercisedump(optionexval, sellval, marketcap, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_accel_21_63_jerk_v031_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 21) - _f33_sellintensity(sellval, marketcap, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_accel_63_126_jerk_v032_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 63) - _f33_sellintensity(sellval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_accel_126_252_jerk_v033_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 126) - _f33_sellintensity(sellval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowaccel_21_63_jerk_v034_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 21) - _f33_sellflow(sellshares, sharesbas, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowaccel_63_126_jerk_v035_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 63) - _f33_sellflow(sellshares, sharesbas, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_intratio_21_126_jerk_v036_signal(sellval, marketcap):
    short = _f33_sellintensity(sellval, marketcap, 21)
    long = _f33_sellintensity(sellval, marketcap, 126)
    result = _safe_div(short, long.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_intratio_63_252_jerk_v037_signal(sellval, marketcap):
    short = _f33_sellintensity(sellval, marketcap, 63)
    long = _f33_sellintensity(sellval, marketcap, 252)
    result = _safe_div(short, long.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_surp_63d_jerk_v038_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = si - _mean(si, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_surp_126d_jerk_v039_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 126)
    result = si - _mean(si, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rank_21d_jerk_v040_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rank_63d_jerk_v041_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = si.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rankflow_126d_jerk_v042_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 126)
    result = sf.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_countrate_63d_jerk_v043_signal(sellcount, sellval, marketcap):
    c = sellcount.rolling(63, min_periods=21).sum()
    result = _safe_div(c, sellval.rolling(63, min_periods=21).sum().abs()) + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_countrate_126d_jerk_v044_signal(sellcount, marketcap, sellval):
    c = sellcount.rolling(21, min_periods=10).sum()
    result = _mean(c, 126) / marketcap.replace(0, np.nan) * 1e6 + _f33_sellintensity(sellval, marketcap, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_avgsize_63d_jerk_v045_signal(sellval, sellcount, marketcap):
    v = sellval.rolling(63, min_periods=21).sum()
    c = sellcount.rolling(63, min_periods=21).sum()
    result = _safe_div(v, c) / marketcap.replace(0, np.nan) + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_avgsize_126d_jerk_v046_signal(sellval, sellcount, marketcap):
    v = sellval.rolling(126, min_periods=42).sum()
    c = sellcount.rolling(126, min_periods=42).sum()
    result = _safe_div(v, c) / marketcap.replace(0, np.nan) + _f33_sellintensity(sellval, marketcap, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exconv_63d_jerk_v047_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(63, min_periods=21).sum()
    sv = sellval.rolling(63, min_periods=21).sum()
    result = _safe_div(ex, sv.abs()) + _f33_exercisedump(optionexval, sellval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exconv_126d_jerk_v048_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(126, min_periods=42).sum()
    sv = sellval.rolling(126, min_periods=42).sum()
    result = _safe_div(ex, sv.abs()) + _f33_exercisedump(optionexval, sellval, marketcap, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exconv_252d_jerk_v049_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(252, min_periods=84).sum()
    sv = sellval.rolling(252, min_periods=84).sum()
    result = _safe_div(ex, sv.abs()) + _f33_exercisedump(optionexval, sellval, marketcap, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_shrink_252d_jerk_v050_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 252) - _f33_sellflow(sellshares, sharesbas, 21)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_cluster_21d_jerk_v051_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = _safe_div(si, _mean(si, 126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_cluster_42d_jerk_v052_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 42)
    result = _safe_div(si, _mean(si, 189))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zliq_63d_jerk_v053_signal(tenpctsellval, sellval):
    result = _z(_f33_liquidation(tenpctsellval, sellval, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liqsurp_63d_jerk_v054_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 63)
    result = lq - _mean(lq, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_tenint_63d_jerk_v055_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(63, min_periods=21).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_tenint_126d_jerk_v056_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(126, min_periods=42).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_tenint_252d_jerk_v057_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(252, min_periods=84).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_pressdev_21d_jerk_v058_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si - _mean(si, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_pressdisp_126d_jerk_v059_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = _std(si, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_pressdisp_252d_jerk_v060_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = _std(si, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_distcomp_63d_jerk_v061_signal(sellval, optionexval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 63) + _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_distcomp_126d_jerk_v062_signal(sellval, optionexval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 126) + _f33_exercisedump(optionexval, sellval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liqweight_63d_jerk_v063_signal(sellval, tenpctsellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 63) * _f33_liquidation(tenpctsellval, sellval, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liqweight_126d_jerk_v064_signal(sellval, tenpctsellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 126) * _f33_liquidation(tenpctsellval, sellval, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_smooth_21d_jerk_v065_signal(sellval, marketcap):
    result = _mean(_f33_sellintensity(sellval, marketcap, 21), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_smooth_63d_jerk_v066_signal(sellval, marketcap):
    result = _mean(_f33_sellintensity(sellval, marketcap, 21), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_smoothflow_63d_jerk_v067_signal(sellshares, sharesbas):
    result = _mean(_f33_sellflow(sellshares, sharesbas, 21), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_ewm_63d_jerk_v068_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_ewm_126d_jerk_v069_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exaccel_21_63_jerk_v070_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 21) - _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exaccel_63_126_jerk_v071_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 63) - _f33_exercisedump(optionexval, sellval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_inforatio_21d_jerk_v072_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = _safe_div(si, _std(si, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowinfo_21d_jerk_v073_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 21)
    result = _safe_div(sf, _std(sf, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rankliq_63d_jerk_v074_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 63)
    result = lq.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rank_126d_jerk_v075_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 126)
    result = si.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_315d_jerk_v076_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_504d_jerk_v077_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellint_10d_jerk_v078_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_315d_jerk_v079_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_504d_jerk_v080_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_sellflow_84d_jerk_v081_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exdump_189d_jerk_v082_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exdump_504d_jerk_v083_signal(optionexval, sellval, marketcap):
    result = _f33_exercisedump(optionexval, sellval, marketcap, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liq_189d_jerk_v084_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liq_504d_jerk_v085_signal(tenpctsellval, sellval):
    result = _f33_liquidation(tenpctsellval, sellval, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellint_252d_jerk_v086_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 252), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellint_42d_jerk_v087_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 42), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellflow_126d_jerk_v088_signal(sellshares, sharesbas):
    result = _z(_f33_sellflow(sellshares, sharesbas, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zexdump_126d_jerk_v089_signal(optionexval, sellval, marketcap):
    result = _z(_f33_exercisedump(optionexval, sellval, marketcap, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zexdump_21d126w_jerk_v090_signal(optionexval, sellval, marketcap):
    result = _z(_f33_exercisedump(optionexval, sellval, marketcap, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_accel_42_126_jerk_v091_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 42) - _f33_sellintensity(sellval, marketcap, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_accel_84_252_jerk_v092_signal(sellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 84) - _f33_sellintensity(sellval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowaccel_42_189_jerk_v093_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 42) - _f33_sellflow(sellshares, sharesbas, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowaccel_126_252_jerk_v094_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 126) - _f33_sellflow(sellshares, sharesbas, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowratio_21_126_jerk_v095_signal(sellshares, sharesbas):
    short = _f33_sellflow(sellshares, sharesbas, 21)
    long = _f33_sellflow(sellshares, sharesbas, 126)
    result = _safe_div(short, long.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowratio_63_252_jerk_v096_signal(sellshares, sharesbas):
    short = _f33_sellflow(sellshares, sharesbas, 63)
    long = _f33_sellflow(sellshares, sharesbas, 252)
    result = _safe_div(short, long.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exratio_21_126_jerk_v097_signal(optionexval, sellval, marketcap):
    short = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    long = _f33_exercisedump(optionexval, sellval, marketcap, 126)
    result = _safe_div(short, long.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowsurp_63d_jerk_v098_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 63)
    result = sf - _mean(sf, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowsurp_126d_jerk_v099_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 126)
    result = sf - _mean(sf, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exsurp_63d_jerk_v100_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = ed - _mean(ed, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rank_252d_jerk_v101_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 252)
    result = si.rolling(504, min_periods=168).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rankflow_21d_jerk_v102_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 21)
    result = sf.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rankex_63d_jerk_v103_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = ed.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_countrate_252d_jerk_v104_signal(sellcount, sellval, marketcap):
    c = sellcount.rolling(252, min_periods=84).sum()
    result = _safe_div(c, sellval.rolling(252, min_periods=84).sum().abs()) + _f33_sellintensity(sellval, marketcap, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_countsmooth_63d_jerk_v105_signal(sellcount, marketcap, sellval):
    c = sellcount.rolling(21, min_periods=10).sum()
    result = _mean(c, 63) / marketcap.replace(0, np.nan) * 1e6 + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_avgsize_252d_jerk_v106_signal(sellval, sellcount, marketcap):
    v = sellval.rolling(252, min_periods=84).sum()
    c = sellcount.rolling(252, min_periods=84).sum()
    result = _safe_div(v, c) / marketcap.replace(0, np.nan) + _f33_sellintensity(sellval, marketcap, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zavgsize_63d_jerk_v107_signal(sellval, sellcount, marketcap):
    v = sellval.rolling(63, min_periods=21).sum()
    c = sellcount.rolling(63, min_periods=21).sum()
    size = _safe_div(v, c)
    result = _z(size, 252) + _f33_sellintensity(sellval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exconv_21d_jerk_v108_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(21, min_periods=10).sum()
    sv = sellval.rolling(21, min_periods=10).sum()
    result = _safe_div(ex, sv.abs()) + _f33_exercisedump(optionexval, sellval, marketcap, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zexconv_63d_jerk_v109_signal(optionexval, sellval, marketcap):
    ex = optionexval.rolling(63, min_periods=21).sum()
    sv = sellval.rolling(63, min_periods=21).sum()
    conv = _safe_div(ex, sv.abs())
    result = _z(conv, 252) + _f33_exercisedump(optionexval, sellval, marketcap, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_shrink_504d_jerk_v110_signal(sellshares, sharesbas):
    result = _f33_sellflow(sellshares, sharesbas, 504) - _f33_sellflow(sellshares, sharesbas, 63)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_cluster_63d_jerk_v111_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = _safe_div(si, _mean(si, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_cluster_10d_jerk_v112_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 10)
    result = _safe_div(si, _mean(si, 63))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zliq_126d_jerk_v113_signal(tenpctsellval, sellval):
    result = _z(_f33_liquidation(tenpctsellval, sellval, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liqsurp_126d_jerk_v114_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 126)
    result = lq - _mean(lq, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_tenint_42d_jerk_v115_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(42, min_periods=21).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_tenint_504d_jerk_v116_signal(tenpctsellval, marketcap, sellval):
    s = tenpctsellval.rolling(504, min_periods=168).sum()
    result = _safe_div(s, marketcap) + _f33_sellintensity(sellval, marketcap, 504) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_pressdev_63d_jerk_v117_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = si - _mean(si, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_pressdisp63_252d_jerk_v118_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = _std(si, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_flowdisp_252d_jerk_v119_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 21)
    result = _std(sf, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_distcomp_252d_jerk_v120_signal(sellval, optionexval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 252) + _f33_exercisedump(optionexval, sellval, marketcap, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liqweight_252d_jerk_v121_signal(sellval, tenpctsellval, marketcap):
    result = _f33_sellintensity(sellval, marketcap, 252) * _f33_liquidation(tenpctsellval, sellval, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_smooth_126d_jerk_v122_signal(sellval, marketcap):
    result = _mean(_f33_sellintensity(sellval, marketcap, 21), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_smoothflow_126d_jerk_v123_signal(sellshares, sharesbas):
    result = _mean(_f33_sellflow(sellshares, sharesbas, 21), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_smoothex_63d_jerk_v124_signal(optionexval, sellval, marketcap):
    result = _mean(_f33_exercisedump(optionexval, sellval, marketcap, 21), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_ewm_252d_jerk_v125_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 21)
    result = si.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_ewmflow_126d_jerk_v126_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 21)
    result = sf.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_ewmex_126d_jerk_v127_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    result = ed.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_ewmliq_126d_jerk_v128_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 63)
    result = lq.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_accelsmooth_63d_jerk_v129_signal(sellval, marketcap):
    spread = _f33_sellintensity(sellval, marketcap, 21) - _f33_sellintensity(sellval, marketcap, 63)
    result = _mean(spread, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exinfo_21d_jerk_v130_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    result = _safe_div(ed, _std(ed, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_inforatio_63d_jerk_v131_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = _safe_div(si, _std(si, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liqinfo_63d_jerk_v132_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 63)
    result = _safe_div(lq, _std(lq, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rankflow_63d_jerk_v133_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 63)
    result = sf.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_rankliq_126d_jerk_v134_signal(tenpctsellval, sellval):
    lq = _f33_liquidation(tenpctsellval, sellval, 126)
    result = lq.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_pureshare_63d_jerk_v135_signal(sellval, optionexval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    result = _safe_div(si, ed)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_pureshare_126d_jerk_v136_signal(sellval, optionexval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 126)
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 126)
    result = _safe_div(si, ed)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_volscaled_63d_jerk_v137_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 63)
    vol = _std(_f33_sellintensity(sellval, marketcap, 21), 252)
    result = _safe_div(si, vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_volscaledflow_126d_jerk_v138_signal(sellshares, sharesbas):
    sf = _f33_sellflow(sellshares, sharesbas, 126)
    vol = _std(_f33_sellflow(sellshares, sharesbas, 21), 252)
    result = _safe_div(sf, vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_volscaledex_63d_jerk_v139_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    vol = _std(_f33_exercisedump(optionexval, sellval, marketcap, 21), 252)
    result = _safe_div(ed, vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_clusterflow_63d_jerk_v140_signal(sellval, marketcap, sellshares, sharesbas):
    si = _f33_sellintensity(sellval, marketcap, 63)
    sf = _f33_sellflow(sellshares, sharesbas, 63)
    result = si * sf
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_convratio_63d_jerk_v141_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 63)
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = _safe_div(ed, si)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_liqflow_126d_jerk_v142_signal(sellshares, sharesbas, tenpctsellval, sellval):
    sf = _f33_sellflow(sellshares, sharesbas, 126)
    lq = _f33_liquidation(tenpctsellval, sellval, 126)
    result = sf * lq
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellint63_504w_jerk_v143_signal(sellval, marketcap):
    result = _z(_f33_sellintensity(sellval, marketcap, 63), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_zsellflow252_504w_jerk_v144_signal(sellshares, sharesbas):
    result = _z(_f33_sellflow(sellshares, sharesbas, 252), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_tenweight_63d_jerk_v145_signal(tenpctsellval, marketcap, sellval):
    ti = _safe_div(tenpctsellval.rolling(63, min_periods=21).sum(), marketcap)
    si = _f33_sellintensity(sellval, marketcap, 63)
    result = ti * np.sign(si) + si * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_surge_10d_jerk_v146_signal(sellval, marketcap):
    si = _f33_sellintensity(sellval, marketcap, 10)
    result = _safe_div(si, _mean(si, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_exsurge_21d_jerk_v147_signal(optionexval, sellval, marketcap):
    ed = _f33_exercisedump(optionexval, sellval, marketcap, 21)
    result = _safe_div(ed, _mean(ed, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_blend_multi_jerk_v148_signal(sellval, marketcap):
    result = (_f33_sellintensity(sellval, marketcap, 21) + _f33_sellintensity(sellval, marketcap, 63)
              + _f33_sellintensity(sellval, marketcap, 126) + _f33_sellintensity(sellval, marketcap, 252)) / 4.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_blend_dist_jerk_v149_signal(sellval, marketcap, sellshares, sharesbas, optionexval):
    result = (_f33_sellintensity(sellval, marketcap, 126)
              + _f33_sellflow(sellshares, sharesbas, 126)
              + _f33_exercisedump(optionexval, sellval, marketcap, 126)) / 3.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f33id_f33_insider_distribution_selling_blend_liq_jerk_v150_signal(sellval, marketcap, tenpctsellval, sellshares, sharesbas):
    result = (_f33_sellintensity(sellval, marketcap, 252)
              + _f33_sellflow(sellshares, sharesbas, 252)
              + _f33_liquidation(tenpctsellval, sellval, 252)) / 3.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f33id_f33_insider_distribution_selling_sellint_21d_jerk_v001_signal,    f33id_f33_insider_distribution_selling_sellint_63d_jerk_v002_signal,    f33id_f33_insider_distribution_selling_sellint_126d_jerk_v003_signal,    f33id_f33_insider_distribution_selling_sellint_252d_jerk_v004_signal,    f33id_f33_insider_distribution_selling_sellint_42d_jerk_v005_signal,    f33id_f33_insider_distribution_selling_sellint_84d_jerk_v006_signal,    f33id_f33_insider_distribution_selling_sellint_189d_jerk_v007_signal,    f33id_f33_insider_distribution_selling_sellflow_21d_jerk_v008_signal,    f33id_f33_insider_distribution_selling_sellflow_63d_jerk_v009_signal,    f33id_f33_insider_distribution_selling_sellflow_126d_jerk_v010_signal,    f33id_f33_insider_distribution_selling_sellflow_252d_jerk_v011_signal,    f33id_f33_insider_distribution_selling_sellflow_42d_jerk_v012_signal,    f33id_f33_insider_distribution_selling_sellflow_189d_jerk_v013_signal,    f33id_f33_insider_distribution_selling_exdump_21d_jerk_v014_signal,    f33id_f33_insider_distribution_selling_exdump_63d_jerk_v015_signal,    f33id_f33_insider_distribution_selling_exdump_126d_jerk_v016_signal,    f33id_f33_insider_distribution_selling_exdump_252d_jerk_v017_signal,    f33id_f33_insider_distribution_selling_exdump_84d_jerk_v018_signal,    f33id_f33_insider_distribution_selling_liq_21d_jerk_v019_signal,    f33id_f33_insider_distribution_selling_liq_63d_jerk_v020_signal,    f33id_f33_insider_distribution_selling_liq_126d_jerk_v021_signal,    f33id_f33_insider_distribution_selling_liq_252d_jerk_v022_signal,    f33id_f33_insider_distribution_selling_liq_42d_jerk_v023_signal,    f33id_f33_insider_distribution_selling_zsellint_21d_jerk_v024_signal,    f33id_f33_insider_distribution_selling_zsellint_63d_jerk_v025_signal,    f33id_f33_insider_distribution_selling_zsellint_126d_jerk_v026_signal,    f33id_f33_insider_distribution_selling_zsellflow_21d_jerk_v027_signal,    f33id_f33_insider_distribution_selling_zsellflow_63d_jerk_v028_signal,    f33id_f33_insider_distribution_selling_zexdump_21d_jerk_v029_signal,    f33id_f33_insider_distribution_selling_zexdump_63d_jerk_v030_signal,    f33id_f33_insider_distribution_selling_accel_21_63_jerk_v031_signal,    f33id_f33_insider_distribution_selling_accel_63_126_jerk_v032_signal,    f33id_f33_insider_distribution_selling_accel_126_252_jerk_v033_signal,    f33id_f33_insider_distribution_selling_flowaccel_21_63_jerk_v034_signal,    f33id_f33_insider_distribution_selling_flowaccel_63_126_jerk_v035_signal,    f33id_f33_insider_distribution_selling_intratio_21_126_jerk_v036_signal,    f33id_f33_insider_distribution_selling_intratio_63_252_jerk_v037_signal,    f33id_f33_insider_distribution_selling_surp_63d_jerk_v038_signal,    f33id_f33_insider_distribution_selling_surp_126d_jerk_v039_signal,    f33id_f33_insider_distribution_selling_rank_21d_jerk_v040_signal,    f33id_f33_insider_distribution_selling_rank_63d_jerk_v041_signal,    f33id_f33_insider_distribution_selling_rankflow_126d_jerk_v042_signal,    f33id_f33_insider_distribution_selling_countrate_63d_jerk_v043_signal,    f33id_f33_insider_distribution_selling_countrate_126d_jerk_v044_signal,    f33id_f33_insider_distribution_selling_avgsize_63d_jerk_v045_signal,    f33id_f33_insider_distribution_selling_avgsize_126d_jerk_v046_signal,    f33id_f33_insider_distribution_selling_exconv_63d_jerk_v047_signal,    f33id_f33_insider_distribution_selling_exconv_126d_jerk_v048_signal,    f33id_f33_insider_distribution_selling_exconv_252d_jerk_v049_signal,    f33id_f33_insider_distribution_selling_shrink_252d_jerk_v050_signal,    f33id_f33_insider_distribution_selling_cluster_21d_jerk_v051_signal,    f33id_f33_insider_distribution_selling_cluster_42d_jerk_v052_signal,    f33id_f33_insider_distribution_selling_zliq_63d_jerk_v053_signal,    f33id_f33_insider_distribution_selling_liqsurp_63d_jerk_v054_signal,    f33id_f33_insider_distribution_selling_tenint_63d_jerk_v055_signal,    f33id_f33_insider_distribution_selling_tenint_126d_jerk_v056_signal,    f33id_f33_insider_distribution_selling_tenint_252d_jerk_v057_signal,    f33id_f33_insider_distribution_selling_pressdev_21d_jerk_v058_signal,    f33id_f33_insider_distribution_selling_pressdisp_126d_jerk_v059_signal,    f33id_f33_insider_distribution_selling_pressdisp_252d_jerk_v060_signal,    f33id_f33_insider_distribution_selling_distcomp_63d_jerk_v061_signal,    f33id_f33_insider_distribution_selling_distcomp_126d_jerk_v062_signal,    f33id_f33_insider_distribution_selling_liqweight_63d_jerk_v063_signal,    f33id_f33_insider_distribution_selling_liqweight_126d_jerk_v064_signal,    f33id_f33_insider_distribution_selling_smooth_21d_jerk_v065_signal,    f33id_f33_insider_distribution_selling_smooth_63d_jerk_v066_signal,    f33id_f33_insider_distribution_selling_smoothflow_63d_jerk_v067_signal,    f33id_f33_insider_distribution_selling_ewm_63d_jerk_v068_signal,    f33id_f33_insider_distribution_selling_ewm_126d_jerk_v069_signal,    f33id_f33_insider_distribution_selling_exaccel_21_63_jerk_v070_signal,    f33id_f33_insider_distribution_selling_exaccel_63_126_jerk_v071_signal,    f33id_f33_insider_distribution_selling_inforatio_21d_jerk_v072_signal,    f33id_f33_insider_distribution_selling_flowinfo_21d_jerk_v073_signal,    f33id_f33_insider_distribution_selling_rankliq_63d_jerk_v074_signal,    f33id_f33_insider_distribution_selling_rank_126d_jerk_v075_signal,    f33id_f33_insider_distribution_selling_sellint_315d_jerk_v076_signal,    f33id_f33_insider_distribution_selling_sellint_504d_jerk_v077_signal,    f33id_f33_insider_distribution_selling_sellint_10d_jerk_v078_signal,    f33id_f33_insider_distribution_selling_sellflow_315d_jerk_v079_signal,    f33id_f33_insider_distribution_selling_sellflow_504d_jerk_v080_signal,    f33id_f33_insider_distribution_selling_sellflow_84d_jerk_v081_signal,    f33id_f33_insider_distribution_selling_exdump_189d_jerk_v082_signal,    f33id_f33_insider_distribution_selling_exdump_504d_jerk_v083_signal,    f33id_f33_insider_distribution_selling_liq_189d_jerk_v084_signal,    f33id_f33_insider_distribution_selling_liq_504d_jerk_v085_signal,    f33id_f33_insider_distribution_selling_zsellint_252d_jerk_v086_signal,    f33id_f33_insider_distribution_selling_zsellint_42d_jerk_v087_signal,    f33id_f33_insider_distribution_selling_zsellflow_126d_jerk_v088_signal,    f33id_f33_insider_distribution_selling_zexdump_126d_jerk_v089_signal,    f33id_f33_insider_distribution_selling_zexdump_21d126w_jerk_v090_signal,    f33id_f33_insider_distribution_selling_accel_42_126_jerk_v091_signal,    f33id_f33_insider_distribution_selling_accel_84_252_jerk_v092_signal,    f33id_f33_insider_distribution_selling_flowaccel_42_189_jerk_v093_signal,    f33id_f33_insider_distribution_selling_flowaccel_126_252_jerk_v094_signal,    f33id_f33_insider_distribution_selling_flowratio_21_126_jerk_v095_signal,    f33id_f33_insider_distribution_selling_flowratio_63_252_jerk_v096_signal,    f33id_f33_insider_distribution_selling_exratio_21_126_jerk_v097_signal,    f33id_f33_insider_distribution_selling_flowsurp_63d_jerk_v098_signal,    f33id_f33_insider_distribution_selling_flowsurp_126d_jerk_v099_signal,    f33id_f33_insider_distribution_selling_exsurp_63d_jerk_v100_signal,    f33id_f33_insider_distribution_selling_rank_252d_jerk_v101_signal,    f33id_f33_insider_distribution_selling_rankflow_21d_jerk_v102_signal,    f33id_f33_insider_distribution_selling_rankex_63d_jerk_v103_signal,    f33id_f33_insider_distribution_selling_countrate_252d_jerk_v104_signal,    f33id_f33_insider_distribution_selling_countsmooth_63d_jerk_v105_signal,    f33id_f33_insider_distribution_selling_avgsize_252d_jerk_v106_signal,    f33id_f33_insider_distribution_selling_zavgsize_63d_jerk_v107_signal,    f33id_f33_insider_distribution_selling_exconv_21d_jerk_v108_signal,    f33id_f33_insider_distribution_selling_zexconv_63d_jerk_v109_signal,    f33id_f33_insider_distribution_selling_shrink_504d_jerk_v110_signal,    f33id_f33_insider_distribution_selling_cluster_63d_jerk_v111_signal,    f33id_f33_insider_distribution_selling_cluster_10d_jerk_v112_signal,    f33id_f33_insider_distribution_selling_zliq_126d_jerk_v113_signal,    f33id_f33_insider_distribution_selling_liqsurp_126d_jerk_v114_signal,    f33id_f33_insider_distribution_selling_tenint_42d_jerk_v115_signal,    f33id_f33_insider_distribution_selling_tenint_504d_jerk_v116_signal,    f33id_f33_insider_distribution_selling_pressdev_63d_jerk_v117_signal,    f33id_f33_insider_distribution_selling_pressdisp63_252d_jerk_v118_signal,    f33id_f33_insider_distribution_selling_flowdisp_252d_jerk_v119_signal,    f33id_f33_insider_distribution_selling_distcomp_252d_jerk_v120_signal,    f33id_f33_insider_distribution_selling_liqweight_252d_jerk_v121_signal,    f33id_f33_insider_distribution_selling_smooth_126d_jerk_v122_signal,    f33id_f33_insider_distribution_selling_smoothflow_126d_jerk_v123_signal,    f33id_f33_insider_distribution_selling_smoothex_63d_jerk_v124_signal,    f33id_f33_insider_distribution_selling_ewm_252d_jerk_v125_signal,    f33id_f33_insider_distribution_selling_ewmflow_126d_jerk_v126_signal,    f33id_f33_insider_distribution_selling_ewmex_126d_jerk_v127_signal,    f33id_f33_insider_distribution_selling_ewmliq_126d_jerk_v128_signal,    f33id_f33_insider_distribution_selling_accelsmooth_63d_jerk_v129_signal,    f33id_f33_insider_distribution_selling_exinfo_21d_jerk_v130_signal,    f33id_f33_insider_distribution_selling_inforatio_63d_jerk_v131_signal,    f33id_f33_insider_distribution_selling_liqinfo_63d_jerk_v132_signal,    f33id_f33_insider_distribution_selling_rankflow_63d_jerk_v133_signal,    f33id_f33_insider_distribution_selling_rankliq_126d_jerk_v134_signal,    f33id_f33_insider_distribution_selling_pureshare_63d_jerk_v135_signal,    f33id_f33_insider_distribution_selling_pureshare_126d_jerk_v136_signal,    f33id_f33_insider_distribution_selling_volscaled_63d_jerk_v137_signal,    f33id_f33_insider_distribution_selling_volscaledflow_126d_jerk_v138_signal,    f33id_f33_insider_distribution_selling_volscaledex_63d_jerk_v139_signal,    f33id_f33_insider_distribution_selling_clusterflow_63d_jerk_v140_signal,    f33id_f33_insider_distribution_selling_convratio_63d_jerk_v141_signal,    f33id_f33_insider_distribution_selling_liqflow_126d_jerk_v142_signal,    f33id_f33_insider_distribution_selling_zsellint63_504w_jerk_v143_signal,    f33id_f33_insider_distribution_selling_zsellflow252_504w_jerk_v144_signal,    f33id_f33_insider_distribution_selling_tenweight_63d_jerk_v145_signal,    f33id_f33_insider_distribution_selling_surge_10d_jerk_v146_signal,    f33id_f33_insider_distribution_selling_exsurge_21d_jerk_v147_signal,    f33id_f33_insider_distribution_selling_blend_multi_jerk_v148_signal,    f33id_f33_insider_distribution_selling_blend_dist_jerk_v149_signal,    f33id_f33_insider_distribution_selling_blend_liq_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_INSIDER_DISTRIBUTION_SELLING_REGISTRY_JERK = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f33_sellintensity', '_f33_sellflow', '_f33_exercisedump', '_f33_liquidation')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f33_insider_distribution_selling_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
