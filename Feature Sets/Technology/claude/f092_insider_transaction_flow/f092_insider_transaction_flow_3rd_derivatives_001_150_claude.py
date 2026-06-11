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


# 21d acceleration of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_accel_21d_3d_v001_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_accel_63d_3d_v002_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_accel_126d_3d_v003_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_accel_252d_3d_v004_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_accel_21d_3d_v005_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_accel_63d_3d_v006_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_accel_126d_3d_v007_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_accel_252d_3d_v008_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_accel_21d_3d_v009_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_accel_63d_3d_v010_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_accel_126d_3d_v011_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_accel_252d_3d_v012_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_accel_21d_3d_v013_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_accel_63d_3d_v014_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_accel_126d_3d_v015_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_accel_252d_3d_v016_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_accel_21d_3d_v017_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_accel_63d_3d_v018_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_accel_126d_3d_v019_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_accel_252d_3d_v020_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_accel_21d_3d_v021_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_accel_63d_3d_v022_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_accel_126d_3d_v023_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_accel_252d_3d_v024_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_accel_21d_3d_v025_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_accel_63d_3d_v026_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_accel_126d_3d_v027_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_accel_252d_3d_v028_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_accel_21d_3d_v029_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_accel_63d_3d_v030_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_accel_126d_3d_v031_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_accel_252d_3d_v032_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_accel_21d_3d_v033_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_accel_63d_3d_v034_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_accel_126d_3d_v035_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_accel_252d_3d_v036_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_accel_21d_3d_v037_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_accel_63d_3d_v038_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_accel_126d_3d_v039_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_accel_252d_3d_v040_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_accel_21d_3d_v041_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_accel_63d_3d_v042_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_accel_126d_3d_v043_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_accel_252d_3d_v044_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_accel_21d_3d_v045_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_accel_63d_3d_v046_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_accel_126d_3d_v047_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_accel_252d_3d_v048_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_accel_21d_3d_v049_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_accel_63d_3d_v050_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_accel_126d_3d_v051_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_accel_252d_3d_v052_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_accel_21d_3d_v053_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_accel_63d_3d_v054_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_accel_126d_3d_v055_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_accel_252d_3d_v056_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_accel_21d_3d_v057_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_accel_63d_3d_v058_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_accel_126d_3d_v059_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_accel_252d_3d_v060_signal(insider_f_value, closeadj):
    base = insider_f_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_accel_21d_3d_v061_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_accel_63d_3d_v062_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_accel_126d_3d_v063_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_accel_252d_3d_v064_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_accel_21d_3d_v065_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_accel_63d_3d_v066_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_accel_126d_3d_v067_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_accel_252d_3d_v068_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_accel_21d_3d_v069_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_accel_63d_3d_v070_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_accel_126d_3d_v071_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_accel_252d_3d_v072_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_accel_21d_3d_v073_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_accel_63d_3d_v074_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_accel_126d_3d_v075_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_accel_252d_3d_v076_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_accel_21d_3d_v077_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_accel_63d_3d_v078_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_accel_126d_3d_v079_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_accel_252d_3d_v080_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_accel_21d_3d_v081_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_accel_63d_3d_v082_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_accel_126d_3d_v083_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_accel_252d_3d_v084_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slopez_21d_z126_3d_v085_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slopez_63d_z252_3d_v086_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slopez_126d_z252_3d_v087_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_slopez_252d_z504_3d_v088_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slopez_21d_z126_3d_v089_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slopez_63d_z252_3d_v090_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slopez_126d_z252_3d_v091_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_slopez_252d_z504_3d_v092_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slopez_21d_z126_3d_v093_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slopez_63d_z252_3d_v094_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slopez_126d_z252_3d_v095_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_slopez_252d_z504_3d_v096_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slopez_21d_z126_3d_v097_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slopez_63d_z252_3d_v098_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slopez_126d_z252_3d_v099_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_slopez_252d_z504_3d_v100_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slopez_21d_z126_3d_v101_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slopez_63d_z252_3d_v102_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slopez_126d_z252_3d_v103_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_slopez_252d_z504_3d_v104_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slopez_21d_z126_3d_v105_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slopez_63d_z252_3d_v106_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slopez_126d_z252_3d_v107_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_slopez_252d_z504_3d_v108_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slopez_21d_z126_3d_v109_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slopez_63d_z252_3d_v110_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slopez_126d_z252_3d_v111_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_slopez_252d_z504_3d_v112_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slopez_21d_z126_3d_v113_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slopez_63d_z252_3d_v114_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slopez_126d_z252_3d_v115_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_slopez_252d_z504_3d_v116_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slopez_21d_z126_3d_v117_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slopez_63d_z252_3d_v118_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slopez_126d_z252_3d_v119_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_slopez_252d_z504_3d_v120_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slopez_21d_z126_3d_v121_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slopez_63d_z252_3d_v122_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slopez_126d_z252_3d_v123_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_slopez_252d_z504_3d_v124_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slopez_21d_z126_3d_v125_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slopez_63d_z252_3d_v126_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slopez_126d_z252_3d_v127_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_slopez_252d_z504_3d_v128_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slopez_21d_z126_3d_v129_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slopez_63d_z252_3d_v130_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slopez_126d_z252_3d_v131_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of s_code_sell_value
def f092itf_f092_insider_transaction_flow_s_code_sell_value_slopez_252d_z504_3d_v132_signal(insider_s_sell_value, closeadj):
    base = insider_s_sell_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slopez_21d_z126_3d_v133_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slopez_63d_z252_3d_v134_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slopez_126d_z252_3d_v135_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of real_sell_value
def f092itf_f092_insider_transaction_flow_real_sell_value_slopez_252d_z504_3d_v136_signal(insider_s_sell_value, insider_f_value, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slopez_21d_z126_3d_v137_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slopez_63d_z252_3d_v138_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slopez_126d_z252_3d_v139_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of real_sell_to_mcap
def f092itf_f092_insider_transaction_flow_real_sell_to_mcap_slopez_252d_z504_3d_v140_signal(insider_s_sell_value, insider_f_value, marketcap, closeadj):
    base = _f092_real_sell(insider_s_sell_value, insider_f_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slopez_21d_z126_3d_v141_signal(insider_f_value, closeadj):
    base = insider_f_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slopez_63d_z252_3d_v142_signal(insider_f_value, closeadj):
    base = insider_f_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slopez_126d_z252_3d_v143_signal(insider_f_value, closeadj):
    base = insider_f_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of f_code_tax_value
def f092itf_f092_insider_transaction_flow_f_code_tax_value_slopez_252d_z504_3d_v144_signal(insider_f_value, closeadj):
    base = insider_f_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slopez_21d_z126_3d_v145_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slopez_63d_z252_3d_v146_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slopez_126d_z252_3d_v147_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of f_code_share_of_sells
def f092itf_f092_insider_transaction_flow_f_code_share_of_sells_slopez_252d_z504_3d_v148_signal(insider_f_value, insider_sell_value, closeadj):
    base = insider_f_value / insider_sell_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slopez_21d_z126_3d_v149_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slopez_63d_z252_3d_v150_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slopez_126d_z252_3d_v151_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of m_code_exercise_value
def f092itf_f092_insider_transaction_flow_m_code_exercise_value_slopez_252d_z504_3d_v152_signal(insider_m_exercise_value, closeadj):
    base = insider_m_exercise_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slopez_21d_z126_3d_v153_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slopez_63d_z252_3d_v154_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slopez_126d_z252_3d_v155_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ten_pct_owner_buy_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_buy_value_slopez_252d_z504_3d_v156_signal(insider_10pct_buy_value, closeadj):
    base = insider_10pct_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slopez_21d_z126_3d_v157_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slopez_63d_z252_3d_v158_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slopez_126d_z252_3d_v159_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ten_pct_owner_sell_value
def f092itf_f092_insider_transaction_flow_ten_pct_owner_sell_value_slopez_252d_z504_3d_v160_signal(insider_10pct_sell_value, closeadj):
    base = insider_10pct_sell_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slopez_21d_z126_3d_v161_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slopez_63d_z252_3d_v162_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slopez_126d_z252_3d_v163_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ten_pct_owner_net
def f092itf_f092_insider_transaction_flow_ten_pct_owner_net_slopez_252d_z504_3d_v164_signal(insider_10pct_buy_value, insider_10pct_sell_value, closeadj):
    base = insider_10pct_buy_value.fillna(0) - insider_10pct_sell_value.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slopez_21d_z126_3d_v165_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slopez_63d_z252_3d_v166_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slopez_126d_z252_3d_v167_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_code_to_sector_median
def f092itf_f092_insider_transaction_flow_p_code_to_sector_median_slopez_252d_z504_3d_v168_signal(insider_p_buy_value, marketcap, p_code_intensity_sector_med, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs() - p_code_intensity_sector_med) / p_code_intensity_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_jerk_21d_3d_v169_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_jerk_63d_3d_v170_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of net_buy_sell_value
def f092itf_f092_insider_transaction_flow_net_buy_sell_value_jerk_126d_3d_v171_signal(insider_buy_value, insider_sell_value, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_jerk_21d_3d_v172_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_jerk_63d_3d_v173_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of buy_value_lvl
def f092itf_f092_insider_transaction_flow_buy_value_lvl_jerk_126d_3d_v174_signal(insider_buy_value, closeadj):
    base = insider_buy_value
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_jerk_21d_3d_v175_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_jerk_63d_3d_v176_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sell_value_lvl
def f092itf_f092_insider_transaction_flow_sell_value_lvl_jerk_126d_3d_v177_signal(insider_sell_value, closeadj):
    base = insider_sell_value
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_jerk_21d_3d_v178_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_jerk_63d_3d_v179_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of net_to_mcap
def f092itf_f092_insider_transaction_flow_net_to_mcap_jerk_126d_3d_v180_signal(insider_buy_value, insider_sell_value, marketcap, closeadj):
    base = _f092_netflow(insider_buy_value, insider_sell_value) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_jerk_21d_3d_v181_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_jerk_63d_3d_v182_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of net_share_balance
def f092itf_f092_insider_transaction_flow_net_share_balance_jerk_126d_3d_v183_signal(insider_buy_shares, insider_sell_shares, closeadj):
    base = insider_buy_shares.fillna(0) - insider_sell_shares.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_jerk_21d_3d_v184_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_jerk_63d_3d_v185_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_code_buy_value
def f092itf_f092_insider_transaction_flow_p_code_buy_value_jerk_126d_3d_v186_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_jerk_21d_3d_v187_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_jerk_63d_3d_v188_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_code_buy_shares
def f092itf_f092_insider_transaction_flow_p_code_buy_shares_jerk_126d_3d_v189_signal(insider_p_buy_shares, closeadj):
    base = insider_p_buy_shares
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_jerk_21d_3d_v190_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_jerk_63d_3d_v191_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_code_to_mcap
def f092itf_f092_insider_transaction_flow_p_code_to_mcap_jerk_126d_3d_v192_signal(insider_p_buy_value, marketcap, closeadj):
    base = insider_p_buy_value / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_jerk_21d_3d_v193_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_jerk_63d_3d_v194_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_code_rolling_30d
def f092itf_f092_insider_transaction_flow_p_code_rolling_30d_jerk_126d_3d_v195_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_jerk_21d_3d_v196_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_jerk_63d_3d_v197_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_code_rolling_90d
def f092itf_f092_insider_transaction_flow_p_code_rolling_90d_jerk_126d_3d_v198_signal(insider_p_buy_value, closeadj):
    base = insider_p_buy_value.rolling(90, min_periods=1).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_jerk_21d_3d_v199_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_code_burst_flag
def f092itf_f092_insider_transaction_flow_p_code_burst_flag_jerk_63d_3d_v200_signal(insider_p_buy_value, closeadj):
    base = (insider_p_buy_value > insider_p_buy_value.rolling(252, min_periods=63).quantile(0.95)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

