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


# 63d z-score of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_z_63d_base_v076_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_z_126d_base_v077_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_z_252d_base_v078_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_z_504d_base_v079_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_z_63d_base_v080_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_z_126d_base_v081_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_z_252d_base_v082_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_z_504d_base_v083_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_z_63d_base_v084_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_z_126d_base_v085_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_z_252d_base_v086_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_z_504d_base_v087_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_z_63d_base_v088_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_z_126d_base_v089_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_z_252d_base_v090_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_z_504d_base_v091_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_z_63d_base_v092_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_z_126d_base_v093_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_z_252d_base_v094_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_z_504d_base_v095_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_z_63d_base_v096_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_z_126d_base_v097_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_z_252d_base_v098_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_z_504d_base_v099_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_z_63d_base_v100_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_z_126d_base_v101_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_z_252d_base_v102_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_z_504d_base_v103_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_distmax_252d_base_v104_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_distmax_504d_base_v105_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_distmax_252d_base_v106_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_distmax_504d_base_v107_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_distmax_252d_base_v108_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_distmax_504d_base_v109_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_distmax_252d_base_v110_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_distmax_504d_base_v111_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_distmax_252d_base_v112_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_distmax_504d_base_v113_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_distmax_252d_base_v114_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_distmax_504d_base_v115_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_distmax_252d_base_v116_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_distmax_504d_base_v117_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_distmed_126d_base_v118_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_distmed_252d_base_v119_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_distmed_504d_base_v120_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_distmed_126d_base_v121_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_distmed_252d_base_v122_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_distmed_504d_base_v123_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_distmed_126d_base_v124_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_distmed_252d_base_v125_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_distmed_504d_base_v126_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_distmed_126d_base_v127_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_distmed_252d_base_v128_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_distmed_504d_base_v129_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_distmed_126d_base_v130_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_distmed_252d_base_v131_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_distmed_504d_base_v132_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_distmed_126d_base_v133_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_distmed_252d_base_v134_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_distmed_504d_base_v135_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_distmed_126d_base_v136_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_distmed_252d_base_v137_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of close_vs_open
def f090adj_f090_price_adjustment_context_close_vs_open_distmed_504d_base_v138_signal(close, open, closeadj):
    base = (close - open) / open.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_chg_63d_base_v139_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_ratio
def f090adj_f090_price_adjustment_context_adj_ratio_chg_252d_base_v140_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_chg_63d_base_v141_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_ratio_chg
def f090adj_f090_price_adjustment_context_adj_ratio_chg_chg_252d_base_v142_signal(closeadj, closeunadj):
    base = _f090_adj_ratio(closeadj, closeunadj).diff()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_chg_63d_base_v143_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_jump_flag
def f090adj_f090_price_adjustment_context_adj_jump_flag_chg_252d_base_v144_signal(closeadj, closeunadj):
    base = (_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_chg_63d_base_v145_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_jump_count_252
def f090adj_f090_price_adjustment_context_adj_jump_count_252_chg_252d_base_v146_signal(closeadj, closeunadj):
    base = ((_f090_adj_ratio(closeadj, closeunadj).diff().abs() > 0.05).astype(float)).rolling(252, min_periods=63).sum()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_chg_63d_base_v147_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intrabar_range
def f090adj_f090_price_adjustment_context_intrabar_range_chg_252d_base_v148_signal(high, low, close, closeadj):
    base = (high - low) / close.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_chg_63d_base_v149_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in adj_return_consistency
def f090adj_f090_price_adjustment_context_adj_return_consistency_chg_252d_base_v150_signal(closeadj, closeunadj):
    base = (closeadj.pct_change() - closeunadj.pct_change()).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

