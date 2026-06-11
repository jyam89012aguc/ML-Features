"""
65_pricing_power_signal — Base Features 076-150
Domain: Margin stability vs Cost growth
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

def prpw_076_rev_z_5d(revenue: pd.Series) -> pd.Series:
    """prpw_076_rev_z_5d"""
    return (_zscore_rolling(revenue, 1260)).shift(5)

def prpw_077_rev_z_21d(revenue: pd.Series) -> pd.Series:
    """prpw_077_rev_z_21d"""
    return (_zscore_rolling(revenue, 1260)).shift(21)

def prpw_078_rev_z_63d(revenue: pd.Series) -> pd.Series:
    """prpw_078_rev_z_63d"""
    return (_zscore_rolling(revenue, 1260)).shift(63)

def prpw_079_rev_z_126d(revenue: pd.Series) -> pd.Series:
    """prpw_079_rev_z_126d"""
    return (_zscore_rolling(revenue, 1260)).shift(126)

def prpw_080_rev_z_252d(revenue: pd.Series) -> pd.Series:
    """prpw_080_rev_z_252d"""
    return (_zscore_rolling(revenue, 1260)).shift(252)

def prpw_081_gp_m_z_5d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_081_gp_m_z_5d"""
    return (_zscore_rolling(_safe_div(gp, revenue), 1260)).shift(5)

def prpw_082_gp_m_z_21d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_082_gp_m_z_21d"""
    return (_zscore_rolling(_safe_div(gp, revenue), 1260)).shift(21)

def prpw_083_gp_m_z_63d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_083_gp_m_z_63d"""
    return (_zscore_rolling(_safe_div(gp, revenue), 1260)).shift(63)

def prpw_084_gp_m_z_126d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_084_gp_m_z_126d"""
    return (_zscore_rolling(_safe_div(gp, revenue), 1260)).shift(126)

def prpw_085_gp_m_z_252d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_085_gp_m_z_252d"""
    return (_zscore_rolling(_safe_div(gp, revenue), 1260)).shift(252)

def prpw_086_ebit_m_z_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_086_ebit_m_z_5d"""
    return (_zscore_rolling(_safe_div(ebit, revenue), 1260)).shift(5)

def prpw_087_ebit_m_z_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_087_ebit_m_z_21d"""
    return (_zscore_rolling(_safe_div(ebit, revenue), 1260)).shift(21)

def prpw_088_ebit_m_z_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_088_ebit_m_z_63d"""
    return (_zscore_rolling(_safe_div(ebit, revenue), 1260)).shift(63)

def prpw_089_ebit_m_z_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_089_ebit_m_z_126d"""
    return (_zscore_rolling(_safe_div(ebit, revenue), 1260)).shift(126)

def prpw_090_ebit_m_z_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_090_ebit_m_z_252d"""
    return (_zscore_rolling(_safe_div(ebit, revenue), 1260)).shift(252)

def prpw_091_cor_rev_z_5d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_091_cor_rev_z_5d"""
    return (_zscore_rolling(_safe_div(cor, revenue), 1260)).shift(5)

def prpw_092_cor_rev_z_21d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_092_cor_rev_z_21d"""
    return (_zscore_rolling(_safe_div(cor, revenue), 1260)).shift(21)

def prpw_093_cor_rev_z_63d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_093_cor_rev_z_63d"""
    return (_zscore_rolling(_safe_div(cor, revenue), 1260)).shift(63)

def prpw_094_cor_rev_z_126d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_094_cor_rev_z_126d"""
    return (_zscore_rolling(_safe_div(cor, revenue), 1260)).shift(126)

def prpw_095_cor_rev_z_252d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_095_cor_rev_z_252d"""
    return (_zscore_rolling(_safe_div(cor, revenue), 1260)).shift(252)

def prpw_096_markup_proxy_5d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_096_markup_proxy_5d"""
    return (_safe_div(revenue, cor)).shift(5)

def prpw_097_markup_proxy_21d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_097_markup_proxy_21d"""
    return (_safe_div(revenue, cor)).shift(21)

def prpw_098_markup_proxy_63d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_098_markup_proxy_63d"""
    return (_safe_div(revenue, cor)).shift(63)

def prpw_099_markup_proxy_126d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_099_markup_proxy_126d"""
    return (_safe_div(revenue, cor)).shift(126)

def prpw_100_markup_proxy_252d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_100_markup_proxy_252d"""
    return (_safe_div(revenue, cor)).shift(252)

def prpw_101_operating_efficiency_5d(revenue: pd.Series, cor: pd.Series, sga: pd.Series) -> pd.Series:
    """prpw_101_operating_efficiency_5d"""
    return (_safe_div(revenue, sga + cor)).shift(5)

def prpw_102_operating_efficiency_21d(revenue: pd.Series, cor: pd.Series, sga: pd.Series) -> pd.Series:
    """prpw_102_operating_efficiency_21d"""
    return (_safe_div(revenue, sga + cor)).shift(21)

def prpw_103_operating_efficiency_63d(revenue: pd.Series, cor: pd.Series, sga: pd.Series) -> pd.Series:
    """prpw_103_operating_efficiency_63d"""
    return (_safe_div(revenue, sga + cor)).shift(63)

def prpw_104_operating_efficiency_126d(revenue: pd.Series, cor: pd.Series, sga: pd.Series) -> pd.Series:
    """prpw_104_operating_efficiency_126d"""
    return (_safe_div(revenue, sga + cor)).shift(126)

def prpw_105_operating_efficiency_252d(revenue: pd.Series, cor: pd.Series, sga: pd.Series) -> pd.Series:
    """prpw_105_operating_efficiency_252d"""
    return (_safe_div(revenue, sga + cor)).shift(252)

def prpw_106_incremental_margin_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_106_incremental_margin_5d"""
    return (_safe_div(ebit.diff(252), revenue.diff(252))).shift(5)

def prpw_107_incremental_margin_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_107_incremental_margin_21d"""
    return (_safe_div(ebit.diff(252), revenue.diff(252))).shift(21)

def prpw_108_incremental_margin_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_108_incremental_margin_63d"""
    return (_safe_div(ebit.diff(252), revenue.diff(252))).shift(63)

def prpw_109_incremental_margin_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_109_incremental_margin_126d"""
    return (_safe_div(ebit.diff(252), revenue.diff(252))).shift(126)

def prpw_110_incremental_margin_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """prpw_110_incremental_margin_252d"""
    return (_safe_div(ebit.diff(252), revenue.diff(252))).shift(252)

def prpw_111_gp_growth_vel_5d(gp: pd.Series) -> pd.Series:
    """prpw_111_gp_growth_vel_5d"""
    return (gp.pct_change(252).diff(63)).shift(5)

def prpw_112_gp_growth_vel_21d(gp: pd.Series) -> pd.Series:
    """prpw_112_gp_growth_vel_21d"""
    return (gp.pct_change(252).diff(63)).shift(21)

def prpw_113_gp_growth_vel_63d(gp: pd.Series) -> pd.Series:
    """prpw_113_gp_growth_vel_63d"""
    return (gp.pct_change(252).diff(63)).shift(63)

def prpw_114_gp_growth_vel_126d(gp: pd.Series) -> pd.Series:
    """prpw_114_gp_growth_vel_126d"""
    return (gp.pct_change(252).diff(63)).shift(126)

def prpw_115_gp_growth_vel_252d(gp: pd.Series) -> pd.Series:
    """prpw_115_gp_growth_vel_252d"""
    return (gp.pct_change(252).diff(63)).shift(252)

def prpw_116_rev_growth_vel_5d(revenue: pd.Series) -> pd.Series:
    """prpw_116_rev_growth_vel_5d"""
    return (revenue.pct_change(252).diff(63)).shift(5)

def prpw_117_rev_growth_vel_21d(revenue: pd.Series) -> pd.Series:
    """prpw_117_rev_growth_vel_21d"""
    return (revenue.pct_change(252).diff(63)).shift(21)

def prpw_118_rev_growth_vel_63d(revenue: pd.Series) -> pd.Series:
    """prpw_118_rev_growth_vel_63d"""
    return (revenue.pct_change(252).diff(63)).shift(63)

def prpw_119_rev_growth_vel_126d(revenue: pd.Series) -> pd.Series:
    """prpw_119_rev_growth_vel_126d"""
    return (revenue.pct_change(252).diff(63)).shift(126)

def prpw_120_rev_growth_vel_252d(revenue: pd.Series) -> pd.Series:
    """prpw_120_rev_growth_vel_252d"""
    return (revenue.pct_change(252).diff(63)).shift(252)

def prpw_121_margin_expansion_index_5d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_121_margin_expansion_index_5d"""
    return ((_safe_div(gp, revenue)).diff(63)).shift(5)

def prpw_122_margin_expansion_index_21d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_122_margin_expansion_index_21d"""
    return ((_safe_div(gp, revenue)).diff(63)).shift(21)

def prpw_123_margin_expansion_index_63d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_123_margin_expansion_index_63d"""
    return ((_safe_div(gp, revenue)).diff(63)).shift(63)

def prpw_124_margin_expansion_index_126d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_124_margin_expansion_index_126d"""
    return ((_safe_div(gp, revenue)).diff(63)).shift(126)

def prpw_125_margin_expansion_index_252d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """prpw_125_margin_expansion_index_252d"""
    return ((_safe_div(gp, revenue)).diff(63)).shift(252)

def prpw_126_sticky_cost_index_5d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_126_sticky_cost_index_5d"""
    return (_safe_div(cor.pct_change(252), revenue.pct_change(252).clip(lower=_EPS))).shift(5)

def prpw_127_sticky_cost_index_21d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_127_sticky_cost_index_21d"""
    return (_safe_div(cor.pct_change(252), revenue.pct_change(252).clip(lower=_EPS))).shift(21)

def prpw_128_sticky_cost_index_63d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_128_sticky_cost_index_63d"""
    return (_safe_div(cor.pct_change(252), revenue.pct_change(252).clip(lower=_EPS))).shift(63)

def prpw_129_sticky_cost_index_126d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_129_sticky_cost_index_126d"""
    return (_safe_div(cor.pct_change(252), revenue.pct_change(252).clip(lower=_EPS))).shift(126)

def prpw_130_sticky_cost_index_252d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_130_sticky_cost_index_252d"""
    return (_safe_div(cor.pct_change(252), revenue.pct_change(252).clip(lower=_EPS))).shift(252)

def prpw_131_pricing_power_z_5d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_131_pricing_power_z_5d"""
    return (_zscore_rolling(_safe_div(revenue.pct_change(252), cor.pct_change(252)), 1260)).shift(5)

def prpw_132_pricing_power_z_21d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_132_pricing_power_z_21d"""
    return (_zscore_rolling(_safe_div(revenue.pct_change(252), cor.pct_change(252)), 1260)).shift(21)

def prpw_133_pricing_power_z_63d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_133_pricing_power_z_63d"""
    return (_zscore_rolling(_safe_div(revenue.pct_change(252), cor.pct_change(252)), 1260)).shift(63)

def prpw_134_pricing_power_z_126d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_134_pricing_power_z_126d"""
    return (_zscore_rolling(_safe_div(revenue.pct_change(252), cor.pct_change(252)), 1260)).shift(126)

def prpw_135_pricing_power_z_252d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_135_pricing_power_z_252d"""
    return (_zscore_rolling(_safe_div(revenue.pct_change(252), cor.pct_change(252)), 1260)).shift(252)

def prpw_136_real_rev_growth_proxy_5d(revenue: pd.Series) -> pd.Series:
    """prpw_136_real_rev_growth_proxy_5d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(5)

def prpw_137_real_rev_growth_proxy_21d(revenue: pd.Series) -> pd.Series:
    """prpw_137_real_rev_growth_proxy_21d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(21)

def prpw_138_real_rev_growth_proxy_63d(revenue: pd.Series) -> pd.Series:
    """prpw_138_real_rev_growth_proxy_63d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(63)

def prpw_139_real_rev_growth_proxy_126d(revenue: pd.Series) -> pd.Series:
    """prpw_139_real_rev_growth_proxy_126d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(126)

def prpw_140_real_rev_growth_proxy_252d(revenue: pd.Series) -> pd.Series:
    """prpw_140_real_rev_growth_proxy_252d"""
    return (revenue.pct_change(252) - _rolling_mean(revenue.pct_change(252), 1260)).shift(252)

def prpw_141_value_add_proxy_5d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_141_value_add_proxy_5d"""
    return (_safe_div(revenue - cor, revenue)).shift(5)

def prpw_142_value_add_proxy_21d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_142_value_add_proxy_21d"""
    return (_safe_div(revenue - cor, revenue)).shift(21)

def prpw_143_value_add_proxy_63d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_143_value_add_proxy_63d"""
    return (_safe_div(revenue - cor, revenue)).shift(63)

def prpw_144_value_add_proxy_126d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_144_value_add_proxy_126d"""
    return (_safe_div(revenue - cor, revenue)).shift(126)

def prpw_145_value_add_proxy_252d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """prpw_145_value_add_proxy_252d"""
    return (_safe_div(revenue - cor, revenue)).shift(252)

def prpw_146_asset_util_chg_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_146_asset_util_chg_5d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(5)

def prpw_147_asset_util_chg_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_147_asset_util_chg_21d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(21)

def prpw_148_asset_util_chg_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_148_asset_util_chg_63d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(63)

def prpw_149_asset_util_chg_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_149_asset_util_chg_126d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(126)

def prpw_150_asset_util_chg_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """prpw_150_asset_util_chg_252d"""
    return ((_safe_div(revenue, assets)).diff(252)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V65_REGISTRY = {
    "prpw_076_rev_z_5d": {"inputs": ['revenue'], "func": prpw_076_rev_z_5d},
    "prpw_077_rev_z_21d": {"inputs": ['revenue'], "func": prpw_077_rev_z_21d},
    "prpw_078_rev_z_63d": {"inputs": ['revenue'], "func": prpw_078_rev_z_63d},
    "prpw_079_rev_z_126d": {"inputs": ['revenue'], "func": prpw_079_rev_z_126d},
    "prpw_080_rev_z_252d": {"inputs": ['revenue'], "func": prpw_080_rev_z_252d},
    "prpw_081_gp_m_z_5d": {"inputs": ['revenue', 'gp'], "func": prpw_081_gp_m_z_5d},
    "prpw_082_gp_m_z_21d": {"inputs": ['revenue', 'gp'], "func": prpw_082_gp_m_z_21d},
    "prpw_083_gp_m_z_63d": {"inputs": ['revenue', 'gp'], "func": prpw_083_gp_m_z_63d},
    "prpw_084_gp_m_z_126d": {"inputs": ['revenue', 'gp'], "func": prpw_084_gp_m_z_126d},
    "prpw_085_gp_m_z_252d": {"inputs": ['revenue', 'gp'], "func": prpw_085_gp_m_z_252d},
    "prpw_086_ebit_m_z_5d": {"inputs": ['revenue', 'ebit'], "func": prpw_086_ebit_m_z_5d},
    "prpw_087_ebit_m_z_21d": {"inputs": ['revenue', 'ebit'], "func": prpw_087_ebit_m_z_21d},
    "prpw_088_ebit_m_z_63d": {"inputs": ['revenue', 'ebit'], "func": prpw_088_ebit_m_z_63d},
    "prpw_089_ebit_m_z_126d": {"inputs": ['revenue', 'ebit'], "func": prpw_089_ebit_m_z_126d},
    "prpw_090_ebit_m_z_252d": {"inputs": ['revenue', 'ebit'], "func": prpw_090_ebit_m_z_252d},
    "prpw_091_cor_rev_z_5d": {"inputs": ['revenue', 'cor'], "func": prpw_091_cor_rev_z_5d},
    "prpw_092_cor_rev_z_21d": {"inputs": ['revenue', 'cor'], "func": prpw_092_cor_rev_z_21d},
    "prpw_093_cor_rev_z_63d": {"inputs": ['revenue', 'cor'], "func": prpw_093_cor_rev_z_63d},
    "prpw_094_cor_rev_z_126d": {"inputs": ['revenue', 'cor'], "func": prpw_094_cor_rev_z_126d},
    "prpw_095_cor_rev_z_252d": {"inputs": ['revenue', 'cor'], "func": prpw_095_cor_rev_z_252d},
    "prpw_096_markup_proxy_5d": {"inputs": ['revenue', 'cor'], "func": prpw_096_markup_proxy_5d},
    "prpw_097_markup_proxy_21d": {"inputs": ['revenue', 'cor'], "func": prpw_097_markup_proxy_21d},
    "prpw_098_markup_proxy_63d": {"inputs": ['revenue', 'cor'], "func": prpw_098_markup_proxy_63d},
    "prpw_099_markup_proxy_126d": {"inputs": ['revenue', 'cor'], "func": prpw_099_markup_proxy_126d},
    "prpw_100_markup_proxy_252d": {"inputs": ['revenue', 'cor'], "func": prpw_100_markup_proxy_252d},
    "prpw_101_operating_efficiency_5d": {"inputs": ['revenue', 'cor', 'sga'], "func": prpw_101_operating_efficiency_5d},
    "prpw_102_operating_efficiency_21d": {"inputs": ['revenue', 'cor', 'sga'], "func": prpw_102_operating_efficiency_21d},
    "prpw_103_operating_efficiency_63d": {"inputs": ['revenue', 'cor', 'sga'], "func": prpw_103_operating_efficiency_63d},
    "prpw_104_operating_efficiency_126d": {"inputs": ['revenue', 'cor', 'sga'], "func": prpw_104_operating_efficiency_126d},
    "prpw_105_operating_efficiency_252d": {"inputs": ['revenue', 'cor', 'sga'], "func": prpw_105_operating_efficiency_252d},
    "prpw_106_incremental_margin_5d": {"inputs": ['revenue', 'ebit'], "func": prpw_106_incremental_margin_5d},
    "prpw_107_incremental_margin_21d": {"inputs": ['revenue', 'ebit'], "func": prpw_107_incremental_margin_21d},
    "prpw_108_incremental_margin_63d": {"inputs": ['revenue', 'ebit'], "func": prpw_108_incremental_margin_63d},
    "prpw_109_incremental_margin_126d": {"inputs": ['revenue', 'ebit'], "func": prpw_109_incremental_margin_126d},
    "prpw_110_incremental_margin_252d": {"inputs": ['revenue', 'ebit'], "func": prpw_110_incremental_margin_252d},
    "prpw_111_gp_growth_vel_5d": {"inputs": ['gp'], "func": prpw_111_gp_growth_vel_5d},
    "prpw_112_gp_growth_vel_21d": {"inputs": ['gp'], "func": prpw_112_gp_growth_vel_21d},
    "prpw_113_gp_growth_vel_63d": {"inputs": ['gp'], "func": prpw_113_gp_growth_vel_63d},
    "prpw_114_gp_growth_vel_126d": {"inputs": ['gp'], "func": prpw_114_gp_growth_vel_126d},
    "prpw_115_gp_growth_vel_252d": {"inputs": ['gp'], "func": prpw_115_gp_growth_vel_252d},
    "prpw_116_rev_growth_vel_5d": {"inputs": ['revenue'], "func": prpw_116_rev_growth_vel_5d},
    "prpw_117_rev_growth_vel_21d": {"inputs": ['revenue'], "func": prpw_117_rev_growth_vel_21d},
    "prpw_118_rev_growth_vel_63d": {"inputs": ['revenue'], "func": prpw_118_rev_growth_vel_63d},
    "prpw_119_rev_growth_vel_126d": {"inputs": ['revenue'], "func": prpw_119_rev_growth_vel_126d},
    "prpw_120_rev_growth_vel_252d": {"inputs": ['revenue'], "func": prpw_120_rev_growth_vel_252d},
    "prpw_121_margin_expansion_index_5d": {"inputs": ['revenue', 'gp'], "func": prpw_121_margin_expansion_index_5d},
    "prpw_122_margin_expansion_index_21d": {"inputs": ['revenue', 'gp'], "func": prpw_122_margin_expansion_index_21d},
    "prpw_123_margin_expansion_index_63d": {"inputs": ['revenue', 'gp'], "func": prpw_123_margin_expansion_index_63d},
    "prpw_124_margin_expansion_index_126d": {"inputs": ['revenue', 'gp'], "func": prpw_124_margin_expansion_index_126d},
    "prpw_125_margin_expansion_index_252d": {"inputs": ['revenue', 'gp'], "func": prpw_125_margin_expansion_index_252d},
    "prpw_126_sticky_cost_index_5d": {"inputs": ['revenue', 'cor'], "func": prpw_126_sticky_cost_index_5d},
    "prpw_127_sticky_cost_index_21d": {"inputs": ['revenue', 'cor'], "func": prpw_127_sticky_cost_index_21d},
    "prpw_128_sticky_cost_index_63d": {"inputs": ['revenue', 'cor'], "func": prpw_128_sticky_cost_index_63d},
    "prpw_129_sticky_cost_index_126d": {"inputs": ['revenue', 'cor'], "func": prpw_129_sticky_cost_index_126d},
    "prpw_130_sticky_cost_index_252d": {"inputs": ['revenue', 'cor'], "func": prpw_130_sticky_cost_index_252d},
    "prpw_131_pricing_power_z_5d": {"inputs": ['revenue', 'cor'], "func": prpw_131_pricing_power_z_5d},
    "prpw_132_pricing_power_z_21d": {"inputs": ['revenue', 'cor'], "func": prpw_132_pricing_power_z_21d},
    "prpw_133_pricing_power_z_63d": {"inputs": ['revenue', 'cor'], "func": prpw_133_pricing_power_z_63d},
    "prpw_134_pricing_power_z_126d": {"inputs": ['revenue', 'cor'], "func": prpw_134_pricing_power_z_126d},
    "prpw_135_pricing_power_z_252d": {"inputs": ['revenue', 'cor'], "func": prpw_135_pricing_power_z_252d},
    "prpw_136_real_rev_growth_proxy_5d": {"inputs": ['revenue'], "func": prpw_136_real_rev_growth_proxy_5d},
    "prpw_137_real_rev_growth_proxy_21d": {"inputs": ['revenue'], "func": prpw_137_real_rev_growth_proxy_21d},
    "prpw_138_real_rev_growth_proxy_63d": {"inputs": ['revenue'], "func": prpw_138_real_rev_growth_proxy_63d},
    "prpw_139_real_rev_growth_proxy_126d": {"inputs": ['revenue'], "func": prpw_139_real_rev_growth_proxy_126d},
    "prpw_140_real_rev_growth_proxy_252d": {"inputs": ['revenue'], "func": prpw_140_real_rev_growth_proxy_252d},
    "prpw_141_value_add_proxy_5d": {"inputs": ['revenue', 'cor'], "func": prpw_141_value_add_proxy_5d},
    "prpw_142_value_add_proxy_21d": {"inputs": ['revenue', 'cor'], "func": prpw_142_value_add_proxy_21d},
    "prpw_143_value_add_proxy_63d": {"inputs": ['revenue', 'cor'], "func": prpw_143_value_add_proxy_63d},
    "prpw_144_value_add_proxy_126d": {"inputs": ['revenue', 'cor'], "func": prpw_144_value_add_proxy_126d},
    "prpw_145_value_add_proxy_252d": {"inputs": ['revenue', 'cor'], "func": prpw_145_value_add_proxy_252d},
    "prpw_146_asset_util_chg_5d": {"inputs": ['revenue', 'assets'], "func": prpw_146_asset_util_chg_5d},
    "prpw_147_asset_util_chg_21d": {"inputs": ['revenue', 'assets'], "func": prpw_147_asset_util_chg_21d},
    "prpw_148_asset_util_chg_63d": {"inputs": ['revenue', 'assets'], "func": prpw_148_asset_util_chg_63d},
    "prpw_149_asset_util_chg_126d": {"inputs": ['revenue', 'assets'], "func": prpw_149_asset_util_chg_126d},
    "prpw_150_asset_util_chg_252d": {"inputs": ['revenue', 'assets'], "func": prpw_150_asset_util_chg_252d},
}
