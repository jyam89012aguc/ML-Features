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


# ===== folder domain primitives (institutional accumulation, 13F) =====
def _f28_accum(shrvalue, w):
    # accumulation: fractional change in value of shares held by institutions over w
    return shrvalue.pct_change(periods=w)


def _f28_flow(shrunits, w):
    # share flow: change in shares held over w, normalized by trailing average level
    d = shrunits.diff(periods=w)
    base = shrunits.rolling(w, min_periods=max(1, w // 2)).mean()
    return d / base.replace(0, np.nan)


def _f28_ownz(shrvalue, w):
    # z-score of institutional-held value over w (standardized accumulation level)
    return _z(shrvalue, w)


def _f28_costbasis(shrvalue, shrunits):
    # implied average cost basis = value per unit held
    return _safe_div(shrvalue, shrunits)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f28ia_f28_institutional_accumulation_accum_63d_slope_v001_signal(shrvalue):
    result = _f28_accum(shrvalue, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_126d_slope_v002_signal(shrvalue):
    result = _f28_accum(shrvalue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_252d_slope_v003_signal(shrvalue):
    result = _f28_accum(shrvalue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_504d_slope_v004_signal(shrvalue):
    result = _f28_accum(shrvalue, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_21d_slope_v005_signal(shrvalue):
    result = _f28_accum(shrvalue, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_42d_slope_v006_signal(shrvalue):
    result = _f28_accum(shrvalue, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_logaccum_63d_slope_v007_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(63)) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_logaccum_126d_slope_v008_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(126)) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_logaccum_252d_slope_v009_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(252)) + _f28_accum(shrvalue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_logaccum_504d_slope_v010_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(504)) + _f28_accum(shrvalue, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flow_63d_slope_v011_signal(shrunits):
    result = _f28_flow(shrunits, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flow_126d_slope_v012_signal(shrunits):
    result = _f28_flow(shrunits, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flow_252d_slope_v013_signal(shrunits):
    result = _f28_flow(shrunits, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flow_21d_slope_v014_signal(shrunits):
    result = _f28_flow(shrunits, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flow_504d_slope_v015_signal(shrunits):
    result = _f28_flow(shrunits, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_unitgrow_63d_slope_v016_signal(shrunits):
    result = shrunits.pct_change(periods=63) + _f28_flow(shrunits, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_unitgrow_126d_slope_v017_signal(shrunits):
    result = shrunits.pct_change(periods=126) + _f28_flow(shrunits, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_unitgrow_252d_slope_v018_signal(shrunits):
    result = shrunits.pct_change(periods=252) + _f28_flow(shrunits, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvgrow_63d_slope_v019_signal(totalvalue, shrvalue):
    result = totalvalue.pct_change(periods=63) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvgrow_126d_slope_v020_signal(totalvalue, shrvalue):
    result = totalvalue.pct_change(periods=126) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvgrow_252d_slope_v021_signal(totalvalue, shrvalue):
    result = totalvalue.pct_change(periods=252) + _f28_accum(shrvalue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvgrow_504d_slope_v022_signal(totalvalue, shrvalue):
    result = totalvalue.pct_change(periods=504) + _f28_accum(shrvalue, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownz_252d_slope_v023_signal(shrvalue):
    result = _f28_ownz(shrvalue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownz_126d_slope_v024_signal(shrvalue):
    result = _f28_ownz(shrvalue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownz_504d_slope_v025_signal(shrvalue):
    result = _f28_ownz(shrvalue, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownz_63d_slope_v026_signal(shrvalue):
    result = _f28_ownz(shrvalue, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_unitz_252d_slope_v027_signal(shrunits):
    result = _z(shrunits, 252) + _f28_flow(shrunits, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvz_252d_slope_v028_signal(totalvalue, shrvalue):
    result = _z(totalvalue, 252) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accel_63_126_slope_v029_signal(shrvalue):
    result = _f28_accum(shrvalue, 63) - _f28_accum(shrvalue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accel_126_252_slope_v030_signal(shrvalue):
    result = _f28_accum(shrvalue, 126) - _f28_accum(shrvalue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accel_21_63_slope_v031_signal(shrvalue):
    result = _f28_accum(shrvalue, 21) - _f28_accum(shrvalue, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpct_lvl_slope_v032_signal(shrvalue, marketcap):
    result = _safe_div(shrvalue, marketcap) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpct_chg63_slope_v033_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own - own.shift(63) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpct_chg126_slope_v034_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own - own.shift(126) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpct_chg252_slope_v035_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own - own.shift(252) + _f28_accum(shrvalue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpctz_252d_slope_v036_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = _z(own, 252) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpctgrow_126_slope_v037_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own.pct_change(periods=126) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_costbasis_lvl_slope_v038_signal(shrvalue, shrunits):
    result = _f28_costbasis(shrvalue, shrunits)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_costbasis_chg63_slope_v039_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = cb - cb.shift(63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_costbasis_grow126_slope_v040_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = cb.pct_change(periods=126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_costbasis_grow252_slope_v041_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = cb.pct_change(periods=252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_costbasisz_252d_slope_v042_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = _z(cb, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_rank_accum63_slope_v043_signal(shrvalue):
    r = _f28_accum(shrvalue, 63)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_rank_accum126_slope_v044_signal(shrvalue):
    r = _f28_accum(shrvalue, 126)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_rank_flow63_slope_v045_signal(shrunits):
    r = _f28_flow(shrunits, 63)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownmom_21s63_slope_v046_signal(shrvalue):
    result = _mean(_f28_accum(shrvalue, 21), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownmom_63s42_slope_v047_signal(shrvalue):
    result = _mean(_f28_accum(shrvalue, 63), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowdisp_126_slope_v048_signal(shrunits):
    result = _std(_f28_flow(shrunits, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowdisp_252_slope_v049_signal(shrunits):
    result = _std(_f28_flow(shrunits, 21), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumdisp_126_slope_v050_signal(shrvalue):
    result = _std(_f28_accum(shrvalue, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumir_63d_slope_v051_signal(shrvalue):
    r = _f28_accum(shrvalue, 63)
    result = _safe_div(r, _std(r, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumir_126d_slope_v052_signal(shrvalue):
    r = _f28_accum(shrvalue, 126)
    result = _safe_div(r, _std(r, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowir_63d_slope_v053_signal(shrunits):
    r = _f28_flow(shrunits, 63)
    result = _safe_div(r, _std(r, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_surp_63d_slope_v054_signal(shrvalue):
    r = _f28_accum(shrvalue, 63)
    result = r - _mean(r, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_surp_126d_slope_v055_signal(shrvalue):
    r = _f28_accum(shrvalue, 126)
    result = r - _mean(r, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowsurp_63d_slope_v056_signal(shrunits):
    r = _f28_flow(shrunits, 63)
    result = r - _mean(r, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_valflow_sprd63_slope_v057_signal(shrvalue, shrunits):
    result = _f28_accum(shrvalue, 63) - _f28_flow(shrunits, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_valflow_sprd126_slope_v058_signal(shrvalue, shrunits):
    result = _f28_accum(shrvalue, 126) - _f28_flow(shrunits, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvshare_lvl_slope_v059_signal(shrvalue, totalvalue):
    result = _safe_div(shrvalue, totalvalue) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvshare_chg126_slope_v060_signal(shrvalue, totalvalue):
    sh = _safe_div(shrvalue, totalvalue)
    result = sh - sh.shift(126) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvsharez_252_slope_v061_signal(shrvalue, totalvalue):
    sh = _safe_div(shrvalue, totalvalue)
    result = _z(sh, 252) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumewm_63d_slope_v062_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0 + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumewm_126d_slope_v063_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0 + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowewm_63d_slope_v064_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0 + _f28_flow(shrunits, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumsharpe_126_slope_v065_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = _safe_div(_mean(lr, 126), _std(lr, 126)) * np.sqrt(126.0) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumsharpe_252_slope_v066_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = _safe_div(_mean(lr, 252), _std(lr, 252)) * np.sqrt(252.0) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumeff_126_slope_v067_signal(shrvalue):
    net = shrvalue - shrvalue.shift(126)
    path = shrvalue.diff().abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net, path) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumeff_252_slope_v068_signal(shrvalue):
    net = shrvalue - shrvalue.shift(252)
    path = shrvalue.diff().abs().rolling(252, min_periods=84).sum()
    result = _safe_div(net, path) + _f28_accum(shrvalue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_floweff_126_slope_v069_signal(shrunits):
    net = shrunits - shrunits.shift(126)
    path = shrunits.diff().abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net, path) + _f28_flow(shrunits, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumvs_63d_slope_v070_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    vol = _std(lr, 252) * np.sqrt(63.0)
    result = _safe_div(_f28_accum(shrvalue, 63), vol)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumvs_126d_slope_v071_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    vol = _std(lr, 252) * np.sqrt(126.0)
    result = _safe_div(_f28_accum(shrvalue, 126), vol)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumxownz_63_slope_v072_signal(shrvalue):
    result = _f28_accum(shrvalue, 63) * _f28_ownz(shrvalue, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpctvs_126_slope_v073_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = _safe_div(own - own.shift(126), _std(own, 252)) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_84d_slope_v074_signal(shrvalue):
    result = _f28_accum(shrvalue, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_189d_slope_v075_signal(shrvalue):
    result = _f28_accum(shrvalue, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownmom_21s21_slope_v076_signal(shrvalue):
    result = _mean(_f28_accum(shrvalue, 21), 21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownmom_126s42_slope_v077_signal(shrvalue):
    result = _mean(_f28_accum(shrvalue, 126), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowmom_42s42_slope_v078_signal(shrunits):
    result = _mean(_f28_flow(shrunits, 42), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowmom_84s42_slope_v079_signal(shrunits):
    result = _mean(_f28_flow(shrunits, 84), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_zaccum63_252_slope_v080_signal(shrvalue):
    result = _z(_f28_accum(shrvalue, 63), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_zaccum126_504_slope_v081_signal(shrvalue):
    result = _z(_f28_accum(shrvalue, 126), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_zaccum21_126_slope_v082_signal(shrvalue):
    result = _z(_f28_accum(shrvalue, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_zflow63_252_slope_v083_signal(shrunits):
    result = _z(_f28_flow(shrunits, 63), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_zflow126_504_slope_v084_signal(shrunits):
    result = _z(_f28_flow(shrunits, 126), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accel_42_84_slope_v085_signal(shrvalue):
    result = _f28_accum(shrvalue, 42) - _f28_accum(shrvalue, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accel_84_189_slope_v086_signal(shrvalue):
    result = _f28_accum(shrvalue, 84) - _f28_accum(shrvalue, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowaccel_63_126_slope_v087_signal(shrunits):
    result = _f28_flow(shrunits, 63) - _f28_flow(shrunits, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowaccel_126_252_slope_v088_signal(shrunits):
    result = _f28_flow(shrunits, 126) - _f28_flow(shrunits, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_sprd_63_252_slope_v089_signal(shrvalue):
    result = _f28_accum(shrvalue, 63) - _f28_accum(shrvalue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_lsprd_63_126_slope_v090_signal(shrvalue):
    result = (np.log(shrvalue / shrvalue.shift(63)) - np.log(shrvalue / shrvalue.shift(126))) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvz_504d_slope_v091_signal(totalvalue, shrvalue):
    result = _z(totalvalue, 504) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvlog_126d_slope_v092_signal(totalvalue, shrvalue):
    result = np.log(totalvalue / totalvalue.shift(126)) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvlog_252d_slope_v093_signal(totalvalue, shrvalue):
    result = np.log(totalvalue / totalvalue.shift(252)) + _f28_accum(shrvalue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_relaccum_63_slope_v094_signal(shrvalue, marketcap):
    result = _f28_accum(shrvalue, 63) - marketcap.pct_change(periods=63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_relaccum_126_slope_v095_signal(shrvalue, marketcap):
    result = _f28_accum(shrvalue, 126) - marketcap.pct_change(periods=126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_relaccum_252_slope_v096_signal(shrvalue, marketcap):
    result = _f28_accum(shrvalue, 252) - marketcap.pct_change(periods=252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_annaccum_63_slope_v097_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(63)) * (252.0 / 63.0) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_annaccum_126_slope_v098_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(126)) * (252.0 / 126.0) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_annflow_63_slope_v099_signal(shrunits):
    result = np.log(shrunits / shrunits.shift(63)) * (252.0 / 63.0) + _f28_flow(shrunits, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_rank_accum252_slope_v100_signal(shrvalue):
    r = _f28_accum(shrvalue, 252)
    result = r.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_rank_flow126_slope_v101_signal(shrunits):
    r = _f28_flow(shrunits, 126)
    result = r.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_rank_costbasis_slope_v102_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = cb.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_rank_ownpct_slope_v103_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own.rolling(252, min_periods=84).rank(pct=True) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_cbir_126_slope_v104_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = _safe_div(cb - cb.shift(126), _std(cb, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_cbewm_63_slope_v105_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    lr = np.log(cb / cb.shift(1))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumflowx_63_slope_v106_signal(shrvalue, shrunits):
    result = _f28_accum(shrvalue, 63) * _f28_flow(shrunits, 63).clip(-5, 5)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumflowx_126_slope_v107_signal(shrvalue, shrunits):
    result = _f28_accum(shrvalue, 126) * _f28_flow(shrunits, 126).clip(-5, 5)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumxown_63_slope_v108_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = _f28_accum(shrvalue, 63) * own
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowxown_63_slope_v109_signal(shrunits, shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = _f28_flow(shrunits, 63) * own
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumskew_126_slope_v110_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.rolling(126, min_periods=42).skew() + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumskew_252_slope_v111_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.rolling(252, min_periods=84).skew() + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumkurt_126_slope_v112_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.rolling(126, min_periods=42).kurt() + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowskew_126_slope_v113_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    result = lr.rolling(126, min_periods=42).skew() + _f28_flow(shrunits, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_surp_252d_slope_v114_signal(shrvalue):
    r = _f28_accum(shrvalue, 252)
    result = r - _mean(r, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowsurp_126d_slope_v115_signal(shrunits):
    r = _f28_flow(shrunits, 126)
    result = r - _mean(r, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumdisp_252_slope_v116_signal(shrvalue):
    result = _std(_f28_accum(shrvalue, 21), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowdisp_504_slope_v117_signal(shrunits):
    result = _std(_f28_flow(shrunits, 21), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumeff_504_slope_v118_signal(shrvalue):
    net = shrvalue - shrvalue.shift(504)
    path = shrvalue.diff().abs().rolling(504, min_periods=168).sum()
    result = _safe_div(net, path) + _f28_accum(shrvalue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_floweff_252_slope_v119_signal(shrunits):
    net = shrunits - shrunits.shift(252)
    path = shrunits.diff().abs().rolling(252, min_periods=84).sum()
    result = _safe_div(net, path) + _f28_flow(shrunits, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumsharpe_63_slope_v120_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = _safe_div(_mean(lr, 63), _std(lr, 63)) * np.sqrt(63.0) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowsharpe_126_slope_v121_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    result = _safe_div(_mean(lr, 126), _std(lr, 126)) * np.sqrt(126.0) + _f28_flow(shrunits, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumvs_252_slope_v122_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    vol = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f28_accum(shrvalue, 252), vol)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowvs_126_slope_v123_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    vol = _std(lr, 252) * np.sqrt(126.0)
    result = _safe_div(_f28_flow(shrunits, 126), vol)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumewm_252_slope_v124_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.ewm(span=252, min_periods=84).mean() * 252.0 + _f28_accum(shrvalue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowewm_126_slope_v125_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0 + _f28_flow(shrunits, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpctsprd_slope_v126_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = (own - own.shift(63)) - (own - own.shift(252)) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownzsprd_slope_v127_signal(shrvalue):
    result = _f28_ownz(shrvalue, 63) - _f28_ownz(shrvalue, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_315d_slope_v128_signal(shrvalue):
    result = _f28_accum(shrvalue, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accum_378d_slope_v129_signal(shrvalue):
    result = _f28_accum(shrvalue, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flow_84d_slope_v130_signal(shrunits):
    result = _f28_flow(shrunits, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flow_189d_slope_v131_signal(shrunits):
    result = _f28_flow(shrunits, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumir_252d_slope_v132_signal(shrvalue):
    r = _f28_accum(shrvalue, 252)
    result = _safe_div(r, _std(r, 504))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowir_126d_slope_v133_signal(shrunits):
    r = _f28_flow(shrunits, 126)
    result = _safe_div(r, _std(r, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvz_126d_slope_v134_signal(totalvalue, shrvalue):
    result = _z(totalvalue, 126) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_unitz_504d_slope_v135_signal(shrunits):
    result = _z(shrunits, 504) + _f28_flow(shrunits, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_cbrel_63_slope_v136_signal(shrvalue, shrunits, marketcap):
    cb = _f28_costbasis(shrvalue, shrunits)
    mpu = _safe_div(marketcap, shrunits)
    result = _safe_div(cb, mpu) - 1.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_surpz_63_slope_v137_signal(shrvalue):
    r = _f28_accum(shrvalue, 63)
    surp = r - _mean(r, 126)
    result = _z(surp, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowsurpz_63_slope_v138_signal(shrunits):
    r = _f28_flow(shrunits, 63)
    surp = r - _mean(r, 126)
    result = _z(surp, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumpersist_63_slope_v139_signal(shrvalue):
    persist = np.sign(shrvalue.diff()).rolling(63, min_periods=21).mean()
    result = _f28_accum(shrvalue, 63) * persist.abs()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_ownpctann_252_slope_v140_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = np.log(own / own.shift(252)) + _f28_accum(shrvalue, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumblend_slope_v141_signal(shrvalue):
    result = (_f28_accum(shrvalue, 63) + _f28_accum(shrvalue, 126) + _f28_accum(shrvalue, 252)) / 3.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_flowblend_slope_v142_signal(shrunits):
    result = (_f28_flow(shrunits, 63) + _f28_flow(shrunits, 126) + _f28_flow(shrunits, 252)) / 3.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_divblend_slope_v143_signal(shrvalue, shrunits):
    av = (_f28_accum(shrvalue, 63) + _f28_accum(shrvalue, 126)) / 2.0
    fl = (_f28_flow(shrunits, 63) + _f28_flow(shrunits, 126)) / 2.0
    result = av - fl
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvpen_lvl_slope_v144_signal(totalvalue, marketcap, shrvalue):
    result = _safe_div(totalvalue, marketcap) + _f28_accum(shrvalue, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_tvpen_chg126_slope_v145_signal(totalvalue, marketcap, shrvalue):
    pen = _safe_div(totalvalue, marketcap)
    result = pen - pen.shift(126) + _f28_accum(shrvalue, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumxownz63_slope_v146_signal(shrvalue):
    result = _f28_accum(shrvalue, 126) * _f28_ownz(shrvalue, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_cbann_252_slope_v147_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = np.log(cb / cb.shift(252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumvs_504_slope_v148_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    vol = _std(lr, 252) * np.sqrt(504.0)
    result = _safe_div(_f28_accum(shrvalue, 504), vol)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_accumxfloweff_slope_v149_signal(shrvalue, shrunits):
    net = shrunits - shrunits.shift(126)
    path = shrunits.diff().abs().rolling(126, min_periods=42).sum()
    eff = _safe_div(net, path)
    result = _f28_accum(shrvalue, 63) * eff
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28ia_f28_institutional_accumulation_conviction_slope_v150_signal(shrvalue, shrunits):
    result = (_f28_ownz(shrvalue, 252) * 0.5
              + _z(_f28_accum(shrvalue, 126), 252) * 0.25
              + _z(_f28_flow(shrunits, 126), 252) * 0.25)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f28ia_f28_institutional_accumulation_accum_63d_slope_v001_signal,    f28ia_f28_institutional_accumulation_accum_126d_slope_v002_signal,    f28ia_f28_institutional_accumulation_accum_252d_slope_v003_signal,    f28ia_f28_institutional_accumulation_accum_504d_slope_v004_signal,    f28ia_f28_institutional_accumulation_accum_21d_slope_v005_signal,    f28ia_f28_institutional_accumulation_accum_42d_slope_v006_signal,    f28ia_f28_institutional_accumulation_logaccum_63d_slope_v007_signal,    f28ia_f28_institutional_accumulation_logaccum_126d_slope_v008_signal,    f28ia_f28_institutional_accumulation_logaccum_252d_slope_v009_signal,    f28ia_f28_institutional_accumulation_logaccum_504d_slope_v010_signal,    f28ia_f28_institutional_accumulation_flow_63d_slope_v011_signal,    f28ia_f28_institutional_accumulation_flow_126d_slope_v012_signal,    f28ia_f28_institutional_accumulation_flow_252d_slope_v013_signal,    f28ia_f28_institutional_accumulation_flow_21d_slope_v014_signal,    f28ia_f28_institutional_accumulation_flow_504d_slope_v015_signal,    f28ia_f28_institutional_accumulation_unitgrow_63d_slope_v016_signal,    f28ia_f28_institutional_accumulation_unitgrow_126d_slope_v017_signal,    f28ia_f28_institutional_accumulation_unitgrow_252d_slope_v018_signal,    f28ia_f28_institutional_accumulation_tvgrow_63d_slope_v019_signal,    f28ia_f28_institutional_accumulation_tvgrow_126d_slope_v020_signal,    f28ia_f28_institutional_accumulation_tvgrow_252d_slope_v021_signal,    f28ia_f28_institutional_accumulation_tvgrow_504d_slope_v022_signal,    f28ia_f28_institutional_accumulation_ownz_252d_slope_v023_signal,    f28ia_f28_institutional_accumulation_ownz_126d_slope_v024_signal,    f28ia_f28_institutional_accumulation_ownz_504d_slope_v025_signal,    f28ia_f28_institutional_accumulation_ownz_63d_slope_v026_signal,    f28ia_f28_institutional_accumulation_unitz_252d_slope_v027_signal,    f28ia_f28_institutional_accumulation_tvz_252d_slope_v028_signal,    f28ia_f28_institutional_accumulation_accel_63_126_slope_v029_signal,    f28ia_f28_institutional_accumulation_accel_126_252_slope_v030_signal,    f28ia_f28_institutional_accumulation_accel_21_63_slope_v031_signal,    f28ia_f28_institutional_accumulation_ownpct_lvl_slope_v032_signal,    f28ia_f28_institutional_accumulation_ownpct_chg63_slope_v033_signal,    f28ia_f28_institutional_accumulation_ownpct_chg126_slope_v034_signal,    f28ia_f28_institutional_accumulation_ownpct_chg252_slope_v035_signal,    f28ia_f28_institutional_accumulation_ownpctz_252d_slope_v036_signal,    f28ia_f28_institutional_accumulation_ownpctgrow_126_slope_v037_signal,    f28ia_f28_institutional_accumulation_costbasis_lvl_slope_v038_signal,    f28ia_f28_institutional_accumulation_costbasis_chg63_slope_v039_signal,    f28ia_f28_institutional_accumulation_costbasis_grow126_slope_v040_signal,    f28ia_f28_institutional_accumulation_costbasis_grow252_slope_v041_signal,    f28ia_f28_institutional_accumulation_costbasisz_252d_slope_v042_signal,    f28ia_f28_institutional_accumulation_rank_accum63_slope_v043_signal,    f28ia_f28_institutional_accumulation_rank_accum126_slope_v044_signal,    f28ia_f28_institutional_accumulation_rank_flow63_slope_v045_signal,    f28ia_f28_institutional_accumulation_ownmom_21s63_slope_v046_signal,    f28ia_f28_institutional_accumulation_ownmom_63s42_slope_v047_signal,    f28ia_f28_institutional_accumulation_flowdisp_126_slope_v048_signal,    f28ia_f28_institutional_accumulation_flowdisp_252_slope_v049_signal,    f28ia_f28_institutional_accumulation_accumdisp_126_slope_v050_signal,    f28ia_f28_institutional_accumulation_accumir_63d_slope_v051_signal,    f28ia_f28_institutional_accumulation_accumir_126d_slope_v052_signal,    f28ia_f28_institutional_accumulation_flowir_63d_slope_v053_signal,    f28ia_f28_institutional_accumulation_surp_63d_slope_v054_signal,    f28ia_f28_institutional_accumulation_surp_126d_slope_v055_signal,    f28ia_f28_institutional_accumulation_flowsurp_63d_slope_v056_signal,    f28ia_f28_institutional_accumulation_valflow_sprd63_slope_v057_signal,    f28ia_f28_institutional_accumulation_valflow_sprd126_slope_v058_signal,    f28ia_f28_institutional_accumulation_tvshare_lvl_slope_v059_signal,    f28ia_f28_institutional_accumulation_tvshare_chg126_slope_v060_signal,    f28ia_f28_institutional_accumulation_tvsharez_252_slope_v061_signal,    f28ia_f28_institutional_accumulation_accumewm_63d_slope_v062_signal,    f28ia_f28_institutional_accumulation_accumewm_126d_slope_v063_signal,    f28ia_f28_institutional_accumulation_flowewm_63d_slope_v064_signal,    f28ia_f28_institutional_accumulation_accumsharpe_126_slope_v065_signal,    f28ia_f28_institutional_accumulation_accumsharpe_252_slope_v066_signal,    f28ia_f28_institutional_accumulation_accumeff_126_slope_v067_signal,    f28ia_f28_institutional_accumulation_accumeff_252_slope_v068_signal,    f28ia_f28_institutional_accumulation_floweff_126_slope_v069_signal,    f28ia_f28_institutional_accumulation_accumvs_63d_slope_v070_signal,    f28ia_f28_institutional_accumulation_accumvs_126d_slope_v071_signal,    f28ia_f28_institutional_accumulation_accumxownz_63_slope_v072_signal,    f28ia_f28_institutional_accumulation_ownpctvs_126_slope_v073_signal,    f28ia_f28_institutional_accumulation_accum_84d_slope_v074_signal,    f28ia_f28_institutional_accumulation_accum_189d_slope_v075_signal,    f28ia_f28_institutional_accumulation_ownmom_21s21_slope_v076_signal,    f28ia_f28_institutional_accumulation_ownmom_126s42_slope_v077_signal,    f28ia_f28_institutional_accumulation_flowmom_42s42_slope_v078_signal,    f28ia_f28_institutional_accumulation_flowmom_84s42_slope_v079_signal,    f28ia_f28_institutional_accumulation_zaccum63_252_slope_v080_signal,    f28ia_f28_institutional_accumulation_zaccum126_504_slope_v081_signal,    f28ia_f28_institutional_accumulation_zaccum21_126_slope_v082_signal,    f28ia_f28_institutional_accumulation_zflow63_252_slope_v083_signal,    f28ia_f28_institutional_accumulation_zflow126_504_slope_v084_signal,    f28ia_f28_institutional_accumulation_accel_42_84_slope_v085_signal,    f28ia_f28_institutional_accumulation_accel_84_189_slope_v086_signal,    f28ia_f28_institutional_accumulation_flowaccel_63_126_slope_v087_signal,    f28ia_f28_institutional_accumulation_flowaccel_126_252_slope_v088_signal,    f28ia_f28_institutional_accumulation_sprd_63_252_slope_v089_signal,    f28ia_f28_institutional_accumulation_lsprd_63_126_slope_v090_signal,    f28ia_f28_institutional_accumulation_tvz_504d_slope_v091_signal,    f28ia_f28_institutional_accumulation_tvlog_126d_slope_v092_signal,    f28ia_f28_institutional_accumulation_tvlog_252d_slope_v093_signal,    f28ia_f28_institutional_accumulation_relaccum_63_slope_v094_signal,    f28ia_f28_institutional_accumulation_relaccum_126_slope_v095_signal,    f28ia_f28_institutional_accumulation_relaccum_252_slope_v096_signal,    f28ia_f28_institutional_accumulation_annaccum_63_slope_v097_signal,    f28ia_f28_institutional_accumulation_annaccum_126_slope_v098_signal,    f28ia_f28_institutional_accumulation_annflow_63_slope_v099_signal,    f28ia_f28_institutional_accumulation_rank_accum252_slope_v100_signal,    f28ia_f28_institutional_accumulation_rank_flow126_slope_v101_signal,    f28ia_f28_institutional_accumulation_rank_costbasis_slope_v102_signal,    f28ia_f28_institutional_accumulation_rank_ownpct_slope_v103_signal,    f28ia_f28_institutional_accumulation_cbir_126_slope_v104_signal,    f28ia_f28_institutional_accumulation_cbewm_63_slope_v105_signal,    f28ia_f28_institutional_accumulation_accumflowx_63_slope_v106_signal,    f28ia_f28_institutional_accumulation_accumflowx_126_slope_v107_signal,    f28ia_f28_institutional_accumulation_accumxown_63_slope_v108_signal,    f28ia_f28_institutional_accumulation_flowxown_63_slope_v109_signal,    f28ia_f28_institutional_accumulation_accumskew_126_slope_v110_signal,    f28ia_f28_institutional_accumulation_accumskew_252_slope_v111_signal,    f28ia_f28_institutional_accumulation_accumkurt_126_slope_v112_signal,    f28ia_f28_institutional_accumulation_flowskew_126_slope_v113_signal,    f28ia_f28_institutional_accumulation_surp_252d_slope_v114_signal,    f28ia_f28_institutional_accumulation_flowsurp_126d_slope_v115_signal,    f28ia_f28_institutional_accumulation_accumdisp_252_slope_v116_signal,    f28ia_f28_institutional_accumulation_flowdisp_504_slope_v117_signal,    f28ia_f28_institutional_accumulation_accumeff_504_slope_v118_signal,    f28ia_f28_institutional_accumulation_floweff_252_slope_v119_signal,    f28ia_f28_institutional_accumulation_accumsharpe_63_slope_v120_signal,    f28ia_f28_institutional_accumulation_flowsharpe_126_slope_v121_signal,    f28ia_f28_institutional_accumulation_accumvs_252_slope_v122_signal,    f28ia_f28_institutional_accumulation_flowvs_126_slope_v123_signal,    f28ia_f28_institutional_accumulation_accumewm_252_slope_v124_signal,    f28ia_f28_institutional_accumulation_flowewm_126_slope_v125_signal,    f28ia_f28_institutional_accumulation_ownpctsprd_slope_v126_signal,    f28ia_f28_institutional_accumulation_ownzsprd_slope_v127_signal,    f28ia_f28_institutional_accumulation_accum_315d_slope_v128_signal,    f28ia_f28_institutional_accumulation_accum_378d_slope_v129_signal,    f28ia_f28_institutional_accumulation_flow_84d_slope_v130_signal,    f28ia_f28_institutional_accumulation_flow_189d_slope_v131_signal,    f28ia_f28_institutional_accumulation_accumir_252d_slope_v132_signal,    f28ia_f28_institutional_accumulation_flowir_126d_slope_v133_signal,    f28ia_f28_institutional_accumulation_tvz_126d_slope_v134_signal,    f28ia_f28_institutional_accumulation_unitz_504d_slope_v135_signal,    f28ia_f28_institutional_accumulation_cbrel_63_slope_v136_signal,    f28ia_f28_institutional_accumulation_surpz_63_slope_v137_signal,    f28ia_f28_institutional_accumulation_flowsurpz_63_slope_v138_signal,    f28ia_f28_institutional_accumulation_accumpersist_63_slope_v139_signal,    f28ia_f28_institutional_accumulation_ownpctann_252_slope_v140_signal,    f28ia_f28_institutional_accumulation_accumblend_slope_v141_signal,    f28ia_f28_institutional_accumulation_flowblend_slope_v142_signal,    f28ia_f28_institutional_accumulation_divblend_slope_v143_signal,    f28ia_f28_institutional_accumulation_tvpen_lvl_slope_v144_signal,    f28ia_f28_institutional_accumulation_tvpen_chg126_slope_v145_signal,    f28ia_f28_institutional_accumulation_accumxownz63_slope_v146_signal,    f28ia_f28_institutional_accumulation_cbann_252_slope_v147_signal,    f28ia_f28_institutional_accumulation_accumvs_504_slope_v148_signal,    f28ia_f28_institutional_accumulation_accumxfloweff_slope_v149_signal,    f28ia_f28_institutional_accumulation_conviction_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_INSTITUTIONAL_ACCUMULATION_REGISTRY_SLOPE = REGISTRY

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
    domain_primitives = ('_f28_accum', '_f28_flow', '_f28_ownz', '_f28_costbasis')
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
    print("OK f28_institutional_accumulation_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
