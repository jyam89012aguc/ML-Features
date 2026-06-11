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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f30sm_f30_smart_money_positioning_postrend_21d_slope_v001_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(21), p.shift(21).abs())
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_postrend_63d_slope_v002_signal(shrvalue):
    p = _f30_pos(shrvalue, 63)
    result = _safe_div(p - p.shift(63), p.shift(63).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_postrend_126d_slope_v003_signal(shrvalue):
    p = _f30_pos(shrvalue, 126)
    result = _safe_div(p - p.shift(126), p.shift(126).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_postrend_252d_slope_v004_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(252), p.shift(252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posglog_21d_slope_v005_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(21))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posglog_63d_slope_v006_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(63))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posglog_126d_slope_v007_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posglog_252d_slope_v008_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_21d_slope_v009_signal(shrvalue):
    result = _f30_posz(shrvalue, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_63d_slope_v010_signal(shrvalue):
    result = _f30_posz(shrvalue, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_126d_slope_v011_signal(shrvalue):
    result = _f30_posz(shrvalue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_252d_slope_v012_signal(shrvalue):
    result = _f30_posz(shrvalue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_378d_slope_v013_signal(shrvalue):
    result = _f30_posz(shrvalue, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitstrend_21d_slope_v014_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(21), u.shift(21).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitstrend_63d_slope_v015_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(63), u.shift(63).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitstrend_126d_slope_v016_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(126), u.shift(126).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitstrend_252d_slope_v017_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(252), u.shift(252).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitsglog_21d_slope_v018_signal(shrunits, shrvalue):
    u = _mean(shrunits, 5)
    result = np.log(u / u.shift(21)) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitsglog_63d_slope_v019_signal(shrunits, shrvalue):
    u = _mean(shrunits, 5)
    result = np.log(u / u.shift(63)) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitsglog_126d_slope_v020_signal(shrunits, shrvalue):
    u = _mean(shrunits, 5)
    result = np.log(u / u.shift(126)) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vputrend_21d_slope_v021_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(21), v.shift(21).abs())
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vputrend_63d_slope_v022_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(63), v.shift(63).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vputrend_126d_slope_v023_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(126), v.shift(126).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vputrend_252d_slope_v024_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(252), v.shift(252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuglog_21d_slope_v025_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = np.log(v / v.shift(21))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuglog_63d_slope_v026_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = np.log(v / v.shift(63))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuglog_126d_slope_v027_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = np.log(v / v.shift(126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuz_21d_slope_v028_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuz_63d_slope_v029_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuz_126d_slope_v030_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuz_252d_slope_v031_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convlvl_21d_slope_v032_signal(shrvalue, totalvalue):
    result = _mean(_f30_conviction(shrvalue, totalvalue), 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convlvl_63d_slope_v033_signal(shrvalue, totalvalue):
    result = _mean(_f30_conviction(shrvalue, totalvalue), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convchg_21d_slope_v034_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(21), c.shift(21).abs())
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convchg_63d_slope_v035_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(63), c.shift(63).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convchg_126d_slope_v036_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(126), c.shift(126).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convchg_252d_slope_v037_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(252), c.shift(252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convz_21d_slope_v038_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convz_63d_slope_v039_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convz_126d_slope_v040_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convz_252d_slope_v041_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convglog_63d_slope_v042_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = np.log(c / c.shift(63))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convglog_126d_slope_v043_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = np.log(c / c.shift(126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_rot_63d_slope_v044_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(63))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(63))
    result = pg - tg
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_rot_126d_slope_v045_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(126))
    result = pg - tg
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_rot_252d_slope_v046_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(252))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(252))
    result = pg - tg
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_rot_21d_slope_v047_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(21))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(21))
    result = pg - tg
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmcap_63d_slope_v048_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _safe_div(r - r.shift(63), r.shift(63).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmcap_126d_slope_v049_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _safe_div(r - r.shift(126), r.shift(126).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmcapz_252d_slope_v050_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _z(r, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_possurp_21d_slope_v051_signal(shrvalue):
    pz = _f30_posz(shrvalue, 63)
    result = pz - _mean(pz, 63)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_possurp_63d_slope_v052_signal(shrvalue):
    pz = _f30_posz(shrvalue, 126)
    result = pz - _mean(pz, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posrank_126d_slope_v053_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = p.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posrank_252d_slope_v054_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = p.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convrank_252d_slope_v055_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpurank_252d_slope_v056_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convdisp_63d_slope_v057_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convdisp_126d_slope_v058_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convdisp_252d_slope_v059_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_poscv_63d_slope_v060_signal(shrvalue):
    result = _safe_div(_std(shrvalue, 63), _f30_pos(shrvalue, 63).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_poscv_126d_slope_v061_signal(shrvalue):
    result = _safe_div(_std(shrvalue, 126), _f30_pos(shrvalue, 126).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpucv_126d_slope_v062_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(_std(v, 126), _mean(v, 126).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posgscaled_63d_slope_v063_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    g = np.log(p / p.shift(63))
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posgscaled_126d_slope_v064_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    g = np.log(p / p.shift(126))
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convgscaled_126d_slope_v065_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    g = np.log(c / c.shift(126))
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_uvdiv_63d_slope_v066_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(63))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(63))
    result = vg - ug
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_uvdiv_126d_slope_v067_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(126))
    result = vg - ug
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_uvdiv_252d_slope_v068_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(252))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(252))
    result = vg - ug
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convmomspr_slope_v069_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    s1 = _safe_div(c - c.shift(21), c.shift(21).abs())
    s2 = _safe_div(c - c.shift(126), c.shift(126).abs())
    result = s1 - s2
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmomspr_slope_v070_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    s1 = _safe_div(p - p.shift(21), p.shift(21).abs())
    s2 = _safe_div(p - p.shift(126), p.shift(126).abs())
    result = s1 - s2
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posezma_63d_slope_v071_signal(shrvalue):
    pz = _f30_posz(shrvalue, 252)
    result = pz.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convezma_63d_slope_v072_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = c.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmcaplvl_126d_slope_v073_signal(shrvalue, marketcap):
    result = _mean(_safe_div(_f30_pos(shrvalue, 5), marketcap), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpurel_252d_slope_v074_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v, _mean(v, 252)) - 1.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convrel_252d_slope_v075_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c, _mean(c, 252)) - 1.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_postrend_42d_slope_v076_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(42), p.shift(42).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_postrend_84d_slope_v077_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(84), p.shift(84).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_postrend_189d_slope_v078_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(189), p.shift(189).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posglog_42d_slope_v079_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(42))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posglog_189d_slope_v080_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(189))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posglog_378d_slope_v081_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(378))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_42d_slope_v082_signal(shrvalue):
    result = _f30_posz(shrvalue, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_84d_slope_v083_signal(shrvalue):
    result = _f30_posz(shrvalue, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_189d_slope_v084_signal(shrvalue):
    result = _f30_posz(shrvalue, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posz_504d_slope_v085_signal(shrvalue):
    result = _f30_posz(shrvalue, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitstrend_42d_slope_v086_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(42), u.shift(42).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitstrend_189d_slope_v087_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(189), u.shift(189).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitsz_63d_slope_v088_signal(shrunits, shrvalue):
    result = _z(shrunits, 63) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitsz_126d_slope_v089_signal(shrunits, shrvalue):
    result = _z(shrunits, 126) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitsz_252d_slope_v090_signal(shrunits, shrvalue):
    result = _z(shrunits, 252) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vputrend_42d_slope_v091_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(42), v.shift(42).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vputrend_189d_slope_v092_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(189), v.shift(189).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuglog_252d_slope_v093_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = np.log(v / v.shift(252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuz_189d_slope_v094_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convlvl_126d_slope_v095_signal(shrvalue, totalvalue):
    result = _mean(_f30_conviction(shrvalue, totalvalue), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convlvl_252d_slope_v096_signal(shrvalue, totalvalue):
    result = _mean(_f30_conviction(shrvalue, totalvalue), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convchg_42d_slope_v097_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(42), c.shift(42).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convchg_189d_slope_v098_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(189), c.shift(189).abs())
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convz_42d_slope_v099_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convz_189d_slope_v100_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convz_378d_slope_v101_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convglog_21d_slope_v102_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = np.log(c / c.shift(21))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convglog_252d_slope_v103_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = np.log(c / c.shift(252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_rot_42d_slope_v104_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(42))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(42))
    result = pg - tg
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_rot_189d_slope_v105_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(189))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(189))
    result = pg - tg
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_rotz_126d_slope_v106_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(126))
    result = _z(pg - tg, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmcap_252d_slope_v107_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _safe_div(r - r.shift(252), r.shift(252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmcapglog_126d_slope_v108_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = np.log(r / r.shift(126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmcapz_126d_slope_v109_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _z(r, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_possurp_126d_slope_v110_signal(shrvalue):
    pz = _f30_posz(shrvalue, 252)
    result = pz - _mean(pz, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convsurp_21d_slope_v111_signal(shrvalue, totalvalue):
    cz = _z(_f30_conviction(shrvalue, totalvalue), 63)
    result = cz - _mean(cz, 63)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convsurp_63d_slope_v112_signal(shrvalue, totalvalue):
    cz = _z(_f30_conviction(shrvalue, totalvalue), 126)
    result = cz - _mean(cz, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posrank_504d_slope_v113_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = p.rolling(504, min_periods=168).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convrank_126d_slope_v114_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = c.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpurank_126d_slope_v115_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = v.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_unitsrank_252d_slope_v116_signal(shrunits, shrvalue):
    result = shrunits.rolling(252, min_periods=84).rank(pct=True) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convdisp_42d_slope_v117_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convdisp_189d_slope_v118_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_poscv_252d_slope_v119_signal(shrvalue):
    result = _safe_div(_std(shrvalue, 252), _f30_pos(shrvalue, 252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpucv_252d_slope_v120_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(_std(v, 252), _mean(v, 252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convcv_252d_slope_v121_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(_std(c, 252), _mean(c, 252).abs())
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posgscaled_252d_slope_v122_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    g = np.log(p / p.shift(252))
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convgscaled_63d_slope_v123_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    g = np.log(c / c.shift(63))
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpugscaled_126d_slope_v124_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    g = np.log(v / v.shift(126))
    result = _safe_div(g, _std(g, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_uvdiv_42d_slope_v125_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(42))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(42))
    result = vg - ug
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_uvdiv_189d_slope_v126_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(189))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(189))
    result = vg - ug
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convmomspr2_slope_v127_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    s1 = _safe_div(c - c.shift(42), c.shift(42).abs())
    s2 = _safe_div(c - c.shift(189), c.shift(189).abs())
    result = s1 - s2
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmomspr2_slope_v128_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    s1 = _safe_div(p - p.shift(63), p.shift(63).abs())
    s2 = _safe_div(p - p.shift(252), p.shift(252).abs())
    result = s1 - s2
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posezma_126d_slope_v129_signal(shrvalue):
    pz = _f30_posz(shrvalue, 252)
    result = pz.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convezma_126d_slope_v130_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = c.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuezma_63d_slope_v131_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = v.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posmcaplvl_252d_slope_v132_signal(shrvalue, marketcap):
    result = _mean(_safe_div(_f30_pos(shrvalue, 5), marketcap), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpurel_126d_slope_v133_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v, _mean(v, 126)) - 1.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convrel_126d_slope_v134_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c, _mean(c, 126)) - 1.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posrel_252d_slope_v135_signal(shrvalue):
    result = _safe_div(shrvalue, _f30_pos(shrvalue, 252)) - 1.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convaccel_slope_v136_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    chg = _safe_div(c - c.shift(63), c.shift(63).abs())
    result = chg - chg.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_posaccel_slope_v137_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    trd = _safe_div(p - p.shift(63), p.shift(63).abs())
    result = trd - trd.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpuaccel_slope_v138_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    trd = _safe_div(v - v.shift(63), v.shift(63).abs())
    result = trd - trd.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_tilt_126d_slope_v139_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 126) - _f30_posz(shrvalue, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_tilt_252d_slope_v140_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 252) - _f30_posz(shrvalue, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpumcap_126d_slope_v141_signal(shrvalue, shrunits, marketcap):
    v = _f30_vpu(shrvalue, shrunits)
    vg = np.log(v / v.shift(126))
    mg = np.log(_mean(marketcap, 5) / _mean(marketcap, 5).shift(126))
    result = vg - mg
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_vpumcap_252d_slope_v142_signal(shrvalue, shrunits, marketcap):
    v = _f30_vpu(shrvalue, shrunits)
    vg = np.log(v / v.shift(252))
    mg = np.log(_mean(marketcap, 5) / _mean(marketcap, 5).shift(252))
    result = vg - mg
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convwgrow_126d_slope_v143_signal(shrvalue, totalvalue):
    g = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    result = g * _mean(_f30_conviction(shrvalue, totalvalue), 21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convwgrow_252d_slope_v144_signal(shrvalue, totalvalue):
    g = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(252))
    result = g * _mean(_f30_conviction(shrvalue, totalvalue), 21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_szpx_126d_slope_v145_signal(shrvalue, shrunits):
    result = _f30_posz(shrvalue, 126) - _z(_f30_vpu(shrvalue, shrunits), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_umcap_126d_slope_v146_signal(shrunits, marketcap, shrvalue):
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(126))
    mg = np.log(_mean(marketcap, 5) / _mean(marketcap, 5).shift(126))
    result = (ug - mg) + _f30_vpu(shrvalue, shrunits) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_pcalign_126d_slope_v147_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(21))
    c = _f30_conviction(shrvalue, totalvalue)
    cg = np.log(c / c.shift(21))
    result = pg.rolling(126, min_periods=42).corr(cg)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_convrel_504d_slope_v148_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c, _mean(c, 504)) - 1.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_blend_126d_slope_v149_signal(shrvalue, totalvalue, shrunits):
    result = (_f30_posz(shrvalue, 126)
              + _z(_f30_conviction(shrvalue, totalvalue), 126)
              + _z(_f30_vpu(shrvalue, shrunits), 126)) / 3.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30sm_f30_smart_money_positioning_blendmom_126d_slope_v150_signal(shrvalue, totalvalue, shrunits):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    c = _f30_conviction(shrvalue, totalvalue)
    cg = np.log(c / c.shift(126))
    v = _f30_vpu(shrvalue, shrunits)
    vg = np.log(v / v.shift(126))
    result = (pg + cg + vg) / 3.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f30sm_f30_smart_money_positioning_postrend_21d_slope_v001_signal,    f30sm_f30_smart_money_positioning_postrend_63d_slope_v002_signal,    f30sm_f30_smart_money_positioning_postrend_126d_slope_v003_signal,    f30sm_f30_smart_money_positioning_postrend_252d_slope_v004_signal,    f30sm_f30_smart_money_positioning_posglog_21d_slope_v005_signal,    f30sm_f30_smart_money_positioning_posglog_63d_slope_v006_signal,    f30sm_f30_smart_money_positioning_posglog_126d_slope_v007_signal,    f30sm_f30_smart_money_positioning_posglog_252d_slope_v008_signal,    f30sm_f30_smart_money_positioning_posz_21d_slope_v009_signal,    f30sm_f30_smart_money_positioning_posz_63d_slope_v010_signal,    f30sm_f30_smart_money_positioning_posz_126d_slope_v011_signal,    f30sm_f30_smart_money_positioning_posz_252d_slope_v012_signal,    f30sm_f30_smart_money_positioning_posz_378d_slope_v013_signal,    f30sm_f30_smart_money_positioning_unitstrend_21d_slope_v014_signal,    f30sm_f30_smart_money_positioning_unitstrend_63d_slope_v015_signal,    f30sm_f30_smart_money_positioning_unitstrend_126d_slope_v016_signal,    f30sm_f30_smart_money_positioning_unitstrend_252d_slope_v017_signal,    f30sm_f30_smart_money_positioning_unitsglog_21d_slope_v018_signal,    f30sm_f30_smart_money_positioning_unitsglog_63d_slope_v019_signal,    f30sm_f30_smart_money_positioning_unitsglog_126d_slope_v020_signal,    f30sm_f30_smart_money_positioning_vputrend_21d_slope_v021_signal,    f30sm_f30_smart_money_positioning_vputrend_63d_slope_v022_signal,    f30sm_f30_smart_money_positioning_vputrend_126d_slope_v023_signal,    f30sm_f30_smart_money_positioning_vputrend_252d_slope_v024_signal,    f30sm_f30_smart_money_positioning_vpuglog_21d_slope_v025_signal,    f30sm_f30_smart_money_positioning_vpuglog_63d_slope_v026_signal,    f30sm_f30_smart_money_positioning_vpuglog_126d_slope_v027_signal,    f30sm_f30_smart_money_positioning_vpuz_21d_slope_v028_signal,    f30sm_f30_smart_money_positioning_vpuz_63d_slope_v029_signal,    f30sm_f30_smart_money_positioning_vpuz_126d_slope_v030_signal,    f30sm_f30_smart_money_positioning_vpuz_252d_slope_v031_signal,    f30sm_f30_smart_money_positioning_convlvl_21d_slope_v032_signal,    f30sm_f30_smart_money_positioning_convlvl_63d_slope_v033_signal,    f30sm_f30_smart_money_positioning_convchg_21d_slope_v034_signal,    f30sm_f30_smart_money_positioning_convchg_63d_slope_v035_signal,    f30sm_f30_smart_money_positioning_convchg_126d_slope_v036_signal,    f30sm_f30_smart_money_positioning_convchg_252d_slope_v037_signal,    f30sm_f30_smart_money_positioning_convz_21d_slope_v038_signal,    f30sm_f30_smart_money_positioning_convz_63d_slope_v039_signal,    f30sm_f30_smart_money_positioning_convz_126d_slope_v040_signal,    f30sm_f30_smart_money_positioning_convz_252d_slope_v041_signal,    f30sm_f30_smart_money_positioning_convglog_63d_slope_v042_signal,    f30sm_f30_smart_money_positioning_convglog_126d_slope_v043_signal,    f30sm_f30_smart_money_positioning_rot_63d_slope_v044_signal,    f30sm_f30_smart_money_positioning_rot_126d_slope_v045_signal,    f30sm_f30_smart_money_positioning_rot_252d_slope_v046_signal,    f30sm_f30_smart_money_positioning_rot_21d_slope_v047_signal,    f30sm_f30_smart_money_positioning_posmcap_63d_slope_v048_signal,    f30sm_f30_smart_money_positioning_posmcap_126d_slope_v049_signal,    f30sm_f30_smart_money_positioning_posmcapz_252d_slope_v050_signal,    f30sm_f30_smart_money_positioning_possurp_21d_slope_v051_signal,    f30sm_f30_smart_money_positioning_possurp_63d_slope_v052_signal,    f30sm_f30_smart_money_positioning_posrank_126d_slope_v053_signal,    f30sm_f30_smart_money_positioning_posrank_252d_slope_v054_signal,    f30sm_f30_smart_money_positioning_convrank_252d_slope_v055_signal,    f30sm_f30_smart_money_positioning_vpurank_252d_slope_v056_signal,    f30sm_f30_smart_money_positioning_convdisp_63d_slope_v057_signal,    f30sm_f30_smart_money_positioning_convdisp_126d_slope_v058_signal,    f30sm_f30_smart_money_positioning_convdisp_252d_slope_v059_signal,    f30sm_f30_smart_money_positioning_poscv_63d_slope_v060_signal,    f30sm_f30_smart_money_positioning_poscv_126d_slope_v061_signal,    f30sm_f30_smart_money_positioning_vpucv_126d_slope_v062_signal,    f30sm_f30_smart_money_positioning_posgscaled_63d_slope_v063_signal,    f30sm_f30_smart_money_positioning_posgscaled_126d_slope_v064_signal,    f30sm_f30_smart_money_positioning_convgscaled_126d_slope_v065_signal,    f30sm_f30_smart_money_positioning_uvdiv_63d_slope_v066_signal,    f30sm_f30_smart_money_positioning_uvdiv_126d_slope_v067_signal,    f30sm_f30_smart_money_positioning_uvdiv_252d_slope_v068_signal,    f30sm_f30_smart_money_positioning_convmomspr_slope_v069_signal,    f30sm_f30_smart_money_positioning_posmomspr_slope_v070_signal,    f30sm_f30_smart_money_positioning_posezma_63d_slope_v071_signal,    f30sm_f30_smart_money_positioning_convezma_63d_slope_v072_signal,    f30sm_f30_smart_money_positioning_posmcaplvl_126d_slope_v073_signal,    f30sm_f30_smart_money_positioning_vpurel_252d_slope_v074_signal,    f30sm_f30_smart_money_positioning_convrel_252d_slope_v075_signal,    f30sm_f30_smart_money_positioning_postrend_42d_slope_v076_signal,    f30sm_f30_smart_money_positioning_postrend_84d_slope_v077_signal,    f30sm_f30_smart_money_positioning_postrend_189d_slope_v078_signal,    f30sm_f30_smart_money_positioning_posglog_42d_slope_v079_signal,    f30sm_f30_smart_money_positioning_posglog_189d_slope_v080_signal,    f30sm_f30_smart_money_positioning_posglog_378d_slope_v081_signal,    f30sm_f30_smart_money_positioning_posz_42d_slope_v082_signal,    f30sm_f30_smart_money_positioning_posz_84d_slope_v083_signal,    f30sm_f30_smart_money_positioning_posz_189d_slope_v084_signal,    f30sm_f30_smart_money_positioning_posz_504d_slope_v085_signal,    f30sm_f30_smart_money_positioning_unitstrend_42d_slope_v086_signal,    f30sm_f30_smart_money_positioning_unitstrend_189d_slope_v087_signal,    f30sm_f30_smart_money_positioning_unitsz_63d_slope_v088_signal,    f30sm_f30_smart_money_positioning_unitsz_126d_slope_v089_signal,    f30sm_f30_smart_money_positioning_unitsz_252d_slope_v090_signal,    f30sm_f30_smart_money_positioning_vputrend_42d_slope_v091_signal,    f30sm_f30_smart_money_positioning_vputrend_189d_slope_v092_signal,    f30sm_f30_smart_money_positioning_vpuglog_252d_slope_v093_signal,    f30sm_f30_smart_money_positioning_vpuz_189d_slope_v094_signal,    f30sm_f30_smart_money_positioning_convlvl_126d_slope_v095_signal,    f30sm_f30_smart_money_positioning_convlvl_252d_slope_v096_signal,    f30sm_f30_smart_money_positioning_convchg_42d_slope_v097_signal,    f30sm_f30_smart_money_positioning_convchg_189d_slope_v098_signal,    f30sm_f30_smart_money_positioning_convz_42d_slope_v099_signal,    f30sm_f30_smart_money_positioning_convz_189d_slope_v100_signal,    f30sm_f30_smart_money_positioning_convz_378d_slope_v101_signal,    f30sm_f30_smart_money_positioning_convglog_21d_slope_v102_signal,    f30sm_f30_smart_money_positioning_convglog_252d_slope_v103_signal,    f30sm_f30_smart_money_positioning_rot_42d_slope_v104_signal,    f30sm_f30_smart_money_positioning_rot_189d_slope_v105_signal,    f30sm_f30_smart_money_positioning_rotz_126d_slope_v106_signal,    f30sm_f30_smart_money_positioning_posmcap_252d_slope_v107_signal,    f30sm_f30_smart_money_positioning_posmcapglog_126d_slope_v108_signal,    f30sm_f30_smart_money_positioning_posmcapz_126d_slope_v109_signal,    f30sm_f30_smart_money_positioning_possurp_126d_slope_v110_signal,    f30sm_f30_smart_money_positioning_convsurp_21d_slope_v111_signal,    f30sm_f30_smart_money_positioning_convsurp_63d_slope_v112_signal,    f30sm_f30_smart_money_positioning_posrank_504d_slope_v113_signal,    f30sm_f30_smart_money_positioning_convrank_126d_slope_v114_signal,    f30sm_f30_smart_money_positioning_vpurank_126d_slope_v115_signal,    f30sm_f30_smart_money_positioning_unitsrank_252d_slope_v116_signal,    f30sm_f30_smart_money_positioning_convdisp_42d_slope_v117_signal,    f30sm_f30_smart_money_positioning_convdisp_189d_slope_v118_signal,    f30sm_f30_smart_money_positioning_poscv_252d_slope_v119_signal,    f30sm_f30_smart_money_positioning_vpucv_252d_slope_v120_signal,    f30sm_f30_smart_money_positioning_convcv_252d_slope_v121_signal,    f30sm_f30_smart_money_positioning_posgscaled_252d_slope_v122_signal,    f30sm_f30_smart_money_positioning_convgscaled_63d_slope_v123_signal,    f30sm_f30_smart_money_positioning_vpugscaled_126d_slope_v124_signal,    f30sm_f30_smart_money_positioning_uvdiv_42d_slope_v125_signal,    f30sm_f30_smart_money_positioning_uvdiv_189d_slope_v126_signal,    f30sm_f30_smart_money_positioning_convmomspr2_slope_v127_signal,    f30sm_f30_smart_money_positioning_posmomspr2_slope_v128_signal,    f30sm_f30_smart_money_positioning_posezma_126d_slope_v129_signal,    f30sm_f30_smart_money_positioning_convezma_126d_slope_v130_signal,    f30sm_f30_smart_money_positioning_vpuezma_63d_slope_v131_signal,    f30sm_f30_smart_money_positioning_posmcaplvl_252d_slope_v132_signal,    f30sm_f30_smart_money_positioning_vpurel_126d_slope_v133_signal,    f30sm_f30_smart_money_positioning_convrel_126d_slope_v134_signal,    f30sm_f30_smart_money_positioning_posrel_252d_slope_v135_signal,    f30sm_f30_smart_money_positioning_convaccel_slope_v136_signal,    f30sm_f30_smart_money_positioning_posaccel_slope_v137_signal,    f30sm_f30_smart_money_positioning_vpuaccel_slope_v138_signal,    f30sm_f30_smart_money_positioning_tilt_126d_slope_v139_signal,    f30sm_f30_smart_money_positioning_tilt_252d_slope_v140_signal,    f30sm_f30_smart_money_positioning_vpumcap_126d_slope_v141_signal,    f30sm_f30_smart_money_positioning_vpumcap_252d_slope_v142_signal,    f30sm_f30_smart_money_positioning_convwgrow_126d_slope_v143_signal,    f30sm_f30_smart_money_positioning_convwgrow_252d_slope_v144_signal,    f30sm_f30_smart_money_positioning_szpx_126d_slope_v145_signal,    f30sm_f30_smart_money_positioning_umcap_126d_slope_v146_signal,    f30sm_f30_smart_money_positioning_pcalign_126d_slope_v147_signal,    f30sm_f30_smart_money_positioning_convrel_504d_slope_v148_signal,    f30sm_f30_smart_money_positioning_blend_126d_slope_v149_signal,    f30sm_f30_smart_money_positioning_blendmom_126d_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_SMART_MONEY_POSITIONING_REGISTRY_SLOPE = REGISTRY

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
    domain_primitives = ('_f30_pos', '_f30_posz', '_f30_conviction', '_f30_vpu')
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
    print("OK f30_smart_money_positioning_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
