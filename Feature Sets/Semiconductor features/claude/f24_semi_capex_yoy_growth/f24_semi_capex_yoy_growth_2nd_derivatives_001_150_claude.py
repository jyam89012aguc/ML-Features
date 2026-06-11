import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f24_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f24_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f24_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 5d slope of capex YoY level
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_yoy_slope_v001_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex YoY level
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_yoy_slope_v002_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex YoY level
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_yoy_slope_v003_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of capex YoY level
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_yoy_slope_v004_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of capex YoY level
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_yoy_slope_v005_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z21_21d_slope_v006_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z21_21d_slope_v007_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z21_21d_slope_v008_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z21_21d_slope_v009_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z21_21d_slope_v010_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z63_63d_slope_v011_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z63_63d_slope_v012_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z63_63d_slope_v013_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z63_63d_slope_v014_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z63_63d_slope_v015_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z126_126d_slope_v016_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z126_126d_slope_v017_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z126_126d_slope_v018_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z126_126d_slope_v019_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z126_126d_slope_v020_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z252_252d_slope_v021_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z252_252d_slope_v022_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z252_252d_slope_v023_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z252_252d_slope_v024_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z252_252d_slope_v025_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of capex QoQ level
def f24cy_f24_semi_capex_yoy_growth_cyqoq_mean_qoq_slope_v026_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex QoQ level
def f24cy_f24_semi_capex_yoy_growth_cyqoq_mean_qoq_slope_v027_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex QoQ level
def f24cy_f24_semi_capex_yoy_growth_cyqoq_mean_qoq_slope_v028_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of capex QoQ level
def f24cy_f24_semi_capex_yoy_growth_cyqoq_mean_qoq_slope_v029_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of capex QoQ level
def f24cy_f24_semi_capex_yoy_growth_cyqoq_mean_qoq_slope_v030_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = cx.pct_change(periods=63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z63_63d_slope_v031_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z63_63d_slope_v032_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z63_63d_slope_v033_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z63_63d_slope_v034_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z63_63d_slope_v035_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z252_252d_slope_v036_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z252_252d_slope_v037_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z252_252d_slope_v038_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z252_252d_slope_v039_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z QoQ
def f24cy_f24_semi_capex_yoy_growth_cyqoq_z252_252d_slope_v040_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=63)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_mean_log_slope_v041_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_mean_log_slope_v042_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_mean_log_slope_v043_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_mean_log_slope_v044_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_mean_log_slope_v045_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z63_63d_slope_v046_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z63_63d_slope_v047_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z63_63d_slope_v048_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z63_63d_slope_v049_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z63_63d_slope_v050_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z252_252d_slope_v051_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z252_252d_slope_v052_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z252_252d_slope_v053_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z252_252d_slope_v054_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z log YoY
def f24cy_f24_semi_capex_yoy_growth_cylog_z252_252d_slope_v055_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / cx.shift(252).abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max63_63d_slope_v056_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max63_63d_slope_v057_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max63_63d_slope_v058_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max63_63d_slope_v059_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max63_63d_slope_v060_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max252_252d_slope_v061_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max252_252d_slope_v062_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max252_252d_slope_v063_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max252_252d_slope_v064_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d max YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max252_252d_slope_v065_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min63_63d_slope_v066_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min63_63d_slope_v067_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min63_63d_slope_v068_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min63_63d_slope_v069_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min63_63d_slope_v070_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min252_252d_slope_v071_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min252_252d_slope_v072_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min252_252d_slope_v073_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min252_252d_slope_v074_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d min YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min252_252d_slope_v075_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _min(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng63_63d_slope_v076_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng63_63d_slope_v077_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng63_63d_slope_v078_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng63_63d_slope_v079_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng63_63d_slope_v080_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng252_252d_slope_v081_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng252_252d_slope_v082_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng252_252d_slope_v083_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng252_252d_slope_v084_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng252_252d_slope_v085_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos63_63d_slope_v086_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos63_63d_slope_v087_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos63_63d_slope_v088_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos63_63d_slope_v089_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos63_63d_slope_v090_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos252_252d_slope_v091_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos252_252d_slope_v092_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos252_252d_slope_v093_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos252_252d_slope_v094_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pos-in-range YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos252_252d_slope_v095_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd63_63d_slope_v096_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd63_63d_slope_v097_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd63_63d_slope_v098_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd63_63d_slope_v099_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd63_63d_slope_v100_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd252_252d_slope_v101_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd252_252d_slope_v102_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd252_252d_slope_v103_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd252_252d_slope_v104_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d YoY drawdown
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd252_252d_slope_v105_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio - _max(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std63_63d_slope_v106_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std63_63d_slope_v107_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std63_63d_slope_v108_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std63_63d_slope_v109_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std63_63d_slope_v110_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std252_252d_slope_v111_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std252_252d_slope_v112_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std252_252d_slope_v113_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std252_252d_slope_v114_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d std YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std252_252d_slope_v115_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = _std(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew63_63d_slope_v116_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew63_63d_slope_v117_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew63_63d_slope_v118_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew63_63d_slope_v119_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew63_63d_slope_v120_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d kurt YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt63_63d_slope_v121_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d kurt YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt63_63d_slope_v122_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d kurt YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt63_63d_slope_v123_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d kurt YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt63_63d_slope_v124_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d kurt YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt63_63d_slope_v125_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit63_63d_slope_v126_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit63_63d_slope_v127_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit63_63d_slope_v128_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit63_63d_slope_v129_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit63_63d_slope_v130_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit252_252d_slope_v131_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit252_252d_slope_v132_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit252_252d_slope_v133_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit252_252d_slope_v134_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d hit-pos YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hit252_252d_slope_v135_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = (ratio > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(5)-ema(63) YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_5v63_slope_v136_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(5)-ema(63) YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_5v63_slope_v137_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(5)-ema(63) YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_5v63_slope_v138_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(5)-ema(63) YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_5v63_slope_v139_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(5)-ema(63) YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_5v63_slope_v140_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d rank YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rank63_63d_slope_v141_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rank YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rank63_63d_slope_v142_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d rank YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rank63_63d_slope_v143_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d rank YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rank63_63d_slope_v144_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d rank YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rank63_63d_slope_v145_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of mix z(63) YoY+QoQ
def f24cy_f24_semi_capex_yoy_growth_cymix_z63_63d_slope_v146_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ry = cx.pct_change(periods=252)
    rq = cx.pct_change(periods=63)
    base = _z(ry, 63) + _z(rq, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mix z(63) YoY+QoQ
def f24cy_f24_semi_capex_yoy_growth_cymix_z63_63d_slope_v147_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ry = cx.pct_change(periods=252)
    rq = cx.pct_change(periods=63)
    base = _z(ry, 63) + _z(rq, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mix z(63) YoY+QoQ
def f24cy_f24_semi_capex_yoy_growth_cymix_z63_63d_slope_v148_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ry = cx.pct_change(periods=252)
    rq = cx.pct_change(periods=63)
    base = _z(ry, 63) + _z(rq, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mix z(63) YoY+QoQ
def f24cy_f24_semi_capex_yoy_growth_cymix_z63_63d_slope_v149_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ry = cx.pct_change(periods=252)
    rq = cx.pct_change(periods=63)
    base = _z(ry, 63) + _z(rq, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of mix z(63) YoY+QoQ
def f24cy_f24_semi_capex_yoy_growth_cymix_z63_63d_slope_v150_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ry = cx.pct_change(periods=252)
    rq = cx.pct_change(periods=63)
    base = _z(ry, 63) + _z(rq, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
