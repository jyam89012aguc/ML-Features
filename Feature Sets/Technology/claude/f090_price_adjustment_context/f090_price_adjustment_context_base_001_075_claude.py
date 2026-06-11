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
def _f090_adj_ratio(closeadj, closeunadj):
    return closeadj / closeunadj.replace(0, np.nan).abs()


# 21d mean of adj_ratio scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_mean_21d_base_v001_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_ratio scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_mean_63d_base_v002_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_ratio scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_mean_126d_base_v003_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_ratio scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_mean_252d_base_v004_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_ratio scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_mean_504d_base_v005_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of adj_ratio_chg scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_chg_mean_21d_base_v006_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_ratio_chg scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_chg_mean_63d_base_v007_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_ratio_chg scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_chg_mean_126d_base_v008_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_ratio_chg scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_chg_mean_252d_base_v009_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_ratio_chg scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_ratio_chg_mean_504d_base_v010_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of adj_jump_flag scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_flag_mean_21d_base_v011_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_jump_flag scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_flag_mean_63d_base_v012_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_jump_flag scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_flag_mean_126d_base_v013_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_jump_flag scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_flag_mean_252d_base_v014_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_jump_flag scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_flag_mean_504d_base_v015_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of adj_jump_count_252 scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_count_252_mean_21d_base_v016_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_jump_count_252 scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_count_252_mean_63d_base_v017_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_jump_count_252 scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_count_252_mean_126d_base_v018_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_jump_count_252 scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_count_252_mean_252d_base_v019_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_jump_count_252 scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_jump_count_252_mean_504d_base_v020_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of intrabar_range scaled by closeadj
def f090adj_f090_price_adjustment_context_intrabar_range_mean_21d_base_v021_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intrabar_range scaled by closeadj
def f090adj_f090_price_adjustment_context_intrabar_range_mean_63d_base_v022_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intrabar_range scaled by closeadj
def f090adj_f090_price_adjustment_context_intrabar_range_mean_126d_base_v023_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intrabar_range scaled by closeadj
def f090adj_f090_price_adjustment_context_intrabar_range_mean_252d_base_v024_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intrabar_range scaled by closeadj
def f090adj_f090_price_adjustment_context_intrabar_range_mean_504d_base_v025_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of adj_return_consistency scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_return_consistency_mean_21d_base_v026_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of adj_return_consistency scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_return_consistency_mean_63d_base_v027_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of adj_return_consistency scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_return_consistency_mean_126d_base_v028_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of adj_return_consistency scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_return_consistency_mean_252d_base_v029_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of adj_return_consistency scaled by closeadj
def f090adj_f090_price_adjustment_context_adj_return_consistency_mean_504d_base_v030_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of close_vs_open scaled by closeadj
def f090adj_f090_price_adjustment_context_close_vs_open_mean_21d_base_v031_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of close_vs_open scaled by closeadj
def f090adj_f090_price_adjustment_context_close_vs_open_mean_63d_base_v032_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of close_vs_open scaled by closeadj
def f090adj_f090_price_adjustment_context_close_vs_open_mean_126d_base_v033_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of close_vs_open scaled by closeadj
def f090adj_f090_price_adjustment_context_close_vs_open_mean_252d_base_v034_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of close_vs_open scaled by closeadj
def f090adj_f090_price_adjustment_context_close_vs_open_mean_504d_base_v035_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_median_63d_base_v036_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_median_252d_base_v037_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_median_504d_base_v038_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_median_63d_base_v039_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_median_252d_base_v040_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_median_504d_base_v041_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_median_63d_base_v042_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_median_252d_base_v043_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_median_504d_base_v044_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_median_63d_base_v045_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_median_252d_base_v046_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_median_504d_base_v047_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_median_63d_base_v048_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_median_252d_base_v049_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_median_504d_base_v050_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_median_63d_base_v051_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_median_252d_base_v052_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_median_504d_base_v053_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_median_63d_base_v054_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_median_252d_base_v055_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_median_504d_base_v056_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_rmax_252d_base_v057_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_rmax_504d_base_v058_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_rmax_252d_base_v059_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_rmax_504d_base_v060_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_rmax_252d_base_v061_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_rmax_504d_base_v062_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_rmax_252d_base_v063_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_rmax_504d_base_v064_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_rmax_252d_base_v065_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_rmax_504d_base_v066_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_rmax_252d_base_v067_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_rmax_504d_base_v068_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_rmax_252d_base_v069_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_rmax_504d_base_v070_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_rmin_252d_base_v071_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_rmin_504d_base_v072_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_rmin_252d_base_v073_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_rmin_504d_base_v074_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_rmin_252d_base_v075_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

