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
def _f094_own_chg(after, before):
    return (after - before) / before.replace(0, np.nan).abs()


# 21d mean of ownership_after_lvl scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_mean_21d_base_v001_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ownership_after_lvl scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_mean_63d_base_v002_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ownership_after_lvl scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_mean_126d_base_v003_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ownership_after_lvl scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_mean_252d_base_v004_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ownership_after_lvl scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_mean_504d_base_v005_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ownership_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_chg_mean_21d_base_v006_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ownership_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_chg_mean_63d_base_v007_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ownership_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_chg_mean_126d_base_v008_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ownership_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_chg_mean_252d_base_v009_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ownership_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_chg_mean_504d_base_v010_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of retention_ratio scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_retention_ratio_mean_21d_base_v011_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of retention_ratio scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_retention_ratio_mean_63d_base_v012_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of retention_ratio scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_retention_ratio_mean_126d_base_v013_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of retention_ratio scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_retention_ratio_mean_252d_base_v014_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of retention_ratio scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_retention_ratio_mean_504d_base_v015_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of transaction_share_pct scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_mean_21d_base_v016_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of transaction_share_pct scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_mean_63d_base_v017_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of transaction_share_pct scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_mean_126d_base_v018_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of transaction_share_pct scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_mean_252d_base_v019_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of transaction_share_pct scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_mean_504d_base_v020_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ownership_yoy_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_mean_21d_base_v021_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ownership_yoy_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_mean_63d_base_v022_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ownership_yoy_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_mean_126d_base_v023_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ownership_yoy_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_mean_252d_base_v024_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ownership_yoy_chg scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_mean_504d_base_v025_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of token_trade_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_mean_21d_base_v026_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of token_trade_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_mean_63d_base_v027_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of token_trade_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_mean_126d_base_v028_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of token_trade_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_mean_252d_base_v029_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of token_trade_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_mean_504d_base_v030_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of meaningful_buy_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_mean_21d_base_v031_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of meaningful_buy_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_mean_63d_base_v032_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of meaningful_buy_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_mean_126d_base_v033_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of meaningful_buy_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_mean_252d_base_v034_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of meaningful_buy_flag scaled by closeadj
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_mean_504d_base_v035_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_median_63d_base_v036_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_median_252d_base_v037_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_median_504d_base_v038_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_median_63d_base_v039_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_median_252d_base_v040_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_median_504d_base_v041_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_median_63d_base_v042_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_median_252d_base_v043_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_median_504d_base_v044_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_median_63d_base_v045_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_median_252d_base_v046_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_median_504d_base_v047_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_median_63d_base_v048_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_median_252d_base_v049_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_median_504d_base_v050_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_median_63d_base_v051_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_median_252d_base_v052_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_median_504d_base_v053_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_median_63d_base_v054_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_median_252d_base_v055_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_median_504d_base_v056_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_rmax_252d_base_v057_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_rmax_504d_base_v058_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_rmax_252d_base_v059_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_rmax_504d_base_v060_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_rmax_252d_base_v061_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_rmax_504d_base_v062_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_rmax_252d_base_v063_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_rmax_504d_base_v064_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_rmax_252d_base_v065_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_rmax_504d_base_v066_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_rmax_252d_base_v067_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_rmax_504d_base_v068_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_rmax_252d_base_v069_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_rmax_504d_base_v070_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_rmin_252d_base_v071_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_rmin_504d_base_v072_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_rmin_252d_base_v073_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_rmin_504d_base_v074_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_rmin_252d_base_v075_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

