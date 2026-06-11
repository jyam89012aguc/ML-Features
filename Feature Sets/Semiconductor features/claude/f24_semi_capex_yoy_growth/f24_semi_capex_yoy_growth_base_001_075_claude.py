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
def _f24_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f24_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f24_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d mean of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_21d_base_v001_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_63d_base_v002_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_126d_base_v003_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_252d_base_v004_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_mean_504d_base_v005_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z_21d_base_v006_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z_63d_base_v007_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z_126d_base_v008_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z_252d_base_v009_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of capex YoY growth
def f24cy_f24_semi_capex_yoy_growth_cyyoy_z_504d_base_v010_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z capex YoY (med/MAD)
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rz_21d_base_v011_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (ratio - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z capex YoY (med/MAD)
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rz_63d_base_v012_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (ratio - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z capex YoY (med/MAD)
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rz_126d_base_v013_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (ratio - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z capex YoY (med/MAD)
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rz_252d_base_v014_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (ratio - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z capex YoY (med/MAD)
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rz_504d_base_v015_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (ratio - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max_21d_base_v016_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max_63d_base_v017_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max_126d_base_v018_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max_252d_base_v019_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_max_504d_base_v020_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min_21d_base_v021_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min_63d_base_v022_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min_126d_base_v023_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min_252d_base_v024_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_min_504d_base_v025_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng_21d_base_v026_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 21) - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng_63d_base_v027_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 63) - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng_126d_base_v028_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 126) - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng_252d_base_v029_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 252) - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_rng_504d_base_v030_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _max(ratio, 504) - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pos-in-range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos_21d_base_v031_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 21)
    hi = _max(ratio, 21)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pos-in-range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos_63d_base_v032_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pos-in-range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos_126d_base_v033_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 126)
    hi = _max(ratio, 126)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pos-in-range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos_252d_base_v034_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pos-in-range capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_pos_504d_base_v035_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    lo = _min(ratio, 504)
    hi = _max(ratio, 504)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown capex YoY from peak
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd_21d_base_v036_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown capex YoY from peak
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd_63d_base_v037_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown capex YoY from peak
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd_126d_base_v038_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown capex YoY from peak
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd_252d_base_v039_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown capex YoY from peak
def f24cy_f24_semi_capex_yoy_growth_cyyoy_dd_504d_base_v040_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up capex YoY from trough
def f24cy_f24_semi_capex_yoy_growth_cyyoy_runup_21d_base_v041_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up capex YoY from trough
def f24cy_f24_semi_capex_yoy_growth_cyyoy_runup_63d_base_v042_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up capex YoY from trough
def f24cy_f24_semi_capex_yoy_growth_cyyoy_runup_126d_base_v043_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up capex YoY from trough
def f24cy_f24_semi_capex_yoy_growth_cyyoy_runup_252d_base_v044_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up capex YoY from trough
def f24cy_f24_semi_capex_yoy_growth_cyyoy_runup_504d_base_v045_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std_21d_base_v046_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _std(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std_63d_base_v047_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _std(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std_126d_base_v048_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _std(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std_252d_base_v049_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _std(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_std_504d_base_v050_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = _std(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew_21d_base_v051_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew_63d_base_v052_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew_126d_base_v053_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew_252d_base_v054_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_skew_504d_base_v055_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurt capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt_21d_base_v056_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurt capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt_63d_base_v057_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurt capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt_126d_base_v058_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurt capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt_252d_base_v059_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurt capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_kurt_504d_base_v060_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit rate positive YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hitpos_21d_base_v061_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = (ratio > 0).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit rate positive YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hitpos_63d_base_v062_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = (ratio > 0).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit rate positive YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hitpos_126d_base_v063_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = (ratio > 0).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit rate positive YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hitpos_252d_base_v064_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = (ratio > 0).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit rate positive YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_hitpos_504d_base_v065_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = (ratio > 0).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cum capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_signcum_21d_base_v066_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = pd.Series(np.sign(ratio), index=ratio.index).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cum capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_signcum_63d_base_v067_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = pd.Series(np.sign(ratio), index=ratio.index).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cum capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_signcum_126d_base_v068_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = pd.Series(np.sign(ratio), index=ratio.index).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cum capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_signcum_252d_base_v069_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = pd.Series(np.sign(ratio), index=ratio.index).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cum capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_signcum_504d_base_v070_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = pd.Series(np.sign(ratio), index=ratio.index).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema(5)-ema(21) capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_21d_base_v071_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema(5)-ema(63) capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_63d_base_v072_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema(5)-ema(126) capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_126d_base_v073_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema(5)-ema(252) capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_252d_base_v074_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema(5)-ema(504) capex YoY
def f24cy_f24_semi_capex_yoy_growth_cyyoy_ema_504d_base_v075_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    ratio = cx.pct_change(periods=252)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
