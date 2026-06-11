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
def _f092_netflow(insider_buy_value, insider_sell_value):
    return insider_buy_value.fillna(0) - insider_sell_value.fillna(0)


def _f092_real_sell(insider_s_sell_value, insider_f_value):
    # F-code = tax withholding on RSU vesting; not a real conviction sell.
    return insider_s_sell_value.fillna(0) - insider_f_value.fillna(0)


# 21d mean of net_buy_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_mean_21d_base_v001_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of net_buy_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_mean_63d_base_v002_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of net_buy_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_mean_126d_base_v003_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of net_buy_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_mean_252d_base_v004_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of net_buy_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_mean_504d_base_v005_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of buy_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_buy_value_lvl_mean_21d_base_v006_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of buy_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_buy_value_lvl_mean_63d_base_v007_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of buy_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_buy_value_lvl_mean_126d_base_v008_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of buy_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_buy_value_lvl_mean_252d_base_v009_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of buy_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_buy_value_lvl_mean_504d_base_v010_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sell_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_sell_value_lvl_mean_21d_base_v011_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sell_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_sell_value_lvl_mean_63d_base_v012_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sell_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_sell_value_lvl_mean_126d_base_v013_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sell_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_sell_value_lvl_mean_252d_base_v014_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sell_value_lvl scaled by closeadj
def f092itf_f092_insider_transaction_flow_sell_value_lvl_mean_504d_base_v015_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of net_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_to_mcap_mean_21d_base_v016_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of net_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_to_mcap_mean_63d_base_v017_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of net_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_to_mcap_mean_126d_base_v018_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of net_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_to_mcap_mean_252d_base_v019_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of net_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_to_mcap_mean_504d_base_v020_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of net_share_balance scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_share_balance_mean_21d_base_v021_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of net_share_balance scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_share_balance_mean_63d_base_v022_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of net_share_balance scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_share_balance_mean_126d_base_v023_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of net_share_balance scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_share_balance_mean_252d_base_v024_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of net_share_balance scaled by closeadj
def f092itf_f092_insider_transaction_flow_net_share_balance_mean_504d_base_v025_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_code_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_value_mean_21d_base_v026_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_code_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_value_mean_63d_base_v027_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_code_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_value_mean_126d_base_v028_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_code_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_value_mean_252d_base_v029_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_code_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_value_mean_504d_base_v030_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_code_buy_shares scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_mean_21d_base_v031_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_code_buy_shares scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_mean_63d_base_v032_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_code_buy_shares scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_mean_126d_base_v033_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_code_buy_shares scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_mean_252d_base_v034_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_code_buy_shares scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_mean_504d_base_v035_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_code_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_mean_21d_base_v036_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_code_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_mean_63d_base_v037_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_code_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_mean_126d_base_v038_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_code_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_mean_252d_base_v039_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_code_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_mean_504d_base_v040_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_code_rolling_30d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_mean_21d_base_v041_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_code_rolling_30d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_mean_63d_base_v042_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_code_rolling_30d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_mean_126d_base_v043_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_code_rolling_30d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_mean_252d_base_v044_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_code_rolling_30d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_mean_504d_base_v045_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_code_rolling_90d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_mean_21d_base_v046_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_code_rolling_90d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_mean_63d_base_v047_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_code_rolling_90d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_mean_126d_base_v048_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_code_rolling_90d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_mean_252d_base_v049_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_code_rolling_90d scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_mean_504d_base_v050_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_code_burst_flag scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_mean_21d_base_v051_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_code_burst_flag scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_mean_63d_base_v052_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_code_burst_flag scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_mean_126d_base_v053_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_code_burst_flag scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_mean_252d_base_v054_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_code_burst_flag scaled by closeadj
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_mean_504d_base_v055_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of s_code_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_s_code_sell_value_mean_21d_base_v056_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of s_code_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_s_code_sell_value_mean_63d_base_v057_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of s_code_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_s_code_sell_value_mean_126d_base_v058_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of s_code_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_s_code_sell_value_mean_252d_base_v059_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of s_code_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_s_code_sell_value_mean_504d_base_v060_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of real_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_value_mean_21d_base_v061_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of real_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_value_mean_63d_base_v062_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of real_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_value_mean_126d_base_v063_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of real_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_value_mean_252d_base_v064_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of real_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_value_mean_504d_base_v065_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of real_sell_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_mean_21d_base_v066_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of real_sell_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_mean_63d_base_v067_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of real_sell_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_mean_126d_base_v068_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of real_sell_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_mean_252d_base_v069_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of real_sell_to_mcap scaled by closeadj
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_mean_504d_base_v070_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of f_code_tax_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_tax_value_mean_21d_base_v071_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of f_code_tax_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_tax_value_mean_63d_base_v072_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of f_code_tax_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_tax_value_mean_126d_base_v073_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of f_code_tax_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_tax_value_mean_252d_base_v074_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of f_code_tax_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_tax_value_mean_504d_base_v075_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of f_code_share_of_sells scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_mean_21d_base_v076_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of f_code_share_of_sells scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_mean_63d_base_v077_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of f_code_share_of_sells scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_mean_126d_base_v078_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of f_code_share_of_sells scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_mean_252d_base_v079_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of f_code_share_of_sells scaled by closeadj
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_mean_504d_base_v080_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of m_code_exercise_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_mean_21d_base_v081_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of m_code_exercise_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_mean_63d_base_v082_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of m_code_exercise_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_mean_126d_base_v083_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of m_code_exercise_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_mean_252d_base_v084_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of m_code_exercise_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_mean_504d_base_v085_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ten_pct_owner_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_mean_21d_base_v086_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ten_pct_owner_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_mean_63d_base_v087_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ten_pct_owner_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_mean_126d_base_v088_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ten_pct_owner_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_mean_252d_base_v089_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ten_pct_owner_buy_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_mean_504d_base_v090_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ten_pct_owner_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_mean_21d_base_v091_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ten_pct_owner_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_mean_63d_base_v092_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ten_pct_owner_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_mean_126d_base_v093_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ten_pct_owner_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_mean_252d_base_v094_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ten_pct_owner_sell_value scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_mean_504d_base_v095_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ten_pct_owner_net scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_mean_21d_base_v096_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ten_pct_owner_net scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_mean_63d_base_v097_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ten_pct_owner_net scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_mean_126d_base_v098_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ten_pct_owner_net scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_mean_252d_base_v099_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ten_pct_owner_net scaled by closeadj
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_mean_504d_base_v100_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

