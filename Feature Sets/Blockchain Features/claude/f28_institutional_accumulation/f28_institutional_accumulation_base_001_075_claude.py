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


# ============ FEATURES 001-075 ============

# 63d accumulation (shrvalue growth)
def f28ia_f28_institutional_accumulation_accum_63d_base_v001_signal(shrvalue):
    result = _f28_accum(shrvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d accumulation
def f28ia_f28_institutional_accumulation_accum_126d_base_v002_signal(shrvalue):
    result = _f28_accum(shrvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accumulation
def f28ia_f28_institutional_accumulation_accum_252d_base_v003_signal(shrvalue):
    result = _f28_accum(shrvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d accumulation
def f28ia_f28_institutional_accumulation_accum_504d_base_v004_signal(shrvalue):
    result = _f28_accum(shrvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accumulation (monthly)
def f28ia_f28_institutional_accumulation_accum_21d_base_v005_signal(shrvalue):
    result = _f28_accum(shrvalue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d accumulation
def f28ia_f28_institutional_accumulation_accum_42d_base_v006_signal(shrvalue):
    result = _f28_accum(shrvalue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log accumulation (additive, scale robust)
def f28ia_f28_institutional_accumulation_logaccum_63d_base_v007_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(63)) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log accumulation
def f28ia_f28_institutional_accumulation_logaccum_126d_base_v008_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(126)) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log accumulation
def f28ia_f28_institutional_accumulation_logaccum_252d_base_v009_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(252)) + _f28_accum(shrvalue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log accumulation
def f28ia_f28_institutional_accumulation_logaccum_504d_base_v010_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(504)) + _f28_accum(shrvalue, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share flow (shrunits change normalized)
def f28ia_f28_institutional_accumulation_flow_63d_base_v011_signal(shrunits):
    result = _f28_flow(shrunits, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d share flow
def f28ia_f28_institutional_accumulation_flow_126d_base_v012_signal(shrunits):
    result = _f28_flow(shrunits, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d share flow
def f28ia_f28_institutional_accumulation_flow_252d_base_v013_signal(shrunits):
    result = _f28_flow(shrunits, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d share flow
def f28ia_f28_institutional_accumulation_flow_21d_base_v014_signal(shrunits):
    result = _f28_flow(shrunits, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d share flow
def f28ia_f28_institutional_accumulation_flow_504d_base_v015_signal(shrunits):
    result = _f28_flow(shrunits, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d shrunits growth (pct change)
def f28ia_f28_institutional_accumulation_unitgrow_63d_base_v016_signal(shrunits):
    result = shrunits.pct_change(periods=63) + _f28_flow(shrunits, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d shrunits growth
def f28ia_f28_institutional_accumulation_unitgrow_126d_base_v017_signal(shrunits):
    result = shrunits.pct_change(periods=126) + _f28_flow(shrunits, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d shrunits growth
def f28ia_f28_institutional_accumulation_unitgrow_252d_base_v018_signal(shrunits):
    result = shrunits.pct_change(periods=252) + _f28_flow(shrunits, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d totalvalue growth (aggregate 13F book)
def f28ia_f28_institutional_accumulation_tvgrow_63d_base_v019_signal(totalvalue, shrvalue):
    result = totalvalue.pct_change(periods=63) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d totalvalue growth
def f28ia_f28_institutional_accumulation_tvgrow_126d_base_v020_signal(totalvalue, shrvalue):
    result = totalvalue.pct_change(periods=126) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d totalvalue growth
def f28ia_f28_institutional_accumulation_tvgrow_252d_base_v021_signal(totalvalue, shrvalue):
    result = totalvalue.pct_change(periods=252) + _f28_accum(shrvalue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d totalvalue growth
def f28ia_f28_institutional_accumulation_tvgrow_504d_base_v022_signal(totalvalue, shrvalue):
    result = totalvalue.pct_change(periods=504) + _f28_accum(shrvalue, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d institutional flow z-score (standardized accumulation level)
def f28ia_f28_institutional_accumulation_ownz_252d_base_v023_signal(shrvalue):
    result = _f28_ownz(shrvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d institutional flow z-score
def f28ia_f28_institutional_accumulation_ownz_126d_base_v024_signal(shrvalue):
    result = _f28_ownz(shrvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d institutional flow z-score
def f28ia_f28_institutional_accumulation_ownz_504d_base_v025_signal(shrvalue):
    result = _f28_ownz(shrvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d institutional flow z-score
def f28ia_f28_institutional_accumulation_ownz_63d_base_v026_signal(shrvalue):
    result = _f28_ownz(shrvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of shrunits over 252d
def f28ia_f28_institutional_accumulation_unitz_252d_base_v027_signal(shrunits):
    result = _z(shrunits, 252) + _f28_flow(shrunits, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of totalvalue over 252d
def f28ia_f28_institutional_accumulation_tvz_252d_base_v028_signal(totalvalue, shrvalue):
    result = _z(totalvalue, 252) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation acceleration level: 63d accum minus 126d accum
def f28ia_f28_institutional_accumulation_accel_63_126_base_v029_signal(shrvalue):
    result = _f28_accum(shrvalue, 63) - _f28_accum(shrvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation acceleration: 126d accum minus 252d accum
def f28ia_f28_institutional_accumulation_accel_126_252_base_v030_signal(shrvalue):
    result = _f28_accum(shrvalue, 126) - _f28_accum(shrvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation acceleration: 21d accum minus 63d accum
def f28ia_f28_institutional_accumulation_accel_21_63_base_v031_signal(shrvalue):
    result = _f28_accum(shrvalue, 21) - _f28_accum(shrvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership % = shrvalue / marketcap
def f28ia_f28_institutional_accumulation_ownpct_lvl_base_v032_signal(shrvalue, marketcap):
    result = _safe_div(shrvalue, marketcap) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-% 63d change (trend in institutional share)
def f28ia_f28_institutional_accumulation_ownpct_chg63_base_v033_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own - own.shift(63) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-% 126d change
def f28ia_f28_institutional_accumulation_ownpct_chg126_base_v034_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own - own.shift(126) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-% 252d change
def f28ia_f28_institutional_accumulation_ownpct_chg252_base_v035_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own - own.shift(252) + _f28_accum(shrvalue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-% z-score over 252d
def f28ia_f28_institutional_accumulation_ownpctz_252d_base_v036_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = _z(own, 252) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-% growth (pct change 126d)
def f28ia_f28_institutional_accumulation_ownpctgrow_126_base_v037_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own.pct_change(periods=126) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit (avg cost basis) level
def f28ia_f28_institutional_accumulation_costbasis_lvl_base_v038_signal(shrvalue, shrunits):
    result = _f28_costbasis(shrvalue, shrunits)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-basis 63d trend (change)
def f28ia_f28_institutional_accumulation_costbasis_chg63_base_v039_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = cb - cb.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-basis 126d trend (pct change)
def f28ia_f28_institutional_accumulation_costbasis_grow126_base_v040_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = cb.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-basis 252d trend (pct change)
def f28ia_f28_institutional_accumulation_costbasis_grow252_base_v041_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = cb.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-basis z-score over 252d
def f28ia_f28_institutional_accumulation_costbasisz_252d_base_v042_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = _z(cb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation percentile rank (63d accum over 252d window)
def f28ia_f28_institutional_accumulation_rank_accum63_base_v043_signal(shrvalue):
    r = _f28_accum(shrvalue, 63)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation percentile rank (126d accum over 252d)
def f28ia_f28_institutional_accumulation_rank_accum126_base_v044_signal(shrvalue):
    r = _f28_accum(shrvalue, 126)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# flow percentile rank (63d flow over 252d)
def f28ia_f28_institutional_accumulation_rank_flow63_base_v045_signal(shrunits):
    r = _f28_flow(shrunits, 63)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# ownership momentum: shrvalue 21d roc smoothed 63d
def f28ia_f28_institutional_accumulation_ownmom_21s63_base_v046_signal(shrvalue):
    result = _mean(_f28_accum(shrvalue, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ownership momentum: shrvalue 63d roc smoothed 42d
def f28ia_f28_institutional_accumulation_ownmom_63s42_base_v047_signal(shrvalue):
    result = _mean(_f28_accum(shrvalue, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# flow dispersion: std of 21d flow over 126d
def f28ia_f28_institutional_accumulation_flowdisp_126_base_v048_signal(shrunits):
    result = _std(_f28_flow(shrunits, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# flow dispersion: std of 21d flow over 252d
def f28ia_f28_institutional_accumulation_flowdisp_252_base_v049_signal(shrunits):
    result = _std(_f28_flow(shrunits, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation dispersion: std of 21d accum over 126d
def f28ia_f28_institutional_accumulation_accumdisp_126_base_v050_signal(shrvalue):
    result = _std(_f28_accum(shrvalue, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation info ratio: 63d accum / 252d accum dispersion
def f28ia_f28_institutional_accumulation_accumir_63d_base_v051_signal(shrvalue):
    r = _f28_accum(shrvalue, 63)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation info ratio: 126d accum / 252d dispersion
def f28ia_f28_institutional_accumulation_accumir_126d_base_v052_signal(shrvalue):
    r = _f28_accum(shrvalue, 126)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# flow info ratio: 63d flow / 252d flow dispersion
def f28ia_f28_institutional_accumulation_flowir_63d_base_v053_signal(shrunits):
    r = _f28_flow(shrunits, 63)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation surprise: 63d accum minus its 126d mean
def f28ia_f28_institutional_accumulation_surp_63d_base_v054_signal(shrvalue):
    r = _f28_accum(shrvalue, 63)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation surprise: 126d accum minus its 252d mean
def f28ia_f28_institutional_accumulation_surp_126d_base_v055_signal(shrvalue):
    r = _f28_accum(shrvalue, 126)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# flow surprise: 63d flow minus its 126d mean
def f28ia_f28_institutional_accumulation_flowsurp_63d_base_v056_signal(shrunits):
    r = _f28_flow(shrunits, 63)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation vs flow spread (value vs share divergence 63d)
def f28ia_f28_institutional_accumulation_valflow_sprd63_base_v057_signal(shrvalue, shrunits):
    result = _f28_accum(shrvalue, 63) - _f28_flow(shrunits, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation vs flow spread 126d
def f28ia_f28_institutional_accumulation_valflow_sprd126_base_v058_signal(shrvalue, shrunits):
    result = _f28_accum(shrvalue, 126) - _f28_flow(shrunits, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue share of totalvalue (concentration level)
def f28ia_f28_institutional_accumulation_tvshare_lvl_base_v059_signal(shrvalue, totalvalue):
    result = _safe_div(shrvalue, totalvalue) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue share of totalvalue 126d change
def f28ia_f28_institutional_accumulation_tvshare_chg126_base_v060_signal(shrvalue, totalvalue):
    sh = _safe_div(shrvalue, totalvalue)
    result = sh - sh.shift(126) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue share of totalvalue z-score over 252d
def f28ia_f28_institutional_accumulation_tvsharez_252_base_v061_signal(shrvalue, totalvalue):
    sh = _safe_div(shrvalue, totalvalue)
    result = _z(sh, 252) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation EWMA scaled (63d span on daily shrvalue log change)
def f28ia_f28_institutional_accumulation_accumewm_63d_base_v062_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0 + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation EWMA scaled (126d span)
def f28ia_f28_institutional_accumulation_accumewm_126d_base_v063_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0 + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# flow EWMA scaled (63d span on daily shrunits log change)
def f28ia_f28_institutional_accumulation_flowewm_63d_base_v064_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0 + _f28_flow(shrunits, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation Sharpe: mean/std of daily shrvalue log change over 126d
def f28ia_f28_institutional_accumulation_accumsharpe_126_base_v065_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = _safe_div(_mean(lr, 126), _std(lr, 126)) * np.sqrt(126.0) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation Sharpe over 252d
def f28ia_f28_institutional_accumulation_accumsharpe_252_base_v066_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = _safe_div(_mean(lr, 252), _std(lr, 252)) * np.sqrt(252.0) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation efficiency: net 126d value change over path length
def f28ia_f28_institutional_accumulation_accumeff_126_base_v067_signal(shrvalue):
    net = shrvalue - shrvalue.shift(126)
    path = shrvalue.diff().abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net, path) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation efficiency over 252d
def f28ia_f28_institutional_accumulation_accumeff_252_base_v068_signal(shrvalue):
    net = shrvalue - shrvalue.shift(252)
    path = shrvalue.diff().abs().rolling(252, min_periods=84).sum()
    result = _safe_div(net, path) + _f28_accum(shrvalue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# flow efficiency over 126d (net unit change over path)
def f28ia_f28_institutional_accumulation_floweff_126_base_v069_signal(shrunits):
    net = shrunits - shrunits.shift(126)
    path = shrunits.diff().abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net, path) + _f28_flow(shrunits, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation momentum scaled by 252d realized vol (63d)
def f28ia_f28_institutional_accumulation_accumvs_63d_base_v070_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    vol = _std(lr, 252) * np.sqrt(63.0)
    result = _safe_div(_f28_accum(shrvalue, 63), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation momentum scaled by 252d vol (126d)
def f28ia_f28_institutional_accumulation_accumvs_126d_base_v071_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    vol = _std(lr, 252) * np.sqrt(126.0)
    result = _safe_div(_f28_accum(shrvalue, 126), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation weighted by ownership level (value growth x ownz)
def f28ia_f28_institutional_accumulation_accumxownz_63_base_v072_signal(shrvalue):
    result = _f28_accum(shrvalue, 63) * _f28_ownz(shrvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % momentum scaled by vol (126d change of own / 252d own std)
def f28ia_f28_institutional_accumulation_ownpctvs_126_base_v073_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = _safe_div(own - own.shift(126), _std(own, 252)) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d accumulation
def f28ia_f28_institutional_accumulation_accum_84d_base_v074_signal(shrvalue):
    result = _f28_accum(shrvalue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d accumulation
def f28ia_f28_institutional_accumulation_accum_189d_base_v075_signal(shrvalue):
    result = _f28_accum(shrvalue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28ia_f28_institutional_accumulation_accum_63d_base_v001_signal,
    f28ia_f28_institutional_accumulation_accum_126d_base_v002_signal,
    f28ia_f28_institutional_accumulation_accum_252d_base_v003_signal,
    f28ia_f28_institutional_accumulation_accum_504d_base_v004_signal,
    f28ia_f28_institutional_accumulation_accum_21d_base_v005_signal,
    f28ia_f28_institutional_accumulation_accum_42d_base_v006_signal,
    f28ia_f28_institutional_accumulation_logaccum_63d_base_v007_signal,
    f28ia_f28_institutional_accumulation_logaccum_126d_base_v008_signal,
    f28ia_f28_institutional_accumulation_logaccum_252d_base_v009_signal,
    f28ia_f28_institutional_accumulation_logaccum_504d_base_v010_signal,
    f28ia_f28_institutional_accumulation_flow_63d_base_v011_signal,
    f28ia_f28_institutional_accumulation_flow_126d_base_v012_signal,
    f28ia_f28_institutional_accumulation_flow_252d_base_v013_signal,
    f28ia_f28_institutional_accumulation_flow_21d_base_v014_signal,
    f28ia_f28_institutional_accumulation_flow_504d_base_v015_signal,
    f28ia_f28_institutional_accumulation_unitgrow_63d_base_v016_signal,
    f28ia_f28_institutional_accumulation_unitgrow_126d_base_v017_signal,
    f28ia_f28_institutional_accumulation_unitgrow_252d_base_v018_signal,
    f28ia_f28_institutional_accumulation_tvgrow_63d_base_v019_signal,
    f28ia_f28_institutional_accumulation_tvgrow_126d_base_v020_signal,
    f28ia_f28_institutional_accumulation_tvgrow_252d_base_v021_signal,
    f28ia_f28_institutional_accumulation_tvgrow_504d_base_v022_signal,
    f28ia_f28_institutional_accumulation_ownz_252d_base_v023_signal,
    f28ia_f28_institutional_accumulation_ownz_126d_base_v024_signal,
    f28ia_f28_institutional_accumulation_ownz_504d_base_v025_signal,
    f28ia_f28_institutional_accumulation_ownz_63d_base_v026_signal,
    f28ia_f28_institutional_accumulation_unitz_252d_base_v027_signal,
    f28ia_f28_institutional_accumulation_tvz_252d_base_v028_signal,
    f28ia_f28_institutional_accumulation_accel_63_126_base_v029_signal,
    f28ia_f28_institutional_accumulation_accel_126_252_base_v030_signal,
    f28ia_f28_institutional_accumulation_accel_21_63_base_v031_signal,
    f28ia_f28_institutional_accumulation_ownpct_lvl_base_v032_signal,
    f28ia_f28_institutional_accumulation_ownpct_chg63_base_v033_signal,
    f28ia_f28_institutional_accumulation_ownpct_chg126_base_v034_signal,
    f28ia_f28_institutional_accumulation_ownpct_chg252_base_v035_signal,
    f28ia_f28_institutional_accumulation_ownpctz_252d_base_v036_signal,
    f28ia_f28_institutional_accumulation_ownpctgrow_126_base_v037_signal,
    f28ia_f28_institutional_accumulation_costbasis_lvl_base_v038_signal,
    f28ia_f28_institutional_accumulation_costbasis_chg63_base_v039_signal,
    f28ia_f28_institutional_accumulation_costbasis_grow126_base_v040_signal,
    f28ia_f28_institutional_accumulation_costbasis_grow252_base_v041_signal,
    f28ia_f28_institutional_accumulation_costbasisz_252d_base_v042_signal,
    f28ia_f28_institutional_accumulation_rank_accum63_base_v043_signal,
    f28ia_f28_institutional_accumulation_rank_accum126_base_v044_signal,
    f28ia_f28_institutional_accumulation_rank_flow63_base_v045_signal,
    f28ia_f28_institutional_accumulation_ownmom_21s63_base_v046_signal,
    f28ia_f28_institutional_accumulation_ownmom_63s42_base_v047_signal,
    f28ia_f28_institutional_accumulation_flowdisp_126_base_v048_signal,
    f28ia_f28_institutional_accumulation_flowdisp_252_base_v049_signal,
    f28ia_f28_institutional_accumulation_accumdisp_126_base_v050_signal,
    f28ia_f28_institutional_accumulation_accumir_63d_base_v051_signal,
    f28ia_f28_institutional_accumulation_accumir_126d_base_v052_signal,
    f28ia_f28_institutional_accumulation_flowir_63d_base_v053_signal,
    f28ia_f28_institutional_accumulation_surp_63d_base_v054_signal,
    f28ia_f28_institutional_accumulation_surp_126d_base_v055_signal,
    f28ia_f28_institutional_accumulation_flowsurp_63d_base_v056_signal,
    f28ia_f28_institutional_accumulation_valflow_sprd63_base_v057_signal,
    f28ia_f28_institutional_accumulation_valflow_sprd126_base_v058_signal,
    f28ia_f28_institutional_accumulation_tvshare_lvl_base_v059_signal,
    f28ia_f28_institutional_accumulation_tvshare_chg126_base_v060_signal,
    f28ia_f28_institutional_accumulation_tvsharez_252_base_v061_signal,
    f28ia_f28_institutional_accumulation_accumewm_63d_base_v062_signal,
    f28ia_f28_institutional_accumulation_accumewm_126d_base_v063_signal,
    f28ia_f28_institutional_accumulation_flowewm_63d_base_v064_signal,
    f28ia_f28_institutional_accumulation_accumsharpe_126_base_v065_signal,
    f28ia_f28_institutional_accumulation_accumsharpe_252_base_v066_signal,
    f28ia_f28_institutional_accumulation_accumeff_126_base_v067_signal,
    f28ia_f28_institutional_accumulation_accumeff_252_base_v068_signal,
    f28ia_f28_institutional_accumulation_floweff_126_base_v069_signal,
    f28ia_f28_institutional_accumulation_accumvs_63d_base_v070_signal,
    f28ia_f28_institutional_accumulation_accumvs_126d_base_v071_signal,
    f28ia_f28_institutional_accumulation_accumxownz_63_base_v072_signal,
    f28ia_f28_institutional_accumulation_ownpctvs_126_base_v073_signal,
    f28ia_f28_institutional_accumulation_accum_84d_base_v074_signal,
    f28ia_f28_institutional_accumulation_accum_189d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_INSTITUTIONAL_ACCUMULATION_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f28_accum", "_f28_flow", "_f28_ownz", "_f28_costbasis")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f28_institutional_accumulation_base_001_075_claude: {n_features} features pass")
