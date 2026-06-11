"""
64_operating_leverage_composite — Base Features 001-075
Domain: OpInc growth vs Rev growth
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

def olec_001_ebit_rev_g_rat_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_001_ebit_rev_g_rat_5d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(5)

def olec_002_ebit_rev_g_rat_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_002_ebit_rev_g_rat_21d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(21)

def olec_003_ebit_rev_g_rat_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_003_ebit_rev_g_rat_63d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(63)

def olec_004_ebit_rev_g_rat_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_004_ebit_rev_g_rat_126d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(126)

def olec_005_ebit_rev_g_rat_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_005_ebit_rev_g_rat_252d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(252)

def olec_006_ebitda_rev_g_rat_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_006_ebitda_rev_g_rat_5d"""
    return (_safe_div(ebitda.pct_change(252), revenue.pct_change(252))).shift(5)

def olec_007_ebitda_rev_g_rat_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_007_ebitda_rev_g_rat_21d"""
    return (_safe_div(ebitda.pct_change(252), revenue.pct_change(252))).shift(21)

def olec_008_ebitda_rev_g_rat_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_008_ebitda_rev_g_rat_63d"""
    return (_safe_div(ebitda.pct_change(252), revenue.pct_change(252))).shift(63)

def olec_009_ebitda_rev_g_rat_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_009_ebitda_rev_g_rat_126d"""
    return (_safe_div(ebitda.pct_change(252), revenue.pct_change(252))).shift(126)

def olec_010_ebitda_rev_g_rat_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_010_ebitda_rev_g_rat_252d"""
    return (_safe_div(ebitda.pct_change(252), revenue.pct_change(252))).shift(252)

def olec_011_ni_rev_g_rat_5d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_011_ni_rev_g_rat_5d"""
    return (_safe_div(netinc.pct_change(252), revenue.pct_change(252))).shift(5)

def olec_012_ni_rev_g_rat_21d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_012_ni_rev_g_rat_21d"""
    return (_safe_div(netinc.pct_change(252), revenue.pct_change(252))).shift(21)

def olec_013_ni_rev_g_rat_63d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_013_ni_rev_g_rat_63d"""
    return (_safe_div(netinc.pct_change(252), revenue.pct_change(252))).shift(63)

def olec_014_ni_rev_g_rat_126d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_014_ni_rev_g_rat_126d"""
    return (_safe_div(netinc.pct_change(252), revenue.pct_change(252))).shift(126)

def olec_015_ni_rev_g_rat_252d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_015_ni_rev_g_rat_252d"""
    return (_safe_div(netinc.pct_change(252), revenue.pct_change(252))).shift(252)

def olec_016_margin_chg_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_016_margin_chg_5d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(5)

def olec_017_margin_chg_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_017_margin_chg_21d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(21)

def olec_018_margin_chg_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_018_margin_chg_63d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(63)

def olec_019_margin_chg_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_019_margin_chg_126d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(126)

def olec_020_margin_chg_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_020_margin_chg_252d"""
    return (_safe_div(ebit, revenue).diff(252)).shift(252)

def olec_021_fixed_cost_proxy_5d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_021_fixed_cost_proxy_5d"""
    return (_safe_div(sga + rnd, revenue)).shift(5)

def olec_022_fixed_cost_proxy_21d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_022_fixed_cost_proxy_21d"""
    return (_safe_div(sga + rnd, revenue)).shift(21)

def olec_023_fixed_cost_proxy_63d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_023_fixed_cost_proxy_63d"""
    return (_safe_div(sga + rnd, revenue)).shift(63)

def olec_024_fixed_cost_proxy_126d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_024_fixed_cost_proxy_126d"""
    return (_safe_div(sga + rnd, revenue)).shift(126)

def olec_025_fixed_cost_proxy_252d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_025_fixed_cost_proxy_252d"""
    return (_safe_div(sga + rnd, revenue)).shift(252)

def olec_026_op_leverage_z_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_026_op_leverage_z_5d"""
    return (_zscore_rolling(_safe_div(ebit.pct_change(252), revenue.pct_change(252)), 1260)).shift(5)

def olec_027_op_leverage_z_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_027_op_leverage_z_21d"""
    return (_zscore_rolling(_safe_div(ebit.pct_change(252), revenue.pct_change(252)), 1260)).shift(21)

def olec_028_op_leverage_z_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_028_op_leverage_z_63d"""
    return (_zscore_rolling(_safe_div(ebit.pct_change(252), revenue.pct_change(252)), 1260)).shift(63)

def olec_029_op_leverage_z_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_029_op_leverage_z_126d"""
    return (_zscore_rolling(_safe_div(ebit.pct_change(252), revenue.pct_change(252)), 1260)).shift(126)

def olec_030_op_leverage_z_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_030_op_leverage_z_252d"""
    return (_zscore_rolling(_safe_div(ebit.pct_change(252), revenue.pct_change(252)), 1260)).shift(252)

def olec_031_rev_g_5d(revenue: pd.Series) -> pd.Series:
    """olec_031_rev_g_5d"""
    return (revenue.pct_change(252)).shift(5)

def olec_032_rev_g_21d(revenue: pd.Series) -> pd.Series:
    """olec_032_rev_g_21d"""
    return (revenue.pct_change(252)).shift(21)

def olec_033_rev_g_63d(revenue: pd.Series) -> pd.Series:
    """olec_033_rev_g_63d"""
    return (revenue.pct_change(252)).shift(63)

def olec_034_rev_g_126d(revenue: pd.Series) -> pd.Series:
    """olec_034_rev_g_126d"""
    return (revenue.pct_change(252)).shift(126)

def olec_035_rev_g_252d(revenue: pd.Series) -> pd.Series:
    """olec_035_rev_g_252d"""
    return (revenue.pct_change(252)).shift(252)

def olec_036_ebit_g_5d(ebit: pd.Series) -> pd.Series:
    """olec_036_ebit_g_5d"""
    return (ebit.pct_change(252)).shift(5)

def olec_037_ebit_g_21d(ebit: pd.Series) -> pd.Series:
    """olec_037_ebit_g_21d"""
    return (ebit.pct_change(252)).shift(21)

def olec_038_ebit_g_63d(ebit: pd.Series) -> pd.Series:
    """olec_038_ebit_g_63d"""
    return (ebit.pct_change(252)).shift(63)

def olec_039_ebit_g_126d(ebit: pd.Series) -> pd.Series:
    """olec_039_ebit_g_126d"""
    return (ebit.pct_change(252)).shift(126)

def olec_040_ebit_g_252d(ebit: pd.Series) -> pd.Series:
    """olec_040_ebit_g_252d"""
    return (ebit.pct_change(252)).shift(252)

def olec_041_gp_m_5d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """olec_041_gp_m_5d"""
    return (_safe_div(gp, revenue)).shift(5)

def olec_042_gp_m_21d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """olec_042_gp_m_21d"""
    return (_safe_div(gp, revenue)).shift(21)

def olec_043_gp_m_63d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """olec_043_gp_m_63d"""
    return (_safe_div(gp, revenue)).shift(63)

def olec_044_gp_m_126d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """olec_044_gp_m_126d"""
    return (_safe_div(gp, revenue)).shift(126)

def olec_045_gp_m_252d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """olec_045_gp_m_252d"""
    return (_safe_div(gp, revenue)).shift(252)

def olec_046_ebit_m_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_046_ebit_m_5d"""
    return (_safe_div(ebit, revenue)).shift(5)

def olec_047_ebit_m_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_047_ebit_m_21d"""
    return (_safe_div(ebit, revenue)).shift(21)

def olec_048_ebit_m_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_048_ebit_m_63d"""
    return (_safe_div(ebit, revenue)).shift(63)

def olec_049_ebit_m_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_049_ebit_m_126d"""
    return (_safe_div(ebit, revenue)).shift(126)

def olec_050_ebit_m_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_050_ebit_m_252d"""
    return (_safe_div(ebit, revenue)).shift(252)

def olec_051_ebitda_m_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_051_ebitda_m_5d"""
    return (_safe_div(ebitda, revenue)).shift(5)

def olec_052_ebitda_m_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_052_ebitda_m_21d"""
    return (_safe_div(ebitda, revenue)).shift(21)

def olec_053_ebitda_m_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_053_ebitda_m_63d"""
    return (_safe_div(ebitda, revenue)).shift(63)

def olec_054_ebitda_m_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_054_ebitda_m_126d"""
    return (_safe_div(ebitda, revenue)).shift(126)

def olec_055_ebitda_m_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """olec_055_ebitda_m_252d"""
    return (_safe_div(ebitda, revenue)).shift(252)

def olec_056_ni_m_5d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_056_ni_m_5d"""
    return (_safe_div(netinc, revenue)).shift(5)

def olec_057_ni_m_21d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_057_ni_m_21d"""
    return (_safe_div(netinc, revenue)).shift(21)

def olec_058_ni_m_63d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_058_ni_m_63d"""
    return (_safe_div(netinc, revenue)).shift(63)

def olec_059_ni_m_126d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_059_ni_m_126d"""
    return (_safe_div(netinc, revenue)).shift(126)

def olec_060_ni_m_252d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """olec_060_ni_m_252d"""
    return (_safe_div(netinc, revenue)).shift(252)

def olec_061_asset_turn_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_061_asset_turn_5d"""
    return (_safe_div(revenue, assets)).shift(5)

def olec_062_asset_turn_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_062_asset_turn_21d"""
    return (_safe_div(revenue, assets)).shift(21)

def olec_063_asset_turn_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_063_asset_turn_63d"""
    return (_safe_div(revenue, assets)).shift(63)

def olec_064_asset_turn_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_064_asset_turn_126d"""
    return (_safe_div(revenue, assets)).shift(126)

def olec_065_asset_turn_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_065_asset_turn_252d"""
    return (_safe_div(revenue, assets)).shift(252)

def olec_066_fixed_asset_turn_5d(revenue: pd.Series, ppnent: pd.Series) -> pd.Series:
    """olec_066_fixed_asset_turn_5d"""
    return (_safe_div(revenue, ppnent)).shift(5)

def olec_067_fixed_asset_turn_21d(revenue: pd.Series, ppnent: pd.Series) -> pd.Series:
    """olec_067_fixed_asset_turn_21d"""
    return (_safe_div(revenue, ppnent)).shift(21)

def olec_068_fixed_asset_turn_63d(revenue: pd.Series, ppnent: pd.Series) -> pd.Series:
    """olec_068_fixed_asset_turn_63d"""
    return (_safe_div(revenue, ppnent)).shift(63)

def olec_069_fixed_asset_turn_126d(revenue: pd.Series, ppnent: pd.Series) -> pd.Series:
    """olec_069_fixed_asset_turn_126d"""
    return (_safe_div(revenue, ppnent)).shift(126)

def olec_070_fixed_asset_turn_252d(revenue: pd.Series, ppnent: pd.Series) -> pd.Series:
    """olec_070_fixed_asset_turn_252d"""
    return (_safe_div(revenue, ppnent)).shift(252)

def olec_071_work_cap_turn_5d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """olec_071_work_cap_turn_5d"""
    return (_safe_div(revenue, workingcapital)).shift(5)

def olec_072_work_cap_turn_21d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """olec_072_work_cap_turn_21d"""
    return (_safe_div(revenue, workingcapital)).shift(21)

def olec_073_work_cap_turn_63d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """olec_073_work_cap_turn_63d"""
    return (_safe_div(revenue, workingcapital)).shift(63)

def olec_074_work_cap_turn_126d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """olec_074_work_cap_turn_126d"""
    return (_safe_div(revenue, workingcapital)).shift(126)

def olec_075_work_cap_turn_252d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """olec_075_work_cap_turn_252d"""
    return (_safe_div(revenue, workingcapital)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V64_REGISTRY = {
    "olec_001_ebit_rev_g_rat_5d": {"inputs": ['revenue', 'ebit'], "func": olec_001_ebit_rev_g_rat_5d},
    "olec_002_ebit_rev_g_rat_21d": {"inputs": ['revenue', 'ebit'], "func": olec_002_ebit_rev_g_rat_21d},
    "olec_003_ebit_rev_g_rat_63d": {"inputs": ['revenue', 'ebit'], "func": olec_003_ebit_rev_g_rat_63d},
    "olec_004_ebit_rev_g_rat_126d": {"inputs": ['revenue', 'ebit'], "func": olec_004_ebit_rev_g_rat_126d},
    "olec_005_ebit_rev_g_rat_252d": {"inputs": ['revenue', 'ebit'], "func": olec_005_ebit_rev_g_rat_252d},
    "olec_006_ebitda_rev_g_rat_5d": {"inputs": ['revenue', 'ebitda'], "func": olec_006_ebitda_rev_g_rat_5d},
    "olec_007_ebitda_rev_g_rat_21d": {"inputs": ['revenue', 'ebitda'], "func": olec_007_ebitda_rev_g_rat_21d},
    "olec_008_ebitda_rev_g_rat_63d": {"inputs": ['revenue', 'ebitda'], "func": olec_008_ebitda_rev_g_rat_63d},
    "olec_009_ebitda_rev_g_rat_126d": {"inputs": ['revenue', 'ebitda'], "func": olec_009_ebitda_rev_g_rat_126d},
    "olec_010_ebitda_rev_g_rat_252d": {"inputs": ['revenue', 'ebitda'], "func": olec_010_ebitda_rev_g_rat_252d},
    "olec_011_ni_rev_g_rat_5d": {"inputs": ['revenue', 'netinc'], "func": olec_011_ni_rev_g_rat_5d},
    "olec_012_ni_rev_g_rat_21d": {"inputs": ['revenue', 'netinc'], "func": olec_012_ni_rev_g_rat_21d},
    "olec_013_ni_rev_g_rat_63d": {"inputs": ['revenue', 'netinc'], "func": olec_013_ni_rev_g_rat_63d},
    "olec_014_ni_rev_g_rat_126d": {"inputs": ['revenue', 'netinc'], "func": olec_014_ni_rev_g_rat_126d},
    "olec_015_ni_rev_g_rat_252d": {"inputs": ['revenue', 'netinc'], "func": olec_015_ni_rev_g_rat_252d},
    "olec_016_margin_chg_5d": {"inputs": ['revenue', 'ebit'], "func": olec_016_margin_chg_5d},
    "olec_017_margin_chg_21d": {"inputs": ['revenue', 'ebit'], "func": olec_017_margin_chg_21d},
    "olec_018_margin_chg_63d": {"inputs": ['revenue', 'ebit'], "func": olec_018_margin_chg_63d},
    "olec_019_margin_chg_126d": {"inputs": ['revenue', 'ebit'], "func": olec_019_margin_chg_126d},
    "olec_020_margin_chg_252d": {"inputs": ['revenue', 'ebit'], "func": olec_020_margin_chg_252d},
    "olec_021_fixed_cost_proxy_5d": {"inputs": ['revenue', 'sga', 'rnd'], "func": olec_021_fixed_cost_proxy_5d},
    "olec_022_fixed_cost_proxy_21d": {"inputs": ['revenue', 'sga', 'rnd'], "func": olec_022_fixed_cost_proxy_21d},
    "olec_023_fixed_cost_proxy_63d": {"inputs": ['revenue', 'sga', 'rnd'], "func": olec_023_fixed_cost_proxy_63d},
    "olec_024_fixed_cost_proxy_126d": {"inputs": ['revenue', 'sga', 'rnd'], "func": olec_024_fixed_cost_proxy_126d},
    "olec_025_fixed_cost_proxy_252d": {"inputs": ['revenue', 'sga', 'rnd'], "func": olec_025_fixed_cost_proxy_252d},
    "olec_026_op_leverage_z_5d": {"inputs": ['revenue', 'ebit'], "func": olec_026_op_leverage_z_5d},
    "olec_027_op_leverage_z_21d": {"inputs": ['revenue', 'ebit'], "func": olec_027_op_leverage_z_21d},
    "olec_028_op_leverage_z_63d": {"inputs": ['revenue', 'ebit'], "func": olec_028_op_leverage_z_63d},
    "olec_029_op_leverage_z_126d": {"inputs": ['revenue', 'ebit'], "func": olec_029_op_leverage_z_126d},
    "olec_030_op_leverage_z_252d": {"inputs": ['revenue', 'ebit'], "func": olec_030_op_leverage_z_252d},
    "olec_031_rev_g_5d": {"inputs": ['revenue'], "func": olec_031_rev_g_5d},
    "olec_032_rev_g_21d": {"inputs": ['revenue'], "func": olec_032_rev_g_21d},
    "olec_033_rev_g_63d": {"inputs": ['revenue'], "func": olec_033_rev_g_63d},
    "olec_034_rev_g_126d": {"inputs": ['revenue'], "func": olec_034_rev_g_126d},
    "olec_035_rev_g_252d": {"inputs": ['revenue'], "func": olec_035_rev_g_252d},
    "olec_036_ebit_g_5d": {"inputs": ['ebit'], "func": olec_036_ebit_g_5d},
    "olec_037_ebit_g_21d": {"inputs": ['ebit'], "func": olec_037_ebit_g_21d},
    "olec_038_ebit_g_63d": {"inputs": ['ebit'], "func": olec_038_ebit_g_63d},
    "olec_039_ebit_g_126d": {"inputs": ['ebit'], "func": olec_039_ebit_g_126d},
    "olec_040_ebit_g_252d": {"inputs": ['ebit'], "func": olec_040_ebit_g_252d},
    "olec_041_gp_m_5d": {"inputs": ['revenue', 'gp'], "func": olec_041_gp_m_5d},
    "olec_042_gp_m_21d": {"inputs": ['revenue', 'gp'], "func": olec_042_gp_m_21d},
    "olec_043_gp_m_63d": {"inputs": ['revenue', 'gp'], "func": olec_043_gp_m_63d},
    "olec_044_gp_m_126d": {"inputs": ['revenue', 'gp'], "func": olec_044_gp_m_126d},
    "olec_045_gp_m_252d": {"inputs": ['revenue', 'gp'], "func": olec_045_gp_m_252d},
    "olec_046_ebit_m_5d": {"inputs": ['revenue', 'ebit'], "func": olec_046_ebit_m_5d},
    "olec_047_ebit_m_21d": {"inputs": ['revenue', 'ebit'], "func": olec_047_ebit_m_21d},
    "olec_048_ebit_m_63d": {"inputs": ['revenue', 'ebit'], "func": olec_048_ebit_m_63d},
    "olec_049_ebit_m_126d": {"inputs": ['revenue', 'ebit'], "func": olec_049_ebit_m_126d},
    "olec_050_ebit_m_252d": {"inputs": ['revenue', 'ebit'], "func": olec_050_ebit_m_252d},
    "olec_051_ebitda_m_5d": {"inputs": ['revenue', 'ebitda'], "func": olec_051_ebitda_m_5d},
    "olec_052_ebitda_m_21d": {"inputs": ['revenue', 'ebitda'], "func": olec_052_ebitda_m_21d},
    "olec_053_ebitda_m_63d": {"inputs": ['revenue', 'ebitda'], "func": olec_053_ebitda_m_63d},
    "olec_054_ebitda_m_126d": {"inputs": ['revenue', 'ebitda'], "func": olec_054_ebitda_m_126d},
    "olec_055_ebitda_m_252d": {"inputs": ['revenue', 'ebitda'], "func": olec_055_ebitda_m_252d},
    "olec_056_ni_m_5d": {"inputs": ['revenue', 'netinc'], "func": olec_056_ni_m_5d},
    "olec_057_ni_m_21d": {"inputs": ['revenue', 'netinc'], "func": olec_057_ni_m_21d},
    "olec_058_ni_m_63d": {"inputs": ['revenue', 'netinc'], "func": olec_058_ni_m_63d},
    "olec_059_ni_m_126d": {"inputs": ['revenue', 'netinc'], "func": olec_059_ni_m_126d},
    "olec_060_ni_m_252d": {"inputs": ['revenue', 'netinc'], "func": olec_060_ni_m_252d},
    "olec_061_asset_turn_5d": {"inputs": ['revenue', 'assets'], "func": olec_061_asset_turn_5d},
    "olec_062_asset_turn_21d": {"inputs": ['revenue', 'assets'], "func": olec_062_asset_turn_21d},
    "olec_063_asset_turn_63d": {"inputs": ['revenue', 'assets'], "func": olec_063_asset_turn_63d},
    "olec_064_asset_turn_126d": {"inputs": ['revenue', 'assets'], "func": olec_064_asset_turn_126d},
    "olec_065_asset_turn_252d": {"inputs": ['revenue', 'assets'], "func": olec_065_asset_turn_252d},
    "olec_066_fixed_asset_turn_5d": {"inputs": ['revenue', 'ppnent'], "func": olec_066_fixed_asset_turn_5d},
    "olec_067_fixed_asset_turn_21d": {"inputs": ['revenue', 'ppnent'], "func": olec_067_fixed_asset_turn_21d},
    "olec_068_fixed_asset_turn_63d": {"inputs": ['revenue', 'ppnent'], "func": olec_068_fixed_asset_turn_63d},
    "olec_069_fixed_asset_turn_126d": {"inputs": ['revenue', 'ppnent'], "func": olec_069_fixed_asset_turn_126d},
    "olec_070_fixed_asset_turn_252d": {"inputs": ['revenue', 'ppnent'], "func": olec_070_fixed_asset_turn_252d},
    "olec_071_work_cap_turn_5d": {"inputs": ['revenue', 'workingcapital'], "func": olec_071_work_cap_turn_5d},
    "olec_072_work_cap_turn_21d": {"inputs": ['revenue', 'workingcapital'], "func": olec_072_work_cap_turn_21d},
    "olec_073_work_cap_turn_63d": {"inputs": ['revenue', 'workingcapital'], "func": olec_073_work_cap_turn_63d},
    "olec_074_work_cap_turn_126d": {"inputs": ['revenue', 'workingcapital'], "func": olec_074_work_cap_turn_126d},
    "olec_075_work_cap_turn_252d": {"inputs": ['revenue', 'workingcapital'], "func": olec_075_work_cap_turn_252d},
}
