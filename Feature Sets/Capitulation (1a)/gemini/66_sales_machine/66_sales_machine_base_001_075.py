"""
66_sales_machine — Base Features 001-075
Domain: Rev / (SGA + R&D)
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

def slsm_001_rev_sga_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_001_rev_sga_5d"""
    return (_safe_div(revenue, sga)).shift(5)

def slsm_002_rev_sga_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_002_rev_sga_21d"""
    return (_safe_div(revenue, sga)).shift(21)

def slsm_003_rev_sga_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_003_rev_sga_63d"""
    return (_safe_div(revenue, sga)).shift(63)

def slsm_004_rev_sga_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_004_rev_sga_126d"""
    return (_safe_div(revenue, sga)).shift(126)

def slsm_005_rev_sga_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_005_rev_sga_252d"""
    return (_safe_div(revenue, sga)).shift(252)

def slsm_006_rev_rnd_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_006_rev_rnd_5d"""
    return (_safe_div(revenue, rnd)).shift(5)

def slsm_007_rev_rnd_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_007_rev_rnd_21d"""
    return (_safe_div(revenue, rnd)).shift(21)

def slsm_008_rev_rnd_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_008_rev_rnd_63d"""
    return (_safe_div(revenue, rnd)).shift(63)

def slsm_009_rev_rnd_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_009_rev_rnd_126d"""
    return (_safe_div(revenue, rnd)).shift(126)

def slsm_010_rev_rnd_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_010_rev_rnd_252d"""
    return (_safe_div(revenue, rnd)).shift(252)

def slsm_011_gp_sga_5d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_011_gp_sga_5d"""
    return (_safe_div(gp, sga)).shift(5)

def slsm_012_gp_sga_21d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_012_gp_sga_21d"""
    return (_safe_div(gp, sga)).shift(21)

def slsm_013_gp_sga_63d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_013_gp_sga_63d"""
    return (_safe_div(gp, sga)).shift(63)

def slsm_014_gp_sga_126d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_014_gp_sga_126d"""
    return (_safe_div(gp, sga)).shift(126)

def slsm_015_gp_sga_252d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_015_gp_sga_252d"""
    return (_safe_div(gp, sga)).shift(252)

def slsm_016_ebit_sga_5d(ebit: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_016_ebit_sga_5d"""
    return (_safe_div(ebit, sga)).shift(5)

def slsm_017_ebit_sga_21d(ebit: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_017_ebit_sga_21d"""
    return (_safe_div(ebit, sga)).shift(21)

def slsm_018_ebit_sga_63d(ebit: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_018_ebit_sga_63d"""
    return (_safe_div(ebit, sga)).shift(63)

def slsm_019_ebit_sga_126d(ebit: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_019_ebit_sga_126d"""
    return (_safe_div(ebit, sga)).shift(126)

def slsm_020_ebit_sga_252d(ebit: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_020_ebit_sga_252d"""
    return (_safe_div(ebit, sga)).shift(252)

def slsm_021_sga_g_5d(sga: pd.Series) -> pd.Series:
    """slsm_021_sga_g_5d"""
    return (sga.pct_change(252)).shift(5)

def slsm_022_sga_g_21d(sga: pd.Series) -> pd.Series:
    """slsm_022_sga_g_21d"""
    return (sga.pct_change(252)).shift(21)

def slsm_023_sga_g_63d(sga: pd.Series) -> pd.Series:
    """slsm_023_sga_g_63d"""
    return (sga.pct_change(252)).shift(63)

def slsm_024_sga_g_126d(sga: pd.Series) -> pd.Series:
    """slsm_024_sga_g_126d"""
    return (sga.pct_change(252)).shift(126)

def slsm_025_sga_g_252d(sga: pd.Series) -> pd.Series:
    """slsm_025_sga_g_252d"""
    return (sga.pct_change(252)).shift(252)

def slsm_026_rev_g_5d(revenue: pd.Series) -> pd.Series:
    """slsm_026_rev_g_5d"""
    return (revenue.pct_change(252)).shift(5)

def slsm_027_rev_g_21d(revenue: pd.Series) -> pd.Series:
    """slsm_027_rev_g_21d"""
    return (revenue.pct_change(252)).shift(21)

def slsm_028_rev_g_63d(revenue: pd.Series) -> pd.Series:
    """slsm_028_rev_g_63d"""
    return (revenue.pct_change(252)).shift(63)

def slsm_029_rev_g_126d(revenue: pd.Series) -> pd.Series:
    """slsm_029_rev_g_126d"""
    return (revenue.pct_change(252)).shift(126)

def slsm_030_rev_g_252d(revenue: pd.Series) -> pd.Series:
    """slsm_030_rev_g_252d"""
    return (revenue.pct_change(252)).shift(252)

def slsm_031_sga_rev_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_031_sga_rev_5d"""
    return (_safe_div(sga, revenue)).shift(5)

def slsm_032_sga_rev_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_032_sga_rev_21d"""
    return (_safe_div(sga, revenue)).shift(21)

def slsm_033_sga_rev_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_033_sga_rev_63d"""
    return (_safe_div(sga, revenue)).shift(63)

def slsm_034_sga_rev_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_034_sga_rev_126d"""
    return (_safe_div(sga, revenue)).shift(126)

def slsm_035_sga_rev_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_035_sga_rev_252d"""
    return (_safe_div(sga, revenue)).shift(252)

def slsm_036_rnd_rev_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_036_rnd_rev_5d"""
    return (_safe_div(rnd, revenue)).shift(5)

def slsm_037_rnd_rev_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_037_rnd_rev_21d"""
    return (_safe_div(rnd, revenue)).shift(21)

def slsm_038_rnd_rev_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_038_rnd_rev_63d"""
    return (_safe_div(rnd, revenue)).shift(63)

def slsm_039_rnd_rev_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_039_rnd_rev_126d"""
    return (_safe_div(rnd, revenue)).shift(126)

def slsm_040_rnd_rev_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_040_rnd_rev_252d"""
    return (_safe_div(rnd, revenue)).shift(252)

def slsm_041_sales_eff_z_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_041_sales_eff_z_5d"""
    return (_zscore_rolling(_safe_div(revenue, sga), 1260)).shift(5)

def slsm_042_sales_eff_z_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_042_sales_eff_z_21d"""
    return (_zscore_rolling(_safe_div(revenue, sga), 1260)).shift(21)

def slsm_043_sales_eff_z_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_043_sales_eff_z_63d"""
    return (_zscore_rolling(_safe_div(revenue, sga), 1260)).shift(63)

def slsm_044_sales_eff_z_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_044_sales_eff_z_126d"""
    return (_zscore_rolling(_safe_div(revenue, sga), 1260)).shift(126)

def slsm_045_sales_eff_z_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_045_sales_eff_z_252d"""
    return (_zscore_rolling(_safe_div(revenue, sga), 1260)).shift(252)

def slsm_046_rnd_eff_z_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_046_rnd_eff_z_5d"""
    return (_zscore_rolling(_safe_div(revenue, rnd), 1260)).shift(5)

def slsm_047_rnd_eff_z_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_047_rnd_eff_z_21d"""
    return (_zscore_rolling(_safe_div(revenue, rnd), 1260)).shift(21)

def slsm_048_rnd_eff_z_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_048_rnd_eff_z_63d"""
    return (_zscore_rolling(_safe_div(revenue, rnd), 1260)).shift(63)

def slsm_049_rnd_eff_z_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_049_rnd_eff_z_126d"""
    return (_zscore_rolling(_safe_div(revenue, rnd), 1260)).shift(126)

def slsm_050_rnd_eff_z_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_050_rnd_eff_z_252d"""
    return (_zscore_rolling(_safe_div(revenue, rnd), 1260)).shift(252)

def slsm_051_sga_intensity_5d(sga: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_051_sga_intensity_5d"""
    return (_safe_div(sga, assets)).shift(5)

def slsm_052_sga_intensity_21d(sga: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_052_sga_intensity_21d"""
    return (_safe_div(sga, assets)).shift(21)

def slsm_053_sga_intensity_63d(sga: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_053_sga_intensity_63d"""
    return (_safe_div(sga, assets)).shift(63)

def slsm_054_sga_intensity_126d(sga: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_054_sga_intensity_126d"""
    return (_safe_div(sga, assets)).shift(126)

def slsm_055_sga_intensity_252d(sga: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_055_sga_intensity_252d"""
    return (_safe_div(sga, assets)).shift(252)

def slsm_056_rnd_intensity_5d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_056_rnd_intensity_5d"""
    return (_safe_div(rnd, assets)).shift(5)

def slsm_057_rnd_intensity_21d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_057_rnd_intensity_21d"""
    return (_safe_div(rnd, assets)).shift(21)

def slsm_058_rnd_intensity_63d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_058_rnd_intensity_63d"""
    return (_safe_div(rnd, assets)).shift(63)

def slsm_059_rnd_intensity_126d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_059_rnd_intensity_126d"""
    return (_safe_div(rnd, assets)).shift(126)

def slsm_060_rnd_intensity_252d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """slsm_060_rnd_intensity_252d"""
    return (_safe_div(rnd, assets)).shift(252)

def slsm_061_rev_per_sga_g_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_061_rev_per_sga_g_5d"""
    return ((_safe_div(revenue, sga)).pct_change(252)).shift(5)

def slsm_062_rev_per_sga_g_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_062_rev_per_sga_g_21d"""
    return ((_safe_div(revenue, sga)).pct_change(252)).shift(21)

def slsm_063_rev_per_sga_g_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_063_rev_per_sga_g_63d"""
    return ((_safe_div(revenue, sga)).pct_change(252)).shift(63)

def slsm_064_rev_per_sga_g_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_064_rev_per_sga_g_126d"""
    return ((_safe_div(revenue, sga)).pct_change(252)).shift(126)

def slsm_065_rev_per_sga_g_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_065_rev_per_sga_g_252d"""
    return ((_safe_div(revenue, sga)).pct_change(252)).shift(252)

def slsm_066_gp_per_sga_g_5d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_066_gp_per_sga_g_5d"""
    return ((_safe_div(gp, sga)).pct_change(252)).shift(5)

def slsm_067_gp_per_sga_g_21d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_067_gp_per_sga_g_21d"""
    return ((_safe_div(gp, sga)).pct_change(252)).shift(21)

def slsm_068_gp_per_sga_g_63d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_068_gp_per_sga_g_63d"""
    return ((_safe_div(gp, sga)).pct_change(252)).shift(63)

def slsm_069_gp_per_sga_g_126d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_069_gp_per_sga_g_126d"""
    return ((_safe_div(gp, sga)).pct_change(252)).shift(126)

def slsm_070_gp_per_sga_g_252d(gp: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_070_gp_per_sga_g_252d"""
    return ((_safe_div(gp, sga)).pct_change(252)).shift(252)

def slsm_071_sga_growth_vel_5d(sga: pd.Series) -> pd.Series:
    """slsm_071_sga_growth_vel_5d"""
    return (sga.pct_change(252).diff(63)).shift(5)

def slsm_072_sga_growth_vel_21d(sga: pd.Series) -> pd.Series:
    """slsm_072_sga_growth_vel_21d"""
    return (sga.pct_change(252).diff(63)).shift(21)

def slsm_073_sga_growth_vel_63d(sga: pd.Series) -> pd.Series:
    """slsm_073_sga_growth_vel_63d"""
    return (sga.pct_change(252).diff(63)).shift(63)

def slsm_074_sga_growth_vel_126d(sga: pd.Series) -> pd.Series:
    """slsm_074_sga_growth_vel_126d"""
    return (sga.pct_change(252).diff(63)).shift(126)

def slsm_075_sga_growth_vel_252d(sga: pd.Series) -> pd.Series:
    """slsm_075_sga_growth_vel_252d"""
    return (sga.pct_change(252).diff(63)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V66_REGISTRY = {
    "slsm_001_rev_sga_5d": {"inputs": ['revenue', 'sga'], "func": slsm_001_rev_sga_5d},
    "slsm_002_rev_sga_21d": {"inputs": ['revenue', 'sga'], "func": slsm_002_rev_sga_21d},
    "slsm_003_rev_sga_63d": {"inputs": ['revenue', 'sga'], "func": slsm_003_rev_sga_63d},
    "slsm_004_rev_sga_126d": {"inputs": ['revenue', 'sga'], "func": slsm_004_rev_sga_126d},
    "slsm_005_rev_sga_252d": {"inputs": ['revenue', 'sga'], "func": slsm_005_rev_sga_252d},
    "slsm_006_rev_rnd_5d": {"inputs": ['revenue', 'rnd'], "func": slsm_006_rev_rnd_5d},
    "slsm_007_rev_rnd_21d": {"inputs": ['revenue', 'rnd'], "func": slsm_007_rev_rnd_21d},
    "slsm_008_rev_rnd_63d": {"inputs": ['revenue', 'rnd'], "func": slsm_008_rev_rnd_63d},
    "slsm_009_rev_rnd_126d": {"inputs": ['revenue', 'rnd'], "func": slsm_009_rev_rnd_126d},
    "slsm_010_rev_rnd_252d": {"inputs": ['revenue', 'rnd'], "func": slsm_010_rev_rnd_252d},
    "slsm_011_gp_sga_5d": {"inputs": ['gp', 'sga'], "func": slsm_011_gp_sga_5d},
    "slsm_012_gp_sga_21d": {"inputs": ['gp', 'sga'], "func": slsm_012_gp_sga_21d},
    "slsm_013_gp_sga_63d": {"inputs": ['gp', 'sga'], "func": slsm_013_gp_sga_63d},
    "slsm_014_gp_sga_126d": {"inputs": ['gp', 'sga'], "func": slsm_014_gp_sga_126d},
    "slsm_015_gp_sga_252d": {"inputs": ['gp', 'sga'], "func": slsm_015_gp_sga_252d},
    "slsm_016_ebit_sga_5d": {"inputs": ['ebit', 'sga'], "func": slsm_016_ebit_sga_5d},
    "slsm_017_ebit_sga_21d": {"inputs": ['ebit', 'sga'], "func": slsm_017_ebit_sga_21d},
    "slsm_018_ebit_sga_63d": {"inputs": ['ebit', 'sga'], "func": slsm_018_ebit_sga_63d},
    "slsm_019_ebit_sga_126d": {"inputs": ['ebit', 'sga'], "func": slsm_019_ebit_sga_126d},
    "slsm_020_ebit_sga_252d": {"inputs": ['ebit', 'sga'], "func": slsm_020_ebit_sga_252d},
    "slsm_021_sga_g_5d": {"inputs": ['sga'], "func": slsm_021_sga_g_5d},
    "slsm_022_sga_g_21d": {"inputs": ['sga'], "func": slsm_022_sga_g_21d},
    "slsm_023_sga_g_63d": {"inputs": ['sga'], "func": slsm_023_sga_g_63d},
    "slsm_024_sga_g_126d": {"inputs": ['sga'], "func": slsm_024_sga_g_126d},
    "slsm_025_sga_g_252d": {"inputs": ['sga'], "func": slsm_025_sga_g_252d},
    "slsm_026_rev_g_5d": {"inputs": ['revenue'], "func": slsm_026_rev_g_5d},
    "slsm_027_rev_g_21d": {"inputs": ['revenue'], "func": slsm_027_rev_g_21d},
    "slsm_028_rev_g_63d": {"inputs": ['revenue'], "func": slsm_028_rev_g_63d},
    "slsm_029_rev_g_126d": {"inputs": ['revenue'], "func": slsm_029_rev_g_126d},
    "slsm_030_rev_g_252d": {"inputs": ['revenue'], "func": slsm_030_rev_g_252d},
    "slsm_031_sga_rev_5d": {"inputs": ['revenue', 'sga'], "func": slsm_031_sga_rev_5d},
    "slsm_032_sga_rev_21d": {"inputs": ['revenue', 'sga'], "func": slsm_032_sga_rev_21d},
    "slsm_033_sga_rev_63d": {"inputs": ['revenue', 'sga'], "func": slsm_033_sga_rev_63d},
    "slsm_034_sga_rev_126d": {"inputs": ['revenue', 'sga'], "func": slsm_034_sga_rev_126d},
    "slsm_035_sga_rev_252d": {"inputs": ['revenue', 'sga'], "func": slsm_035_sga_rev_252d},
    "slsm_036_rnd_rev_5d": {"inputs": ['revenue', 'rnd'], "func": slsm_036_rnd_rev_5d},
    "slsm_037_rnd_rev_21d": {"inputs": ['revenue', 'rnd'], "func": slsm_037_rnd_rev_21d},
    "slsm_038_rnd_rev_63d": {"inputs": ['revenue', 'rnd'], "func": slsm_038_rnd_rev_63d},
    "slsm_039_rnd_rev_126d": {"inputs": ['revenue', 'rnd'], "func": slsm_039_rnd_rev_126d},
    "slsm_040_rnd_rev_252d": {"inputs": ['revenue', 'rnd'], "func": slsm_040_rnd_rev_252d},
    "slsm_041_sales_eff_z_5d": {"inputs": ['revenue', 'sga'], "func": slsm_041_sales_eff_z_5d},
    "slsm_042_sales_eff_z_21d": {"inputs": ['revenue', 'sga'], "func": slsm_042_sales_eff_z_21d},
    "slsm_043_sales_eff_z_63d": {"inputs": ['revenue', 'sga'], "func": slsm_043_sales_eff_z_63d},
    "slsm_044_sales_eff_z_126d": {"inputs": ['revenue', 'sga'], "func": slsm_044_sales_eff_z_126d},
    "slsm_045_sales_eff_z_252d": {"inputs": ['revenue', 'sga'], "func": slsm_045_sales_eff_z_252d},
    "slsm_046_rnd_eff_z_5d": {"inputs": ['revenue', 'rnd'], "func": slsm_046_rnd_eff_z_5d},
    "slsm_047_rnd_eff_z_21d": {"inputs": ['revenue', 'rnd'], "func": slsm_047_rnd_eff_z_21d},
    "slsm_048_rnd_eff_z_63d": {"inputs": ['revenue', 'rnd'], "func": slsm_048_rnd_eff_z_63d},
    "slsm_049_rnd_eff_z_126d": {"inputs": ['revenue', 'rnd'], "func": slsm_049_rnd_eff_z_126d},
    "slsm_050_rnd_eff_z_252d": {"inputs": ['revenue', 'rnd'], "func": slsm_050_rnd_eff_z_252d},
    "slsm_051_sga_intensity_5d": {"inputs": ['sga', 'assets'], "func": slsm_051_sga_intensity_5d},
    "slsm_052_sga_intensity_21d": {"inputs": ['sga', 'assets'], "func": slsm_052_sga_intensity_21d},
    "slsm_053_sga_intensity_63d": {"inputs": ['sga', 'assets'], "func": slsm_053_sga_intensity_63d},
    "slsm_054_sga_intensity_126d": {"inputs": ['sga', 'assets'], "func": slsm_054_sga_intensity_126d},
    "slsm_055_sga_intensity_252d": {"inputs": ['sga', 'assets'], "func": slsm_055_sga_intensity_252d},
    "slsm_056_rnd_intensity_5d": {"inputs": ['rnd', 'assets'], "func": slsm_056_rnd_intensity_5d},
    "slsm_057_rnd_intensity_21d": {"inputs": ['rnd', 'assets'], "func": slsm_057_rnd_intensity_21d},
    "slsm_058_rnd_intensity_63d": {"inputs": ['rnd', 'assets'], "func": slsm_058_rnd_intensity_63d},
    "slsm_059_rnd_intensity_126d": {"inputs": ['rnd', 'assets'], "func": slsm_059_rnd_intensity_126d},
    "slsm_060_rnd_intensity_252d": {"inputs": ['rnd', 'assets'], "func": slsm_060_rnd_intensity_252d},
    "slsm_061_rev_per_sga_g_5d": {"inputs": ['revenue', 'sga'], "func": slsm_061_rev_per_sga_g_5d},
    "slsm_062_rev_per_sga_g_21d": {"inputs": ['revenue', 'sga'], "func": slsm_062_rev_per_sga_g_21d},
    "slsm_063_rev_per_sga_g_63d": {"inputs": ['revenue', 'sga'], "func": slsm_063_rev_per_sga_g_63d},
    "slsm_064_rev_per_sga_g_126d": {"inputs": ['revenue', 'sga'], "func": slsm_064_rev_per_sga_g_126d},
    "slsm_065_rev_per_sga_g_252d": {"inputs": ['revenue', 'sga'], "func": slsm_065_rev_per_sga_g_252d},
    "slsm_066_gp_per_sga_g_5d": {"inputs": ['gp', 'sga'], "func": slsm_066_gp_per_sga_g_5d},
    "slsm_067_gp_per_sga_g_21d": {"inputs": ['gp', 'sga'], "func": slsm_067_gp_per_sga_g_21d},
    "slsm_068_gp_per_sga_g_63d": {"inputs": ['gp', 'sga'], "func": slsm_068_gp_per_sga_g_63d},
    "slsm_069_gp_per_sga_g_126d": {"inputs": ['gp', 'sga'], "func": slsm_069_gp_per_sga_g_126d},
    "slsm_070_gp_per_sga_g_252d": {"inputs": ['gp', 'sga'], "func": slsm_070_gp_per_sga_g_252d},
    "slsm_071_sga_growth_vel_5d": {"inputs": ['sga'], "func": slsm_071_sga_growth_vel_5d},
    "slsm_072_sga_growth_vel_21d": {"inputs": ['sga'], "func": slsm_072_sga_growth_vel_21d},
    "slsm_073_sga_growth_vel_63d": {"inputs": ['sga'], "func": slsm_073_sga_growth_vel_63d},
    "slsm_074_sga_growth_vel_126d": {"inputs": ['sga'], "func": slsm_074_sga_growth_vel_126d},
    "slsm_075_sga_growth_vel_252d": {"inputs": ['sga'], "func": slsm_075_sga_growth_vel_252d},
}
