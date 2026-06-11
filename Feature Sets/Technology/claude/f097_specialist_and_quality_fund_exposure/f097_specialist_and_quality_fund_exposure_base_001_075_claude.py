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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f097_specshare(specialist_value, inst_total_value):
    return specialist_value / inst_total_value.replace(0, np.nan).abs()


# 21d mean of specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_mean_21d_base_v001_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_mean_63d_base_v002_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_mean_126d_base_v003_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_mean_252d_base_v004_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_mean_504d_base_v005_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of quality_long_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_mean_21d_base_v006_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of quality_long_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_mean_63d_base_v007_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of quality_long_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_mean_126d_base_v008_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of quality_long_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_mean_252d_base_v009_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of quality_long_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_mean_504d_base_v010_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of hedge_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_mean_21d_base_v011_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of hedge_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_mean_63d_base_v012_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of hedge_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_mean_126d_base_v013_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of hedge_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_mean_252d_base_v014_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of hedge_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_mean_504d_base_v015_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of etf_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_mean_21d_base_v016_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of etf_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_mean_63d_base_v017_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of etf_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_mean_126d_base_v018_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of etf_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_mean_252d_base_v019_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of etf_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_mean_504d_base_v020_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of specialist_value_yoy scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_mean_21d_base_v021_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of specialist_value_yoy scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_mean_63d_base_v022_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of specialist_value_yoy scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_mean_126d_base_v023_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of specialist_value_yoy scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_mean_252d_base_v024_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of specialist_value_yoy scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_mean_504d_base_v025_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of named_specialist_count scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_mean_21d_base_v026_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of named_specialist_count scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_mean_63d_base_v027_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of named_specialist_count scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_mean_126d_base_v028_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of named_specialist_count scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_mean_252d_base_v029_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of named_specialist_count scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_mean_504d_base_v030_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of etf_minus_active scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_mean_21d_base_v031_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of etf_minus_active scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_mean_63d_base_v032_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of etf_minus_active scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_mean_126d_base_v033_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of etf_minus_active scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_mean_252d_base_v034_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of etf_minus_active scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_mean_504d_base_v035_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_mean_21d_base_v036_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_mean_63d_base_v037_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_mean_126d_base_v038_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_mean_252d_base_v039_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_mean_504d_base_v040_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of specialist_qoq_pct scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_mean_21d_base_v041_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of specialist_qoq_pct scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_mean_63d_base_v042_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of specialist_qoq_pct scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_mean_126d_base_v043_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of specialist_qoq_pct scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_mean_252d_base_v044_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of specialist_qoq_pct scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_mean_504d_base_v045_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of quality_long_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_mean_21d_base_v046_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of quality_long_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_mean_63d_base_v047_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of quality_long_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_mean_126d_base_v048_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of quality_long_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_mean_252d_base_v049_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of quality_long_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_mean_504d_base_v050_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of hedge_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_mean_21d_base_v051_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of hedge_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_mean_63d_base_v052_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of hedge_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_mean_126d_base_v053_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of hedge_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_mean_252d_base_v054_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of hedge_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_mean_504d_base_v055_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of etf_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_mean_21d_base_v056_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of etf_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_mean_63d_base_v057_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of etf_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_mean_126d_base_v058_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of etf_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_mean_252d_base_v059_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of etf_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_mean_504d_base_v060_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of active_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_mean_21d_base_v061_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of active_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_mean_63d_base_v062_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of active_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_mean_126d_base_v063_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of active_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_mean_252d_base_v064_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of active_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_mean_504d_base_v065_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of etf_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_mean_21d_base_v066_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of etf_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_mean_63d_base_v067_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of etf_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_mean_126d_base_v068_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of etf_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_mean_252d_base_v069_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of etf_share_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_mean_504d_base_v070_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of named_specialist_qoq_chg scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_mean_21d_base_v071_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of named_specialist_qoq_chg scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_mean_63d_base_v072_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of named_specialist_qoq_chg scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_mean_126d_base_v073_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of named_specialist_qoq_chg scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_mean_252d_base_v074_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of named_specialist_qoq_chg scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_mean_504d_base_v075_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of named_specialist_entering_flag scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_mean_21d_base_v076_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of named_specialist_entering_flag scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_mean_63d_base_v077_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of named_specialist_entering_flag scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_mean_126d_base_v078_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of named_specialist_entering_flag scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_mean_252d_base_v079_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of named_specialist_entering_flag scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_mean_504d_base_v080_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of growth_specialist_value scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_mean_21d_base_v081_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of growth_specialist_value scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_mean_63d_base_v082_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of growth_specialist_value scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_mean_126d_base_v083_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of growth_specialist_value scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_mean_252d_base_v084_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of growth_specialist_value scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_mean_504d_base_v085_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of growth_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_mean_21d_base_v086_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of growth_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_mean_63d_base_v087_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of growth_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_mean_126d_base_v088_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of growth_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_mean_252d_base_v089_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of growth_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_mean_504d_base_v090_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of top5_specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_mean_21d_base_v091_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top5_specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_mean_63d_base_v092_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top5_specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_mean_126d_base_v093_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top5_specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_mean_252d_base_v094_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top5_specialist_share scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_mean_504d_base_v095_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of top5_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_mean_21d_base_v096_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top5_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_mean_63d_base_v097_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top5_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_mean_126d_base_v098_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top5_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_mean_252d_base_v099_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top5_specialist_qoq_delta scaled by closeadj
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_mean_504d_base_v100_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

