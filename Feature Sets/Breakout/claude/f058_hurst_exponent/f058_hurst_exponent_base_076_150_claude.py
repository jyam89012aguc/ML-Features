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
def _f058_rolling_variance(close, w):
    ret = np.log(close.replace(0, np.nan).abs()).diff()
    return ret.rolling(w, min_periods=max(1, w // 2)).var()


def _f058_hurst_proxy(close, w):
    ret = np.log(close.replace(0, np.nan).abs()).diff()
    var_w = ret.rolling(w, min_periods=max(1, w // 2)).var()
    var_1 = ret.rolling(max(2, w // 4), min_periods=2).var()
    return 0.5 * np.log(var_w / var_1.replace(0, np.nan)).abs() / float(np.log(max(2, w)))


def _f058_persistence_score(close, w):
    ret = np.log(close.replace(0, np.nan).abs()).diff()
    m = ret.rolling(w, min_periods=max(1, w // 2)).mean()
    centered = ret - m
    num = (centered * centered.shift(1)).rolling(w, min_periods=max(1, w // 2)).mean()
    den = (centered * centered).rolling(w, min_periods=max(1, w // 2)).mean()
    return num / den.replace(0, np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_5d_base_v076_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 5), 252)) * _z(_f058_rolling_variance(closeadj, 5), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_10d_base_v077_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 10), 252)) * _z(_f058_rolling_variance(closeadj, 10), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_21d_base_v078_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 21), 252)) * _z(_f058_rolling_variance(closeadj, 21), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_42d_base_v079_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 42), 252)) * _z(_f058_rolling_variance(closeadj, 42), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_63d_base_v080_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 63), 252)) * _z(_f058_rolling_variance(closeadj, 63), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_126d_base_v081_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 126), 252)) * _z(_f058_rolling_variance(closeadj, 126), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_189d_base_v082_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 189), 252)) * _z(_f058_rolling_variance(closeadj, 189), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_252d_base_v083_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 252), 252)) * _z(_f058_rolling_variance(closeadj, 252), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_378d_base_v084_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 378), 252)) * _z(_f058_rolling_variance(closeadj, 378), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarsqrt_504d_base_v085_signal(closeadj):
    result = np.sign(_z(_f058_rolling_variance(closeadj, 504), 252)) * _z(_f058_rolling_variance(closeadj, 504), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_5d_base_v086_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 5), 252)) * _z(_f058_hurst_proxy(closeadj, 5), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_10d_base_v087_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 10), 252)) * _z(_f058_hurst_proxy(closeadj, 10), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_21d_base_v088_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 21), 252)) * _z(_f058_hurst_proxy(closeadj, 21), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_42d_base_v089_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 42), 252)) * _z(_f058_hurst_proxy(closeadj, 42), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_63d_base_v090_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 63), 252)) * _z(_f058_hurst_proxy(closeadj, 63), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_126d_base_v091_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 126), 252)) * _z(_f058_hurst_proxy(closeadj, 126), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_189d_base_v092_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 189), 252)) * _z(_f058_hurst_proxy(closeadj, 189), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_252d_base_v093_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 252), 252)) * _z(_f058_hurst_proxy(closeadj, 252), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_378d_base_v094_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 378), 252)) * _z(_f058_hurst_proxy(closeadj, 378), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstsqrt_504d_base_v095_signal(closeadj):
    result = np.sign(_z(_f058_hurst_proxy(closeadj, 504), 252)) * _z(_f058_hurst_proxy(closeadj, 504), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_5d_base_v096_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 5), 252)) * _z(_f058_persistence_score(closeadj, 5), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_10d_base_v097_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 10), 252)) * _z(_f058_persistence_score(closeadj, 10), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_21d_base_v098_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 21), 252)) * _z(_f058_persistence_score(closeadj, 21), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_42d_base_v099_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 42), 252)) * _z(_f058_persistence_score(closeadj, 42), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_63d_base_v100_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 63), 252)) * _z(_f058_persistence_score(closeadj, 63), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_126d_base_v101_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 126), 252)) * _z(_f058_persistence_score(closeadj, 126), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_189d_base_v102_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 189), 252)) * _z(_f058_persistence_score(closeadj, 189), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_252d_base_v103_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 252), 252)) * _z(_f058_persistence_score(closeadj, 252), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_378d_base_v104_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 378), 252)) * _z(_f058_persistence_score(closeadj, 378), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perssqrt_504d_base_v105_signal(closeadj):
    result = np.sign(_z(_f058_persistence_score(closeadj, 504), 252)) * _z(_f058_persistence_score(closeadj, 504), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_5d_base_v106_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 5), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_10d_base_v107_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 10), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_21d_base_v108_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 21), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_42d_base_v109_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 42), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_63d_base_v110_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 63), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_126d_base_v111_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 126), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_189d_base_v112_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 189), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_252d_base_v113_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 252), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_378d_base_v114_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 378), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarclip_504d_base_v115_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 504), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_5d_base_v116_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 5), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_10d_base_v117_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 10), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_21d_base_v118_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 21), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_42d_base_v119_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 42), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_63d_base_v120_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 63), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_126d_base_v121_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 126), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_189d_base_v122_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 189), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_252d_base_v123_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 252), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_378d_base_v124_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 378), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstclip_504d_base_v125_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 504), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_5d_base_v126_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 5), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_10d_base_v127_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 10), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_21d_base_v128_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 21), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_42d_base_v129_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 42), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_63d_base_v130_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 63), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_126d_base_v131_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 126), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_189d_base_v132_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 189), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_252d_base_v133_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 252), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_378d_base_v134_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 378), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persclip_504d_base_v135_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 504), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_5d_base_v136_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 5), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_10d_base_v137_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 10), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_21d_base_v138_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 21), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_42d_base_v139_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 42), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_63d_base_v140_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 63), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_126d_base_v141_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 126), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_189d_base_v142_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 189), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_252d_base_v143_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 252), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_378d_base_v144_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 378), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvaremaz_504d_base_v145_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 504), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstemaz_5d_base_v146_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 5), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstemaz_10d_base_v147_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 10), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstemaz_21d_base_v148_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 21), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstemaz_42d_base_v149_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 42), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstemaz_63d_base_v150_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 63), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f058hex_f058_hurst_exponent_rvarsqrt_5d_base_v076_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_10d_base_v077_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_21d_base_v078_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_42d_base_v079_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_63d_base_v080_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_126d_base_v081_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_189d_base_v082_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_252d_base_v083_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_378d_base_v084_signal,
    f058hex_f058_hurst_exponent_rvarsqrt_504d_base_v085_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_5d_base_v086_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_10d_base_v087_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_21d_base_v088_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_42d_base_v089_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_63d_base_v090_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_126d_base_v091_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_189d_base_v092_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_252d_base_v093_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_378d_base_v094_signal,
    f058hex_f058_hurst_exponent_hrstsqrt_504d_base_v095_signal,
    f058hex_f058_hurst_exponent_perssqrt_5d_base_v096_signal,
    f058hex_f058_hurst_exponent_perssqrt_10d_base_v097_signal,
    f058hex_f058_hurst_exponent_perssqrt_21d_base_v098_signal,
    f058hex_f058_hurst_exponent_perssqrt_42d_base_v099_signal,
    f058hex_f058_hurst_exponent_perssqrt_63d_base_v100_signal,
    f058hex_f058_hurst_exponent_perssqrt_126d_base_v101_signal,
    f058hex_f058_hurst_exponent_perssqrt_189d_base_v102_signal,
    f058hex_f058_hurst_exponent_perssqrt_252d_base_v103_signal,
    f058hex_f058_hurst_exponent_perssqrt_378d_base_v104_signal,
    f058hex_f058_hurst_exponent_perssqrt_504d_base_v105_signal,
    f058hex_f058_hurst_exponent_rvarclip_5d_base_v106_signal,
    f058hex_f058_hurst_exponent_rvarclip_10d_base_v107_signal,
    f058hex_f058_hurst_exponent_rvarclip_21d_base_v108_signal,
    f058hex_f058_hurst_exponent_rvarclip_42d_base_v109_signal,
    f058hex_f058_hurst_exponent_rvarclip_63d_base_v110_signal,
    f058hex_f058_hurst_exponent_rvarclip_126d_base_v111_signal,
    f058hex_f058_hurst_exponent_rvarclip_189d_base_v112_signal,
    f058hex_f058_hurst_exponent_rvarclip_252d_base_v113_signal,
    f058hex_f058_hurst_exponent_rvarclip_378d_base_v114_signal,
    f058hex_f058_hurst_exponent_rvarclip_504d_base_v115_signal,
    f058hex_f058_hurst_exponent_hrstclip_5d_base_v116_signal,
    f058hex_f058_hurst_exponent_hrstclip_10d_base_v117_signal,
    f058hex_f058_hurst_exponent_hrstclip_21d_base_v118_signal,
    f058hex_f058_hurst_exponent_hrstclip_42d_base_v119_signal,
    f058hex_f058_hurst_exponent_hrstclip_63d_base_v120_signal,
    f058hex_f058_hurst_exponent_hrstclip_126d_base_v121_signal,
    f058hex_f058_hurst_exponent_hrstclip_189d_base_v122_signal,
    f058hex_f058_hurst_exponent_hrstclip_252d_base_v123_signal,
    f058hex_f058_hurst_exponent_hrstclip_378d_base_v124_signal,
    f058hex_f058_hurst_exponent_hrstclip_504d_base_v125_signal,
    f058hex_f058_hurst_exponent_persclip_5d_base_v126_signal,
    f058hex_f058_hurst_exponent_persclip_10d_base_v127_signal,
    f058hex_f058_hurst_exponent_persclip_21d_base_v128_signal,
    f058hex_f058_hurst_exponent_persclip_42d_base_v129_signal,
    f058hex_f058_hurst_exponent_persclip_63d_base_v130_signal,
    f058hex_f058_hurst_exponent_persclip_126d_base_v131_signal,
    f058hex_f058_hurst_exponent_persclip_189d_base_v132_signal,
    f058hex_f058_hurst_exponent_persclip_252d_base_v133_signal,
    f058hex_f058_hurst_exponent_persclip_378d_base_v134_signal,
    f058hex_f058_hurst_exponent_persclip_504d_base_v135_signal,
    f058hex_f058_hurst_exponent_rvaremaz_5d_base_v136_signal,
    f058hex_f058_hurst_exponent_rvaremaz_10d_base_v137_signal,
    f058hex_f058_hurst_exponent_rvaremaz_21d_base_v138_signal,
    f058hex_f058_hurst_exponent_rvaremaz_42d_base_v139_signal,
    f058hex_f058_hurst_exponent_rvaremaz_63d_base_v140_signal,
    f058hex_f058_hurst_exponent_rvaremaz_126d_base_v141_signal,
    f058hex_f058_hurst_exponent_rvaremaz_189d_base_v142_signal,
    f058hex_f058_hurst_exponent_rvaremaz_252d_base_v143_signal,
    f058hex_f058_hurst_exponent_rvaremaz_378d_base_v144_signal,
    f058hex_f058_hurst_exponent_rvaremaz_504d_base_v145_signal,
    f058hex_f058_hurst_exponent_hrstemaz_5d_base_v146_signal,
    f058hex_f058_hurst_exponent_hrstemaz_10d_base_v147_signal,
    f058hex_f058_hurst_exponent_hrstemaz_21d_base_v148_signal,
    f058hex_f058_hurst_exponent_hrstemaz_42d_base_v149_signal,
    f058hex_f058_hurst_exponent_hrstemaz_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F058_HURST_EXPONENT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f058_rolling_variance", "_f058_hurst_proxy", "_f058_persistence_score",)
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
    print(f"OK f058_hurst_exponent_base_076_150_claude: {n_features} features pass")
