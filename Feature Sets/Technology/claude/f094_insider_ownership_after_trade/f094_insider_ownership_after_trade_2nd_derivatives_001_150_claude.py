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
def _f094_own_chg(after, before):
    return (after - before) / before.replace(0, np.nan).abs()


# 21d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slope_21d_2d_v001_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slope_63d_2d_v002_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slope_126d_2d_v003_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slope_252d_2d_v004_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slope_504d_2d_v005_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slope_21d_2d_v006_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slope_63d_2d_v007_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slope_126d_2d_v008_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slope_252d_2d_v009_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slope_504d_2d_v010_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slope_21d_2d_v011_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slope_63d_2d_v012_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slope_126d_2d_v013_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slope_252d_2d_v014_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slope_504d_2d_v015_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slope_21d_2d_v016_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slope_63d_2d_v017_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slope_126d_2d_v018_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slope_252d_2d_v019_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slope_504d_2d_v020_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slope_21d_2d_v021_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slope_63d_2d_v022_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slope_126d_2d_v023_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slope_252d_2d_v024_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slope_504d_2d_v025_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slope_21d_2d_v026_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slope_63d_2d_v027_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slope_126d_2d_v028_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slope_252d_2d_v029_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slope_504d_2d_v030_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slope_21d_2d_v031_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slope_63d_2d_v032_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slope_126d_2d_v033_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slope_252d_2d_v034_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slope_504d_2d_v035_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_sm21_sl21_2d_v036_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_sm63_sl21_2d_v037_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_sm63_sl63_2d_v038_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_sm252_sl63_2d_v039_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_sm252_sl126_2d_v040_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_sm21_sl21_2d_v041_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _mean(_f094_own_chg(insider_shares_after, insider_shares_before), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_sm63_sl21_2d_v042_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _mean(_f094_own_chg(insider_shares_after, insider_shares_before), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_sm63_sl63_2d_v043_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _mean(_f094_own_chg(insider_shares_after, insider_shares_before), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_sm252_sl63_2d_v044_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _mean(_f094_own_chg(insider_shares_after, insider_shares_before), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_sm252_sl126_2d_v045_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _mean(_f094_own_chg(insider_shares_after, insider_shares_before), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_sm21_sl21_2d_v046_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = _mean(insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_sm63_sl21_2d_v047_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = _mean(insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_sm63_sl63_2d_v048_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = _mean(insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_sm252_sl63_2d_v049_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = _mean(insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_sm252_sl126_2d_v050_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = _mean(insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_sm21_sl21_2d_v051_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_sm63_sl21_2d_v052_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_sm63_sl63_2d_v053_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_sm252_sl63_2d_v054_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_sm252_sl126_2d_v055_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_sm21_sl21_2d_v056_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_sm63_sl21_2d_v057_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_sm63_sl63_2d_v058_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_sm252_sl63_2d_v059_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_sm252_sl126_2d_v060_signal(insider_shares_after, closeadj):
    base = _mean(insider_shares_after.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_sm21_sl21_2d_v061_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean((insider_transaction_shares < 0.005 * insider_shares_before).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_sm63_sl21_2d_v062_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean((insider_transaction_shares < 0.005 * insider_shares_before).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_sm63_sl63_2d_v063_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean((insider_transaction_shares < 0.005 * insider_shares_before).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_sm252_sl63_2d_v064_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean((insider_transaction_shares < 0.005 * insider_shares_before).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_sm252_sl126_2d_v065_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean((insider_transaction_shares < 0.005 * insider_shares_before).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_sm21_sl21_2d_v066_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_sm63_sl21_2d_v067_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_sm63_sl63_2d_v068_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_sm252_sl63_2d_v069_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_sm252_sl126_2d_v070_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = _mean(((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_pctslope_21d_2d_v071_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_pctslope_63d_2d_v072_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_pctslope_252d_2d_v073_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_pctslope_21d_2d_v074_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_pctslope_63d_2d_v075_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_pctslope_252d_2d_v076_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_pctslope_21d_2d_v077_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_pctslope_63d_2d_v078_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_pctslope_252d_2d_v079_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_pctslope_21d_2d_v080_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_pctslope_63d_2d_v081_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_pctslope_252d_2d_v082_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_pctslope_21d_2d_v083_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_pctslope_63d_2d_v084_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_pctslope_252d_2d_v085_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_pctslope_21d_2d_v086_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_pctslope_63d_2d_v087_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_pctslope_252d_2d_v088_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_pctslope_21d_2d_v089_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_pctslope_63d_2d_v090_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_pctslope_252d_2d_v091_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_sgnslope_21d_2d_v092_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_sgnslope_63d_2d_v093_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_sgnslope_252d_2d_v094_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_sgnslope_21d_2d_v095_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_sgnslope_63d_2d_v096_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_sgnslope_252d_2d_v097_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_sgnslope_21d_2d_v098_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_sgnslope_63d_2d_v099_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_sgnslope_252d_2d_v100_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_sgnslope_21d_2d_v101_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_sgnslope_63d_2d_v102_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_sgnslope_252d_2d_v103_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_sgnslope_21d_2d_v104_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_sgnslope_63d_2d_v105_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_sgnslope_252d_2d_v106_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_sgnslope_21d_2d_v107_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_sgnslope_63d_2d_v108_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_sgnslope_252d_2d_v109_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_sgnslope_21d_2d_v110_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_sgnslope_63d_2d_v111_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_sgnslope_252d_2d_v112_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_logmagslope_21d_2d_v113_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_logmagslope_63d_2d_v114_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_logmagslope_252d_2d_v115_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_logmagslope_21d_2d_v116_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_logmagslope_63d_2d_v117_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_logmagslope_252d_2d_v118_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_logmagslope_21d_2d_v119_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_logmagslope_63d_2d_v120_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_logmagslope_252d_2d_v121_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_logmagslope_21d_2d_v122_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_logmagslope_63d_2d_v123_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_logmagslope_252d_2d_v124_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_logmagslope_21d_2d_v125_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_logmagslope_63d_2d_v126_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_logmagslope_252d_2d_v127_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_logmagslope_21d_2d_v128_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_logmagslope_63d_2d_v129_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_logmagslope_252d_2d_v130_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_logmagslope_21d_2d_v131_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_logmagslope_63d_2d_v132_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_logmagslope_252d_2d_v133_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ownership_after_lvl|
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_logslope_63d_2d_v134_signal(insider_shares_after, closeadj):
    base = np.log((insider_shares_after).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ownership_after_lvl|
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_logslope_252d_2d_v135_signal(insider_shares_after, closeadj):
    base = np.log((insider_shares_after).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ownership_chg|
def f094iow_f094_insider_ownership_after_trade_ownership_chg_logslope_63d_2d_v136_signal(insider_shares_after, insider_shares_before, closeadj):
    base = np.log((_f094_own_chg(insider_shares_after, insider_shares_before)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ownership_chg|
def f094iow_f094_insider_ownership_after_trade_ownership_chg_logslope_252d_2d_v137_signal(insider_shares_after, insider_shares_before, closeadj):
    base = np.log((_f094_own_chg(insider_shares_after, insider_shares_before)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|retention_ratio|
def f094iow_f094_insider_ownership_after_trade_retention_ratio_logslope_63d_2d_v138_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = np.log((insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|retention_ratio|
def f094iow_f094_insider_ownership_after_trade_retention_ratio_logslope_252d_2d_v139_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = np.log((insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|transaction_share_pct|
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_logslope_63d_2d_v140_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = np.log((insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|transaction_share_pct|
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_logslope_252d_2d_v141_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = np.log((insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ownership_yoy_chg|
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_logslope_63d_2d_v142_signal(insider_shares_after, closeadj):
    base = np.log((insider_shares_after.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ownership_yoy_chg|
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_logslope_252d_2d_v143_signal(insider_shares_after, closeadj):
    base = np.log((insider_shares_after.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|token_trade_flag|
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_logslope_63d_2d_v144_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = np.log(((insider_transaction_shares < 0.005 * insider_shares_before).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|token_trade_flag|
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_logslope_252d_2d_v145_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = np.log(((insider_transaction_shares < 0.005 * insider_shares_before).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|meaningful_buy_flag|
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_logslope_63d_2d_v146_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = np.log((((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|meaningful_buy_flag|
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_logslope_252d_2d_v147_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = np.log((((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

