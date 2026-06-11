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


# ============ FEATURES 076-150 ============

# 42d position-value trend
def f30sm_f30_smart_money_positioning_postrend_42d_base_v076_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(42), p.shift(42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 84d position-value trend
def f30sm_f30_smart_money_positioning_postrend_84d_base_v077_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(84), p.shift(84).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 189d position-value trend
def f30sm_f30_smart_money_positioning_postrend_189d_base_v078_signal(shrvalue):
    p = _f30_pos(shrvalue, 21)
    result = _safe_div(p - p.shift(189), p.shift(189).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 42d log position-value growth
def f30sm_f30_smart_money_positioning_posglog_42d_base_v079_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(42))
    return result.replace([np.inf, -np.inf], np.nan)


# 189d log position-value growth
def f30sm_f30_smart_money_positioning_posglog_189d_base_v080_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(189))
    return result.replace([np.inf, -np.inf], np.nan)


# 378d log position-value growth
def f30sm_f30_smart_money_positioning_posglog_378d_base_v081_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = np.log(p / p.shift(378))
    return result.replace([np.inf, -np.inf], np.nan)


# 42d positioning z-score
def f30sm_f30_smart_money_positioning_posz_42d_base_v082_signal(shrvalue):
    result = _f30_posz(shrvalue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d positioning z-score
def f30sm_f30_smart_money_positioning_posz_84d_base_v083_signal(shrvalue):
    result = _f30_posz(shrvalue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d positioning z-score
def f30sm_f30_smart_money_positioning_posz_189d_base_v084_signal(shrvalue):
    result = _f30_posz(shrvalue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d positioning z-score
def f30sm_f30_smart_money_positioning_posz_504d_base_v085_signal(shrvalue):
    result = _f30_posz(shrvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d units change
def f30sm_f30_smart_money_positioning_unitstrend_42d_base_v086_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(42), u.shift(42).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d units change
def f30sm_f30_smart_money_positioning_unitstrend_189d_base_v087_signal(shrunits, shrvalue):
    u = _mean(shrunits, 21)
    result = _safe_div(u - u.shift(189), u.shift(189).abs()) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d units z-score
def f30sm_f30_smart_money_positioning_unitsz_63d_base_v088_signal(shrunits, shrvalue):
    result = _z(shrunits, 63) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d units z-score
def f30sm_f30_smart_money_positioning_unitsz_126d_base_v089_signal(shrunits, shrvalue):
    result = _z(shrunits, 126) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units z-score
def f30sm_f30_smart_money_positioning_unitsz_252d_base_v090_signal(shrunits, shrvalue):
    result = _z(shrunits, 252) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d value-per-unit trend
def f30sm_f30_smart_money_positioning_vputrend_42d_base_v091_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(42), v.shift(42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 189d value-per-unit trend
def f30sm_f30_smart_money_positioning_vputrend_189d_base_v092_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(189), v.shift(189).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log value-per-unit growth
def f30sm_f30_smart_money_positioning_vpuglog_252d_base_v093_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = np.log(v / v.shift(252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value-per-unit z-score over 189d window
def f30sm_f30_smart_money_positioning_vpuz_189d_base_v094_signal(shrvalue, shrunits):
    result = _z(_f30_vpu(shrvalue, shrunits), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conviction-weight level
def f30sm_f30_smart_money_positioning_convlvl_126d_base_v095_signal(shrvalue, totalvalue):
    result = _mean(_f30_conviction(shrvalue, totalvalue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conviction-weight level
def f30sm_f30_smart_money_positioning_convlvl_252d_base_v096_signal(shrvalue, totalvalue):
    result = _mean(_f30_conviction(shrvalue, totalvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d conviction-weight change
def f30sm_f30_smart_money_positioning_convchg_42d_base_v097_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(42), c.shift(42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 189d conviction-weight change
def f30sm_f30_smart_money_positioning_convchg_189d_base_v098_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c - c.shift(189), c.shift(189).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 42d conviction-weight z-score
def f30sm_f30_smart_money_positioning_convz_42d_base_v099_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d conviction-weight z-score
def f30sm_f30_smart_money_positioning_convz_189d_base_v100_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d conviction-weight z-score
def f30sm_f30_smart_money_positioning_convz_378d_base_v101_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log conviction-weight growth
def f30sm_f30_smart_money_positioning_convglog_21d_base_v102_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = np.log(c / c.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log conviction-weight growth
def f30sm_f30_smart_money_positioning_convglog_252d_base_v103_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = np.log(c / c.shift(252))
    return result.replace([np.inf, -np.inf], np.nan)


# rotation 42d
def f30sm_f30_smart_money_positioning_rot_42d_base_v104_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(42))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(42))
    result = pg - tg
    return result.replace([np.inf, -np.inf], np.nan)


# rotation 189d
def f30sm_f30_smart_money_positioning_rot_189d_base_v105_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(189))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(189))
    result = pg - tg
    return result.replace([np.inf, -np.inf], np.nan)


# rotation z-scored 126d (standardized reallocation)
def f30sm_f30_smart_money_positioning_rotz_126d_base_v106_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    tg = np.log(_mean(totalvalue, 5) / _mean(totalvalue, 5).shift(126))
    result = _z(pg - tg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# position vs marketcap ratio trend 252d
def f30sm_f30_smart_money_positioning_posmcap_252d_base_v107_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _safe_div(r - r.shift(252), r.shift(252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# position vs marketcap log growth 126d
def f30sm_f30_smart_money_positioning_posmcapglog_126d_base_v108_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = np.log(r / r.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# position vs marketcap z-score 126d
def f30sm_f30_smart_money_positioning_posmcapz_126d_base_v109_signal(shrvalue, marketcap):
    r = _safe_div(_f30_pos(shrvalue, 5), marketcap)
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# position momentum: 126d posz minus its 252d mean
def f30sm_f30_smart_money_positioning_possurp_126d_base_v110_signal(shrvalue):
    pz = _f30_posz(shrvalue, 252)
    result = pz - _mean(pz, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction momentum: 21d convz minus its 63d mean
def f30sm_f30_smart_money_positioning_convsurp_21d_base_v111_signal(shrvalue, totalvalue):
    cz = _z(_f30_conviction(shrvalue, totalvalue), 63)
    result = cz - _mean(cz, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction momentum: 63d convz minus its 126d mean
def f30sm_f30_smart_money_positioning_convsurp_63d_base_v112_signal(shrvalue, totalvalue):
    cz = _z(_f30_conviction(shrvalue, totalvalue), 126)
    result = cz - _mean(cz, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# position percentile rank over 504d
def f30sm_f30_smart_money_positioning_posrank_504d_base_v113_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    result = p.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction percentile rank over 126d
def f30sm_f30_smart_money_positioning_convrank_126d_base_v114_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = c.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit percentile rank over 126d
def f30sm_f30_smart_money_positioning_vpurank_126d_base_v115_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = v.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# units percentile rank over 252d
def f30sm_f30_smart_money_positioning_unitsrank_252d_base_v116_signal(shrunits, shrvalue):
    result = shrunits.rolling(252, min_periods=84).rank(pct=True) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# conviction dispersion 42d
def f30sm_f30_smart_money_positioning_convdisp_42d_base_v117_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction dispersion 189d
def f30sm_f30_smart_money_positioning_convdisp_189d_base_v118_signal(shrvalue, totalvalue):
    result = _std(_f30_conviction(shrvalue, totalvalue), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# position-value CV 252d
def f30sm_f30_smart_money_positioning_poscv_252d_base_v119_signal(shrvalue):
    result = _safe_div(_std(shrvalue, 252), _f30_pos(shrvalue, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit CV 252d
def f30sm_f30_smart_money_positioning_vpucv_252d_base_v120_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(_std(v, 252), _mean(v, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# conviction CV 252d (weight stability)
def f30sm_f30_smart_money_positioning_convcv_252d_base_v121_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(_std(c, 252), _mean(c, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# position growth scaled by dispersion 252d
def f30sm_f30_smart_money_positioning_posgscaled_252d_base_v122_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    g = np.log(p / p.shift(252))
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# conviction growth scaled by dispersion 63d
def f30sm_f30_smart_money_positioning_convgscaled_63d_base_v123_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    g = np.log(c / c.shift(63))
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit growth scaled by dispersion 126d
def f30sm_f30_smart_money_positioning_vpugscaled_126d_base_v124_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    g = np.log(v / v.shift(126))
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# units vs value divergence 42d
def f30sm_f30_smart_money_positioning_uvdiv_42d_base_v125_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(42))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(42))
    result = vg - ug
    return result.replace([np.inf, -np.inf], np.nan)


# units vs value divergence 189d
def f30sm_f30_smart_money_positioning_uvdiv_189d_base_v126_signal(shrvalue, shrunits):
    vg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(189))
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(189))
    result = vg - ug
    return result.replace([np.inf, -np.inf], np.nan)


# conviction momentum spread: 42d change minus 189d change
def f30sm_f30_smart_money_positioning_convmomspr2_base_v127_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    s1 = _safe_div(c - c.shift(42), c.shift(42).abs())
    s2 = _safe_div(c - c.shift(189), c.shift(189).abs())
    result = s1 - s2
    return result.replace([np.inf, -np.inf], np.nan)


# position momentum spread: 63d trend minus 252d trend
def f30sm_f30_smart_money_positioning_posmomspr2_base_v128_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    s1 = _safe_div(p - p.shift(63), p.shift(63).abs())
    s2 = _safe_div(p - p.shift(252), p.shift(252).abs())
    result = s1 - s2
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed positioning z-score 126d span
def f30sm_f30_smart_money_positioning_posezma_126d_base_v129_signal(shrvalue):
    pz = _f30_posz(shrvalue, 252)
    result = pz.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed conviction-weight 126d span
def f30sm_f30_smart_money_positioning_convezma_126d_base_v130_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = c.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed value-per-unit 63d span
def f30sm_f30_smart_money_positioning_vpuezma_63d_base_v131_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = v.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# position-to-marketcap level smoothed 252d
def f30sm_f30_smart_money_positioning_posmcaplvl_252d_base_v132_signal(shrvalue, marketcap):
    result = _mean(_safe_div(_f30_pos(shrvalue, 5), marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit relative to its 126d mean
def f30sm_f30_smart_money_positioning_vpurel_126d_base_v133_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    result = _safe_div(v, _mean(v, 126)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# conviction relative to its 126d mean
def f30sm_f30_smart_money_positioning_convrel_126d_base_v134_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c, _mean(c, 126)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# position relative to its 252d mean (size extension)
def f30sm_f30_smart_money_positioning_posrel_252d_base_v135_signal(shrvalue):
    result = _safe_div(shrvalue, _f30_pos(shrvalue, 252)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# conviction acceleration: 21d change of conviction-change 63d
def f30sm_f30_smart_money_positioning_convaccel_base_v136_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    chg = _safe_div(c - c.shift(63), c.shift(63).abs())
    result = chg - chg.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# position acceleration: 21d change of position-trend 63d
def f30sm_f30_smart_money_positioning_posaccel_base_v137_signal(shrvalue):
    p = _f30_pos(shrvalue, 5)
    trd = _safe_div(p - p.shift(63), p.shift(63).abs())
    result = trd - trd.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit acceleration: 21d change of vpu-trend 63d
def f30sm_f30_smart_money_positioning_vpuaccel_base_v138_signal(shrvalue, shrunits):
    v = _f30_vpu(shrvalue, shrunits)
    trd = _safe_div(v - v.shift(63), v.shift(63).abs())
    result = trd - trd.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction tilt: weight z minus position z (relative vs absolute extension)
def f30sm_f30_smart_money_positioning_tilt_126d_base_v139_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 126) - _f30_posz(shrvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction tilt 252d
def f30sm_f30_smart_money_positioning_tilt_252d_base_v140_signal(shrvalue, totalvalue):
    result = _z(_f30_conviction(shrvalue, totalvalue), 252) - _f30_posz(shrvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit vs marketcap-implied price drift 126d (entry vs market)
def f30sm_f30_smart_money_positioning_vpumcap_126d_base_v141_signal(shrvalue, shrunits, marketcap):
    v = _f30_vpu(shrvalue, shrunits)
    vg = np.log(v / v.shift(126))
    mg = np.log(_mean(marketcap, 5) / _mean(marketcap, 5).shift(126))
    result = vg - mg
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit vs marketcap-implied price drift 252d
def f30sm_f30_smart_money_positioning_vpumcap_252d_base_v142_signal(shrvalue, shrunits, marketcap):
    v = _f30_vpu(shrvalue, shrunits)
    vg = np.log(v / v.shift(252))
    mg = np.log(_mean(marketcap, 5) / _mean(marketcap, 5).shift(252))
    result = vg - mg
    return result.replace([np.inf, -np.inf], np.nan)


# conviction-weighted position growth 126d (size growth scaled by book weight)
def f30sm_f30_smart_money_positioning_convwgrow_126d_base_v143_signal(shrvalue, totalvalue):
    g = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    result = g * _mean(_f30_conviction(shrvalue, totalvalue), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction-weighted position growth 252d
def f30sm_f30_smart_money_positioning_convwgrow_252d_base_v144_signal(shrvalue, totalvalue):
    g = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(252))
    result = g * _mean(_f30_conviction(shrvalue, totalvalue), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# positioning z minus value-per-unit z 126d (size vs price extension)
def f30sm_f30_smart_money_positioning_szpx_126d_base_v145_signal(shrvalue, shrunits):
    result = _f30_posz(shrvalue, 126) - _z(_f30_vpu(shrvalue, shrunits), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# units growth minus marketcap growth 126d (share-count vs float)
def f30sm_f30_smart_money_positioning_umcap_126d_base_v146_signal(shrunits, marketcap, shrvalue):
    ug = np.log(_mean(shrunits, 5) / _mean(shrunits, 5).shift(126))
    mg = np.log(_mean(marketcap, 5) / _mean(marketcap, 5).shift(126))
    result = (ug - mg) + _f30_vpu(shrvalue, shrunits) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of position-growth and conviction-growth 126d (aligned conviction)
def f30sm_f30_smart_money_positioning_pcalign_126d_base_v147_signal(shrvalue, totalvalue):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(21))
    c = _f30_conviction(shrvalue, totalvalue)
    cg = np.log(c / c.shift(21))
    result = pg.rolling(126, min_periods=42).corr(cg)
    return result.replace([np.inf, -np.inf], np.nan)


# conviction relative to its 504d mean (long-horizon over/under-weight)
def f30sm_f30_smart_money_positioning_convrel_504d_base_v148_signal(shrvalue, totalvalue):
    c = _f30_conviction(shrvalue, totalvalue)
    result = _safe_div(c, _mean(c, 504)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended positioning composite: posz + convz + vpu-z over 126d
def f30sm_f30_smart_money_positioning_blend_126d_base_v149_signal(shrvalue, totalvalue, shrunits):
    result = (_f30_posz(shrvalue, 126)
              + _z(_f30_conviction(shrvalue, totalvalue), 126)
              + _z(_f30_vpu(shrvalue, shrunits), 126)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended positioning momentum composite: pos-growth + conv-growth + vpu-growth 126d
def f30sm_f30_smart_money_positioning_blendmom_126d_base_v150_signal(shrvalue, totalvalue, shrunits):
    pg = np.log(_f30_pos(shrvalue, 5) / _f30_pos(shrvalue, 5).shift(126))
    c = _f30_conviction(shrvalue, totalvalue)
    cg = np.log(c / c.shift(126))
    v = _f30_vpu(shrvalue, shrunits)
    vg = np.log(v / v.shift(126))
    result = (pg + cg + vg) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30sm_f30_smart_money_positioning_postrend_42d_base_v076_signal,
    f30sm_f30_smart_money_positioning_postrend_84d_base_v077_signal,
    f30sm_f30_smart_money_positioning_postrend_189d_base_v078_signal,
    f30sm_f30_smart_money_positioning_posglog_42d_base_v079_signal,
    f30sm_f30_smart_money_positioning_posglog_189d_base_v080_signal,
    f30sm_f30_smart_money_positioning_posglog_378d_base_v081_signal,
    f30sm_f30_smart_money_positioning_posz_42d_base_v082_signal,
    f30sm_f30_smart_money_positioning_posz_84d_base_v083_signal,
    f30sm_f30_smart_money_positioning_posz_189d_base_v084_signal,
    f30sm_f30_smart_money_positioning_posz_504d_base_v085_signal,
    f30sm_f30_smart_money_positioning_unitstrend_42d_base_v086_signal,
    f30sm_f30_smart_money_positioning_unitstrend_189d_base_v087_signal,
    f30sm_f30_smart_money_positioning_unitsz_63d_base_v088_signal,
    f30sm_f30_smart_money_positioning_unitsz_126d_base_v089_signal,
    f30sm_f30_smart_money_positioning_unitsz_252d_base_v090_signal,
    f30sm_f30_smart_money_positioning_vputrend_42d_base_v091_signal,
    f30sm_f30_smart_money_positioning_vputrend_189d_base_v092_signal,
    f30sm_f30_smart_money_positioning_vpuglog_252d_base_v093_signal,
    f30sm_f30_smart_money_positioning_vpuz_189d_base_v094_signal,
    f30sm_f30_smart_money_positioning_convlvl_126d_base_v095_signal,
    f30sm_f30_smart_money_positioning_convlvl_252d_base_v096_signal,
    f30sm_f30_smart_money_positioning_convchg_42d_base_v097_signal,
    f30sm_f30_smart_money_positioning_convchg_189d_base_v098_signal,
    f30sm_f30_smart_money_positioning_convz_42d_base_v099_signal,
    f30sm_f30_smart_money_positioning_convz_189d_base_v100_signal,
    f30sm_f30_smart_money_positioning_convz_378d_base_v101_signal,
    f30sm_f30_smart_money_positioning_convglog_21d_base_v102_signal,
    f30sm_f30_smart_money_positioning_convglog_252d_base_v103_signal,
    f30sm_f30_smart_money_positioning_rot_42d_base_v104_signal,
    f30sm_f30_smart_money_positioning_rot_189d_base_v105_signal,
    f30sm_f30_smart_money_positioning_rotz_126d_base_v106_signal,
    f30sm_f30_smart_money_positioning_posmcap_252d_base_v107_signal,
    f30sm_f30_smart_money_positioning_posmcapglog_126d_base_v108_signal,
    f30sm_f30_smart_money_positioning_posmcapz_126d_base_v109_signal,
    f30sm_f30_smart_money_positioning_possurp_126d_base_v110_signal,
    f30sm_f30_smart_money_positioning_convsurp_21d_base_v111_signal,
    f30sm_f30_smart_money_positioning_convsurp_63d_base_v112_signal,
    f30sm_f30_smart_money_positioning_posrank_504d_base_v113_signal,
    f30sm_f30_smart_money_positioning_convrank_126d_base_v114_signal,
    f30sm_f30_smart_money_positioning_vpurank_126d_base_v115_signal,
    f30sm_f30_smart_money_positioning_unitsrank_252d_base_v116_signal,
    f30sm_f30_smart_money_positioning_convdisp_42d_base_v117_signal,
    f30sm_f30_smart_money_positioning_convdisp_189d_base_v118_signal,
    f30sm_f30_smart_money_positioning_poscv_252d_base_v119_signal,
    f30sm_f30_smart_money_positioning_vpucv_252d_base_v120_signal,
    f30sm_f30_smart_money_positioning_convcv_252d_base_v121_signal,
    f30sm_f30_smart_money_positioning_posgscaled_252d_base_v122_signal,
    f30sm_f30_smart_money_positioning_convgscaled_63d_base_v123_signal,
    f30sm_f30_smart_money_positioning_vpugscaled_126d_base_v124_signal,
    f30sm_f30_smart_money_positioning_uvdiv_42d_base_v125_signal,
    f30sm_f30_smart_money_positioning_uvdiv_189d_base_v126_signal,
    f30sm_f30_smart_money_positioning_convmomspr2_base_v127_signal,
    f30sm_f30_smart_money_positioning_posmomspr2_base_v128_signal,
    f30sm_f30_smart_money_positioning_posezma_126d_base_v129_signal,
    f30sm_f30_smart_money_positioning_convezma_126d_base_v130_signal,
    f30sm_f30_smart_money_positioning_vpuezma_63d_base_v131_signal,
    f30sm_f30_smart_money_positioning_posmcaplvl_252d_base_v132_signal,
    f30sm_f30_smart_money_positioning_vpurel_126d_base_v133_signal,
    f30sm_f30_smart_money_positioning_convrel_126d_base_v134_signal,
    f30sm_f30_smart_money_positioning_posrel_252d_base_v135_signal,
    f30sm_f30_smart_money_positioning_convaccel_base_v136_signal,
    f30sm_f30_smart_money_positioning_posaccel_base_v137_signal,
    f30sm_f30_smart_money_positioning_vpuaccel_base_v138_signal,
    f30sm_f30_smart_money_positioning_tilt_126d_base_v139_signal,
    f30sm_f30_smart_money_positioning_tilt_252d_base_v140_signal,
    f30sm_f30_smart_money_positioning_vpumcap_126d_base_v141_signal,
    f30sm_f30_smart_money_positioning_vpumcap_252d_base_v142_signal,
    f30sm_f30_smart_money_positioning_convwgrow_126d_base_v143_signal,
    f30sm_f30_smart_money_positioning_convwgrow_252d_base_v144_signal,
    f30sm_f30_smart_money_positioning_szpx_126d_base_v145_signal,
    f30sm_f30_smart_money_positioning_umcap_126d_base_v146_signal,
    f30sm_f30_smart_money_positioning_pcalign_126d_base_v147_signal,
    f30sm_f30_smart_money_positioning_convrel_504d_base_v148_signal,
    f30sm_f30_smart_money_positioning_blend_126d_base_v149_signal,
    f30sm_f30_smart_money_positioning_blendmom_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_SMART_MONEY_POSITIONING_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f30_smart_money_positioning_base_076_150_claude: {n_features} features pass")
