"""
63_cash_earnings_divergence — Base Features 001-075
Domain: OCF vs NetInc (Accrual tracking)
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

def cedv_001_ocf_ni_rat_5d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_001_ocf_ni_rat_5d"""
    return (_safe_div(ocf, netinc)).shift(5)

def cedv_002_ocf_ni_rat_21d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_002_ocf_ni_rat_21d"""
    return (_safe_div(ocf, netinc)).shift(21)

def cedv_003_ocf_ni_rat_63d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_003_ocf_ni_rat_63d"""
    return (_safe_div(ocf, netinc)).shift(63)

def cedv_004_ocf_ni_rat_126d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_004_ocf_ni_rat_126d"""
    return (_safe_div(ocf, netinc)).shift(126)

def cedv_005_ocf_ni_rat_252d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_005_ocf_ni_rat_252d"""
    return (_safe_div(ocf, netinc)).shift(252)

def cedv_006_fcf_ni_rat_5d(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_006_fcf_ni_rat_5d"""
    return (_safe_div(fcf, netinc)).shift(5)

def cedv_007_fcf_ni_rat_21d(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_007_fcf_ni_rat_21d"""
    return (_safe_div(fcf, netinc)).shift(21)

def cedv_008_fcf_ni_rat_63d(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_008_fcf_ni_rat_63d"""
    return (_safe_div(fcf, netinc)).shift(63)

def cedv_009_fcf_ni_rat_126d(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_009_fcf_ni_rat_126d"""
    return (_safe_div(fcf, netinc)).shift(126)

def cedv_010_fcf_ni_rat_252d(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_010_fcf_ni_rat_252d"""
    return (_safe_div(fcf, netinc)).shift(252)

def cedv_011_accrual_assets_5d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_011_accrual_assets_5d"""
    return (_safe_div(netinc - ocf, assets)).shift(5)

def cedv_012_accrual_assets_21d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_012_accrual_assets_21d"""
    return (_safe_div(netinc - ocf, assets)).shift(21)

def cedv_013_accrual_assets_63d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_013_accrual_assets_63d"""
    return (_safe_div(netinc - ocf, assets)).shift(63)

def cedv_014_accrual_assets_126d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_014_accrual_assets_126d"""
    return (_safe_div(netinc - ocf, assets)).shift(126)

def cedv_015_accrual_assets_252d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_015_accrual_assets_252d"""
    return (_safe_div(netinc - ocf, assets)).shift(252)

def cedv_016_working_cap_ocf_5d(ocf: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_016_working_cap_ocf_5d"""
    return (_safe_div(workingcapital.diff(252), ocf)).shift(5)

def cedv_017_working_cap_ocf_21d(ocf: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_017_working_cap_ocf_21d"""
    return (_safe_div(workingcapital.diff(252), ocf)).shift(21)

def cedv_018_working_cap_ocf_63d(ocf: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_018_working_cap_ocf_63d"""
    return (_safe_div(workingcapital.diff(252), ocf)).shift(63)

def cedv_019_working_cap_ocf_126d(ocf: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_019_working_cap_ocf_126d"""
    return (_safe_div(workingcapital.diff(252), ocf)).shift(126)

def cedv_020_working_cap_ocf_252d(ocf: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_020_working_cap_ocf_252d"""
    return (_safe_div(workingcapital.diff(252), ocf)).shift(252)

def cedv_021_ni_margin_5d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cedv_021_ni_margin_5d"""
    return (_safe_div(netinc, revenue)).shift(5)

def cedv_022_ni_margin_21d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cedv_022_ni_margin_21d"""
    return (_safe_div(netinc, revenue)).shift(21)

def cedv_023_ni_margin_63d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cedv_023_ni_margin_63d"""
    return (_safe_div(netinc, revenue)).shift(63)

def cedv_024_ni_margin_126d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cedv_024_ni_margin_126d"""
    return (_safe_div(netinc, revenue)).shift(126)

def cedv_025_ni_margin_252d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """cedv_025_ni_margin_252d"""
    return (_safe_div(netinc, revenue)).shift(252)

def cedv_026_ocf_margin_5d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_026_ocf_margin_5d"""
    return (_safe_div(ocf, revenue)).shift(5)

def cedv_027_ocf_margin_21d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_027_ocf_margin_21d"""
    return (_safe_div(ocf, revenue)).shift(21)

def cedv_028_ocf_margin_63d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_028_ocf_margin_63d"""
    return (_safe_div(ocf, revenue)).shift(63)

def cedv_029_ocf_margin_126d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_029_ocf_margin_126d"""
    return (_safe_div(ocf, revenue)).shift(126)

def cedv_030_ocf_margin_252d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_030_ocf_margin_252d"""
    return (_safe_div(ocf, revenue)).shift(252)

def cedv_031_fcf_margin_5d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_031_fcf_margin_5d"""
    return (_safe_div(fcf, revenue)).shift(5)

def cedv_032_fcf_margin_21d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_032_fcf_margin_21d"""
    return (_safe_div(fcf, revenue)).shift(21)

def cedv_033_fcf_margin_63d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_033_fcf_margin_63d"""
    return (_safe_div(fcf, revenue)).shift(63)

def cedv_034_fcf_margin_126d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_034_fcf_margin_126d"""
    return (_safe_div(fcf, revenue)).shift(126)

def cedv_035_fcf_margin_252d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """cedv_035_fcf_margin_252d"""
    return (_safe_div(fcf, revenue)).shift(252)

def cedv_036_capex_ocf_5d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """cedv_036_capex_ocf_5d"""
    return (_safe_div(capex, ocf)).shift(5)

def cedv_037_capex_ocf_21d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """cedv_037_capex_ocf_21d"""
    return (_safe_div(capex, ocf)).shift(21)

def cedv_038_capex_ocf_63d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """cedv_038_capex_ocf_63d"""
    return (_safe_div(capex, ocf)).shift(63)

def cedv_039_capex_ocf_126d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """cedv_039_capex_ocf_126d"""
    return (_safe_div(capex, ocf)).shift(126)

def cedv_040_capex_ocf_252d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """cedv_040_capex_ocf_252d"""
    return (_safe_div(capex, ocf)).shift(252)

def cedv_041_ni_g_5d(netinc: pd.Series) -> pd.Series:
    """cedv_041_ni_g_5d"""
    return (netinc.pct_change(252)).shift(5)

def cedv_042_ni_g_21d(netinc: pd.Series) -> pd.Series:
    """cedv_042_ni_g_21d"""
    return (netinc.pct_change(252)).shift(21)

def cedv_043_ni_g_63d(netinc: pd.Series) -> pd.Series:
    """cedv_043_ni_g_63d"""
    return (netinc.pct_change(252)).shift(63)

def cedv_044_ni_g_126d(netinc: pd.Series) -> pd.Series:
    """cedv_044_ni_g_126d"""
    return (netinc.pct_change(252)).shift(126)

def cedv_045_ni_g_252d(netinc: pd.Series) -> pd.Series:
    """cedv_045_ni_g_252d"""
    return (netinc.pct_change(252)).shift(252)

def cedv_046_ocf_g_5d(ocf: pd.Series) -> pd.Series:
    """cedv_046_ocf_g_5d"""
    return (ocf.pct_change(252)).shift(5)

def cedv_047_ocf_g_21d(ocf: pd.Series) -> pd.Series:
    """cedv_047_ocf_g_21d"""
    return (ocf.pct_change(252)).shift(21)

def cedv_048_ocf_g_63d(ocf: pd.Series) -> pd.Series:
    """cedv_048_ocf_g_63d"""
    return (ocf.pct_change(252)).shift(63)

def cedv_049_ocf_g_126d(ocf: pd.Series) -> pd.Series:
    """cedv_049_ocf_g_126d"""
    return (ocf.pct_change(252)).shift(126)

def cedv_050_ocf_g_252d(ocf: pd.Series) -> pd.Series:
    """cedv_050_ocf_g_252d"""
    return (ocf.pct_change(252)).shift(252)

def cedv_051_div_g_5d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_051_div_g_5d"""
    return ((netinc - ocf).diff(252)).shift(5)

def cedv_052_div_g_21d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_052_div_g_21d"""
    return ((netinc - ocf).diff(252)).shift(21)

def cedv_053_div_g_63d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_053_div_g_63d"""
    return ((netinc - ocf).diff(252)).shift(63)

def cedv_054_div_g_126d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_054_div_g_126d"""
    return ((netinc - ocf).diff(252)).shift(126)

def cedv_055_div_g_252d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_055_div_g_252d"""
    return ((netinc - ocf).diff(252)).shift(252)

def cedv_056_asset_g_5d(assets: pd.Series) -> pd.Series:
    """cedv_056_asset_g_5d"""
    return (assets.pct_change(252)).shift(5)

def cedv_057_asset_g_21d(assets: pd.Series) -> pd.Series:
    """cedv_057_asset_g_21d"""
    return (assets.pct_change(252)).shift(21)

def cedv_058_asset_g_63d(assets: pd.Series) -> pd.Series:
    """cedv_058_asset_g_63d"""
    return (assets.pct_change(252)).shift(63)

def cedv_059_asset_g_126d(assets: pd.Series) -> pd.Series:
    """cedv_059_asset_g_126d"""
    return (assets.pct_change(252)).shift(126)

def cedv_060_asset_g_252d(assets: pd.Series) -> pd.Series:
    """cedv_060_asset_g_252d"""
    return (assets.pct_change(252)).shift(252)

def cedv_061_liab_g_5d(liabs: pd.Series) -> pd.Series:
    """cedv_061_liab_g_5d"""
    return (liabs.pct_change(252)).shift(5)

def cedv_062_liab_g_21d(liabs: pd.Series) -> pd.Series:
    """cedv_062_liab_g_21d"""
    return (liabs.pct_change(252)).shift(21)

def cedv_063_liab_g_63d(liabs: pd.Series) -> pd.Series:
    """cedv_063_liab_g_63d"""
    return (liabs.pct_change(252)).shift(63)

def cedv_064_liab_g_126d(liabs: pd.Series) -> pd.Series:
    """cedv_064_liab_g_126d"""
    return (liabs.pct_change(252)).shift(126)

def cedv_065_liab_g_252d(liabs: pd.Series) -> pd.Series:
    """cedv_065_liab_g_252d"""
    return (liabs.pct_change(252)).shift(252)

def cedv_066_equity_g_5d(equity: pd.Series) -> pd.Series:
    """cedv_066_equity_g_5d"""
    return (equity.pct_change(252)).shift(5)

def cedv_067_equity_g_21d(equity: pd.Series) -> pd.Series:
    """cedv_067_equity_g_21d"""
    return (equity.pct_change(252)).shift(21)

def cedv_068_equity_g_63d(equity: pd.Series) -> pd.Series:
    """cedv_068_equity_g_63d"""
    return (equity.pct_change(252)).shift(63)

def cedv_069_equity_g_126d(equity: pd.Series) -> pd.Series:
    """cedv_069_equity_g_126d"""
    return (equity.pct_change(252)).shift(126)

def cedv_070_equity_g_252d(equity: pd.Series) -> pd.Series:
    """cedv_070_equity_g_252d"""
    return (equity.pct_change(252)).shift(252)

def cedv_071_mc_ocf_5d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_071_mc_ocf_5d"""
    return (_safe_div(marketcap, ocf)).shift(5)

def cedv_072_mc_ocf_21d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_072_mc_ocf_21d"""
    return (_safe_div(marketcap, ocf)).shift(21)

def cedv_073_mc_ocf_63d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_073_mc_ocf_63d"""
    return (_safe_div(marketcap, ocf)).shift(63)

def cedv_074_mc_ocf_126d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_074_mc_ocf_126d"""
    return (_safe_div(marketcap, ocf)).shift(126)

def cedv_075_mc_ocf_252d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_075_mc_ocf_252d"""
    return (_safe_div(marketcap, ocf)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V63_REGISTRY = {
    "cedv_001_ocf_ni_rat_5d": {"inputs": ['netinc', 'ocf'], "func": cedv_001_ocf_ni_rat_5d},
    "cedv_002_ocf_ni_rat_21d": {"inputs": ['netinc', 'ocf'], "func": cedv_002_ocf_ni_rat_21d},
    "cedv_003_ocf_ni_rat_63d": {"inputs": ['netinc', 'ocf'], "func": cedv_003_ocf_ni_rat_63d},
    "cedv_004_ocf_ni_rat_126d": {"inputs": ['netinc', 'ocf'], "func": cedv_004_ocf_ni_rat_126d},
    "cedv_005_ocf_ni_rat_252d": {"inputs": ['netinc', 'ocf'], "func": cedv_005_ocf_ni_rat_252d},
    "cedv_006_fcf_ni_rat_5d": {"inputs": ['netinc', 'fcf'], "func": cedv_006_fcf_ni_rat_5d},
    "cedv_007_fcf_ni_rat_21d": {"inputs": ['netinc', 'fcf'], "func": cedv_007_fcf_ni_rat_21d},
    "cedv_008_fcf_ni_rat_63d": {"inputs": ['netinc', 'fcf'], "func": cedv_008_fcf_ni_rat_63d},
    "cedv_009_fcf_ni_rat_126d": {"inputs": ['netinc', 'fcf'], "func": cedv_009_fcf_ni_rat_126d},
    "cedv_010_fcf_ni_rat_252d": {"inputs": ['netinc', 'fcf'], "func": cedv_010_fcf_ni_rat_252d},
    "cedv_011_accrual_assets_5d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_011_accrual_assets_5d},
    "cedv_012_accrual_assets_21d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_012_accrual_assets_21d},
    "cedv_013_accrual_assets_63d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_013_accrual_assets_63d},
    "cedv_014_accrual_assets_126d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_014_accrual_assets_126d},
    "cedv_015_accrual_assets_252d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_015_accrual_assets_252d},
    "cedv_016_working_cap_ocf_5d": {"inputs": ['ocf', 'workingcapital'], "func": cedv_016_working_cap_ocf_5d},
    "cedv_017_working_cap_ocf_21d": {"inputs": ['ocf', 'workingcapital'], "func": cedv_017_working_cap_ocf_21d},
    "cedv_018_working_cap_ocf_63d": {"inputs": ['ocf', 'workingcapital'], "func": cedv_018_working_cap_ocf_63d},
    "cedv_019_working_cap_ocf_126d": {"inputs": ['ocf', 'workingcapital'], "func": cedv_019_working_cap_ocf_126d},
    "cedv_020_working_cap_ocf_252d": {"inputs": ['ocf', 'workingcapital'], "func": cedv_020_working_cap_ocf_252d},
    "cedv_021_ni_margin_5d": {"inputs": ['revenue', 'netinc'], "func": cedv_021_ni_margin_5d},
    "cedv_022_ni_margin_21d": {"inputs": ['revenue', 'netinc'], "func": cedv_022_ni_margin_21d},
    "cedv_023_ni_margin_63d": {"inputs": ['revenue', 'netinc'], "func": cedv_023_ni_margin_63d},
    "cedv_024_ni_margin_126d": {"inputs": ['revenue', 'netinc'], "func": cedv_024_ni_margin_126d},
    "cedv_025_ni_margin_252d": {"inputs": ['revenue', 'netinc'], "func": cedv_025_ni_margin_252d},
    "cedv_026_ocf_margin_5d": {"inputs": ['revenue', 'ocf'], "func": cedv_026_ocf_margin_5d},
    "cedv_027_ocf_margin_21d": {"inputs": ['revenue', 'ocf'], "func": cedv_027_ocf_margin_21d},
    "cedv_028_ocf_margin_63d": {"inputs": ['revenue', 'ocf'], "func": cedv_028_ocf_margin_63d},
    "cedv_029_ocf_margin_126d": {"inputs": ['revenue', 'ocf'], "func": cedv_029_ocf_margin_126d},
    "cedv_030_ocf_margin_252d": {"inputs": ['revenue', 'ocf'], "func": cedv_030_ocf_margin_252d},
    "cedv_031_fcf_margin_5d": {"inputs": ['revenue', 'fcf'], "func": cedv_031_fcf_margin_5d},
    "cedv_032_fcf_margin_21d": {"inputs": ['revenue', 'fcf'], "func": cedv_032_fcf_margin_21d},
    "cedv_033_fcf_margin_63d": {"inputs": ['revenue', 'fcf'], "func": cedv_033_fcf_margin_63d},
    "cedv_034_fcf_margin_126d": {"inputs": ['revenue', 'fcf'], "func": cedv_034_fcf_margin_126d},
    "cedv_035_fcf_margin_252d": {"inputs": ['revenue', 'fcf'], "func": cedv_035_fcf_margin_252d},
    "cedv_036_capex_ocf_5d": {"inputs": ['ocf', 'capex'], "func": cedv_036_capex_ocf_5d},
    "cedv_037_capex_ocf_21d": {"inputs": ['ocf', 'capex'], "func": cedv_037_capex_ocf_21d},
    "cedv_038_capex_ocf_63d": {"inputs": ['ocf', 'capex'], "func": cedv_038_capex_ocf_63d},
    "cedv_039_capex_ocf_126d": {"inputs": ['ocf', 'capex'], "func": cedv_039_capex_ocf_126d},
    "cedv_040_capex_ocf_252d": {"inputs": ['ocf', 'capex'], "func": cedv_040_capex_ocf_252d},
    "cedv_041_ni_g_5d": {"inputs": ['netinc'], "func": cedv_041_ni_g_5d},
    "cedv_042_ni_g_21d": {"inputs": ['netinc'], "func": cedv_042_ni_g_21d},
    "cedv_043_ni_g_63d": {"inputs": ['netinc'], "func": cedv_043_ni_g_63d},
    "cedv_044_ni_g_126d": {"inputs": ['netinc'], "func": cedv_044_ni_g_126d},
    "cedv_045_ni_g_252d": {"inputs": ['netinc'], "func": cedv_045_ni_g_252d},
    "cedv_046_ocf_g_5d": {"inputs": ['ocf'], "func": cedv_046_ocf_g_5d},
    "cedv_047_ocf_g_21d": {"inputs": ['ocf'], "func": cedv_047_ocf_g_21d},
    "cedv_048_ocf_g_63d": {"inputs": ['ocf'], "func": cedv_048_ocf_g_63d},
    "cedv_049_ocf_g_126d": {"inputs": ['ocf'], "func": cedv_049_ocf_g_126d},
    "cedv_050_ocf_g_252d": {"inputs": ['ocf'], "func": cedv_050_ocf_g_252d},
    "cedv_051_div_g_5d": {"inputs": ['netinc', 'ocf'], "func": cedv_051_div_g_5d},
    "cedv_052_div_g_21d": {"inputs": ['netinc', 'ocf'], "func": cedv_052_div_g_21d},
    "cedv_053_div_g_63d": {"inputs": ['netinc', 'ocf'], "func": cedv_053_div_g_63d},
    "cedv_054_div_g_126d": {"inputs": ['netinc', 'ocf'], "func": cedv_054_div_g_126d},
    "cedv_055_div_g_252d": {"inputs": ['netinc', 'ocf'], "func": cedv_055_div_g_252d},
    "cedv_056_asset_g_5d": {"inputs": ['assets'], "func": cedv_056_asset_g_5d},
    "cedv_057_asset_g_21d": {"inputs": ['assets'], "func": cedv_057_asset_g_21d},
    "cedv_058_asset_g_63d": {"inputs": ['assets'], "func": cedv_058_asset_g_63d},
    "cedv_059_asset_g_126d": {"inputs": ['assets'], "func": cedv_059_asset_g_126d},
    "cedv_060_asset_g_252d": {"inputs": ['assets'], "func": cedv_060_asset_g_252d},
    "cedv_061_liab_g_5d": {"inputs": ['liabs'], "func": cedv_061_liab_g_5d},
    "cedv_062_liab_g_21d": {"inputs": ['liabs'], "func": cedv_062_liab_g_21d},
    "cedv_063_liab_g_63d": {"inputs": ['liabs'], "func": cedv_063_liab_g_63d},
    "cedv_064_liab_g_126d": {"inputs": ['liabs'], "func": cedv_064_liab_g_126d},
    "cedv_065_liab_g_252d": {"inputs": ['liabs'], "func": cedv_065_liab_g_252d},
    "cedv_066_equity_g_5d": {"inputs": ['equity'], "func": cedv_066_equity_g_5d},
    "cedv_067_equity_g_21d": {"inputs": ['equity'], "func": cedv_067_equity_g_21d},
    "cedv_068_equity_g_63d": {"inputs": ['equity'], "func": cedv_068_equity_g_63d},
    "cedv_069_equity_g_126d": {"inputs": ['equity'], "func": cedv_069_equity_g_126d},
    "cedv_070_equity_g_252d": {"inputs": ['equity'], "func": cedv_070_equity_g_252d},
    "cedv_071_mc_ocf_5d": {"inputs": ['ocf', 'marketcap'], "func": cedv_071_mc_ocf_5d},
    "cedv_072_mc_ocf_21d": {"inputs": ['ocf', 'marketcap'], "func": cedv_072_mc_ocf_21d},
    "cedv_073_mc_ocf_63d": {"inputs": ['ocf', 'marketcap'], "func": cedv_073_mc_ocf_63d},
    "cedv_074_mc_ocf_126d": {"inputs": ['ocf', 'marketcap'], "func": cedv_074_mc_ocf_126d},
    "cedv_075_mc_ocf_252d": {"inputs": ['ocf', 'marketcap'], "func": cedv_075_mc_ocf_252d},
}
