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


# 21d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slope_21d_2d_v001_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slope_63d_2d_v002_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slope_126d_2d_v003_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slope_252d_2d_v004_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_slope_504d_2d_v005_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slope_21d_2d_v006_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slope_63d_2d_v007_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slope_126d_2d_v008_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slope_252d_2d_v009_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_slope_504d_2d_v010_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slope_21d_2d_v011_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slope_63d_2d_v012_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slope_126d_2d_v013_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slope_252d_2d_v014_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_slope_504d_2d_v015_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slope_21d_2d_v016_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slope_63d_2d_v017_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slope_126d_2d_v018_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slope_252d_2d_v019_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_slope_504d_2d_v020_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slope_21d_2d_v021_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slope_63d_2d_v022_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slope_126d_2d_v023_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slope_252d_2d_v024_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_slope_504d_2d_v025_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slope_21d_2d_v026_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slope_63d_2d_v027_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slope_126d_2d_v028_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slope_252d_2d_v029_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_slope_504d_2d_v030_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slope_21d_2d_v031_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slope_63d_2d_v032_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slope_126d_2d_v033_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slope_252d_2d_v034_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_slope_504d_2d_v035_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_sm21_sl21_2d_v036_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_sm63_sl21_2d_v037_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_sm63_sl63_2d_v038_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_sm252_sl63_2d_v039_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_sm252_sl126_2d_v040_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_sm21_sl21_2d_v041_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj).diff(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_sm63_sl21_2d_v042_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj).diff(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_sm63_sl63_2d_v043_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj).diff(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_sm252_sl63_2d_v044_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj).diff(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_sm252_sl126_2d_v045_signal(closeadj, closeunadj):
    base = _mean(_f090_adj_ratio(closeadj, closeunadj).diff(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_sm21_sl21_2d_v046_signal(closeadj, closeunadj):
    base = _mean((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_sm63_sl21_2d_v047_signal(closeadj, closeunadj):
    base = _mean((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_sm63_sl63_2d_v048_signal(closeadj, closeunadj):
    base = _mean((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_sm252_sl63_2d_v049_signal(closeadj, closeunadj):
    base = _mean((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_sm252_sl126_2d_v050_signal(closeadj, closeunadj):
    base = _mean((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_sm21_sl21_2d_v051_signal(closeadj, closeunadj):
    base = _mean(((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_sm63_sl21_2d_v052_signal(closeadj, closeunadj):
    base = _mean(((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_sm63_sl63_2d_v053_signal(closeadj, closeunadj):
    base = _mean(((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_sm252_sl63_2d_v054_signal(closeadj, closeunadj):
    base = _mean(((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_sm252_sl126_2d_v055_signal(closeadj, closeunadj):
    base = _mean(((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_sm21_sl21_2d_v056_signal(high, low, close, closeadj):
    base = _mean((high - low) / close.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_sm63_sl21_2d_v057_signal(high, low, close, closeadj):
    base = _mean((high - low) / close.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_sm63_sl63_2d_v058_signal(high, low, close, closeadj):
    base = _mean((high - low) / close.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_sm252_sl63_2d_v059_signal(high, low, close, closeadj):
    base = _mean((high - low) / close.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_sm252_sl126_2d_v060_signal(high, low, close, closeadj):
    base = _mean((high - low) / close.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_sm21_sl21_2d_v061_signal(closeadj, closeunadj):
    base = _mean((closeadj.pct_change() - closeunadj.pct_change()).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_sm63_sl21_2d_v062_signal(closeadj, closeunadj):
    base = _mean((closeadj.pct_change() - closeunadj.pct_change()).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_sm63_sl63_2d_v063_signal(closeadj, closeunadj):
    base = _mean((closeadj.pct_change() - closeunadj.pct_change()).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_sm252_sl63_2d_v064_signal(closeadj, closeunadj):
    base = _mean((closeadj.pct_change() - closeunadj.pct_change()).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_sm252_sl126_2d_v065_signal(closeadj, closeunadj):
    base = _mean((closeadj.pct_change() - closeunadj.pct_change()).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_sm21_sl21_2d_v066_signal(close, open, closeadj):
    base = _mean((close - open) / open.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_sm63_sl21_2d_v067_signal(close, open, closeadj):
    base = _mean((close - open) / open.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_sm63_sl63_2d_v068_signal(close, open, closeadj):
    base = _mean((close - open) / open.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_sm252_sl63_2d_v069_signal(close, open, closeadj):
    base = _mean((close - open) / open.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_sm252_sl126_2d_v070_signal(close, open, closeadj):
    base = _mean((close - open) / open.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_pctslope_21d_2d_v071_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_pctslope_63d_2d_v072_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_pctslope_252d_2d_v073_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_pctslope_21d_2d_v074_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_pctslope_63d_2d_v075_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_pctslope_252d_2d_v076_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_pctslope_21d_2d_v077_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_pctslope_63d_2d_v078_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_pctslope_252d_2d_v079_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_pctslope_21d_2d_v080_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_pctslope_63d_2d_v081_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_pctslope_252d_2d_v082_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_pctslope_21d_2d_v083_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_pctslope_63d_2d_v084_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_pctslope_252d_2d_v085_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_pctslope_21d_2d_v086_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_pctslope_63d_2d_v087_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_pctslope_252d_2d_v088_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_pctslope_21d_2d_v089_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_pctslope_63d_2d_v090_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_pctslope_252d_2d_v091_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_sgnslope_21d_2d_v092_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_sgnslope_63d_2d_v093_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_sgnslope_252d_2d_v094_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_sgnslope_21d_2d_v095_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_sgnslope_63d_2d_v096_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_sgnslope_252d_2d_v097_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_sgnslope_21d_2d_v098_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_sgnslope_63d_2d_v099_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_sgnslope_252d_2d_v100_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_sgnslope_21d_2d_v101_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_sgnslope_63d_2d_v102_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_sgnslope_252d_2d_v103_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_sgnslope_21d_2d_v104_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_sgnslope_63d_2d_v105_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_sgnslope_252d_2d_v106_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_sgnslope_21d_2d_v107_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_sgnslope_63d_2d_v108_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_sgnslope_252d_2d_v109_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_sgnslope_21d_2d_v110_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_sgnslope_63d_2d_v111_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_sgnslope_252d_2d_v112_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_logmagslope_21d_2d_v113_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_logmagslope_63d_2d_v114_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_logmagslope_252d_2d_v115_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_logmagslope_21d_2d_v116_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_logmagslope_63d_2d_v117_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_logmagslope_252d_2d_v118_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_logmagslope_21d_2d_v119_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_logmagslope_63d_2d_v120_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_logmagslope_252d_2d_v121_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_logmagslope_21d_2d_v122_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_logmagslope_63d_2d_v123_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_logmagslope_252d_2d_v124_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_logmagslope_21d_2d_v125_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_logmagslope_63d_2d_v126_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_logmagslope_252d_2d_v127_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_logmagslope_21d_2d_v128_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_logmagslope_63d_2d_v129_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_logmagslope_252d_2d_v130_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_logmagslope_21d_2d_v131_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_logmagslope_63d_2d_v132_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_logmagslope_252d_2d_v133_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_ratio|
def f090adj_f090_price_adjustment_context_adj_ratio_logslope_63d_2d_v134_signal(closeadj, closeunadj):
    base = np.log((_f090_adj_ratio(closeadj, closeunadj)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_ratio|
def f090adj_f090_price_adjustment_context_adj_ratio_logslope_252d_2d_v135_signal(closeadj, closeunadj):
    base = np.log((_f090_adj_ratio(closeadj, closeunadj)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_ratio_chg|
def f090adj_f090_price_adjustment_context_adj_ratio_chg_logslope_63d_2d_v136_signal(closeadj, closeunadj):
    base = np.log((_f090_adj_ratio(closeadj, closeunadj).diff()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_ratio_chg|
def f090adj_f090_price_adjustment_context_adj_ratio_chg_logslope_252d_2d_v137_signal(closeadj, closeunadj):
    base = np.log((_f090_adj_ratio(closeadj, closeunadj).diff()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_jump_flag|
def f090adj_f090_price_adjustment_context_adj_jump_flag_logslope_63d_2d_v138_signal(closeadj, closeunadj):
    base = np.log(((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_jump_flag|
def f090adj_f090_price_adjustment_context_adj_jump_flag_logslope_252d_2d_v139_signal(closeadj, closeunadj):
    base = np.log(((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_jump_count_252|
def f090adj_f090_price_adjustment_context_adj_jump_count_252_logslope_63d_2d_v140_signal(closeadj, closeunadj):
    base = np.log((((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_jump_count_252|
def f090adj_f090_price_adjustment_context_adj_jump_count_252_logslope_252d_2d_v141_signal(closeadj, closeunadj):
    base = np.log((((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intrabar_range|
def f090adj_f090_price_adjustment_context_intrabar_range_logslope_63d_2d_v142_signal(high, low, close, closeadj):
    base = np.log(((high - low) / close.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intrabar_range|
def f090adj_f090_price_adjustment_context_intrabar_range_logslope_252d_2d_v143_signal(high, low, close, closeadj):
    base = np.log(((high - low) / close.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|adj_return_consistency|
def f090adj_f090_price_adjustment_context_adj_return_consistency_logslope_63d_2d_v144_signal(closeadj, closeunadj):
    base = np.log(((closeadj.pct_change() - closeunadj.pct_change()).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|adj_return_consistency|
def f090adj_f090_price_adjustment_context_adj_return_consistency_logslope_252d_2d_v145_signal(closeadj, closeunadj):
    base = np.log(((closeadj.pct_change() - closeunadj.pct_change()).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|close_vs_open|
def f090adj_f090_price_adjustment_context_close_vs_open_logslope_63d_2d_v146_signal(close, open, closeadj):
    base = np.log(((close - open) / open.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|close_vs_open|
def f090adj_f090_price_adjustment_context_close_vs_open_logslope_252d_2d_v147_signal(close, open, closeadj):
    base = np.log(((close - open) / open.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

