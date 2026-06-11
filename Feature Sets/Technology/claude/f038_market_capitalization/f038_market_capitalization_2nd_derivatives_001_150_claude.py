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


# 21d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slope_21d_2d_v001_signal(marketcap, closeadj):
    base = marketcap
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slope_63d_2d_v002_signal(marketcap, closeadj):
    base = marketcap
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slope_126d_2d_v003_signal(marketcap, closeadj):
    base = marketcap
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slope_252d_2d_v004_signal(marketcap, closeadj):
    base = marketcap
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_slope_504d_2d_v005_signal(marketcap, closeadj):
    base = marketcap
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slope_21d_2d_v006_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slope_63d_2d_v007_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slope_126d_2d_v008_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slope_252d_2d_v009_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_slope_504d_2d_v010_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slope_21d_2d_v011_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slope_63d_2d_v012_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slope_126d_2d_v013_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slope_252d_2d_v014_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_slope_504d_2d_v015_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slope_21d_2d_v016_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slope_63d_2d_v017_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slope_126d_2d_v018_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slope_252d_2d_v019_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_slope_504d_2d_v020_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slope_21d_2d_v021_signal(close, closeadj):
    base = close
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slope_63d_2d_v022_signal(close, closeadj):
    base = close
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slope_126d_2d_v023_signal(close, closeadj):
    base = close
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slope_252d_2d_v024_signal(close, closeadj):
    base = close
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_slope_504d_2d_v025_signal(close, closeadj):
    base = close
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slope_21d_2d_v026_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slope_63d_2d_v027_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slope_126d_2d_v028_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slope_252d_2d_v029_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_slope_504d_2d_v030_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slope_21d_2d_v031_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slope_63d_2d_v032_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slope_126d_2d_v033_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slope_252d_2d_v034_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_slope_504d_2d_v035_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_sm21_sl21_2d_v036_signal(marketcap, closeadj):
    base = _mean(marketcap, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_sm63_sl21_2d_v037_signal(marketcap, closeadj):
    base = _mean(marketcap, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_sm63_sl63_2d_v038_signal(marketcap, closeadj):
    base = _mean(marketcap, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_sm252_sl63_2d_v039_signal(marketcap, closeadj):
    base = _mean(marketcap, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_sm252_sl126_2d_v040_signal(marketcap, closeadj):
    base = _mean(marketcap, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_sm21_sl21_2d_v041_signal(marketcap, closeadj):
    base = _mean(_f038_logmc(marketcap), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_sm63_sl21_2d_v042_signal(marketcap, closeadj):
    base = _mean(_f038_logmc(marketcap), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_sm63_sl63_2d_v043_signal(marketcap, closeadj):
    base = _mean(_f038_logmc(marketcap), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_sm252_sl63_2d_v044_signal(marketcap, closeadj):
    base = _mean(_f038_logmc(marketcap), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_sm252_sl126_2d_v045_signal(marketcap, closeadj):
    base = _mean(_f038_logmc(marketcap), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_sm21_sl21_2d_v046_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_sm63_sl21_2d_v047_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_sm63_sl63_2d_v048_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_sm252_sl63_2d_v049_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_sm252_sl126_2d_v050_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_sm21_sl21_2d_v051_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_sm63_sl21_2d_v052_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_sm63_sl63_2d_v053_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_sm252_sl63_2d_v054_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_sm252_sl126_2d_v055_signal(marketcap, closeadj):
    base = _mean(marketcap.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_sm21_sl21_2d_v056_signal(close, closeadj):
    base = _mean(close, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_sm63_sl21_2d_v057_signal(close, closeadj):
    base = _mean(close, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_sm63_sl63_2d_v058_signal(close, closeadj):
    base = _mean(close, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_sm252_sl63_2d_v059_signal(close, closeadj):
    base = _mean(close, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_sm252_sl126_2d_v060_signal(close, closeadj):
    base = _mean(close, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_sm21_sl21_2d_v061_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_sm63_sl21_2d_v062_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_sm63_sl63_2d_v063_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_sm252_sl63_2d_v064_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_sm252_sl126_2d_v065_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_sm21_sl21_2d_v066_signal(marketcap, assets, closeadj):
    base = _mean(marketcap / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_sm63_sl21_2d_v067_signal(marketcap, assets, closeadj):
    base = _mean(marketcap / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_sm63_sl63_2d_v068_signal(marketcap, assets, closeadj):
    base = _mean(marketcap / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_sm252_sl63_2d_v069_signal(marketcap, assets, closeadj):
    base = _mean(marketcap / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_sm252_sl126_2d_v070_signal(marketcap, assets, closeadj):
    base = _mean(marketcap / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_pctslope_21d_2d_v071_signal(marketcap, closeadj):
    base = marketcap
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_pctslope_63d_2d_v072_signal(marketcap, closeadj):
    base = marketcap
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_pctslope_252d_2d_v073_signal(marketcap, closeadj):
    base = marketcap
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_pctslope_21d_2d_v074_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_pctslope_63d_2d_v075_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_pctslope_252d_2d_v076_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_pctslope_21d_2d_v077_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_pctslope_63d_2d_v078_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_pctslope_252d_2d_v079_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_pctslope_21d_2d_v080_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_pctslope_63d_2d_v081_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_pctslope_252d_2d_v082_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_pctslope_21d_2d_v083_signal(close, closeadj):
    base = close
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_pctslope_63d_2d_v084_signal(close, closeadj):
    base = close
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_pctslope_252d_2d_v085_signal(close, closeadj):
    base = close
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_pctslope_21d_2d_v086_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_pctslope_63d_2d_v087_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_pctslope_252d_2d_v088_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_pctslope_21d_2d_v089_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_pctslope_63d_2d_v090_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_pctslope_252d_2d_v091_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_sgnslope_21d_2d_v092_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_sgnslope_63d_2d_v093_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_sgnslope_252d_2d_v094_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_sgnslope_21d_2d_v095_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_sgnslope_63d_2d_v096_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_sgnslope_252d_2d_v097_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_sgnslope_21d_2d_v098_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_sgnslope_63d_2d_v099_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_sgnslope_252d_2d_v100_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_sgnslope_21d_2d_v101_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_sgnslope_63d_2d_v102_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_sgnslope_252d_2d_v103_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_sgnslope_21d_2d_v104_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_sgnslope_63d_2d_v105_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_sgnslope_252d_2d_v106_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_sgnslope_21d_2d_v107_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_sgnslope_63d_2d_v108_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_sgnslope_252d_2d_v109_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_sgnslope_21d_2d_v110_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_sgnslope_63d_2d_v111_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_sgnslope_252d_2d_v112_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_logmagslope_21d_2d_v113_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_logmagslope_63d_2d_v114_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_logmagslope_252d_2d_v115_signal(marketcap, closeadj):
    base = marketcap
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_logmagslope_21d_2d_v116_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_logmagslope_63d_2d_v117_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_logmagslope_252d_2d_v118_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_logmagslope_21d_2d_v119_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_logmagslope_63d_2d_v120_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_logmagslope_252d_2d_v121_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_logmagslope_21d_2d_v122_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_logmagslope_63d_2d_v123_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_logmagslope_252d_2d_v124_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_logmagslope_21d_2d_v125_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_logmagslope_63d_2d_v126_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_logmagslope_252d_2d_v127_signal(close, closeadj):
    base = close
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_logmagslope_21d_2d_v128_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_logmagslope_63d_2d_v129_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_logmagslope_252d_2d_v130_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_logmagslope_21d_2d_v131_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_logmagslope_63d_2d_v132_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_logmagslope_252d_2d_v133_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|marketcap_lvl|
def f038mcp_f038_market_capitalization_marketcap_lvl_logslope_63d_2d_v134_signal(marketcap, closeadj):
    base = np.log((marketcap).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|marketcap_lvl|
def f038mcp_f038_market_capitalization_marketcap_lvl_logslope_252d_2d_v135_signal(marketcap, closeadj):
    base = np.log((marketcap).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|log_mcap|
def f038mcp_f038_market_capitalization_log_mcap_logslope_63d_2d_v136_signal(marketcap, closeadj):
    base = np.log((_f038_logmc(marketcap)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|log_mcap|
def f038mcp_f038_market_capitalization_log_mcap_logslope_252d_2d_v137_signal(marketcap, closeadj):
    base = np.log((_f038_logmc(marketcap)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|mcap_yoy|
def f038mcp_f038_market_capitalization_mcap_yoy_logslope_63d_2d_v138_signal(marketcap, closeadj):
    base = np.log((marketcap.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|mcap_yoy|
def f038mcp_f038_market_capitalization_mcap_yoy_logslope_252d_2d_v139_signal(marketcap, closeadj):
    base = np.log((marketcap.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|mcap_qoq|
def f038mcp_f038_market_capitalization_mcap_qoq_logslope_63d_2d_v140_signal(marketcap, closeadj):
    base = np.log((marketcap.pct_change(periods=63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|mcap_qoq|
def f038mcp_f038_market_capitalization_mcap_qoq_logslope_252d_2d_v141_signal(marketcap, closeadj):
    base = np.log((marketcap.pct_change(periods=63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|price_per_share|
def f038mcp_f038_market_capitalization_price_per_share_logslope_63d_2d_v142_signal(close, closeadj):
    base = np.log((close).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|price_per_share|
def f038mcp_f038_market_capitalization_price_per_share_logslope_252d_2d_v143_signal(close, closeadj):
    base = np.log((close).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|mcap_to_rev|
def f038mcp_f038_market_capitalization_mcap_to_rev_logslope_63d_2d_v144_signal(marketcap, revenue, closeadj):
    base = np.log((marketcap / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|mcap_to_rev|
def f038mcp_f038_market_capitalization_mcap_to_rev_logslope_252d_2d_v145_signal(marketcap, revenue, closeadj):
    base = np.log((marketcap / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|mcap_to_asset|
def f038mcp_f038_market_capitalization_mcap_to_asset_logslope_63d_2d_v146_signal(marketcap, assets, closeadj):
    base = np.log((marketcap / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|mcap_to_asset|
def f038mcp_f038_market_capitalization_mcap_to_asset_logslope_252d_2d_v147_signal(marketcap, assets, closeadj):
    base = np.log((marketcap / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

