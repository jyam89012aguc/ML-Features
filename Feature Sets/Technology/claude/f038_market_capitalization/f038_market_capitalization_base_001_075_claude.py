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
def _f038_logmc(marketcap):
    return np.log(marketcap.abs().replace(0, np.nan))


# 21d mean of marketcap_lvl scaled by closeadj
def f038mcp_f038_market_capitalization_marketcap_lvl_mean_21d_base_v001_signal(marketcap, closeadj):
    base = marketcap
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of marketcap_lvl scaled by closeadj
def f038mcp_f038_market_capitalization_marketcap_lvl_mean_63d_base_v002_signal(marketcap, closeadj):
    base = marketcap
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of marketcap_lvl scaled by closeadj
def f038mcp_f038_market_capitalization_marketcap_lvl_mean_126d_base_v003_signal(marketcap, closeadj):
    base = marketcap
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of marketcap_lvl scaled by closeadj
def f038mcp_f038_market_capitalization_marketcap_lvl_mean_252d_base_v004_signal(marketcap, closeadj):
    base = marketcap
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of marketcap_lvl scaled by closeadj
def f038mcp_f038_market_capitalization_marketcap_lvl_mean_504d_base_v005_signal(marketcap, closeadj):
    base = marketcap
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of log_mcap scaled by closeadj
def f038mcp_f038_market_capitalization_log_mcap_mean_21d_base_v006_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of log_mcap scaled by closeadj
def f038mcp_f038_market_capitalization_log_mcap_mean_63d_base_v007_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of log_mcap scaled by closeadj
def f038mcp_f038_market_capitalization_log_mcap_mean_126d_base_v008_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of log_mcap scaled by closeadj
def f038mcp_f038_market_capitalization_log_mcap_mean_252d_base_v009_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of log_mcap scaled by closeadj
def f038mcp_f038_market_capitalization_log_mcap_mean_504d_base_v010_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of mcap_yoy scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_yoy_mean_21d_base_v011_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_yoy scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_yoy_mean_63d_base_v012_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_yoy scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_yoy_mean_126d_base_v013_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_yoy scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_yoy_mean_252d_base_v014_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_yoy scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_yoy_mean_504d_base_v015_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of mcap_qoq scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_qoq_mean_21d_base_v016_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_qoq scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_qoq_mean_63d_base_v017_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_qoq scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_qoq_mean_126d_base_v018_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_qoq scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_qoq_mean_252d_base_v019_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_qoq scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_qoq_mean_504d_base_v020_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of price_per_share scaled by closeadj
def f038mcp_f038_market_capitalization_price_per_share_mean_21d_base_v021_signal(close, closeadj):
    base = close
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of price_per_share scaled by closeadj
def f038mcp_f038_market_capitalization_price_per_share_mean_63d_base_v022_signal(close, closeadj):
    base = close
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of price_per_share scaled by closeadj
def f038mcp_f038_market_capitalization_price_per_share_mean_126d_base_v023_signal(close, closeadj):
    base = close
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of price_per_share scaled by closeadj
def f038mcp_f038_market_capitalization_price_per_share_mean_252d_base_v024_signal(close, closeadj):
    base = close
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of price_per_share scaled by closeadj
def f038mcp_f038_market_capitalization_price_per_share_mean_504d_base_v025_signal(close, closeadj):
    base = close
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of mcap_to_rev scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_rev_mean_21d_base_v026_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_to_rev scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_rev_mean_63d_base_v027_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_to_rev scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_rev_mean_126d_base_v028_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_to_rev scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_rev_mean_252d_base_v029_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_to_rev scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_rev_mean_504d_base_v030_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of mcap_to_asset scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_asset_mean_21d_base_v031_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_to_asset scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_asset_mean_63d_base_v032_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_to_asset scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_asset_mean_126d_base_v033_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_to_asset scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_asset_mean_252d_base_v034_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_to_asset scaled by closeadj
def f038mcp_f038_market_capitalization_mcap_to_asset_mean_504d_base_v035_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_median_63d_base_v036_signal(marketcap, closeadj):
    base = marketcap
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_median_252d_base_v037_signal(marketcap, closeadj):
    base = marketcap
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_median_504d_base_v038_signal(marketcap, closeadj):
    base = marketcap
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_median_63d_base_v039_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_median_252d_base_v040_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_median_504d_base_v041_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_median_63d_base_v042_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_median_252d_base_v043_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_median_504d_base_v044_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_median_63d_base_v045_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_median_252d_base_v046_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_median_504d_base_v047_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_median_63d_base_v048_signal(close, closeadj):
    base = close
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_median_252d_base_v049_signal(close, closeadj):
    base = close
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_median_504d_base_v050_signal(close, closeadj):
    base = close
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_median_63d_base_v051_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_median_252d_base_v052_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_median_504d_base_v053_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_median_63d_base_v054_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_median_252d_base_v055_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_median_504d_base_v056_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_rmax_252d_base_v057_signal(marketcap, closeadj):
    base = marketcap
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_rmax_504d_base_v058_signal(marketcap, closeadj):
    base = marketcap
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_rmax_252d_base_v059_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_rmax_504d_base_v060_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_rmax_252d_base_v061_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_rmax_504d_base_v062_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_rmax_252d_base_v063_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_rmax_504d_base_v064_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_rmax_252d_base_v065_signal(close, closeadj):
    base = close
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_rmax_504d_base_v066_signal(close, closeadj):
    base = close
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_rmax_252d_base_v067_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_rmax_504d_base_v068_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_rmax_252d_base_v069_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_rmax_504d_base_v070_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_rmin_252d_base_v071_signal(marketcap, closeadj):
    base = marketcap
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_rmin_504d_base_v072_signal(marketcap, closeadj):
    base = marketcap
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_rmin_252d_base_v073_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_rmin_504d_base_v074_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_rmin_252d_base_v075_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

