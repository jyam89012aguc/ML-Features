"""
67_moat_trajectory — Base Features 076-150
Domain: ROIC persistence, Margin leadership
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

def moat_076_roic_accel_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_076_roic_accel_5d"""
    return ((_safe_div(ebit, assets)).diff(252).diff(63)).shift(5)

def moat_077_roic_accel_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_077_roic_accel_21d"""
    return ((_safe_div(ebit, assets)).diff(252).diff(63)).shift(21)

def moat_078_roic_accel_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_078_roic_accel_63d"""
    return ((_safe_div(ebit, assets)).diff(252).diff(63)).shift(63)

def moat_079_roic_accel_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_079_roic_accel_126d"""
    return ((_safe_div(ebit, assets)).diff(252).diff(63)).shift(126)

def moat_080_roic_accel_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_080_roic_accel_252d"""
    return ((_safe_div(ebit, assets)).diff(252).diff(63)).shift(252)

def moat_081_roe_accel_5d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_081_roe_accel_5d"""
    return ((_safe_div(netinc, equity)).diff(252).diff(63)).shift(5)

def moat_082_roe_accel_21d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_082_roe_accel_21d"""
    return ((_safe_div(netinc, equity)).diff(252).diff(63)).shift(21)

def moat_083_roe_accel_63d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_083_roe_accel_63d"""
    return ((_safe_div(netinc, equity)).diff(252).diff(63)).shift(63)

def moat_084_roe_accel_126d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_084_roe_accel_126d"""
    return ((_safe_div(netinc, equity)).diff(252).diff(63)).shift(126)

def moat_085_roe_accel_252d(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """moat_085_roe_accel_252d"""
    return ((_safe_div(netinc, equity)).diff(252).diff(63)).shift(252)

def moat_086_margin_accel_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_086_margin_accel_5d"""
    return ((_safe_div(ebit, revenue)).diff(252).diff(63)).shift(5)

def moat_087_margin_accel_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_087_margin_accel_21d"""
    return ((_safe_div(ebit, revenue)).diff(252).diff(63)).shift(21)

def moat_088_margin_accel_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_088_margin_accel_63d"""
    return ((_safe_div(ebit, revenue)).diff(252).diff(63)).shift(63)

def moat_089_margin_accel_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_089_margin_accel_126d"""
    return ((_safe_div(ebit, revenue)).diff(252).diff(63)).shift(126)

def moat_090_margin_accel_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """moat_090_margin_accel_252d"""
    return ((_safe_div(ebit, revenue)).diff(252).diff(63)).shift(252)

def moat_091_asset_turn_accel_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_091_asset_turn_accel_5d"""
    return ((_safe_div(revenue, assets)).diff(252).diff(63)).shift(5)

def moat_092_asset_turn_accel_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_092_asset_turn_accel_21d"""
    return ((_safe_div(revenue, assets)).diff(252).diff(63)).shift(21)

def moat_093_asset_turn_accel_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_093_asset_turn_accel_63d"""
    return ((_safe_div(revenue, assets)).diff(252).diff(63)).shift(63)

def moat_094_asset_turn_accel_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_094_asset_turn_accel_126d"""
    return ((_safe_div(revenue, assets)).diff(252).diff(63)).shift(126)

def moat_095_asset_turn_accel_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_095_asset_turn_accel_252d"""
    return ((_safe_div(revenue, assets)).diff(252).diff(63)).shift(252)

def moat_096_competitive_advantage_score_5d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_096_competitive_advantage_score_5d"""
    return (_safe_div(ebit, sga + rnd)).shift(5)

def moat_097_competitive_advantage_score_21d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_097_competitive_advantage_score_21d"""
    return (_safe_div(ebit, sga + rnd)).shift(21)

def moat_098_competitive_advantage_score_63d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_098_competitive_advantage_score_63d"""
    return (_safe_div(ebit, sga + rnd)).shift(63)

def moat_099_competitive_advantage_score_126d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_099_competitive_advantage_score_126d"""
    return (_safe_div(ebit, sga + rnd)).shift(126)

def moat_100_competitive_advantage_score_252d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_100_competitive_advantage_score_252d"""
    return (_safe_div(ebit, sga + rnd)).shift(252)

def moat_101_market_dominance_proxy_5d(revenue: pd.Series) -> pd.Series:
    """moat_101_market_dominance_proxy_5d"""
    return (_safe_div(revenue, revenue.rolling(1260).mean())).shift(5)

def moat_102_market_dominance_proxy_21d(revenue: pd.Series) -> pd.Series:
    """moat_102_market_dominance_proxy_21d"""
    return (_safe_div(revenue, revenue.rolling(1260).mean())).shift(21)

def moat_103_market_dominance_proxy_63d(revenue: pd.Series) -> pd.Series:
    """moat_103_market_dominance_proxy_63d"""
    return (_safe_div(revenue, revenue.rolling(1260).mean())).shift(63)

def moat_104_market_dominance_proxy_126d(revenue: pd.Series) -> pd.Series:
    """moat_104_market_dominance_proxy_126d"""
    return (_safe_div(revenue, revenue.rolling(1260).mean())).shift(126)

def moat_105_market_dominance_proxy_252d(revenue: pd.Series) -> pd.Series:
    """moat_105_market_dominance_proxy_252d"""
    return (_safe_div(revenue, revenue.rolling(1260).mean())).shift(252)

def moat_106_profit_retention_5d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """moat_106_profit_retention_5d"""
    return (1 - _safe_div(taxexp, ebt)).shift(5)

def moat_107_profit_retention_21d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """moat_107_profit_retention_21d"""
    return (1 - _safe_div(taxexp, ebt)).shift(21)

def moat_108_profit_retention_63d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """moat_108_profit_retention_63d"""
    return (1 - _safe_div(taxexp, ebt)).shift(63)

def moat_109_profit_retention_126d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """moat_109_profit_retention_126d"""
    return (1 - _safe_div(taxexp, ebt)).shift(126)

def moat_110_profit_retention_252d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """moat_110_profit_retention_252d"""
    return (1 - _safe_div(taxexp, ebt)).shift(252)

def moat_111_reinvestment_rat_5d(capex: pd.Series) -> pd.Series:
    """moat_111_reinvestment_rat_5d"""
    return (_safe_div(capex, depamor)).shift(5)

def moat_112_reinvestment_rat_21d(capex: pd.Series) -> pd.Series:
    """moat_112_reinvestment_rat_21d"""
    return (_safe_div(capex, depamor)).shift(21)

def moat_113_reinvestment_rat_63d(capex: pd.Series) -> pd.Series:
    """moat_113_reinvestment_rat_63d"""
    return (_safe_div(capex, depamor)).shift(63)

def moat_114_reinvestment_rat_126d(capex: pd.Series) -> pd.Series:
    """moat_114_reinvestment_rat_126d"""
    return (_safe_div(capex, depamor)).shift(126)

def moat_115_reinvestment_rat_252d(capex: pd.Series) -> pd.Series:
    """moat_115_reinvestment_rat_252d"""
    return (_safe_div(capex, depamor)).shift(252)

def moat_116_moat_decay_index_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_116_moat_decay_index_5d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(5)

def moat_117_moat_decay_index_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_117_moat_decay_index_21d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(21)

def moat_118_moat_decay_index_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_118_moat_decay_index_63d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(63)

def moat_119_moat_decay_index_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_119_moat_decay_index_126d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(126)

def moat_120_moat_decay_index_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_120_moat_decay_index_252d"""
    return ((_safe_div(ebit, assets)).diff(1260)).shift(252)

def moat_121_brand_power_proxy_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """moat_121_brand_power_proxy_5d"""
    return (_safe_div(revenue, sga)).shift(5)

def moat_122_brand_power_proxy_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """moat_122_brand_power_proxy_21d"""
    return (_safe_div(revenue, sga)).shift(21)

def moat_123_brand_power_proxy_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """moat_123_brand_power_proxy_63d"""
    return (_safe_div(revenue, sga)).shift(63)

def moat_124_brand_power_proxy_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """moat_124_brand_power_proxy_126d"""
    return (_safe_div(revenue, sga)).shift(126)

def moat_125_brand_power_proxy_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """moat_125_brand_power_proxy_252d"""
    return (_safe_div(revenue, sga)).shift(252)

def moat_126_r_and_d_moat_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_126_r_and_d_moat_5d"""
    return (_safe_div(rnd, revenue)).shift(5)

def moat_127_r_and_d_moat_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_127_r_and_d_moat_21d"""
    return (_safe_div(rnd, revenue)).shift(21)

def moat_128_r_and_d_moat_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_128_r_and_d_moat_63d"""
    return (_safe_div(rnd, revenue)).shift(63)

def moat_129_r_and_d_moat_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_129_r_and_d_moat_126d"""
    return (_safe_div(rnd, revenue)).shift(126)

def moat_130_r_and_d_moat_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """moat_130_r_and_d_moat_252d"""
    return (_safe_div(rnd, revenue)).shift(252)

def moat_131_capex_moat_5d(capex: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_131_capex_moat_5d"""
    return (_safe_div(capex, assets)).shift(5)

def moat_132_capex_moat_21d(capex: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_132_capex_moat_21d"""
    return (_safe_div(capex, assets)).shift(21)

def moat_133_capex_moat_63d(capex: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_133_capex_moat_63d"""
    return (_safe_div(capex, assets)).shift(63)

def moat_134_capex_moat_126d(capex: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_134_capex_moat_126d"""
    return (_safe_div(capex, assets)).shift(126)

def moat_135_capex_moat_252d(capex: pd.Series, assets: pd.Series) -> pd.Series:
    """moat_135_capex_moat_252d"""
    return (_safe_div(capex, assets)).shift(252)

def moat_136_intangible_moat_5d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """moat_136_intangible_moat_5d"""
    return (_safe_div(assets - ppnent - currentassets, assets)).shift(5)

def moat_137_intangible_moat_21d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """moat_137_intangible_moat_21d"""
    return (_safe_div(assets - ppnent - currentassets, assets)).shift(21)

def moat_138_intangible_moat_63d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """moat_138_intangible_moat_63d"""
    return (_safe_div(assets - ppnent - currentassets, assets)).shift(63)

def moat_139_intangible_moat_126d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """moat_139_intangible_moat_126d"""
    return (_safe_div(assets - ppnent - currentassets, assets)).shift(126)

def moat_140_intangible_moat_252d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """moat_140_intangible_moat_252d"""
    return (_safe_div(assets - ppnent - currentassets, assets)).shift(252)

def moat_141_pricing_power_moat_5d(gp: pd.Series, cor: pd.Series) -> pd.Series:
    """moat_141_pricing_power_moat_5d"""
    return (_safe_div(gp, cor)).shift(5)

def moat_142_pricing_power_moat_21d(gp: pd.Series, cor: pd.Series) -> pd.Series:
    """moat_142_pricing_power_moat_21d"""
    return (_safe_div(gp, cor)).shift(21)

def moat_143_pricing_power_moat_63d(gp: pd.Series, cor: pd.Series) -> pd.Series:
    """moat_143_pricing_power_moat_63d"""
    return (_safe_div(gp, cor)).shift(63)

def moat_144_pricing_power_moat_126d(gp: pd.Series, cor: pd.Series) -> pd.Series:
    """moat_144_pricing_power_moat_126d"""
    return (_safe_div(gp, cor)).shift(126)

def moat_145_pricing_power_moat_252d(gp: pd.Series, cor: pd.Series) -> pd.Series:
    """moat_145_pricing_power_moat_252d"""
    return (_safe_div(gp, cor)).shift(252)

def moat_146_scale_moat_5d(assets: pd.Series) -> pd.Series:
    """moat_146_scale_moat_5d"""
    return (np.log1p(assets)).shift(5)

def moat_147_scale_moat_21d(assets: pd.Series) -> pd.Series:
    """moat_147_scale_moat_21d"""
    return (np.log1p(assets)).shift(21)

def moat_148_scale_moat_63d(assets: pd.Series) -> pd.Series:
    """moat_148_scale_moat_63d"""
    return (np.log1p(assets)).shift(63)

def moat_149_scale_moat_126d(assets: pd.Series) -> pd.Series:
    """moat_149_scale_moat_126d"""
    return (np.log1p(assets)).shift(126)

def moat_150_scale_moat_252d(assets: pd.Series) -> pd.Series:
    """moat_150_scale_moat_252d"""
    return (np.log1p(assets)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V67_REGISTRY = {
    "moat_076_roic_accel_5d": {"inputs": ['ebit', 'assets'], "func": moat_076_roic_accel_5d},
    "moat_077_roic_accel_21d": {"inputs": ['ebit', 'assets'], "func": moat_077_roic_accel_21d},
    "moat_078_roic_accel_63d": {"inputs": ['ebit', 'assets'], "func": moat_078_roic_accel_63d},
    "moat_079_roic_accel_126d": {"inputs": ['ebit', 'assets'], "func": moat_079_roic_accel_126d},
    "moat_080_roic_accel_252d": {"inputs": ['ebit', 'assets'], "func": moat_080_roic_accel_252d},
    "moat_081_roe_accel_5d": {"inputs": ['netinc', 'equity'], "func": moat_081_roe_accel_5d},
    "moat_082_roe_accel_21d": {"inputs": ['netinc', 'equity'], "func": moat_082_roe_accel_21d},
    "moat_083_roe_accel_63d": {"inputs": ['netinc', 'equity'], "func": moat_083_roe_accel_63d},
    "moat_084_roe_accel_126d": {"inputs": ['netinc', 'equity'], "func": moat_084_roe_accel_126d},
    "moat_085_roe_accel_252d": {"inputs": ['netinc', 'equity'], "func": moat_085_roe_accel_252d},
    "moat_086_margin_accel_5d": {"inputs": ['revenue', 'ebit'], "func": moat_086_margin_accel_5d},
    "moat_087_margin_accel_21d": {"inputs": ['revenue', 'ebit'], "func": moat_087_margin_accel_21d},
    "moat_088_margin_accel_63d": {"inputs": ['revenue', 'ebit'], "func": moat_088_margin_accel_63d},
    "moat_089_margin_accel_126d": {"inputs": ['revenue', 'ebit'], "func": moat_089_margin_accel_126d},
    "moat_090_margin_accel_252d": {"inputs": ['revenue', 'ebit'], "func": moat_090_margin_accel_252d},
    "moat_091_asset_turn_accel_5d": {"inputs": ['revenue', 'assets'], "func": moat_091_asset_turn_accel_5d},
    "moat_092_asset_turn_accel_21d": {"inputs": ['revenue', 'assets'], "func": moat_092_asset_turn_accel_21d},
    "moat_093_asset_turn_accel_63d": {"inputs": ['revenue', 'assets'], "func": moat_093_asset_turn_accel_63d},
    "moat_094_asset_turn_accel_126d": {"inputs": ['revenue', 'assets'], "func": moat_094_asset_turn_accel_126d},
    "moat_095_asset_turn_accel_252d": {"inputs": ['revenue', 'assets'], "func": moat_095_asset_turn_accel_252d},
    "moat_096_competitive_advantage_score_5d": {"inputs": ['ebit', 'sga', 'rnd'], "func": moat_096_competitive_advantage_score_5d},
    "moat_097_competitive_advantage_score_21d": {"inputs": ['ebit', 'sga', 'rnd'], "func": moat_097_competitive_advantage_score_21d},
    "moat_098_competitive_advantage_score_63d": {"inputs": ['ebit', 'sga', 'rnd'], "func": moat_098_competitive_advantage_score_63d},
    "moat_099_competitive_advantage_score_126d": {"inputs": ['ebit', 'sga', 'rnd'], "func": moat_099_competitive_advantage_score_126d},
    "moat_100_competitive_advantage_score_252d": {"inputs": ['ebit', 'sga', 'rnd'], "func": moat_100_competitive_advantage_score_252d},
    "moat_101_market_dominance_proxy_5d": {"inputs": ['revenue'], "func": moat_101_market_dominance_proxy_5d},
    "moat_102_market_dominance_proxy_21d": {"inputs": ['revenue'], "func": moat_102_market_dominance_proxy_21d},
    "moat_103_market_dominance_proxy_63d": {"inputs": ['revenue'], "func": moat_103_market_dominance_proxy_63d},
    "moat_104_market_dominance_proxy_126d": {"inputs": ['revenue'], "func": moat_104_market_dominance_proxy_126d},
    "moat_105_market_dominance_proxy_252d": {"inputs": ['revenue'], "func": moat_105_market_dominance_proxy_252d},
    "moat_106_profit_retention_5d": {"inputs": ['taxexp', 'ebt'], "func": moat_106_profit_retention_5d},
    "moat_107_profit_retention_21d": {"inputs": ['taxexp', 'ebt'], "func": moat_107_profit_retention_21d},
    "moat_108_profit_retention_63d": {"inputs": ['taxexp', 'ebt'], "func": moat_108_profit_retention_63d},
    "moat_109_profit_retention_126d": {"inputs": ['taxexp', 'ebt'], "func": moat_109_profit_retention_126d},
    "moat_110_profit_retention_252d": {"inputs": ['taxexp', 'ebt'], "func": moat_110_profit_retention_252d},
    "moat_111_reinvestment_rat_5d": {"inputs": ['capex'], "func": moat_111_reinvestment_rat_5d},
    "moat_112_reinvestment_rat_21d": {"inputs": ['capex'], "func": moat_112_reinvestment_rat_21d},
    "moat_113_reinvestment_rat_63d": {"inputs": ['capex'], "func": moat_113_reinvestment_rat_63d},
    "moat_114_reinvestment_rat_126d": {"inputs": ['capex'], "func": moat_114_reinvestment_rat_126d},
    "moat_115_reinvestment_rat_252d": {"inputs": ['capex'], "func": moat_115_reinvestment_rat_252d},
    "moat_116_moat_decay_index_5d": {"inputs": ['ebit', 'assets'], "func": moat_116_moat_decay_index_5d},
    "moat_117_moat_decay_index_21d": {"inputs": ['ebit', 'assets'], "func": moat_117_moat_decay_index_21d},
    "moat_118_moat_decay_index_63d": {"inputs": ['ebit', 'assets'], "func": moat_118_moat_decay_index_63d},
    "moat_119_moat_decay_index_126d": {"inputs": ['ebit', 'assets'], "func": moat_119_moat_decay_index_126d},
    "moat_120_moat_decay_index_252d": {"inputs": ['ebit', 'assets'], "func": moat_120_moat_decay_index_252d},
    "moat_121_brand_power_proxy_5d": {"inputs": ['revenue', 'sga'], "func": moat_121_brand_power_proxy_5d},
    "moat_122_brand_power_proxy_21d": {"inputs": ['revenue', 'sga'], "func": moat_122_brand_power_proxy_21d},
    "moat_123_brand_power_proxy_63d": {"inputs": ['revenue', 'sga'], "func": moat_123_brand_power_proxy_63d},
    "moat_124_brand_power_proxy_126d": {"inputs": ['revenue', 'sga'], "func": moat_124_brand_power_proxy_126d},
    "moat_125_brand_power_proxy_252d": {"inputs": ['revenue', 'sga'], "func": moat_125_brand_power_proxy_252d},
    "moat_126_r_and_d_moat_5d": {"inputs": ['revenue', 'rnd'], "func": moat_126_r_and_d_moat_5d},
    "moat_127_r_and_d_moat_21d": {"inputs": ['revenue', 'rnd'], "func": moat_127_r_and_d_moat_21d},
    "moat_128_r_and_d_moat_63d": {"inputs": ['revenue', 'rnd'], "func": moat_128_r_and_d_moat_63d},
    "moat_129_r_and_d_moat_126d": {"inputs": ['revenue', 'rnd'], "func": moat_129_r_and_d_moat_126d},
    "moat_130_r_and_d_moat_252d": {"inputs": ['revenue', 'rnd'], "func": moat_130_r_and_d_moat_252d},
    "moat_131_capex_moat_5d": {"inputs": ['capex', 'assets'], "func": moat_131_capex_moat_5d},
    "moat_132_capex_moat_21d": {"inputs": ['capex', 'assets'], "func": moat_132_capex_moat_21d},
    "moat_133_capex_moat_63d": {"inputs": ['capex', 'assets'], "func": moat_133_capex_moat_63d},
    "moat_134_capex_moat_126d": {"inputs": ['capex', 'assets'], "func": moat_134_capex_moat_126d},
    "moat_135_capex_moat_252d": {"inputs": ['capex', 'assets'], "func": moat_135_capex_moat_252d},
    "moat_136_intangible_moat_5d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": moat_136_intangible_moat_5d},
    "moat_137_intangible_moat_21d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": moat_137_intangible_moat_21d},
    "moat_138_intangible_moat_63d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": moat_138_intangible_moat_63d},
    "moat_139_intangible_moat_126d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": moat_139_intangible_moat_126d},
    "moat_140_intangible_moat_252d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": moat_140_intangible_moat_252d},
    "moat_141_pricing_power_moat_5d": {"inputs": ['gp', 'cor'], "func": moat_141_pricing_power_moat_5d},
    "moat_142_pricing_power_moat_21d": {"inputs": ['gp', 'cor'], "func": moat_142_pricing_power_moat_21d},
    "moat_143_pricing_power_moat_63d": {"inputs": ['gp', 'cor'], "func": moat_143_pricing_power_moat_63d},
    "moat_144_pricing_power_moat_126d": {"inputs": ['gp', 'cor'], "func": moat_144_pricing_power_moat_126d},
    "moat_145_pricing_power_moat_252d": {"inputs": ['gp', 'cor'], "func": moat_145_pricing_power_moat_252d},
    "moat_146_scale_moat_5d": {"inputs": ['assets'], "func": moat_146_scale_moat_5d},
    "moat_147_scale_moat_21d": {"inputs": ['assets'], "func": moat_147_scale_moat_21d},
    "moat_148_scale_moat_63d": {"inputs": ['assets'], "func": moat_148_scale_moat_63d},
    "moat_149_scale_moat_126d": {"inputs": ['assets'], "func": moat_149_scale_moat_126d},
    "moat_150_scale_moat_252d": {"inputs": ['assets'], "func": moat_150_scale_moat_252d},
}
