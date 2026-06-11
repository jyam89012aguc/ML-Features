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


# 21d acceleration of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_accel_21d_3d_v001_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_accel_63d_3d_v002_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_accel_126d_3d_v003_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_accel_252d_3d_v004_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_accel_21d_3d_v005_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_accel_63d_3d_v006_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_accel_126d_3d_v007_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_accel_252d_3d_v008_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_accel_21d_3d_v009_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_accel_63d_3d_v010_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_accel_126d_3d_v011_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_accel_252d_3d_v012_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_accel_21d_3d_v013_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_accel_63d_3d_v014_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_accel_126d_3d_v015_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_accel_252d_3d_v016_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_accel_21d_3d_v017_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_accel_63d_3d_v018_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_accel_126d_3d_v019_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_accel_252d_3d_v020_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_accel_21d_3d_v021_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_accel_63d_3d_v022_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_accel_126d_3d_v023_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_accel_252d_3d_v024_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_accel_21d_3d_v025_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_accel_63d_3d_v026_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_accel_126d_3d_v027_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_accel_252d_3d_v028_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slopez_21d_z126_3d_v029_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slopez_63d_z252_3d_v030_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slopez_126d_z252_3d_v031_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_slopez_252d_z504_3d_v032_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slopez_21d_z126_3d_v033_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slopez_63d_z252_3d_v034_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slopez_126d_z252_3d_v035_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_slopez_252d_z504_3d_v036_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slopez_21d_z126_3d_v037_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slopez_63d_z252_3d_v038_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slopez_126d_z252_3d_v039_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_slopez_252d_z504_3d_v040_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slopez_21d_z126_3d_v041_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slopez_63d_z252_3d_v042_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slopez_126d_z252_3d_v043_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_slopez_252d_z504_3d_v044_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slopez_21d_z126_3d_v045_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slopez_63d_z252_3d_v046_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slopez_126d_z252_3d_v047_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_slopez_252d_z504_3d_v048_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slopez_21d_z126_3d_v049_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slopez_63d_z252_3d_v050_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slopez_126d_z252_3d_v051_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_slopez_252d_z504_3d_v052_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slopez_21d_z126_3d_v053_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slopez_63d_z252_3d_v054_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slopez_126d_z252_3d_v055_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_slopez_252d_z504_3d_v056_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_jerk_21d_3d_v057_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_jerk_63d_3d_v058_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_jerk_126d_3d_v059_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_jerk_21d_3d_v060_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_jerk_63d_3d_v061_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_jerk_126d_3d_v062_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_jerk_21d_3d_v063_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_jerk_63d_3d_v064_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_jerk_126d_3d_v065_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_jerk_21d_3d_v066_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_jerk_63d_3d_v067_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_jerk_126d_3d_v068_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_jerk_21d_3d_v069_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_jerk_63d_3d_v070_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_jerk_126d_3d_v071_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_jerk_21d_3d_v072_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_jerk_63d_3d_v073_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_jerk_126d_3d_v074_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_jerk_21d_3d_v075_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_jerk_63d_3d_v076_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_jerk_126d_3d_v077_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ownership_after_lvl smoothed over 252d
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_smoothaccel_63d_sm252_3d_v078_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ownership_after_lvl smoothed over 504d
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_smoothaccel_252d_sm504_3d_v079_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ownership_chg smoothed over 252d
def f094iow_f094_insider_ownership_after_trade_ownership_chg_smoothaccel_63d_sm252_3d_v080_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ownership_chg smoothed over 504d
def f094iow_f094_insider_ownership_after_trade_ownership_chg_smoothaccel_252d_sm504_3d_v081_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of retention_ratio smoothed over 252d
def f094iow_f094_insider_ownership_after_trade_retention_ratio_smoothaccel_63d_sm252_3d_v082_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of retention_ratio smoothed over 504d
def f094iow_f094_insider_ownership_after_trade_retention_ratio_smoothaccel_252d_sm504_3d_v083_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of transaction_share_pct smoothed over 252d
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_smoothaccel_63d_sm252_3d_v084_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of transaction_share_pct smoothed over 504d
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_smoothaccel_252d_sm504_3d_v085_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ownership_yoy_chg smoothed over 252d
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_smoothaccel_63d_sm252_3d_v086_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ownership_yoy_chg smoothed over 504d
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_smoothaccel_252d_sm504_3d_v087_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of token_trade_flag smoothed over 252d
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_smoothaccel_63d_sm252_3d_v088_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of token_trade_flag smoothed over 504d
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_smoothaccel_252d_sm504_3d_v089_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of meaningful_buy_flag smoothed over 252d
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_smoothaccel_63d_sm252_3d_v090_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of meaningful_buy_flag smoothed over 504d
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_smoothaccel_252d_sm504_3d_v091_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_accelz_21d_z252_3d_v092_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_accelz_63d_z504_3d_v093_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_accelz_21d_z252_3d_v094_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_accelz_63d_z504_3d_v095_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_accelz_21d_z252_3d_v096_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_accelz_63d_z504_3d_v097_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_accelz_21d_z252_3d_v098_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_accelz_63d_z504_3d_v099_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_accelz_21d_z252_3d_v100_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_accelz_63d_z504_3d_v101_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_accelz_21d_z252_3d_v102_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_accelz_63d_z504_3d_v103_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_accelz_21d_z252_3d_v104_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_accelz_63d_z504_3d_v105_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ownership_after_lvl (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_signflip_63d_3d_v106_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ownership_after_lvl (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_signflip_252d_3d_v107_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ownership_chg (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_ownership_chg_signflip_63d_3d_v108_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ownership_chg (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_ownership_chg_signflip_252d_3d_v109_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in retention_ratio (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_retention_ratio_signflip_63d_3d_v110_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in retention_ratio (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_retention_ratio_signflip_252d_3d_v111_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in transaction_share_pct (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_signflip_63d_3d_v112_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in transaction_share_pct (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_signflip_252d_3d_v113_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ownership_yoy_chg (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_signflip_63d_3d_v114_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ownership_yoy_chg (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_signflip_252d_3d_v115_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in token_trade_flag (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_signflip_63d_3d_v116_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in token_trade_flag (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_signflip_252d_3d_v117_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in meaningful_buy_flag (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_signflip_63d_3d_v118_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in meaningful_buy_flag (raw count, no price scaling)
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_signflip_252d_3d_v119_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ownership_after_lvl normalized by 252d range
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_rngaccel_63d_r252_3d_v120_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ownership_after_lvl normalized by 504d range
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_rngaccel_252d_r504_3d_v121_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ownership_chg normalized by 252d range
def f094iow_f094_insider_ownership_after_trade_ownership_chg_rngaccel_63d_r252_3d_v122_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ownership_chg normalized by 504d range
def f094iow_f094_insider_ownership_after_trade_ownership_chg_rngaccel_252d_r504_3d_v123_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retention_ratio normalized by 252d range
def f094iow_f094_insider_ownership_after_trade_retention_ratio_rngaccel_63d_r252_3d_v124_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retention_ratio normalized by 504d range
def f094iow_f094_insider_ownership_after_trade_retention_ratio_rngaccel_252d_r504_3d_v125_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of transaction_share_pct normalized by 252d range
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_rngaccel_63d_r252_3d_v126_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of transaction_share_pct normalized by 504d range
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_rngaccel_252d_r504_3d_v127_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ownership_yoy_chg normalized by 252d range
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_rngaccel_63d_r252_3d_v128_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ownership_yoy_chg normalized by 504d range
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_rngaccel_252d_r504_3d_v129_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of token_trade_flag normalized by 252d range
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_rngaccel_63d_r252_3d_v130_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of token_trade_flag normalized by 504d range
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_rngaccel_252d_r504_3d_v131_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of meaningful_buy_flag normalized by 252d range
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_rngaccel_63d_r252_3d_v132_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of meaningful_buy_flag normalized by 504d range
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_rngaccel_252d_r504_3d_v133_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_cumslope_21d_3d_v134_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_cumslope_63d_3d_v135_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_cumslope_252d_3d_v136_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_cumslope_21d_3d_v137_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_cumslope_63d_3d_v138_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_cumslope_252d_3d_v139_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_cumslope_21d_3d_v140_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_cumslope_63d_3d_v141_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_cumslope_252d_3d_v142_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_cumslope_21d_3d_v143_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_cumslope_63d_3d_v144_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_cumslope_252d_3d_v145_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_cumslope_21d_3d_v146_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_cumslope_63d_3d_v147_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_cumslope_252d_3d_v148_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_cumslope_21d_3d_v149_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_cumslope_63d_3d_v150_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

