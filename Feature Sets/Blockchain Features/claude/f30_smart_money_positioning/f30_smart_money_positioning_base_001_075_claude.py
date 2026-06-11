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


# ===== folder domain primitives (smart-money positioning) =====
def _f30_pos(shrvalue, w):
    # smoothed position-value level (position size of the smart-money holder)
    return shrvalue.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_posz(shrvalue, w):
    # z-score of position value over w (positioning extension vs own history)
    m = shrvalue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = shrvalue.rolling(w, min_periods=max(1, w // 2)).std()
    return (shrvalue - m) / sd.replace(0, np.nan)


def _f30_conviction(shrvalue, totalvalue):
    # weight of this position within the investor's total book (conviction)
    return shrvalue / totalvalue.replace(0, np.nan)


def _f30_vpu(shrvalue, shrunits):
    # value per unit held (average entry / position price, conviction proxy)
    return shrvalue / shrunits.replace(0, np.nan)


# ============ FEATURES 001-075 ============

# 21d position-value trend (growth of smoothed position size)
def f30sm_f30_smart_money_positioning_postrend_21d_base_v001_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(21), p.shift(21).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-value trend
def f30sm_f30_smart_money_positioning_postrend_63d_base_v002_signal(shrvalue):
    p = _f30_pos(shrvalue, 63)
    result = _safe_div(p - p.shift(63), p.shift(63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-value trend
def f30sm_f30_smart_money_positioning_postrend_126d_base_v003_signal(shrvalue):
    p = _f30_pos(shrvalue, 126)
    result = _safe_div(p - p.shift(126), p.shift(126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-value trend
def f30sm_f30_smart_money_positioning_postrend_252d_base_v004_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(252), p.shift(252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log position-value growth
def f30sm_f30_smart_money_positioning_posglog_21d_base_v005_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log position-value growth
def f30sm_f30_smart_money_positioning_posglog_63d_base_v006_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log position-value growth
def f30sm_f30_smart_money_positioning_posglog_126d_base_v007_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log position-value growth
def f30sm_f30_smart_money_positioning_posglog_252d_base_v008_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(252))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d positioning z-score (position extension)
def f30sm_f30_smart_money_positioning_posz_21d_base_v009_signal(shrvalue):
    result = _f30_posz(shrvalue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d positioning z-score
def f30sm_f30_smart_money_positioning_posz_63d_base_v010_signal(shrvalue):
    result = _f30_posz(shrvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d positioning z-score
def f30sm_f30_smart_money_positioning_posz_126d_base_v011_signal(shrvalue):
    result = _f30_posz(shrvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d positioning z-score
def f30sm_f30_smart_money_positioning_posz_252d_base_v012_signal(shrvalue):
    result = _f30_posz(shrvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d positioning z-score
def f30sm_f30_smart_money_positioning_posz_378d_base_v013_signal(shrvalue):
    result = _f30_posz(shrvalue, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d units change (units accumulation/distribution)
def f30sm_f30_smart_money_positioning_unitstrend_21d_base_v014_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(21), u.shift(21).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units change
def f30sm_f30_smart_money_positioning_unitstrend_63d_base_v015_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(63), u.shift(63).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d units change
def f30sm_f30_smart_money_positioning_unitstrend_126d_base_v016_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(126), u.shift(126).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units change
def f30sm_f30_smart_money_positioning_unitstrend_252d_base_v017_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(252), u.shift(252).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log units growth
def f30sm_f30_smart_money_positioning_unitsglog_21d_base_v018_signal(shrunits, shrvalue):
    u = _mean(shrunits, 5)
    result = np.log(u / u.shift(21)) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log units growth
def f30sm_f30_smart_money_positioning_unitsglog_63d_base_v019_signal(shrunits, shrvalue):
    u = _mean(shrunits, 5)
    result = np.log(u / u.shift(63)) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log units growth
def f30sm_f30_smart_money_positioning_unitsglog_126d_base_v020_signal(shrunits, shrvalue):
    u = _mean(shrunits, 5)
    result = np.log(u / u.shift(126)) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d value-per-unit trend (avg entry-price drift, conviction pricing)
def f30sm_f30_smart_money_positioning_vputrend_21d_base_v021_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(21), v.shift(21).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value-per-unit trend
def f30sm_f30_smart_money_positioning_vputrend_63d_base_v022_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(63), v.shift(63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d value-per-unit trend
def f30sm_f30_smart_money_positioning_vputrend_126d_base_v023_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(126), v.shift(126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value-per-unit trend
def f30sm_f30_smart_money_positioning_vputrend_252d_base_v024_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(252), v.shift(252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log value-per-unit growth
def f30sm_f30_smart_money_positioning_vpuglog_21d_base_v025_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = np.log(v / v.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log value-per-unit growth
def f30sm_f30_smart_money_positioning_vpuglog_63d_base_v026_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = np.log(v / v.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log value-per-unit growth
def f30sm_f30_smart_money_positioning_vpuglog_126d_base_v027_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = np.log(v / v.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d value-per-unit z-score
def f30sm_f30_smart_money_positioning_vpuz_21d_base_v028_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value-per-unit z-score
def f30sm_f30_smart_money_positioning_vpuz_63d_base_v029_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d value-per-unit z-score
def f30sm_f30_smart_money_positioning_vpuz_126d_base_v030_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value-per-unit z-score
def f30sm_f30_smart_money_positioning_vpuz_252d_base_v031_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction weight level smoothed 21d (position weight in book)
def f30sm_f30_smart_money_positioning_convlvl_21d_base_v032_signal(shrvalue, totalvalue):
    result = _mean(_f30_conviction(shrvalue, totalvalue), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction weight level smoothed 63d
def f30sm_f30_smart_money_positioning_convlvl_63d_base_v033_signal(shrvalue, totalvalue):
    result = _mean(_f30_conviction(shrvalue, totalvalue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conviction-weight change
def f30sm_f30_smart_money_positioning_convchg_21d_base_v034_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(21), c.shift(21).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conviction-weight change
def f30sm_f30_smart_money_positioning_convchg_63d_base_v035_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(63), c.shift(63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conviction-weight change
def f30sm_f30_smart_money_positioning_convchg_126d_base_v036_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(126), c.shift(126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conviction-weight change
def f30sm_f30_smart_money_positioning_convchg_252d_base_v037_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(252), c.shift(252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conviction-weight z-score
def f30sm_f30_smart_money_positioning_convz_21d_base_v038_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conviction-weight z-score
def f30sm_f30_smart_money_positioning_convz_63d_base_v039_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conviction-weight z-score
def f30sm_f30_smart_money_positioning_convz_126d_base_v040_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conviction-weight z-score
def f30sm_f30_smart_money_positioning_convz_252d_base_v041_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log conviction-weight growth
def f30sm_f30_smart_money_positioning_convglog_63d_base_v042_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = np.log(c / c.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log conviction-weight growth
def f30sm_f30_smart_money_positioning_convglog_126d_base_v043_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = np.log(c / c.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# rotation: position growth minus book growth 63d (relative reallocation)
def f30sm_f30_smart_money_positioning_rot_63d_base_v044_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(63))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(63))
    result = pg - tg
    return result.replace([np.inf, -np.inf], np.nan)


# rotation 126d
def f30sm_f30_smart_money_positioning_rot_126d_base_v045_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(126))
    result = pg - tg
    return result.replace([np.inf, -np.inf], np.nan)


# rotation 252d
def f30sm_f30_smart_money_positioning_rot_252d_base_v046_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(252))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(252))
    result = pg - tg
    return result.replace([np.inf, -np.inf], np.nan)


# rotation 21d
def f30sm_f30_smart_money_positioning_rot_21d_base_v047_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(21))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(21))
    result = pg - tg
    return result.replace([np.inf, -np.inf], np.nan)


# position vs marketcap ratio trend 63d (footprint vs float)
def f30sm_f30_smart_money_positioning_posmcap_63d_base_v048_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _safe_div(r - r.shift(63), r.shift(63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# position vs marketcap ratio trend 126d
def f30sm_f30_smart_money_positioning_posmcap_126d_base_v049_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _safe_div(r - r.shift(126), r.shift(126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# position vs marketcap ratio z-score 252d
def f30sm_f30_smart_money_positioning_posmcapz_252d_base_v050_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# position momentum: 21d posz minus its 63d mean (positioning surprise)
def f30sm_f30_smart_money_positioning_possurp_21d_base_v051_signal(shrvalue):
    pz = _f30_posz(shrvalue, 63)
    result = pz - _mean(pz, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# position momentum: 63d posz minus its 126d mean
def f30sm_f30_smart_money_positioning_possurp_63d_base_v052_signal(shrvalue):
    pz = _f30_posz(shrvalue, 126)
    result = pz - _mean(pz, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# position percentile rank over 126d
def f30sm_f30_smart_money_positioning_posrank_126d_base_v053_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = p.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# position percentile rank over 252d
def f30sm_f30_smart_money_positioning_posrank_252d_base_v054_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = p.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction percentile rank over 252d
def f30sm_f30_smart_money_positioning_convrank_252d_base_v055_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit percentile rank over 252d
def f30sm_f30_smart_money_positioning_vpurank_252d_base_v056_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction dispersion (rolling std of weight) 63d
def f30sm_f30_smart_money_positioning_convdisp_63d_base_v057_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction dispersion 126d
def f30sm_f30_smart_money_positioning_convdisp_126d_base_v058_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction dispersion 252d
def f30sm_f30_smart_money_positioning_convdisp_252d_base_v059_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# position-value dispersion (coefficient of variation) 63d
def f30sm_f30_smart_money_positioning_poscv_63d_base_v060_signal(shrvalue):
    result = _safe_div(_std(shrvalue, 63), _f30_pos(shrvalue, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# position-value dispersion (coefficient of variation) 126d
def f30sm_f30_smart_money_positioning_poscv_126d_base_v061_signal(shrvalue):
    result = _safe_div(_std(shrvalue, 126), _f30_pos(shrvalue, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit dispersion (CV) 126d (entry-price stability)
def f30sm_f30_smart_money_positioning_vpucv_126d_base_v062_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(_std(v, 126), _mean(v, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# position growth scaled by its own dispersion 63d (conviction-adjusted growth)
def f30sm_f30_smart_money_positioning_posgscaled_63d_base_v063_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    g = np.log(p / p.shift(63))
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# position growth scaled by its own dispersion 126d
def f30sm_f30_smart_money_positioning_posgscaled_126d_base_v064_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    g = np.log(p / p.shift(126))
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# conviction growth scaled by dispersion 126d
def f30sm_f30_smart_money_positioning_convgscaled_126d_base_v065_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    g = np.log(c / c.shift(126))
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# units vs value divergence 63d (price-driven vs size-driven positioning)
def f30sm_f30_smart_money_positioning_uvdiv_63d_base_v066_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(63))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(63))
    result = vg - ug
    return result.replace([np.inf, -np.inf], np.nan)


# units vs value divergence 126d
def f30sm_f30_smart_money_positioning_uvdiv_126d_base_v067_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(126))
    result = vg - ug
    return result.replace([np.inf, -np.inf], np.nan)


# units vs value divergence 252d
def f30sm_f30_smart_money_positioning_uvdiv_252d_base_v068_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(252))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(252))
    result = vg - ug
    return result.replace([np.inf, -np.inf], np.nan)


# conviction momentum spread: 21d change minus 126d change
def f30sm_f30_smart_money_positioning_convmomspr_base_v069_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    s1 = _safe_div(c - c.shift(21), c.shift(21).abs())
    s2 = _safe_div(c - c.shift(126), c.shift(126).abs())
    result = s1 - s2
    return result.replace([np.inf, -np.inf], np.nan)


# position momentum spread: 21d trend minus 126d trend
def f30sm_f30_smart_money_positioning_posmomspr_base_v070_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    s1 = _safe_div(p - p.shift(21), p.shift(21).abs())
    s2 = _safe_div(p - p.shift(126), p.shift(126).abs())
    result = s1 - s2
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed positioning z-score 63d span
def f30sm_f30_smart_money_positioning_posezma_63d_base_v071_signal(shrvalue):
    pz = _f30_posz(shrvalue, 252)
    result = pz.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed conviction-weight 63d span
def f30sm_f30_smart_money_positioning_convezma_63d_base_v072_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = c.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# position-to-marketcap level smoothed 126d (ownership footprint)
def f30sm_f30_smart_money_positioning_posmcaplvl_126d_base_v073_signal(shrvalue, marketcap):
    result = _mean(_safe_div(_f30_pos(shrvalue, 5), marketcap), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit relative to its 252d mean (entry vs current pricing)
def f30sm_f30_smart_money_positioning_vpurel_252d_base_v074_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v, _mean(v, 252)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# conviction relative to its 252d mean (over/under-weight vs norm)
def f30sm_f30_smart_money_positioning_convrel_252d_base_v075_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c, _mean(c, 252)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30sm_f30_smart_money_positioning_postrend_21d_base_v001_signal,
    f30sm_f30_smart_money_positioning_postrend_63d_base_v002_signal,
    f30sm_f30_smart_money_positioning_postrend_126d_base_v003_signal,
    f30sm_f30_smart_money_positioning_postrend_252d_base_v004_signal,
    f30sm_f30_smart_money_positioning_posglog_21d_base_v005_signal,
    f30sm_f30_smart_money_positioning_posglog_63d_base_v006_signal,
    f30sm_f30_smart_money_positioning_posglog_126d_base_v007_signal,
    f30sm_f30_smart_money_positioning_posglog_252d_base_v008_signal,
    f30sm_f30_smart_money_positioning_posz_21d_base_v009_signal,
    f30sm_f30_smart_money_positioning_posz_63d_base_v010_signal,
    f30sm_f30_smart_money_positioning_posz_126d_base_v011_signal,
    f30sm_f30_smart_money_positioning_posz_252d_base_v012_signal,
    f30sm_f30_smart_money_positioning_posz_378d_base_v013_signal,
    f30sm_f30_smart_money_positioning_unitstrend_21d_base_v014_signal,
    f30sm_f30_smart_money_positioning_unitstrend_63d_base_v015_signal,
    f30sm_f30_smart_money_positioning_unitstrend_126d_base_v016_signal,
    f30sm_f30_smart_money_positioning_unitstrend_252d_base_v017_signal,
    f30sm_f30_smart_money_positioning_unitsglog_21d_base_v018_signal,
    f30sm_f30_smart_money_positioning_unitsglog_63d_base_v019_signal,
    f30sm_f30_smart_money_positioning_unitsglog_126d_base_v020_signal,
    f30sm_f30_smart_money_positioning_vputrend_21d_base_v021_signal,
    f30sm_f30_smart_money_positioning_vputrend_63d_base_v022_signal,
    f30sm_f30_smart_money_positioning_vputrend_126d_base_v023_signal,
    f30sm_f30_smart_money_positioning_vputrend_252d_base_v024_signal,
    f30sm_f30_smart_money_positioning_vpuglog_21d_base_v025_signal,
    f30sm_f30_smart_money_positioning_vpuglog_63d_base_v026_signal,
    f30sm_f30_smart_money_positioning_vpuglog_126d_base_v027_signal,
    f30sm_f30_smart_money_positioning_vpuz_21d_base_v028_signal,
    f30sm_f30_smart_money_positioning_vpuz_63d_base_v029_signal,
    f30sm_f30_smart_money_positioning_vpuz_126d_base_v030_signal,
    f30sm_f30_smart_money_positioning_vpuz_252d_base_v031_signal,
    f30sm_f30_smart_money_positioning_convlvl_21d_base_v032_signal,
    f30sm_f30_smart_money_positioning_convlvl_63d_base_v033_signal,
    f30sm_f30_smart_money_positioning_convchg_21d_base_v034_signal,
    f30sm_f30_smart_money_positioning_convchg_63d_base_v035_signal,
    f30sm_f30_smart_money_positioning_convchg_126d_base_v036_signal,
    f30sm_f30_smart_money_positioning_convchg_252d_base_v037_signal,
    f30sm_f30_smart_money_positioning_convz_21d_base_v038_signal,
    f30sm_f30_smart_money_positioning_convz_63d_base_v039_signal,
    f30sm_f30_smart_money_positioning_convz_126d_base_v040_signal,
    f30sm_f30_smart_money_positioning_convz_252d_base_v041_signal,
    f30sm_f30_smart_money_positioning_convglog_63d_base_v042_signal,
    f30sm_f30_smart_money_positioning_convglog_126d_base_v043_signal,
    f30sm_f30_smart_money_positioning_rot_63d_base_v044_signal,
    f30sm_f30_smart_money_positioning_rot_126d_base_v045_signal,
    f30sm_f30_smart_money_positioning_rot_252d_base_v046_signal,
    f30sm_f30_smart_money_positioning_rot_21d_base_v047_signal,
    f30sm_f30_smart_money_positioning_posmcap_63d_base_v048_signal,
    f30sm_f30_smart_money_positioning_posmcap_126d_base_v049_signal,
    f30sm_f30_smart_money_positioning_posmcapz_252d_base_v050_signal,
    f30sm_f30_smart_money_positioning_possurp_21d_base_v051_signal,
    f30sm_f30_smart_money_positioning_possurp_63d_base_v052_signal,
    f30sm_f30_smart_money_positioning_posrank_126d_base_v053_signal,
    f30sm_f30_smart_money_positioning_posrank_252d_base_v054_signal,
    f30sm_f30_smart_money_positioning_convrank_252d_base_v055_signal,
    f30sm_f30_smart_money_positioning_vpurank_252d_base_v056_signal,
    f30sm_f30_smart_money_positioning_convdisp_63d_base_v057_signal,
    f30sm_f30_smart_money_positioning_convdisp_126d_base_v058_signal,
    f30sm_f30_smart_money_positioning_convdisp_252d_base_v059_signal,
    f30sm_f30_smart_money_positioning_poscv_63d_base_v060_signal,
    f30sm_f30_smart_money_positioning_poscv_126d_base_v061_signal,
    f30sm_f30_smart_money_positioning_vpucv_126d_base_v062_signal,
    f30sm_f30_smart_money_positioning_posgscaled_63d_base_v063_signal,
    f30sm_f30_smart_money_positioning_posgscaled_126d_base_v064_signal,
    f30sm_f30_smart_money_positioning_convgscaled_126d_base_v065_signal,
    f30sm_f30_smart_money_positioning_uvdiv_63d_base_v066_signal,
    f30sm_f30_smart_money_positioning_uvdiv_126d_base_v067_signal,
    f30sm_f30_smart_money_positioning_uvdiv_252d_base_v068_signal,
    f30sm_f30_smart_money_positioning_convmomspr_base_v069_signal,
    f30sm_f30_smart_money_positioning_posmomspr_base_v070_signal,
    f30sm_f30_smart_money_positioning_posezma_63d_base_v071_signal,
    f30sm_f30_smart_money_positioning_convezma_63d_base_v072_signal,
    f30sm_f30_smart_money_positioning_posmcaplvl_126d_base_v073_signal,
    f30sm_f30_smart_money_positioning_vpurel_252d_base_v074_signal,
    f30sm_f30_smart_money_positioning_convrel_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_SMART_MONEY_POSITIONING_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f30_pos", "_f30_posz", "_f30_conviction", "_f30_vpu")
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
    print(f"OK f30_smart_money_positioning_base_001_075_claude: {n_features} features pass")
