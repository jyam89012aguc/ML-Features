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
def _f038_logmc(marketcap):
    return np.log(marketcap.abs().replace(0, np.nan))


# 21d acceleration of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_accel_21d_3d_v001_signal(marketcap, closeadj):
    base = marketcap
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_accel_63d_3d_v002_signal(marketcap, closeadj):
    base = marketcap
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_accel_126d_3d_v003_signal(marketcap, closeadj):
    base = marketcap
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_accel_252d_3d_v004_signal(marketcap, closeadj):
    base = marketcap
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_accel_21d_3d_v005_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_accel_63d_3d_v006_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_accel_126d_3d_v007_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_accel_252d_3d_v008_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_accel_21d_3d_v009_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_accel_63d_3d_v010_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_accel_126d_3d_v011_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_accel_252d_3d_v012_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_accel_21d_3d_v013_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_accel_63d_3d_v014_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_accel_126d_3d_v015_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_accel_252d_3d_v016_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_accel_21d_3d_v017_signal(close, closeadj):
    base = close
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_accel_63d_3d_v018_signal(close, closeadj):
    base = close
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_accel_126d_3d_v019_signal(close, closeadj):
    base = close
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_accel_252d_3d_v020_signal(close, closeadj):
    base = close
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_accel_21d_3d_v021_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_accel_63d_3d_v022_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_accel_126d_3d_v023_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_accel_252d_3d_v024_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_accel_21d_3d_v025_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_accel_63d_3d_v026_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_accel_126d_3d_v027_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_accel_252d_3d_v028_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slopez_21d_z126_3d_v029_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slopez_63d_z252_3d_v030_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slopez_126d_z252_3d_v031_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slopez_252d_z504_3d_v032_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slopez_21d_z126_3d_v033_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slopez_63d_z252_3d_v034_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slopez_126d_z252_3d_v035_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slopez_252d_z504_3d_v036_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slopez_21d_z126_3d_v037_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slopez_63d_z252_3d_v038_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slopez_126d_z252_3d_v039_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slopez_252d_z504_3d_v040_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slopez_21d_z126_3d_v041_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slopez_63d_z252_3d_v042_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slopez_126d_z252_3d_v043_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slopez_252d_z504_3d_v044_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slopez_21d_z126_3d_v045_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slopez_63d_z252_3d_v046_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slopez_126d_z252_3d_v047_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slopez_252d_z504_3d_v048_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slopez_21d_z126_3d_v049_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slopez_63d_z252_3d_v050_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slopez_126d_z252_3d_v051_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slopez_252d_z504_3d_v052_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slopez_21d_z126_3d_v053_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slopez_63d_z252_3d_v054_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slopez_126d_z252_3d_v055_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slopez_252d_z504_3d_v056_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_jerk_21d_3d_v057_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_jerk_63d_3d_v058_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_jerk_126d_3d_v059_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_jerk_21d_3d_v060_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_jerk_63d_3d_v061_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_jerk_126d_3d_v062_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_jerk_21d_3d_v063_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_jerk_63d_3d_v064_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_jerk_126d_3d_v065_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_jerk_21d_3d_v066_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_jerk_63d_3d_v067_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_jerk_126d_3d_v068_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_jerk_21d_3d_v069_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_jerk_63d_3d_v070_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_jerk_126d_3d_v071_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_jerk_21d_3d_v072_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_jerk_63d_3d_v073_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_jerk_126d_3d_v074_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_jerk_21d_3d_v075_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_jerk_63d_3d_v076_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_jerk_126d_3d_v077_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of marketcap_lvl smoothed over 252d
def f038mcp_f038_market_capitalization_marketcap_lvl_smoothaccel_63d_sm252_3d_v078_signal(marketcap, closeadj):
    base = marketcap
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of marketcap_lvl smoothed over 504d
def f038mcp_f038_market_capitalization_marketcap_lvl_smoothaccel_252d_sm504_3d_v079_signal(marketcap, closeadj):
    base = marketcap
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of log_mcap smoothed over 252d
def f038mcp_f038_market_capitalization_log_mcap_smoothaccel_63d_sm252_3d_v080_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of log_mcap smoothed over 504d
def f038mcp_f038_market_capitalization_log_mcap_smoothaccel_252d_sm504_3d_v081_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_yoy smoothed over 252d
def f038mcp_f038_market_capitalization_mcap_yoy_smoothaccel_63d_sm252_3d_v082_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_yoy smoothed over 504d
def f038mcp_f038_market_capitalization_mcap_yoy_smoothaccel_252d_sm504_3d_v083_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_qoq smoothed over 252d
def f038mcp_f038_market_capitalization_mcap_qoq_smoothaccel_63d_sm252_3d_v084_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_qoq smoothed over 504d
def f038mcp_f038_market_capitalization_mcap_qoq_smoothaccel_252d_sm504_3d_v085_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of price_per_share smoothed over 252d
def f038mcp_f038_market_capitalization_price_per_share_smoothaccel_63d_sm252_3d_v086_signal(close, closeadj):
    base = close
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of price_per_share smoothed over 504d
def f038mcp_f038_market_capitalization_price_per_share_smoothaccel_252d_sm504_3d_v087_signal(close, closeadj):
    base = close
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_to_rev smoothed over 252d
def f038mcp_f038_market_capitalization_mcap_to_rev_smoothaccel_63d_sm252_3d_v088_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_to_rev smoothed over 504d
def f038mcp_f038_market_capitalization_mcap_to_rev_smoothaccel_252d_sm504_3d_v089_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_to_asset smoothed over 252d
def f038mcp_f038_market_capitalization_mcap_to_asset_smoothaccel_63d_sm252_3d_v090_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_to_asset smoothed over 504d
def f038mcp_f038_market_capitalization_mcap_to_asset_smoothaccel_252d_sm504_3d_v091_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_accelz_21d_z252_3d_v092_signal(marketcap, closeadj):
    base = marketcap
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_accelz_63d_z504_3d_v093_signal(marketcap, closeadj):
    base = marketcap
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_accelz_21d_z252_3d_v094_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_accelz_63d_z504_3d_v095_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_accelz_21d_z252_3d_v096_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_accelz_63d_z504_3d_v097_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_accelz_21d_z252_3d_v098_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_accelz_63d_z504_3d_v099_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_accelz_21d_z252_3d_v100_signal(close, closeadj):
    base = close
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_accelz_63d_z504_3d_v101_signal(close, closeadj):
    base = close
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_accelz_21d_z252_3d_v102_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_accelz_63d_z504_3d_v103_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_accelz_21d_z252_3d_v104_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_accelz_63d_z504_3d_v105_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in marketcap_lvl (raw count, no price scaling)
def f038mcp_f038_market_capitalization_marketcap_lvl_signflip_63d_3d_v106_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in marketcap_lvl (raw count, no price scaling)
def f038mcp_f038_market_capitalization_marketcap_lvl_signflip_252d_3d_v107_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in log_mcap (raw count, no price scaling)
def f038mcp_f038_market_capitalization_log_mcap_signflip_63d_3d_v108_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in log_mcap (raw count, no price scaling)
def f038mcp_f038_market_capitalization_log_mcap_signflip_252d_3d_v109_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in mcap_yoy (raw count, no price scaling)
def f038mcp_f038_market_capitalization_mcap_yoy_signflip_63d_3d_v110_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in mcap_yoy (raw count, no price scaling)
def f038mcp_f038_market_capitalization_mcap_yoy_signflip_252d_3d_v111_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in mcap_qoq (raw count, no price scaling)
def f038mcp_f038_market_capitalization_mcap_qoq_signflip_63d_3d_v112_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in mcap_qoq (raw count, no price scaling)
def f038mcp_f038_market_capitalization_mcap_qoq_signflip_252d_3d_v113_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in price_per_share (raw count, no price scaling)
def f038mcp_f038_market_capitalization_price_per_share_signflip_63d_3d_v114_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in price_per_share (raw count, no price scaling)
def f038mcp_f038_market_capitalization_price_per_share_signflip_252d_3d_v115_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in mcap_to_rev (raw count, no price scaling)
def f038mcp_f038_market_capitalization_mcap_to_rev_signflip_63d_3d_v116_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in mcap_to_rev (raw count, no price scaling)
def f038mcp_f038_market_capitalization_mcap_to_rev_signflip_252d_3d_v117_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in mcap_to_asset (raw count, no price scaling)
def f038mcp_f038_market_capitalization_mcap_to_asset_signflip_63d_3d_v118_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in mcap_to_asset (raw count, no price scaling)
def f038mcp_f038_market_capitalization_mcap_to_asset_signflip_252d_3d_v119_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of marketcap_lvl normalized by 252d range
def f038mcp_f038_market_capitalization_marketcap_lvl_rngaccel_63d_r252_3d_v120_signal(marketcap, closeadj):
    base = marketcap
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of marketcap_lvl normalized by 504d range
def f038mcp_f038_market_capitalization_marketcap_lvl_rngaccel_252d_r504_3d_v121_signal(marketcap, closeadj):
    base = marketcap
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_mcap normalized by 252d range
def f038mcp_f038_market_capitalization_log_mcap_rngaccel_63d_r252_3d_v122_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_mcap normalized by 504d range
def f038mcp_f038_market_capitalization_log_mcap_rngaccel_252d_r504_3d_v123_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_yoy normalized by 252d range
def f038mcp_f038_market_capitalization_mcap_yoy_rngaccel_63d_r252_3d_v124_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_yoy normalized by 504d range
def f038mcp_f038_market_capitalization_mcap_yoy_rngaccel_252d_r504_3d_v125_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_qoq normalized by 252d range
def f038mcp_f038_market_capitalization_mcap_qoq_rngaccel_63d_r252_3d_v126_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_qoq normalized by 504d range
def f038mcp_f038_market_capitalization_mcap_qoq_rngaccel_252d_r504_3d_v127_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of price_per_share normalized by 252d range
def f038mcp_f038_market_capitalization_price_per_share_rngaccel_63d_r252_3d_v128_signal(close, closeadj):
    base = close
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of price_per_share normalized by 504d range
def f038mcp_f038_market_capitalization_price_per_share_rngaccel_252d_r504_3d_v129_signal(close, closeadj):
    base = close
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_rev normalized by 252d range
def f038mcp_f038_market_capitalization_mcap_to_rev_rngaccel_63d_r252_3d_v130_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_rev normalized by 504d range
def f038mcp_f038_market_capitalization_mcap_to_rev_rngaccel_252d_r504_3d_v131_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_asset normalized by 252d range
def f038mcp_f038_market_capitalization_mcap_to_asset_rngaccel_63d_r252_3d_v132_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_asset normalized by 504d range
def f038mcp_f038_market_capitalization_mcap_to_asset_rngaccel_252d_r504_3d_v133_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_cumslope_21d_3d_v134_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_cumslope_63d_3d_v135_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_cumslope_252d_3d_v136_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_cumslope_21d_3d_v137_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_cumslope_63d_3d_v138_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_cumslope_252d_3d_v139_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_cumslope_21d_3d_v140_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_cumslope_63d_3d_v141_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_cumslope_252d_3d_v142_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_cumslope_21d_3d_v143_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_cumslope_63d_3d_v144_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_cumslope_252d_3d_v145_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_cumslope_21d_3d_v146_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_cumslope_63d_3d_v147_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_cumslope_252d_3d_v148_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_cumslope_21d_3d_v149_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_cumslope_63d_3d_v150_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

