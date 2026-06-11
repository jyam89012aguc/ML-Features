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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f25_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f25_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f25_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d mean of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_mean_21d_base_v001_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_mean_63d_base_v002_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_mean_126d_base_v003_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_mean_252d_base_v004_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_mean_504d_base_v005_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_z_21d_base_v006_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_z_63d_base_v007_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_z_126d_base_v008_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_z_252d_base_v009_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_z_504d_base_v010_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rz_21d_base_v011_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (ratio - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rz_63d_base_v012_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (ratio - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rz_126d_base_v013_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (ratio - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rz_252d_base_v014_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (ratio - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rz_504d_base_v015_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (ratio - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_max_21d_base_v016_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_max_63d_base_v017_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_max_126d_base_v018_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_max_252d_base_v019_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_max_504d_base_v020_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_min_21d_base_v021_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_min_63d_base_v022_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_min_126d_base_v023_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_min_252d_base_v024_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min capex accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_min_504d_base_v025_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rng_21d_base_v026_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 21) - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rng_63d_base_v027_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 63) - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rng_126d_base_v028_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 126) - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rng_252d_base_v029_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 252) - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range accel YoY
def f25ca_f25_semi_capex_acceleration_cayoyac_rng_504d_base_v030_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=252)
    ratio = g.diff(periods=252)
    result = _max(ratio, 504) - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_mean_21d_base_v031_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_mean_63d_base_v032_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_mean_126d_base_v033_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_mean_252d_base_v034_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_mean_504d_base_v035_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_z_21d_base_v036_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_z_63d_base_v037_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_z_126d_base_v038_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_z_252d_base_v039_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_z_504d_base_v040_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_std_21d_base_v041_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _std(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_std_63d_base_v042_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _std(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_std_126d_base_v043_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _std(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_std_252d_base_v044_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _std(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_std_504d_base_v045_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = _std(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_skew_21d_base_v046_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_skew_63d_base_v047_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_skew_126d_base_v048_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_skew_252d_base_v049_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_skew_504d_base_v050_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurt of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_kurt_21d_base_v051_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurt of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_kurt_63d_base_v052_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurt of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_kurt_126d_base_v053_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurt of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_kurt_252d_base_v054_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurt of capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_kurt_504d_base_v055_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pos-in-range capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_pos_21d_base_v056_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    lo = _min(ratio, 21)
    hi = _max(ratio, 21)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pos-in-range capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_pos_63d_base_v057_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pos-in-range capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_pos_126d_base_v058_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    lo = _min(ratio, 126)
    hi = _max(ratio, 126)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pos-in-range capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_pos_252d_base_v059_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pos-in-range capex 2nd-diff
def f25ca_f25_semi_capex_acceleration_cadiff2_pos_504d_base_v060_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.diff(periods=63).diff(periods=63)
    lo = _min(ratio, 504)
    hi = _max(ratio, 504)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z accel QoQ + YoY
def f25ca_f25_semi_capex_acceleration_camix_compos_21d_base_v061_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    gq = cx.pct_change(periods=63).diff(periods=63)
    gy = cx.pct_change(periods=252).diff(periods=252)
    result = _z(gq, 21) + _z(gy, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z accel QoQ + YoY
def f25ca_f25_semi_capex_acceleration_camix_compos_63d_base_v062_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    gq = cx.pct_change(periods=63).diff(periods=63)
    gy = cx.pct_change(periods=252).diff(periods=252)
    result = _z(gq, 63) + _z(gy, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z accel QoQ + YoY
def f25ca_f25_semi_capex_acceleration_camix_compos_126d_base_v063_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    gq = cx.pct_change(periods=63).diff(periods=63)
    gy = cx.pct_change(periods=252).diff(periods=252)
    result = _z(gq, 126) + _z(gy, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z accel QoQ + YoY
def f25ca_f25_semi_capex_acceleration_camix_compos_252d_base_v064_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    gq = cx.pct_change(periods=63).diff(periods=63)
    gy = cx.pct_change(periods=252).diff(periods=252)
    result = _z(gq, 252) + _z(gy, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z accel QoQ + YoY
def f25ca_f25_semi_capex_acceleration_camix_compos_504d_base_v065_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    gq = cx.pct_change(periods=63).diff(periods=63)
    gy = cx.pct_change(periods=252).diff(periods=252)
    result = _z(gq, 504) + _z(gy, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quartile rank accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_quart_21d_base_v066_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quartile rank accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_quart_63d_base_v067_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d quartile rank accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_quart_126d_base_v068_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quartile rank accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_quart_252d_base_v069_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quartile rank accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_quart_504d_base_v070_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d deviation from median accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_devmed_21d_base_v071_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deviation from median accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_devmed_63d_base_v072_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 126d deviation from median accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_devmed_126d_base_v073_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deviation from median accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_devmed_252d_base_v074_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deviation from median accel QoQ
def f25ca_f25_semi_capex_acceleration_caaccel_devmed_504d_base_v075_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    g = cx.pct_change(periods=63)
    ratio = g.diff(periods=63)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)
