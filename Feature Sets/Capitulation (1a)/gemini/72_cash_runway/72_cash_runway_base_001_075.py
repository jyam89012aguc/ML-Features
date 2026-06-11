"""
72_cash_runway — Base Features 001-075
Domain: Cash / Burn rate (OCF negative)
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

def runw_001_cash_burn_rat_5d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_001_cash_burn_rat_5d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).shift(5)

def runw_002_cash_burn_rat_21d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_002_cash_burn_rat_21d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).shift(21)

def runw_003_cash_burn_rat_63d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_003_cash_burn_rat_63d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).shift(63)

def runw_004_cash_burn_rat_126d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_004_cash_burn_rat_126d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).shift(126)

def runw_005_cash_burn_rat_252d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_005_cash_burn_rat_252d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).shift(252)

def runw_006_cash_assets_5d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_006_cash_assets_5d"""
    return (_safe_div(cashnequiv, assets)).shift(5)

def runw_007_cash_assets_21d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_007_cash_assets_21d"""
    return (_safe_div(cashnequiv, assets)).shift(21)

def runw_008_cash_assets_63d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_008_cash_assets_63d"""
    return (_safe_div(cashnequiv, assets)).shift(63)

def runw_009_cash_assets_126d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_009_cash_assets_126d"""
    return (_safe_div(cashnequiv, assets)).shift(126)

def runw_010_cash_assets_252d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_010_cash_assets_252d"""
    return (_safe_div(cashnequiv, assets)).shift(252)

def runw_011_cash_liabs_5d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_011_cash_liabs_5d"""
    return (_safe_div(cashnequiv, liabs)).shift(5)

def runw_012_cash_liabs_21d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_012_cash_liabs_21d"""
    return (_safe_div(cashnequiv, liabs)).shift(21)

def runw_013_cash_liabs_63d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_013_cash_liabs_63d"""
    return (_safe_div(cashnequiv, liabs)).shift(63)

def runw_014_cash_liabs_126d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_014_cash_liabs_126d"""
    return (_safe_div(cashnequiv, liabs)).shift(126)

def runw_015_cash_liabs_252d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_015_cash_liabs_252d"""
    return (_safe_div(cashnequiv, liabs)).shift(252)

def runw_016_cash_marketcap_5d(cashnequiv: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_016_cash_marketcap_5d"""
    return (_safe_div(cashnequiv, marketcap)).shift(5)

def runw_017_cash_marketcap_21d(cashnequiv: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_017_cash_marketcap_21d"""
    return (_safe_div(cashnequiv, marketcap)).shift(21)

def runw_018_cash_marketcap_63d(cashnequiv: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_018_cash_marketcap_63d"""
    return (_safe_div(cashnequiv, marketcap)).shift(63)

def runw_019_cash_marketcap_126d(cashnequiv: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_019_cash_marketcap_126d"""
    return (_safe_div(cashnequiv, marketcap)).shift(126)

def runw_020_cash_marketcap_252d(cashnequiv: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_020_cash_marketcap_252d"""
    return (_safe_div(cashnequiv, marketcap)).shift(252)

def runw_021_ocf_negative_ind_5d(ocf: pd.Series) -> pd.Series:
    """runw_021_ocf_negative_ind_5d"""
    return ((ocf < 0).astype(float)).shift(5)

def runw_022_ocf_negative_ind_21d(ocf: pd.Series) -> pd.Series:
    """runw_022_ocf_negative_ind_21d"""
    return ((ocf < 0).astype(float)).shift(21)

def runw_023_ocf_negative_ind_63d(ocf: pd.Series) -> pd.Series:
    """runw_023_ocf_negative_ind_63d"""
    return ((ocf < 0).astype(float)).shift(63)

def runw_024_ocf_negative_ind_126d(ocf: pd.Series) -> pd.Series:
    """runw_024_ocf_negative_ind_126d"""
    return ((ocf < 0).astype(float)).shift(126)

def runw_025_ocf_negative_ind_252d(ocf: pd.Series) -> pd.Series:
    """runw_025_ocf_negative_ind_252d"""
    return ((ocf < 0).astype(float)).shift(252)

def runw_026_fcf_negative_ind_5d(fcf: pd.Series) -> pd.Series:
    """runw_026_fcf_negative_ind_5d"""
    return ((fcf < 0).astype(float)).shift(5)

def runw_027_fcf_negative_ind_21d(fcf: pd.Series) -> pd.Series:
    """runw_027_fcf_negative_ind_21d"""
    return ((fcf < 0).astype(float)).shift(21)

def runw_028_fcf_negative_ind_63d(fcf: pd.Series) -> pd.Series:
    """runw_028_fcf_negative_ind_63d"""
    return ((fcf < 0).astype(float)).shift(63)

def runw_029_fcf_negative_ind_126d(fcf: pd.Series) -> pd.Series:
    """runw_029_fcf_negative_ind_126d"""
    return ((fcf < 0).astype(float)).shift(126)

def runw_030_fcf_negative_ind_252d(fcf: pd.Series) -> pd.Series:
    """runw_030_fcf_negative_ind_252d"""
    return ((fcf < 0).astype(float)).shift(252)

def runw_031_burn_rate_g_5d(ocf: pd.Series) -> pd.Series:
    """runw_031_burn_rate_g_5d"""
    return (ocf.clip(upper=-_EPS).abs().pct_change(252)).shift(5)

def runw_032_burn_rate_g_21d(ocf: pd.Series) -> pd.Series:
    """runw_032_burn_rate_g_21d"""
    return (ocf.clip(upper=-_EPS).abs().pct_change(252)).shift(21)

def runw_033_burn_rate_g_63d(ocf: pd.Series) -> pd.Series:
    """runw_033_burn_rate_g_63d"""
    return (ocf.clip(upper=-_EPS).abs().pct_change(252)).shift(63)

def runw_034_burn_rate_g_126d(ocf: pd.Series) -> pd.Series:
    """runw_034_burn_rate_g_126d"""
    return (ocf.clip(upper=-_EPS).abs().pct_change(252)).shift(126)

def runw_035_burn_rate_g_252d(ocf: pd.Series) -> pd.Series:
    """runw_035_burn_rate_g_252d"""
    return (ocf.clip(upper=-_EPS).abs().pct_change(252)).shift(252)

def runw_036_cash_g_5d(cashnequiv: pd.Series) -> pd.Series:
    """runw_036_cash_g_5d"""
    return (cashnequiv.pct_change(252)).shift(5)

def runw_037_cash_g_21d(cashnequiv: pd.Series) -> pd.Series:
    """runw_037_cash_g_21d"""
    return (cashnequiv.pct_change(252)).shift(21)

def runw_038_cash_g_63d(cashnequiv: pd.Series) -> pd.Series:
    """runw_038_cash_g_63d"""
    return (cashnequiv.pct_change(252)).shift(63)

def runw_039_cash_g_126d(cashnequiv: pd.Series) -> pd.Series:
    """runw_039_cash_g_126d"""
    return (cashnequiv.pct_change(252)).shift(126)

def runw_040_cash_g_252d(cashnequiv: pd.Series) -> pd.Series:
    """runw_040_cash_g_252d"""
    return (cashnequiv.pct_change(252)).shift(252)

def runw_041_runway_months_5d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_041_runway_months_5d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs() / 12)).shift(5)

def runw_042_runway_months_21d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_042_runway_months_21d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs() / 12)).shift(21)

def runw_043_runway_months_63d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_043_runway_months_63d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs() / 12)).shift(63)

def runw_044_runway_months_126d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_044_runway_months_126d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs() / 12)).shift(126)

def runw_045_runway_months_252d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_045_runway_months_252d"""
    return (_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs() / 12)).shift(252)

def runw_046_survival_index_5d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_046_survival_index_5d"""
    return (_safe_div(cashnequiv + ocf.rolling(252).sum().clip(lower=0), ocf.rolling(252).sum().clip(upper=-_EPS).abs())).shift(5)

def runw_047_survival_index_21d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_047_survival_index_21d"""
    return (_safe_div(cashnequiv + ocf.rolling(252).sum().clip(lower=0), ocf.rolling(252).sum().clip(upper=-_EPS).abs())).shift(21)

def runw_048_survival_index_63d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_048_survival_index_63d"""
    return (_safe_div(cashnequiv + ocf.rolling(252).sum().clip(lower=0), ocf.rolling(252).sum().clip(upper=-_EPS).abs())).shift(63)

def runw_049_survival_index_126d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_049_survival_index_126d"""
    return (_safe_div(cashnequiv + ocf.rolling(252).sum().clip(lower=0), ocf.rolling(252).sum().clip(upper=-_EPS).abs())).shift(126)

def runw_050_survival_index_252d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_050_survival_index_252d"""
    return (_safe_div(cashnequiv + ocf.rolling(252).sum().clip(lower=0), ocf.rolling(252).sum().clip(upper=-_EPS).abs())).shift(252)

def runw_051_distress_z_5d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_051_distress_z_5d"""
    return (_zscore_rolling(_safe_div(cashnequiv, assets), 1260)).shift(5)

def runw_052_distress_z_21d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_052_distress_z_21d"""
    return (_zscore_rolling(_safe_div(cashnequiv, assets), 1260)).shift(21)

def runw_053_distress_z_63d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_053_distress_z_63d"""
    return (_zscore_rolling(_safe_div(cashnequiv, assets), 1260)).shift(63)

def runw_054_distress_z_126d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_054_distress_z_126d"""
    return (_zscore_rolling(_safe_div(cashnequiv, assets), 1260)).shift(126)

def runw_055_distress_z_252d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_055_distress_z_252d"""
    return (_zscore_rolling(_safe_div(cashnequiv, assets), 1260)).shift(252)

def runw_056_liquidity_rat_5d(cashnequiv: pd.Series, receivables: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_056_liquidity_rat_5d"""
    return (_safe_div(cashnequiv + receivables, currentassets)).shift(5)

def runw_057_liquidity_rat_21d(cashnequiv: pd.Series, receivables: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_057_liquidity_rat_21d"""
    return (_safe_div(cashnequiv + receivables, currentassets)).shift(21)

def runw_058_liquidity_rat_63d(cashnequiv: pd.Series, receivables: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_058_liquidity_rat_63d"""
    return (_safe_div(cashnequiv + receivables, currentassets)).shift(63)

def runw_059_liquidity_rat_126d(cashnequiv: pd.Series, receivables: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_059_liquidity_rat_126d"""
    return (_safe_div(cashnequiv + receivables, currentassets)).shift(126)

def runw_060_liquidity_rat_252d(cashnequiv: pd.Series, receivables: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_060_liquidity_rat_252d"""
    return (_safe_div(cashnequiv + receivables, currentassets)).shift(252)

def runw_061_quick_rat_5d(liabs: pd.Series, inventory: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_061_quick_rat_5d"""
    return (_safe_div(currentassets - inventory, liabs)).shift(5)

def runw_062_quick_rat_21d(liabs: pd.Series, inventory: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_062_quick_rat_21d"""
    return (_safe_div(currentassets - inventory, liabs)).shift(21)

def runw_063_quick_rat_63d(liabs: pd.Series, inventory: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_063_quick_rat_63d"""
    return (_safe_div(currentassets - inventory, liabs)).shift(63)

def runw_064_quick_rat_126d(liabs: pd.Series, inventory: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_064_quick_rat_126d"""
    return (_safe_div(currentassets - inventory, liabs)).shift(126)

def runw_065_quick_rat_252d(liabs: pd.Series, inventory: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_065_quick_rat_252d"""
    return (_safe_div(currentassets - inventory, liabs)).shift(252)

def runw_066_current_rat_5d(liabs: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_066_current_rat_5d"""
    return (_safe_div(currentassets, liabs)).shift(5)

def runw_067_current_rat_21d(liabs: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_067_current_rat_21d"""
    return (_safe_div(currentassets, liabs)).shift(21)

def runw_068_current_rat_63d(liabs: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_068_current_rat_63d"""
    return (_safe_div(currentassets, liabs)).shift(63)

def runw_069_current_rat_126d(liabs: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_069_current_rat_126d"""
    return (_safe_div(currentassets, liabs)).shift(126)

def runw_070_current_rat_252d(liabs: pd.Series, currentassets: pd.Series) -> pd.Series:
    """runw_070_current_rat_252d"""
    return (_safe_div(currentassets, liabs)).shift(252)

def runw_071_working_cap_assets_5d(assets: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """runw_071_working_cap_assets_5d"""
    return (_safe_div(workingcapital, assets)).shift(5)

def runw_072_working_cap_assets_21d(assets: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """runw_072_working_cap_assets_21d"""
    return (_safe_div(workingcapital, assets)).shift(21)

def runw_073_working_cap_assets_63d(assets: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """runw_073_working_cap_assets_63d"""
    return (_safe_div(workingcapital, assets)).shift(63)

def runw_074_working_cap_assets_126d(assets: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """runw_074_working_cap_assets_126d"""
    return (_safe_div(workingcapital, assets)).shift(126)

def runw_075_working_cap_assets_252d(assets: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """runw_075_working_cap_assets_252d"""
    return (_safe_div(workingcapital, assets)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V72_REGISTRY = {
    "runw_001_cash_burn_rat_5d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_001_cash_burn_rat_5d},
    "runw_002_cash_burn_rat_21d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_002_cash_burn_rat_21d},
    "runw_003_cash_burn_rat_63d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_003_cash_burn_rat_63d},
    "runw_004_cash_burn_rat_126d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_004_cash_burn_rat_126d},
    "runw_005_cash_burn_rat_252d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_005_cash_burn_rat_252d},
    "runw_006_cash_assets_5d": {"inputs": ['assets', 'cashnequiv'], "func": runw_006_cash_assets_5d},
    "runw_007_cash_assets_21d": {"inputs": ['assets', 'cashnequiv'], "func": runw_007_cash_assets_21d},
    "runw_008_cash_assets_63d": {"inputs": ['assets', 'cashnequiv'], "func": runw_008_cash_assets_63d},
    "runw_009_cash_assets_126d": {"inputs": ['assets', 'cashnequiv'], "func": runw_009_cash_assets_126d},
    "runw_010_cash_assets_252d": {"inputs": ['assets', 'cashnequiv'], "func": runw_010_cash_assets_252d},
    "runw_011_cash_liabs_5d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_011_cash_liabs_5d},
    "runw_012_cash_liabs_21d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_012_cash_liabs_21d},
    "runw_013_cash_liabs_63d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_013_cash_liabs_63d},
    "runw_014_cash_liabs_126d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_014_cash_liabs_126d},
    "runw_015_cash_liabs_252d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_015_cash_liabs_252d},
    "runw_016_cash_marketcap_5d": {"inputs": ['cashnequiv', 'marketcap'], "func": runw_016_cash_marketcap_5d},
    "runw_017_cash_marketcap_21d": {"inputs": ['cashnequiv', 'marketcap'], "func": runw_017_cash_marketcap_21d},
    "runw_018_cash_marketcap_63d": {"inputs": ['cashnequiv', 'marketcap'], "func": runw_018_cash_marketcap_63d},
    "runw_019_cash_marketcap_126d": {"inputs": ['cashnequiv', 'marketcap'], "func": runw_019_cash_marketcap_126d},
    "runw_020_cash_marketcap_252d": {"inputs": ['cashnequiv', 'marketcap'], "func": runw_020_cash_marketcap_252d},
    "runw_021_ocf_negative_ind_5d": {"inputs": ['ocf'], "func": runw_021_ocf_negative_ind_5d},
    "runw_022_ocf_negative_ind_21d": {"inputs": ['ocf'], "func": runw_022_ocf_negative_ind_21d},
    "runw_023_ocf_negative_ind_63d": {"inputs": ['ocf'], "func": runw_023_ocf_negative_ind_63d},
    "runw_024_ocf_negative_ind_126d": {"inputs": ['ocf'], "func": runw_024_ocf_negative_ind_126d},
    "runw_025_ocf_negative_ind_252d": {"inputs": ['ocf'], "func": runw_025_ocf_negative_ind_252d},
    "runw_026_fcf_negative_ind_5d": {"inputs": ['fcf'], "func": runw_026_fcf_negative_ind_5d},
    "runw_027_fcf_negative_ind_21d": {"inputs": ['fcf'], "func": runw_027_fcf_negative_ind_21d},
    "runw_028_fcf_negative_ind_63d": {"inputs": ['fcf'], "func": runw_028_fcf_negative_ind_63d},
    "runw_029_fcf_negative_ind_126d": {"inputs": ['fcf'], "func": runw_029_fcf_negative_ind_126d},
    "runw_030_fcf_negative_ind_252d": {"inputs": ['fcf'], "func": runw_030_fcf_negative_ind_252d},
    "runw_031_burn_rate_g_5d": {"inputs": ['ocf'], "func": runw_031_burn_rate_g_5d},
    "runw_032_burn_rate_g_21d": {"inputs": ['ocf'], "func": runw_032_burn_rate_g_21d},
    "runw_033_burn_rate_g_63d": {"inputs": ['ocf'], "func": runw_033_burn_rate_g_63d},
    "runw_034_burn_rate_g_126d": {"inputs": ['ocf'], "func": runw_034_burn_rate_g_126d},
    "runw_035_burn_rate_g_252d": {"inputs": ['ocf'], "func": runw_035_burn_rate_g_252d},
    "runw_036_cash_g_5d": {"inputs": ['cashnequiv'], "func": runw_036_cash_g_5d},
    "runw_037_cash_g_21d": {"inputs": ['cashnequiv'], "func": runw_037_cash_g_21d},
    "runw_038_cash_g_63d": {"inputs": ['cashnequiv'], "func": runw_038_cash_g_63d},
    "runw_039_cash_g_126d": {"inputs": ['cashnequiv'], "func": runw_039_cash_g_126d},
    "runw_040_cash_g_252d": {"inputs": ['cashnequiv'], "func": runw_040_cash_g_252d},
    "runw_041_runway_months_5d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_041_runway_months_5d},
    "runw_042_runway_months_21d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_042_runway_months_21d},
    "runw_043_runway_months_63d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_043_runway_months_63d},
    "runw_044_runway_months_126d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_044_runway_months_126d},
    "runw_045_runway_months_252d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_045_runway_months_252d},
    "runw_046_survival_index_5d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_046_survival_index_5d},
    "runw_047_survival_index_21d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_047_survival_index_21d},
    "runw_048_survival_index_63d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_048_survival_index_63d},
    "runw_049_survival_index_126d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_049_survival_index_126d},
    "runw_050_survival_index_252d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_050_survival_index_252d},
    "runw_051_distress_z_5d": {"inputs": ['assets', 'cashnequiv'], "func": runw_051_distress_z_5d},
    "runw_052_distress_z_21d": {"inputs": ['assets', 'cashnequiv'], "func": runw_052_distress_z_21d},
    "runw_053_distress_z_63d": {"inputs": ['assets', 'cashnequiv'], "func": runw_053_distress_z_63d},
    "runw_054_distress_z_126d": {"inputs": ['assets', 'cashnequiv'], "func": runw_054_distress_z_126d},
    "runw_055_distress_z_252d": {"inputs": ['assets', 'cashnequiv'], "func": runw_055_distress_z_252d},
    "runw_056_liquidity_rat_5d": {"inputs": ['cashnequiv', 'receivables', 'currentassets'], "func": runw_056_liquidity_rat_5d},
    "runw_057_liquidity_rat_21d": {"inputs": ['cashnequiv', 'receivables', 'currentassets'], "func": runw_057_liquidity_rat_21d},
    "runw_058_liquidity_rat_63d": {"inputs": ['cashnequiv', 'receivables', 'currentassets'], "func": runw_058_liquidity_rat_63d},
    "runw_059_liquidity_rat_126d": {"inputs": ['cashnequiv', 'receivables', 'currentassets'], "func": runw_059_liquidity_rat_126d},
    "runw_060_liquidity_rat_252d": {"inputs": ['cashnequiv', 'receivables', 'currentassets'], "func": runw_060_liquidity_rat_252d},
    "runw_061_quick_rat_5d": {"inputs": ['liabs', 'inventory', 'currentassets'], "func": runw_061_quick_rat_5d},
    "runw_062_quick_rat_21d": {"inputs": ['liabs', 'inventory', 'currentassets'], "func": runw_062_quick_rat_21d},
    "runw_063_quick_rat_63d": {"inputs": ['liabs', 'inventory', 'currentassets'], "func": runw_063_quick_rat_63d},
    "runw_064_quick_rat_126d": {"inputs": ['liabs', 'inventory', 'currentassets'], "func": runw_064_quick_rat_126d},
    "runw_065_quick_rat_252d": {"inputs": ['liabs', 'inventory', 'currentassets'], "func": runw_065_quick_rat_252d},
    "runw_066_current_rat_5d": {"inputs": ['liabs', 'currentassets'], "func": runw_066_current_rat_5d},
    "runw_067_current_rat_21d": {"inputs": ['liabs', 'currentassets'], "func": runw_067_current_rat_21d},
    "runw_068_current_rat_63d": {"inputs": ['liabs', 'currentassets'], "func": runw_068_current_rat_63d},
    "runw_069_current_rat_126d": {"inputs": ['liabs', 'currentassets'], "func": runw_069_current_rat_126d},
    "runw_070_current_rat_252d": {"inputs": ['liabs', 'currentassets'], "func": runw_070_current_rat_252d},
    "runw_071_working_cap_assets_5d": {"inputs": ['assets', 'workingcapital'], "func": runw_071_working_cap_assets_5d},
    "runw_072_working_cap_assets_21d": {"inputs": ['assets', 'workingcapital'], "func": runw_072_working_cap_assets_21d},
    "runw_073_working_cap_assets_63d": {"inputs": ['assets', 'workingcapital'], "func": runw_073_working_cap_assets_63d},
    "runw_074_working_cap_assets_126d": {"inputs": ['assets', 'workingcapital'], "func": runw_074_working_cap_assets_126d},
    "runw_075_working_cap_assets_252d": {"inputs": ['assets', 'workingcapital'], "func": runw_075_working_cap_assets_252d},
}
