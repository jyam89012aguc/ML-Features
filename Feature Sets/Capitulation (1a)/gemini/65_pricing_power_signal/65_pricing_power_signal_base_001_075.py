"""
65_pricing_power_signal — Base Features 001-075
Domain: Margin stability vs Cost growth
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

def prpw_001_gp_m_5d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_001_gp_m_5d"""
    return (_safe_div(gp, revenue)).shift(5)

def prpw_002_gp_m_21d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_002_gp_m_21d"""
    return (_safe_div(gp, revenue)).shift(21)

def prpw_003_gp_m_63d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_003_gp_m_63d"""
    return (_safe_div(gp, revenue)).shift(63)

def prpw_004_gp_m_126d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_004_gp_m_126d"""
    return (_safe_div(gp, revenue)).shift(126)

def prpw_005_gp_m_252d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_005_gp_m_252d"""
    return (_safe_div(gp, revenue)).shift(252)

def prpw_006_ebit_m_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_006_ebit_m_5d"""
    return (_safe_div(ebit, revenue)).shift(5)

def prpw_007_ebit_m_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_007_ebit_m_21d"""
    return (_safe_div(ebit, revenue)).shift(21)

def prpw_008_ebit_m_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_008_ebit_m_63d"""
    return (_safe_div(ebit, revenue)).shift(63)

def prpw_009_ebit_m_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_009_ebit_m_126d"""
    return (_safe_div(ebit, revenue)).shift(126)

def prpw_010_ebit_m_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_010_ebit_m_252d"""
    return (_safe_div(ebit, revenue)).shift(252)

def prpw_011_cor_rev_5d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_011_cor_rev_5d"""
    return (_safe_div(cor, revenue)).shift(5)

def prpw_012_cor_rev_21d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_012_cor_rev_21d"""
    return (_safe_div(cor, revenue)).shift(21)

def prpw_013_cor_rev_63d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_013_cor_rev_63d"""
    return (_safe_div(cor, revenue)).shift(63)

def prpw_014_cor_rev_126d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_014_cor_rev_126d"""
    return (_safe_div(cor, revenue)).shift(126)

def prpw_015_cor_rev_252d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_015_cor_rev_252d"""
    return (_safe_div(cor, revenue)).shift(252)

def prpw_016_gp_g_5d(gp: pd.Series) -> pd.Series:
    """prpw_016_gp_g_5d"""
    return (gp.pct_change(252)).shift(5)

def prpw_017_gp_g_21d(gp: pd.Series) -> pd.Series:
    """prpw_017_gp_g_21d"""
    return (gp.pct_change(252)).shift(21)

def prpw_018_gp_g_63d(gp: pd.Series) -> pd.Series:
    """prpw_018_gp_g_63d"""
    return (gp.pct_change(252)).shift(63)

def prpw_019_gp_g_126d(gp: pd.Series) -> pd.Series:
    """prpw_019_gp_g_126d"""
    return (gp.pct_change(252)).shift(126)

def prpw_020_gp_g_252d(gp: pd.Series) -> pd.Series:
    """prpw_020_gp_g_252d"""
    return (gp.pct_change(252)).shift(252)

def prpw_021_rev_g_5d(revenue: pd.Series) -> pd.Series:
    """prpw_021_rev_g_5d"""
    return (revenue.pct_change(252)).shift(5)

def prpw_022_rev_g_21d(revenue: pd.Series) -> pd.Series:
    """prpw_022_rev_g_21d"""
    return (revenue.pct_change(252)).shift(21)

def prpw_023_rev_g_63d(revenue: pd.Series) -> pd.Series:
    """prpw_023_rev_g_63d"""
    return (revenue.pct_change(252)).shift(63)

def prpw_024_rev_g_126d(revenue: pd.Series) -> pd.Series:
    """prpw_024_rev_g_126d"""
    return (revenue.pct_change(252)).shift(126)

def prpw_025_rev_g_252d(revenue: pd.Series) -> pd.Series:
    """prpw_025_rev_g_252d"""
    return (revenue.pct_change(252)).shift(252)

def prpw_026_gp_m_chg_5d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_026_gp_m_chg_5d"""
    return (_safe_div(gp, revenue).diff(252)).shift(5)

def prpw_027_gp_m_chg_21d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_027_gp_m_chg_21d"""
    return (_safe_div(gp, revenue).diff(252)).shift(21)

def prpw_028_gp_m_chg_63d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_028_gp_m_chg_63d"""
    return (_safe_div(gp, revenue).diff(252)).shift(63)

def prpw_029_gp_m_chg_126d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_029_gp_m_chg_126d"""
    return (_safe_div(gp, revenue).diff(252)).shift(126)

def prpw_030_gp_m_chg_252d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_030_gp_m_chg_252d"""
    return (_safe_div(gp, revenue).diff(252)).shift(252)

def prpw_031_ebit_m_chg_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_031_ebit_m_chg_5d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(5)

def prpw_032_ebit_m_chg_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_032_ebit_m_chg_21d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(21)

def prpw_033_ebit_m_chg_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_033_ebit_m_chg_63d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(63)

def prpw_034_ebit_m_chg_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_034_ebit_m_chg_126d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(126)

def prpw_035_ebit_m_chg_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_035_ebit_m_chg_252d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(252)

def prpw_036_cor_g_5d(cor: pd.Series) -> pd.Series:
    """prpw_036_cor_g_5d"""
    return (cor.pct_change(252)).shift(5)

def prpw_037_cor_g_21d(cor: pd.Series) -> pd.Series:
    """prpw_037_cor_g_21d"""
    return (cor.pct_change(252)).shift(21)

def prpw_038_cor_g_63d(cor: pd.Series) -> pd.Series:
    """prpw_038_cor_g_63d"""
    return (cor.pct_change(252)).shift(63)

def prpw_039_cor_g_126d(cor: pd.Series) -> pd.Series:
    """prpw_039_cor_g_126d"""
    return (cor.pct_change(252)).shift(126)

def prpw_040_cor_g_252d(cor: pd.Series) -> pd.Series:
    """prpw_040_cor_g_252d"""
    return (cor.pct_change(252)).shift(252)

def prpw_041_price_power_index_5d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_041_price_power_index_5d"""
    return (_safe_div(revenue.pct_change(252), cor.pct_change(252))).shift(5)

def prpw_042_price_power_index_21d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_042_price_power_index_21d"""
    return (_safe_div(revenue.pct_change(252), cor.pct_change(252))).shift(21)

def prpw_043_price_power_index_63d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_043_price_power_index_63d"""
    return (_safe_div(revenue.pct_change(252), cor.pct_change(252))).shift(63)

def prpw_044_price_power_index_126d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_044_price_power_index_126d"""
    return (_safe_div(revenue.pct_change(252), cor.pct_change(252))).shift(126)

def prpw_045_price_power_index_252d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_045_price_power_index_252d"""
    return (_safe_div(revenue.pct_change(252), cor.pct_change(252))).shift(252)

def prpw_046_margin_stability_5d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_046_margin_stability_5d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(gp, revenue), 252))).shift(5)

def prpw_047_margin_stability_21d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_047_margin_stability_21d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(gp, revenue), 252))).shift(21)

def prpw_048_margin_stability_63d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_048_margin_stability_63d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(gp, revenue), 252))).shift(63)

def prpw_049_margin_stability_126d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_049_margin_stability_126d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(gp, revenue), 252))).shift(126)

def prpw_050_margin_stability_252d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_050_margin_stability_252d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(gp, revenue), 252))).shift(252)

def prpw_051_unit_cost_proxy_5d(cor: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_051_unit_cost_proxy_5d"""
    return (_safe_div(cor, assets)).shift(5)

def prpw_052_unit_cost_proxy_21d(cor: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_052_unit_cost_proxy_21d"""
    return (_safe_div(cor, assets)).shift(21)

def prpw_053_unit_cost_proxy_63d(cor: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_053_unit_cost_proxy_63d"""
    return (_safe_div(cor, assets)).shift(63)

def prpw_054_unit_cost_proxy_126d(cor: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_054_unit_cost_proxy_126d"""
    return (_safe_div(cor, assets)).shift(126)

def prpw_055_unit_cost_proxy_252d(cor: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_055_unit_cost_proxy_252d"""
    return (_safe_div(cor, assets)).shift(252)

def prpw_056_unit_rev_proxy_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_056_unit_rev_proxy_5d"""
    return (_safe_div(revenue, assets)).shift(5)

def prpw_057_unit_rev_proxy_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_057_unit_rev_proxy_21d"""
    return (_safe_div(revenue, assets)).shift(21)

def prpw_058_unit_rev_proxy_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_058_unit_rev_proxy_63d"""
    return (_safe_div(revenue, assets)).shift(63)

def prpw_059_unit_rev_proxy_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_059_unit_rev_proxy_126d"""
    return (_safe_div(revenue, assets)).shift(126)

def prpw_060_unit_rev_proxy_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_060_unit_rev_proxy_252d"""
    return (_safe_div(revenue, assets)).shift(252)

def prpw_061_gp_per_assets_5d(gp: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_061_gp_per_assets_5d"""
    return (_safe_div(gp, assets)).shift(5)

def prpw_062_gp_per_assets_21d(gp: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_062_gp_per_assets_21d"""
    return (_safe_div(gp, assets)).shift(21)

def prpw_063_gp_per_assets_63d(gp: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_063_gp_per_assets_63d"""
    return (_safe_div(gp, assets)).shift(63)

def prpw_064_gp_per_assets_126d(gp: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_064_gp_per_assets_126d"""
    return (_safe_div(gp, assets)).shift(126)

def prpw_065_gp_per_assets_252d(gp: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_065_gp_per_assets_252d"""
    return (_safe_div(gp, assets)).shift(252)

def prpw_066_ebit_per_assets_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_066_ebit_per_assets_5d"""
    return (_safe_div(ebit, assets)).shift(5)

def prpw_067_ebit_per_assets_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_067_ebit_per_assets_21d"""
    return (_safe_div(ebit, assets)).shift(21)

def prpw_068_ebit_per_assets_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_068_ebit_per_assets_63d"""
    return (_safe_div(ebit, assets)).shift(63)

def prpw_069_ebit_per_assets_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_069_ebit_per_assets_126d"""
    return (_safe_div(ebit, assets)).shift(126)

def prpw_070_ebit_per_assets_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_070_ebit_per_assets_252d"""
    return (_safe_div(ebit, assets)).shift(252)

def prpw_071_ps_rat_5d(ps: pd.Series) -> pd.Series:
    """prpw_071_ps_rat_5d"""
    return (ps).shift(5)

def prpw_072_ps_rat_21d(ps: pd.Series) -> pd.Series:
    """prpw_072_ps_rat_21d"""
    return (ps).shift(21)

def prpw_073_ps_rat_63d(ps: pd.Series) -> pd.Series:
    """prpw_073_ps_rat_63d"""
    return (ps).shift(63)

def prpw_074_ps_rat_126d(ps: pd.Series) -> pd.Series:
    """prpw_074_ps_rat_126d"""
    return (ps).shift(126)

def prpw_075_ps_rat_252d(ps: pd.Series) -> pd.Series:
    """prpw_075_ps_rat_252d"""
    return (ps).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V65_REGISTRY = {
    "prpw_001_gp_m_5d": {"inputs": ['revenue', 'gp'], "func": prpw_001_gp_m_5d},
    "prpw_002_gp_m_21d": {"inputs": ['revenue', 'gp'], "func": prpw_002_gp_m_21d},
    "prpw_003_gp_m_63d": {"inputs": ['revenue', 'gp'], "func": prpw_003_gp_m_63d},
    "prpw_004_gp_m_126d": {"inputs": ['revenue', 'gp'], "func": prpw_004_gp_m_126d},
    "prpw_005_gp_m_252d": {"inputs": ['revenue', 'gp'], "func": prpw_005_gp_m_252d},
    "prpw_006_ebit_m_5d": {"inputs": ['revenue', 'ebit'], "func": prpw_006_ebit_m_5d},
    "prpw_007_ebit_m_21d": {"inputs": ['revenue', 'ebit'], "func": prpw_007_ebit_m_21d},
    "prpw_008_ebit_m_63d": {"inputs": ['revenue', 'ebit'], "func": prpw_008_ebit_m_63d},
    "prpw_009_ebit_m_126d": {"inputs": ['revenue', 'ebit'], "func": prpw_009_ebit_m_126d},
    "prpw_010_ebit_m_252d": {"inputs": ['revenue', 'ebit'], "func": prpw_010_ebit_m_252d},
    "prpw_011_cor_rev_5d": {"inputs": ['revenue', 'cor'], "func": prpw_011_cor_rev_5d},
    "prpw_012_cor_rev_21d": {"inputs": ['revenue', 'cor'], "func": prpw_012_cor_rev_21d},
    "prpw_013_cor_rev_63d": {"inputs": ['revenue', 'cor'], "func": prpw_013_cor_rev_63d},
    "prpw_014_cor_rev_126d": {"inputs": ['revenue', 'cor'], "func": prpw_014_cor_rev_126d},
    "prpw_015_cor_rev_252d": {"inputs": ['revenue', 'cor'], "func": prpw_015_cor_rev_252d},
    "prpw_016_gp_g_5d": {"inputs": ['gp'], "func": prpw_016_gp_g_5d},
    "prpw_017_gp_g_21d": {"inputs": ['gp'], "func": prpw_017_gp_g_21d},
    "prpw_018_gp_g_63d": {"inputs": ['gp'], "func": prpw_018_gp_g_63d},
    "prpw_019_gp_g_126d": {"inputs": ['gp'], "func": prpw_019_gp_g_126d},
    "prpw_020_gp_g_252d": {"inputs": ['gp'], "func": prpw_020_gp_g_252d},
    "prpw_021_rev_g_5d": {"inputs": ['revenue'], "func": prpw_021_rev_g_5d},
    "prpw_022_rev_g_21d": {"inputs": ['revenue'], "func": prpw_022_rev_g_21d},
    "prpw_023_rev_g_63d": {"inputs": ['revenue'], "func": prpw_023_rev_g_63d},
    "prpw_024_rev_g_126d": {"inputs": ['revenue'], "func": prpw_024_rev_g_126d},
    "prpw_025_rev_g_252d": {"inputs": ['revenue'], "func": prpw_025_rev_g_252d},
    "prpw_026_gp_m_chg_5d": {"inputs": ['revenue', 'gp'], "func": prpw_026_gp_m_chg_5d},
    "prpw_027_gp_m_chg_21d": {"inputs": ['revenue', 'gp'], "func": prpw_027_gp_m_chg_21d},
    "prpw_028_gp_m_chg_63d": {"inputs": ['revenue', 'gp'], "func": prpw_028_gp_m_chg_63d},
    "prpw_029_gp_m_chg_126d": {"inputs": ['revenue', 'gp'], "func": prpw_029_gp_m_chg_126d},
    "prpw_030_gp_m_chg_252d": {"inputs": ['revenue', 'gp'], "func": prpw_030_gp_m_chg_252d},
    "prpw_031_ebit_m_chg_5d": {"inputs": ['revenue', 'ebit'], "func": prpw_031_ebit_m_chg_5d},
    "prpw_032_ebit_m_chg_21d": {"inputs": ['revenue', 'ebit'], "func": prpw_032_ebit_m_chg_21d},
    "prpw_033_ebit_m_chg_63d": {"inputs": ['revenue', 'ebit'], "func": prpw_033_ebit_m_chg_63d},
    "prpw_034_ebit_m_chg_126d": {"inputs": ['revenue', 'ebit'], "func": prpw_034_ebit_m_chg_126d},
    "prpw_035_ebit_m_chg_252d": {"inputs": ['revenue', 'ebit'], "func": prpw_035_ebit_m_chg_252d},
    "prpw_036_cor_g_5d": {"inputs": ['cor'], "func": prpw_036_cor_g_5d},
    "prpw_037_cor_g_21d": {"inputs": ['cor'], "func": prpw_037_cor_g_21d},
    "prpw_038_cor_g_63d": {"inputs": ['cor'], "func": prpw_038_cor_g_63d},
    "prpw_039_cor_g_126d": {"inputs": ['cor'], "func": prpw_039_cor_g_126d},
    "prpw_040_cor_g_252d": {"inputs": ['cor'], "func": prpw_040_cor_g_252d},
    "prpw_041_price_power_index_5d": {"inputs": ['revenue', 'cor'], "func": prpw_041_price_power_index_5d},
    "prpw_042_price_power_index_21d": {"inputs": ['revenue', 'cor'], "func": prpw_042_price_power_index_21d},
    "prpw_043_price_power_index_63d": {"inputs": ['revenue', 'cor'], "func": prpw_043_price_power_index_63d},
    "prpw_044_price_power_index_126d": {"inputs": ['revenue', 'cor'], "func": prpw_044_price_power_index_126d},
    "prpw_045_price_power_index_252d": {"inputs": ['revenue', 'cor'], "func": prpw_045_price_power_index_252d},
    "prpw_046_margin_stability_5d": {"inputs": ['revenue', 'gp'], "func": prpw_046_margin_stability_5d},
    "prpw_047_margin_stability_21d": {"inputs": ['revenue', 'gp'], "func": prpw_047_margin_stability_21d},
    "prpw_048_margin_stability_63d": {"inputs": ['revenue', 'gp'], "func": prpw_048_margin_stability_63d},
    "prpw_049_margin_stability_126d": {"inputs": ['revenue', 'gp'], "func": prpw_049_margin_stability_126d},
    "prpw_050_margin_stability_252d": {"inputs": ['revenue', 'gp'], "func": prpw_050_margin_stability_252d},
    "prpw_051_unit_cost_proxy_5d": {"inputs": ['cor', 'assets'], "func": prpw_051_unit_cost_proxy_5d},
    "prpw_052_unit_cost_proxy_21d": {"inputs": ['cor', 'assets'], "func": prpw_052_unit_cost_proxy_21d},
    "prpw_053_unit_cost_proxy_63d": {"inputs": ['cor', 'assets'], "func": prpw_053_unit_cost_proxy_63d},
    "prpw_054_unit_cost_proxy_126d": {"inputs": ['cor', 'assets'], "func": prpw_054_unit_cost_proxy_126d},
    "prpw_055_unit_cost_proxy_252d": {"inputs": ['cor', 'assets'], "func": prpw_055_unit_cost_proxy_252d},
    "prpw_056_unit_rev_proxy_5d": {"inputs": ['revenue', 'assets'], "func": prpw_056_unit_rev_proxy_5d},
    "prpw_057_unit_rev_proxy_21d": {"inputs": ['revenue', 'assets'], "func": prpw_057_unit_rev_proxy_21d},
    "prpw_058_unit_rev_proxy_63d": {"inputs": ['revenue', 'assets'], "func": prpw_058_unit_rev_proxy_63d},
    "prpw_059_unit_rev_proxy_126d": {"inputs": ['revenue', 'assets'], "func": prpw_059_unit_rev_proxy_126d},
    "prpw_060_unit_rev_proxy_252d": {"inputs": ['revenue', 'assets'], "func": prpw_060_unit_rev_proxy_252d},
    "prpw_061_gp_per_assets_5d": {"inputs": ['gp', 'assets'], "func": prpw_061_gp_per_assets_5d},
    "prpw_062_gp_per_assets_21d": {"inputs": ['gp', 'assets'], "func": prpw_062_gp_per_assets_21d},
    "prpw_063_gp_per_assets_63d": {"inputs": ['gp', 'assets'], "func": prpw_063_gp_per_assets_63d},
    "prpw_064_gp_per_assets_126d": {"inputs": ['gp', 'assets'], "func": prpw_064_gp_per_assets_126d},
    "prpw_065_gp_per_assets_252d": {"inputs": ['gp', 'assets'], "func": prpw_065_gp_per_assets_252d},
    "prpw_066_ebit_per_assets_5d": {"inputs": ['ebit', 'assets'], "func": prpw_066_ebit_per_assets_5d},
    "prpw_067_ebit_per_assets_21d": {"inputs": ['ebit', 'assets'], "func": prpw_067_ebit_per_assets_21d},
    "prpw_068_ebit_per_assets_63d": {"inputs": ['ebit', 'assets'], "func": prpw_068_ebit_per_assets_63d},
    "prpw_069_ebit_per_assets_126d": {"inputs": ['ebit', 'assets'], "func": prpw_069_ebit_per_assets_126d},
    "prpw_070_ebit_per_assets_252d": {"inputs": ['ebit', 'assets'], "func": prpw_070_ebit_per_assets_252d},
    "prpw_071_ps_rat_5d": {"inputs": ['ps'], "func": prpw_071_ps_rat_5d},
    "prpw_072_ps_rat_21d": {"inputs": ['ps'], "func": prpw_072_ps_rat_21d},
    "prpw_073_ps_rat_63d": {"inputs": ['ps'], "func": prpw_073_ps_rat_63d},
    "prpw_074_ps_rat_126d": {"inputs": ['ps'], "func": prpw_074_ps_rat_126d},
    "prpw_075_ps_rat_252d": {"inputs": ['ps'], "func": prpw_075_ps_rat_252d},
}
