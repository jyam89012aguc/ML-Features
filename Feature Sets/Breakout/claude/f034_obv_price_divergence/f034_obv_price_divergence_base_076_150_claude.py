import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f034_obv_proxy(closeadj, volume):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    return (sign * volume).cumsum()


def _f034_price_slope(closeadj, w):
    return closeadj.diff(w) / closeadj.abs().replace(0, np.nan)


def _f034_obv_price_gap(closeadj, volume, w):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    obv = (sign * volume).cumsum()
    obv_sl = obv.diff(w) / obv.abs().replace(0, np.nan)
    price_sl = closeadj.diff(w) / closeadj.abs().replace(0, np.nan)
    return (obv_sl - price_sl) * closeadj


def f034opd_f034_obv_price_divergence_sqgap_126d_base_v076_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_189d_base_v077_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 189)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_252d_base_v078_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_378d_base_v079_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 378)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_504d_base_v080_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 504)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_5d_base_v081_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 5)
    dv = closeadj * volume
    result = g * _mean(dv, 5) / _mean(dv, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_10d_base_v082_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 10)
    dv = closeadj * volume
    result = g * _mean(dv, 5) / _mean(dv, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_21d_base_v083_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    dv = closeadj * volume
    result = g * _mean(dv, 10) / _mean(dv, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_42d_base_v084_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 42)
    dv = closeadj * volume
    result = g * _mean(dv, 21) / _mean(dv, 42).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_63d_base_v085_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    dv = closeadj * volume
    result = g * _mean(dv, 31) / _mean(dv, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_126d_base_v086_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    dv = closeadj * volume
    result = g * _mean(dv, 63) / _mean(dv, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_189d_base_v087_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 189)
    dv = closeadj * volume
    result = g * _mean(dv, 94) / _mean(dv, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_252d_base_v088_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    dv = closeadj * volume
    result = g * _mean(dv, 126) / _mean(dv, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_378d_base_v089_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 378)
    dv = closeadj * volume
    result = g * _mean(dv, 189) / _mean(dv, 378).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_504d_base_v090_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 504)
    dv = closeadj * volume
    result = g * _mean(dv, 252) / _mean(dv, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_5d_base_v091_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 5)
    result = g.diff(2)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_10d_base_v092_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 10)
    result = g.diff(2)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_21d_base_v093_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    result = g.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_42d_base_v094_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 42)
    result = g.diff(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_63d_base_v095_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    result = g.diff(15)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_126d_base_v096_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    result = g.diff(31)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_189d_base_v097_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 189)
    result = g.diff(47)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_252d_base_v098_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    result = g.diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_378d_base_v099_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 378)
    result = g.diff(94)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_diffgap_504d_base_v100_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 504)
    result = g.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_5d_base_v101_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(5) / o.abs().replace(0, np.nan)
    result = _mean(sl, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_10d_base_v102_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(10) / o.abs().replace(0, np.nan)
    result = _mean(sl, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_21d_base_v103_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(21) / o.abs().replace(0, np.nan)
    result = _mean(sl, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_42d_base_v104_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(42) / o.abs().replace(0, np.nan)
    result = _mean(sl, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_63d_base_v105_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(63) / o.abs().replace(0, np.nan)
    result = _mean(sl, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_126d_base_v106_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(126) / o.abs().replace(0, np.nan)
    result = _mean(sl, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_189d_base_v107_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(189) / o.abs().replace(0, np.nan)
    result = _mean(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_252d_base_v108_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    result = _mean(sl, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_378d_base_v109_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(378) / o.abs().replace(0, np.nan)
    result = _mean(sl, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_504d_base_v110_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(504) / o.abs().replace(0, np.nan)
    result = _mean(sl, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_5d_base_v111_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(5) / o.abs().replace(0, np.nan)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_10d_base_v112_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(10) / o.abs().replace(0, np.nan)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_21d_base_v113_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(21) / o.abs().replace(0, np.nan)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_42d_base_v114_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(42) / o.abs().replace(0, np.nan)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_63d_base_v115_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(63) / o.abs().replace(0, np.nan)
    result = _z(sl, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_126d_base_v116_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(126) / o.abs().replace(0, np.nan)
    result = _z(sl, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_189d_base_v117_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(189) / o.abs().replace(0, np.nan)
    result = _z(sl, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_252d_base_v118_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    result = _z(sl, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_378d_base_v119_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(378) / o.abs().replace(0, np.nan)
    result = _z(sl, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_504d_base_v120_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(504) / o.abs().replace(0, np.nan)
    result = _z(sl, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_5d_base_v121_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 5)
    result = _z(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_10d_base_v122_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 10)
    result = _z(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_21d_base_v123_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    result = _z(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_42d_base_v124_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 42)
    result = _z(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_63d_base_v125_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    result = _z(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_126d_base_v126_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    result = _z(p, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_189d_base_v127_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 189)
    result = _z(p, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_252d_base_v128_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    result = _z(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_378d_base_v129_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 378)
    result = _z(p, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_504d_base_v130_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 504)
    result = _z(p, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_5d_base_v131_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 5)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_10d_base_v132_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 10)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_21d_base_v133_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_42d_base_v134_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 42)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_63d_base_v135_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_126d_base_v136_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_189d_base_v137_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 189)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_252d_base_v138_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_378d_base_v139_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 378)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_504d_base_v140_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 504)
    result = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_5d_base_v141_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 5)
    result = g.ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_10d_base_v142_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 10)
    result = g.ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_21d_base_v143_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    result = g.ewm(span=10, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_42d_base_v144_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 42)
    result = g.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_63d_base_v145_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    result = g.ewm(span=31, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_126d_base_v146_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    result = g.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_189d_base_v147_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 189)
    result = g.ewm(span=94, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_252d_base_v148_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    result = g.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_378d_base_v149_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 378)
    result = g.ewm(span=189, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_504d_base_v150_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 504)
    result = g.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f034opd_f034_obv_price_divergence_sqgap_126d_base_v076_signal,
    f034opd_f034_obv_price_divergence_sqgap_189d_base_v077_signal,
    f034opd_f034_obv_price_divergence_sqgap_252d_base_v078_signal,
    f034opd_f034_obv_price_divergence_sqgap_378d_base_v079_signal,
    f034opd_f034_obv_price_divergence_sqgap_504d_base_v080_signal,
    f034opd_f034_obv_price_divergence_gapxdv_5d_base_v081_signal,
    f034opd_f034_obv_price_divergence_gapxdv_10d_base_v082_signal,
    f034opd_f034_obv_price_divergence_gapxdv_21d_base_v083_signal,
    f034opd_f034_obv_price_divergence_gapxdv_42d_base_v084_signal,
    f034opd_f034_obv_price_divergence_gapxdv_63d_base_v085_signal,
    f034opd_f034_obv_price_divergence_gapxdv_126d_base_v086_signal,
    f034opd_f034_obv_price_divergence_gapxdv_189d_base_v087_signal,
    f034opd_f034_obv_price_divergence_gapxdv_252d_base_v088_signal,
    f034opd_f034_obv_price_divergence_gapxdv_378d_base_v089_signal,
    f034opd_f034_obv_price_divergence_gapxdv_504d_base_v090_signal,
    f034opd_f034_obv_price_divergence_diffgap_5d_base_v091_signal,
    f034opd_f034_obv_price_divergence_diffgap_10d_base_v092_signal,
    f034opd_f034_obv_price_divergence_diffgap_21d_base_v093_signal,
    f034opd_f034_obv_price_divergence_diffgap_42d_base_v094_signal,
    f034opd_f034_obv_price_divergence_diffgap_63d_base_v095_signal,
    f034opd_f034_obv_price_divergence_diffgap_126d_base_v096_signal,
    f034opd_f034_obv_price_divergence_diffgap_189d_base_v097_signal,
    f034opd_f034_obv_price_divergence_diffgap_252d_base_v098_signal,
    f034opd_f034_obv_price_divergence_diffgap_378d_base_v099_signal,
    f034opd_f034_obv_price_divergence_diffgap_504d_base_v100_signal,
    f034opd_f034_obv_price_divergence_smoslope_5d_base_v101_signal,
    f034opd_f034_obv_price_divergence_smoslope_10d_base_v102_signal,
    f034opd_f034_obv_price_divergence_smoslope_21d_base_v103_signal,
    f034opd_f034_obv_price_divergence_smoslope_42d_base_v104_signal,
    f034opd_f034_obv_price_divergence_smoslope_63d_base_v105_signal,
    f034opd_f034_obv_price_divergence_smoslope_126d_base_v106_signal,
    f034opd_f034_obv_price_divergence_smoslope_189d_base_v107_signal,
    f034opd_f034_obv_price_divergence_smoslope_252d_base_v108_signal,
    f034opd_f034_obv_price_divergence_smoslope_378d_base_v109_signal,
    f034opd_f034_obv_price_divergence_smoslope_504d_base_v110_signal,
    f034opd_f034_obv_price_divergence_zoslope_5d_base_v111_signal,
    f034opd_f034_obv_price_divergence_zoslope_10d_base_v112_signal,
    f034opd_f034_obv_price_divergence_zoslope_21d_base_v113_signal,
    f034opd_f034_obv_price_divergence_zoslope_42d_base_v114_signal,
    f034opd_f034_obv_price_divergence_zoslope_63d_base_v115_signal,
    f034opd_f034_obv_price_divergence_zoslope_126d_base_v116_signal,
    f034opd_f034_obv_price_divergence_zoslope_189d_base_v117_signal,
    f034opd_f034_obv_price_divergence_zoslope_252d_base_v118_signal,
    f034opd_f034_obv_price_divergence_zoslope_378d_base_v119_signal,
    f034opd_f034_obv_price_divergence_zoslope_504d_base_v120_signal,
    f034opd_f034_obv_price_divergence_zpslope_5d_base_v121_signal,
    f034opd_f034_obv_price_divergence_zpslope_10d_base_v122_signal,
    f034opd_f034_obv_price_divergence_zpslope_21d_base_v123_signal,
    f034opd_f034_obv_price_divergence_zpslope_42d_base_v124_signal,
    f034opd_f034_obv_price_divergence_zpslope_63d_base_v125_signal,
    f034opd_f034_obv_price_divergence_zpslope_126d_base_v126_signal,
    f034opd_f034_obv_price_divergence_zpslope_189d_base_v127_signal,
    f034opd_f034_obv_price_divergence_zpslope_252d_base_v128_signal,
    f034opd_f034_obv_price_divergence_zpslope_378d_base_v129_signal,
    f034opd_f034_obv_price_divergence_zpslope_504d_base_v130_signal,
    f034opd_f034_obv_price_divergence_absgap_5d_base_v131_signal,
    f034opd_f034_obv_price_divergence_absgap_10d_base_v132_signal,
    f034opd_f034_obv_price_divergence_absgap_21d_base_v133_signal,
    f034opd_f034_obv_price_divergence_absgap_42d_base_v134_signal,
    f034opd_f034_obv_price_divergence_absgap_63d_base_v135_signal,
    f034opd_f034_obv_price_divergence_absgap_126d_base_v136_signal,
    f034opd_f034_obv_price_divergence_absgap_189d_base_v137_signal,
    f034opd_f034_obv_price_divergence_absgap_252d_base_v138_signal,
    f034opd_f034_obv_price_divergence_absgap_378d_base_v139_signal,
    f034opd_f034_obv_price_divergence_absgap_504d_base_v140_signal,
    f034opd_f034_obv_price_divergence_emagap_5d_base_v141_signal,
    f034opd_f034_obv_price_divergence_emagap_10d_base_v142_signal,
    f034opd_f034_obv_price_divergence_emagap_21d_base_v143_signal,
    f034opd_f034_obv_price_divergence_emagap_42d_base_v144_signal,
    f034opd_f034_obv_price_divergence_emagap_63d_base_v145_signal,
    f034opd_f034_obv_price_divergence_emagap_126d_base_v146_signal,
    f034opd_f034_obv_price_divergence_emagap_189d_base_v147_signal,
    f034opd_f034_obv_price_divergence_emagap_252d_base_v148_signal,
    f034opd_f034_obv_price_divergence_emagap_378d_base_v149_signal,
    f034opd_f034_obv_price_divergence_emagap_504d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F034_OBV_PRICE_DIVERGENCE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f034_obv_proxy', '_f034_price_slope', '_f034_obv_price_gap')
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f034_obv_price_divergence_base_076_150_claude: {n_features} features pass")
