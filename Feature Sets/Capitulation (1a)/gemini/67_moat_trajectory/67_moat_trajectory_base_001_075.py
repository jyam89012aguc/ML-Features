"""
67_moat_trajectory — Base Features 001-075
Domain: ROIC persistence, Margin leadership
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

def moat_001_roic_5d(ebit: pd.Series, assets: pd.Series, liabs: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """moat_001_roic_5d"""
    return (_safe_div(ebit, assets - liabs + debtn.fillna(0) + debtc.fillna(0))).shift(5)

def moat_002_roic_21d(ebit: pd.Series, assets: pd.Series, liabs: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """moat_002_roic_21d"""
    return (_safe_div(ebit, assets - liabs + debtn.fillna(0) + debtc.fillna(0))).shift(21)

def moat_003_roic_63d(ebit: pd.Series, assets: pd.Series, liabs: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """moat_003_roic_63d"""
    return (_safe_div(ebit, assets - liabs + debtn.fillna(0) + debtc.fillna(0))).shift(63)

def moat_004_roic_126d(ebit: pd.Series, assets: pd.Series, liabs: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """moat_004_roic_126d"""
    return (_safe_div(ebit, assets - liabs + debtn.fillna(0) + debtc.fillna(0))).shift(126)

def moat_005_roic_252d(ebit: pd.Series, assets: pd.Series, liabs: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """moat_005_roic_252d"""
    return (_safe_div(ebit, assets - liabs + debtn.fillna(0) + debtc.fillna(0))).shift(252)

def moat_006_roe_5d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_006_roe_5d"""
    return (_safe_div(netinc, equity)).shift(5)

def moat_007_roe_21d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_007_roe_21d"""
    return (_safe_div(netinc, equity)).shift(21)

def moat_008_roe_63d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_008_roe_63d"""
    return (_safe_div(netinc, equity)).shift(63)

def moat_009_roe_126d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_009_roe_126d"""
    return (_safe_div(netinc, equity)).shift(126)

def moat_010_roe_252d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_010_roe_252d"""
    return (_safe_div(netinc, equity)).shift(252)

def moat_011_roa_5d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_011_roa_5d"""
    return (_safe_div(netinc, assets)).shift(5)

def moat_012_roa_21d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_012_roa_21d"""
    return (_safe_div(netinc, assets)).shift(21)

def moat_013_roa_63d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_013_roa_63d"""
    return (_safe_div(netinc, assets)).shift(63)

def moat_014_roa_126d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_014_roa_126d"""
    return (_safe_div(netinc, assets)).shift(126)

def moat_015_roa_252d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_015_roa_252d"""
    return (_safe_div(netinc, assets)).shift(252)

def moat_016_roic_chg_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_016_roic_chg_5d"""
    return ((_safe_div(ebit, assets)).diff(252)).shift(5)

def moat_017_roic_chg_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_017_roic_chg_21d"""
    return ((_safe_div(ebit, assets)).diff(252)).shift(21)

def moat_018_roic_chg_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_018_roic_chg_63d"""
    return ((_safe_div(ebit, assets)).diff(252)).shift(63)

def moat_019_roic_chg_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_019_roic_chg_126d"""
    return ((_safe_div(ebit, assets)).diff(252)).shift(126)

def moat_020_roic_chg_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_020_roic_chg_252d"""
    return ((_safe_div(ebit, assets)).diff(252)).shift(252)

def moat_021_roe_chg_5d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_021_roe_chg_5d"""
    return ((_safe_div(netinc, equity)).diff(252)).shift(5)

def moat_022_roe_chg_21d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_022_roe_chg_21d"""
    return ((_safe_div(netinc, equity)).diff(252)).shift(21)

def moat_023_roe_chg_63d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_023_roe_chg_63d"""
    return ((_safe_div(netinc, equity)).diff(252)).shift(63)

def moat_024_roe_chg_126d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_024_roe_chg_126d"""
    return ((_safe_div(netinc, equity)).diff(252)).shift(126)

def moat_025_roe_chg_252d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_025_roe_chg_252d"""
    return ((_safe_div(netinc, equity)).diff(252)).shift(252)

def moat_026_roic_z_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_026_roic_z_5d"""
    return (_zscore_rolling(_safe_div(ebit, assets), 1260)).shift(5)

def moat_027_roic_z_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_027_roic_z_21d"""
    return (_zscore_rolling(_safe_div(ebit, assets), 1260)).shift(21)

def moat_028_roic_z_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_028_roic_z_63d"""
    return (_zscore_rolling(_safe_div(ebit, assets), 1260)).shift(63)

def moat_029_roic_z_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_029_roic_z_126d"""
    return (_zscore_rolling(_safe_div(ebit, assets), 1260)).shift(126)

def moat_030_roic_z_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_030_roic_z_252d"""
    return (_zscore_rolling(_safe_div(ebit, assets), 1260)).shift(252)

def moat_031_gp_m_5d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """moat_031_gp_m_5d"""
    return (_safe_div(gp, revenue)).shift(5)

def moat_032_gp_m_21d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """moat_032_gp_m_21d"""
    return (_safe_div(gp, revenue)).shift(21)

def moat_033_gp_m_63d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """moat_033_gp_m_63d"""
    return (_safe_div(gp, revenue)).shift(63)

def moat_034_gp_m_126d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """moat_034_gp_m_126d"""
    return (_safe_div(gp, revenue)).shift(126)

def moat_035_gp_m_252d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """moat_035_gp_m_252d"""
    return (_safe_div(gp, revenue)).shift(252)

def moat_036_ebit_m_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_036_ebit_m_5d"""
    return (_safe_div(ebit, revenue)).shift(5)

def moat_037_ebit_m_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_037_ebit_m_21d"""
    return (_safe_div(ebit, revenue)).shift(21)

def moat_038_ebit_m_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_038_ebit_m_63d"""
    return (_safe_div(ebit, revenue)).shift(63)

def moat_039_ebit_m_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_039_ebit_m_126d"""
    return (_safe_div(ebit, revenue)).shift(126)

def moat_040_ebit_m_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_040_ebit_m_252d"""
    return (_safe_div(ebit, revenue)).shift(252)

def moat_041_asset_turn_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_041_asset_turn_5d"""
    return (_safe_div(revenue, assets)).shift(5)

def moat_042_asset_turn_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_042_asset_turn_21d"""
    return (_safe_div(revenue, assets)).shift(21)

def moat_043_asset_turn_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_043_asset_turn_63d"""
    return (_safe_div(revenue, assets)).shift(63)

def moat_044_asset_turn_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_044_asset_turn_126d"""
    return (_safe_div(revenue, assets)).shift(126)

def moat_045_asset_turn_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_045_asset_turn_252d"""
    return (_safe_div(revenue, assets)).shift(252)

def moat_046_moat_index_5d(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_046_moat_index_5d"""
    return (_safe_div(ebit, revenue) * _safe_div(revenue, assets)).shift(5)

def moat_047_moat_index_21d(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_047_moat_index_21d"""
    return (_safe_div(ebit, revenue) * _safe_div(revenue, assets)).shift(21)

def moat_048_moat_index_63d(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_048_moat_index_63d"""
    return (_safe_div(ebit, revenue) * _safe_div(revenue, assets)).shift(63)

def moat_049_moat_index_126d(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_049_moat_index_126d"""
    return (_safe_div(ebit, revenue) * _safe_div(revenue, assets)).shift(126)

def moat_050_moat_index_252d(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_050_moat_index_252d"""
    return (_safe_div(ebit, revenue) * _safe_div(revenue, assets)).shift(252)

def moat_051_excess_return_5d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_051_excess_return_5d"""
    return (_safe_div(netinc, equity) - 0.10).shift(5)

def moat_052_excess_return_21d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_052_excess_return_21d"""
    return (_safe_div(netinc, equity) - 0.10).shift(21)

def moat_053_excess_return_63d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_053_excess_return_63d"""
    return (_safe_div(netinc, equity) - 0.10).shift(63)

def moat_054_excess_return_126d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_054_excess_return_126d"""
    return (_safe_div(netinc, equity) - 0.10).shift(126)

def moat_055_excess_return_252d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_055_excess_return_252d"""
    return (_safe_div(netinc, equity) - 0.10).shift(252)

def moat_056_roic_persistence_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_056_roic_persistence_5d"""
    return (_safe_div(_safe_div(ebit, assets), _rolling_mean(_safe_div(ebit, assets), 1260))).shift(5)

def moat_057_roic_persistence_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_057_roic_persistence_21d"""
    return (_safe_div(_safe_div(ebit, assets), _rolling_mean(_safe_div(ebit, assets), 1260))).shift(21)

def moat_058_roic_persistence_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_058_roic_persistence_63d"""
    return (_safe_div(_safe_div(ebit, assets), _rolling_mean(_safe_div(ebit, assets), 1260))).shift(63)

def moat_059_roic_persistence_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_059_roic_persistence_126d"""
    return (_safe_div(_safe_div(ebit, assets), _rolling_mean(_safe_div(ebit, assets), 1260))).shift(126)

def moat_060_roic_persistence_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_060_roic_persistence_252d"""
    return (_safe_div(_safe_div(ebit, assets), _rolling_mean(_safe_div(ebit, assets), 1260))).shift(252)

def moat_061_margin_leadership_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_061_margin_leadership_5d"""
    return (_safe_div(_safe_div(ebit, revenue), _rolling_max(_safe_div(ebit, revenue), 1260))).shift(5)

def moat_062_margin_leadership_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_062_margin_leadership_21d"""
    return (_safe_div(_safe_div(ebit, revenue), _rolling_max(_safe_div(ebit, revenue), 1260))).shift(21)

def moat_063_margin_leadership_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_063_margin_leadership_63d"""
    return (_safe_div(_safe_div(ebit, revenue), _rolling_max(_safe_div(ebit, revenue), 1260))).shift(63)

def moat_064_margin_leadership_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_064_margin_leadership_126d"""
    return (_safe_div(_safe_div(ebit, revenue), _rolling_max(_safe_div(ebit, revenue), 1260))).shift(126)

def moat_065_margin_leadership_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_065_margin_leadership_252d"""
    return (_safe_div(_safe_div(ebit, revenue), _rolling_max(_safe_div(ebit, revenue), 1260))).shift(252)

def moat_066_roe_persistence_5d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_066_roe_persistence_5d"""
    return (_safe_div(_safe_div(netinc, equity), _rolling_mean(_safe_div(netinc, equity), 1260))).shift(5)

def moat_067_roe_persistence_21d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_067_roe_persistence_21d"""
    return (_safe_div(_safe_div(netinc, equity), _rolling_mean(_safe_div(netinc, equity), 1260))).shift(21)

def moat_068_roe_persistence_63d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_068_roe_persistence_63d"""
    return (_safe_div(_safe_div(netinc, equity), _rolling_mean(_safe_div(netinc, equity), 1260))).shift(63)

def moat_069_roe_persistence_126d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_069_roe_persistence_126d"""
    return (_safe_div(_safe_div(netinc, equity), _rolling_mean(_safe_div(netinc, equity), 1260))).shift(126)

def moat_070_roe_persistence_252d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_070_roe_persistence_252d"""
    return (_safe_div(_safe_div(netinc, equity), _rolling_mean(_safe_div(netinc, equity), 1260))).shift(252)

def moat_071_roic_vol_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_071_roic_vol_5d"""
    return (_rolling_std(_safe_div(ebit, assets), 252)).shift(5)

def moat_072_roic_vol_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_072_roic_vol_21d"""
    return (_rolling_std(_safe_div(ebit, assets), 252)).shift(21)

def moat_073_roic_vol_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_073_roic_vol_63d"""
    return (_rolling_std(_safe_div(ebit, assets), 252)).shift(63)

def moat_074_roic_vol_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_074_roic_vol_126d"""
    return (_rolling_std(_safe_div(ebit, assets), 252)).shift(126)

def moat_075_roic_vol_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_075_roic_vol_252d"""
    return (_rolling_std(_safe_div(ebit, assets), 252)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V67_REGISTRY = {
    "moat_001_roic_5d": {"inputs": ['ebit', 'assets', 'liabs', 'debtn', 'debtc'], "func": moat_001_roic_5d},
    "moat_002_roic_21d": {"inputs": ['ebit', 'assets', 'liabs', 'debtn', 'debtc'], "func": moat_002_roic_21d},
    "moat_003_roic_63d": {"inputs": ['ebit', 'assets', 'liabs', 'debtn', 'debtc'], "func": moat_003_roic_63d},
    "moat_004_roic_126d": {"inputs": ['ebit', 'assets', 'liabs', 'debtn', 'debtc'], "func": moat_004_roic_126d},
    "moat_005_roic_252d": {"inputs": ['ebit', 'assets', 'liabs', 'debtn', 'debtc'], "func": moat_005_roic_252d},
    "moat_006_roe_5d": {"inputs": ['netinc', 'equity'], "func": moat_006_roe_5d},
    "moat_007_roe_21d": {"inputs": ['netinc', 'equity'], "func": moat_007_roe_21d},
    "moat_008_roe_63d": {"inputs": ['netinc', 'equity'], "func": moat_008_roe_63d},
    "moat_009_roe_126d": {"inputs": ['netinc', 'equity'], "func": moat_009_roe_126d},
    "moat_010_roe_252d": {"inputs": ['netinc', 'equity'], "func": moat_010_roe_252d},
    "moat_011_roa_5d": {"inputs": ['netinc', 'assets'], "func": moat_011_roa_5d},
    "moat_012_roa_21d": {"inputs": ['netinc', 'assets'], "func": moat_012_roa_21d},
    "moat_013_roa_63d": {"inputs": ['netinc', 'assets'], "func": moat_013_roa_63d},
    "moat_014_roa_126d": {"inputs": ['netinc', 'assets'], "func": moat_014_roa_126d},
    "moat_015_roa_252d": {"inputs": ['netinc', 'assets'], "func": moat_015_roa_252d},
    "moat_016_roic_chg_5d": {"inputs": ['ebit', 'assets'], "func": moat_016_roic_chg_5d},
    "moat_017_roic_chg_21d": {"inputs": ['ebit', 'assets'], "func": moat_017_roic_chg_21d},
    "moat_018_roic_chg_63d": {"inputs": ['ebit', 'assets'], "func": moat_018_roic_chg_63d},
    "moat_019_roic_chg_126d": {"inputs": ['ebit', 'assets'], "func": moat_019_roic_chg_126d},
    "moat_020_roic_chg_252d": {"inputs": ['ebit', 'assets'], "func": moat_020_roic_chg_252d},
    "moat_021_roe_chg_5d": {"inputs": ['netinc', 'equity'], "func": moat_021_roe_chg_5d},
    "moat_022_roe_chg_21d": {"inputs": ['netinc', 'equity'], "func": moat_022_roe_chg_21d},
    "moat_023_roe_chg_63d": {"inputs": ['netinc', 'equity'], "func": moat_023_roe_chg_63d},
    "moat_024_roe_chg_126d": {"inputs": ['netinc', 'equity'], "func": moat_024_roe_chg_126d},
    "moat_025_roe_chg_252d": {"inputs": ['netinc', 'equity'], "func": moat_025_roe_chg_252d},
    "moat_026_roic_z_5d": {"inputs": ['ebit', 'assets'], "func": moat_026_roic_z_5d},
    "moat_027_roic_z_21d": {"inputs": ['ebit', 'assets'], "func": moat_027_roic_z_21d},
    "moat_028_roic_z_63d": {"inputs": ['ebit', 'assets'], "func": moat_028_roic_z_63d},
    "moat_029_roic_z_126d": {"inputs": ['ebit', 'assets'], "func": moat_029_roic_z_126d},
    "moat_030_roic_z_252d": {"inputs": ['ebit', 'assets'], "func": moat_030_roic_z_252d},
    "moat_031_gp_m_5d": {"inputs": ['revenue', 'gp'], "func": moat_031_gp_m_5d},
    "moat_032_gp_m_21d": {"inputs": ['revenue', 'gp'], "func": moat_032_gp_m_21d},
    "moat_033_gp_m_63d": {"inputs": ['revenue', 'gp'], "func": moat_033_gp_m_63d},
    "moat_034_gp_m_126d": {"inputs": ['revenue', 'gp'], "func": moat_034_gp_m_126d},
    "moat_035_gp_m_252d": {"inputs": ['revenue', 'gp'], "func": moat_035_gp_m_252d},
    "moat_036_ebit_m_5d": {"inputs": ['revenue', 'ebit'], "func": moat_036_ebit_m_5d},
    "moat_037_ebit_m_21d": {"inputs": ['revenue', 'ebit'], "func": moat_037_ebit_m_21d},
    "moat_038_ebit_m_63d": {"inputs": ['revenue', 'ebit'], "func": moat_038_ebit_m_63d},
    "moat_039_ebit_m_126d": {"inputs": ['revenue', 'ebit'], "func": moat_039_ebit_m_126d},
    "moat_040_ebit_m_252d": {"inputs": ['revenue', 'ebit'], "func": moat_040_ebit_m_252d},
    "moat_041_asset_turn_5d": {"inputs": ['revenue', 'assets'], "func": moat_041_asset_turn_5d},
    "moat_042_asset_turn_21d": {"inputs": ['revenue', 'assets'], "func": moat_042_asset_turn_21d},
    "moat_043_asset_turn_63d": {"inputs": ['revenue', 'assets'], "func": moat_043_asset_turn_63d},
    "moat_044_asset_turn_126d": {"inputs": ['revenue', 'assets'], "func": moat_044_asset_turn_126d},
    "moat_045_asset_turn_252d": {"inputs": ['revenue', 'assets'], "func": moat_045_asset_turn_252d},
    "moat_046_moat_index_5d": {"inputs": ['revenue', 'ebit', 'assets'], "func": moat_046_moat_index_5d},
    "moat_047_moat_index_21d": {"inputs": ['revenue', 'ebit', 'assets'], "func": moat_047_moat_index_21d},
    "moat_048_moat_index_63d": {"inputs": ['revenue', 'ebit', 'assets'], "func": moat_048_moat_index_63d},
    "moat_049_moat_index_126d": {"inputs": ['revenue', 'ebit', 'assets'], "func": moat_049_moat_index_126d},
    "moat_050_moat_index_252d": {"inputs": ['revenue', 'ebit', 'assets'], "func": moat_050_moat_index_252d},
    "moat_051_excess_return_5d": {"inputs": ['netinc', 'equity'], "func": moat_051_excess_return_5d},
    "moat_052_excess_return_21d": {"inputs": ['netinc', 'equity'], "func": moat_052_excess_return_21d},
    "moat_053_excess_return_63d": {"inputs": ['netinc', 'equity'], "func": moat_053_excess_return_63d},
    "moat_054_excess_return_126d": {"inputs": ['netinc', 'equity'], "func": moat_054_excess_return_126d},
    "moat_055_excess_return_252d": {"inputs": ['netinc', 'equity'], "func": moat_055_excess_return_252d},
    "moat_056_roic_persistence_5d": {"inputs": ['ebit', 'assets'], "func": moat_056_roic_persistence_5d},
    "moat_057_roic_persistence_21d": {"inputs": ['ebit', 'assets'], "func": moat_057_roic_persistence_21d},
    "moat_058_roic_persistence_63d": {"inputs": ['ebit', 'assets'], "func": moat_058_roic_persistence_63d},
    "moat_059_roic_persistence_126d": {"inputs": ['ebit', 'assets'], "func": moat_059_roic_persistence_126d},
    "moat_060_roic_persistence_252d": {"inputs": ['ebit', 'assets'], "func": moat_060_roic_persistence_252d},
    "moat_061_margin_leadership_5d": {"inputs": ['revenue', 'ebit'], "func": moat_061_margin_leadership_5d},
    "moat_062_margin_leadership_21d": {"inputs": ['revenue', 'ebit'], "func": moat_062_margin_leadership_21d},
    "moat_063_margin_leadership_63d": {"inputs": ['revenue', 'ebit'], "func": moat_063_margin_leadership_63d},
    "moat_064_margin_leadership_126d": {"inputs": ['revenue', 'ebit'], "func": moat_064_margin_leadership_126d},
    "moat_065_margin_leadership_252d": {"inputs": ['revenue', 'ebit'], "func": moat_065_margin_leadership_252d},
    "moat_066_roe_persistence_5d": {"inputs": ['netinc', 'equity'], "func": moat_066_roe_persistence_5d},
    "moat_067_roe_persistence_21d": {"inputs": ['netinc', 'equity'], "func": moat_067_roe_persistence_21d},
    "moat_068_roe_persistence_63d": {"inputs": ['netinc', 'equity'], "func": moat_068_roe_persistence_63d},
    "moat_069_roe_persistence_126d": {"inputs": ['netinc', 'equity'], "func": moat_069_roe_persistence_126d},
    "moat_070_roe_persistence_252d": {"inputs": ['netinc', 'equity'], "func": moat_070_roe_persistence_252d},
    "moat_071_roic_vol_5d": {"inputs": ['ebit', 'assets'], "func": moat_071_roic_vol_5d},
    "moat_072_roic_vol_21d": {"inputs": ['ebit', 'assets'], "func": moat_072_roic_vol_21d},
    "moat_073_roic_vol_63d": {"inputs": ['ebit', 'assets'], "func": moat_073_roic_vol_63d},
    "moat_074_roic_vol_126d": {"inputs": ['ebit', 'assets'], "func": moat_074_roic_vol_126d},
    "moat_075_roic_vol_252d": {"inputs": ['ebit', 'assets'], "func": moat_075_roic_vol_252d},
}
