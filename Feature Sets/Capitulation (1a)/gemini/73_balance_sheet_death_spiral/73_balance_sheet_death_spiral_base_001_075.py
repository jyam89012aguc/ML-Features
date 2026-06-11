"""
73_balance_sheet_death_spiral — Base Features 001-075
Domain: Assets shrinking + Liabs growing
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

def bsds_001_asset_shrinkage_5d(assets: pd.Series) -> pd.Series:
    """bsds_001_asset_shrinkage_5d"""
    return (assets.pct_change(252)).shift(5)

def bsds_002_asset_shrinkage_21d(assets: pd.Series) -> pd.Series:
    """bsds_002_asset_shrinkage_21d"""
    return (assets.pct_change(252)).shift(21)

def bsds_003_asset_shrinkage_63d(assets: pd.Series) -> pd.Series:
    """bsds_003_asset_shrinkage_63d"""
    return (assets.pct_change(252)).shift(63)

def bsds_004_asset_shrinkage_126d(assets: pd.Series) -> pd.Series:
    """bsds_004_asset_shrinkage_126d"""
    return (assets.pct_change(252)).shift(126)

def bsds_005_asset_shrinkage_252d(assets: pd.Series) -> pd.Series:
    """bsds_005_asset_shrinkage_252d"""
    return (assets.pct_change(252)).shift(252)

def bsds_006_liab_expansion_5d(liabs: pd.Series) -> pd.Series:
    """bsds_006_liab_expansion_5d"""
    return (liabs.pct_change(252)).shift(5)

def bsds_007_liab_expansion_21d(liabs: pd.Series) -> pd.Series:
    """bsds_007_liab_expansion_21d"""
    return (liabs.pct_change(252)).shift(21)

def bsds_008_liab_expansion_63d(liabs: pd.Series) -> pd.Series:
    """bsds_008_liab_expansion_63d"""
    return (liabs.pct_change(252)).shift(63)

def bsds_009_liab_expansion_126d(liabs: pd.Series) -> pd.Series:
    """bsds_009_liab_expansion_126d"""
    return (liabs.pct_change(252)).shift(126)

def bsds_010_liab_expansion_252d(liabs: pd.Series) -> pd.Series:
    """bsds_010_liab_expansion_252d"""
    return (liabs.pct_change(252)).shift(252)

def bsds_011_equity_erosion_5d(equity: pd.Series) -> pd.Series:
    """bsds_011_equity_erosion_5d"""
    return (equity.pct_change(252)).shift(5)

def bsds_012_equity_erosion_21d(equity: pd.Series) -> pd.Series:
    """bsds_012_equity_erosion_21d"""
    return (equity.pct_change(252)).shift(21)

def bsds_013_equity_erosion_63d(equity: pd.Series) -> pd.Series:
    """bsds_013_equity_erosion_63d"""
    return (equity.pct_change(252)).shift(63)

def bsds_014_equity_erosion_126d(equity: pd.Series) -> pd.Series:
    """bsds_014_equity_erosion_126d"""
    return (equity.pct_change(252)).shift(126)

def bsds_015_equity_erosion_252d(equity: pd.Series) -> pd.Series:
    """bsds_015_equity_erosion_252d"""
    return (equity.pct_change(252)).shift(252)

def bsds_016_death_spiral_index_5d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_016_death_spiral_index_5d"""
    return (liabs.pct_change(252) - assets.pct_change(252)).shift(5)

def bsds_017_death_spiral_index_21d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_017_death_spiral_index_21d"""
    return (liabs.pct_change(252) - assets.pct_change(252)).shift(21)

def bsds_018_death_spiral_index_63d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_018_death_spiral_index_63d"""
    return (liabs.pct_change(252) - assets.pct_change(252)).shift(63)

def bsds_019_death_spiral_index_126d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_019_death_spiral_index_126d"""
    return (liabs.pct_change(252) - assets.pct_change(252)).shift(126)

def bsds_020_death_spiral_index_252d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_020_death_spiral_index_252d"""
    return (liabs.pct_change(252) - assets.pct_change(252)).shift(252)

def bsds_021_leverage_spiral_5d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_021_leverage_spiral_5d"""
    return ((_safe_div(liabs, assets)).diff(252)).shift(5)

def bsds_022_leverage_spiral_21d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_022_leverage_spiral_21d"""
    return ((_safe_div(liabs, assets)).diff(252)).shift(21)

def bsds_023_leverage_spiral_63d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_023_leverage_spiral_63d"""
    return ((_safe_div(liabs, assets)).diff(252)).shift(63)

def bsds_024_leverage_spiral_126d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_024_leverage_spiral_126d"""
    return ((_safe_div(liabs, assets)).diff(252)).shift(126)

def bsds_025_leverage_spiral_252d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_025_leverage_spiral_252d"""
    return ((_safe_div(liabs, assets)).diff(252)).shift(252)

def bsds_026_insolvency_momentum_5d(equity: pd.Series) -> pd.Series:
    """bsds_026_insolvency_momentum_5d"""
    return (equity.diff(252)).shift(5)

def bsds_027_insolvency_momentum_21d(equity: pd.Series) -> pd.Series:
    """bsds_027_insolvency_momentum_21d"""
    return (equity.diff(252)).shift(21)

def bsds_028_insolvency_momentum_63d(equity: pd.Series) -> pd.Series:
    """bsds_028_insolvency_momentum_63d"""
    return (equity.diff(252)).shift(63)

def bsds_029_insolvency_momentum_126d(equity: pd.Series) -> pd.Series:
    """bsds_029_insolvency_momentum_126d"""
    return (equity.diff(252)).shift(126)

def bsds_030_insolvency_momentum_252d(equity: pd.Series) -> pd.Series:
    """bsds_030_insolvency_momentum_252d"""
    return (equity.diff(252)).shift(252)

def bsds_031_asset_quality_decay_5d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """bsds_031_asset_quality_decay_5d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(5)

def bsds_032_asset_quality_decay_21d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """bsds_032_asset_quality_decay_21d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(21)

def bsds_033_asset_quality_decay_63d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """bsds_033_asset_quality_decay_63d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(63)

def bsds_034_asset_quality_decay_126d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """bsds_034_asset_quality_decay_126d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(126)

def bsds_035_asset_quality_decay_252d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """bsds_035_asset_quality_decay_252d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(252)

def bsds_036_working_cap_collapse_5d(workingcapital: pd.Series) -> pd.Series:
    """bsds_036_working_cap_collapse_5d"""
    return (workingcapital.diff(252)).shift(5)

def bsds_037_working_cap_collapse_21d(workingcapital: pd.Series) -> pd.Series:
    """bsds_037_working_cap_collapse_21d"""
    return (workingcapital.diff(252)).shift(21)

def bsds_038_working_cap_collapse_63d(workingcapital: pd.Series) -> pd.Series:
    """bsds_038_working_cap_collapse_63d"""
    return (workingcapital.diff(252)).shift(63)

def bsds_039_working_cap_collapse_126d(workingcapital: pd.Series) -> pd.Series:
    """bsds_039_working_cap_collapse_126d"""
    return (workingcapital.diff(252)).shift(126)

def bsds_040_working_cap_collapse_252d(workingcapital: pd.Series) -> pd.Series:
    """bsds_040_working_cap_collapse_252d"""
    return (workingcapital.diff(252)).shift(252)

def bsds_041_cash_drain_5d(cashnequiv: pd.Series) -> pd.Series:
    """bsds_041_cash_drain_5d"""
    return (cashnequiv.diff(252)).shift(5)

def bsds_042_cash_drain_21d(cashnequiv: pd.Series) -> pd.Series:
    """bsds_042_cash_drain_21d"""
    return (cashnequiv.diff(252)).shift(21)

def bsds_043_cash_drain_63d(cashnequiv: pd.Series) -> pd.Series:
    """bsds_043_cash_drain_63d"""
    return (cashnequiv.diff(252)).shift(63)

def bsds_044_cash_drain_126d(cashnequiv: pd.Series) -> pd.Series:
    """bsds_044_cash_drain_126d"""
    return (cashnequiv.diff(252)).shift(126)

def bsds_045_cash_drain_252d(cashnequiv: pd.Series) -> pd.Series:
    """bsds_045_cash_drain_252d"""
    return (cashnequiv.diff(252)).shift(252)

def bsds_046_debt_accumulation_5d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """bsds_046_debt_accumulation_5d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).diff(252)).shift(5)

def bsds_047_debt_accumulation_21d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """bsds_047_debt_accumulation_21d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).diff(252)).shift(21)

def bsds_048_debt_accumulation_63d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """bsds_048_debt_accumulation_63d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).diff(252)).shift(63)

def bsds_049_debt_accumulation_126d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """bsds_049_debt_accumulation_126d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).diff(252)).shift(126)

def bsds_050_debt_accumulation_252d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """bsds_050_debt_accumulation_252d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).diff(252)).shift(252)

def bsds_051_asset_turnover_decay_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_051_asset_turnover_decay_5d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(5)

def bsds_052_asset_turnover_decay_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_052_asset_turnover_decay_21d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(21)

def bsds_053_asset_turnover_decay_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_053_asset_turnover_decay_63d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(63)

def bsds_054_asset_turnover_decay_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_054_asset_turnover_decay_126d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(126)

def bsds_055_asset_turnover_decay_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_055_asset_turnover_decay_252d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(252)

def bsds_056_roi_collapse_5d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_056_roi_collapse_5d"""
    return ((_safe_div(netinc, assets)).diff(252)).shift(5)

def bsds_057_roi_collapse_21d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_057_roi_collapse_21d"""
    return ((_safe_div(netinc, assets)).diff(252)).shift(21)

def bsds_058_roi_collapse_63d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_058_roi_collapse_63d"""
    return ((_safe_div(netinc, assets)).diff(252)).shift(63)

def bsds_059_roi_collapse_126d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_059_roi_collapse_126d"""
    return ((_safe_div(netinc, assets)).diff(252)).shift(126)

def bsds_060_roi_collapse_252d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """bsds_060_roi_collapse_252d"""
    return ((_safe_div(netinc, assets)).diff(252)).shift(252)

def bsds_061_death_spiral_z_5d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_061_death_spiral_z_5d"""
    return (_zscore_rolling(liabs.pct_change(252) - assets.pct_change(252), 1260)).shift(5)

def bsds_062_death_spiral_z_21d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_062_death_spiral_z_21d"""
    return (_zscore_rolling(liabs.pct_change(252) - assets.pct_change(252), 1260)).shift(21)

def bsds_063_death_spiral_z_63d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_063_death_spiral_z_63d"""
    return (_zscore_rolling(liabs.pct_change(252) - assets.pct_change(252), 1260)).shift(63)

def bsds_064_death_spiral_z_126d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_064_death_spiral_z_126d"""
    return (_zscore_rolling(liabs.pct_change(252) - assets.pct_change(252), 1260)).shift(126)

def bsds_065_death_spiral_z_252d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_065_death_spiral_z_252d"""
    return (_zscore_rolling(liabs.pct_change(252) - assets.pct_change(252), 1260)).shift(252)

def bsds_066_equity_to_assets_decay_5d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_066_equity_to_assets_decay_5d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(5)

def bsds_067_equity_to_assets_decay_21d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_067_equity_to_assets_decay_21d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(21)

def bsds_068_equity_to_assets_decay_63d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_068_equity_to_assets_decay_63d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(63)

def bsds_069_equity_to_assets_decay_126d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_069_equity_to_assets_decay_126d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(126)

def bsds_070_equity_to_assets_decay_252d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_070_equity_to_assets_decay_252d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(252)

def bsds_071_liab_to_rev_spike_5d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_071_liab_to_rev_spike_5d"""
    return ((_safe_div(liabs, revenue)).diff(252)).shift(5)

def bsds_072_liab_to_rev_spike_21d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_072_liab_to_rev_spike_21d"""
    return ((_safe_div(liabs, revenue)).diff(252)).shift(21)

def bsds_073_liab_to_rev_spike_63d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_073_liab_to_rev_spike_63d"""
    return ((_safe_div(liabs, revenue)).diff(252)).shift(63)

def bsds_074_liab_to_rev_spike_126d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_074_liab_to_rev_spike_126d"""
    return ((_safe_div(liabs, revenue)).diff(252)).shift(126)

def bsds_075_liab_to_rev_spike_252d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_075_liab_to_rev_spike_252d"""
    return ((_safe_div(liabs, revenue)).diff(252)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V73_REGISTRY = {
    "bsds_001_asset_shrinkage_5d": {"inputs": ['assets'], "func": bsds_001_asset_shrinkage_5d},
    "bsds_002_asset_shrinkage_21d": {"inputs": ['assets'], "func": bsds_002_asset_shrinkage_21d},
    "bsds_003_asset_shrinkage_63d": {"inputs": ['assets'], "func": bsds_003_asset_shrinkage_63d},
    "bsds_004_asset_shrinkage_126d": {"inputs": ['assets'], "func": bsds_004_asset_shrinkage_126d},
    "bsds_005_asset_shrinkage_252d": {"inputs": ['assets'], "func": bsds_005_asset_shrinkage_252d},
    "bsds_006_liab_expansion_5d": {"inputs": ['liabs'], "func": bsds_006_liab_expansion_5d},
    "bsds_007_liab_expansion_21d": {"inputs": ['liabs'], "func": bsds_007_liab_expansion_21d},
    "bsds_008_liab_expansion_63d": {"inputs": ['liabs'], "func": bsds_008_liab_expansion_63d},
    "bsds_009_liab_expansion_126d": {"inputs": ['liabs'], "func": bsds_009_liab_expansion_126d},
    "bsds_010_liab_expansion_252d": {"inputs": ['liabs'], "func": bsds_010_liab_expansion_252d},
    "bsds_011_equity_erosion_5d": {"inputs": ['equity'], "func": bsds_011_equity_erosion_5d},
    "bsds_012_equity_erosion_21d": {"inputs": ['equity'], "func": bsds_012_equity_erosion_21d},
    "bsds_013_equity_erosion_63d": {"inputs": ['equity'], "func": bsds_013_equity_erosion_63d},
    "bsds_014_equity_erosion_126d": {"inputs": ['equity'], "func": bsds_014_equity_erosion_126d},
    "bsds_015_equity_erosion_252d": {"inputs": ['equity'], "func": bsds_015_equity_erosion_252d},
    "bsds_016_death_spiral_index_5d": {"inputs": ['assets', 'liabs'], "func": bsds_016_death_spiral_index_5d},
    "bsds_017_death_spiral_index_21d": {"inputs": ['assets', 'liabs'], "func": bsds_017_death_spiral_index_21d},
    "bsds_018_death_spiral_index_63d": {"inputs": ['assets', 'liabs'], "func": bsds_018_death_spiral_index_63d},
    "bsds_019_death_spiral_index_126d": {"inputs": ['assets', 'liabs'], "func": bsds_019_death_spiral_index_126d},
    "bsds_020_death_spiral_index_252d": {"inputs": ['assets', 'liabs'], "func": bsds_020_death_spiral_index_252d},
    "bsds_021_leverage_spiral_5d": {"inputs": ['assets', 'liabs'], "func": bsds_021_leverage_spiral_5d},
    "bsds_022_leverage_spiral_21d": {"inputs": ['assets', 'liabs'], "func": bsds_022_leverage_spiral_21d},
    "bsds_023_leverage_spiral_63d": {"inputs": ['assets', 'liabs'], "func": bsds_023_leverage_spiral_63d},
    "bsds_024_leverage_spiral_126d": {"inputs": ['assets', 'liabs'], "func": bsds_024_leverage_spiral_126d},
    "bsds_025_leverage_spiral_252d": {"inputs": ['assets', 'liabs'], "func": bsds_025_leverage_spiral_252d},
    "bsds_026_insolvency_momentum_5d": {"inputs": ['equity'], "func": bsds_026_insolvency_momentum_5d},
    "bsds_027_insolvency_momentum_21d": {"inputs": ['equity'], "func": bsds_027_insolvency_momentum_21d},
    "bsds_028_insolvency_momentum_63d": {"inputs": ['equity'], "func": bsds_028_insolvency_momentum_63d},
    "bsds_029_insolvency_momentum_126d": {"inputs": ['equity'], "func": bsds_029_insolvency_momentum_126d},
    "bsds_030_insolvency_momentum_252d": {"inputs": ['equity'], "func": bsds_030_insolvency_momentum_252d},
    "bsds_031_asset_quality_decay_5d": {"inputs": ['assets', 'ppnent'], "func": bsds_031_asset_quality_decay_5d},
    "bsds_032_asset_quality_decay_21d": {"inputs": ['assets', 'ppnent'], "func": bsds_032_asset_quality_decay_21d},
    "bsds_033_asset_quality_decay_63d": {"inputs": ['assets', 'ppnent'], "func": bsds_033_asset_quality_decay_63d},
    "bsds_034_asset_quality_decay_126d": {"inputs": ['assets', 'ppnent'], "func": bsds_034_asset_quality_decay_126d},
    "bsds_035_asset_quality_decay_252d": {"inputs": ['assets', 'ppnent'], "func": bsds_035_asset_quality_decay_252d},
    "bsds_036_working_cap_collapse_5d": {"inputs": ['workingcapital'], "func": bsds_036_working_cap_collapse_5d},
    "bsds_037_working_cap_collapse_21d": {"inputs": ['workingcapital'], "func": bsds_037_working_cap_collapse_21d},
    "bsds_038_working_cap_collapse_63d": {"inputs": ['workingcapital'], "func": bsds_038_working_cap_collapse_63d},
    "bsds_039_working_cap_collapse_126d": {"inputs": ['workingcapital'], "func": bsds_039_working_cap_collapse_126d},
    "bsds_040_working_cap_collapse_252d": {"inputs": ['workingcapital'], "func": bsds_040_working_cap_collapse_252d},
    "bsds_041_cash_drain_5d": {"inputs": ['cashnequiv'], "func": bsds_041_cash_drain_5d},
    "bsds_042_cash_drain_21d": {"inputs": ['cashnequiv'], "func": bsds_042_cash_drain_21d},
    "bsds_043_cash_drain_63d": {"inputs": ['cashnequiv'], "func": bsds_043_cash_drain_63d},
    "bsds_044_cash_drain_126d": {"inputs": ['cashnequiv'], "func": bsds_044_cash_drain_126d},
    "bsds_045_cash_drain_252d": {"inputs": ['cashnequiv'], "func": bsds_045_cash_drain_252d},
    "bsds_046_debt_accumulation_5d": {"inputs": ['debtn', 'debtc'], "func": bsds_046_debt_accumulation_5d},
    "bsds_047_debt_accumulation_21d": {"inputs": ['debtn', 'debtc'], "func": bsds_047_debt_accumulation_21d},
    "bsds_048_debt_accumulation_63d": {"inputs": ['debtn', 'debtc'], "func": bsds_048_debt_accumulation_63d},
    "bsds_049_debt_accumulation_126d": {"inputs": ['debtn', 'debtc'], "func": bsds_049_debt_accumulation_126d},
    "bsds_050_debt_accumulation_252d": {"inputs": ['debtn', 'debtc'], "func": bsds_050_debt_accumulation_252d},
    "bsds_051_asset_turnover_decay_5d": {"inputs": ['revenue', 'assets'], "func": bsds_051_asset_turnover_decay_5d},
    "bsds_052_asset_turnover_decay_21d": {"inputs": ['revenue', 'assets'], "func": bsds_052_asset_turnover_decay_21d},
    "bsds_053_asset_turnover_decay_63d": {"inputs": ['revenue', 'assets'], "func": bsds_053_asset_turnover_decay_63d},
    "bsds_054_asset_turnover_decay_126d": {"inputs": ['revenue', 'assets'], "func": bsds_054_asset_turnover_decay_126d},
    "bsds_055_asset_turnover_decay_252d": {"inputs": ['revenue', 'assets'], "func": bsds_055_asset_turnover_decay_252d},
    "bsds_056_roi_collapse_5d": {"inputs": ['netinc', 'assets'], "func": bsds_056_roi_collapse_5d},
    "bsds_057_roi_collapse_21d": {"inputs": ['netinc', 'assets'], "func": bsds_057_roi_collapse_21d},
    "bsds_058_roi_collapse_63d": {"inputs": ['netinc', 'assets'], "func": bsds_058_roi_collapse_63d},
    "bsds_059_roi_collapse_126d": {"inputs": ['netinc', 'assets'], "func": bsds_059_roi_collapse_126d},
    "bsds_060_roi_collapse_252d": {"inputs": ['netinc', 'assets'], "func": bsds_060_roi_collapse_252d},
    "bsds_061_death_spiral_z_5d": {"inputs": ['assets', 'liabs'], "func": bsds_061_death_spiral_z_5d},
    "bsds_062_death_spiral_z_21d": {"inputs": ['assets', 'liabs'], "func": bsds_062_death_spiral_z_21d},
    "bsds_063_death_spiral_z_63d": {"inputs": ['assets', 'liabs'], "func": bsds_063_death_spiral_z_63d},
    "bsds_064_death_spiral_z_126d": {"inputs": ['assets', 'liabs'], "func": bsds_064_death_spiral_z_126d},
    "bsds_065_death_spiral_z_252d": {"inputs": ['assets', 'liabs'], "func": bsds_065_death_spiral_z_252d},
    "bsds_066_equity_to_assets_decay_5d": {"inputs": ['assets', 'equity'], "func": bsds_066_equity_to_assets_decay_5d},
    "bsds_067_equity_to_assets_decay_21d": {"inputs": ['assets', 'equity'], "func": bsds_067_equity_to_assets_decay_21d},
    "bsds_068_equity_to_assets_decay_63d": {"inputs": ['assets', 'equity'], "func": bsds_068_equity_to_assets_decay_63d},
    "bsds_069_equity_to_assets_decay_126d": {"inputs": ['assets', 'equity'], "func": bsds_069_equity_to_assets_decay_126d},
    "bsds_070_equity_to_assets_decay_252d": {"inputs": ['assets', 'equity'], "func": bsds_070_equity_to_assets_decay_252d},
    "bsds_071_liab_to_rev_spike_5d": {"inputs": ['revenue', 'liabs'], "func": bsds_071_liab_to_rev_spike_5d},
    "bsds_072_liab_to_rev_spike_21d": {"inputs": ['revenue', 'liabs'], "func": bsds_072_liab_to_rev_spike_21d},
    "bsds_073_liab_to_rev_spike_63d": {"inputs": ['revenue', 'liabs'], "func": bsds_073_liab_to_rev_spike_63d},
    "bsds_074_liab_to_rev_spike_126d": {"inputs": ['revenue', 'liabs'], "func": bsds_074_liab_to_rev_spike_126d},
    "bsds_075_liab_to_rev_spike_252d": {"inputs": ['revenue', 'liabs'], "func": bsds_075_liab_to_rev_spike_252d},
}
