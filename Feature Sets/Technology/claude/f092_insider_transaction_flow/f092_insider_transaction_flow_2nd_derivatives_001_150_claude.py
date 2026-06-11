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
def _f092_netflow(insider_buy_value, insider_sell_value):
    return insider_buy_value.fillna(0) - insider_sell_value.fillna(0)


def _f092_real_sell(insider_s_sell_value, insider_f_value):
    # F-code = tax withholding on RSU vesting; not a real conviction sell.
    return insider_s_sell_value.fillna(0) - insider_f_value.fillna(0)


# 21d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slope_21d_2d_v001_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slope_63d_2d_v002_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slope_126d_2d_v003_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slope_252d_2d_v004_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slope_504d_2d_v005_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slope_21d_2d_v006_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slope_63d_2d_v007_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slope_126d_2d_v008_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slope_252d_2d_v009_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slope_504d_2d_v010_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slope_21d_2d_v011_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slope_63d_2d_v012_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slope_126d_2d_v013_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slope_252d_2d_v014_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slope_504d_2d_v015_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slope_21d_2d_v016_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slope_63d_2d_v017_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slope_126d_2d_v018_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slope_252d_2d_v019_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slope_504d_2d_v020_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slope_21d_2d_v021_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slope_63d_2d_v022_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slope_126d_2d_v023_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slope_252d_2d_v024_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slope_504d_2d_v025_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slope_21d_2d_v026_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slope_63d_2d_v027_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slope_126d_2d_v028_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slope_252d_2d_v029_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slope_504d_2d_v030_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slope_21d_2d_v031_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slope_63d_2d_v032_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slope_126d_2d_v033_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slope_252d_2d_v034_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slope_504d_2d_v035_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slope_21d_2d_v036_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slope_63d_2d_v037_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slope_126d_2d_v038_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slope_252d_2d_v039_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slope_504d_2d_v040_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slope_21d_2d_v041_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slope_63d_2d_v042_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slope_126d_2d_v043_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slope_252d_2d_v044_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slope_504d_2d_v045_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slope_21d_2d_v046_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slope_63d_2d_v047_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slope_126d_2d_v048_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slope_252d_2d_v049_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slope_504d_2d_v050_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slope_21d_2d_v051_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slope_63d_2d_v052_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slope_126d_2d_v053_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slope_252d_2d_v054_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slope_504d_2d_v055_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slope_21d_2d_v056_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slope_63d_2d_v057_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slope_126d_2d_v058_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slope_252d_2d_v059_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slope_504d_2d_v060_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slope_21d_2d_v061_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slope_63d_2d_v062_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slope_126d_2d_v063_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slope_252d_2d_v064_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slope_504d_2d_v065_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slope_21d_2d_v066_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slope_63d_2d_v067_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slope_126d_2d_v068_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slope_252d_2d_v069_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slope_504d_2d_v070_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slope_21d_2d_v071_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slope_63d_2d_v072_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slope_126d_2d_v073_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slope_252d_2d_v074_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slope_504d_2d_v075_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slope_21d_2d_v076_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slope_63d_2d_v077_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slope_126d_2d_v078_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slope_252d_2d_v079_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slope_504d_2d_v080_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slope_21d_2d_v081_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slope_63d_2d_v082_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slope_126d_2d_v083_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slope_252d_2d_v084_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slope_504d_2d_v085_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slope_21d_2d_v086_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slope_63d_2d_v087_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slope_126d_2d_v088_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slope_252d_2d_v089_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slope_504d_2d_v090_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slope_21d_2d_v091_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slope_63d_2d_v092_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slope_126d_2d_v093_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slope_252d_2d_v094_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slope_504d_2d_v095_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slope_21d_2d_v096_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slope_63d_2d_v097_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slope_126d_2d_v098_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slope_252d_2d_v099_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slope_504d_2d_v100_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slope_21d_2d_v101_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slope_63d_2d_v102_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slope_126d_2d_v103_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slope_252d_2d_v104_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slope_504d_2d_v105_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_sm21_sl21_2d_v106_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_sm63_sl21_2d_v107_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_sm63_sl63_2d_v108_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_sm252_sl63_2d_v109_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_sm252_sl126_2d_v110_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_sm21_sl21_2d_v111_signal(insider_buy_value, closeadj):
    base = _mean(insider_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_sm63_sl21_2d_v112_signal(insider_buy_value, closeadj):
    base = _mean(insider_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_sm63_sl63_2d_v113_signal(insider_buy_value, closeadj):
    base = _mean(insider_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_sm252_sl63_2d_v114_signal(insider_buy_value, closeadj):
    base = _mean(insider_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_sm252_sl126_2d_v115_signal(insider_buy_value, closeadj):
    base = _mean(insider_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_sm21_sl21_2d_v116_signal(insider_sell_value, closeadj):
    base = _mean(insider_sell_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_sm63_sl21_2d_v117_signal(insider_sell_value, closeadj):
    base = _mean(insider_sell_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_sm63_sl63_2d_v118_signal(insider_sell_value, closeadj):
    base = _mean(insider_sell_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_sm252_sl63_2d_v119_signal(insider_sell_value, closeadj):
    base = _mean(insider_sell_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_sm252_sl126_2d_v120_signal(insider_sell_value, closeadj):
    base = _mean(insider_sell_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_sm21_sl21_2d_v121_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_sm63_sl21_2d_v122_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_sm63_sl63_2d_v123_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_sm252_sl63_2d_v124_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_sm252_sl126_2d_v125_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _mean(_f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_sm21_sl21_2d_v126_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = _mean(insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_sm63_sl21_2d_v127_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = _mean(insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_sm63_sl63_2d_v128_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = _mean(insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_sm252_sl63_2d_v129_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = _mean(insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_sm252_sl126_2d_v130_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = _mean(insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_sm21_sl21_2d_v131_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_sm63_sl21_2d_v132_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_sm63_sl63_2d_v133_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_sm252_sl63_2d_v134_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_sm252_sl126_2d_v135_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_sm21_sl21_2d_v136_signal(insider_p_buy_shares, closeadj):
    base = _mean(insider_p_buy_shares, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_sm63_sl21_2d_v137_signal(insider_p_buy_shares, closeadj):
    base = _mean(insider_p_buy_shares, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_sm63_sl63_2d_v138_signal(insider_p_buy_shares, closeadj):
    base = _mean(insider_p_buy_shares, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_sm252_sl63_2d_v139_signal(insider_p_buy_shares, closeadj):
    base = _mean(insider_p_buy_shares, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_sm252_sl126_2d_v140_signal(insider_p_buy_shares, closeadj):
    base = _mean(insider_p_buy_shares, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_sm21_sl21_2d_v141_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean(insider_p_buy_value / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_sm63_sl21_2d_v142_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean(insider_p_buy_value / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_sm63_sl63_2d_v143_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean(insider_p_buy_value / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_sm252_sl63_2d_v144_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean(insider_p_buy_value / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_sm252_sl126_2d_v145_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean(insider_p_buy_value / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_sm21_sl21_2d_v146_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(30, min_periods=1).sum(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_sm63_sl21_2d_v147_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(30, min_periods=1).sum(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_sm63_sl63_2d_v148_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(30, min_periods=1).sum(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_sm252_sl63_2d_v149_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(30, min_periods=1).sum(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_sm252_sl126_2d_v150_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(30, min_periods=1).sum(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_sm21_sl21_2d_v151_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(90, min_periods=1).sum(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_sm63_sl21_2d_v152_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(90, min_periods=1).sum(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_sm63_sl63_2d_v153_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(90, min_periods=1).sum(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_sm252_sl63_2d_v154_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(90, min_periods=1).sum(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_sm252_sl126_2d_v155_signal(insider_p_buy_value, closeadj):
    base = _mean(insider_p_buy_value.rolling(90, min_periods=1).sum(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_sm21_sl21_2d_v156_signal(insider_p_buy_value, closeadj):
    base = _mean((insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_sm63_sl21_2d_v157_signal(insider_p_buy_value, closeadj):
    base = _mean((insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_sm63_sl63_2d_v158_signal(insider_p_buy_value, closeadj):
    base = _mean((insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_sm252_sl63_2d_v159_signal(insider_p_buy_value, closeadj):
    base = _mean((insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_sm252_sl126_2d_v160_signal(insider_p_buy_value, closeadj):
    base = _mean((insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_sm21_sl21_2d_v161_signal(insider_s_sell_value, closeadj):
    base = _mean(insider_s_sell_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_sm63_sl21_2d_v162_signal(insider_s_sell_value, closeadj):
    base = _mean(insider_s_sell_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_sm63_sl63_2d_v163_signal(insider_s_sell_value, closeadj):
    base = _mean(insider_s_sell_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_sm252_sl63_2d_v164_signal(insider_s_sell_value, closeadj):
    base = _mean(insider_s_sell_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_sm252_sl126_2d_v165_signal(insider_s_sell_value, closeadj):
    base = _mean(insider_s_sell_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_sm21_sl21_2d_v166_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_sm63_sl21_2d_v167_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_sm63_sl63_2d_v168_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_sm252_sl63_2d_v169_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_sm252_sl126_2d_v170_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_sm21_sl21_2d_v171_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_sm63_sl21_2d_v172_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_sm63_sl63_2d_v173_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_sm252_sl63_2d_v174_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_sm252_sl126_2d_v175_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _mean(_f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_sm21_sl21_2d_v176_signal(insider_f_value, closeadj):
    base = _mean(insider_f_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_sm63_sl21_2d_v177_signal(insider_f_value, closeadj):
    base = _mean(insider_f_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_sm63_sl63_2d_v178_signal(insider_f_value, closeadj):
    base = _mean(insider_f_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_sm252_sl63_2d_v179_signal(insider_f_value, closeadj):
    base = _mean(insider_f_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_sm252_sl126_2d_v180_signal(insider_f_value, closeadj):
    base = _mean(insider_f_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_sm21_sl21_2d_v181_signal(insider_f_value, insider_sell_value, closeadj):
    base = _mean(insider_f_value / insider_sell_value.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_sm63_sl21_2d_v182_signal(insider_f_value, insider_sell_value, closeadj):
    base = _mean(insider_f_value / insider_sell_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_sm63_sl63_2d_v183_signal(insider_f_value, insider_sell_value, closeadj):
    base = _mean(insider_f_value / insider_sell_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_sm252_sl63_2d_v184_signal(insider_f_value, insider_sell_value, closeadj):
    base = _mean(insider_f_value / insider_sell_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_sm252_sl126_2d_v185_signal(insider_f_value, insider_sell_value, closeadj):
    base = _mean(insider_f_value / insider_sell_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_sm21_sl21_2d_v186_signal(insider_m_exercise_value, closeadj):
    base = _mean(insider_m_exercise_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_sm63_sl21_2d_v187_signal(insider_m_exercise_value, closeadj):
    base = _mean(insider_m_exercise_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_sm63_sl63_2d_v188_signal(insider_m_exercise_value, closeadj):
    base = _mean(insider_m_exercise_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_sm252_sl63_2d_v189_signal(insider_m_exercise_value, closeadj):
    base = _mean(insider_m_exercise_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_sm252_sl126_2d_v190_signal(insider_m_exercise_value, closeadj):
    base = _mean(insider_m_exercise_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_sm21_sl21_2d_v191_signal(insider_10pct_buy_value, closeadj):
    base = _mean(insider_10pct_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_sm63_sl21_2d_v192_signal(insider_10pct_buy_value, closeadj):
    base = _mean(insider_10pct_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_sm63_sl63_2d_v193_signal(insider_10pct_buy_value, closeadj):
    base = _mean(insider_10pct_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_sm252_sl63_2d_v194_signal(insider_10pct_buy_value, closeadj):
    base = _mean(insider_10pct_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_sm252_sl126_2d_v195_signal(insider_10pct_buy_value, closeadj):
    base = _mean(insider_10pct_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_sm21_sl21_2d_v196_signal(insider_10pct_sell_value, closeadj):
    base = _mean(insider_10pct_sell_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_sm63_sl21_2d_v197_signal(insider_10pct_sell_value, closeadj):
    base = _mean(insider_10pct_sell_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_sm63_sl63_2d_v198_signal(insider_10pct_sell_value, closeadj):
    base = _mean(insider_10pct_sell_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_sm252_sl63_2d_v199_signal(insider_10pct_sell_value, closeadj):
    base = _mean(insider_10pct_sell_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_sm252_sl126_2d_v200_signal(insider_10pct_sell_value, closeadj):
    base = _mean(insider_10pct_sell_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

