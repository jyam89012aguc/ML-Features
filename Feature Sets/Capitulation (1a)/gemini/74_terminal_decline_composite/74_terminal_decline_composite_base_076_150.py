"""
74_terminal_decline_composite — Base Features 076-150
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

def tedc_076_rev_g_term_vel_5d(revenue: pd.Series) -> pd.Series:
    """tedc_076_rev_g_term_vel_5d"""
    return (revenue.pct_change(1260).diff(252)).shift(5)

def tedc_077_rev_g_term_vel_21d(revenue: pd.Series) -> pd.Series:
    """tedc_077_rev_g_term_vel_21d"""
    return (revenue.pct_change(1260).diff(252)).shift(21)

def tedc_078_rev_g_term_vel_63d(revenue: pd.Series) -> pd.Series:
    """tedc_078_rev_g_term_vel_63d"""
    return (revenue.pct_change(1260).diff(252)).shift(63)

def tedc_079_rev_g_term_vel_126d(revenue: pd.Series) -> pd.Series:
    """tedc_079_rev_g_term_vel_126d"""
    return (revenue.pct_change(1260).diff(252)).shift(126)

def tedc_080_rev_g_term_vel_252d(revenue: pd.Series) -> pd.Series:
    """tedc_080_rev_g_term_vel_252d"""
    return (revenue.pct_change(1260).diff(252)).shift(252)

def tedc_081_ni_g_term_vel_5d(netinc: pd.Series) -> pd.Series:
    """tedc_081_ni_g_term_vel_5d"""
    return (netinc.pct_change(1260).diff(252)).shift(5)

def tedc_082_ni_g_term_vel_21d(netinc: pd.Series) -> pd.Series:
    """tedc_082_ni_g_term_vel_21d"""
    return (netinc.pct_change(1260).diff(252)).shift(21)

def tedc_083_ni_g_term_vel_63d(netinc: pd.Series) -> pd.Series:
    """tedc_083_ni_g_term_vel_63d"""
    return (netinc.pct_change(1260).diff(252)).shift(63)

def tedc_084_ni_g_term_vel_126d(netinc: pd.Series) -> pd.Series:
    """tedc_084_ni_g_term_vel_126d"""
    return (netinc.pct_change(1260).diff(252)).shift(126)

def tedc_085_ni_g_term_vel_252d(netinc: pd.Series) -> pd.Series:
    """tedc_085_ni_g_term_vel_252d"""
    return (netinc.pct_change(1260).diff(252)).shift(252)

def tedc_086_mc_g_term_vel_5d(marketcap: pd.Series) -> pd.Series:
    """tedc_086_mc_g_term_vel_5d"""
    return (marketcap.pct_change(1260).diff(252)).shift(5)

def tedc_087_mc_g_term_vel_21d(marketcap: pd.Series) -> pd.Series:
    """tedc_087_mc_g_term_vel_21d"""
    return (marketcap.pct_change(1260).diff(252)).shift(21)

def tedc_088_mc_g_term_vel_63d(marketcap: pd.Series) -> pd.Series:
    """tedc_088_mc_g_term_vel_63d"""
    return (marketcap.pct_change(1260).diff(252)).shift(63)

def tedc_089_mc_g_term_vel_126d(marketcap: pd.Series) -> pd.Series:
    """tedc_089_mc_g_term_vel_126d"""
    return (marketcap.pct_change(1260).diff(252)).shift(126)

def tedc_090_mc_g_term_vel_252d(marketcap: pd.Series) -> pd.Series:
    """tedc_090_mc_g_term_vel_252d"""
    return (marketcap.pct_change(1260).diff(252)).shift(252)

def tedc_091_terminal_velocity_5d(revenue: pd.Series) -> pd.Series:
    """tedc_091_terminal_velocity_5d"""
    return (terminal_decline_index.diff(252)).shift(5)

def tedc_092_terminal_velocity_21d(revenue: pd.Series) -> pd.Series:
    """tedc_092_terminal_velocity_21d"""
    return (terminal_decline_index.diff(252)).shift(21)

def tedc_093_terminal_velocity_63d(revenue: pd.Series) -> pd.Series:
    """tedc_093_terminal_velocity_63d"""
    return (terminal_decline_index.diff(252)).shift(63)

def tedc_094_terminal_velocity_126d(revenue: pd.Series) -> pd.Series:
    """tedc_094_terminal_velocity_126d"""
    return (terminal_decline_index.diff(252)).shift(126)

def tedc_095_terminal_velocity_252d(revenue: pd.Series) -> pd.Series:
    """tedc_095_terminal_velocity_252d"""
    return (terminal_decline_index.diff(252)).shift(252)

def tedc_096_decay_acceleration_5d(revenue: pd.Series) -> pd.Series:
    """tedc_096_decay_acceleration_5d"""
    return (terminal_decline_index.diff(252).diff(63)).shift(5)

def tedc_097_decay_acceleration_21d(revenue: pd.Series) -> pd.Series:
    """tedc_097_decay_acceleration_21d"""
    return (terminal_decline_index.diff(252).diff(63)).shift(21)

def tedc_098_decay_acceleration_63d(revenue: pd.Series) -> pd.Series:
    """tedc_098_decay_acceleration_63d"""
    return (terminal_decline_index.diff(252).diff(63)).shift(63)

def tedc_099_decay_acceleration_126d(revenue: pd.Series) -> pd.Series:
    """tedc_099_decay_acceleration_126d"""
    return (terminal_decline_index.diff(252).diff(63)).shift(126)

def tedc_100_decay_acceleration_252d(revenue: pd.Series) -> pd.Series:
    """tedc_100_decay_acceleration_252d"""
    return (terminal_decline_index.diff(252).diff(63)).shift(252)

def tedc_101_secular_decline_ind_5d(revenue: pd.Series) -> pd.Series:
    """tedc_101_secular_decline_ind_5d"""
    return ((revenue.pct_change(1260) < 0) & (revenue.pct_change(252) < 0)).shift(5)

def tedc_102_secular_decline_ind_21d(revenue: pd.Series) -> pd.Series:
    """tedc_102_secular_decline_ind_21d"""
    return ((revenue.pct_change(1260) < 0) & (revenue.pct_change(252) < 0)).shift(21)

def tedc_103_secular_decline_ind_63d(revenue: pd.Series) -> pd.Series:
    """tedc_103_secular_decline_ind_63d"""
    return ((revenue.pct_change(1260) < 0) & (revenue.pct_change(252) < 0)).shift(63)

def tedc_104_secular_decline_ind_126d(revenue: pd.Series) -> pd.Series:
    """tedc_104_secular_decline_ind_126d"""
    return ((revenue.pct_change(1260) < 0) & (revenue.pct_change(252) < 0)).shift(126)

def tedc_105_secular_decline_ind_252d(revenue: pd.Series) -> pd.Series:
    """tedc_105_secular_decline_ind_252d"""
    return ((revenue.pct_change(1260) < 0) & (revenue.pct_change(252) < 0)).shift(252)

def tedc_106_value_trap_proxy_5d(revenue: pd.Series, ps: pd.Series) -> pd.Series:
    """tedc_106_value_trap_proxy_5d"""
    return ((ps < ps.rolling(1260).mean()) & (revenue.pct_change(252) < 0)).shift(5)

def tedc_107_value_trap_proxy_21d(revenue: pd.Series, ps: pd.Series) -> pd.Series:
    """tedc_107_value_trap_proxy_21d"""
    return ((ps < ps.rolling(1260).mean()) & (revenue.pct_change(252) < 0)).shift(21)

def tedc_108_value_trap_proxy_63d(revenue: pd.Series, ps: pd.Series) -> pd.Series:
    """tedc_108_value_trap_proxy_63d"""
    return ((ps < ps.rolling(1260).mean()) & (revenue.pct_change(252) < 0)).shift(63)

def tedc_109_value_trap_proxy_126d(revenue: pd.Series, ps: pd.Series) -> pd.Series:
    """tedc_109_value_trap_proxy_126d"""
    return ((ps < ps.rolling(1260).mean()) & (revenue.pct_change(252) < 0)).shift(126)

def tedc_110_value_trap_proxy_252d(revenue: pd.Series, ps: pd.Series) -> pd.Series:
    """tedc_110_value_trap_proxy_252d"""
    return ((ps < ps.rolling(1260).mean()) & (revenue.pct_change(252) < 0)).shift(252)

def tedc_111_asset_waste_index_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_111_asset_waste_index_5d"""
    return ((_safe_div(revenue, assets)).diff(1260)).shift(5)

def tedc_112_asset_waste_index_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_112_asset_waste_index_21d"""
    return ((_safe_div(revenue, assets)).diff(1260)).shift(21)

def tedc_113_asset_waste_index_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_113_asset_waste_index_63d"""
    return ((_safe_div(revenue, assets)).diff(1260)).shift(63)

def tedc_114_asset_waste_index_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_114_asset_waste_index_126d"""
    return ((_safe_div(revenue, assets)).diff(1260)).shift(126)

def tedc_115_asset_waste_index_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """tedc_115_asset_waste_index_252d"""
    return ((_safe_div(revenue, assets)).diff(1260)).shift(252)

def tedc_116_liab_per_rev_term_5d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """tedc_116_liab_per_rev_term_5d"""
    return ((_safe_div(liabs, revenue)).diff(1260)).shift(5)

def tedc_117_liab_per_rev_term_21d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """tedc_117_liab_per_rev_term_21d"""
    return ((_safe_div(liabs, revenue)).diff(1260)).shift(21)

def tedc_118_liab_per_rev_term_63d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """tedc_118_liab_per_rev_term_63d"""
    return ((_safe_div(liabs, revenue)).diff(1260)).shift(63)

def tedc_119_liab_per_rev_term_126d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """tedc_119_liab_per_rev_term_126d"""
    return ((_safe_div(liabs, revenue)).diff(1260)).shift(126)

def tedc_120_liab_per_rev_term_252d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """tedc_120_liab_per_rev_term_252d"""
    return ((_safe_div(liabs, revenue)).diff(1260)).shift(252)

def tedc_121_equity_burn_term_5d(equity: pd.Series) -> pd.Series:
    """tedc_121_equity_burn_term_5d"""
    return (equity.pct_change(1260)).shift(5)

def tedc_122_equity_burn_term_21d(equity: pd.Series) -> pd.Series:
    """tedc_122_equity_burn_term_21d"""
    return (equity.pct_change(1260)).shift(21)

def tedc_123_equity_burn_term_63d(equity: pd.Series) -> pd.Series:
    """tedc_123_equity_burn_term_63d"""
    return (equity.pct_change(1260)).shift(63)

def tedc_124_equity_burn_term_126d(equity: pd.Series) -> pd.Series:
    """tedc_124_equity_burn_term_126d"""
    return (equity.pct_change(1260)).shift(126)

def tedc_125_equity_burn_term_252d(equity: pd.Series) -> pd.Series:
    """tedc_125_equity_burn_term_252d"""
    return (equity.pct_change(1260)).shift(252)

def tedc_126_survival_probability_proxy_5d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """tedc_126_survival_probability_proxy_5d"""
    return (_safe_div(cashnequiv, liabs).rolling(1260).mean()).shift(5)

def tedc_127_survival_probability_proxy_21d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """tedc_127_survival_probability_proxy_21d"""
    return (_safe_div(cashnequiv, liabs).rolling(1260).mean()).shift(21)

def tedc_128_survival_probability_proxy_63d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """tedc_128_survival_probability_proxy_63d"""
    return (_safe_div(cashnequiv, liabs).rolling(1260).mean()).shift(63)

def tedc_129_survival_probability_proxy_126d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """tedc_129_survival_probability_proxy_126d"""
    return (_safe_div(cashnequiv, liabs).rolling(1260).mean()).shift(126)

def tedc_130_survival_probability_proxy_252d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """tedc_130_survival_probability_proxy_252d"""
    return (_safe_div(cashnequiv, liabs).rolling(1260).mean()).shift(252)

def tedc_131_terminal_exhaustion_5d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """tedc_131_terminal_exhaustion_5d"""
    return ((_safe_div(ocf, capex)).diff(1260)).shift(5)

def tedc_132_terminal_exhaustion_21d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """tedc_132_terminal_exhaustion_21d"""
    return ((_safe_div(ocf, capex)).diff(1260)).shift(21)

def tedc_133_terminal_exhaustion_63d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """tedc_133_terminal_exhaustion_63d"""
    return ((_safe_div(ocf, capex)).diff(1260)).shift(63)

def tedc_134_terminal_exhaustion_126d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """tedc_134_terminal_exhaustion_126d"""
    return ((_safe_div(ocf, capex)).diff(1260)).shift(126)

def tedc_135_terminal_exhaustion_252d(ocf: pd.Series, capex: pd.Series) -> pd.Series:
    """tedc_135_terminal_exhaustion_252d"""
    return ((_safe_div(ocf, capex)).diff(1260)).shift(252)

def tedc_136_market_irrelevance_proxy_5d(marketcap: pd.Series) -> pd.Series:
    """tedc_136_market_irrelevance_proxy_5d"""
    return (marketcap / marketcap.rolling(2520).max()).shift(5)

def tedc_137_market_irrelevance_proxy_21d(marketcap: pd.Series) -> pd.Series:
    """tedc_137_market_irrelevance_proxy_21d"""
    return (marketcap / marketcap.rolling(2520).max()).shift(21)

def tedc_138_market_irrelevance_proxy_63d(marketcap: pd.Series) -> pd.Series:
    """tedc_138_market_irrelevance_proxy_63d"""
    return (marketcap / marketcap.rolling(2520).max()).shift(63)

def tedc_139_market_irrelevance_proxy_126d(marketcap: pd.Series) -> pd.Series:
    """tedc_139_market_irrelevance_proxy_126d"""
    return (marketcap / marketcap.rolling(2520).max()).shift(126)

def tedc_140_market_irrelevance_proxy_252d(marketcap: pd.Series) -> pd.Series:
    """tedc_140_market_irrelevance_proxy_252d"""
    return (marketcap / marketcap.rolling(2520).max()).shift(252)

def tedc_141_secular_margin_collapse_5d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """tedc_141_secular_margin_collapse_5d"""
    return ((_safe_div(gp, revenue)).diff(1260)).shift(5)

def tedc_142_secular_margin_collapse_21d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """tedc_142_secular_margin_collapse_21d"""
    return ((_safe_div(gp, revenue)).diff(1260)).shift(21)

def tedc_143_secular_margin_collapse_63d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """tedc_143_secular_margin_collapse_63d"""
    return ((_safe_div(gp, revenue)).diff(1260)).shift(63)

def tedc_144_secular_margin_collapse_126d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """tedc_144_secular_margin_collapse_126d"""
    return ((_safe_div(gp, revenue)).diff(1260)).shift(126)

def tedc_145_secular_margin_collapse_252d(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """tedc_145_secular_margin_collapse_252d"""
    return ((_safe_div(gp, revenue)).diff(1260)).shift(252)

def tedc_146_terminal_composite_z_5d(revenue: pd.Series) -> pd.Series:
    """tedc_146_terminal_composite_z_5d"""
    return (_zscore_rolling(terminal_decline_index, 2520)).shift(5)

def tedc_147_terminal_composite_z_21d(revenue: pd.Series) -> pd.Series:
    """tedc_147_terminal_composite_z_21d"""
    return (_zscore_rolling(terminal_decline_index, 2520)).shift(21)

def tedc_148_terminal_composite_z_63d(revenue: pd.Series) -> pd.Series:
    """tedc_148_terminal_composite_z_63d"""
    return (_zscore_rolling(terminal_decline_index, 2520)).shift(63)

def tedc_149_terminal_composite_z_126d(revenue: pd.Series) -> pd.Series:
    """tedc_149_terminal_composite_z_126d"""
    return (_zscore_rolling(terminal_decline_index, 2520)).shift(126)

def tedc_150_terminal_composite_z_252d(revenue: pd.Series) -> pd.Series:
    """tedc_150_terminal_composite_z_252d"""
    return (_zscore_rolling(terminal_decline_index, 2520)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V74_REGISTRY = {
    "tedc_076_rev_g_term_vel_5d": {"inputs": ['revenue'], "func": tedc_076_rev_g_term_vel_5d},
    "tedc_077_rev_g_term_vel_21d": {"inputs": ['revenue'], "func": tedc_077_rev_g_term_vel_21d},
    "tedc_078_rev_g_term_vel_63d": {"inputs": ['revenue'], "func": tedc_078_rev_g_term_vel_63d},
    "tedc_079_rev_g_term_vel_126d": {"inputs": ['revenue'], "func": tedc_079_rev_g_term_vel_126d},
    "tedc_080_rev_g_term_vel_252d": {"inputs": ['revenue'], "func": tedc_080_rev_g_term_vel_252d},
    "tedc_081_ni_g_term_vel_5d": {"inputs": ['netinc'], "func": tedc_081_ni_g_term_vel_5d},
    "tedc_082_ni_g_term_vel_21d": {"inputs": ['netinc'], "func": tedc_082_ni_g_term_vel_21d},
    "tedc_083_ni_g_term_vel_63d": {"inputs": ['netinc'], "func": tedc_083_ni_g_term_vel_63d},
    "tedc_084_ni_g_term_vel_126d": {"inputs": ['netinc'], "func": tedc_084_ni_g_term_vel_126d},
    "tedc_085_ni_g_term_vel_252d": {"inputs": ['netinc'], "func": tedc_085_ni_g_term_vel_252d},
    "tedc_086_mc_g_term_vel_5d": {"inputs": ['marketcap'], "func": tedc_086_mc_g_term_vel_5d},
    "tedc_087_mc_g_term_vel_21d": {"inputs": ['marketcap'], "func": tedc_087_mc_g_term_vel_21d},
    "tedc_088_mc_g_term_vel_63d": {"inputs": ['marketcap'], "func": tedc_088_mc_g_term_vel_63d},
    "tedc_089_mc_g_term_vel_126d": {"inputs": ['marketcap'], "func": tedc_089_mc_g_term_vel_126d},
    "tedc_090_mc_g_term_vel_252d": {"inputs": ['marketcap'], "func": tedc_090_mc_g_term_vel_252d},
    "tedc_091_terminal_velocity_5d": {"inputs": ['revenue'], "func": tedc_091_terminal_velocity_5d},
    "tedc_092_terminal_velocity_21d": {"inputs": ['revenue'], "func": tedc_092_terminal_velocity_21d},
    "tedc_093_terminal_velocity_63d": {"inputs": ['revenue'], "func": tedc_093_terminal_velocity_63d},
    "tedc_094_terminal_velocity_126d": {"inputs": ['revenue'], "func": tedc_094_terminal_velocity_126d},
    "tedc_095_terminal_velocity_252d": {"inputs": ['revenue'], "func": tedc_095_terminal_velocity_252d},
    "tedc_096_decay_acceleration_5d": {"inputs": ['revenue'], "func": tedc_096_decay_acceleration_5d},
    "tedc_097_decay_acceleration_21d": {"inputs": ['revenue'], "func": tedc_097_decay_acceleration_21d},
    "tedc_098_decay_acceleration_63d": {"inputs": ['revenue'], "func": tedc_098_decay_acceleration_63d},
    "tedc_099_decay_acceleration_126d": {"inputs": ['revenue'], "func": tedc_099_decay_acceleration_126d},
    "tedc_100_decay_acceleration_252d": {"inputs": ['revenue'], "func": tedc_100_decay_acceleration_252d},
    "tedc_101_secular_decline_ind_5d": {"inputs": ['revenue'], "func": tedc_101_secular_decline_ind_5d},
    "tedc_102_secular_decline_ind_21d": {"inputs": ['revenue'], "func": tedc_102_secular_decline_ind_21d},
    "tedc_103_secular_decline_ind_63d": {"inputs": ['revenue'], "func": tedc_103_secular_decline_ind_63d},
    "tedc_104_secular_decline_ind_126d": {"inputs": ['revenue'], "func": tedc_104_secular_decline_ind_126d},
    "tedc_105_secular_decline_ind_252d": {"inputs": ['revenue'], "func": tedc_105_secular_decline_ind_252d},
    "tedc_106_value_trap_proxy_5d": {"inputs": ['revenue', 'ps'], "func": tedc_106_value_trap_proxy_5d},
    "tedc_107_value_trap_proxy_21d": {"inputs": ['revenue', 'ps'], "func": tedc_107_value_trap_proxy_21d},
    "tedc_108_value_trap_proxy_63d": {"inputs": ['revenue', 'ps'], "func": tedc_108_value_trap_proxy_63d},
    "tedc_109_value_trap_proxy_126d": {"inputs": ['revenue', 'ps'], "func": tedc_109_value_trap_proxy_126d},
    "tedc_110_value_trap_proxy_252d": {"inputs": ['revenue', 'ps'], "func": tedc_110_value_trap_proxy_252d},
    "tedc_111_asset_waste_index_5d": {"inputs": ['revenue', 'assets'], "func": tedc_111_asset_waste_index_5d},
    "tedc_112_asset_waste_index_21d": {"inputs": ['revenue', 'assets'], "func": tedc_112_asset_waste_index_21d},
    "tedc_113_asset_waste_index_63d": {"inputs": ['revenue', 'assets'], "func": tedc_113_asset_waste_index_63d},
    "tedc_114_asset_waste_index_126d": {"inputs": ['revenue', 'assets'], "func": tedc_114_asset_waste_index_126d},
    "tedc_115_asset_waste_index_252d": {"inputs": ['revenue', 'assets'], "func": tedc_115_asset_waste_index_252d},
    "tedc_116_liab_per_rev_term_5d": {"inputs": ['revenue', 'liabs'], "func": tedc_116_liab_per_rev_term_5d},
    "tedc_117_liab_per_rev_term_21d": {"inputs": ['revenue', 'liabs'], "func": tedc_117_liab_per_rev_term_21d},
    "tedc_118_liab_per_rev_term_63d": {"inputs": ['revenue', 'liabs'], "func": tedc_118_liab_per_rev_term_63d},
    "tedc_119_liab_per_rev_term_126d": {"inputs": ['revenue', 'liabs'], "func": tedc_119_liab_per_rev_term_126d},
    "tedc_120_liab_per_rev_term_252d": {"inputs": ['revenue', 'liabs'], "func": tedc_120_liab_per_rev_term_252d},
    "tedc_121_equity_burn_term_5d": {"inputs": ['equity'], "func": tedc_121_equity_burn_term_5d},
    "tedc_122_equity_burn_term_21d": {"inputs": ['equity'], "func": tedc_122_equity_burn_term_21d},
    "tedc_123_equity_burn_term_63d": {"inputs": ['equity'], "func": tedc_123_equity_burn_term_63d},
    "tedc_124_equity_burn_term_126d": {"inputs": ['equity'], "func": tedc_124_equity_burn_term_126d},
    "tedc_125_equity_burn_term_252d": {"inputs": ['equity'], "func": tedc_125_equity_burn_term_252d},
    "tedc_126_survival_probability_proxy_5d": {"inputs": ['liabs', 'cashnequiv'], "func": tedc_126_survival_probability_proxy_5d},
    "tedc_127_survival_probability_proxy_21d": {"inputs": ['liabs', 'cashnequiv'], "func": tedc_127_survival_probability_proxy_21d},
    "tedc_128_survival_probability_proxy_63d": {"inputs": ['liabs', 'cashnequiv'], "func": tedc_128_survival_probability_proxy_63d},
    "tedc_129_survival_probability_proxy_126d": {"inputs": ['liabs', 'cashnequiv'], "func": tedc_129_survival_probability_proxy_126d},
    "tedc_130_survival_probability_proxy_252d": {"inputs": ['liabs', 'cashnequiv'], "func": tedc_130_survival_probability_proxy_252d},
    "tedc_131_terminal_exhaustion_5d": {"inputs": ['ocf', 'capex'], "func": tedc_131_terminal_exhaustion_5d},
    "tedc_132_terminal_exhaustion_21d": {"inputs": ['ocf', 'capex'], "func": tedc_132_terminal_exhaustion_21d},
    "tedc_133_terminal_exhaustion_63d": {"inputs": ['ocf', 'capex'], "func": tedc_133_terminal_exhaustion_63d},
    "tedc_134_terminal_exhaustion_126d": {"inputs": ['ocf', 'capex'], "func": tedc_134_terminal_exhaustion_126d},
    "tedc_135_terminal_exhaustion_252d": {"inputs": ['ocf', 'capex'], "func": tedc_135_terminal_exhaustion_252d},
    "tedc_136_market_irrelevance_proxy_5d": {"inputs": ['marketcap'], "func": tedc_136_market_irrelevance_proxy_5d},
    "tedc_137_market_irrelevance_proxy_21d": {"inputs": ['marketcap'], "func": tedc_137_market_irrelevance_proxy_21d},
    "tedc_138_market_irrelevance_proxy_63d": {"inputs": ['marketcap'], "func": tedc_138_market_irrelevance_proxy_63d},
    "tedc_139_market_irrelevance_proxy_126d": {"inputs": ['marketcap'], "func": tedc_139_market_irrelevance_proxy_126d},
    "tedc_140_market_irrelevance_proxy_252d": {"inputs": ['marketcap'], "func": tedc_140_market_irrelevance_proxy_252d},
    "tedc_141_secular_margin_collapse_5d": {"inputs": ['revenue', 'gp'], "func": tedc_141_secular_margin_collapse_5d},
    "tedc_142_secular_margin_collapse_21d": {"inputs": ['revenue', 'gp'], "func": tedc_142_secular_margin_collapse_21d},
    "tedc_143_secular_margin_collapse_63d": {"inputs": ['revenue', 'gp'], "func": tedc_143_secular_margin_collapse_63d},
    "tedc_144_secular_margin_collapse_126d": {"inputs": ['revenue', 'gp'], "func": tedc_144_secular_margin_collapse_126d},
    "tedc_145_secular_margin_collapse_252d": {"inputs": ['revenue', 'gp'], "func": tedc_145_secular_margin_collapse_252d},
    "tedc_146_terminal_composite_z_5d": {"inputs": ['revenue'], "func": tedc_146_terminal_composite_z_5d},
    "tedc_147_terminal_composite_z_21d": {"inputs": ['revenue'], "func": tedc_147_terminal_composite_z_21d},
    "tedc_148_terminal_composite_z_63d": {"inputs": ['revenue'], "func": tedc_148_terminal_composite_z_63d},
    "tedc_149_terminal_composite_z_126d": {"inputs": ['revenue'], "func": tedc_149_terminal_composite_z_126d},
    "tedc_150_terminal_composite_z_252d": {"inputs": ['revenue'], "func": tedc_150_terminal_composite_z_252d},
}
