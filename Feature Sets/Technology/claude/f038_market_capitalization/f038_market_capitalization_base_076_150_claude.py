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


# 63d z-score of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_z_63d_base_v076_signal(marketcap, closeadj):
    base = marketcap
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_z_126d_base_v077_signal(marketcap, closeadj):
    base = marketcap
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_z_252d_base_v078_signal(marketcap, closeadj):
    base = marketcap
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_z_504d_base_v079_signal(marketcap, closeadj):
    base = marketcap
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_z_63d_base_v080_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_z_126d_base_v081_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_z_252d_base_v082_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_z_504d_base_v083_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_z_63d_base_v084_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_z_126d_base_v085_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_z_252d_base_v086_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_z_504d_base_v087_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_z_63d_base_v088_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_z_126d_base_v089_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_z_252d_base_v090_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_z_504d_base_v091_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_z_63d_base_v092_signal(close, closeadj):
    base = close
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_z_126d_base_v093_signal(close, closeadj):
    base = close
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_z_252d_base_v094_signal(close, closeadj):
    base = close
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_z_504d_base_v095_signal(close, closeadj):
    base = close
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_z_63d_base_v096_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_z_126d_base_v097_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_z_252d_base_v098_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_z_504d_base_v099_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_z_63d_base_v100_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_z_126d_base_v101_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_z_252d_base_v102_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_z_504d_base_v103_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_distmax_252d_base_v104_signal(marketcap, closeadj):
    base = marketcap
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_distmax_504d_base_v105_signal(marketcap, closeadj):
    base = marketcap
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_distmax_252d_base_v106_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_distmax_504d_base_v107_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_distmax_252d_base_v108_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_distmax_504d_base_v109_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_distmax_252d_base_v110_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_distmax_504d_base_v111_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_distmax_252d_base_v112_signal(close, closeadj):
    base = close
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_distmax_504d_base_v113_signal(close, closeadj):
    base = close
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_distmax_252d_base_v114_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_distmax_504d_base_v115_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_distmax_252d_base_v116_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_distmax_504d_base_v117_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_distmed_126d_base_v118_signal(marketcap, closeadj):
    base = marketcap
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_distmed_252d_base_v119_signal(marketcap, closeadj):
    base = marketcap
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_distmed_504d_base_v120_signal(marketcap, closeadj):
    base = marketcap
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_distmed_126d_base_v121_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_distmed_252d_base_v122_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of log_mcap
def f038mcp_f038_market_capitalization_log_mcap_distmed_504d_base_v123_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_distmed_126d_base_v124_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_distmed_252d_base_v125_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_distmed_504d_base_v126_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_distmed_126d_base_v127_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_distmed_252d_base_v128_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_distmed_504d_base_v129_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_distmed_126d_base_v130_signal(close, closeadj):
    base = close
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_distmed_252d_base_v131_signal(close, closeadj):
    base = close
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of price_per_share
def f038mcp_f038_market_capitalization_price_per_share_distmed_504d_base_v132_signal(close, closeadj):
    base = close
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_distmed_126d_base_v133_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_distmed_252d_base_v134_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_distmed_504d_base_v135_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_distmed_126d_base_v136_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_distmed_252d_base_v137_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of mcap_to_asset
def f038mcp_f038_market_capitalization_mcap_to_asset_distmed_504d_base_v138_signal(marketcap, assets, closeadj):
    base = marketcap / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_chg_63d_base_v139_signal(marketcap, closeadj):
    base = marketcap
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in marketcap_lvl
def f038mcp_f038_market_capitalization_marketcap_lvl_chg_252d_base_v140_signal(marketcap, closeadj):
    base = marketcap
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in log_mcap
def f038mcp_f038_market_capitalization_log_mcap_chg_63d_base_v141_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in log_mcap
def f038mcp_f038_market_capitalization_log_mcap_chg_252d_base_v142_signal(marketcap, closeadj):
    base = _f038_logmc(marketcap)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_chg_63d_base_v143_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in mcap_yoy
def f038mcp_f038_market_capitalization_mcap_yoy_chg_252d_base_v144_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_chg_63d_base_v145_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in mcap_qoq
def f038mcp_f038_market_capitalization_mcap_qoq_chg_252d_base_v146_signal(marketcap, closeadj):
    base = marketcap.pct_change(periods=63)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in price_per_share
def f038mcp_f038_market_capitalization_price_per_share_chg_63d_base_v147_signal(close, closeadj):
    base = close
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in price_per_share
def f038mcp_f038_market_capitalization_price_per_share_chg_252d_base_v148_signal(close, closeadj):
    base = close
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_chg_63d_base_v149_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in mcap_to_rev
def f038mcp_f038_market_capitalization_mcap_to_rev_chg_252d_base_v150_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

