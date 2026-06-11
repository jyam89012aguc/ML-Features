"""
70_accounting_manipulation — Base Features 001-075
Domain: Beneish M-score proxies, Accruals/Assets
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

def acmn_001_dsi_5d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_001_dsi_5d"""
    return (_safe_div(inventory, cor / 365)).shift(5)

def acmn_002_dsi_21d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_002_dsi_21d"""
    return (_safe_div(inventory, cor / 365)).shift(21)

def acmn_003_dsi_63d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_003_dsi_63d"""
    return (_safe_div(inventory, cor / 365)).shift(63)

def acmn_004_dsi_126d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_004_dsi_126d"""
    return (_safe_div(inventory, cor / 365)).shift(126)

def acmn_005_dsi_252d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_005_dsi_252d"""
    return (_safe_div(inventory, cor / 365)).shift(252)

def acmn_006_dso_5d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_006_dso_5d"""
    return (_safe_div(receivables, revenue / 365)).shift(5)

def acmn_007_dso_21d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_007_dso_21d"""
    return (_safe_div(receivables, revenue / 365)).shift(21)

def acmn_008_dso_63d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_008_dso_63d"""
    return (_safe_div(receivables, revenue / 365)).shift(63)

def acmn_009_dso_126d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_009_dso_126d"""
    return (_safe_div(receivables, revenue / 365)).shift(126)

def acmn_010_dso_252d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_010_dso_252d"""
    return (_safe_div(receivables, revenue / 365)).shift(252)

def acmn_011_aqi_5d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_011_aqi_5d"""
    return (_safe_div(1 - (ppnent + currentassets) / assets, 1)).shift(5)

def acmn_012_aqi_21d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_012_aqi_21d"""
    return (_safe_div(1 - (ppnent + currentassets) / assets, 1)).shift(21)

def acmn_013_aqi_63d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_013_aqi_63d"""
    return (_safe_div(1 - (ppnent + currentassets) / assets, 1)).shift(63)

def acmn_014_aqi_126d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_014_aqi_126d"""
    return (_safe_div(1 - (ppnent + currentassets) / assets, 1)).shift(126)

def acmn_015_aqi_252d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_015_aqi_252d"""
    return (_safe_div(1 - (ppnent + currentassets) / assets, 1)).shift(252)

def acmn_016_sgi_5d(revenue: pd.Series) -> pd.Series:
    """acmn_016_sgi_5d"""
    return (revenue.pct_change(252)).shift(5)

def acmn_017_sgi_21d(revenue: pd.Series) -> pd.Series:
    """acmn_017_sgi_21d"""
    return (revenue.pct_change(252)).shift(21)

def acmn_018_sgi_63d(revenue: pd.Series) -> pd.Series:
    """acmn_018_sgi_63d"""
    return (revenue.pct_change(252)).shift(63)

def acmn_019_sgi_126d(revenue: pd.Series) -> pd.Series:
    """acmn_019_sgi_126d"""
    return (revenue.pct_change(252)).shift(126)

def acmn_020_sgi_252d(revenue: pd.Series) -> pd.Series:
    """acmn_020_sgi_252d"""
    return (revenue.pct_change(252)).shift(252)

def acmn_021_depi_5d(ppnent: pd.Series) -> pd.Series:
    """acmn_021_depi_5d"""
    return _safe_div(_safe_div(depamor.shift(252), ppnent.shift(252) + depamor.shift(252)), _safe_div(depamor, ppnent + depamor))

def acmn_022_depi_21d(ppnent: pd.Series) -> pd.Series:
    """acmn_022_depi_21d"""
    return _safe_div(_safe_div(depamor.shift(252), ppnent.shift(252) + depamor.shift(252)), _safe_div(depamor, ppnent + depamor))

def acmn_023_depi_63d(ppnent: pd.Series) -> pd.Series:
    """acmn_023_depi_63d"""
    return _safe_div(_safe_div(depamor.shift(252), ppnent.shift(252) + depamor.shift(252)), _safe_div(depamor, ppnent + depamor))

def acmn_024_depi_126d(ppnent: pd.Series) -> pd.Series:
    """acmn_024_depi_126d"""
    return _safe_div(_safe_div(depamor.shift(252), ppnent.shift(252) + depamor.shift(252)), _safe_div(depamor, ppnent + depamor))

def acmn_025_depi_252d(ppnent: pd.Series) -> pd.Series:
    """acmn_025_depi_252d"""
    return _safe_div(_safe_div(depamor.shift(252), ppnent.shift(252) + depamor.shift(252)), _safe_div(depamor, ppnent + depamor))

def acmn_026_sgai_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """acmn_026_sgai_5d"""
    return _safe_div(_safe_div(sga, revenue), _safe_div(sga.shift(252), revenue.shift(252)))

def acmn_027_sgai_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """acmn_027_sgai_21d"""
    return _safe_div(_safe_div(sga, revenue), _safe_div(sga.shift(252), revenue.shift(252)))

def acmn_028_sgai_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """acmn_028_sgai_63d"""
    return _safe_div(_safe_div(sga, revenue), _safe_div(sga.shift(252), revenue.shift(252)))

def acmn_029_sgai_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """acmn_029_sgai_126d"""
    return _safe_div(_safe_div(sga, revenue), _safe_div(sga.shift(252), revenue.shift(252)))

def acmn_030_sgai_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """acmn_030_sgai_252d"""
    return _safe_div(_safe_div(sga, revenue), _safe_div(sga.shift(252), revenue.shift(252)))

def acmn_031_lvgi_5d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """acmn_031_lvgi_5d"""
    return _safe_div(_safe_div(liabs, assets), _safe_div(liabs.shift(252), assets.shift(252)))

def acmn_032_lvgi_21d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """acmn_032_lvgi_21d"""
    return _safe_div(_safe_div(liabs, assets), _safe_div(liabs.shift(252), assets.shift(252)))

def acmn_033_lvgi_63d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """acmn_033_lvgi_63d"""
    return _safe_div(_safe_div(liabs, assets), _safe_div(liabs.shift(252), assets.shift(252)))

def acmn_034_lvgi_126d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """acmn_034_lvgi_126d"""
    return _safe_div(_safe_div(liabs, assets), _safe_div(liabs.shift(252), assets.shift(252)))

def acmn_035_lvgi_252d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """acmn_035_lvgi_252d"""
    return _safe_div(_safe_div(liabs, assets), _safe_div(liabs.shift(252), assets.shift(252)))

def acmn_036_tata_5d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_036_tata_5d"""
    return (_safe_div(netinc - ocf, assets)).shift(5)

def acmn_037_tata_21d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_037_tata_21d"""
    return (_safe_div(netinc - ocf, assets)).shift(21)

def acmn_038_tata_63d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_038_tata_63d"""
    return (_safe_div(netinc - ocf, assets)).shift(63)

def acmn_039_tata_126d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_039_tata_126d"""
    return (_safe_div(netinc - ocf, assets)).shift(126)

def acmn_040_tata_252d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_040_tata_252d"""
    return (_safe_div(netinc - ocf, assets)).shift(252)

def acmn_041_m_score_proxy_5d(revenue: pd.Series, netinc: pd.Series, cor: pd.Series, ocf: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_041_m_score_proxy_5d"""
    return ((_safe_div(receivables, revenue) + _safe_div(inventory, cor) + _safe_div(netinc - ocf, assets))).shift(5)

def acmn_042_m_score_proxy_21d(revenue: pd.Series, netinc: pd.Series, cor: pd.Series, ocf: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_042_m_score_proxy_21d"""
    return ((_safe_div(receivables, revenue) + _safe_div(inventory, cor) + _safe_div(netinc - ocf, assets))).shift(21)

def acmn_043_m_score_proxy_63d(revenue: pd.Series, netinc: pd.Series, cor: pd.Series, ocf: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_043_m_score_proxy_63d"""
    return ((_safe_div(receivables, revenue) + _safe_div(inventory, cor) + _safe_div(netinc - ocf, assets))).shift(63)

def acmn_044_m_score_proxy_126d(revenue: pd.Series, netinc: pd.Series, cor: pd.Series, ocf: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_044_m_score_proxy_126d"""
    return ((_safe_div(receivables, revenue) + _safe_div(inventory, cor) + _safe_div(netinc - ocf, assets))).shift(126)

def acmn_045_m_score_proxy_252d(revenue: pd.Series, netinc: pd.Series, cor: pd.Series, ocf: pd.Series, assets: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_045_m_score_proxy_252d"""
    return ((_safe_div(receivables, revenue) + _safe_div(inventory, cor) + _safe_div(netinc - ocf, assets))).shift(252)

def acmn_046_accrual_z_5d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_046_accrual_z_5d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(5)

def acmn_047_accrual_z_21d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_047_accrual_z_21d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(21)

def acmn_048_accrual_z_63d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_048_accrual_z_63d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(63)

def acmn_049_accrual_z_126d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_049_accrual_z_126d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(126)

def acmn_050_accrual_z_252d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_050_accrual_z_252d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(252)

def acmn_051_revenue_inflation_proxy_5d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_051_revenue_inflation_proxy_5d"""
    return (_safe_div(receivables.diff(252), revenue.diff(252))).shift(5)

def acmn_052_revenue_inflation_proxy_21d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_052_revenue_inflation_proxy_21d"""
    return (_safe_div(receivables.diff(252), revenue.diff(252))).shift(21)

def acmn_053_revenue_inflation_proxy_63d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_053_revenue_inflation_proxy_63d"""
    return (_safe_div(receivables.diff(252), revenue.diff(252))).shift(63)

def acmn_054_revenue_inflation_proxy_126d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_054_revenue_inflation_proxy_126d"""
    return (_safe_div(receivables.diff(252), revenue.diff(252))).shift(126)

def acmn_055_revenue_inflation_proxy_252d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_055_revenue_inflation_proxy_252d"""
    return (_safe_div(receivables.diff(252), revenue.diff(252))).shift(252)

def acmn_056_inventory_inflation_proxy_5d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_056_inventory_inflation_proxy_5d"""
    return (_safe_div(inventory.diff(252), cor.diff(252))).shift(5)

def acmn_057_inventory_inflation_proxy_21d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_057_inventory_inflation_proxy_21d"""
    return (_safe_div(inventory.diff(252), cor.diff(252))).shift(21)

def acmn_058_inventory_inflation_proxy_63d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_058_inventory_inflation_proxy_63d"""
    return (_safe_div(inventory.diff(252), cor.diff(252))).shift(63)

def acmn_059_inventory_inflation_proxy_126d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_059_inventory_inflation_proxy_126d"""
    return (_safe_div(inventory.diff(252), cor.diff(252))).shift(126)

def acmn_060_inventory_inflation_proxy_252d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_060_inventory_inflation_proxy_252d"""
    return (_safe_div(inventory.diff(252), cor.diff(252))).shift(252)

def acmn_061_asset_quality_decay_5d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_061_asset_quality_decay_5d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(5)

def acmn_062_asset_quality_decay_21d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_062_asset_quality_decay_21d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(21)

def acmn_063_asset_quality_decay_63d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_063_asset_quality_decay_63d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(63)

def acmn_064_asset_quality_decay_126d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_064_asset_quality_decay_126d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(126)

def acmn_065_asset_quality_decay_252d(assets: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_065_asset_quality_decay_252d"""
    return ((_safe_div(ppnent, assets)).diff(252)).shift(252)

def acmn_066_soft_assets_rat_5d(assets: pd.Series, cashnequiv: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_066_soft_assets_rat_5d"""
    return (_safe_div(assets - ppnent - cashnequiv, assets)).shift(5)

def acmn_067_soft_assets_rat_21d(assets: pd.Series, cashnequiv: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_067_soft_assets_rat_21d"""
    return (_safe_div(assets - ppnent - cashnequiv, assets)).shift(21)

def acmn_068_soft_assets_rat_63d(assets: pd.Series, cashnequiv: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_068_soft_assets_rat_63d"""
    return (_safe_div(assets - ppnent - cashnequiv, assets)).shift(63)

def acmn_069_soft_assets_rat_126d(assets: pd.Series, cashnequiv: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_069_soft_assets_rat_126d"""
    return (_safe_div(assets - ppnent - cashnequiv, assets)).shift(126)

def acmn_070_soft_assets_rat_252d(assets: pd.Series, cashnequiv: pd.Series, ppnent: pd.Series) -> pd.Series:
    """acmn_070_soft_assets_rat_252d"""
    return (_safe_div(assets - ppnent - cashnequiv, assets)).shift(252)

def acmn_071_earnings_smoothness_5d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_071_earnings_smoothness_5d"""
    return (_safe_div(_rolling_std(netinc, 252), _rolling_std(ocf, 252))).shift(5)

def acmn_072_earnings_smoothness_21d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_072_earnings_smoothness_21d"""
    return (_safe_div(_rolling_std(netinc, 252), _rolling_std(ocf, 252))).shift(21)

def acmn_073_earnings_smoothness_63d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_073_earnings_smoothness_63d"""
    return (_safe_div(_rolling_std(netinc, 252), _rolling_std(ocf, 252))).shift(63)

def acmn_074_earnings_smoothness_126d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_074_earnings_smoothness_126d"""
    return (_safe_div(_rolling_std(netinc, 252), _rolling_std(ocf, 252))).shift(126)

def acmn_075_earnings_smoothness_252d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_075_earnings_smoothness_252d"""
    return (_safe_div(_rolling_std(netinc, 252), _rolling_std(ocf, 252))).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V70_REGISTRY = {
    "acmn_001_dsi_5d": {"inputs": ['cor', 'inventory'], "func": acmn_001_dsi_5d},
    "acmn_002_dsi_21d": {"inputs": ['cor', 'inventory'], "func": acmn_002_dsi_21d},
    "acmn_003_dsi_63d": {"inputs": ['cor', 'inventory'], "func": acmn_003_dsi_63d},
    "acmn_004_dsi_126d": {"inputs": ['cor', 'inventory'], "func": acmn_004_dsi_126d},
    "acmn_005_dsi_252d": {"inputs": ['cor', 'inventory'], "func": acmn_005_dsi_252d},
    "acmn_006_dso_5d": {"inputs": ['revenue', 'receivables'], "func": acmn_006_dso_5d},
    "acmn_007_dso_21d": {"inputs": ['revenue', 'receivables'], "func": acmn_007_dso_21d},
    "acmn_008_dso_63d": {"inputs": ['revenue', 'receivables'], "func": acmn_008_dso_63d},
    "acmn_009_dso_126d": {"inputs": ['revenue', 'receivables'], "func": acmn_009_dso_126d},
    "acmn_010_dso_252d": {"inputs": ['revenue', 'receivables'], "func": acmn_010_dso_252d},
    "acmn_011_aqi_5d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_011_aqi_5d},
    "acmn_012_aqi_21d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_012_aqi_21d},
    "acmn_013_aqi_63d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_013_aqi_63d},
    "acmn_014_aqi_126d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_014_aqi_126d},
    "acmn_015_aqi_252d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_015_aqi_252d},
    "acmn_016_sgi_5d": {"inputs": ['revenue'], "func": acmn_016_sgi_5d},
    "acmn_017_sgi_21d": {"inputs": ['revenue'], "func": acmn_017_sgi_21d},
    "acmn_018_sgi_63d": {"inputs": ['revenue'], "func": acmn_018_sgi_63d},
    "acmn_019_sgi_126d": {"inputs": ['revenue'], "func": acmn_019_sgi_126d},
    "acmn_020_sgi_252d": {"inputs": ['revenue'], "func": acmn_020_sgi_252d},
    "acmn_021_depi_5d": {"inputs": ['ppnent'], "func": acmn_021_depi_5d},
    "acmn_022_depi_21d": {"inputs": ['ppnent'], "func": acmn_022_depi_21d},
    "acmn_023_depi_63d": {"inputs": ['ppnent'], "func": acmn_023_depi_63d},
    "acmn_024_depi_126d": {"inputs": ['ppnent'], "func": acmn_024_depi_126d},
    "acmn_025_depi_252d": {"inputs": ['ppnent'], "func": acmn_025_depi_252d},
    "acmn_026_sgai_5d": {"inputs": ['revenue', 'sga'], "func": acmn_026_sgai_5d},
    "acmn_027_sgai_21d": {"inputs": ['revenue', 'sga'], "func": acmn_027_sgai_21d},
    "acmn_028_sgai_63d": {"inputs": ['revenue', 'sga'], "func": acmn_028_sgai_63d},
    "acmn_029_sgai_126d": {"inputs": ['revenue', 'sga'], "func": acmn_029_sgai_126d},
    "acmn_030_sgai_252d": {"inputs": ['revenue', 'sga'], "func": acmn_030_sgai_252d},
    "acmn_031_lvgi_5d": {"inputs": ['assets', 'liabs'], "func": acmn_031_lvgi_5d},
    "acmn_032_lvgi_21d": {"inputs": ['assets', 'liabs'], "func": acmn_032_lvgi_21d},
    "acmn_033_lvgi_63d": {"inputs": ['assets', 'liabs'], "func": acmn_033_lvgi_63d},
    "acmn_034_lvgi_126d": {"inputs": ['assets', 'liabs'], "func": acmn_034_lvgi_126d},
    "acmn_035_lvgi_252d": {"inputs": ['assets', 'liabs'], "func": acmn_035_lvgi_252d},
    "acmn_036_tata_5d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_036_tata_5d},
    "acmn_037_tata_21d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_037_tata_21d},
    "acmn_038_tata_63d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_038_tata_63d},
    "acmn_039_tata_126d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_039_tata_126d},
    "acmn_040_tata_252d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_040_tata_252d},
    "acmn_041_m_score_proxy_5d": {"inputs": ['revenue', 'netinc', 'cor', 'ocf', 'assets', 'inventory', 'receivables'], "func": acmn_041_m_score_proxy_5d},
    "acmn_042_m_score_proxy_21d": {"inputs": ['revenue', 'netinc', 'cor', 'ocf', 'assets', 'inventory', 'receivables'], "func": acmn_042_m_score_proxy_21d},
    "acmn_043_m_score_proxy_63d": {"inputs": ['revenue', 'netinc', 'cor', 'ocf', 'assets', 'inventory', 'receivables'], "func": acmn_043_m_score_proxy_63d},
    "acmn_044_m_score_proxy_126d": {"inputs": ['revenue', 'netinc', 'cor', 'ocf', 'assets', 'inventory', 'receivables'], "func": acmn_044_m_score_proxy_126d},
    "acmn_045_m_score_proxy_252d": {"inputs": ['revenue', 'netinc', 'cor', 'ocf', 'assets', 'inventory', 'receivables'], "func": acmn_045_m_score_proxy_252d},
    "acmn_046_accrual_z_5d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_046_accrual_z_5d},
    "acmn_047_accrual_z_21d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_047_accrual_z_21d},
    "acmn_048_accrual_z_63d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_048_accrual_z_63d},
    "acmn_049_accrual_z_126d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_049_accrual_z_126d},
    "acmn_050_accrual_z_252d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_050_accrual_z_252d},
    "acmn_051_revenue_inflation_proxy_5d": {"inputs": ['revenue', 'receivables'], "func": acmn_051_revenue_inflation_proxy_5d},
    "acmn_052_revenue_inflation_proxy_21d": {"inputs": ['revenue', 'receivables'], "func": acmn_052_revenue_inflation_proxy_21d},
    "acmn_053_revenue_inflation_proxy_63d": {"inputs": ['revenue', 'receivables'], "func": acmn_053_revenue_inflation_proxy_63d},
    "acmn_054_revenue_inflation_proxy_126d": {"inputs": ['revenue', 'receivables'], "func": acmn_054_revenue_inflation_proxy_126d},
    "acmn_055_revenue_inflation_proxy_252d": {"inputs": ['revenue', 'receivables'], "func": acmn_055_revenue_inflation_proxy_252d},
    "acmn_056_inventory_inflation_proxy_5d": {"inputs": ['cor', 'inventory'], "func": acmn_056_inventory_inflation_proxy_5d},
    "acmn_057_inventory_inflation_proxy_21d": {"inputs": ['cor', 'inventory'], "func": acmn_057_inventory_inflation_proxy_21d},
    "acmn_058_inventory_inflation_proxy_63d": {"inputs": ['cor', 'inventory'], "func": acmn_058_inventory_inflation_proxy_63d},
    "acmn_059_inventory_inflation_proxy_126d": {"inputs": ['cor', 'inventory'], "func": acmn_059_inventory_inflation_proxy_126d},
    "acmn_060_inventory_inflation_proxy_252d": {"inputs": ['cor', 'inventory'], "func": acmn_060_inventory_inflation_proxy_252d},
    "acmn_061_asset_quality_decay_5d": {"inputs": ['assets', 'ppnent'], "func": acmn_061_asset_quality_decay_5d},
    "acmn_062_asset_quality_decay_21d": {"inputs": ['assets', 'ppnent'], "func": acmn_062_asset_quality_decay_21d},
    "acmn_063_asset_quality_decay_63d": {"inputs": ['assets', 'ppnent'], "func": acmn_063_asset_quality_decay_63d},
    "acmn_064_asset_quality_decay_126d": {"inputs": ['assets', 'ppnent'], "func": acmn_064_asset_quality_decay_126d},
    "acmn_065_asset_quality_decay_252d": {"inputs": ['assets', 'ppnent'], "func": acmn_065_asset_quality_decay_252d},
    "acmn_066_soft_assets_rat_5d": {"inputs": ['assets', 'cashnequiv', 'ppnent'], "func": acmn_066_soft_assets_rat_5d},
    "acmn_067_soft_assets_rat_21d": {"inputs": ['assets', 'cashnequiv', 'ppnent'], "func": acmn_067_soft_assets_rat_21d},
    "acmn_068_soft_assets_rat_63d": {"inputs": ['assets', 'cashnequiv', 'ppnent'], "func": acmn_068_soft_assets_rat_63d},
    "acmn_069_soft_assets_rat_126d": {"inputs": ['assets', 'cashnequiv', 'ppnent'], "func": acmn_069_soft_assets_rat_126d},
    "acmn_070_soft_assets_rat_252d": {"inputs": ['assets', 'cashnequiv', 'ppnent'], "func": acmn_070_soft_assets_rat_252d},
    "acmn_071_earnings_smoothness_5d": {"inputs": ['netinc', 'ocf'], "func": acmn_071_earnings_smoothness_5d},
    "acmn_072_earnings_smoothness_21d": {"inputs": ['netinc', 'ocf'], "func": acmn_072_earnings_smoothness_21d},
    "acmn_073_earnings_smoothness_63d": {"inputs": ['netinc', 'ocf'], "func": acmn_073_earnings_smoothness_63d},
    "acmn_074_earnings_smoothness_126d": {"inputs": ['netinc', 'ocf'], "func": acmn_074_earnings_smoothness_126d},
    "acmn_075_earnings_smoothness_252d": {"inputs": ['netinc', 'ocf'], "func": acmn_075_earnings_smoothness_252d},
}
