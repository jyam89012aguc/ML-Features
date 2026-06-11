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
def _f090_adj_ratio(closeadj, closeunadj):
    return closeadj / closeunadj.replace(0, np.nan).abs()


# 21d acceleration of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_accel_21d_3d_v001_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_accel_63d_3d_v002_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_accel_126d_3d_v003_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_accel_252d_3d_v004_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_accel_21d_3d_v005_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_accel_63d_3d_v006_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_accel_126d_3d_v007_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_accel_252d_3d_v008_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_accel_21d_3d_v009_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_accel_63d_3d_v010_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_accel_126d_3d_v011_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_accel_252d_3d_v012_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_accel_21d_3d_v013_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_accel_63d_3d_v014_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_accel_126d_3d_v015_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_accel_252d_3d_v016_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_accel_21d_3d_v017_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_accel_63d_3d_v018_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_accel_126d_3d_v019_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_accel_252d_3d_v020_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_accel_21d_3d_v021_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_accel_63d_3d_v022_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_accel_126d_3d_v023_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_accel_252d_3d_v024_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_accel_21d_3d_v025_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_accel_63d_3d_v026_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_accel_126d_3d_v027_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_accel_252d_3d_v028_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slopez_21d_z126_3d_v029_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slopez_63d_z252_3d_v030_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slopez_126d_z252_3d_v031_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slopez_252d_z504_3d_v032_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slopez_21d_z126_3d_v033_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slopez_63d_z252_3d_v034_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slopez_126d_z252_3d_v035_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slopez_252d_z504_3d_v036_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slopez_21d_z126_3d_v037_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slopez_63d_z252_3d_v038_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slopez_126d_z252_3d_v039_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slopez_252d_z504_3d_v040_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slopez_21d_z126_3d_v041_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slopez_63d_z252_3d_v042_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slopez_126d_z252_3d_v043_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slopez_252d_z504_3d_v044_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slopez_21d_z126_3d_v045_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slopez_63d_z252_3d_v046_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slopez_126d_z252_3d_v047_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slopez_252d_z504_3d_v048_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slopez_21d_z126_3d_v049_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slopez_63d_z252_3d_v050_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slopez_126d_z252_3d_v051_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slopez_252d_z504_3d_v052_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slopez_21d_z126_3d_v053_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slopez_63d_z252_3d_v054_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slopez_126d_z252_3d_v055_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slopez_252d_z504_3d_v056_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_jerk_21d_3d_v057_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_jerk_63d_3d_v058_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_jerk_126d_3d_v059_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_jerk_21d_3d_v060_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_jerk_63d_3d_v061_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_jerk_126d_3d_v062_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_jerk_21d_3d_v063_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_jerk_63d_3d_v064_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_jerk_126d_3d_v065_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_jerk_21d_3d_v066_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_jerk_63d_3d_v067_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_jerk_126d_3d_v068_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_jerk_21d_3d_v069_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_jerk_63d_3d_v070_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_jerk_126d_3d_v071_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_jerk_21d_3d_v072_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_jerk_63d_3d_v073_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_jerk_126d_3d_v074_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_jerk_21d_3d_v075_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_jerk_63d_3d_v076_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_jerk_126d_3d_v077_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_ratio smoothed over 252d
def f090adj_f090_price_adjustment_context_adj_ratio_smoothaccel_63d_sm252_3d_v078_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_ratio smoothed over 504d
def f090adj_f090_price_adjustment_context_adj_ratio_smoothaccel_252d_sm504_3d_v079_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_ratio_chg smoothed over 252d
def f090adj_f090_price_adjustment_context_adj_ratio_chg_smoothaccel_63d_sm252_3d_v080_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_ratio_chg smoothed over 504d
def f090adj_f090_price_adjustment_context_adj_ratio_chg_smoothaccel_252d_sm504_3d_v081_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_jump_flag smoothed over 252d
def f090adj_f090_price_adjustment_context_adj_jump_flag_smoothaccel_63d_sm252_3d_v082_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_jump_flag smoothed over 504d
def f090adj_f090_price_adjustment_context_adj_jump_flag_smoothaccel_252d_sm504_3d_v083_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_jump_count_252 smoothed over 252d
def f090adj_f090_price_adjustment_context_adj_jump_count_252_smoothaccel_63d_sm252_3d_v084_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_jump_count_252 smoothed over 504d
def f090adj_f090_price_adjustment_context_adj_jump_count_252_smoothaccel_252d_sm504_3d_v085_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intrabar_range smoothed over 252d
def f090adj_f090_price_adjustment_context_intrabar_range_smoothaccel_63d_sm252_3d_v086_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intrabar_range smoothed over 504d
def f090adj_f090_price_adjustment_context_intrabar_range_smoothaccel_252d_sm504_3d_v087_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of adj_return_consistency smoothed over 252d
def f090adj_f090_price_adjustment_context_adj_return_consistency_smoothaccel_63d_sm252_3d_v088_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of adj_return_consistency smoothed over 504d
def f090adj_f090_price_adjustment_context_adj_return_consistency_smoothaccel_252d_sm504_3d_v089_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of close_vs_open smoothed over 252d
def f090adj_f090_price_adjustment_context_close_vs_open_smoothaccel_63d_sm252_3d_v090_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of close_vs_open smoothed over 504d
def f090adj_f090_price_adjustment_context_close_vs_open_smoothaccel_252d_sm504_3d_v091_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_accelz_21d_z252_3d_v092_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_accelz_63d_z504_3d_v093_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_accelz_21d_z252_3d_v094_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_accelz_63d_z504_3d_v095_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_accelz_21d_z252_3d_v096_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_accelz_63d_z504_3d_v097_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_accelz_21d_z252_3d_v098_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_accelz_63d_z504_3d_v099_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_accelz_21d_z252_3d_v100_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_accelz_63d_z504_3d_v101_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_accelz_21d_z252_3d_v102_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_accelz_63d_z504_3d_v103_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_accelz_21d_z252_3d_v104_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_accelz_63d_z504_3d_v105_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_ratio (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_ratio_signflip_63d_3d_v106_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_ratio (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_ratio_signflip_252d_3d_v107_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_ratio_chg (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_ratio_chg_signflip_63d_3d_v108_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_ratio_chg (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_ratio_chg_signflip_252d_3d_v109_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_jump_flag (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_jump_flag_signflip_63d_3d_v110_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_jump_flag (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_jump_flag_signflip_252d_3d_v111_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_jump_count_252 (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_jump_count_252_signflip_63d_3d_v112_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_jump_count_252 (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_jump_count_252_signflip_252d_3d_v113_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intrabar_range (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_intrabar_range_signflip_63d_3d_v114_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intrabar_range (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_intrabar_range_signflip_252d_3d_v115_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in adj_return_consistency (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_return_consistency_signflip_63d_3d_v116_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in adj_return_consistency (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_adj_return_consistency_signflip_252d_3d_v117_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in close_vs_open (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_close_vs_open_signflip_63d_3d_v118_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in close_vs_open (raw count, no price scaling)
def f090adj_f090_price_adjustment_context_close_vs_open_signflip_252d_3d_v119_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_ratio normalized by 252d range
def f090adj_f090_price_adjustment_context_adj_ratio_rngaccel_63d_r252_3d_v120_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_ratio normalized by 504d range
def f090adj_f090_price_adjustment_context_adj_ratio_rngaccel_252d_r504_3d_v121_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_ratio_chg normalized by 252d range
def f090adj_f090_price_adjustment_context_adj_ratio_chg_rngaccel_63d_r252_3d_v122_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_ratio_chg normalized by 504d range
def f090adj_f090_price_adjustment_context_adj_ratio_chg_rngaccel_252d_r504_3d_v123_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_jump_flag normalized by 252d range
def f090adj_f090_price_adjustment_context_adj_jump_flag_rngaccel_63d_r252_3d_v124_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_jump_flag normalized by 504d range
def f090adj_f090_price_adjustment_context_adj_jump_flag_rngaccel_252d_r504_3d_v125_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_jump_count_252 normalized by 252d range
def f090adj_f090_price_adjustment_context_adj_jump_count_252_rngaccel_63d_r252_3d_v126_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_jump_count_252 normalized by 504d range
def f090adj_f090_price_adjustment_context_adj_jump_count_252_rngaccel_252d_r504_3d_v127_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intrabar_range normalized by 252d range
def f090adj_f090_price_adjustment_context_intrabar_range_rngaccel_63d_r252_3d_v128_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intrabar_range normalized by 504d range
def f090adj_f090_price_adjustment_context_intrabar_range_rngaccel_252d_r504_3d_v129_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of adj_return_consistency normalized by 252d range
def f090adj_f090_price_adjustment_context_adj_return_consistency_rngaccel_63d_r252_3d_v130_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of adj_return_consistency normalized by 504d range
def f090adj_f090_price_adjustment_context_adj_return_consistency_rngaccel_252d_r504_3d_v131_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of close_vs_open normalized by 252d range
def f090adj_f090_price_adjustment_context_close_vs_open_rngaccel_63d_r252_3d_v132_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of close_vs_open normalized by 504d range
def f090adj_f090_price_adjustment_context_close_vs_open_rngaccel_252d_r504_3d_v133_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_cumslope_21d_3d_v134_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_cumslope_63d_3d_v135_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_cumslope_252d_3d_v136_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_cumslope_21d_3d_v137_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_cumslope_63d_3d_v138_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_cumslope_252d_3d_v139_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_cumslope_21d_3d_v140_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_cumslope_63d_3d_v141_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_cumslope_252d_3d_v142_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_cumslope_21d_3d_v143_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_cumslope_63d_3d_v144_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_cumslope_252d_3d_v145_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_cumslope_21d_3d_v146_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_cumslope_63d_3d_v147_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_cumslope_252d_3d_v148_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_cumslope_21d_3d_v149_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_cumslope_63d_3d_v150_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

