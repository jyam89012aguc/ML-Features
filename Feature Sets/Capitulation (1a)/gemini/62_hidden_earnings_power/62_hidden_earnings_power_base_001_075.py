"""
62_hidden_earnings_power — Base Features 001-075
Domain: OpInc vs NetInc divergence, tax rate anomalies
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

def herp_001_op_ni_div_5d(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_001_op_ni_div_5d"""
    return (_safe_div(ebit, netinc)).shift(5)

def herp_002_op_ni_div_21d(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_002_op_ni_div_21d"""
    return (_safe_div(ebit, netinc)).shift(21)

def herp_003_op_ni_div_63d(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_003_op_ni_div_63d"""
    return (_safe_div(ebit, netinc)).shift(63)

def herp_004_op_ni_div_126d(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_004_op_ni_div_126d"""
    return (_safe_div(ebit, netinc)).shift(126)

def herp_005_op_ni_div_252d(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_005_op_ni_div_252d"""
    return (_safe_div(ebit, netinc)).shift(252)

def herp_006_tax_rat_5d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_006_tax_rat_5d"""
    return (_safe_div(taxexp, ebt)).shift(5)

def herp_007_tax_rat_21d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_007_tax_rat_21d"""
    return (_safe_div(taxexp, ebt)).shift(21)

def herp_008_tax_rat_63d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_008_tax_rat_63d"""
    return (_safe_div(taxexp, ebt)).shift(63)

def herp_009_tax_rat_126d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_009_tax_rat_126d"""
    return (_safe_div(taxexp, ebt)).shift(126)

def herp_010_tax_rat_252d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_010_tax_rat_252d"""
    return (_safe_div(taxexp, ebt)).shift(252)

def herp_011_non_op_rat_5d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_011_non_op_rat_5d"""
    return (_safe_div(netinc - ebit, revenue)).shift(5)

def herp_012_non_op_rat_21d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_012_non_op_rat_21d"""
    return (_safe_div(netinc - ebit, revenue)).shift(21)

def herp_013_non_op_rat_63d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_013_non_op_rat_63d"""
    return (_safe_div(netinc - ebit, revenue)).shift(63)

def herp_014_non_op_rat_126d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_014_non_op_rat_126d"""
    return (_safe_div(netinc - ebit, revenue)).shift(126)

def herp_015_non_op_rat_252d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_015_non_op_rat_252d"""
    return (_safe_div(netinc - ebit, revenue)).shift(252)

def herp_016_ebitda_ni_div_5d(ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_016_ebitda_ni_div_5d"""
    return (_safe_div(ebitda, netinc)).shift(5)

def herp_017_ebitda_ni_div_21d(ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_017_ebitda_ni_div_21d"""
    return (_safe_div(ebitda, netinc)).shift(21)

def herp_018_ebitda_ni_div_63d(ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_018_ebitda_ni_div_63d"""
    return (_safe_div(ebitda, netinc)).shift(63)

def herp_019_ebitda_ni_div_126d(ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_019_ebitda_ni_div_126d"""
    return (_safe_div(ebitda, netinc)).shift(126)

def herp_020_ebitda_ni_div_252d(ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_020_ebitda_ni_div_252d"""
    return (_safe_div(ebitda, netinc)).shift(252)

def herp_021_rnd_cap_proxy_5d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_021_rnd_cap_proxy_5d"""
    return (_safe_div(rnd, assets)).shift(5)

def herp_022_rnd_cap_proxy_21d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_022_rnd_cap_proxy_21d"""
    return (_safe_div(rnd, assets)).shift(21)

def herp_023_rnd_cap_proxy_63d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_023_rnd_cap_proxy_63d"""
    return (_safe_div(rnd, assets)).shift(63)

def herp_024_rnd_cap_proxy_126d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_024_rnd_cap_proxy_126d"""
    return (_safe_div(rnd, assets)).shift(126)

def herp_025_rnd_cap_proxy_252d(rnd: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_025_rnd_cap_proxy_252d"""
    return (_safe_div(rnd, assets)).shift(252)

def herp_026_sga_eff_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_026_sga_eff_5d"""
    return (_safe_div(revenue, sga)).shift(5)

def herp_027_sga_eff_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_027_sga_eff_21d"""
    return (_safe_div(revenue, sga)).shift(21)

def herp_028_sga_eff_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_028_sga_eff_63d"""
    return (_safe_div(revenue, sga)).shift(63)

def herp_029_sga_eff_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_029_sga_eff_126d"""
    return (_safe_div(revenue, sga)).shift(126)

def herp_030_sga_eff_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """herp_030_sga_eff_252d"""
    return (_safe_div(revenue, sga)).shift(252)

def herp_031_dep_cap_rat_5d(capex: pd.Series) -> pd.Series:
    """herp_031_dep_cap_rat_5d"""
    return (_safe_div(depamor, capex)).shift(5)

def herp_032_dep_cap_rat_21d(capex: pd.Series) -> pd.Series:
    """herp_032_dep_cap_rat_21d"""
    return (_safe_div(depamor, capex)).shift(21)

def herp_033_dep_cap_rat_63d(capex: pd.Series) -> pd.Series:
    """herp_033_dep_cap_rat_63d"""
    return (_safe_div(depamor, capex)).shift(63)

def herp_034_dep_cap_rat_126d(capex: pd.Series) -> pd.Series:
    """herp_034_dep_cap_rat_126d"""
    return (_safe_div(depamor, capex)).shift(126)

def herp_035_dep_cap_rat_252d(capex: pd.Series) -> pd.Series:
    """herp_035_dep_cap_rat_252d"""
    return (_safe_div(depamor, capex)).shift(252)

def herp_036_interest_cov_5d(ebit: pd.Series, int_exp: pd.Series) -> pd.Series:
    """herp_036_interest_cov_5d"""
    return (_safe_div(ebit, int_exp)).shift(5)

def herp_037_interest_cov_21d(ebit: pd.Series, int_exp: pd.Series) -> pd.Series:
    """herp_037_interest_cov_21d"""
    return (_safe_div(ebit, int_exp)).shift(21)

def herp_038_interest_cov_63d(ebit: pd.Series, int_exp: pd.Series) -> pd.Series:
    """herp_038_interest_cov_63d"""
    return (_safe_div(ebit, int_exp)).shift(63)

def herp_039_interest_cov_126d(ebit: pd.Series, int_exp: pd.Series) -> pd.Series:
    """herp_039_interest_cov_126d"""
    return (_safe_div(ebit, int_exp)).shift(126)

def herp_040_interest_cov_252d(ebit: pd.Series, int_exp: pd.Series) -> pd.Series:
    """herp_040_interest_cov_252d"""
    return (_safe_div(ebit, int_exp)).shift(252)

def herp_041_tax_anomaly_5d(revenue: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_041_tax_anomaly_5d"""
    return (_safe_div(taxexp, revenue)).shift(5)

def herp_042_tax_anomaly_21d(revenue: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_042_tax_anomaly_21d"""
    return (_safe_div(taxexp, revenue)).shift(21)

def herp_043_tax_anomaly_63d(revenue: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_043_tax_anomaly_63d"""
    return (_safe_div(taxexp, revenue)).shift(63)

def herp_044_tax_anomaly_126d(revenue: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_044_tax_anomaly_126d"""
    return (_safe_div(taxexp, revenue)).shift(126)

def herp_045_tax_anomaly_252d(revenue: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_045_tax_anomaly_252d"""
    return (_safe_div(taxexp, revenue)).shift(252)

def herp_046_deferred_tax_rat_5d(taxexp: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_046_deferred_tax_rat_5d"""
    return (_safe_div(taxexp.diff(252), assets)).shift(5)

def herp_047_deferred_tax_rat_21d(taxexp: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_047_deferred_tax_rat_21d"""
    return (_safe_div(taxexp.diff(252), assets)).shift(21)

def herp_048_deferred_tax_rat_63d(taxexp: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_048_deferred_tax_rat_63d"""
    return (_safe_div(taxexp.diff(252), assets)).shift(63)

def herp_049_deferred_tax_rat_126d(taxexp: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_049_deferred_tax_rat_126d"""
    return (_safe_div(taxexp.diff(252), assets)).shift(126)

def herp_050_deferred_tax_rat_252d(taxexp: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_050_deferred_tax_rat_252d"""
    return (_safe_div(taxexp.diff(252), assets)).shift(252)

def herp_051_op_margin_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_051_op_margin_5d"""
    return (_safe_div(ebit, revenue)).shift(5)

def herp_052_op_margin_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_052_op_margin_21d"""
    return (_safe_div(ebit, revenue)).shift(21)

def herp_053_op_margin_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_053_op_margin_63d"""
    return (_safe_div(ebit, revenue)).shift(63)

def herp_054_op_margin_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_054_op_margin_126d"""
    return (_safe_div(ebit, revenue)).shift(126)

def herp_055_op_margin_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_055_op_margin_252d"""
    return (_safe_div(ebit, revenue)).shift(252)

def herp_056_net_margin_5d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_056_net_margin_5d"""
    return (_safe_div(netinc, revenue)).shift(5)

def herp_057_net_margin_21d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_057_net_margin_21d"""
    return (_safe_div(netinc, revenue)).shift(21)

def herp_058_net_margin_63d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_058_net_margin_63d"""
    return (_safe_div(netinc, revenue)).shift(63)

def herp_059_net_margin_126d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_059_net_margin_126d"""
    return (_safe_div(netinc, revenue)).shift(126)

def herp_060_net_margin_252d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_060_net_margin_252d"""
    return (_safe_div(netinc, revenue)).shift(252)

def herp_061_margin_div_5d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_061_margin_div_5d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue))).shift(5)

def herp_062_margin_div_21d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_062_margin_div_21d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue))).shift(21)

def herp_063_margin_div_63d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_063_margin_div_63d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue))).shift(63)

def herp_064_margin_div_126d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_064_margin_div_126d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue))).shift(126)

def herp_065_margin_div_252d(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """herp_065_margin_div_252d"""
    return ((_safe_div(ebit, revenue) - _safe_div(netinc, revenue))).shift(252)

def herp_066_ebit_assets_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_066_ebit_assets_5d"""
    return (_safe_div(ebit, assets)).shift(5)

def herp_067_ebit_assets_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_067_ebit_assets_21d"""
    return (_safe_div(ebit, assets)).shift(21)

def herp_068_ebit_assets_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_068_ebit_assets_63d"""
    return (_safe_div(ebit, assets)).shift(63)

def herp_069_ebit_assets_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_069_ebit_assets_126d"""
    return (_safe_div(ebit, assets)).shift(126)

def herp_070_ebit_assets_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_070_ebit_assets_252d"""
    return (_safe_div(ebit, assets)).shift(252)

def herp_071_ni_assets_5d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_071_ni_assets_5d"""
    return (_safe_div(netinc, assets)).shift(5)

def herp_072_ni_assets_21d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_072_ni_assets_21d"""
    return (_safe_div(netinc, assets)).shift(21)

def herp_073_ni_assets_63d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_073_ni_assets_63d"""
    return (_safe_div(netinc, assets)).shift(63)

def herp_074_ni_assets_126d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_074_ni_assets_126d"""
    return (_safe_div(netinc, assets)).shift(126)

def herp_075_ni_assets_252d(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_075_ni_assets_252d"""
    return (_safe_div(netinc, assets)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V62_REGISTRY = {
    "herp_001_op_ni_div_5d": {"inputs": ['ebit', 'netinc'], "func": herp_001_op_ni_div_5d},
    "herp_002_op_ni_div_21d": {"inputs": ['ebit', 'netinc'], "func": herp_002_op_ni_div_21d},
    "herp_003_op_ni_div_63d": {"inputs": ['ebit', 'netinc'], "func": herp_003_op_ni_div_63d},
    "herp_004_op_ni_div_126d": {"inputs": ['ebit', 'netinc'], "func": herp_004_op_ni_div_126d},
    "herp_005_op_ni_div_252d": {"inputs": ['ebit', 'netinc'], "func": herp_005_op_ni_div_252d},
    "herp_006_tax_rat_5d": {"inputs": ['taxexp', 'ebt'], "func": herp_006_tax_rat_5d},
    "herp_007_tax_rat_21d": {"inputs": ['taxexp', 'ebt'], "func": herp_007_tax_rat_21d},
    "herp_008_tax_rat_63d": {"inputs": ['taxexp', 'ebt'], "func": herp_008_tax_rat_63d},
    "herp_009_tax_rat_126d": {"inputs": ['taxexp', 'ebt'], "func": herp_009_tax_rat_126d},
    "herp_010_tax_rat_252d": {"inputs": ['taxexp', 'ebt'], "func": herp_010_tax_rat_252d},
    "herp_011_non_op_rat_5d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_011_non_op_rat_5d},
    "herp_012_non_op_rat_21d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_012_non_op_rat_21d},
    "herp_013_non_op_rat_63d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_013_non_op_rat_63d},
    "herp_014_non_op_rat_126d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_014_non_op_rat_126d},
    "herp_015_non_op_rat_252d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_015_non_op_rat_252d},
    "herp_016_ebitda_ni_div_5d": {"inputs": ['ebitda', 'netinc'], "func": herp_016_ebitda_ni_div_5d},
    "herp_017_ebitda_ni_div_21d": {"inputs": ['ebitda', 'netinc'], "func": herp_017_ebitda_ni_div_21d},
    "herp_018_ebitda_ni_div_63d": {"inputs": ['ebitda', 'netinc'], "func": herp_018_ebitda_ni_div_63d},
    "herp_019_ebitda_ni_div_126d": {"inputs": ['ebitda', 'netinc'], "func": herp_019_ebitda_ni_div_126d},
    "herp_020_ebitda_ni_div_252d": {"inputs": ['ebitda', 'netinc'], "func": herp_020_ebitda_ni_div_252d},
    "herp_021_rnd_cap_proxy_5d": {"inputs": ['rnd', 'assets'], "func": herp_021_rnd_cap_proxy_5d},
    "herp_022_rnd_cap_proxy_21d": {"inputs": ['rnd', 'assets'], "func": herp_022_rnd_cap_proxy_21d},
    "herp_023_rnd_cap_proxy_63d": {"inputs": ['rnd', 'assets'], "func": herp_023_rnd_cap_proxy_63d},
    "herp_024_rnd_cap_proxy_126d": {"inputs": ['rnd', 'assets'], "func": herp_024_rnd_cap_proxy_126d},
    "herp_025_rnd_cap_proxy_252d": {"inputs": ['rnd', 'assets'], "func": herp_025_rnd_cap_proxy_252d},
    "herp_026_sga_eff_5d": {"inputs": ['revenue', 'sga'], "func": herp_026_sga_eff_5d},
    "herp_027_sga_eff_21d": {"inputs": ['revenue', 'sga'], "func": herp_027_sga_eff_21d},
    "herp_028_sga_eff_63d": {"inputs": ['revenue', 'sga'], "func": herp_028_sga_eff_63d},
    "herp_029_sga_eff_126d": {"inputs": ['revenue', 'sga'], "func": herp_029_sga_eff_126d},
    "herp_030_sga_eff_252d": {"inputs": ['revenue', 'sga'], "func": herp_030_sga_eff_252d},
    "herp_031_dep_cap_rat_5d": {"inputs": ['capex'], "func": herp_031_dep_cap_rat_5d},
    "herp_032_dep_cap_rat_21d": {"inputs": ['capex'], "func": herp_032_dep_cap_rat_21d},
    "herp_033_dep_cap_rat_63d": {"inputs": ['capex'], "func": herp_033_dep_cap_rat_63d},
    "herp_034_dep_cap_rat_126d": {"inputs": ['capex'], "func": herp_034_dep_cap_rat_126d},
    "herp_035_dep_cap_rat_252d": {"inputs": ['capex'], "func": herp_035_dep_cap_rat_252d},
    "herp_036_interest_cov_5d": {"inputs": ['ebit', 'int_exp'], "func": herp_036_interest_cov_5d},
    "herp_037_interest_cov_21d": {"inputs": ['ebit', 'int_exp'], "func": herp_037_interest_cov_21d},
    "herp_038_interest_cov_63d": {"inputs": ['ebit', 'int_exp'], "func": herp_038_interest_cov_63d},
    "herp_039_interest_cov_126d": {"inputs": ['ebit', 'int_exp'], "func": herp_039_interest_cov_126d},
    "herp_040_interest_cov_252d": {"inputs": ['ebit', 'int_exp'], "func": herp_040_interest_cov_252d},
    "herp_041_tax_anomaly_5d": {"inputs": ['revenue', 'taxexp'], "func": herp_041_tax_anomaly_5d},
    "herp_042_tax_anomaly_21d": {"inputs": ['revenue', 'taxexp'], "func": herp_042_tax_anomaly_21d},
    "herp_043_tax_anomaly_63d": {"inputs": ['revenue', 'taxexp'], "func": herp_043_tax_anomaly_63d},
    "herp_044_tax_anomaly_126d": {"inputs": ['revenue', 'taxexp'], "func": herp_044_tax_anomaly_126d},
    "herp_045_tax_anomaly_252d": {"inputs": ['revenue', 'taxexp'], "func": herp_045_tax_anomaly_252d},
    "herp_046_deferred_tax_rat_5d": {"inputs": ['taxexp', 'assets'], "func": herp_046_deferred_tax_rat_5d},
    "herp_047_deferred_tax_rat_21d": {"inputs": ['taxexp', 'assets'], "func": herp_047_deferred_tax_rat_21d},
    "herp_048_deferred_tax_rat_63d": {"inputs": ['taxexp', 'assets'], "func": herp_048_deferred_tax_rat_63d},
    "herp_049_deferred_tax_rat_126d": {"inputs": ['taxexp', 'assets'], "func": herp_049_deferred_tax_rat_126d},
    "herp_050_deferred_tax_rat_252d": {"inputs": ['taxexp', 'assets'], "func": herp_050_deferred_tax_rat_252d},
    "herp_051_op_margin_5d": {"inputs": ['revenue', 'ebit'], "func": herp_051_op_margin_5d},
    "herp_052_op_margin_21d": {"inputs": ['revenue', 'ebit'], "func": herp_052_op_margin_21d},
    "herp_053_op_margin_63d": {"inputs": ['revenue', 'ebit'], "func": herp_053_op_margin_63d},
    "herp_054_op_margin_126d": {"inputs": ['revenue', 'ebit'], "func": herp_054_op_margin_126d},
    "herp_055_op_margin_252d": {"inputs": ['revenue', 'ebit'], "func": herp_055_op_margin_252d},
    "herp_056_net_margin_5d": {"inputs": ['revenue', 'netinc'], "func": herp_056_net_margin_5d},
    "herp_057_net_margin_21d": {"inputs": ['revenue', 'netinc'], "func": herp_057_net_margin_21d},
    "herp_058_net_margin_63d": {"inputs": ['revenue', 'netinc'], "func": herp_058_net_margin_63d},
    "herp_059_net_margin_126d": {"inputs": ['revenue', 'netinc'], "func": herp_059_net_margin_126d},
    "herp_060_net_margin_252d": {"inputs": ['revenue', 'netinc'], "func": herp_060_net_margin_252d},
    "herp_061_margin_div_5d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_061_margin_div_5d},
    "herp_062_margin_div_21d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_062_margin_div_21d},
    "herp_063_margin_div_63d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_063_margin_div_63d},
    "herp_064_margin_div_126d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_064_margin_div_126d},
    "herp_065_margin_div_252d": {"inputs": ['revenue', 'ebit', 'netinc'], "func": herp_065_margin_div_252d},
    "herp_066_ebit_assets_5d": {"inputs": ['ebit', 'assets'], "func": herp_066_ebit_assets_5d},
    "herp_067_ebit_assets_21d": {"inputs": ['ebit', 'assets'], "func": herp_067_ebit_assets_21d},
    "herp_068_ebit_assets_63d": {"inputs": ['ebit', 'assets'], "func": herp_068_ebit_assets_63d},
    "herp_069_ebit_assets_126d": {"inputs": ['ebit', 'assets'], "func": herp_069_ebit_assets_126d},
    "herp_070_ebit_assets_252d": {"inputs": ['ebit', 'assets'], "func": herp_070_ebit_assets_252d},
    "herp_071_ni_assets_5d": {"inputs": ['netinc', 'assets'], "func": herp_071_ni_assets_5d},
    "herp_072_ni_assets_21d": {"inputs": ['netinc', 'assets'], "func": herp_072_ni_assets_21d},
    "herp_073_ni_assets_63d": {"inputs": ['netinc', 'assets'], "func": herp_073_ni_assets_63d},
    "herp_074_ni_assets_126d": {"inputs": ['netinc', 'assets'], "func": herp_074_ni_assets_126d},
    "herp_075_ni_assets_252d": {"inputs": ['netinc', 'assets'], "func": herp_075_ni_assets_252d},
}
