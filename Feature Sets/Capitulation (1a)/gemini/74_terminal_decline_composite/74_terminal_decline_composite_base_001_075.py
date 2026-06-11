"""
74_terminal_decline_composite — Base Features 001-075
Domain: Composite of all forensic decay signals
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

def tedc_001_rev_g_term_5d(revenue: pd.Series) -> pd.Series:
    """tedc_001_rev_g_term_5d"""
    return (revenue.pct_change(1260)).shift(5)

def tedc_002_rev_g_term_21d(revenue: pd.Series) -> pd.Series:
    """tedc_002_rev_g_term_21d"""
    return (revenue.pct_change(1260)).shift(21)

def tedc_003_rev_g_term_63d(revenue: pd.Series) -> pd.Series:
    """tedc_003_rev_g_term_63d"""
    return (revenue.pct_change(1260)).shift(63)

def tedc_004_rev_g_term_126d(revenue: pd.Series) -> pd.Series:
    """tedc_004_rev_g_term_126d"""
    return (revenue.pct_change(1260)).shift(126)

def tedc_005_rev_g_term_252d(revenue: pd.Series) -> pd.Series:
    """tedc_005_rev_g_term_252d"""
    return (revenue.pct_change(1260)).shift(252)

def tedc_006_ni_g_term_5d(netinc: pd.Series) -> pd.Series:
    """tedc_006_ni_g_term_5d"""
    return (netinc.pct_change(1260)).shift(5)

def tedc_007_ni_g_term_21d(netinc: pd.Series) -> pd.Series:
    """tedc_007_ni_g_term_21d"""
    return (netinc.pct_change(1260)).shift(21)

def tedc_008_ni_g_term_63d(netinc: pd.Series) -> pd.Series:
    """tedc_008_ni_g_term_63d"""
    return (netinc.pct_change(1260)).shift(63)

def tedc_009_ni_g_term_126d(netinc: pd.Series) -> pd.Series:
    """tedc_009_ni_g_term_126d"""
    return (netinc.pct_change(1260)).shift(126)

def tedc_010_ni_g_term_252d(netinc: pd.Series) -> pd.Series:
    """tedc_010_ni_g_term_252d"""
    return (netinc.pct_change(1260)).shift(252)

def tedc_011_mc_g_term_5d(marketcap: pd.Series) -> pd.Series:
    """tedc_011_mc_g_term_5d"""
    return (marketcap.pct_change(1260)).shift(5)

def tedc_012_mc_g_term_21d(marketcap: pd.Series) -> pd.Series:
    """tedc_012_mc_g_term_21d"""
    return (marketcap.pct_change(1260)).shift(21)

def tedc_013_mc_g_term_63d(marketcap: pd.Series) -> pd.Series:
    """tedc_013_mc_g_term_63d"""
    return (marketcap.pct_change(1260)).shift(63)

def tedc_014_mc_g_term_126d(marketcap: pd.Series) -> pd.Series:
    """tedc_014_mc_g_term_126d"""
    return (marketcap.pct_change(1260)).shift(126)

def tedc_015_mc_g_term_252d(marketcap: pd.Series) -> pd.Series:
    """tedc_015_mc_g_term_252d"""
    return (marketcap.pct_change(1260)).shift(252)

def tedc_016_asset_g_term_5d(assets: pd.Series) -> pd.Series:
    """tedc_016_asset_g_term_5d"""
    return (assets.pct_change(1260)).shift(5)

def tedc_017_asset_g_term_21d(assets: pd.Series) -> pd.Series:
    """tedc_017_asset_g_term_21d"""
    return (assets.pct_change(1260)).shift(21)

def tedc_018_asset_g_term_63d(assets: pd.Series) -> pd.Series:
    """tedc_018_asset_g_term_63d"""
    return (assets.pct_change(1260)).shift(63)

def tedc_019_asset_g_term_126d(assets: pd.Series) -> pd.Series:
    """tedc_019_asset_g_term_126d"""
    return (assets.pct_change(1260)).shift(126)

def tedc_020_asset_g_term_252d(assets: pd.Series) -> pd.Series:
    """tedc_020_asset_g_term_252d"""
    return (assets.pct_change(1260)).shift(252)

def tedc_021_terminal_decline_index_5d(revenue: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_021_terminal_decline_index_5d"""
    return ((revenue.pct_change(1260) + netinc.pct_change(1260) + assets.pct_change(1260)) / 3).shift(5)

def tedc_022_terminal_decline_index_21d(revenue: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_022_terminal_decline_index_21d"""
    return ((revenue.pct_change(1260) + netinc.pct_change(1260) + assets.pct_change(1260)) / 3).shift(21)

def tedc_023_terminal_decline_index_63d(revenue: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_023_terminal_decline_index_63d"""
    return ((revenue.pct_change(1260) + netinc.pct_change(1260) + assets.pct_change(1260)) / 3).shift(63)

def tedc_024_terminal_decline_index_126d(revenue: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_024_terminal_decline_index_126d"""
    return ((revenue.pct_change(1260) + netinc.pct_change(1260) + assets.pct_change(1260)) / 3).shift(126)

def tedc_025_terminal_decline_index_252d(revenue: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_025_terminal_decline_index_252d"""
    return ((revenue.pct_change(1260) + netinc.pct_change(1260) + assets.pct_change(1260)) / 3).shift(252)

def tedc_026_margin_decay_term_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """tedc_026_margin_decay_term_5d"""
    return ((_safe_div(ebit, revenue)).diff(1260)).shift(5)

def tedc_027_margin_decay_term_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """tedc_027_margin_decay_term_21d"""
    return ((_safe_div(ebit, revenue)).diff(1260)).shift(21)

def tedc_028_margin_decay_term_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """tedc_028_margin_decay_term_63d"""
    return ((_safe_div(ebit, revenue)).diff(1260)).shift(63)

def tedc_029_margin_decay_term_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """tedc_029_margin_decay_term_126d"""
    return ((_safe_div(ebit, revenue)).diff(1260)).shift(126)

def tedc_030_margin_decay_term_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """tedc_030_margin_decay_term_252d"""
    return ((_safe_div(ebit, revenue)).diff(1260)).shift(252)

def tedc_031_roic_decay_term_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_031_roic_decay_term_5d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(5)

def tedc_032_roic_decay_term_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_032_roic_decay_term_21d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(21)

def tedc_033_roic_decay_term_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_033_roic_decay_term_63d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(63)

def tedc_034_roic_decay_term_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_034_roic_decay_term_126d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(126)

def tedc_035_roic_decay_term_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_035_roic_decay_term_252d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(252)

def tedc_036_market_share_loss_5d(revenue: pd.Series) -> pd.Series:
    """tedc_036_market_share_loss_5d"""
    return ((_safe_div(revenue, revenue.rolling(1260).sum())).diff(1260)).shift(5)

def tedc_037_market_share_loss_21d(revenue: pd.Series) -> pd.Series:
    """tedc_037_market_share_loss_21d"""
    return ((_safe_div(revenue, revenue.rolling(1260).sum())).diff(1260)).shift(21)

def tedc_038_market_share_loss_63d(revenue: pd.Series) -> pd.Series:
    """tedc_038_market_share_loss_63d"""
    return ((_safe_div(revenue, revenue.rolling(1260).sum())).diff(1260)).shift(63)

def tedc_039_market_share_loss_126d(revenue: pd.Series) -> pd.Series:
    """tedc_039_market_share_loss_126d"""
    return ((_safe_div(revenue, revenue.rolling(1260).sum())).diff(1260)).shift(126)

def tedc_040_market_share_loss_252d(revenue: pd.Series) -> pd.Series:
    """tedc_040_market_share_loss_252d"""
    return ((_safe_div(revenue, revenue.rolling(1260).sum())).diff(1260)).shift(252)

def tedc_041_valuation_collapse_5d(ps: pd.Series) -> pd.Series:
    """tedc_041_valuation_collapse_5d"""
    return (ps / ps.rolling(1260).max()).shift(5)

def tedc_042_valuation_collapse_21d(ps: pd.Series) -> pd.Series:
    """tedc_042_valuation_collapse_21d"""
    return (ps / ps.rolling(1260).max()).shift(21)

def tedc_043_valuation_collapse_63d(ps: pd.Series) -> pd.Series:
    """tedc_043_valuation_collapse_63d"""
    return (ps / ps.rolling(1260).max()).shift(63)

def tedc_044_valuation_collapse_126d(ps: pd.Series) -> pd.Series:
    """tedc_044_valuation_collapse_126d"""
    return (ps / ps.rolling(1260).max()).shift(126)

def tedc_045_valuation_collapse_252d(ps: pd.Series) -> pd.Series:
    """tedc_045_valuation_collapse_252d"""
    return (ps / ps.rolling(1260).max()).shift(252)

def tedc_046_efficiency_decay_5d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_046_efficiency_decay_5d"""
    return ((_safe_div(revenue, sga + rnd)).diff(1260)).shift(5)

def tedc_047_efficiency_decay_21d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_047_efficiency_decay_21d"""
    return ((_safe_div(revenue, sga + rnd)).diff(1260)).shift(21)

def tedc_048_efficiency_decay_63d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_048_efficiency_decay_63d"""
    return ((_safe_div(revenue, sga + rnd)).diff(1260)).shift(63)

def tedc_049_efficiency_decay_126d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_049_efficiency_decay_126d"""
    return ((_safe_div(revenue, sga + rnd)).diff(1260)).shift(126)

def tedc_050_efficiency_decay_252d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_050_efficiency_decay_252d"""
    return ((_safe_div(revenue, sga + rnd)).diff(1260)).shift(252)

def tedc_051_terminal_z_5d(revenue: pd.Series) -> pd.Series:
    """tedc_051_terminal_z_5d"""
    return (_zscore_rolling(revenue.pct_change(1260), 2520)).shift(5)

def tedc_052_terminal_z_21d(revenue: pd.Series) -> pd.Series:
    """tedc_052_terminal_z_21d"""
    return (_zscore_rolling(revenue.pct_change(1260), 2520)).shift(21)

def tedc_053_terminal_z_63d(revenue: pd.Series) -> pd.Series:
    """tedc_053_terminal_z_63d"""
    return (_zscore_rolling(revenue.pct_change(1260), 2520)).shift(63)

def tedc_054_terminal_z_126d(revenue: pd.Series) -> pd.Series:
    """tedc_054_terminal_z_126d"""
    return (_zscore_rolling(revenue.pct_change(1260), 2520)).shift(126)

def tedc_055_terminal_z_252d(revenue: pd.Series) -> pd.Series:
    """tedc_055_terminal_z_252d"""
    return (_zscore_rolling(revenue.pct_change(1260), 2520)).shift(252)

def tedc_056_obsolescence_proxy_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_056_obsolescence_proxy_5d"""
    return ((_safe_div(rnd, revenue)).diff(1260)).shift(5)

def tedc_057_obsolescence_proxy_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_057_obsolescence_proxy_21d"""
    return ((_safe_div(rnd, revenue)).diff(1260)).shift(21)

def tedc_058_obsolescence_proxy_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_058_obsolescence_proxy_63d"""
    return ((_safe_div(rnd, revenue)).diff(1260)).shift(63)

def tedc_059_obsolescence_proxy_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_059_obsolescence_proxy_126d"""
    return ((_safe_div(rnd, revenue)).diff(1260)).shift(126)

def tedc_060_obsolescence_proxy_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """tedc_060_obsolescence_proxy_252d"""
    return ((_safe_div(rnd, revenue)).diff(1260)).shift(252)

def tedc_061_capital_starvation_5d(capex: pd.Series) -> pd.Series:
    """tedc_061_capital_starvation_5d"""
    return ((_safe_div(capex, depamor)).diff(1260)).shift(5)

def tedc_062_capital_starvation_21d(capex: pd.Series) -> pd.Series:
    """tedc_062_capital_starvation_21d"""
    return ((_safe_div(capex, depamor)).diff(1260)).shift(21)

def tedc_063_capital_starvation_63d(capex: pd.Series) -> pd.Series:
    """tedc_063_capital_starvation_63d"""
    return ((_safe_div(capex, depamor)).diff(1260)).shift(63)

def tedc_064_capital_starvation_126d(capex: pd.Series) -> pd.Series:
    """tedc_064_capital_starvation_126d"""
    return ((_safe_div(capex, depamor)).diff(1260)).shift(126)

def tedc_065_capital_starvation_252d(capex: pd.Series) -> pd.Series:
    """tedc_065_capital_starvation_252d"""
    return ((_safe_div(capex, depamor)).diff(1260)).shift(252)

def tedc_066_dividend_cut_proxy_5d(netinc: pd.Series, shareswa: pd.Series) -> pd.Series:
    """tedc_066_dividend_cut_proxy_5d"""
    return ((_safe_div(netinc, shareswa)).diff(1260)).shift(5)

def tedc_067_dividend_cut_proxy_21d(netinc: pd.Series, shareswa: pd.Series) -> pd.Series:
    """tedc_067_dividend_cut_proxy_21d"""
    return ((_safe_div(netinc, shareswa)).diff(1260)).shift(21)

def tedc_068_dividend_cut_proxy_63d(netinc: pd.Series, shareswa: pd.Series) -> pd.Series:
    """tedc_068_dividend_cut_proxy_63d"""
    return ((_safe_div(netinc, shareswa)).diff(1260)).shift(63)

def tedc_069_dividend_cut_proxy_126d(netinc: pd.Series, shareswa: pd.Series) -> pd.Series:
    """tedc_069_dividend_cut_proxy_126d"""
    return ((_safe_div(netinc, shareswa)).diff(1260)).shift(126)

def tedc_070_dividend_cut_proxy_252d(netinc: pd.Series, shareswa: pd.Series) -> pd.Series:
    """tedc_070_dividend_cut_proxy_252d"""
    return ((_safe_div(netinc, shareswa)).diff(1260)).shift(252)

def tedc_071_terminal_decay_score_5d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """tedc_071_terminal_decay_score_5d"""
    return ((_zscore_rolling(revenue, 1260) + _zscore_rolling(netinc, 1260)) / 2).shift(5)

def tedc_072_terminal_decay_score_21d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """tedc_072_terminal_decay_score_21d"""
    return ((_zscore_rolling(revenue, 1260) + _zscore_rolling(netinc, 1260)) / 2).shift(21)

def tedc_073_terminal_decay_score_63d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """tedc_073_terminal_decay_score_63d"""
    return ((_zscore_rolling(revenue, 1260) + _zscore_rolling(netinc, 1260)) / 2).shift(63)

def tedc_074_terminal_decay_score_126d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """tedc_074_terminal_decay_score_126d"""
    return ((_zscore_rolling(revenue, 1260) + _zscore_rolling(netinc, 1260)) / 2).shift(126)

def tedc_075_terminal_decay_score_252d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """tedc_075_terminal_decay_score_252d"""
    return ((_zscore_rolling(revenue, 1260) + _zscore_rolling(netinc, 1260)) / 2).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V74_REGISTRY = {
    "tedc_001_rev_g_term_5d": {"inputs": ['revenue'], "func": tedc_001_rev_g_term_5d},
    "tedc_002_rev_g_term_21d": {"inputs": ['revenue'], "func": tedc_002_rev_g_term_21d},
    "tedc_003_rev_g_term_63d": {"inputs": ['revenue'], "func": tedc_003_rev_g_term_63d},
    "tedc_004_rev_g_term_126d": {"inputs": ['revenue'], "func": tedc_004_rev_g_term_126d},
    "tedc_005_rev_g_term_252d": {"inputs": ['revenue'], "func": tedc_005_rev_g_term_252d},
    "tedc_006_ni_g_term_5d": {"inputs": ['netinc'], "func": tedc_006_ni_g_term_5d},
    "tedc_007_ni_g_term_21d": {"inputs": ['netinc'], "func": tedc_007_ni_g_term_21d},
    "tedc_008_ni_g_term_63d": {"inputs": ['netinc'], "func": tedc_008_ni_g_term_63d},
    "tedc_009_ni_g_term_126d": {"inputs": ['netinc'], "func": tedc_009_ni_g_term_126d},
    "tedc_010_ni_g_term_252d": {"inputs": ['netinc'], "func": tedc_010_ni_g_term_252d},
    "tedc_011_mc_g_term_5d": {"inputs": ['marketcap'], "func": tedc_011_mc_g_term_5d},
    "tedc_012_mc_g_term_21d": {"inputs": ['marketcap'], "func": tedc_012_mc_g_term_21d},
    "tedc_013_mc_g_term_63d": {"inputs": ['marketcap'], "func": tedc_013_mc_g_term_63d},
    "tedc_014_mc_g_term_126d": {"inputs": ['marketcap'], "func": tedc_014_mc_g_term_126d},
    "tedc_015_mc_g_term_252d": {"inputs": ['marketcap'], "func": tedc_015_mc_g_term_252d},
    "tedc_016_asset_g_term_5d": {"inputs": ['assets'], "func": tedc_016_asset_g_term_5d},
    "tedc_017_asset_g_term_21d": {"inputs": ['assets'], "func": tedc_017_asset_g_term_21d},
    "tedc_018_asset_g_term_63d": {"inputs": ['assets'], "func": tedc_018_asset_g_term_63d},
    "tedc_019_asset_g_term_126d": {"inputs": ['assets'], "func": tedc_019_asset_g_term_126d},
    "tedc_020_asset_g_term_252d": {"inputs": ['assets'], "func": tedc_020_asset_g_term_252d},
    "tedc_021_terminal_decline_index_5d": {"inputs": ['revenue', 'netinc', 'assets'], "func": tedc_021_terminal_decline_index_5d},
    "tedc_022_terminal_decline_index_21d": {"inputs": ['revenue', 'netinc', 'assets'], "func": tedc_022_terminal_decline_index_21d},
    "tedc_023_terminal_decline_index_63d": {"inputs": ['revenue', 'netinc', 'assets'], "func": tedc_023_terminal_decline_index_63d},
    "tedc_024_terminal_decline_index_126d": {"inputs": ['revenue', 'netinc', 'assets'], "func": tedc_024_terminal_decline_index_126d},
    "tedc_025_terminal_decline_index_252d": {"inputs": ['revenue', 'netinc', 'assets'], "func": tedc_025_terminal_decline_index_252d},
    "tedc_026_margin_decay_term_5d": {"inputs": ['revenue', 'ebit'], "func": tedc_026_margin_decay_term_5d},
    "tedc_027_margin_decay_term_21d": {"inputs": ['revenue', 'ebit'], "func": tedc_027_margin_decay_term_21d},
    "tedc_028_margin_decay_term_63d": {"inputs": ['revenue', 'ebit'], "func": tedc_028_margin_decay_term_63d},
    "tedc_029_margin_decay_term_126d": {"inputs": ['revenue', 'ebit'], "func": tedc_029_margin_decay_term_126d},
    "tedc_030_margin_decay_term_252d": {"inputs": ['revenue', 'ebit'], "func": tedc_030_margin_decay_term_252d},
    "tedc_031_roic_decay_term_5d": {"inputs": ['ebit', 'assets'], "func": tedc_031_roic_decay_term_5d},
    "tedc_032_roic_decay_term_21d": {"inputs": ['ebit', 'assets'], "func": tedc_032_roic_decay_term_21d},
    "tedc_033_roic_decay_term_63d": {"inputs": ['ebit', 'assets'], "func": tedc_033_roic_decay_term_63d},
    "tedc_034_roic_decay_term_126d": {"inputs": ['ebit', 'assets'], "func": tedc_034_roic_decay_term_126d},
    "tedc_035_roic_decay_term_252d": {"inputs": ['ebit', 'assets'], "func": tedc_035_roic_decay_term_252d},
    "tedc_036_market_share_loss_5d": {"inputs": ['revenue'], "func": tedc_036_market_share_loss_5d},
    "tedc_037_market_share_loss_21d": {"inputs": ['revenue'], "func": tedc_037_market_share_loss_21d},
    "tedc_038_market_share_loss_63d": {"inputs": ['revenue'], "func": tedc_038_market_share_loss_63d},
    "tedc_039_market_share_loss_126d": {"inputs": ['revenue'], "func": tedc_039_market_share_loss_126d},
    "tedc_040_market_share_loss_252d": {"inputs": ['revenue'], "func": tedc_040_market_share_loss_252d},
    "tedc_041_valuation_collapse_5d": {"inputs": ['ps'], "func": tedc_041_valuation_collapse_5d},
    "tedc_042_valuation_collapse_21d": {"inputs": ['ps'], "func": tedc_042_valuation_collapse_21d},
    "tedc_043_valuation_collapse_63d": {"inputs": ['ps'], "func": tedc_043_valuation_collapse_63d},
    "tedc_044_valuation_collapse_126d": {"inputs": ['ps'], "func": tedc_044_valuation_collapse_126d},
    "tedc_045_valuation_collapse_252d": {"inputs": ['ps'], "func": tedc_045_valuation_collapse_252d},
    "tedc_046_efficiency_decay_5d": {"inputs": ['revenue', 'sga', 'rnd'], "func": tedc_046_efficiency_decay_5d},
    "tedc_047_efficiency_decay_21d": {"inputs": ['revenue', 'sga', 'rnd'], "func": tedc_047_efficiency_decay_21d},
    "tedc_048_efficiency_decay_63d": {"inputs": ['revenue', 'sga', 'rnd'], "func": tedc_048_efficiency_decay_63d},
    "tedc_049_efficiency_decay_126d": {"inputs": ['revenue', 'sga', 'rnd'], "func": tedc_049_efficiency_decay_126d},
    "tedc_050_efficiency_decay_252d": {"inputs": ['revenue', 'sga', 'rnd'], "func": tedc_050_efficiency_decay_252d},
    "tedc_051_terminal_z_5d": {"inputs": ['revenue'], "func": tedc_051_terminal_z_5d},
    "tedc_052_terminal_z_21d": {"inputs": ['revenue'], "func": tedc_052_terminal_z_21d},
    "tedc_053_terminal_z_63d": {"inputs": ['revenue'], "func": tedc_053_terminal_z_63d},
    "tedc_054_terminal_z_126d": {"inputs": ['revenue'], "func": tedc_054_terminal_z_126d},
    "tedc_055_terminal_z_252d": {"inputs": ['revenue'], "func": tedc_055_terminal_z_252d},
    "tedc_056_obsolescence_proxy_5d": {"inputs": ['revenue', 'rnd'], "func": tedc_056_obsolescence_proxy_5d},
    "tedc_057_obsolescence_proxy_21d": {"inputs": ['revenue', 'rnd'], "func": tedc_057_obsolescence_proxy_21d},
    "tedc_058_obsolescence_proxy_63d": {"inputs": ['revenue', 'rnd'], "func": tedc_058_obsolescence_proxy_63d},
    "tedc_059_obsolescence_proxy_126d": {"inputs": ['revenue', 'rnd'], "func": tedc_059_obsolescence_proxy_126d},
    "tedc_060_obsolescence_proxy_252d": {"inputs": ['revenue', 'rnd'], "func": tedc_060_obsolescence_proxy_252d},
    "tedc_061_capital_starvation_5d": {"inputs": ['capex'], "func": tedc_061_capital_starvation_5d},
    "tedc_062_capital_starvation_21d": {"inputs": ['capex'], "func": tedc_062_capital_starvation_21d},
    "tedc_063_capital_starvation_63d": {"inputs": ['capex'], "func": tedc_063_capital_starvation_63d},
    "tedc_064_capital_starvation_126d": {"inputs": ['capex'], "func": tedc_064_capital_starvation_126d},
    "tedc_065_capital_starvation_252d": {"inputs": ['capex'], "func": tedc_065_capital_starvation_252d},
    "tedc_066_dividend_cut_proxy_5d": {"inputs": ['netinc', 'shareswa'], "func": tedc_066_dividend_cut_proxy_5d},
    "tedc_067_dividend_cut_proxy_21d": {"inputs": ['netinc', 'shareswa'], "func": tedc_067_dividend_cut_proxy_21d},
    "tedc_068_dividend_cut_proxy_63d": {"inputs": ['netinc', 'shareswa'], "func": tedc_068_dividend_cut_proxy_63d},
    "tedc_069_dividend_cut_proxy_126d": {"inputs": ['netinc', 'shareswa'], "func": tedc_069_dividend_cut_proxy_126d},
    "tedc_070_dividend_cut_proxy_252d": {"inputs": ['netinc', 'shareswa'], "func": tedc_070_dividend_cut_proxy_252d},
    "tedc_071_terminal_decay_score_5d": {"inputs": ['revenue', 'netinc'], "func": tedc_071_terminal_decay_score_5d},
    "tedc_072_terminal_decay_score_21d": {"inputs": ['revenue', 'netinc'], "func": tedc_072_terminal_decay_score_21d},
    "tedc_073_terminal_decay_score_63d": {"inputs": ['revenue', 'netinc'], "func": tedc_073_terminal_decay_score_63d},
    "tedc_074_terminal_decay_score_126d": {"inputs": ['revenue', 'netinc'], "func": tedc_074_terminal_decay_score_126d},
    "tedc_075_terminal_decay_score_252d": {"inputs": ['revenue', 'netinc'], "func": tedc_075_terminal_decay_score_252d},
}
