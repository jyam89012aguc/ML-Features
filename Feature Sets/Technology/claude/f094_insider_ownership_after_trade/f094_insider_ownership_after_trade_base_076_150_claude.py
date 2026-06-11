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


# 63d z-score of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_z_63d_base_v076_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_z_126d_base_v077_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_z_252d_base_v078_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_z_504d_base_v079_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_z_63d_base_v080_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_z_126d_base_v081_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_z_252d_base_v082_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_z_504d_base_v083_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_z_63d_base_v084_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_z_126d_base_v085_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_z_252d_base_v086_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_z_504d_base_v087_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_z_63d_base_v088_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_z_126d_base_v089_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_z_252d_base_v090_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_z_504d_base_v091_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_z_63d_base_v092_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_z_126d_base_v093_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_z_252d_base_v094_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_z_504d_base_v095_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_z_63d_base_v096_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_z_126d_base_v097_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_z_252d_base_v098_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_z_504d_base_v099_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_z_63d_base_v100_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_z_126d_base_v101_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_z_252d_base_v102_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_z_504d_base_v103_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_distmax_252d_base_v104_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_distmax_504d_base_v105_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_distmax_252d_base_v106_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_distmax_504d_base_v107_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_distmax_252d_base_v108_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_distmax_504d_base_v109_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_distmax_252d_base_v110_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_distmax_504d_base_v111_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_distmax_252d_base_v112_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_distmax_504d_base_v113_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_distmax_252d_base_v114_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_distmax_504d_base_v115_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_distmax_252d_base_v116_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_distmax_504d_base_v117_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_distmed_126d_base_v118_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_distmed_252d_base_v119_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_distmed_504d_base_v120_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_distmed_126d_base_v121_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_distmed_252d_base_v122_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_distmed_504d_base_v123_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_distmed_126d_base_v124_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_distmed_252d_base_v125_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_distmed_504d_base_v126_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_distmed_126d_base_v127_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_distmed_252d_base_v128_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_distmed_504d_base_v129_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_distmed_126d_base_v130_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_distmed_252d_base_v131_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_distmed_504d_base_v132_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_distmed_126d_base_v133_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_distmed_252d_base_v134_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_distmed_504d_base_v135_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_distmed_126d_base_v136_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_distmed_252d_base_v137_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of meaningful_buy_flag
def f094iow_f094_insider_ownership_after_trade_meaningful_buy_flag_distmed_504d_base_v138_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = ((insider_transaction_shares > 0) & (insider_transaction_shares > 0.05 * insider_shares_before)).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_chg_63d_base_v139_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ownership_after_lvl
def f094iow_f094_insider_ownership_after_trade_ownership_after_lvl_chg_252d_base_v140_signal(insider_shares_after, closeadj):
    base = insider_shares_after
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_chg_63d_base_v141_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ownership_chg
def f094iow_f094_insider_ownership_after_trade_ownership_chg_chg_252d_base_v142_signal(insider_shares_after, insider_shares_before, closeadj):
    base = _f094_own_chg(insider_shares_after, insider_shares_before)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_chg_63d_base_v143_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in retention_ratio
def f094iow_f094_insider_ownership_after_trade_retention_ratio_chg_252d_base_v144_signal(insider_shares_after, insider_sell_shares, closeadj):
    base = insider_shares_after / (insider_shares_after + insider_sell_shares.fillna(0)).replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_chg_63d_base_v145_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in transaction_share_pct
def f094iow_f094_insider_ownership_after_trade_transaction_share_pct_chg_252d_base_v146_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = insider_transaction_shares / insider_shares_before.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_chg_63d_base_v147_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ownership_yoy_chg
def f094iow_f094_insider_ownership_after_trade_ownership_yoy_chg_chg_252d_base_v148_signal(insider_shares_after, closeadj):
    base = insider_shares_after.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_chg_63d_base_v149_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in token_trade_flag
def f094iow_f094_insider_ownership_after_trade_token_trade_flag_chg_252d_base_v150_signal(insider_transaction_shares, insider_shares_before, closeadj):
    base = (insider_transaction_shares < 0.005 * insider_shares_before).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

