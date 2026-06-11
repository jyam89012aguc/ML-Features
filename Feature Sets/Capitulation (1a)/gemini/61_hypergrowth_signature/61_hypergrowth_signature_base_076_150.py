"""
61_hypergrowth_signature — Base Features 076-150
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

def hygr_076_rule40_z_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_076_rule40_z_5d"""
    return (_zscore_rolling(_safe_div(ebitda, revenue) + revenue.pct_change(252), 1260)).shift(5)

def hygr_077_rule40_z_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_077_rule40_z_21d"""
    return (_zscore_rolling(_safe_div(ebitda, revenue) + revenue.pct_change(252), 1260)).shift(21)

def hygr_078_rule40_z_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_078_rule40_z_63d"""
    return (_zscore_rolling(_safe_div(ebitda, revenue) + revenue.pct_change(252), 1260)).shift(63)

def hygr_079_rule40_z_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_079_rule40_z_126d"""
    return (_zscore_rolling(_safe_div(ebitda, revenue) + revenue.pct_change(252), 1260)).shift(126)

def hygr_080_rule40_z_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_080_rule40_z_252d"""
    return (_zscore_rolling(_safe_div(ebitda, revenue) + revenue.pct_change(252), 1260)).shift(252)

def hygr_081_rev_p_mc_5d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_081_rev_p_mc_5d"""
    return (_safe_div(revenue, marketcap)).shift(5)

def hygr_082_rev_p_mc_21d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_082_rev_p_mc_21d"""
    return (_safe_div(revenue, marketcap)).shift(21)

def hygr_083_rev_p_mc_63d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_083_rev_p_mc_63d"""
    return (_safe_div(revenue, marketcap)).shift(63)

def hygr_084_rev_p_mc_126d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_084_rev_p_mc_126d"""
    return (_safe_div(revenue, marketcap)).shift(126)

def hygr_085_rev_p_mc_252d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """hygr_085_rev_p_mc_252d"""
    return (_safe_div(revenue, marketcap)).shift(252)

def hygr_086_hg_persistence_5d(revenue: pd.Series) -> pd.Series:
    """hygr_086_hg_persistence_5d"""
    return _safe_div(revenue.pct_change(252), revenue.pct_change(252).shift(252))

def hygr_087_hg_persistence_21d(revenue: pd.Series) -> pd.Series:
    """hygr_087_hg_persistence_21d"""
    return _safe_div(revenue.pct_change(252), revenue.pct_change(252).shift(252))

def hygr_088_hg_persistence_63d(revenue: pd.Series) -> pd.Series:
    """hygr_088_hg_persistence_63d"""
    return _safe_div(revenue.pct_change(252), revenue.pct_change(252).shift(252))

def hygr_089_hg_persistence_126d(revenue: pd.Series) -> pd.Series:
    """hygr_089_hg_persistence_126d"""
    return _safe_div(revenue.pct_change(252), revenue.pct_change(252).shift(252))

def hygr_090_hg_persistence_252d(revenue: pd.Series) -> pd.Series:
    """hygr_090_hg_persistence_252d"""
    return _safe_div(revenue.pct_change(252), revenue.pct_change(252).shift(252))

def hygr_091_log_rev_5d(revenue: pd.Series) -> pd.Series:
    """hygr_091_log_rev_5d"""
    return (np.log1p(revenue.clip(lower=0))).shift(5)

def hygr_092_log_rev_21d(revenue: pd.Series) -> pd.Series:
    """hygr_092_log_rev_21d"""
    return (np.log1p(revenue.clip(lower=0))).shift(21)

def hygr_093_log_rev_63d(revenue: pd.Series) -> pd.Series:
    """hygr_093_log_rev_63d"""
    return (np.log1p(revenue.clip(lower=0))).shift(63)

def hygr_094_log_rev_126d(revenue: pd.Series) -> pd.Series:
    """hygr_094_log_rev_126d"""
    return (np.log1p(revenue.clip(lower=0))).shift(126)

def hygr_095_log_rev_252d(revenue: pd.Series) -> pd.Series:
    """hygr_095_log_rev_252d"""
    return (np.log1p(revenue.clip(lower=0))).shift(252)

def hygr_096_rev_g_accel_5d(revenue: pd.Series) -> pd.Series:
    """hygr_096_rev_g_accel_5d"""
    return (revenue.pct_change(252).diff(63)).shift(5)

def hygr_097_rev_g_accel_21d(revenue: pd.Series) -> pd.Series:
    """hygr_097_rev_g_accel_21d"""
    return (revenue.pct_change(252).diff(63)).shift(21)

def hygr_098_rev_g_accel_63d(revenue: pd.Series) -> pd.Series:
    """hygr_098_rev_g_accel_63d"""
    return (revenue.pct_change(252).diff(63)).shift(63)

def hygr_099_rev_g_accel_126d(revenue: pd.Series) -> pd.Series:
    """hygr_099_rev_g_accel_126d"""
    return (revenue.pct_change(252).diff(63)).shift(126)

def hygr_100_rev_g_accel_252d(revenue: pd.Series) -> pd.Series:
    """hygr_100_rev_g_accel_252d"""
    return (revenue.pct_change(252).diff(63)).shift(252)

def hygr_101_fcf_m_5d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_101_fcf_m_5d"""
    return (_safe_div(fcf, revenue)).shift(5)

def hygr_102_fcf_m_21d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_102_fcf_m_21d"""
    return (_safe_div(fcf, revenue)).shift(21)

def hygr_103_fcf_m_63d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_103_fcf_m_63d"""
    return (_safe_div(fcf, revenue)).shift(63)

def hygr_104_fcf_m_126d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_104_fcf_m_126d"""
    return (_safe_div(fcf, revenue)).shift(126)

def hygr_105_fcf_m_252d(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """hygr_105_fcf_m_252d"""
    return (_safe_div(fcf, revenue)).shift(252)

def hygr_106_ebitda_m_5d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_106_ebitda_m_5d"""
    return (_safe_div(ebitda, revenue)).shift(5)

def hygr_107_ebitda_m_21d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_107_ebitda_m_21d"""
    return (_safe_div(ebitda, revenue)).shift(21)

def hygr_108_ebitda_m_63d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_108_ebitda_m_63d"""
    return (_safe_div(ebitda, revenue)).shift(63)

def hygr_109_ebitda_m_126d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_109_ebitda_m_126d"""
    return (_safe_div(ebitda, revenue)).shift(126)

def hygr_110_ebitda_m_252d(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """hygr_110_ebitda_m_252d"""
    return (_safe_div(ebitda, revenue)).shift(252)

def hygr_111_ni_m_5d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """hygr_111_ni_m_5d"""
    return (_safe_div(netinc, revenue)).shift(5)

def hygr_112_ni_m_21d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """hygr_112_ni_m_21d"""
    return (_safe_div(netinc, revenue)).shift(21)

def hygr_113_ni_m_63d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """hygr_113_ni_m_63d"""
    return (_safe_div(netinc, revenue)).shift(63)

def hygr_114_ni_m_126d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """hygr_114_ni_m_126d"""
    return (_safe_div(netinc, revenue)).shift(126)

def hygr_115_ni_m_252d(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """hygr_115_ni_m_252d"""
    return (_safe_div(netinc, revenue)).shift(252)

def hygr_116_capex_rev_5d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """hygr_116_capex_rev_5d"""
    return (_safe_div(capex, revenue)).shift(5)

def hygr_117_capex_rev_21d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """hygr_117_capex_rev_21d"""
    return (_safe_div(capex, revenue)).shift(21)

def hygr_118_capex_rev_63d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """hygr_118_capex_rev_63d"""
    return (_safe_div(capex, revenue)).shift(63)

def hygr_119_capex_rev_126d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """hygr_119_capex_rev_126d"""
    return (_safe_div(capex, revenue)).shift(126)

def hygr_120_capex_rev_252d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """hygr_120_capex_rev_252d"""
    return (_safe_div(capex, revenue)).shift(252)

def hygr_121_asset_turn_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """hygr_121_asset_turn_5d"""
    return (_safe_div(revenue, assets)).shift(5)

def hygr_122_asset_turn_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """hygr_122_asset_turn_21d"""
    return (_safe_div(revenue, assets)).shift(21)

def hygr_123_asset_turn_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """hygr_123_asset_turn_63d"""
    return (_safe_div(revenue, assets)).shift(63)

def hygr_124_asset_turn_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """hygr_124_asset_turn_126d"""
    return (_safe_div(revenue, assets)).shift(126)

def hygr_125_asset_turn_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """hygr_125_asset_turn_252d"""
    return (_safe_div(revenue, assets)).shift(252)

def hygr_126_roe_5d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """hygr_126_roe_5d"""
    return (_safe_div(netinc, equity)).shift(5)

def hygr_127_roe_21d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """hygr_127_roe_21d"""
    return (_safe_div(netinc, equity)).shift(21)

def hygr_128_roe_63d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """hygr_128_roe_63d"""
    return (_safe_div(netinc, equity)).shift(63)

def hygr_129_roe_126d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """hygr_129_roe_126d"""
    return (_safe_div(netinc, equity)).shift(126)

def hygr_130_roe_252d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """hygr_130_roe_252d"""
    return (_safe_div(netinc, equity)).shift(252)

def hygr_131_roic_5d(ebit: pd.Series, assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """hygr_131_roic_5d"""
    return (_safe_div(ebit * (1 - 0.25), assets - cashnequiv.fillna(0))).shift(5)

def hygr_132_roic_21d(ebit: pd.Series, assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """hygr_132_roic_21d"""
    return (_safe_div(ebit * (1 - 0.25), assets - cashnequiv.fillna(0))).shift(21)

def hygr_133_roic_63d(ebit: pd.Series, assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """hygr_133_roic_63d"""
    return (_safe_div(ebit * (1 - 0.25), assets - cashnequiv.fillna(0))).shift(63)

def hygr_134_roic_126d(ebit: pd.Series, assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """hygr_134_roic_126d"""
    return (_safe_div(ebit * (1 - 0.25), assets - cashnequiv.fillna(0))).shift(126)

def hygr_135_roic_252d(ebit: pd.Series, assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """hygr_135_roic_252d"""
    return (_safe_div(ebit * (1 - 0.25), assets - cashnequiv.fillna(0))).shift(252)

def hygr_136_rev_per_share_g_5d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_136_rev_per_share_g_5d"""
    return ((_safe_div(revenue, shareswa)).pct_change(252)).shift(5)

def hygr_137_rev_per_share_g_21d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_137_rev_per_share_g_21d"""
    return ((_safe_div(revenue, shareswa)).pct_change(252)).shift(21)

def hygr_138_rev_per_share_g_63d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_138_rev_per_share_g_63d"""
    return ((_safe_div(revenue, shareswa)).pct_change(252)).shift(63)

def hygr_139_rev_per_share_g_126d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_139_rev_per_share_g_126d"""
    return ((_safe_div(revenue, shareswa)).pct_change(252)).shift(126)

def hygr_140_rev_per_share_g_252d(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """hygr_140_rev_per_share_g_252d"""
    return ((_safe_div(revenue, shareswa)).pct_change(252)).shift(252)

def hygr_141_market_share_proxy_5d(revenue: pd.Series) -> pd.Series:
    """hygr_141_market_share_proxy_5d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(5)

def hygr_142_market_share_proxy_21d(revenue: pd.Series) -> pd.Series:
    """hygr_142_market_share_proxy_21d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(21)

def hygr_143_market_share_proxy_63d(revenue: pd.Series) -> pd.Series:
    """hygr_143_market_share_proxy_63d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(63)

def hygr_144_market_share_proxy_126d(revenue: pd.Series) -> pd.Series:
    """hygr_144_market_share_proxy_126d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(126)

def hygr_145_market_share_proxy_252d(revenue: pd.Series) -> pd.Series:
    """hygr_145_market_share_proxy_252d"""
    return (_safe_div(revenue, revenue.rolling(252).sum())).shift(252)

def hygr_146_valuation_compression_5d(ps: pd.Series) -> pd.Series:
    """hygr_146_valuation_compression_5d"""
    return (_safe_div(ps, ps.rolling(252).max())).shift(5)

def hygr_147_valuation_compression_21d(ps: pd.Series) -> pd.Series:
    """hygr_147_valuation_compression_21d"""
    return (_safe_div(ps, ps.rolling(252).max())).shift(21)

def hygr_148_valuation_compression_63d(ps: pd.Series) -> pd.Series:
    """hygr_148_valuation_compression_63d"""
    return (_safe_div(ps, ps.rolling(252).max())).shift(63)

def hygr_149_valuation_compression_126d(ps: pd.Series) -> pd.Series:
    """hygr_149_valuation_compression_126d"""
    return (_safe_div(ps, ps.rolling(252).max())).shift(126)

def hygr_150_valuation_compression_252d(ps: pd.Series) -> pd.Series:
    """hygr_150_valuation_compression_252d"""
    return (_safe_div(ps, ps.rolling(252).max())).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V61_REGISTRY = {
    "hygr_076_rule40_z_5d": {"inputs": ['revenue', 'ebitda'], "func": hygr_076_rule40_z_5d},
    "hygr_077_rule40_z_21d": {"inputs": ['revenue', 'ebitda'], "func": hygr_077_rule40_z_21d},
    "hygr_078_rule40_z_63d": {"inputs": ['revenue', 'ebitda'], "func": hygr_078_rule40_z_63d},
    "hygr_079_rule40_z_126d": {"inputs": ['revenue', 'ebitda'], "func": hygr_079_rule40_z_126d},
    "hygr_080_rule40_z_252d": {"inputs": ['revenue', 'ebitda'], "func": hygr_080_rule40_z_252d},
    "hygr_081_rev_p_mc_5d": {"inputs": ['revenue', 'marketcap'], "func": hygr_081_rev_p_mc_5d},
    "hygr_082_rev_p_mc_21d": {"inputs": ['revenue', 'marketcap'], "func": hygr_082_rev_p_mc_21d},
    "hygr_083_rev_p_mc_63d": {"inputs": ['revenue', 'marketcap'], "func": hygr_083_rev_p_mc_63d},
    "hygr_084_rev_p_mc_126d": {"inputs": ['revenue', 'marketcap'], "func": hygr_084_rev_p_mc_126d},
    "hygr_085_rev_p_mc_252d": {"inputs": ['revenue', 'marketcap'], "func": hygr_085_rev_p_mc_252d},
    "hygr_086_hg_persistence_5d": {"inputs": ['revenue'], "func": hygr_086_hg_persistence_5d},
    "hygr_087_hg_persistence_21d": {"inputs": ['revenue'], "func": hygr_087_hg_persistence_21d},
    "hygr_088_hg_persistence_63d": {"inputs": ['revenue'], "func": hygr_088_hg_persistence_63d},
    "hygr_089_hg_persistence_126d": {"inputs": ['revenue'], "func": hygr_089_hg_persistence_126d},
    "hygr_090_hg_persistence_252d": {"inputs": ['revenue'], "func": hygr_090_hg_persistence_252d},
    "hygr_091_log_rev_5d": {"inputs": ['revenue'], "func": hygr_091_log_rev_5d},
    "hygr_092_log_rev_21d": {"inputs": ['revenue'], "func": hygr_092_log_rev_21d},
    "hygr_093_log_rev_63d": {"inputs": ['revenue'], "func": hygr_093_log_rev_63d},
    "hygr_094_log_rev_126d": {"inputs": ['revenue'], "func": hygr_094_log_rev_126d},
    "hygr_095_log_rev_252d": {"inputs": ['revenue'], "func": hygr_095_log_rev_252d},
    "hygr_096_rev_g_accel_5d": {"inputs": ['revenue'], "func": hygr_096_rev_g_accel_5d},
    "hygr_097_rev_g_accel_21d": {"inputs": ['revenue'], "func": hygr_097_rev_g_accel_21d},
    "hygr_098_rev_g_accel_63d": {"inputs": ['revenue'], "func": hygr_098_rev_g_accel_63d},
    "hygr_099_rev_g_accel_126d": {"inputs": ['revenue'], "func": hygr_099_rev_g_accel_126d},
    "hygr_100_rev_g_accel_252d": {"inputs": ['revenue'], "func": hygr_100_rev_g_accel_252d},
    "hygr_101_fcf_m_5d": {"inputs": ['revenue', 'fcf'], "func": hygr_101_fcf_m_5d},
    "hygr_102_fcf_m_21d": {"inputs": ['revenue', 'fcf'], "func": hygr_102_fcf_m_21d},
    "hygr_103_fcf_m_63d": {"inputs": ['revenue', 'fcf'], "func": hygr_103_fcf_m_63d},
    "hygr_104_fcf_m_126d": {"inputs": ['revenue', 'fcf'], "func": hygr_104_fcf_m_126d},
    "hygr_105_fcf_m_252d": {"inputs": ['revenue', 'fcf'], "func": hygr_105_fcf_m_252d},
    "hygr_106_ebitda_m_5d": {"inputs": ['revenue', 'ebitda'], "func": hygr_106_ebitda_m_5d},
    "hygr_107_ebitda_m_21d": {"inputs": ['revenue', 'ebitda'], "func": hygr_107_ebitda_m_21d},
    "hygr_108_ebitda_m_63d": {"inputs": ['revenue', 'ebitda'], "func": hygr_108_ebitda_m_63d},
    "hygr_109_ebitda_m_126d": {"inputs": ['revenue', 'ebitda'], "func": hygr_109_ebitda_m_126d},
    "hygr_110_ebitda_m_252d": {"inputs": ['revenue', 'ebitda'], "func": hygr_110_ebitda_m_252d},
    "hygr_111_ni_m_5d": {"inputs": ['revenue', 'netinc'], "func": hygr_111_ni_m_5d},
    "hygr_112_ni_m_21d": {"inputs": ['revenue', 'netinc'], "func": hygr_112_ni_m_21d},
    "hygr_113_ni_m_63d": {"inputs": ['revenue', 'netinc'], "func": hygr_113_ni_m_63d},
    "hygr_114_ni_m_126d": {"inputs": ['revenue', 'netinc'], "func": hygr_114_ni_m_126d},
    "hygr_115_ni_m_252d": {"inputs": ['revenue', 'netinc'], "func": hygr_115_ni_m_252d},
    "hygr_116_capex_rev_5d": {"inputs": ['revenue', 'capex'], "func": hygr_116_capex_rev_5d},
    "hygr_117_capex_rev_21d": {"inputs": ['revenue', 'capex'], "func": hygr_117_capex_rev_21d},
    "hygr_118_capex_rev_63d": {"inputs": ['revenue', 'capex'], "func": hygr_118_capex_rev_63d},
    "hygr_119_capex_rev_126d": {"inputs": ['revenue', 'capex'], "func": hygr_119_capex_rev_126d},
    "hygr_120_capex_rev_252d": {"inputs": ['revenue', 'capex'], "func": hygr_120_capex_rev_252d},
    "hygr_121_asset_turn_5d": {"inputs": ['revenue', 'assets'], "func": hygr_121_asset_turn_5d},
    "hygr_122_asset_turn_21d": {"inputs": ['revenue', 'assets'], "func": hygr_122_asset_turn_21d},
    "hygr_123_asset_turn_63d": {"inputs": ['revenue', 'assets'], "func": hygr_123_asset_turn_63d},
    "hygr_124_asset_turn_126d": {"inputs": ['revenue', 'assets'], "func": hygr_124_asset_turn_126d},
    "hygr_125_asset_turn_252d": {"inputs": ['revenue', 'assets'], "func": hygr_125_asset_turn_252d},
    "hygr_126_roe_5d": {"inputs": ['netinc', 'equity'], "func": hygr_126_roe_5d},
    "hygr_127_roe_21d": {"inputs": ['netinc', 'equity'], "func": hygr_127_roe_21d},
    "hygr_128_roe_63d": {"inputs": ['netinc', 'equity'], "func": hygr_128_roe_63d},
    "hygr_129_roe_126d": {"inputs": ['netinc', 'equity'], "func": hygr_129_roe_126d},
    "hygr_130_roe_252d": {"inputs": ['netinc', 'equity'], "func": hygr_130_roe_252d},
    "hygr_131_roic_5d": {"inputs": ['ebit', 'assets', 'cashnequiv'], "func": hygr_131_roic_5d},
    "hygr_132_roic_21d": {"inputs": ['ebit', 'assets', 'cashnequiv'], "func": hygr_132_roic_21d},
    "hygr_133_roic_63d": {"inputs": ['ebit', 'assets', 'cashnequiv'], "func": hygr_133_roic_63d},
    "hygr_134_roic_126d": {"inputs": ['ebit', 'assets', 'cashnequiv'], "func": hygr_134_roic_126d},
    "hygr_135_roic_252d": {"inputs": ['ebit', 'assets', 'cashnequiv'], "func": hygr_135_roic_252d},
    "hygr_136_rev_per_share_g_5d": {"inputs": ['revenue', 'shareswa'], "func": hygr_136_rev_per_share_g_5d},
    "hygr_137_rev_per_share_g_21d": {"inputs": ['revenue', 'shareswa'], "func": hygr_137_rev_per_share_g_21d},
    "hygr_138_rev_per_share_g_63d": {"inputs": ['revenue', 'shareswa'], "func": hygr_138_rev_per_share_g_63d},
    "hygr_139_rev_per_share_g_126d": {"inputs": ['revenue', 'shareswa'], "func": hygr_139_rev_per_share_g_126d},
    "hygr_140_rev_per_share_g_252d": {"inputs": ['revenue', 'shareswa'], "func": hygr_140_rev_per_share_g_252d},
    "hygr_141_market_share_proxy_5d": {"inputs": ['revenue'], "func": hygr_141_market_share_proxy_5d},
    "hygr_142_market_share_proxy_21d": {"inputs": ['revenue'], "func": hygr_142_market_share_proxy_21d},
    "hygr_143_market_share_proxy_63d": {"inputs": ['revenue'], "func": hygr_143_market_share_proxy_63d},
    "hygr_144_market_share_proxy_126d": {"inputs": ['revenue'], "func": hygr_144_market_share_proxy_126d},
    "hygr_145_market_share_proxy_252d": {"inputs": ['revenue'], "func": hygr_145_market_share_proxy_252d},
    "hygr_146_valuation_compression_5d": {"inputs": ['ps'], "func": hygr_146_valuation_compression_5d},
    "hygr_147_valuation_compression_21d": {"inputs": ['ps'], "func": hygr_147_valuation_compression_21d},
    "hygr_148_valuation_compression_63d": {"inputs": ['ps'], "func": hygr_148_valuation_compression_63d},
    "hygr_149_valuation_compression_126d": {"inputs": ['ps'], "func": hygr_149_valuation_compression_126d},
    "hygr_150_valuation_compression_252d": {"inputs": ['ps'], "func": hygr_150_valuation_compression_252d},
}
