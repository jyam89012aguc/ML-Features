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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f097_specshare(specialist_value, inst_total_value):
    return specialist_value / inst_total_value.replace(0, np.nan).abs()


# 21d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slope_21d_2d_v001_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slope_63d_2d_v002_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slope_126d_2d_v003_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slope_252d_2d_v004_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slope_504d_2d_v005_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slope_21d_2d_v006_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slope_63d_2d_v007_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slope_126d_2d_v008_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slope_252d_2d_v009_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slope_504d_2d_v010_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slope_21d_2d_v011_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slope_63d_2d_v012_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slope_126d_2d_v013_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slope_252d_2d_v014_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slope_504d_2d_v015_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slope_21d_2d_v016_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slope_63d_2d_v017_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slope_126d_2d_v018_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slope_252d_2d_v019_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slope_504d_2d_v020_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slope_21d_2d_v021_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slope_63d_2d_v022_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slope_126d_2d_v023_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slope_252d_2d_v024_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slope_504d_2d_v025_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slope_21d_2d_v026_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slope_63d_2d_v027_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slope_126d_2d_v028_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slope_252d_2d_v029_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slope_504d_2d_v030_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slope_21d_2d_v031_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slope_63d_2d_v032_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slope_126d_2d_v033_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slope_252d_2d_v034_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slope_504d_2d_v035_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slope_21d_2d_v036_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slope_63d_2d_v037_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slope_126d_2d_v038_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slope_252d_2d_v039_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slope_504d_2d_v040_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slope_21d_2d_v041_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slope_63d_2d_v042_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slope_126d_2d_v043_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slope_252d_2d_v044_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slope_504d_2d_v045_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slope_21d_2d_v046_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slope_63d_2d_v047_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slope_126d_2d_v048_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slope_252d_2d_v049_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slope_504d_2d_v050_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slope_21d_2d_v051_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slope_63d_2d_v052_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slope_126d_2d_v053_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slope_252d_2d_v054_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slope_504d_2d_v055_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slope_21d_2d_v056_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slope_63d_2d_v057_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slope_126d_2d_v058_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slope_252d_2d_v059_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slope_504d_2d_v060_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slope_21d_2d_v061_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slope_63d_2d_v062_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slope_126d_2d_v063_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slope_252d_2d_v064_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slope_504d_2d_v065_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slope_21d_2d_v066_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slope_63d_2d_v067_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slope_126d_2d_v068_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slope_252d_2d_v069_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slope_504d_2d_v070_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slope_21d_2d_v071_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slope_63d_2d_v072_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slope_126d_2d_v073_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slope_252d_2d_v074_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slope_504d_2d_v075_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slope_21d_2d_v076_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slope_63d_2d_v077_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slope_126d_2d_v078_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slope_252d_2d_v079_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slope_504d_2d_v080_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slope_21d_2d_v081_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slope_63d_2d_v082_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slope_126d_2d_v083_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slope_252d_2d_v084_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slope_504d_2d_v085_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slope_21d_2d_v086_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slope_63d_2d_v087_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slope_126d_2d_v088_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slope_252d_2d_v089_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slope_504d_2d_v090_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slope_21d_2d_v091_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slope_63d_2d_v092_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slope_126d_2d_v093_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slope_252d_2d_v094_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slope_504d_2d_v095_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slope_21d_2d_v096_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slope_63d_2d_v097_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slope_126d_2d_v098_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slope_252d_2d_v099_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slope_504d_2d_v100_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_sm21_sl21_2d_v101_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _mean(_f097_specshare(specialist_fund_value, inst_total_value), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_sm63_sl21_2d_v102_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _mean(_f097_specshare(specialist_fund_value, inst_total_value), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_sm63_sl63_2d_v103_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _mean(_f097_specshare(specialist_fund_value, inst_total_value), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_sm252_sl63_2d_v104_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _mean(_f097_specshare(specialist_fund_value, inst_total_value), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_sm252_sl126_2d_v105_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _mean(_f097_specshare(specialist_fund_value, inst_total_value), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_sm21_sl21_2d_v106_signal(quality_long_value, inst_total_value, closeadj):
    base = _mean(quality_long_value / inst_total_value.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_sm63_sl21_2d_v107_signal(quality_long_value, inst_total_value, closeadj):
    base = _mean(quality_long_value / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_sm63_sl63_2d_v108_signal(quality_long_value, inst_total_value, closeadj):
    base = _mean(quality_long_value / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_sm252_sl63_2d_v109_signal(quality_long_value, inst_total_value, closeadj):
    base = _mean(quality_long_value / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_sm252_sl126_2d_v110_signal(quality_long_value, inst_total_value, closeadj):
    base = _mean(quality_long_value / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_sm21_sl21_2d_v111_signal(hedge_fund_value, inst_total_value, closeadj):
    base = _mean(hedge_fund_value / inst_total_value.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_sm63_sl21_2d_v112_signal(hedge_fund_value, inst_total_value, closeadj):
    base = _mean(hedge_fund_value / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_sm63_sl63_2d_v113_signal(hedge_fund_value, inst_total_value, closeadj):
    base = _mean(hedge_fund_value / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_sm252_sl63_2d_v114_signal(hedge_fund_value, inst_total_value, closeadj):
    base = _mean(hedge_fund_value / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_sm252_sl126_2d_v115_signal(hedge_fund_value, inst_total_value, closeadj):
    base = _mean(hedge_fund_value / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_sm21_sl21_2d_v116_signal(etf_value, inst_total_value, closeadj):
    base = _mean(etf_value / inst_total_value.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_sm63_sl21_2d_v117_signal(etf_value, inst_total_value, closeadj):
    base = _mean(etf_value / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_sm63_sl63_2d_v118_signal(etf_value, inst_total_value, closeadj):
    base = _mean(etf_value / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_sm252_sl63_2d_v119_signal(etf_value, inst_total_value, closeadj):
    base = _mean(etf_value / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_sm252_sl126_2d_v120_signal(etf_value, inst_total_value, closeadj):
    base = _mean(etf_value / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_sm21_sl21_2d_v121_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_sm63_sl21_2d_v122_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_sm63_sl63_2d_v123_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_sm252_sl63_2d_v124_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_sm252_sl126_2d_v125_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_sm21_sl21_2d_v126_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_sm63_sl21_2d_v127_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_sm63_sl63_2d_v128_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_sm252_sl63_2d_v129_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_sm252_sl126_2d_v130_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_sm21_sl21_2d_v131_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = _mean(etf_value - (quality_long_value + hedge_fund_value), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_sm63_sl21_2d_v132_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = _mean(etf_value - (quality_long_value + hedge_fund_value), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_sm63_sl63_2d_v133_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = _mean(etf_value - (quality_long_value + hedge_fund_value), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_sm252_sl63_2d_v134_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = _mean(etf_value - (quality_long_value + hedge_fund_value), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_sm252_sl126_2d_v135_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = _mean(etf_value - (quality_long_value + hedge_fund_value), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_sm21_sl21_2d_v136_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_sm63_sl21_2d_v137_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_sm63_sl63_2d_v138_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_sm252_sl63_2d_v139_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_sm252_sl126_2d_v140_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_sm21_sl21_2d_v141_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_sm63_sl21_2d_v142_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_sm63_sl63_2d_v143_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_sm252_sl63_2d_v144_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_sm252_sl126_2d_v145_signal(specialist_fund_value, closeadj):
    base = _mean(specialist_fund_value.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_sm21_sl21_2d_v146_signal(quality_long_value, closeadj):
    base = _mean(quality_long_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_sm63_sl21_2d_v147_signal(quality_long_value, closeadj):
    base = _mean(quality_long_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_sm63_sl63_2d_v148_signal(quality_long_value, closeadj):
    base = _mean(quality_long_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_sm252_sl63_2d_v149_signal(quality_long_value, closeadj):
    base = _mean(quality_long_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_sm252_sl126_2d_v150_signal(quality_long_value, closeadj):
    base = _mean(quality_long_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_sm21_sl21_2d_v151_signal(hedge_fund_value, closeadj):
    base = _mean(hedge_fund_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_sm63_sl21_2d_v152_signal(hedge_fund_value, closeadj):
    base = _mean(hedge_fund_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_sm63_sl63_2d_v153_signal(hedge_fund_value, closeadj):
    base = _mean(hedge_fund_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_sm252_sl63_2d_v154_signal(hedge_fund_value, closeadj):
    base = _mean(hedge_fund_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_sm252_sl126_2d_v155_signal(hedge_fund_value, closeadj):
    base = _mean(hedge_fund_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_sm21_sl21_2d_v156_signal(etf_value, closeadj):
    base = _mean(etf_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_sm63_sl21_2d_v157_signal(etf_value, closeadj):
    base = _mean(etf_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_sm63_sl63_2d_v158_signal(etf_value, closeadj):
    base = _mean(etf_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_sm252_sl63_2d_v159_signal(etf_value, closeadj):
    base = _mean(etf_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_sm252_sl126_2d_v160_signal(etf_value, closeadj):
    base = _mean(etf_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_sm21_sl21_2d_v161_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = _mean(((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_sm63_sl21_2d_v162_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = _mean(((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_sm63_sl63_2d_v163_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = _mean(((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_sm252_sl63_2d_v164_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = _mean(((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_sm252_sl126_2d_v165_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = _mean(((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_sm21_sl21_2d_v166_signal(etf_value, inst_total_value, closeadj):
    base = _mean((etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_sm63_sl21_2d_v167_signal(etf_value, inst_total_value, closeadj):
    base = _mean((etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_sm63_sl63_2d_v168_signal(etf_value, inst_total_value, closeadj):
    base = _mean((etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_sm252_sl63_2d_v169_signal(etf_value, inst_total_value, closeadj):
    base = _mean((etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_sm252_sl126_2d_v170_signal(etf_value, inst_total_value, closeadj):
    base = _mean((etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_sm21_sl21_2d_v171_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_sm63_sl21_2d_v172_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_sm63_sl63_2d_v173_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_sm252_sl63_2d_v174_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_sm252_sl126_2d_v175_signal(named_specialist_holder_count, closeadj):
    base = _mean(named_specialist_holder_count.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_sm21_sl21_2d_v176_signal(named_specialist_holder_count, closeadj):
    base = _mean((named_specialist_holder_count.diff(periods=63) > 2).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_sm63_sl21_2d_v177_signal(named_specialist_holder_count, closeadj):
    base = _mean((named_specialist_holder_count.diff(periods=63) > 2).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_sm63_sl63_2d_v178_signal(named_specialist_holder_count, closeadj):
    base = _mean((named_specialist_holder_count.diff(periods=63) > 2).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_sm252_sl63_2d_v179_signal(named_specialist_holder_count, closeadj):
    base = _mean((named_specialist_holder_count.diff(periods=63) > 2).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_sm252_sl126_2d_v180_signal(named_specialist_holder_count, closeadj):
    base = _mean((named_specialist_holder_count.diff(periods=63) > 2).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_sm21_sl21_2d_v181_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_sm63_sl21_2d_v182_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_sm63_sl63_2d_v183_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_sm252_sl63_2d_v184_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_sm252_sl126_2d_v185_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_sm21_sl21_2d_v186_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_sm63_sl21_2d_v187_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_sm63_sl63_2d_v188_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_sm252_sl63_2d_v189_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_sm252_sl126_2d_v190_signal(growth_specialist_value, closeadj):
    base = _mean(growth_specialist_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_sm21_sl21_2d_v191_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = _mean(top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_sm63_sl21_2d_v192_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = _mean(top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_sm63_sl63_2d_v193_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = _mean(top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_sm252_sl63_2d_v194_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = _mean(top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_sm252_sl126_2d_v195_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = _mean(top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_sm21_sl21_2d_v196_signal(top5_specialist_value, closeadj):
    base = _mean(top5_specialist_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_sm63_sl21_2d_v197_signal(top5_specialist_value, closeadj):
    base = _mean(top5_specialist_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_sm63_sl63_2d_v198_signal(top5_specialist_value, closeadj):
    base = _mean(top5_specialist_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_sm252_sl63_2d_v199_signal(top5_specialist_value, closeadj):
    base = _mean(top5_specialist_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_sm252_sl126_2d_v200_signal(top5_specialist_value, closeadj):
    base = _mean(top5_specialist_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

