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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _logret(s, w):
    return np.log(s.replace(0, np.nan)).diff(periods=w)


def _f07_tangible_bv(equity, intangibles):
    return equity - intangibles


def _f07_tangible_bvps(equity, intangibles, sharesbas):
    tbv = equity - intangibles
    return tbv / sharesbas.replace(0, np.nan)


def _f07_tbv_growth(equity, intangibles, sharesbas, w):
    tbvps = (equity - intangibles) / sharesbas.replace(0, np.nan)
    return tbvps.pct_change(periods=w)


def f07tbc_f07_tangible_book_compound_tbvgrowthz_126d_base_v076_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthz_252d_base_v077_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthstd_21d_base_v078_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthstd_63d_base_v079_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthstd_126d_base_v080_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthstd_252d_base_v081_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsxgrowth_21d_base_v082_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    result = bvps * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsxgrowth_63d_base_v083_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    result = bvps * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsxgrowth_126d_base_v084_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    result = bvps * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsxgrowth_252d_base_v085_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    result = bvps * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthratio_21v63_base_v086_signal(equity, intangibles, sharesbas, closeadj):
    a = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    b = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthratio_63v252_base_v087_signal(equity, intangibles, sharesbas, closeadj):
    a = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    b = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthratio_126v504_base_v088_signal(equity, intangibles, sharesbas, closeadj):
    a = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    b = _f07_tbv_growth(equity, intangibles, sharesbas, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthratio_42v189_base_v089_signal(equity, intangibles, sharesbas, closeadj):
    a = _f07_tbv_growth(equity, intangibles, sharesbas, 42)
    b = _f07_tbv_growth(equity, intangibles, sharesbas, 189)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsemax_21d_base_v090_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps - _ema(bvps, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsemax_63d_base_v091_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps - _ema(bvps, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsemax_126d_base_v092_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps - _ema(bvps, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsemax_252d_base_v093_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps - _ema(bvps, 252)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvcompound_63d_base_v094_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = (base / base.shift(63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvcompound_126d_base_v095_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = (base / base.shift(126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvcompound_252d_base_v096_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = (base / base.shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvcompound_504d_base_v097_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = (base / base.shift(504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpscompound_63d_base_v098_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = (bvps / bvps.shift(63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpscompound_126d_base_v099_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = (bvps / bvps.shift(126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpscompound_252d_base_v100_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = (bvps / bvps.shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpscompound_504d_base_v101_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = (bvps / bvps.shift(504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxintang_63d_base_v102_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    intratio = intangibles / equity.replace(0, np.nan)
    result = g * intratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxintang_252d_base_v103_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    intratio = intangibles / equity.replace(0, np.nan)
    result = g * intratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsdev_21d_base_v104_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = (base - _mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsdev_63d_base_v105_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = (base - _mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsdev_126d_base_v106_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = (base - _mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsdev_252d_base_v107_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_21d_base_v108_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=21)
    result = _mean(base, 21) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_42d_base_v109_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=42)
    result = _mean(base, 42) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_63d_base_v110_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=63)
    result = _mean(base, 63) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_126d_base_v111_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=126)
    result = _mean(base, 126) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_189d_base_v112_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=189)
    result = _mean(base, 189) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_252d_base_v113_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=252)
    result = _mean(base, 252) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_378d_base_v114_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=378)
    result = _mean(base, 378) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_504d_base_v115_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=504)
    result = _mean(base, 504) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_21d_base_v116_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=21)
    result = _mean(base, 21) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_42d_base_v117_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=42)
    result = _mean(base, 42) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_63d_base_v118_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=63)
    result = _mean(base, 63) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_126d_base_v119_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=126)
    result = _mean(base, 126) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_189d_base_v120_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=189)
    result = _mean(base, 189) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_252d_base_v121_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=252)
    result = _mean(base, 252) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_378d_base_v122_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=378)
    result = _mean(base, 378) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_504d_base_v123_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=504)
    result = _mean(base, 504) * rv
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_21d_base_v124_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    dil = sharesbas.pct_change(periods=21)
    result = g * dil * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_42d_base_v125_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 42)
    dil = sharesbas.pct_change(periods=42)
    result = g * dil * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_63d_base_v126_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    dil = sharesbas.pct_change(periods=63)
    result = g * dil * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_126d_base_v127_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    dil = sharesbas.pct_change(periods=126)
    result = g * dil * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_189d_base_v128_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 189)
    dil = sharesbas.pct_change(periods=189)
    result = g * dil * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_252d_base_v129_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    dil = sharesbas.pct_change(periods=252)
    result = g * dil * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_378d_base_v130_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 378)
    dil = sharesbas.pct_change(periods=378)
    result = g * dil * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_504d_base_v131_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 504)
    dil = sharesbas.pct_change(periods=504)
    result = g * dil * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_21d_base_v132_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.abs() / _mean(base.abs(), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_42d_base_v133_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.abs() / _mean(base.abs(), 42).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_63d_base_v134_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.abs() / _mean(base.abs(), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_126d_base_v135_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.abs() / _mean(base.abs(), 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_189d_base_v136_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.abs() / _mean(base.abs(), 189).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_252d_base_v137_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.abs() / _mean(base.abs(), 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_378d_base_v138_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.abs() / _mean(base.abs(), 378).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_21d_base_v139_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    result = g * eq_ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_42d_base_v140_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 42)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    result = g * eq_ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_63d_base_v141_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    result = g * eq_ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_126d_base_v142_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    result = g * eq_ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_189d_base_v143_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 189)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    result = g * eq_ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_252d_base_v144_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    result = g * eq_ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_21d_base_v145_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps.rolling(21, min_periods=max(1, 21//2)).sum() / _mean(bvps, 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_42d_base_v146_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps.rolling(42, min_periods=max(1, 42//2)).sum() / _mean(bvps, 42).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_63d_base_v147_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps.rolling(63, min_periods=max(1, 63//2)).sum() / _mean(bvps, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_126d_base_v148_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps.rolling(126, min_periods=max(1, 126//2)).sum() / _mean(bvps, 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_189d_base_v149_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps.rolling(189, min_periods=max(1, 189//2)).sum() / _mean(bvps, 189).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_252d_base_v150_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps.rolling(252, min_periods=max(1, 252//2)).sum() / _mean(bvps, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07tbc_f07_tangible_book_compound_tbvgrowthz_126d_base_v076_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthz_252d_base_v077_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthstd_21d_base_v078_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthstd_63d_base_v079_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthstd_126d_base_v080_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthstd_252d_base_v081_signal,
    f07tbc_f07_tangible_book_compound_tbvpsxgrowth_21d_base_v082_signal,
    f07tbc_f07_tangible_book_compound_tbvpsxgrowth_63d_base_v083_signal,
    f07tbc_f07_tangible_book_compound_tbvpsxgrowth_126d_base_v084_signal,
    f07tbc_f07_tangible_book_compound_tbvpsxgrowth_252d_base_v085_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthratio_21v63_base_v086_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthratio_63v252_base_v087_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthratio_126v504_base_v088_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthratio_42v189_base_v089_signal,
    f07tbc_f07_tangible_book_compound_tbvpsemax_21d_base_v090_signal,
    f07tbc_f07_tangible_book_compound_tbvpsemax_63d_base_v091_signal,
    f07tbc_f07_tangible_book_compound_tbvpsemax_126d_base_v092_signal,
    f07tbc_f07_tangible_book_compound_tbvpsemax_252d_base_v093_signal,
    f07tbc_f07_tangible_book_compound_tbvcompound_63d_base_v094_signal,
    f07tbc_f07_tangible_book_compound_tbvcompound_126d_base_v095_signal,
    f07tbc_f07_tangible_book_compound_tbvcompound_252d_base_v096_signal,
    f07tbc_f07_tangible_book_compound_tbvcompound_504d_base_v097_signal,
    f07tbc_f07_tangible_book_compound_tbvpscompound_63d_base_v098_signal,
    f07tbc_f07_tangible_book_compound_tbvpscompound_126d_base_v099_signal,
    f07tbc_f07_tangible_book_compound_tbvpscompound_252d_base_v100_signal,
    f07tbc_f07_tangible_book_compound_tbvpscompound_504d_base_v101_signal,
    f07tbc_f07_tangible_book_compound_tbvgxintang_63d_base_v102_signal,
    f07tbc_f07_tangible_book_compound_tbvgxintang_252d_base_v103_signal,
    f07tbc_f07_tangible_book_compound_tbvpsdev_21d_base_v104_signal,
    f07tbc_f07_tangible_book_compound_tbvpsdev_63d_base_v105_signal,
    f07tbc_f07_tangible_book_compound_tbvpsdev_126d_base_v106_signal,
    f07tbc_f07_tangible_book_compound_tbvpsdev_252d_base_v107_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_21d_base_v108_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_42d_base_v109_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_63d_base_v110_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_126d_base_v111_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_189d_base_v112_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_252d_base_v113_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_378d_base_v114_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_504d_base_v115_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_21d_base_v116_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_42d_base_v117_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_63d_base_v118_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_126d_base_v119_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_189d_base_v120_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_252d_base_v121_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_378d_base_v122_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_504d_base_v123_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_21d_base_v124_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_42d_base_v125_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_63d_base_v126_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_126d_base_v127_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_189d_base_v128_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_252d_base_v129_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_378d_base_v130_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_504d_base_v131_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_21d_base_v132_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_42d_base_v133_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_63d_base_v134_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_126d_base_v135_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_189d_base_v136_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_252d_base_v137_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_378d_base_v138_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_21d_base_v139_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_42d_base_v140_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_63d_base_v141_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_126d_base_v142_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_189d_base_v143_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_252d_base_v144_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_21d_base_v145_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_42d_base_v146_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_63d_base_v147_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_126d_base_v148_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_189d_base_v149_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_252d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_TANGIBLE_BOOK_COMPOUND_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    cols = {
        "closeadj": closeadj, "volume": volume, "revenue": revenue,
        "netinc": netinc, "assets": assets, "equity": equity, "debt": debt,
        "intangibles": intangibles, "sharesbas": sharesbas, "roa": roa, "roe": roe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f07_tangible_bv', '_f07_tangible_bvps', '_f07_tbv_growth')
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
    print(f"OK f07_tangible_book_compound_base_076_150_claude: {n_features} features pass")
