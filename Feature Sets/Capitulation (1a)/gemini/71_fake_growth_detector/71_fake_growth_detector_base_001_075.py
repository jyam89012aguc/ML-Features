"""
71_fake_growth_detector — Base Features 001-075
Domain: Debt-funded revenue growth signals
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

def fgrd_001_debt_funded_growth_5d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_001_debt_funded_growth_5d"""
    return (_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(5)

def fgrd_002_debt_funded_growth_21d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_002_debt_funded_growth_21d"""
    return (_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(21)

def fgrd_003_debt_funded_growth_63d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_003_debt_funded_growth_63d"""
    return (_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(63)

def fgrd_004_debt_funded_growth_126d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_004_debt_funded_growth_126d"""
    return (_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(126)

def fgrd_005_debt_funded_growth_252d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_005_debt_funded_growth_252d"""
    return (_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(252)

def fgrd_006_liab_funded_growth_5d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_006_liab_funded_growth_5d"""
    return (_safe_div(revenue.diff(252), liabs.diff(252))).shift(5)

def fgrd_007_liab_funded_growth_21d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_007_liab_funded_growth_21d"""
    return (_safe_div(revenue.diff(252), liabs.diff(252))).shift(21)

def fgrd_008_liab_funded_growth_63d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_008_liab_funded_growth_63d"""
    return (_safe_div(revenue.diff(252), liabs.diff(252))).shift(63)

def fgrd_009_liab_funded_growth_126d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_009_liab_funded_growth_126d"""
    return (_safe_div(revenue.diff(252), liabs.diff(252))).shift(126)

def fgrd_010_liab_funded_growth_252d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_010_liab_funded_growth_252d"""
    return (_safe_div(revenue.diff(252), liabs.diff(252))).shift(252)

def fgrd_011_equity_funded_growth_5d(revenue: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_011_equity_funded_growth_5d"""
    return (_safe_div(revenue.diff(252), equity.diff(252))).shift(5)

def fgrd_012_equity_funded_growth_21d(revenue: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_012_equity_funded_growth_21d"""
    return (_safe_div(revenue.diff(252), equity.diff(252))).shift(21)

def fgrd_013_equity_funded_growth_63d(revenue: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_013_equity_funded_growth_63d"""
    return (_safe_div(revenue.diff(252), equity.diff(252))).shift(63)

def fgrd_014_equity_funded_growth_126d(revenue: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_014_equity_funded_growth_126d"""
    return (_safe_div(revenue.diff(252), equity.diff(252))).shift(126)

def fgrd_015_equity_funded_growth_252d(revenue: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_015_equity_funded_growth_252d"""
    return (_safe_div(revenue.diff(252), equity.diff(252))).shift(252)

def fgrd_016_debt_rev_rat_5d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_016_debt_rev_rat_5d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), revenue)).shift(5)

def fgrd_017_debt_rev_rat_21d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_017_debt_rev_rat_21d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), revenue)).shift(21)

def fgrd_018_debt_rev_rat_63d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_018_debt_rev_rat_63d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), revenue)).shift(63)

def fgrd_019_debt_rev_rat_126d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_019_debt_rev_rat_126d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), revenue)).shift(126)

def fgrd_020_debt_rev_rat_252d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_020_debt_rev_rat_252d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), revenue)).shift(252)

def fgrd_021_liab_rev_rat_5d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_021_liab_rev_rat_5d"""
    return (_safe_div(liabs, revenue)).shift(5)

def fgrd_022_liab_rev_rat_21d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_022_liab_rev_rat_21d"""
    return (_safe_div(liabs, revenue)).shift(21)

def fgrd_023_liab_rev_rat_63d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_023_liab_rev_rat_63d"""
    return (_safe_div(liabs, revenue)).shift(63)

def fgrd_024_liab_rev_rat_126d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_024_liab_rev_rat_126d"""
    return (_safe_div(liabs, revenue)).shift(126)

def fgrd_025_liab_rev_rat_252d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_025_liab_rev_rat_252d"""
    return (_safe_div(liabs, revenue)).shift(252)

def fgrd_026_debt_g_5d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_026_debt_g_5d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252)).shift(5)

def fgrd_027_debt_g_21d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_027_debt_g_21d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252)).shift(21)

def fgrd_028_debt_g_63d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_028_debt_g_63d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252)).shift(63)

def fgrd_029_debt_g_126d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_029_debt_g_126d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252)).shift(126)

def fgrd_030_debt_g_252d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_030_debt_g_252d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252)).shift(252)

def fgrd_031_rev_g_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_031_rev_g_5d"""
    return (revenue.pct_change(252)).shift(5)

def fgrd_032_rev_g_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_032_rev_g_21d"""
    return (revenue.pct_change(252)).shift(21)

def fgrd_033_rev_g_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_033_rev_g_63d"""
    return (revenue.pct_change(252)).shift(63)

def fgrd_034_rev_g_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_034_rev_g_126d"""
    return (revenue.pct_change(252)).shift(126)

def fgrd_035_rev_g_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_035_rev_g_252d"""
    return (revenue.pct_change(252)).shift(252)

def fgrd_036_growth_quality_5d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_036_growth_quality_5d"""
    return (_safe_div(revenue.pct_change(252), (debtn.fillna(0) + debtc.fillna(0)).pct_change(252))).shift(5)

def fgrd_037_growth_quality_21d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_037_growth_quality_21d"""
    return (_safe_div(revenue.pct_change(252), (debtn.fillna(0) + debtc.fillna(0)).pct_change(252))).shift(21)

def fgrd_038_growth_quality_63d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_038_growth_quality_63d"""
    return (_safe_div(revenue.pct_change(252), (debtn.fillna(0) + debtc.fillna(0)).pct_change(252))).shift(63)

def fgrd_039_growth_quality_126d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_039_growth_quality_126d"""
    return (_safe_div(revenue.pct_change(252), (debtn.fillna(0) + debtc.fillna(0)).pct_change(252))).shift(126)

def fgrd_040_growth_quality_252d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_040_growth_quality_252d"""
    return (_safe_div(revenue.pct_change(252), (debtn.fillna(0) + debtc.fillna(0)).pct_change(252))).shift(252)

def fgrd_041_fake_growth_index_5d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_041_fake_growth_index_5d"""
    return (revenue.pct_change(252) - ocf.pct_change(252)).shift(5)

def fgrd_042_fake_growth_index_21d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_042_fake_growth_index_21d"""
    return (revenue.pct_change(252) - ocf.pct_change(252)).shift(21)

def fgrd_043_fake_growth_index_63d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_043_fake_growth_index_63d"""
    return (revenue.pct_change(252) - ocf.pct_change(252)).shift(63)

def fgrd_044_fake_growth_index_126d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_044_fake_growth_index_126d"""
    return (revenue.pct_change(252) - ocf.pct_change(252)).shift(126)

def fgrd_045_fake_growth_index_252d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_045_fake_growth_index_252d"""
    return (revenue.pct_change(252) - ocf.pct_change(252)).shift(252)

def fgrd_046_acquisition_growth_proxy_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_046_acquisition_growth_proxy_5d"""
    return (assets.pct_change(252) - revenue.pct_change(252)).shift(5)

def fgrd_047_acquisition_growth_proxy_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_047_acquisition_growth_proxy_21d"""
    return (assets.pct_change(252) - revenue.pct_change(252)).shift(21)

def fgrd_048_acquisition_growth_proxy_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_048_acquisition_growth_proxy_63d"""
    return (assets.pct_change(252) - revenue.pct_change(252)).shift(63)

def fgrd_049_acquisition_growth_proxy_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_049_acquisition_growth_proxy_126d"""
    return (assets.pct_change(252) - revenue.pct_change(252)).shift(126)

def fgrd_050_acquisition_growth_proxy_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_050_acquisition_growth_proxy_252d"""
    return (assets.pct_change(252) - revenue.pct_change(252)).shift(252)

def fgrd_051_dilution_growth_proxy_5d(shareswa: pd.Series) -> pd.Series:
    """fgrd_051_dilution_growth_proxy_5d"""
    return (shareswa.pct_change(252)).shift(5)

def fgrd_052_dilution_growth_proxy_21d(shareswa: pd.Series) -> pd.Series:
    """fgrd_052_dilution_growth_proxy_21d"""
    return (shareswa.pct_change(252)).shift(21)

def fgrd_053_dilution_growth_proxy_63d(shareswa: pd.Series) -> pd.Series:
    """fgrd_053_dilution_growth_proxy_63d"""
    return (shareswa.pct_change(252)).shift(63)

def fgrd_054_dilution_growth_proxy_126d(shareswa: pd.Series) -> pd.Series:
    """fgrd_054_dilution_growth_proxy_126d"""
    return (shareswa.pct_change(252)).shift(126)

def fgrd_055_dilution_growth_proxy_252d(shareswa: pd.Series) -> pd.Series:
    """fgrd_055_dilution_growth_proxy_252d"""
    return (shareswa.pct_change(252)).shift(252)

def fgrd_056_capex_debt_rat_5d(capex: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_056_capex_debt_rat_5d"""
    return (_safe_div(capex, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(5)

def fgrd_057_capex_debt_rat_21d(capex: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_057_capex_debt_rat_21d"""
    return (_safe_div(capex, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(21)

def fgrd_058_capex_debt_rat_63d(capex: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_058_capex_debt_rat_63d"""
    return (_safe_div(capex, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(63)

def fgrd_059_capex_debt_rat_126d(capex: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_059_capex_debt_rat_126d"""
    return (_safe_div(capex, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(126)

def fgrd_060_capex_debt_rat_252d(capex: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_060_capex_debt_rat_252d"""
    return (_safe_div(capex, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(252)

def fgrd_061_interest_burden_5d(revenue: pd.Series, int_exp: pd.Series) -> pd.Series:
    """fgrd_061_interest_burden_5d"""
    return (_safe_div(int_exp, revenue)).shift(5)

def fgrd_062_interest_burden_21d(revenue: pd.Series, int_exp: pd.Series) -> pd.Series:
    """fgrd_062_interest_burden_21d"""
    return (_safe_div(int_exp, revenue)).shift(21)

def fgrd_063_interest_burden_63d(revenue: pd.Series, int_exp: pd.Series) -> pd.Series:
    """fgrd_063_interest_burden_63d"""
    return (_safe_div(int_exp, revenue)).shift(63)

def fgrd_064_interest_burden_126d(revenue: pd.Series, int_exp: pd.Series) -> pd.Series:
    """fgrd_064_interest_burden_126d"""
    return (_safe_div(int_exp, revenue)).shift(126)

def fgrd_065_interest_burden_252d(revenue: pd.Series, int_exp: pd.Series) -> pd.Series:
    """fgrd_065_interest_burden_252d"""
    return (_safe_div(int_exp, revenue)).shift(252)

def fgrd_066_leverage_velocity_5d(assets: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_066_leverage_velocity_5d"""
    return ((_safe_div(debtn.fillna(0) + debtc.fillna(0), assets)).diff(63)).shift(5)

def fgrd_067_leverage_velocity_21d(assets: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_067_leverage_velocity_21d"""
    return ((_safe_div(debtn.fillna(0) + debtc.fillna(0), assets)).diff(63)).shift(21)

def fgrd_068_leverage_velocity_63d(assets: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_068_leverage_velocity_63d"""
    return ((_safe_div(debtn.fillna(0) + debtc.fillna(0), assets)).diff(63)).shift(63)

def fgrd_069_leverage_velocity_126d(assets: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_069_leverage_velocity_126d"""
    return ((_safe_div(debtn.fillna(0) + debtc.fillna(0), assets)).diff(63)).shift(126)

def fgrd_070_leverage_velocity_252d(assets: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_070_leverage_velocity_252d"""
    return ((_safe_div(debtn.fillna(0) + debtc.fillna(0), assets)).diff(63)).shift(252)

def fgrd_071_growth_sustainability_5d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_071_growth_sustainability_5d"""
    return (_safe_div(ocf, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(5)

def fgrd_072_growth_sustainability_21d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_072_growth_sustainability_21d"""
    return (_safe_div(ocf, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(21)

def fgrd_073_growth_sustainability_63d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_073_growth_sustainability_63d"""
    return (_safe_div(ocf, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(63)

def fgrd_074_growth_sustainability_126d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_074_growth_sustainability_126d"""
    return (_safe_div(ocf, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(126)

def fgrd_075_growth_sustainability_252d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_075_growth_sustainability_252d"""
    return (_safe_div(ocf, (debtn.fillna(0) + debtc.fillna(0)).diff(252))).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V71_REGISTRY = {
    "fgrd_001_debt_funded_growth_5d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_001_debt_funded_growth_5d},
    "fgrd_002_debt_funded_growth_21d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_002_debt_funded_growth_21d},
    "fgrd_003_debt_funded_growth_63d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_003_debt_funded_growth_63d},
    "fgrd_004_debt_funded_growth_126d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_004_debt_funded_growth_126d},
    "fgrd_005_debt_funded_growth_252d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_005_debt_funded_growth_252d},
    "fgrd_006_liab_funded_growth_5d": {"inputs": ['revenue', 'liabs'], "func": fgrd_006_liab_funded_growth_5d},
    "fgrd_007_liab_funded_growth_21d": {"inputs": ['revenue', 'liabs'], "func": fgrd_007_liab_funded_growth_21d},
    "fgrd_008_liab_funded_growth_63d": {"inputs": ['revenue', 'liabs'], "func": fgrd_008_liab_funded_growth_63d},
    "fgrd_009_liab_funded_growth_126d": {"inputs": ['revenue', 'liabs'], "func": fgrd_009_liab_funded_growth_126d},
    "fgrd_010_liab_funded_growth_252d": {"inputs": ['revenue', 'liabs'], "func": fgrd_010_liab_funded_growth_252d},
    "fgrd_011_equity_funded_growth_5d": {"inputs": ['revenue', 'equity'], "func": fgrd_011_equity_funded_growth_5d},
    "fgrd_012_equity_funded_growth_21d": {"inputs": ['revenue', 'equity'], "func": fgrd_012_equity_funded_growth_21d},
    "fgrd_013_equity_funded_growth_63d": {"inputs": ['revenue', 'equity'], "func": fgrd_013_equity_funded_growth_63d},
    "fgrd_014_equity_funded_growth_126d": {"inputs": ['revenue', 'equity'], "func": fgrd_014_equity_funded_growth_126d},
    "fgrd_015_equity_funded_growth_252d": {"inputs": ['revenue', 'equity'], "func": fgrd_015_equity_funded_growth_252d},
    "fgrd_016_debt_rev_rat_5d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_016_debt_rev_rat_5d},
    "fgrd_017_debt_rev_rat_21d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_017_debt_rev_rat_21d},
    "fgrd_018_debt_rev_rat_63d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_018_debt_rev_rat_63d},
    "fgrd_019_debt_rev_rat_126d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_019_debt_rev_rat_126d},
    "fgrd_020_debt_rev_rat_252d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_020_debt_rev_rat_252d},
    "fgrd_021_liab_rev_rat_5d": {"inputs": ['revenue', 'liabs'], "func": fgrd_021_liab_rev_rat_5d},
    "fgrd_022_liab_rev_rat_21d": {"inputs": ['revenue', 'liabs'], "func": fgrd_022_liab_rev_rat_21d},
    "fgrd_023_liab_rev_rat_63d": {"inputs": ['revenue', 'liabs'], "func": fgrd_023_liab_rev_rat_63d},
    "fgrd_024_liab_rev_rat_126d": {"inputs": ['revenue', 'liabs'], "func": fgrd_024_liab_rev_rat_126d},
    "fgrd_025_liab_rev_rat_252d": {"inputs": ['revenue', 'liabs'], "func": fgrd_025_liab_rev_rat_252d},
    "fgrd_026_debt_g_5d": {"inputs": ['debtn', 'debtc'], "func": fgrd_026_debt_g_5d},
    "fgrd_027_debt_g_21d": {"inputs": ['debtn', 'debtc'], "func": fgrd_027_debt_g_21d},
    "fgrd_028_debt_g_63d": {"inputs": ['debtn', 'debtc'], "func": fgrd_028_debt_g_63d},
    "fgrd_029_debt_g_126d": {"inputs": ['debtn', 'debtc'], "func": fgrd_029_debt_g_126d},
    "fgrd_030_debt_g_252d": {"inputs": ['debtn', 'debtc'], "func": fgrd_030_debt_g_252d},
    "fgrd_031_rev_g_5d": {"inputs": ['revenue'], "func": fgrd_031_rev_g_5d},
    "fgrd_032_rev_g_21d": {"inputs": ['revenue'], "func": fgrd_032_rev_g_21d},
    "fgrd_033_rev_g_63d": {"inputs": ['revenue'], "func": fgrd_033_rev_g_63d},
    "fgrd_034_rev_g_126d": {"inputs": ['revenue'], "func": fgrd_034_rev_g_126d},
    "fgrd_035_rev_g_252d": {"inputs": ['revenue'], "func": fgrd_035_rev_g_252d},
    "fgrd_036_growth_quality_5d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_036_growth_quality_5d},
    "fgrd_037_growth_quality_21d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_037_growth_quality_21d},
    "fgrd_038_growth_quality_63d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_038_growth_quality_63d},
    "fgrd_039_growth_quality_126d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_039_growth_quality_126d},
    "fgrd_040_growth_quality_252d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_040_growth_quality_252d},
    "fgrd_041_fake_growth_index_5d": {"inputs": ['revenue', 'ocf'], "func": fgrd_041_fake_growth_index_5d},
    "fgrd_042_fake_growth_index_21d": {"inputs": ['revenue', 'ocf'], "func": fgrd_042_fake_growth_index_21d},
    "fgrd_043_fake_growth_index_63d": {"inputs": ['revenue', 'ocf'], "func": fgrd_043_fake_growth_index_63d},
    "fgrd_044_fake_growth_index_126d": {"inputs": ['revenue', 'ocf'], "func": fgrd_044_fake_growth_index_126d},
    "fgrd_045_fake_growth_index_252d": {"inputs": ['revenue', 'ocf'], "func": fgrd_045_fake_growth_index_252d},
    "fgrd_046_acquisition_growth_proxy_5d": {"inputs": ['revenue', 'assets'], "func": fgrd_046_acquisition_growth_proxy_5d},
    "fgrd_047_acquisition_growth_proxy_21d": {"inputs": ['revenue', 'assets'], "func": fgrd_047_acquisition_growth_proxy_21d},
    "fgrd_048_acquisition_growth_proxy_63d": {"inputs": ['revenue', 'assets'], "func": fgrd_048_acquisition_growth_proxy_63d},
    "fgrd_049_acquisition_growth_proxy_126d": {"inputs": ['revenue', 'assets'], "func": fgrd_049_acquisition_growth_proxy_126d},
    "fgrd_050_acquisition_growth_proxy_252d": {"inputs": ['revenue', 'assets'], "func": fgrd_050_acquisition_growth_proxy_252d},
    "fgrd_051_dilution_growth_proxy_5d": {"inputs": ['shareswa'], "func": fgrd_051_dilution_growth_proxy_5d},
    "fgrd_052_dilution_growth_proxy_21d": {"inputs": ['shareswa'], "func": fgrd_052_dilution_growth_proxy_21d},
    "fgrd_053_dilution_growth_proxy_63d": {"inputs": ['shareswa'], "func": fgrd_053_dilution_growth_proxy_63d},
    "fgrd_054_dilution_growth_proxy_126d": {"inputs": ['shareswa'], "func": fgrd_054_dilution_growth_proxy_126d},
    "fgrd_055_dilution_growth_proxy_252d": {"inputs": ['shareswa'], "func": fgrd_055_dilution_growth_proxy_252d},
    "fgrd_056_capex_debt_rat_5d": {"inputs": ['capex', 'debtn', 'debtc'], "func": fgrd_056_capex_debt_rat_5d},
    "fgrd_057_capex_debt_rat_21d": {"inputs": ['capex', 'debtn', 'debtc'], "func": fgrd_057_capex_debt_rat_21d},
    "fgrd_058_capex_debt_rat_63d": {"inputs": ['capex', 'debtn', 'debtc'], "func": fgrd_058_capex_debt_rat_63d},
    "fgrd_059_capex_debt_rat_126d": {"inputs": ['capex', 'debtn', 'debtc'], "func": fgrd_059_capex_debt_rat_126d},
    "fgrd_060_capex_debt_rat_252d": {"inputs": ['capex', 'debtn', 'debtc'], "func": fgrd_060_capex_debt_rat_252d},
    "fgrd_061_interest_burden_5d": {"inputs": ['revenue', 'int_exp'], "func": fgrd_061_interest_burden_5d},
    "fgrd_062_interest_burden_21d": {"inputs": ['revenue', 'int_exp'], "func": fgrd_062_interest_burden_21d},
    "fgrd_063_interest_burden_63d": {"inputs": ['revenue', 'int_exp'], "func": fgrd_063_interest_burden_63d},
    "fgrd_064_interest_burden_126d": {"inputs": ['revenue', 'int_exp'], "func": fgrd_064_interest_burden_126d},
    "fgrd_065_interest_burden_252d": {"inputs": ['revenue', 'int_exp'], "func": fgrd_065_interest_burden_252d},
    "fgrd_066_leverage_velocity_5d": {"inputs": ['assets', 'debtn', 'debtc'], "func": fgrd_066_leverage_velocity_5d},
    "fgrd_067_leverage_velocity_21d": {"inputs": ['assets', 'debtn', 'debtc'], "func": fgrd_067_leverage_velocity_21d},
    "fgrd_068_leverage_velocity_63d": {"inputs": ['assets', 'debtn', 'debtc'], "func": fgrd_068_leverage_velocity_63d},
    "fgrd_069_leverage_velocity_126d": {"inputs": ['assets', 'debtn', 'debtc'], "func": fgrd_069_leverage_velocity_126d},
    "fgrd_070_leverage_velocity_252d": {"inputs": ['assets', 'debtn', 'debtc'], "func": fgrd_070_leverage_velocity_252d},
    "fgrd_071_growth_sustainability_5d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_071_growth_sustainability_5d},
    "fgrd_072_growth_sustainability_21d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_072_growth_sustainability_21d},
    "fgrd_073_growth_sustainability_63d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_073_growth_sustainability_63d},
    "fgrd_074_growth_sustainability_126d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_074_growth_sustainability_126d},
    "fgrd_075_growth_sustainability_252d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_075_growth_sustainability_252d},
}
