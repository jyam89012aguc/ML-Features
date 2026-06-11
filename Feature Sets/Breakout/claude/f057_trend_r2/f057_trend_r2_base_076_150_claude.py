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
def _f057_trend_fit(close, w):
    lp = np.log(close.replace(0, np.nan).abs())
    m = lp.rolling(w, min_periods=max(1, w // 2)).mean()
    slope = (lp - lp.shift(w)) / float(w)
    return m + slope * (w / 2.0)


def _f057_trend_r2(close, w):
    lp = np.log(close.replace(0, np.nan).abs())
    var_total = lp.rolling(w, min_periods=max(1, w // 2)).var()
    slope = (lp - lp.shift(w)) / float(w)
    explained = (slope * slope) * (w * w - 1) / 12.0
    return 1.0 - (var_total - explained) / var_total.replace(0, np.nan)


def _f057_smoothness_score(close, w):
    ret = close.pct_change()
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    m_abs = ret.abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return m_abs / sd.replace(0, np.nan)


def f057trq_f057_trend_r2_tfitsqrt_5d_base_v076_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 5), 252)) * _z(_f057_trend_fit(closeadj, 5), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_10d_base_v077_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 10), 252)) * _z(_f057_trend_fit(closeadj, 10), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_21d_base_v078_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 21), 252)) * _z(_f057_trend_fit(closeadj, 21), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_42d_base_v079_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 42), 252)) * _z(_f057_trend_fit(closeadj, 42), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_63d_base_v080_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 63), 252)) * _z(_f057_trend_fit(closeadj, 63), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_126d_base_v081_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 126), 252)) * _z(_f057_trend_fit(closeadj, 126), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_189d_base_v082_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 189), 252)) * _z(_f057_trend_fit(closeadj, 189), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_252d_base_v083_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 252), 252)) * _z(_f057_trend_fit(closeadj, 252), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_378d_base_v084_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 378), 252)) * _z(_f057_trend_fit(closeadj, 378), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitsqrt_504d_base_v085_signal(closeadj):
    result = np.sign(_z(_f057_trend_fit(closeadj, 504), 252)) * _z(_f057_trend_fit(closeadj, 504), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_5d_base_v086_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 5), 252)) * _z(_f057_trend_r2(closeadj, 5), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_10d_base_v087_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 10), 252)) * _z(_f057_trend_r2(closeadj, 10), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_21d_base_v088_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 21), 252)) * _z(_f057_trend_r2(closeadj, 21), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_42d_base_v089_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 42), 252)) * _z(_f057_trend_r2(closeadj, 42), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_63d_base_v090_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 63), 252)) * _z(_f057_trend_r2(closeadj, 63), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_126d_base_v091_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 126), 252)) * _z(_f057_trend_r2(closeadj, 126), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_189d_base_v092_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 189), 252)) * _z(_f057_trend_r2(closeadj, 189), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_252d_base_v093_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 252), 252)) * _z(_f057_trend_r2(closeadj, 252), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_378d_base_v094_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 378), 252)) * _z(_f057_trend_r2(closeadj, 378), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndsqrt_504d_base_v095_signal(closeadj):
    result = np.sign(_z(_f057_trend_r2(closeadj, 504), 252)) * _z(_f057_trend_r2(closeadj, 504), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_5d_base_v096_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 5), 252)) * _z(_f057_smoothness_score(closeadj, 5), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_10d_base_v097_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 10), 252)) * _z(_f057_smoothness_score(closeadj, 10), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_21d_base_v098_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 21), 252)) * _z(_f057_smoothness_score(closeadj, 21), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_42d_base_v099_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 42), 252)) * _z(_f057_smoothness_score(closeadj, 42), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_63d_base_v100_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 63), 252)) * _z(_f057_smoothness_score(closeadj, 63), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_126d_base_v101_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 126), 252)) * _z(_f057_smoothness_score(closeadj, 126), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_189d_base_v102_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 189), 252)) * _z(_f057_smoothness_score(closeadj, 189), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_252d_base_v103_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 252), 252)) * _z(_f057_smoothness_score(closeadj, 252), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_378d_base_v104_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 378), 252)) * _z(_f057_smoothness_score(closeadj, 378), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthsqrt_504d_base_v105_signal(closeadj):
    result = np.sign(_z(_f057_smoothness_score(closeadj, 504), 252)) * _z(_f057_smoothness_score(closeadj, 504), 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_5d_base_v106_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 5), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_10d_base_v107_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 10), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_21d_base_v108_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 21), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_42d_base_v109_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 42), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_63d_base_v110_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 63), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_126d_base_v111_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 126), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_189d_base_v112_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 189), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_252d_base_v113_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 252), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_378d_base_v114_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 378), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitclip_504d_base_v115_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 504), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_5d_base_v116_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 5), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_10d_base_v117_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 10), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_21d_base_v118_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 21), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_42d_base_v119_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 42), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_63d_base_v120_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 63), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_126d_base_v121_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 126), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_189d_base_v122_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 189), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_252d_base_v123_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 252), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_378d_base_v124_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 378), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndclip_504d_base_v125_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 504), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_5d_base_v126_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 5), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_10d_base_v127_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 10), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_21d_base_v128_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 21), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_42d_base_v129_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 42), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_63d_base_v130_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 63), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_126d_base_v131_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 126), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_189d_base_v132_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 189), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_252d_base_v133_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 252), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_378d_base_v134_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 378), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_smthclip_504d_base_v135_signal(closeadj):
    result = _z(_f057_smoothness_score(closeadj, 504), 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_5d_base_v136_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 5), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_10d_base_v137_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 10), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_21d_base_v138_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 21), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_42d_base_v139_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 42), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_63d_base_v140_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 63), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_126d_base_v141_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 126), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_189d_base_v142_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 189), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_252d_base_v143_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 252), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_378d_base_v144_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 378), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_tfitemaz_504d_base_v145_signal(closeadj):
    result = _z(_f057_trend_fit(closeadj, 504), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndemaz_5d_base_v146_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 5), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndemaz_10d_base_v147_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 10), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndemaz_21d_base_v148_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 21), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndemaz_42d_base_v149_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 42), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f057trq_f057_trend_r2_trndemaz_63d_base_v150_signal(closeadj):
    result = _z(_f057_trend_r2(closeadj, 63), 252).ewm(span=21, min_periods=10).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f057trq_f057_trend_r2_tfitsqrt_5d_base_v076_signal,
    f057trq_f057_trend_r2_tfitsqrt_10d_base_v077_signal,
    f057trq_f057_trend_r2_tfitsqrt_21d_base_v078_signal,
    f057trq_f057_trend_r2_tfitsqrt_42d_base_v079_signal,
    f057trq_f057_trend_r2_tfitsqrt_63d_base_v080_signal,
    f057trq_f057_trend_r2_tfitsqrt_126d_base_v081_signal,
    f057trq_f057_trend_r2_tfitsqrt_189d_base_v082_signal,
    f057trq_f057_trend_r2_tfitsqrt_252d_base_v083_signal,
    f057trq_f057_trend_r2_tfitsqrt_378d_base_v084_signal,
    f057trq_f057_trend_r2_tfitsqrt_504d_base_v085_signal,
    f057trq_f057_trend_r2_trndsqrt_5d_base_v086_signal,
    f057trq_f057_trend_r2_trndsqrt_10d_base_v087_signal,
    f057trq_f057_trend_r2_trndsqrt_21d_base_v088_signal,
    f057trq_f057_trend_r2_trndsqrt_42d_base_v089_signal,
    f057trq_f057_trend_r2_trndsqrt_63d_base_v090_signal,
    f057trq_f057_trend_r2_trndsqrt_126d_base_v091_signal,
    f057trq_f057_trend_r2_trndsqrt_189d_base_v092_signal,
    f057trq_f057_trend_r2_trndsqrt_252d_base_v093_signal,
    f057trq_f057_trend_r2_trndsqrt_378d_base_v094_signal,
    f057trq_f057_trend_r2_trndsqrt_504d_base_v095_signal,
    f057trq_f057_trend_r2_smthsqrt_5d_base_v096_signal,
    f057trq_f057_trend_r2_smthsqrt_10d_base_v097_signal,
    f057trq_f057_trend_r2_smthsqrt_21d_base_v098_signal,
    f057trq_f057_trend_r2_smthsqrt_42d_base_v099_signal,
    f057trq_f057_trend_r2_smthsqrt_63d_base_v100_signal,
    f057trq_f057_trend_r2_smthsqrt_126d_base_v101_signal,
    f057trq_f057_trend_r2_smthsqrt_189d_base_v102_signal,
    f057trq_f057_trend_r2_smthsqrt_252d_base_v103_signal,
    f057trq_f057_trend_r2_smthsqrt_378d_base_v104_signal,
    f057trq_f057_trend_r2_smthsqrt_504d_base_v105_signal,
    f057trq_f057_trend_r2_tfitclip_5d_base_v106_signal,
    f057trq_f057_trend_r2_tfitclip_10d_base_v107_signal,
    f057trq_f057_trend_r2_tfitclip_21d_base_v108_signal,
    f057trq_f057_trend_r2_tfitclip_42d_base_v109_signal,
    f057trq_f057_trend_r2_tfitclip_63d_base_v110_signal,
    f057trq_f057_trend_r2_tfitclip_126d_base_v111_signal,
    f057trq_f057_trend_r2_tfitclip_189d_base_v112_signal,
    f057trq_f057_trend_r2_tfitclip_252d_base_v113_signal,
    f057trq_f057_trend_r2_tfitclip_378d_base_v114_signal,
    f057trq_f057_trend_r2_tfitclip_504d_base_v115_signal,
    f057trq_f057_trend_r2_trndclip_5d_base_v116_signal,
    f057trq_f057_trend_r2_trndclip_10d_base_v117_signal,
    f057trq_f057_trend_r2_trndclip_21d_base_v118_signal,
    f057trq_f057_trend_r2_trndclip_42d_base_v119_signal,
    f057trq_f057_trend_r2_trndclip_63d_base_v120_signal,
    f057trq_f057_trend_r2_trndclip_126d_base_v121_signal,
    f057trq_f057_trend_r2_trndclip_189d_base_v122_signal,
    f057trq_f057_trend_r2_trndclip_252d_base_v123_signal,
    f057trq_f057_trend_r2_trndclip_378d_base_v124_signal,
    f057trq_f057_trend_r2_trndclip_504d_base_v125_signal,
    f057trq_f057_trend_r2_smthclip_5d_base_v126_signal,
    f057trq_f057_trend_r2_smthclip_10d_base_v127_signal,
    f057trq_f057_trend_r2_smthclip_21d_base_v128_signal,
    f057trq_f057_trend_r2_smthclip_42d_base_v129_signal,
    f057trq_f057_trend_r2_smthclip_63d_base_v130_signal,
    f057trq_f057_trend_r2_smthclip_126d_base_v131_signal,
    f057trq_f057_trend_r2_smthclip_189d_base_v132_signal,
    f057trq_f057_trend_r2_smthclip_252d_base_v133_signal,
    f057trq_f057_trend_r2_smthclip_378d_base_v134_signal,
    f057trq_f057_trend_r2_smthclip_504d_base_v135_signal,
    f057trq_f057_trend_r2_tfitemaz_5d_base_v136_signal,
    f057trq_f057_trend_r2_tfitemaz_10d_base_v137_signal,
    f057trq_f057_trend_r2_tfitemaz_21d_base_v138_signal,
    f057trq_f057_trend_r2_tfitemaz_42d_base_v139_signal,
    f057trq_f057_trend_r2_tfitemaz_63d_base_v140_signal,
    f057trq_f057_trend_r2_tfitemaz_126d_base_v141_signal,
    f057trq_f057_trend_r2_tfitemaz_189d_base_v142_signal,
    f057trq_f057_trend_r2_tfitemaz_252d_base_v143_signal,
    f057trq_f057_trend_r2_tfitemaz_378d_base_v144_signal,
    f057trq_f057_trend_r2_tfitemaz_504d_base_v145_signal,
    f057trq_f057_trend_r2_trndemaz_5d_base_v146_signal,
    f057trq_f057_trend_r2_trndemaz_10d_base_v147_signal,
    f057trq_f057_trend_r2_trndemaz_21d_base_v148_signal,
    f057trq_f057_trend_r2_trndemaz_42d_base_v149_signal,
    f057trq_f057_trend_r2_trndemaz_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F057_TREND_R2_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f057_trend_fit", "_f057_trend_r2", "_f057_smoothness_score",)
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
    print(f"OK f057_trend_r2_base_076_150_claude: {n_features} features pass")
