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


# 21d acceleration of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_accel_21d_3d_v001_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_accel_63d_3d_v002_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_accel_126d_3d_v003_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_accel_252d_3d_v004_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_accel_21d_3d_v005_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_accel_63d_3d_v006_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_accel_126d_3d_v007_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_accel_252d_3d_v008_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_accel_21d_3d_v009_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_accel_63d_3d_v010_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_accel_126d_3d_v011_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_accel_252d_3d_v012_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_accel_21d_3d_v013_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_accel_63d_3d_v014_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_accel_126d_3d_v015_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_accel_252d_3d_v016_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_accel_21d_3d_v017_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_accel_63d_3d_v018_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_accel_126d_3d_v019_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_accel_252d_3d_v020_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_accel_21d_3d_v021_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_accel_63d_3d_v022_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_accel_126d_3d_v023_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_accel_252d_3d_v024_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_accel_21d_3d_v025_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_accel_63d_3d_v026_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_accel_126d_3d_v027_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_accel_252d_3d_v028_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_accel_21d_3d_v029_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_accel_63d_3d_v030_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_accel_126d_3d_v031_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_accel_252d_3d_v032_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_accel_21d_3d_v033_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_accel_63d_3d_v034_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_accel_126d_3d_v035_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_accel_252d_3d_v036_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_accel_21d_3d_v037_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_accel_63d_3d_v038_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_accel_126d_3d_v039_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_accel_252d_3d_v040_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_accel_21d_3d_v041_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_accel_63d_3d_v042_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_accel_126d_3d_v043_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_accel_252d_3d_v044_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_accel_21d_3d_v045_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_accel_63d_3d_v046_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_accel_126d_3d_v047_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_accel_252d_3d_v048_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_accel_21d_3d_v049_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_accel_63d_3d_v050_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_accel_126d_3d_v051_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_accel_252d_3d_v052_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_accel_21d_3d_v053_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_accel_63d_3d_v054_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_accel_126d_3d_v055_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_accel_252d_3d_v056_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_accel_21d_3d_v057_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_accel_63d_3d_v058_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_accel_126d_3d_v059_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_accel_252d_3d_v060_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_accel_21d_3d_v061_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_accel_63d_3d_v062_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_accel_126d_3d_v063_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_accel_252d_3d_v064_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_accel_21d_3d_v065_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_accel_63d_3d_v066_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_accel_126d_3d_v067_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_accel_252d_3d_v068_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_accel_21d_3d_v069_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_accel_63d_3d_v070_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_accel_126d_3d_v071_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_accel_252d_3d_v072_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_accel_21d_3d_v073_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_accel_63d_3d_v074_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_accel_126d_3d_v075_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_accel_252d_3d_v076_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_accel_21d_3d_v077_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_accel_63d_3d_v078_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_accel_126d_3d_v079_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_accel_252d_3d_v080_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slopez_21d_z126_3d_v081_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slopez_63d_z252_3d_v082_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slopez_126d_z252_3d_v083_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_slopez_252d_z504_3d_v084_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slopez_21d_z126_3d_v085_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slopez_63d_z252_3d_v086_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slopez_126d_z252_3d_v087_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_slopez_252d_z504_3d_v088_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slopez_21d_z126_3d_v089_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slopez_63d_z252_3d_v090_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slopez_126d_z252_3d_v091_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_slopez_252d_z504_3d_v092_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slopez_21d_z126_3d_v093_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slopez_63d_z252_3d_v094_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slopez_126d_z252_3d_v095_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_slopez_252d_z504_3d_v096_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slopez_21d_z126_3d_v097_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slopez_63d_z252_3d_v098_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slopez_126d_z252_3d_v099_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_slopez_252d_z504_3d_v100_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slopez_21d_z126_3d_v101_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slopez_63d_z252_3d_v102_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slopez_126d_z252_3d_v103_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_slopez_252d_z504_3d_v104_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slopez_21d_z126_3d_v105_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slopez_63d_z252_3d_v106_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slopez_126d_z252_3d_v107_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_slopez_252d_z504_3d_v108_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slopez_21d_z126_3d_v109_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slopez_63d_z252_3d_v110_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slopez_126d_z252_3d_v111_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_slopez_252d_z504_3d_v112_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slopez_21d_z126_3d_v113_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slopez_63d_z252_3d_v114_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slopez_126d_z252_3d_v115_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_slopez_252d_z504_3d_v116_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slopez_21d_z126_3d_v117_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slopez_63d_z252_3d_v118_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slopez_126d_z252_3d_v119_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_slopez_252d_z504_3d_v120_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slopez_21d_z126_3d_v121_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slopez_63d_z252_3d_v122_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slopez_126d_z252_3d_v123_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_slopez_252d_z504_3d_v124_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slopez_21d_z126_3d_v125_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slopez_63d_z252_3d_v126_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slopez_126d_z252_3d_v127_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_slopez_252d_z504_3d_v128_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slopez_21d_z126_3d_v129_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slopez_63d_z252_3d_v130_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slopez_126d_z252_3d_v131_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_slopez_252d_z504_3d_v132_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slopez_21d_z126_3d_v133_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slopez_63d_z252_3d_v134_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slopez_126d_z252_3d_v135_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_slopez_252d_z504_3d_v136_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slopez_21d_z126_3d_v137_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slopez_63d_z252_3d_v138_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slopez_126d_z252_3d_v139_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_slopez_252d_z504_3d_v140_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slopez_21d_z126_3d_v141_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slopez_63d_z252_3d_v142_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slopez_126d_z252_3d_v143_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_slopez_252d_z504_3d_v144_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slopez_21d_z126_3d_v145_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slopez_63d_z252_3d_v146_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slopez_126d_z252_3d_v147_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_slopez_252d_z504_3d_v148_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slopez_21d_z126_3d_v149_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slopez_63d_z252_3d_v150_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slopez_126d_z252_3d_v151_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_slopez_252d_z504_3d_v152_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slopez_21d_z126_3d_v153_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slopez_63d_z252_3d_v154_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slopez_126d_z252_3d_v155_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_slopez_252d_z504_3d_v156_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slopez_21d_z126_3d_v157_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slopez_63d_z252_3d_v158_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slopez_126d_z252_3d_v159_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_slopez_252d_z504_3d_v160_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_jerk_21d_3d_v161_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_jerk_63d_3d_v162_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_jerk_126d_3d_v163_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_jerk_21d_3d_v164_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_jerk_63d_3d_v165_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_jerk_126d_3d_v166_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_jerk_21d_3d_v167_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_jerk_63d_3d_v168_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_jerk_126d_3d_v169_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_jerk_21d_3d_v170_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_jerk_63d_3d_v171_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_jerk_126d_3d_v172_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_jerk_21d_3d_v173_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_jerk_63d_3d_v174_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_jerk_126d_3d_v175_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_jerk_21d_3d_v176_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_jerk_63d_3d_v177_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_jerk_126d_3d_v178_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_jerk_21d_3d_v179_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_jerk_63d_3d_v180_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_jerk_126d_3d_v181_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_jerk_21d_3d_v182_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_jerk_63d_3d_v183_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_jerk_126d_3d_v184_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_jerk_21d_3d_v185_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_jerk_63d_3d_v186_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_jerk_126d_3d_v187_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_jerk_21d_3d_v188_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_jerk_63d_3d_v189_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_jerk_126d_3d_v190_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_jerk_21d_3d_v191_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_jerk_63d_3d_v192_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_jerk_126d_3d_v193_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_jerk_21d_3d_v194_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_jerk_63d_3d_v195_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_jerk_126d_3d_v196_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_jerk_21d_3d_v197_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_jerk_63d_3d_v198_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_jerk_126d_3d_v199_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_jerk_21d_3d_v200_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

