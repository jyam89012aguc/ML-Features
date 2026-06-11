"""
61_hypergrowth_signature — Base Features 001-075
Domain: High RevG + High Multiples persistence
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

def hygr_001_rev_g_5d(revenue: pd.Series) -> pd.Series:
    """hygr_001_rev_g_5d"""
    return (revenue.pct_change(252)).shift(5)

def hygr_002_rev_g_21d(revenue: pd.Series) -> pd.Series:
    """hygr_002_rev_g_21d"""
    return (revenue.pct_change(252)).shift(21)

def hygr_003_rev_g_63d(revenue: pd.Series) -> pd.Series:
    """hygr_003_rev_g_63d"""
    return (revenue.pct_change(252)).shift(63)

def hygr_004_rev_g_126d(revenue: pd.Series) -> pd.Series:
    """hygr_004_rev_g_126d"""
    return (revenue.pct_change(252)).shift(126)

def hygr_005_rev_g_252d(revenue: pd.Series) -> pd.Series:
    """hygr_005_rev_g_252d"""
    return (revenue.pct_change(252)).shift(252)

def hygr_006_rule40_eb_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_006_rule40_eb_5d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252))).shift(5)

def hygr_007_rule40_eb_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_007_rule40_eb_21d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252))).shift(21)

def hygr_008_rule40_eb_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_008_rule40_eb_63d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252))).shift(63)

def hygr_009_rule40_eb_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_009_rule40_eb_126d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252))).shift(126)

def hygr_010_rule40_eb_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_010_rule40_eb_252d"""
    return ((_safe_div(ebitda, revenue) + revenue.pct_change(252))).shift(252)

def hygr_011_rule40_fcf_5d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_011_rule40_fcf_5d"""
    return ((_safe_div(fcf, revenue) + revenue.pct_change(252))).shift(5)

def hygr_012_rule40_fcf_21d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_012_rule40_fcf_21d"""
    return ((_safe_div(fcf, revenue) + revenue.pct_change(252))).shift(21)

def hygr_013_rule40_fcf_63d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_013_rule40_fcf_63d"""
    return ((_safe_div(fcf, revenue) + revenue.pct_change(252))).shift(63)

def hygr_014_rule40_fcf_126d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_014_rule40_fcf_126d"""
    return ((_safe_div(fcf, revenue) + revenue.pct_change(252))).shift(126)

def hygr_015_rule40_fcf_252d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_015_rule40_fcf_252d"""
    return ((_safe_div(fcf, revenue) + revenue.pct_change(252))).shift(252)

def hygr_016_ps_rat_5d(ps: pd.Series) -> pd.Series:
    """hygr_016_ps_rat_5d"""
    return (ps).shift(5)

def hygr_017_ps_rat_21d(ps: pd.Series) -> pd.Series:
    """hygr_017_ps_rat_21d"""
    return (ps).shift(21)

def hygr_018_ps_rat_63d(ps: pd.Series) -> pd.Series:
    """hygr_018_ps_rat_63d"""
    return (ps).shift(63)

def hygr_019_ps_rat_126d(ps: pd.Series) -> pd.Series:
    """hygr_019_ps_rat_126d"""
    return (ps).shift(126)

def hygr_020_ps_rat_252d(ps: pd.Series) -> pd.Series:
    """hygr_020_ps_rat_252d"""
    return (ps).shift(252)

def hygr_021_ev_rev_5d(revenue: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_021_ev_rev_5d"""
    return (_safe_div(marketcap + debtn.fillna(0) + debtc.fillna(0) - cashnequiv.fillna(0), revenue)).shift(5)

def hygr_022_ev_rev_21d(revenue: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_022_ev_rev_21d"""
    return (_safe_div(marketcap + debtn.fillna(0) + debtc.fillna(0) - cashnequiv.fillna(0), revenue)).shift(21)

def hygr_023_ev_rev_63d(revenue: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_023_ev_rev_63d"""
    return (_safe_div(marketcap + debtn.fillna(0) + debtc.fillna(0) - cashnequiv.fillna(0), revenue)).shift(63)

def hygr_024_ev_rev_126d(revenue: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_024_ev_rev_126d"""
    return (_safe_div(marketcap + debtn.fillna(0) + debtc.fillna(0) - cashnequiv.fillna(0), revenue)).shift(126)

def hygr_025_ev_rev_252d(revenue: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_025_ev_rev_252d"""
    return (_safe_div(marketcap + debtn.fillna(0) + debtc.fillna(0) - cashnequiv.fillna(0), revenue)).shift(252)

def hygr_026_rev_rps_5d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_026_rev_rps_5d"""
    return (_safe_div(revenue, shareswa)).shift(5)

def hygr_027_rev_rps_21d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_027_rev_rps_21d"""
    return (_safe_div(revenue, shareswa)).shift(21)

def hygr_028_rev_rps_63d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_028_rev_rps_63d"""
    return (_safe_div(revenue, shareswa)).shift(63)

def hygr_029_rev_rps_126d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_029_rev_rps_126d"""
    return (_safe_div(revenue, shareswa)).shift(126)

def hygr_030_rev_rps_252d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_030_rev_rps_252d"""
    return (_safe_div(revenue, shareswa)).shift(252)

def hygr_031_gp_g_5d(gp: pd.Series) -> pd.Series:
    """hygr_031_gp_g_5d"""
    return (gp.pct_change(252)).shift(5)

def hygr_032_gp_g_21d(gp: pd.Series) -> pd.Series:
    """hygr_032_gp_g_21d"""
    return (gp.pct_change(252)).shift(21)

def hygr_033_gp_g_63d(gp: pd.Series) -> pd.Series:
    """hygr_033_gp_g_63d"""
    return (gp.pct_change(252)).shift(63)

def hygr_034_gp_g_126d(gp: pd.Series) -> pd.Series:
    """hygr_034_gp_g_126d"""
    return (gp.pct_change(252)).shift(126)

def hygr_035_gp_g_252d(gp: pd.Series) -> pd.Series:
    """hygr_035_gp_g_252d"""
    return (gp.pct_change(252)).shift(252)

def hygr_036_ebitda_g_5d(ebitda: pd.Series) -> pd.Series:
    """hygr_036_ebitda_g_5d"""
    return (ebitda.pct_change(252)).shift(5)

def hygr_037_ebitda_g_21d(ebitda: pd.Series) -> pd.Series:
    """hygr_037_ebitda_g_21d"""
    return (ebitda.pct_change(252)).shift(21)

def hygr_038_ebitda_g_63d(ebitda: pd.Series) -> pd.Series:
    """hygr_038_ebitda_g_63d"""
    return (ebitda.pct_change(252)).shift(63)

def hygr_039_ebitda_g_126d(ebitda: pd.Series) -> pd.Series:
    """hygr_039_ebitda_g_126d"""
    return (ebitda.pct_change(252)).shift(126)

def hygr_040_ebitda_g_252d(ebitda: pd.Series) -> pd.Series:
    """hygr_040_ebitda_g_252d"""
    return (ebitda.pct_change(252)).shift(252)

def hygr_041_rd_rev_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """hygr_041_rd_rev_5d"""
    return (_safe_div(rnd, revenue)).shift(5)

def hygr_042_rd_rev_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """hygr_042_rd_rev_21d"""
    return (_safe_div(rnd, revenue)).shift(21)

def hygr_043_rd_rev_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """hygr_043_rd_rev_63d"""
    return (_safe_div(rnd, revenue)).shift(63)

def hygr_044_rd_rev_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """hygr_044_rd_rev_126d"""
    return (_safe_div(rnd, revenue)).shift(126)

def hygr_045_rd_rev_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """hygr_045_rd_rev_252d"""
    return (_safe_div(rnd, revenue)).shift(252)

def hygr_046_sga_rev_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """hygr_046_sga_rev_5d"""
    return (_safe_div(sga, revenue)).shift(5)

def hygr_047_sga_rev_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """hygr_047_sga_rev_21d"""
    return (_safe_div(sga, revenue)).shift(21)

def hygr_048_sga_rev_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """hygr_048_sga_rev_63d"""
    return (_safe_div(sga, revenue)).shift(63)

def hygr_049_sga_rev_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """hygr_049_sga_rev_126d"""
    return (_safe_div(sga, revenue)).shift(126)

def hygr_050_sga_rev_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """hygr_050_sga_rev_252d"""
    return (_safe_div(sga, revenue)).shift(252)

def hygr_051_mc_rev_5d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_051_mc_rev_5d"""
    return (_safe_div(marketcap, revenue)).shift(5)

def hygr_052_mc_rev_21d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_052_mc_rev_21d"""
    return (_safe_div(marketcap, revenue)).shift(21)

def hygr_053_mc_rev_63d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_053_mc_rev_63d"""
    return (_safe_div(marketcap, revenue)).shift(63)

def hygr_054_mc_rev_126d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_054_mc_rev_126d"""
    return (_safe_div(marketcap, revenue)).shift(126)

def hygr_055_mc_rev_252d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_055_mc_rev_252d"""
    return (_safe_div(marketcap, revenue)).shift(252)

def hygr_056_pe_rat_5d(pe: pd.Series) -> pd.Series:
    """hygr_056_pe_rat_5d"""
    return (pe).shift(5)

def hygr_057_pe_rat_21d(pe: pd.Series) -> pd.Series:
    """hygr_057_pe_rat_21d"""
    return (pe).shift(21)

def hygr_058_pe_rat_63d(pe: pd.Series) -> pd.Series:
    """hygr_058_pe_rat_63d"""
    return (pe).shift(63)

def hygr_059_pe_rat_126d(pe: pd.Series) -> pd.Series:
    """hygr_059_pe_rat_126d"""
    return (pe).shift(126)

def hygr_060_pe_rat_252d(pe: pd.Series) -> pd.Series:
    """hygr_060_pe_rat_252d"""
    return (pe).shift(252)

def hygr_061_fcf_yield_5d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_061_fcf_yield_5d"""
    return (_safe_div(fcf, marketcap)).shift(5)

def hygr_062_fcf_yield_21d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_062_fcf_yield_21d"""
    return (_safe_div(fcf, marketcap)).shift(21)

def hygr_063_fcf_yield_63d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_063_fcf_yield_63d"""
    return (_safe_div(fcf, marketcap)).shift(63)

def hygr_064_fcf_yield_126d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_064_fcf_yield_126d"""
    return (_safe_div(fcf, marketcap)).shift(126)

def hygr_065_fcf_yield_252d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_065_fcf_yield_252d"""
    return (_safe_div(fcf, marketcap)).shift(252)

def hygr_066_ebitda_yield_5d(ebitda: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_066_ebitda_yield_5d"""
    return (_safe_div(ebitda, marketcap)).shift(5)

def hygr_067_ebitda_yield_21d(ebitda: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_067_ebitda_yield_21d"""
    return (_safe_div(ebitda, marketcap)).shift(21)

def hygr_068_ebitda_yield_63d(ebitda: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_068_ebitda_yield_63d"""
    return (_safe_div(ebitda, marketcap)).shift(63)

def hygr_069_ebitda_yield_126d(ebitda: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_069_ebitda_yield_126d"""
    return (_safe_div(ebitda, marketcap)).shift(126)

def hygr_070_ebitda_yield_252d(ebitda: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_070_ebitda_yield_252d"""
    return (_safe_div(ebitda, marketcap)).shift(252)

def hygr_071_rev_z_5d(revenue: pd.Series) -> pd.Series:
    """hygr_071_rev_z_5d"""
    return (_zscore_rolling(revenue, 1260)).shift(5)

def hygr_072_rev_z_21d(revenue: pd.Series) -> pd.Series:
    """hygr_072_rev_z_21d"""
    return (_zscore_rolling(revenue, 1260)).shift(21)

def hygr_073_rev_z_63d(revenue: pd.Series) -> pd.Series:
    """hygr_073_rev_z_63d"""
    return (_zscore_rolling(revenue, 1260)).shift(63)

def hygr_074_rev_z_126d(revenue: pd.Series) -> pd.Series:
    """hygr_074_rev_z_126d"""
    return (_zscore_rolling(revenue, 1260)).shift(126)

def hygr_075_rev_z_252d(revenue: pd.Series) -> pd.Series:
    """hygr_075_rev_z_252d"""
    return (_zscore_rolling(revenue, 1260)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V61_REGISTRY = {
    "hygr_001_rev_g_5d": {"inputs": ['revenue'], "func": hygr_001_rev_g_5d},
    "hygr_002_rev_g_21d": {"inputs": ['revenue'], "func": hygr_002_rev_g_21d},
    "hygr_003_rev_g_63d": {"inputs": ['revenue'], "func": hygr_003_rev_g_63d},
    "hygr_004_rev_g_126d": {"inputs": ['revenue'], "func": hygr_004_rev_g_126d},
    "hygr_005_rev_g_252d": {"inputs": ['revenue'], "func": hygr_005_rev_g_252d},
    "hygr_006_rule40_eb_5d": {"inputs": ['revenue', 'ebitda'], "func": hygr_006_rule40_eb_5d},
    "hygr_007_rule40_eb_21d": {"inputs": ['revenue', 'ebitda'], "func": hygr_007_rule40_eb_21d},
    "hygr_008_rule40_eb_63d": {"inputs": ['revenue', 'ebitda'], "func": hygr_008_rule40_eb_63d},
    "hygr_009_rule40_eb_126d": {"inputs": ['revenue', 'ebitda'], "func": hygr_009_rule40_eb_126d},
    "hygr_010_rule40_eb_252d": {"inputs": ['revenue', 'ebitda'], "func": hygr_010_rule40_eb_252d},
    "hygr_011_rule40_fcf_5d": {"inputs": ['revenue', 'fcf'], "func": hygr_011_rule40_fcf_5d},
    "hygr_012_rule40_fcf_21d": {"inputs": ['revenue', 'fcf'], "func": hygr_012_rule40_fcf_21d},
    "hygr_013_rule40_fcf_63d": {"inputs": ['revenue', 'fcf'], "func": hygr_013_rule40_fcf_63d},
    "hygr_014_rule40_fcf_126d": {"inputs": ['revenue', 'fcf'], "func": hygr_014_rule40_fcf_126d},
    "hygr_015_rule40_fcf_252d": {"inputs": ['revenue', 'fcf'], "func": hygr_015_rule40_fcf_252d},
    "hygr_016_ps_rat_5d": {"inputs": ['ps'], "func": hygr_016_ps_rat_5d},
    "hygr_017_ps_rat_21d": {"inputs": ['ps'], "func": hygr_017_ps_rat_21d},
    "hygr_018_ps_rat_63d": {"inputs": ['ps'], "func": hygr_018_ps_rat_63d},
    "hygr_019_ps_rat_126d": {"inputs": ['ps'], "func": hygr_019_ps_rat_126d},
    "hygr_020_ps_rat_252d": {"inputs": ['ps'], "func": hygr_020_ps_rat_252d},
    "hygr_021_ev_rev_5d": {"inputs": ['revenue', 'cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": hygr_021_ev_rev_5d},
    "hygr_022_ev_rev_21d": {"inputs": ['revenue', 'cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": hygr_022_ev_rev_21d},
    "hygr_023_ev_rev_63d": {"inputs": ['revenue', 'cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": hygr_023_ev_rev_63d},
    "hygr_024_ev_rev_126d": {"inputs": ['revenue', 'cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": hygr_024_ev_rev_126d},
    "hygr_025_ev_rev_252d": {"inputs": ['revenue', 'cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": hygr_025_ev_rev_252d},
    "hygr_026_rev_rps_5d": {"inputs": ['revenue', 'shareswa'], "func": hygr_026_rev_rps_5d},
    "hygr_027_rev_rps_21d": {"inputs": ['revenue', 'shareswa'], "func": hygr_027_rev_rps_21d},
    "hygr_028_rev_rps_63d": {"inputs": ['revenue', 'shareswa'], "func": hygr_028_rev_rps_63d},
    "hygr_029_rev_rps_126d": {"inputs": ['revenue', 'shareswa'], "func": hygr_029_rev_rps_126d},
    "hygr_030_rev_rps_252d": {"inputs": ['revenue', 'shareswa'], "func": hygr_030_rev_rps_252d},
    "hygr_031_gp_g_5d": {"inputs": ['gp'], "func": hygr_031_gp_g_5d},
    "hygr_032_gp_g_21d": {"inputs": ['gp'], "func": hygr_032_gp_g_21d},
    "hygr_033_gp_g_63d": {"inputs": ['gp'], "func": hygr_033_gp_g_63d},
    "hygr_034_gp_g_126d": {"inputs": ['gp'], "func": hygr_034_gp_g_126d},
    "hygr_035_gp_g_252d": {"inputs": ['gp'], "func": hygr_035_gp_g_252d},
    "hygr_036_ebitda_g_5d": {"inputs": ['ebitda'], "func": hygr_036_ebitda_g_5d},
    "hygr_037_ebitda_g_21d": {"inputs": ['ebitda'], "func": hygr_037_ebitda_g_21d},
    "hygr_038_ebitda_g_63d": {"inputs": ['ebitda'], "func": hygr_038_ebitda_g_63d},
    "hygr_039_ebitda_g_126d": {"inputs": ['ebitda'], "func": hygr_039_ebitda_g_126d},
    "hygr_040_ebitda_g_252d": {"inputs": ['ebitda'], "func": hygr_040_ebitda_g_252d},
    "hygr_041_rd_rev_5d": {"inputs": ['revenue', 'rnd'], "func": hygr_041_rd_rev_5d},
    "hygr_042_rd_rev_21d": {"inputs": ['revenue', 'rnd'], "func": hygr_042_rd_rev_21d},
    "hygr_043_rd_rev_63d": {"inputs": ['revenue', 'rnd'], "func": hygr_043_rd_rev_63d},
    "hygr_044_rd_rev_126d": {"inputs": ['revenue', 'rnd'], "func": hygr_044_rd_rev_126d},
    "hygr_045_rd_rev_252d": {"inputs": ['revenue', 'rnd'], "func": hygr_045_rd_rev_252d},
    "hygr_046_sga_rev_5d": {"inputs": ['revenue', 'sga'], "func": hygr_046_sga_rev_5d},
    "hygr_047_sga_rev_21d": {"inputs": ['revenue', 'sga'], "func": hygr_047_sga_rev_21d},
    "hygr_048_sga_rev_63d": {"inputs": ['revenue', 'sga'], "func": hygr_048_sga_rev_63d},
    "hygr_049_sga_rev_126d": {"inputs": ['revenue', 'sga'], "func": hygr_049_sga_rev_126d},
    "hygr_050_sga_rev_252d": {"inputs": ['revenue', 'sga'], "func": hygr_050_sga_rev_252d},
    "hygr_051_mc_rev_5d": {"inputs": ['revenue', 'marketcap'], "func": hygr_051_mc_rev_5d},
    "hygr_052_mc_rev_21d": {"inputs": ['revenue', 'marketcap'], "func": hygr_052_mc_rev_21d},
    "hygr_053_mc_rev_63d": {"inputs": ['revenue', 'marketcap'], "func": hygr_053_mc_rev_63d},
    "hygr_054_mc_rev_126d": {"inputs": ['revenue', 'marketcap'], "func": hygr_054_mc_rev_126d},
    "hygr_055_mc_rev_252d": {"inputs": ['revenue', 'marketcap'], "func": hygr_055_mc_rev_252d},
    "hygr_056_pe_rat_5d": {"inputs": ['pe'], "func": hygr_056_pe_rat_5d},
    "hygr_057_pe_rat_21d": {"inputs": ['pe'], "func": hygr_057_pe_rat_21d},
    "hygr_058_pe_rat_63d": {"inputs": ['pe'], "func": hygr_058_pe_rat_63d},
    "hygr_059_pe_rat_126d": {"inputs": ['pe'], "func": hygr_059_pe_rat_126d},
    "hygr_060_pe_rat_252d": {"inputs": ['pe'], "func": hygr_060_pe_rat_252d},
    "hygr_061_fcf_yield_5d": {"inputs": ['fcf', 'marketcap'], "func": hygr_061_fcf_yield_5d},
    "hygr_062_fcf_yield_21d": {"inputs": ['fcf', 'marketcap'], "func": hygr_062_fcf_yield_21d},
    "hygr_063_fcf_yield_63d": {"inputs": ['fcf', 'marketcap'], "func": hygr_063_fcf_yield_63d},
    "hygr_064_fcf_yield_126d": {"inputs": ['fcf', 'marketcap'], "func": hygr_064_fcf_yield_126d},
    "hygr_065_fcf_yield_252d": {"inputs": ['fcf', 'marketcap'], "func": hygr_065_fcf_yield_252d},
    "hygr_066_ebitda_yield_5d": {"inputs": ['ebitda', 'marketcap'], "func": hygr_066_ebitda_yield_5d},
    "hygr_067_ebitda_yield_21d": {"inputs": ['ebitda', 'marketcap'], "func": hygr_067_ebitda_yield_21d},
    "hygr_068_ebitda_yield_63d": {"inputs": ['ebitda', 'marketcap'], "func": hygr_068_ebitda_yield_63d},
    "hygr_069_ebitda_yield_126d": {"inputs": ['ebitda', 'marketcap'], "func": hygr_069_ebitda_yield_126d},
    "hygr_070_ebitda_yield_252d": {"inputs": ['ebitda', 'marketcap'], "func": hygr_070_ebitda_yield_252d},
    "hygr_071_rev_z_5d": {"inputs": ['revenue'], "func": hygr_071_rev_z_5d},
    "hygr_072_rev_z_21d": {"inputs": ['revenue'], "func": hygr_072_rev_z_21d},
    "hygr_073_rev_z_63d": {"inputs": ['revenue'], "func": hygr_073_rev_z_63d},
    "hygr_074_rev_z_126d": {"inputs": ['revenue'], "func": hygr_074_rev_z_126d},
    "hygr_075_rev_z_252d": {"inputs": ['revenue'], "func": hygr_075_rev_z_252d},
}
