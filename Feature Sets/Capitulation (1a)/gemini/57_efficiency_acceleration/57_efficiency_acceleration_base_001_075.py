"""
57_efficiency_acceleration — Base Features 001-075
Domain: efficiency_acceleration
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def effa_001_asset_turnover_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_001_asset_turnover_lvl_5d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 5)

def effa_002_asset_turnover_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_002_asset_turnover_zscore_5d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 5)

def effa_003_asset_turnover_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_003_asset_turnover_rank_5d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 5)

def effa_004_asset_turnover_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_004_asset_turnover_lvl_21d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 21)

def effa_005_asset_turnover_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_005_asset_turnover_zscore_21d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 21)

def effa_006_asset_turnover_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_006_asset_turnover_rank_21d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 21)

def effa_007_asset_turnover_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_007_asset_turnover_lvl_63d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 63)

def effa_008_asset_turnover_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_008_asset_turnover_zscore_63d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 63)

def effa_009_asset_turnover_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_009_asset_turnover_rank_63d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 63)

def effa_010_asset_turnover_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_010_asset_turnover_lvl_126d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 126)

def effa_011_asset_turnover_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_011_asset_turnover_zscore_126d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 126)

def effa_012_asset_turnover_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_012_asset_turnover_rank_126d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 126)

def effa_013_asset_turnover_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_013_asset_turnover_lvl_252d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 252)

def effa_014_asset_turnover_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_014_asset_turnover_zscore_252d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 252)

def effa_015_asset_turnover_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_015_asset_turnover_rank_252d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 252)

def effa_016_inventory_turnover_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_016_inventory_turnover_lvl_5d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 5)

def effa_017_inventory_turnover_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_017_inventory_turnover_zscore_5d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 5)

def effa_018_inventory_turnover_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_018_inventory_turnover_rank_5d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 5)

def effa_019_inventory_turnover_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_019_inventory_turnover_lvl_21d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 21)

def effa_020_inventory_turnover_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_020_inventory_turnover_zscore_21d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 21)

def effa_021_inventory_turnover_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_021_inventory_turnover_rank_21d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 21)

def effa_022_inventory_turnover_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_022_inventory_turnover_lvl_63d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 63)

def effa_023_inventory_turnover_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_023_inventory_turnover_zscore_63d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 63)

def effa_024_inventory_turnover_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_024_inventory_turnover_rank_63d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 63)

def effa_025_inventory_turnover_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_025_inventory_turnover_lvl_126d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 126)

def effa_026_inventory_turnover_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_026_inventory_turnover_zscore_126d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 126)

def effa_027_inventory_turnover_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_027_inventory_turnover_rank_126d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 126)

def effa_028_inventory_turnover_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_028_inventory_turnover_lvl_252d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 252)

def effa_029_inventory_turnover_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_029_inventory_turnover_zscore_252d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 252)

def effa_030_inventory_turnover_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_030_inventory_turnover_rank_252d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 252)

def effa_031_sales_to_assets_chg_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_031_sales_to_assets_chg_lvl_5d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rolling_mean(base, 5)

def effa_032_sales_to_assets_chg_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_032_sales_to_assets_chg_zscore_5d"""
    base = _safe_div(revenue, assets).diff(252)
    return _zscore_rolling(base, 5)

def effa_033_sales_to_assets_chg_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_033_sales_to_assets_chg_rank_5d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rank_pct(base, 5)

def effa_034_sales_to_assets_chg_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_034_sales_to_assets_chg_lvl_21d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rolling_mean(base, 21)

def effa_035_sales_to_assets_chg_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_035_sales_to_assets_chg_zscore_21d"""
    base = _safe_div(revenue, assets).diff(252)
    return _zscore_rolling(base, 21)

def effa_036_sales_to_assets_chg_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_036_sales_to_assets_chg_rank_21d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rank_pct(base, 21)

def effa_037_sales_to_assets_chg_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_037_sales_to_assets_chg_lvl_63d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rolling_mean(base, 63)

def effa_038_sales_to_assets_chg_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_038_sales_to_assets_chg_zscore_63d"""
    base = _safe_div(revenue, assets).diff(252)
    return _zscore_rolling(base, 63)

def effa_039_sales_to_assets_chg_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_039_sales_to_assets_chg_rank_63d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rank_pct(base, 63)

def effa_040_sales_to_assets_chg_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_040_sales_to_assets_chg_lvl_126d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rolling_mean(base, 126)

def effa_041_sales_to_assets_chg_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_041_sales_to_assets_chg_zscore_126d"""
    base = _safe_div(revenue, assets).diff(252)
    return _zscore_rolling(base, 126)

def effa_042_sales_to_assets_chg_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_042_sales_to_assets_chg_rank_126d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rank_pct(base, 126)

def effa_043_sales_to_assets_chg_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_043_sales_to_assets_chg_lvl_252d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rolling_mean(base, 252)

def effa_044_sales_to_assets_chg_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_044_sales_to_assets_chg_zscore_252d"""
    base = _safe_div(revenue, assets).diff(252)
    return _zscore_rolling(base, 252)

def effa_045_sales_to_assets_chg_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_045_sales_to_assets_chg_rank_252d"""
    base = _safe_div(revenue, assets).diff(252)
    return _rank_pct(base, 252)

def effa_046_inventory_efficiency_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_046_inventory_efficiency_lvl_5d"""
    base = _safe_div(revenue, inventory)
    return _rolling_mean(base, 5)

def effa_047_inventory_efficiency_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_047_inventory_efficiency_zscore_5d"""
    base = _safe_div(revenue, inventory)
    return _zscore_rolling(base, 5)

def effa_048_inventory_efficiency_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_048_inventory_efficiency_rank_5d"""
    base = _safe_div(revenue, inventory)
    return _rank_pct(base, 5)

def effa_049_inventory_efficiency_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_049_inventory_efficiency_lvl_21d"""
    base = _safe_div(revenue, inventory)
    return _rolling_mean(base, 21)

def effa_050_inventory_efficiency_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_050_inventory_efficiency_zscore_21d"""
    base = _safe_div(revenue, inventory)
    return _zscore_rolling(base, 21)

def effa_051_inventory_efficiency_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_051_inventory_efficiency_rank_21d"""
    base = _safe_div(revenue, inventory)
    return _rank_pct(base, 21)

def effa_052_inventory_efficiency_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_052_inventory_efficiency_lvl_63d"""
    base = _safe_div(revenue, inventory)
    return _rolling_mean(base, 63)

def effa_053_inventory_efficiency_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_053_inventory_efficiency_zscore_63d"""
    base = _safe_div(revenue, inventory)
    return _zscore_rolling(base, 63)

def effa_054_inventory_efficiency_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_054_inventory_efficiency_rank_63d"""
    base = _safe_div(revenue, inventory)
    return _rank_pct(base, 63)

def effa_055_inventory_efficiency_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_055_inventory_efficiency_lvl_126d"""
    base = _safe_div(revenue, inventory)
    return _rolling_mean(base, 126)

def effa_056_inventory_efficiency_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_056_inventory_efficiency_zscore_126d"""
    base = _safe_div(revenue, inventory)
    return _zscore_rolling(base, 126)

def effa_057_inventory_efficiency_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_057_inventory_efficiency_rank_126d"""
    base = _safe_div(revenue, inventory)
    return _rank_pct(base, 126)

def effa_058_inventory_efficiency_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_058_inventory_efficiency_lvl_252d"""
    base = _safe_div(revenue, inventory)
    return _rolling_mean(base, 252)

def effa_059_inventory_efficiency_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_059_inventory_efficiency_zscore_252d"""
    base = _safe_div(revenue, inventory)
    return _zscore_rolling(base, 252)

def effa_060_inventory_efficiency_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_060_inventory_efficiency_rank_252d"""
    base = _safe_div(revenue, inventory)
    return _rank_pct(base, 252)

def effa_061_efficiency_idx_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_061_efficiency_idx_lvl_5d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rolling_mean(base, 5)

def effa_062_efficiency_idx_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_062_efficiency_idx_zscore_5d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _zscore_rolling(base, 5)

def effa_063_efficiency_idx_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_063_efficiency_idx_rank_5d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rank_pct(base, 5)

def effa_064_efficiency_idx_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_064_efficiency_idx_lvl_21d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rolling_mean(base, 21)

def effa_065_efficiency_idx_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_065_efficiency_idx_zscore_21d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _zscore_rolling(base, 21)

def effa_066_efficiency_idx_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_066_efficiency_idx_rank_21d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rank_pct(base, 21)

def effa_067_efficiency_idx_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_067_efficiency_idx_lvl_63d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rolling_mean(base, 63)

def effa_068_efficiency_idx_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_068_efficiency_idx_zscore_63d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _zscore_rolling(base, 63)

def effa_069_efficiency_idx_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_069_efficiency_idx_rank_63d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rank_pct(base, 63)

def effa_070_efficiency_idx_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_070_efficiency_idx_lvl_126d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rolling_mean(base, 126)

def effa_071_efficiency_idx_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_071_efficiency_idx_zscore_126d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _zscore_rolling(base, 126)

def effa_072_efficiency_idx_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_072_efficiency_idx_rank_126d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rank_pct(base, 126)

def effa_073_efficiency_idx_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_073_efficiency_idx_lvl_252d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rolling_mean(base, 252)

def effa_074_efficiency_idx_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_074_efficiency_idx_zscore_252d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _zscore_rolling(base, 252)

def effa_075_efficiency_idx_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_075_efficiency_idx_rank_252d"""
    base = _safe_div(revenue, assets) * _safe_div(cor, inventory)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V57_REGISTRY = {
    "effa_001_asset_turnover_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_001_asset_turnover_lvl_5d},
    "effa_002_asset_turnover_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_002_asset_turnover_zscore_5d},
    "effa_003_asset_turnover_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_003_asset_turnover_rank_5d},
    "effa_004_asset_turnover_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_004_asset_turnover_lvl_21d},
    "effa_005_asset_turnover_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_005_asset_turnover_zscore_21d},
    "effa_006_asset_turnover_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_006_asset_turnover_rank_21d},
    "effa_007_asset_turnover_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_007_asset_turnover_lvl_63d},
    "effa_008_asset_turnover_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_008_asset_turnover_zscore_63d},
    "effa_009_asset_turnover_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_009_asset_turnover_rank_63d},
    "effa_010_asset_turnover_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_010_asset_turnover_lvl_126d},
    "effa_011_asset_turnover_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_011_asset_turnover_zscore_126d},
    "effa_012_asset_turnover_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_012_asset_turnover_rank_126d},
    "effa_013_asset_turnover_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_013_asset_turnover_lvl_252d},
    "effa_014_asset_turnover_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_014_asset_turnover_zscore_252d},
    "effa_015_asset_turnover_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_015_asset_turnover_rank_252d},
    "effa_016_inventory_turnover_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_016_inventory_turnover_lvl_5d},
    "effa_017_inventory_turnover_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_017_inventory_turnover_zscore_5d},
    "effa_018_inventory_turnover_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_018_inventory_turnover_rank_5d},
    "effa_019_inventory_turnover_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_019_inventory_turnover_lvl_21d},
    "effa_020_inventory_turnover_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_020_inventory_turnover_zscore_21d},
    "effa_021_inventory_turnover_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_021_inventory_turnover_rank_21d},
    "effa_022_inventory_turnover_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_022_inventory_turnover_lvl_63d},
    "effa_023_inventory_turnover_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_023_inventory_turnover_zscore_63d},
    "effa_024_inventory_turnover_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_024_inventory_turnover_rank_63d},
    "effa_025_inventory_turnover_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_025_inventory_turnover_lvl_126d},
    "effa_026_inventory_turnover_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_026_inventory_turnover_zscore_126d},
    "effa_027_inventory_turnover_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_027_inventory_turnover_rank_126d},
    "effa_028_inventory_turnover_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_028_inventory_turnover_lvl_252d},
    "effa_029_inventory_turnover_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_029_inventory_turnover_zscore_252d},
    "effa_030_inventory_turnover_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_030_inventory_turnover_rank_252d},
    "effa_031_sales_to_assets_chg_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_031_sales_to_assets_chg_lvl_5d},
    "effa_032_sales_to_assets_chg_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_032_sales_to_assets_chg_zscore_5d},
    "effa_033_sales_to_assets_chg_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_033_sales_to_assets_chg_rank_5d},
    "effa_034_sales_to_assets_chg_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_034_sales_to_assets_chg_lvl_21d},
    "effa_035_sales_to_assets_chg_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_035_sales_to_assets_chg_zscore_21d},
    "effa_036_sales_to_assets_chg_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_036_sales_to_assets_chg_rank_21d},
    "effa_037_sales_to_assets_chg_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_037_sales_to_assets_chg_lvl_63d},
    "effa_038_sales_to_assets_chg_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_038_sales_to_assets_chg_zscore_63d},
    "effa_039_sales_to_assets_chg_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_039_sales_to_assets_chg_rank_63d},
    "effa_040_sales_to_assets_chg_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_040_sales_to_assets_chg_lvl_126d},
    "effa_041_sales_to_assets_chg_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_041_sales_to_assets_chg_zscore_126d},
    "effa_042_sales_to_assets_chg_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_042_sales_to_assets_chg_rank_126d},
    "effa_043_sales_to_assets_chg_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_043_sales_to_assets_chg_lvl_252d},
    "effa_044_sales_to_assets_chg_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_044_sales_to_assets_chg_zscore_252d},
    "effa_045_sales_to_assets_chg_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_045_sales_to_assets_chg_rank_252d},
    "effa_046_inventory_efficiency_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_046_inventory_efficiency_lvl_5d},
    "effa_047_inventory_efficiency_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_047_inventory_efficiency_zscore_5d},
    "effa_048_inventory_efficiency_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_048_inventory_efficiency_rank_5d},
    "effa_049_inventory_efficiency_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_049_inventory_efficiency_lvl_21d},
    "effa_050_inventory_efficiency_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_050_inventory_efficiency_zscore_21d},
    "effa_051_inventory_efficiency_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_051_inventory_efficiency_rank_21d},
    "effa_052_inventory_efficiency_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_052_inventory_efficiency_lvl_63d},
    "effa_053_inventory_efficiency_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_053_inventory_efficiency_zscore_63d},
    "effa_054_inventory_efficiency_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_054_inventory_efficiency_rank_63d},
    "effa_055_inventory_efficiency_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_055_inventory_efficiency_lvl_126d},
    "effa_056_inventory_efficiency_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_056_inventory_efficiency_zscore_126d},
    "effa_057_inventory_efficiency_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_057_inventory_efficiency_rank_126d},
    "effa_058_inventory_efficiency_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_058_inventory_efficiency_lvl_252d},
    "effa_059_inventory_efficiency_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_059_inventory_efficiency_zscore_252d},
    "effa_060_inventory_efficiency_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_060_inventory_efficiency_rank_252d},
    "effa_061_efficiency_idx_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_061_efficiency_idx_lvl_5d},
    "effa_062_efficiency_idx_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_062_efficiency_idx_zscore_5d},
    "effa_063_efficiency_idx_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_063_efficiency_idx_rank_5d},
    "effa_064_efficiency_idx_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_064_efficiency_idx_lvl_21d},
    "effa_065_efficiency_idx_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_065_efficiency_idx_zscore_21d},
    "effa_066_efficiency_idx_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_066_efficiency_idx_rank_21d},
    "effa_067_efficiency_idx_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_067_efficiency_idx_lvl_63d},
    "effa_068_efficiency_idx_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_068_efficiency_idx_zscore_63d},
    "effa_069_efficiency_idx_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_069_efficiency_idx_rank_63d},
    "effa_070_efficiency_idx_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_070_efficiency_idx_lvl_126d},
    "effa_071_efficiency_idx_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_071_efficiency_idx_zscore_126d},
    "effa_072_efficiency_idx_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_072_efficiency_idx_rank_126d},
    "effa_073_efficiency_idx_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_073_efficiency_idx_lvl_252d},
    "effa_074_efficiency_idx_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_074_efficiency_idx_zscore_252d},
    "effa_075_efficiency_idx_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_075_efficiency_idx_rank_252d},
}
