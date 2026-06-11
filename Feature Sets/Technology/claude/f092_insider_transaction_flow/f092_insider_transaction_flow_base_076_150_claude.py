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


# 63d z-score of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_z_63d_base_v076_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_z_126d_base_v077_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_z_252d_base_v078_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_z_504d_base_v079_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_z_63d_base_v080_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_z_126d_base_v081_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_z_252d_base_v082_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_z_504d_base_v083_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_z_63d_base_v084_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_z_126d_base_v085_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_z_252d_base_v086_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_z_504d_base_v087_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_z_63d_base_v088_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_z_126d_base_v089_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_z_252d_base_v090_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_z_504d_base_v091_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_z_63d_base_v092_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_z_126d_base_v093_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_z_252d_base_v094_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_z_504d_base_v095_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_z_63d_base_v096_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_z_126d_base_v097_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_z_252d_base_v098_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_z_504d_base_v099_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_z_63d_base_v100_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_z_126d_base_v101_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_z_252d_base_v102_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_z_504d_base_v103_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_z_63d_base_v104_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_z_126d_base_v105_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_z_252d_base_v106_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_z_504d_base_v107_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_z_63d_base_v108_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_z_126d_base_v109_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_z_252d_base_v110_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_z_504d_base_v111_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_z_63d_base_v112_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_z_126d_base_v113_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_z_252d_base_v114_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_z_504d_base_v115_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_z_63d_base_v116_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_z_126d_base_v117_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_z_252d_base_v118_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_z_504d_base_v119_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_z_63d_base_v120_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_z_126d_base_v121_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_z_252d_base_v122_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_z_504d_base_v123_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_z_63d_base_v124_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_z_126d_base_v125_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_z_252d_base_v126_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_z_504d_base_v127_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_z_63d_base_v128_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_z_126d_base_v129_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_z_252d_base_v130_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_z_504d_base_v131_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_z_63d_base_v132_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_z_126d_base_v133_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_z_252d_base_v134_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_z_504d_base_v135_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_z_63d_base_v136_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_z_126d_base_v137_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_z_252d_base_v138_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_z_504d_base_v139_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_z_63d_base_v140_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_z_126d_base_v141_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_z_252d_base_v142_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_z_504d_base_v143_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_z_63d_base_v144_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_z_126d_base_v145_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_z_252d_base_v146_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_z_504d_base_v147_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_z_63d_base_v148_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_z_126d_base_v149_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_z_252d_base_v150_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_z_504d_base_v151_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_z_63d_base_v152_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_z_126d_base_v153_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_z_252d_base_v154_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_z_504d_base_v155_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_z_63d_base_v156_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_z_126d_base_v157_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_z_252d_base_v158_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_z_504d_base_v159_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_distmax_252d_base_v160_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_distmax_504d_base_v161_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_distmax_252d_base_v162_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_distmax_504d_base_v163_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_distmax_252d_base_v164_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_distmax_504d_base_v165_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_distmax_252d_base_v166_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_distmax_504d_base_v167_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_distmax_252d_base_v168_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_distmax_504d_base_v169_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_distmax_252d_base_v170_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_distmax_504d_base_v171_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_distmax_252d_base_v172_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_distmax_504d_base_v173_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_distmax_252d_base_v174_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_distmax_504d_base_v175_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

