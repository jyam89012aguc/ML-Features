"""
41_efficiency_snapshot — Base Features 001-075
Domain: efficiency_snapshot
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

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _pct_change(s: pd.Series, periods: int) -> pd.Series:
    return _safe_div(s - s.shift(periods), s.shift(periods).abs())

# ── Feature functions ────────────────────────────────────────────────────────

def effi_001_asset_turnover_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_001_asset_turnover_lvl_5d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 5)

def effi_002_asset_turnover_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_002_asset_turnover_zscore_5d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 5)

def effi_003_asset_turnover_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_003_asset_turnover_rank_5d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 5)

def effi_004_asset_turnover_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_004_asset_turnover_lvl_21d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 21)

def effi_005_asset_turnover_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_005_asset_turnover_zscore_21d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 21)

def effi_006_asset_turnover_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_006_asset_turnover_rank_21d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 21)

def effi_007_asset_turnover_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_007_asset_turnover_lvl_63d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 63)

def effi_008_asset_turnover_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_008_asset_turnover_zscore_63d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 63)

def effi_009_asset_turnover_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_009_asset_turnover_rank_63d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 63)

def effi_010_asset_turnover_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_010_asset_turnover_lvl_126d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 126)

def effi_011_asset_turnover_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_011_asset_turnover_zscore_126d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 126)

def effi_012_asset_turnover_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_012_asset_turnover_rank_126d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 126)

def effi_013_asset_turnover_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_013_asset_turnover_lvl_252d"""
    base = _safe_div(revenue, assets)
    return _rolling_mean(base, 252)

def effi_014_asset_turnover_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_014_asset_turnover_zscore_252d"""
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 252)

def effi_015_asset_turnover_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_015_asset_turnover_rank_252d"""
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 252)

def effi_016_inventory_turnover_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_016_inventory_turnover_lvl_5d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 5)

def effi_017_inventory_turnover_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_017_inventory_turnover_zscore_5d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 5)

def effi_018_inventory_turnover_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_018_inventory_turnover_rank_5d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 5)

def effi_019_inventory_turnover_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_019_inventory_turnover_lvl_21d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 21)

def effi_020_inventory_turnover_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_020_inventory_turnover_zscore_21d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 21)

def effi_021_inventory_turnover_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_021_inventory_turnover_rank_21d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 21)

def effi_022_inventory_turnover_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_022_inventory_turnover_lvl_63d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 63)

def effi_023_inventory_turnover_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_023_inventory_turnover_zscore_63d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 63)

def effi_024_inventory_turnover_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_024_inventory_turnover_rank_63d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 63)

def effi_025_inventory_turnover_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_025_inventory_turnover_lvl_126d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 126)

def effi_026_inventory_turnover_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_026_inventory_turnover_zscore_126d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 126)

def effi_027_inventory_turnover_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_027_inventory_turnover_rank_126d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 126)

def effi_028_inventory_turnover_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_028_inventory_turnover_lvl_252d"""
    base = _safe_div(cor, inventory)
    return _rolling_mean(base, 252)

def effi_029_inventory_turnover_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_029_inventory_turnover_zscore_252d"""
    base = _safe_div(cor, inventory)
    return _zscore_rolling(base, 252)

def effi_030_inventory_turnover_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_030_inventory_turnover_rank_252d"""
    base = _safe_div(cor, inventory)
    return _rank_pct(base, 252)

def effi_031_receivables_turnover_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_031_receivables_turnover_lvl_5d"""
    base = _safe_div(revenue, receivables)
    return _rolling_mean(base, 5)

def effi_032_receivables_turnover_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_032_receivables_turnover_zscore_5d"""
    base = _safe_div(revenue, receivables)
    return _zscore_rolling(base, 5)

def effi_033_receivables_turnover_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_033_receivables_turnover_rank_5d"""
    base = _safe_div(revenue, receivables)
    return _rank_pct(base, 5)

def effi_034_receivables_turnover_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_034_receivables_turnover_lvl_21d"""
    base = _safe_div(revenue, receivables)
    return _rolling_mean(base, 21)

def effi_035_receivables_turnover_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_035_receivables_turnover_zscore_21d"""
    base = _safe_div(revenue, receivables)
    return _zscore_rolling(base, 21)

def effi_036_receivables_turnover_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_036_receivables_turnover_rank_21d"""
    base = _safe_div(revenue, receivables)
    return _rank_pct(base, 21)

def effi_037_receivables_turnover_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_037_receivables_turnover_lvl_63d"""
    base = _safe_div(revenue, receivables)
    return _rolling_mean(base, 63)

def effi_038_receivables_turnover_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_038_receivables_turnover_zscore_63d"""
    base = _safe_div(revenue, receivables)
    return _zscore_rolling(base, 63)

def effi_039_receivables_turnover_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_039_receivables_turnover_rank_63d"""
    base = _safe_div(revenue, receivables)
    return _rank_pct(base, 63)

def effi_040_receivables_turnover_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_040_receivables_turnover_lvl_126d"""
    base = _safe_div(revenue, receivables)
    return _rolling_mean(base, 126)

def effi_041_receivables_turnover_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_041_receivables_turnover_zscore_126d"""
    base = _safe_div(revenue, receivables)
    return _zscore_rolling(base, 126)

def effi_042_receivables_turnover_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_042_receivables_turnover_rank_126d"""
    base = _safe_div(revenue, receivables)
    return _rank_pct(base, 126)

def effi_043_receivables_turnover_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_043_receivables_turnover_lvl_252d"""
    base = _safe_div(revenue, receivables)
    return _rolling_mean(base, 252)

def effi_044_receivables_turnover_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_044_receivables_turnover_zscore_252d"""
    base = _safe_div(revenue, receivables)
    return _zscore_rolling(base, 252)

def effi_045_receivables_turnover_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_045_receivables_turnover_rank_252d"""
    base = _safe_div(revenue, receivables)
    return _rank_pct(base, 252)

def effi_046_fixed_asset_turnover_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_046_fixed_asset_turnover_lvl_5d"""
    base = _safe_div(revenue, ppnent)
    return _rolling_mean(base, 5)

def effi_047_fixed_asset_turnover_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_047_fixed_asset_turnover_zscore_5d"""
    base = _safe_div(revenue, ppnent)
    return _zscore_rolling(base, 5)

def effi_048_fixed_asset_turnover_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_048_fixed_asset_turnover_rank_5d"""
    base = _safe_div(revenue, ppnent)
    return _rank_pct(base, 5)

def effi_049_fixed_asset_turnover_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_049_fixed_asset_turnover_lvl_21d"""
    base = _safe_div(revenue, ppnent)
    return _rolling_mean(base, 21)

def effi_050_fixed_asset_turnover_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_050_fixed_asset_turnover_zscore_21d"""
    base = _safe_div(revenue, ppnent)
    return _zscore_rolling(base, 21)

def effi_051_fixed_asset_turnover_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_051_fixed_asset_turnover_rank_21d"""
    base = _safe_div(revenue, ppnent)
    return _rank_pct(base, 21)

def effi_052_fixed_asset_turnover_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_052_fixed_asset_turnover_lvl_63d"""
    base = _safe_div(revenue, ppnent)
    return _rolling_mean(base, 63)

def effi_053_fixed_asset_turnover_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_053_fixed_asset_turnover_zscore_63d"""
    base = _safe_div(revenue, ppnent)
    return _zscore_rolling(base, 63)

def effi_054_fixed_asset_turnover_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_054_fixed_asset_turnover_rank_63d"""
    base = _safe_div(revenue, ppnent)
    return _rank_pct(base, 63)

def effi_055_fixed_asset_turnover_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_055_fixed_asset_turnover_lvl_126d"""
    base = _safe_div(revenue, ppnent)
    return _rolling_mean(base, 126)

def effi_056_fixed_asset_turnover_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_056_fixed_asset_turnover_zscore_126d"""
    base = _safe_div(revenue, ppnent)
    return _zscore_rolling(base, 126)

def effi_057_fixed_asset_turnover_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_057_fixed_asset_turnover_rank_126d"""
    base = _safe_div(revenue, ppnent)
    return _rank_pct(base, 126)

def effi_058_fixed_asset_turnover_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_058_fixed_asset_turnover_lvl_252d"""
    base = _safe_div(revenue, ppnent)
    return _rolling_mean(base, 252)

def effi_059_fixed_asset_turnover_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_059_fixed_asset_turnover_zscore_252d"""
    base = _safe_div(revenue, ppnent)
    return _zscore_rolling(base, 252)

def effi_060_fixed_asset_turnover_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_060_fixed_asset_turnover_rank_252d"""
    base = _safe_div(revenue, ppnent)
    return _rank_pct(base, 252)

def effi_061_payables_turnover_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_061_payables_turnover_lvl_5d"""
    base = _safe_div(cor, payables)
    return _rolling_mean(base, 5)

def effi_062_payables_turnover_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_062_payables_turnover_zscore_5d"""
    base = _safe_div(cor, payables)
    return _zscore_rolling(base, 5)

def effi_063_payables_turnover_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_063_payables_turnover_rank_5d"""
    base = _safe_div(cor, payables)
    return _rank_pct(base, 5)

def effi_064_payables_turnover_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_064_payables_turnover_lvl_21d"""
    base = _safe_div(cor, payables)
    return _rolling_mean(base, 21)

def effi_065_payables_turnover_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_065_payables_turnover_zscore_21d"""
    base = _safe_div(cor, payables)
    return _zscore_rolling(base, 21)

def effi_066_payables_turnover_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_066_payables_turnover_rank_21d"""
    base = _safe_div(cor, payables)
    return _rank_pct(base, 21)

def effi_067_payables_turnover_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_067_payables_turnover_lvl_63d"""
    base = _safe_div(cor, payables)
    return _rolling_mean(base, 63)

def effi_068_payables_turnover_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_068_payables_turnover_zscore_63d"""
    base = _safe_div(cor, payables)
    return _zscore_rolling(base, 63)

def effi_069_payables_turnover_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_069_payables_turnover_rank_63d"""
    base = _safe_div(cor, payables)
    return _rank_pct(base, 63)

def effi_070_payables_turnover_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_070_payables_turnover_lvl_126d"""
    base = _safe_div(cor, payables)
    return _rolling_mean(base, 126)

def effi_071_payables_turnover_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_071_payables_turnover_zscore_126d"""
    base = _safe_div(cor, payables)
    return _zscore_rolling(base, 126)

def effi_072_payables_turnover_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_072_payables_turnover_rank_126d"""
    base = _safe_div(cor, payables)
    return _rank_pct(base, 126)

def effi_073_payables_turnover_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_073_payables_turnover_lvl_252d"""
    base = _safe_div(cor, payables)
    return _rolling_mean(base, 252)

def effi_074_payables_turnover_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_074_payables_turnover_zscore_252d"""
    base = _safe_div(cor, payables)
    return _zscore_rolling(base, 252)

def effi_075_payables_turnover_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series, payables: pd.Series, cor: pd.Series, ppnent: pd.Series) -> pd.Series:
    """effi_075_payables_turnover_rank_252d"""
    base = _safe_div(cor, payables)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V41_REGISTRY = {
    "effi_001_asset_turnover_lvl_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_001_asset_turnover_lvl_5d},
    "effi_002_asset_turnover_zscore_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_002_asset_turnover_zscore_5d},
    "effi_003_asset_turnover_rank_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_003_asset_turnover_rank_5d},
    "effi_004_asset_turnover_lvl_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_004_asset_turnover_lvl_21d},
    "effi_005_asset_turnover_zscore_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_005_asset_turnover_zscore_21d},
    "effi_006_asset_turnover_rank_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_006_asset_turnover_rank_21d},
    "effi_007_asset_turnover_lvl_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_007_asset_turnover_lvl_63d},
    "effi_008_asset_turnover_zscore_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_008_asset_turnover_zscore_63d},
    "effi_009_asset_turnover_rank_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_009_asset_turnover_rank_63d},
    "effi_010_asset_turnover_lvl_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_010_asset_turnover_lvl_126d},
    "effi_011_asset_turnover_zscore_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_011_asset_turnover_zscore_126d},
    "effi_012_asset_turnover_rank_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_012_asset_turnover_rank_126d},
    "effi_013_asset_turnover_lvl_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_013_asset_turnover_lvl_252d},
    "effi_014_asset_turnover_zscore_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_014_asset_turnover_zscore_252d},
    "effi_015_asset_turnover_rank_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_015_asset_turnover_rank_252d},
    "effi_016_inventory_turnover_lvl_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_016_inventory_turnover_lvl_5d},
    "effi_017_inventory_turnover_zscore_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_017_inventory_turnover_zscore_5d},
    "effi_018_inventory_turnover_rank_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_018_inventory_turnover_rank_5d},
    "effi_019_inventory_turnover_lvl_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_019_inventory_turnover_lvl_21d},
    "effi_020_inventory_turnover_zscore_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_020_inventory_turnover_zscore_21d},
    "effi_021_inventory_turnover_rank_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_021_inventory_turnover_rank_21d},
    "effi_022_inventory_turnover_lvl_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_022_inventory_turnover_lvl_63d},
    "effi_023_inventory_turnover_zscore_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_023_inventory_turnover_zscore_63d},
    "effi_024_inventory_turnover_rank_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_024_inventory_turnover_rank_63d},
    "effi_025_inventory_turnover_lvl_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_025_inventory_turnover_lvl_126d},
    "effi_026_inventory_turnover_zscore_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_026_inventory_turnover_zscore_126d},
    "effi_027_inventory_turnover_rank_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_027_inventory_turnover_rank_126d},
    "effi_028_inventory_turnover_lvl_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_028_inventory_turnover_lvl_252d},
    "effi_029_inventory_turnover_zscore_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_029_inventory_turnover_zscore_252d},
    "effi_030_inventory_turnover_rank_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_030_inventory_turnover_rank_252d},
    "effi_031_receivables_turnover_lvl_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_031_receivables_turnover_lvl_5d},
    "effi_032_receivables_turnover_zscore_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_032_receivables_turnover_zscore_5d},
    "effi_033_receivables_turnover_rank_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_033_receivables_turnover_rank_5d},
    "effi_034_receivables_turnover_lvl_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_034_receivables_turnover_lvl_21d},
    "effi_035_receivables_turnover_zscore_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_035_receivables_turnover_zscore_21d},
    "effi_036_receivables_turnover_rank_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_036_receivables_turnover_rank_21d},
    "effi_037_receivables_turnover_lvl_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_037_receivables_turnover_lvl_63d},
    "effi_038_receivables_turnover_zscore_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_038_receivables_turnover_zscore_63d},
    "effi_039_receivables_turnover_rank_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_039_receivables_turnover_rank_63d},
    "effi_040_receivables_turnover_lvl_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_040_receivables_turnover_lvl_126d},
    "effi_041_receivables_turnover_zscore_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_041_receivables_turnover_zscore_126d},
    "effi_042_receivables_turnover_rank_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_042_receivables_turnover_rank_126d},
    "effi_043_receivables_turnover_lvl_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_043_receivables_turnover_lvl_252d},
    "effi_044_receivables_turnover_zscore_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_044_receivables_turnover_zscore_252d},
    "effi_045_receivables_turnover_rank_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_045_receivables_turnover_rank_252d},
    "effi_046_fixed_asset_turnover_lvl_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_046_fixed_asset_turnover_lvl_5d},
    "effi_047_fixed_asset_turnover_zscore_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_047_fixed_asset_turnover_zscore_5d},
    "effi_048_fixed_asset_turnover_rank_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_048_fixed_asset_turnover_rank_5d},
    "effi_049_fixed_asset_turnover_lvl_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_049_fixed_asset_turnover_lvl_21d},
    "effi_050_fixed_asset_turnover_zscore_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_050_fixed_asset_turnover_zscore_21d},
    "effi_051_fixed_asset_turnover_rank_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_051_fixed_asset_turnover_rank_21d},
    "effi_052_fixed_asset_turnover_lvl_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_052_fixed_asset_turnover_lvl_63d},
    "effi_053_fixed_asset_turnover_zscore_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_053_fixed_asset_turnover_zscore_63d},
    "effi_054_fixed_asset_turnover_rank_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_054_fixed_asset_turnover_rank_63d},
    "effi_055_fixed_asset_turnover_lvl_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_055_fixed_asset_turnover_lvl_126d},
    "effi_056_fixed_asset_turnover_zscore_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_056_fixed_asset_turnover_zscore_126d},
    "effi_057_fixed_asset_turnover_rank_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_057_fixed_asset_turnover_rank_126d},
    "effi_058_fixed_asset_turnover_lvl_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_058_fixed_asset_turnover_lvl_252d},
    "effi_059_fixed_asset_turnover_zscore_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_059_fixed_asset_turnover_zscore_252d},
    "effi_060_fixed_asset_turnover_rank_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_060_fixed_asset_turnover_rank_252d},
    "effi_061_payables_turnover_lvl_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_061_payables_turnover_lvl_5d},
    "effi_062_payables_turnover_zscore_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_062_payables_turnover_zscore_5d},
    "effi_063_payables_turnover_rank_5d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_063_payables_turnover_rank_5d},
    "effi_064_payables_turnover_lvl_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_064_payables_turnover_lvl_21d},
    "effi_065_payables_turnover_zscore_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_065_payables_turnover_zscore_21d},
    "effi_066_payables_turnover_rank_21d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_066_payables_turnover_rank_21d},
    "effi_067_payables_turnover_lvl_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_067_payables_turnover_lvl_63d},
    "effi_068_payables_turnover_zscore_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_068_payables_turnover_zscore_63d},
    "effi_069_payables_turnover_rank_63d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_069_payables_turnover_rank_63d},
    "effi_070_payables_turnover_lvl_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_070_payables_turnover_lvl_126d},
    "effi_071_payables_turnover_zscore_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_071_payables_turnover_zscore_126d},
    "effi_072_payables_turnover_rank_126d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_072_payables_turnover_rank_126d},
    "effi_073_payables_turnover_lvl_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_073_payables_turnover_lvl_252d},
    "effi_074_payables_turnover_zscore_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_074_payables_turnover_zscore_252d},
    "effi_075_payables_turnover_rank_252d": {"inputs": ['revenue', 'assets', 'inventory', 'receivables', 'payables', 'cor', 'ppnent'], "func": effi_075_payables_turnover_rank_252d},
}
