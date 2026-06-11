"""
68_winner_take_all_signal — Base Features 001-075
Domain: Market share growth proxy
Asset class: US equities | Daily SF1 Fundamentals
Target context: capitulation
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd
from typing import Dict, Any

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────
def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, np.nan)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).std()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w); sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)

# ── Feature functions ────────────────────────────────────────────────────────

def wtas_001_rev_mkt_share_proxy_5d(revenue: pd.Series) -> pd.Series:
    """wtas_001_rev_mkt_share_proxy_5d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(5)

def wtas_002_rev_mkt_share_proxy_21d(revenue: pd.Series) -> pd.Series:
    """wtas_002_rev_mkt_share_proxy_21d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(21)

def wtas_003_rev_mkt_share_proxy_63d(revenue: pd.Series) -> pd.Series:
    """wtas_003_rev_mkt_share_proxy_63d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(63)

def wtas_004_rev_mkt_share_proxy_126d(revenue: pd.Series) -> pd.Series:
    """wtas_004_rev_mkt_share_proxy_126d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(126)

def wtas_005_rev_mkt_share_proxy_252d(revenue: pd.Series) -> pd.Series:
    """wtas_005_rev_mkt_share_proxy_252d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(252)

def wtas_006_mc_mkt_share_proxy_5d(marketcap: pd.Series) -> pd.Series:
    """wtas_006_mc_mkt_share_proxy_5d"""
    return (_safe_div(marketcap, marketcap.rolling(252).sum())).shift(5)

def wtas_007_mc_mkt_share_proxy_21d(marketcap: pd.Series) -> pd.Series:
    """wtas_007_mc_mkt_share_proxy_21d"""
    return (_safe_div(marketcap, marketcap.rolling(252).sum())).shift(21)

def wtas_008_mc_mkt_share_proxy_63d(marketcap: pd.Series) -> pd.Series:
    """wtas_008_mc_mkt_share_proxy_63d"""
    return (_safe_div(marketcap, marketcap.rolling(252).sum())).shift(63)

def wtas_009_mc_mkt_share_proxy_126d(marketcap: pd.Series) -> pd.Series:
    """wtas_009_mc_mkt_share_proxy_126d"""
    return (_safe_div(marketcap, marketcap.rolling(252).sum())).shift(126)

def wtas_010_mc_mkt_share_proxy_252d(marketcap: pd.Series) -> pd.Series:
    """wtas_010_mc_mkt_share_proxy_252d"""
    return (_safe_div(marketcap, marketcap.rolling(252).sum())).shift(252)

def wtas_011_rev_g_rel_5d(revenue: pd.Series) -> pd.Series:
    """wtas_011_rev_g_rel_5d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(5)

def wtas_012_rev_g_rel_21d(revenue: pd.Series) -> pd.Series:
    """wtas_012_rev_g_rel_21d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(21)

def wtas_013_rev_g_rel_63d(revenue: pd.Series) -> pd.Series:
    """wtas_013_rev_g_rel_63d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(63)

def wtas_014_rev_g_rel_126d(revenue: pd.Series) -> pd.Series:
    """wtas_014_rev_g_rel_126d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(126)

def wtas_015_rev_g_rel_252d(revenue: pd.Series) -> pd.Series:
    """wtas_015_rev_g_rel_252d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(252)

def wtas_016_mc_g_rel_5d(marketcap: pd.Series) -> pd.Series:
    """wtas_016_mc_g_rel_5d"""
    return (marketcap.pct_change(252) - _rolling_mean(marketcap.pct_change(252), 1260)).shift(5)

def wtas_017_mc_g_rel_21d(marketcap: pd.Series) -> pd.Series:
    """wtas_017_mc_g_rel_21d"""
    return (marketcap.pct_change(252) - _rolling_mean(marketcap.pct_change(252), 1260)).shift(21)

def wtas_018_mc_g_rel_63d(marketcap: pd.Series) -> pd.Series:
    """wtas_018_mc_g_rel_63d"""
    return (marketcap.pct_change(252) - _rolling_mean(marketcap.pct_change(252), 1260)).shift(63)

def wtas_019_mc_g_rel_126d(marketcap: pd.Series) -> pd.Series:
    """wtas_019_mc_g_rel_126d"""
    return (marketcap.pct_change(252) - _rolling_mean(marketcap.pct_change(252), 1260)).shift(126)

def wtas_020_mc_g_rel_252d(marketcap: pd.Series) -> pd.Series:
    """wtas_020_mc_g_rel_252d"""
    return (marketcap.pct_change(252) - _rolling_mean(marketcap.pct_change(252), 1260)).shift(252)

def wtas_021_winner_index_5d(revenue: pd.Series) -> pd.Series:
    """wtas_021_winner_index_5d"""
    return (_safe_div(revenue.pct_change(252), revenue.pct_change(252).rolling(1260).std())).shift(5)

def wtas_022_winner_index_21d(revenue: pd.Series) -> pd.Series:
    """wtas_022_winner_index_21d"""
    return (_safe_div(revenue.pct_change(252), revenue.pct_change(252).rolling(1260).std())).shift(21)

def wtas_023_winner_index_63d(revenue: pd.Series) -> pd.Series:
    """wtas_023_winner_index_63d"""
    return (_safe_div(revenue.pct_change(252), revenue.pct_change(252).rolling(1260).std())).shift(63)

def wtas_024_winner_index_126d(revenue: pd.Series) -> pd.Series:
    """wtas_024_winner_index_126d"""
    return (_safe_div(revenue.pct_change(252), revenue.pct_change(252).rolling(1260).std())).shift(126)

def wtas_025_winner_index_252d(revenue: pd.Series) -> pd.Series:
    """wtas_025_winner_index_252d"""
    return (_safe_div(revenue.pct_change(252), revenue.pct_change(252).rolling(1260).std())).shift(252)

def wtas_026_dominance_rat_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_026_dominance_rat_5d"""
    return (_safe_div(revenue, assets)).shift(5)

def wtas_027_dominance_rat_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_027_dominance_rat_21d"""
    return (_safe_div(revenue, assets)).shift(21)

def wtas_028_dominance_rat_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_028_dominance_rat_63d"""
    return (_safe_div(revenue, assets)).shift(63)

def wtas_029_dominance_rat_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_029_dominance_rat_126d"""
    return (_safe_div(revenue, assets)).shift(126)

def wtas_030_dominance_rat_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_030_dominance_rat_252d"""
    return (_safe_div(revenue, assets)).shift(252)

def wtas_031_asset_g_rel_5d(assets: pd.Series) -> pd.Series:
    """wtas_031_asset_g_rel_5d"""
    return (assets.pct_change(252) - _rolling_mean(assets.pct_change(252), 1260)).shift(5)

def wtas_032_asset_g_rel_21d(assets: pd.Series) -> pd.Series:
    """wtas_032_asset_g_rel_21d"""
    return (assets.pct_change(252) - _rolling_mean(assets.pct_change(252), 1260)).shift(21)

def wtas_033_asset_g_rel_63d(assets: pd.Series) -> pd.Series:
    """wtas_033_asset_g_rel_63d"""
    return (assets.pct_change(252) - _rolling_mean(assets.pct_change(252), 1260)).shift(63)

def wtas_034_asset_g_rel_126d(assets: pd.Series) -> pd.Series:
    """wtas_034_asset_g_rel_126d"""
    return (assets.pct_change(252) - _rolling_mean(assets.pct_change(252), 1260)).shift(126)

def wtas_035_asset_g_rel_252d(assets: pd.Series) -> pd.Series:
    """wtas_035_asset_g_rel_252d"""
    return (assets.pct_change(252) - _rolling_mean(assets.pct_change(252), 1260)).shift(252)

def wtas_036_rev_acceleration_5d(revenue: pd.Series) -> pd.Series:
    """wtas_036_rev_acceleration_5d"""
    return (revenue.pct_change(252).diff(63)).shift(5)

def wtas_037_rev_acceleration_21d(revenue: pd.Series) -> pd.Series:
    """wtas_037_rev_acceleration_21d"""
    return (revenue.pct_change(252).diff(63)).shift(21)

def wtas_038_rev_acceleration_63d(revenue: pd.Series) -> pd.Series:
    """wtas_038_rev_acceleration_63d"""
    return (revenue.pct_change(252).diff(63)).shift(63)

def wtas_039_rev_acceleration_126d(revenue: pd.Series) -> pd.Series:
    """wtas_039_rev_acceleration_126d"""
    return (revenue.pct_change(252).diff(63)).shift(126)

def wtas_040_rev_acceleration_252d(revenue: pd.Series) -> pd.Series:
    """wtas_040_rev_acceleration_252d"""
    return (revenue.pct_change(252).diff(63)).shift(252)

def wtas_041_mc_acceleration_5d(marketcap: pd.Series) -> pd.Series:
    """wtas_041_mc_acceleration_5d"""
    return (marketcap.pct_change(252).diff(63)).shift(5)

def wtas_042_mc_acceleration_21d(marketcap: pd.Series) -> pd.Series:
    """wtas_042_mc_acceleration_21d"""
    return (marketcap.pct_change(252).diff(63)).shift(21)

def wtas_043_mc_acceleration_63d(marketcap: pd.Series) -> pd.Series:
    """wtas_043_mc_acceleration_63d"""
    return (marketcap.pct_change(252).diff(63)).shift(63)

def wtas_044_mc_acceleration_126d(marketcap: pd.Series) -> pd.Series:
    """wtas_044_mc_acceleration_126d"""
    return (marketcap.pct_change(252).diff(63)).shift(126)

def wtas_045_mc_acceleration_252d(marketcap: pd.Series) -> pd.Series:
    """wtas_045_mc_acceleration_252d"""
    return (marketcap.pct_change(252).diff(63)).shift(252)

def wtas_046_network_effect_proxy_5d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_046_network_effect_proxy_5d"""
    return (_safe_div(revenue, marketcap).diff(252)).shift(5)

def wtas_047_network_effect_proxy_21d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_047_network_effect_proxy_21d"""
    return (_safe_div(revenue, marketcap).diff(252)).shift(21)

def wtas_048_network_effect_proxy_63d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_048_network_effect_proxy_63d"""
    return (_safe_div(revenue, marketcap).diff(252)).shift(63)

def wtas_049_network_effect_proxy_126d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_049_network_effect_proxy_126d"""
    return (_safe_div(revenue, marketcap).diff(252)).shift(126)

def wtas_050_network_effect_proxy_252d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_050_network_effect_proxy_252d"""
    return (_safe_div(revenue, marketcap).diff(252)).shift(252)

def wtas_051_winner_take_all_z_5d(revenue: pd.Series) -> pd.Series:
    """wtas_051_winner_take_all_z_5d"""
    return (_zscore_rolling(revenue, 1260)).shift(5)

def wtas_052_winner_take_all_z_21d(revenue: pd.Series) -> pd.Series:
    """wtas_052_winner_take_all_z_21d"""
    return (_zscore_rolling(revenue, 1260)).shift(21)

def wtas_053_winner_take_all_z_63d(revenue: pd.Series) -> pd.Series:
    """wtas_053_winner_take_all_z_63d"""
    return (_zscore_rolling(revenue, 1260)).shift(63)

def wtas_054_winner_take_all_z_126d(revenue: pd.Series) -> pd.Series:
    """wtas_054_winner_take_all_z_126d"""
    return (_zscore_rolling(revenue, 1260)).shift(126)

def wtas_055_winner_take_all_z_252d(revenue: pd.Series) -> pd.Series:
    """wtas_055_winner_take_all_z_252d"""
    return (_zscore_rolling(revenue, 1260)).shift(252)

def wtas_056_market_cap_concentration_5d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_056_market_cap_concentration_5d"""
    return (_safe_div(marketcap, assets)).shift(5)

def wtas_057_market_cap_concentration_21d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_057_market_cap_concentration_21d"""
    return (_safe_div(marketcap, assets)).shift(21)

def wtas_058_market_cap_concentration_63d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_058_market_cap_concentration_63d"""
    return (_safe_div(marketcap, assets)).shift(63)

def wtas_059_market_cap_concentration_126d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_059_market_cap_concentration_126d"""
    return (_safe_div(marketcap, assets)).shift(126)

def wtas_060_market_cap_concentration_252d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_060_market_cap_concentration_252d"""
    return (_safe_div(marketcap, assets)).shift(252)

def wtas_061_rev_per_asset_g_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_061_rev_per_asset_g_5d"""
    return ((_safe_div(revenue, assets)).pct_change(252)).shift(5)

def wtas_062_rev_per_asset_g_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_062_rev_per_asset_g_21d"""
    return ((_safe_div(revenue, assets)).pct_change(252)).shift(21)

def wtas_063_rev_per_asset_g_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_063_rev_per_asset_g_63d"""
    return ((_safe_div(revenue, assets)).pct_change(252)).shift(63)

def wtas_064_rev_per_asset_g_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_064_rev_per_asset_g_126d"""
    return ((_safe_div(revenue, assets)).pct_change(252)).shift(126)

def wtas_065_rev_per_asset_g_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_065_rev_per_asset_g_252d"""
    return ((_safe_div(revenue, assets)).pct_change(252)).shift(252)

def wtas_066_mc_per_asset_g_5d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_066_mc_per_asset_g_5d"""
    return ((_safe_div(marketcap, assets)).pct_change(252)).shift(5)

def wtas_067_mc_per_asset_g_21d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_067_mc_per_asset_g_21d"""
    return ((_safe_div(marketcap, assets)).pct_change(252)).shift(21)

def wtas_068_mc_per_asset_g_63d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_068_mc_per_asset_g_63d"""
    return ((_safe_div(marketcap, assets)).pct_change(252)).shift(63)

def wtas_069_mc_per_asset_g_126d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_069_mc_per_asset_g_126d"""
    return ((_safe_div(marketcap, assets)).pct_change(252)).shift(126)

def wtas_070_mc_per_asset_g_252d(assets: pd.Series, marketcap: pd.Series) -> pd.Series:
    """wtas_070_mc_per_asset_g_252d"""
    return ((_safe_div(marketcap, assets)).pct_change(252)).shift(252)

def wtas_071_dominance_persistence_5d(revenue: pd.Series) -> pd.Series:
    """wtas_071_dominance_persistence_5d"""
    return _safe_div(revenue, revenue.shift(252))

def wtas_072_dominance_persistence_21d(revenue: pd.Series) -> pd.Series:
    """wtas_072_dominance_persistence_21d"""
    return _safe_div(revenue, revenue.shift(252))

def wtas_073_dominance_persistence_63d(revenue: pd.Series) -> pd.Series:
    """wtas_073_dominance_persistence_63d"""
    return _safe_div(revenue, revenue.shift(252))

def wtas_074_dominance_persistence_126d(revenue: pd.Series) -> pd.Series:
    """wtas_074_dominance_persistence_126d"""
    return _safe_div(revenue, revenue.shift(252))

def wtas_075_dominance_persistence_252d(revenue: pd.Series) -> pd.Series:
    """wtas_075_dominance_persistence_252d"""
    return _safe_div(revenue, revenue.shift(252))

# ── Registry ──────────────────────────────────────────────────────────────────
V68_REGISTRY = {
    "wtas_001_rev_mkt_share_proxy_5d": {"inputs": ['revenue'], "func": wtas_001_rev_mkt_share_proxy_5d},
    "wtas_002_rev_mkt_share_proxy_21d": {"inputs": ['revenue'], "func": wtas_002_rev_mkt_share_proxy_21d},
    "wtas_003_rev_mkt_share_proxy_63d": {"inputs": ['revenue'], "func": wtas_003_rev_mkt_share_proxy_63d},
    "wtas_004_rev_mkt_share_proxy_126d": {"inputs": ['revenue'], "func": wtas_004_rev_mkt_share_proxy_126d},
    "wtas_005_rev_mkt_share_proxy_252d": {"inputs": ['revenue'], "func": wtas_005_rev_mkt_share_proxy_252d},
    "wtas_006_mc_mkt_share_proxy_5d": {"inputs": ['marketcap'], "func": wtas_006_mc_mkt_share_proxy_5d},
    "wtas_007_mc_mkt_share_proxy_21d": {"inputs": ['marketcap'], "func": wtas_007_mc_mkt_share_proxy_21d},
    "wtas_008_mc_mkt_share_proxy_63d": {"inputs": ['marketcap'], "func": wtas_008_mc_mkt_share_proxy_63d},
    "wtas_009_mc_mkt_share_proxy_126d": {"inputs": ['marketcap'], "func": wtas_009_mc_mkt_share_proxy_126d},
    "wtas_010_mc_mkt_share_proxy_252d": {"inputs": ['marketcap'], "func": wtas_010_mc_mkt_share_proxy_252d},
    "wtas_011_rev_g_rel_5d": {"inputs": ['revenue'], "func": wtas_011_rev_g_rel_5d},
    "wtas_012_rev_g_rel_21d": {"inputs": ['revenue'], "func": wtas_012_rev_g_rel_21d},
    "wtas_013_rev_g_rel_63d": {"inputs": ['revenue'], "func": wtas_013_rev_g_rel_63d},
    "wtas_014_rev_g_rel_126d": {"inputs": ['revenue'], "func": wtas_014_rev_g_rel_126d},
    "wtas_015_rev_g_rel_252d": {"inputs": ['revenue'], "func": wtas_015_rev_g_rel_252d},
    "wtas_016_mc_g_rel_5d": {"inputs": ['marketcap'], "func": wtas_016_mc_g_rel_5d},
    "wtas_017_mc_g_rel_21d": {"inputs": ['marketcap'], "func": wtas_017_mc_g_rel_21d},
    "wtas_018_mc_g_rel_63d": {"inputs": ['marketcap'], "func": wtas_018_mc_g_rel_63d},
    "wtas_019_mc_g_rel_126d": {"inputs": ['marketcap'], "func": wtas_019_mc_g_rel_126d},
    "wtas_020_mc_g_rel_252d": {"inputs": ['marketcap'], "func": wtas_020_mc_g_rel_252d},
    "wtas_021_winner_index_5d": {"inputs": ['revenue'], "func": wtas_021_winner_index_5d},
    "wtas_022_winner_index_21d": {"inputs": ['revenue'], "func": wtas_022_winner_index_21d},
    "wtas_023_winner_index_63d": {"inputs": ['revenue'], "func": wtas_023_winner_index_63d},
    "wtas_024_winner_index_126d": {"inputs": ['revenue'], "func": wtas_024_winner_index_126d},
    "wtas_025_winner_index_252d": {"inputs": ['revenue'], "func": wtas_025_winner_index_252d},
    "wtas_026_dominance_rat_5d": {"inputs": ['revenue', 'assets'], "func": wtas_026_dominance_rat_5d},
    "wtas_027_dominance_rat_21d": {"inputs": ['revenue', 'assets'], "func": wtas_027_dominance_rat_21d},
    "wtas_028_dominance_rat_63d": {"inputs": ['revenue', 'assets'], "func": wtas_028_dominance_rat_63d},
    "wtas_029_dominance_rat_126d": {"inputs": ['revenue', 'assets'], "func": wtas_029_dominance_rat_126d},
    "wtas_030_dominance_rat_252d": {"inputs": ['revenue', 'assets'], "func": wtas_030_dominance_rat_252d},
    "wtas_031_asset_g_rel_5d": {"inputs": ['assets'], "func": wtas_031_asset_g_rel_5d},
    "wtas_032_asset_g_rel_21d": {"inputs": ['assets'], "func": wtas_032_asset_g_rel_21d},
    "wtas_033_asset_g_rel_63d": {"inputs": ['assets'], "func": wtas_033_asset_g_rel_63d},
    "wtas_034_asset_g_rel_126d": {"inputs": ['assets'], "func": wtas_034_asset_g_rel_126d},
    "wtas_035_asset_g_rel_252d": {"inputs": ['assets'], "func": wtas_035_asset_g_rel_252d},
    "wtas_036_rev_acceleration_5d": {"inputs": ['revenue'], "func": wtas_036_rev_acceleration_5d},
    "wtas_037_rev_acceleration_21d": {"inputs": ['revenue'], "func": wtas_037_rev_acceleration_21d},
    "wtas_038_rev_acceleration_63d": {"inputs": ['revenue'], "func": wtas_038_rev_acceleration_63d},
    "wtas_039_rev_acceleration_126d": {"inputs": ['revenue'], "func": wtas_039_rev_acceleration_126d},
    "wtas_040_rev_acceleration_252d": {"inputs": ['revenue'], "func": wtas_040_rev_acceleration_252d},
    "wtas_041_mc_acceleration_5d": {"inputs": ['marketcap'], "func": wtas_041_mc_acceleration_5d},
    "wtas_042_mc_acceleration_21d": {"inputs": ['marketcap'], "func": wtas_042_mc_acceleration_21d},
    "wtas_043_mc_acceleration_63d": {"inputs": ['marketcap'], "func": wtas_043_mc_acceleration_63d},
    "wtas_044_mc_acceleration_126d": {"inputs": ['marketcap'], "func": wtas_044_mc_acceleration_126d},
    "wtas_045_mc_acceleration_252d": {"inputs": ['marketcap'], "func": wtas_045_mc_acceleration_252d},
    "wtas_046_network_effect_proxy_5d": {"inputs": ['revenue', 'marketcap'], "func": wtas_046_network_effect_proxy_5d},
    "wtas_047_network_effect_proxy_21d": {"inputs": ['revenue', 'marketcap'], "func": wtas_047_network_effect_proxy_21d},
    "wtas_048_network_effect_proxy_63d": {"inputs": ['revenue', 'marketcap'], "func": wtas_048_network_effect_proxy_63d},
    "wtas_049_network_effect_proxy_126d": {"inputs": ['revenue', 'marketcap'], "func": wtas_049_network_effect_proxy_126d},
    "wtas_050_network_effect_proxy_252d": {"inputs": ['revenue', 'marketcap'], "func": wtas_050_network_effect_proxy_252d},
    "wtas_051_winner_take_all_z_5d": {"inputs": ['revenue'], "func": wtas_051_winner_take_all_z_5d},
    "wtas_052_winner_take_all_z_21d": {"inputs": ['revenue'], "func": wtas_052_winner_take_all_z_21d},
    "wtas_053_winner_take_all_z_63d": {"inputs": ['revenue'], "func": wtas_053_winner_take_all_z_63d},
    "wtas_054_winner_take_all_z_126d": {"inputs": ['revenue'], "func": wtas_054_winner_take_all_z_126d},
    "wtas_055_winner_take_all_z_252d": {"inputs": ['revenue'], "func": wtas_055_winner_take_all_z_252d},
    "wtas_056_market_cap_concentration_5d": {"inputs": ['assets', 'marketcap'], "func": wtas_056_market_cap_concentration_5d},
    "wtas_057_market_cap_concentration_21d": {"inputs": ['assets', 'marketcap'], "func": wtas_057_market_cap_concentration_21d},
    "wtas_058_market_cap_concentration_63d": {"inputs": ['assets', 'marketcap'], "func": wtas_058_market_cap_concentration_63d},
    "wtas_059_market_cap_concentration_126d": {"inputs": ['assets', 'marketcap'], "func": wtas_059_market_cap_concentration_126d},
    "wtas_060_market_cap_concentration_252d": {"inputs": ['assets', 'marketcap'], "func": wtas_060_market_cap_concentration_252d},
    "wtas_061_rev_per_asset_g_5d": {"inputs": ['revenue', 'assets'], "func": wtas_061_rev_per_asset_g_5d},
    "wtas_062_rev_per_asset_g_21d": {"inputs": ['revenue', 'assets'], "func": wtas_062_rev_per_asset_g_21d},
    "wtas_063_rev_per_asset_g_63d": {"inputs": ['revenue', 'assets'], "func": wtas_063_rev_per_asset_g_63d},
    "wtas_064_rev_per_asset_g_126d": {"inputs": ['revenue', 'assets'], "func": wtas_064_rev_per_asset_g_126d},
    "wtas_065_rev_per_asset_g_252d": {"inputs": ['revenue', 'assets'], "func": wtas_065_rev_per_asset_g_252d},
    "wtas_066_mc_per_asset_g_5d": {"inputs": ['assets', 'marketcap'], "func": wtas_066_mc_per_asset_g_5d},
    "wtas_067_mc_per_asset_g_21d": {"inputs": ['assets', 'marketcap'], "func": wtas_067_mc_per_asset_g_21d},
    "wtas_068_mc_per_asset_g_63d": {"inputs": ['assets', 'marketcap'], "func": wtas_068_mc_per_asset_g_63d},
    "wtas_069_mc_per_asset_g_126d": {"inputs": ['assets', 'marketcap'], "func": wtas_069_mc_per_asset_g_126d},
    "wtas_070_mc_per_asset_g_252d": {"inputs": ['assets', 'marketcap'], "func": wtas_070_mc_per_asset_g_252d},
    "wtas_071_dominance_persistence_5d": {"inputs": ['revenue'], "func": wtas_071_dominance_persistence_5d},
    "wtas_072_dominance_persistence_21d": {"inputs": ['revenue'], "func": wtas_072_dominance_persistence_21d},
    "wtas_073_dominance_persistence_63d": {"inputs": ['revenue'], "func": wtas_073_dominance_persistence_63d},
    "wtas_074_dominance_persistence_126d": {"inputs": ['revenue'], "func": wtas_074_dominance_persistence_126d},
    "wtas_075_dominance_persistence_252d": {"inputs": ['revenue'], "func": wtas_075_dominance_persistence_252d},
}
