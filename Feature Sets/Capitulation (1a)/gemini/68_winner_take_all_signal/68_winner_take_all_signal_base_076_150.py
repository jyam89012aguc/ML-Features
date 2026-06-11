"""
68_winner_take_all_signal — Base Features 076-150
Domain: Market share growth proxy
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

def wtas_076_rev_rank_1y_5d(revenue: pd.Series) -> pd.Series:
    """wtas_076_rev_rank_1y_5d"""
    return (_zscore_rolling(revenue, 252)).shift(5)

def wtas_077_rev_rank_1y_21d(revenue: pd.Series) -> pd.Series:
    """wtas_077_rev_rank_1y_21d"""
    return (_zscore_rolling(revenue, 252)).shift(21)

def wtas_078_rev_rank_1y_63d(revenue: pd.Series) -> pd.Series:
    """wtas_078_rev_rank_1y_63d"""
    return (_zscore_rolling(revenue, 252)).shift(63)

def wtas_079_rev_rank_1y_126d(revenue: pd.Series) -> pd.Series:
    """wtas_079_rev_rank_1y_126d"""
    return (_zscore_rolling(revenue, 252)).shift(126)

def wtas_080_rev_rank_1y_252d(revenue: pd.Series) -> pd.Series:
    """wtas_080_rev_rank_1y_252d"""
    return (_zscore_rolling(revenue, 252)).shift(252)

def wtas_081_mc_rank_1y_5d(marketcap: pd.Series) -> pd.Series:
    """wtas_081_mc_rank_1y_5d"""
    return (_zscore_rolling(marketcap, 252)).shift(5)

def wtas_082_mc_rank_1y_21d(marketcap: pd.Series) -> pd.Series:
    """wtas_082_mc_rank_1y_21d"""
    return (_zscore_rolling(marketcap, 252)).shift(21)

def wtas_083_mc_rank_1y_63d(marketcap: pd.Series) -> pd.Series:
    """wtas_083_mc_rank_1y_63d"""
    return (_zscore_rolling(marketcap, 252)).shift(63)

def wtas_084_mc_rank_1y_126d(marketcap: pd.Series) -> pd.Series:
    """wtas_084_mc_rank_1y_126d"""
    return (_zscore_rolling(marketcap, 252)).shift(126)

def wtas_085_mc_rank_1y_252d(marketcap: pd.Series) -> pd.Series:
    """wtas_085_mc_rank_1y_252d"""
    return (_zscore_rolling(marketcap, 252)).shift(252)

def wtas_086_winner_velocity_5d(revenue: pd.Series) -> pd.Series:
    """wtas_086_winner_velocity_5d"""
    return (revenue.pct_change(252).diff(21)).shift(5)

def wtas_087_winner_velocity_21d(revenue: pd.Series) -> pd.Series:
    """wtas_087_winner_velocity_21d"""
    return (revenue.pct_change(252).diff(21)).shift(21)

def wtas_088_winner_velocity_63d(revenue: pd.Series) -> pd.Series:
    """wtas_088_winner_velocity_63d"""
    return (revenue.pct_change(252).diff(21)).shift(63)

def wtas_089_winner_velocity_126d(revenue: pd.Series) -> pd.Series:
    """wtas_089_winner_velocity_126d"""
    return (revenue.pct_change(252).diff(21)).shift(126)

def wtas_090_winner_velocity_252d(revenue: pd.Series) -> pd.Series:
    """wtas_090_winner_velocity_252d"""
    return (revenue.pct_change(252).diff(21)).shift(252)

def wtas_091_winner_acceleration_5d(revenue: pd.Series) -> pd.Series:
    """wtas_091_winner_acceleration_5d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(5)

def wtas_092_winner_acceleration_21d(revenue: pd.Series) -> pd.Series:
    """wtas_092_winner_acceleration_21d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(21)

def wtas_093_winner_acceleration_63d(revenue: pd.Series) -> pd.Series:
    """wtas_093_winner_acceleration_63d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(63)

def wtas_094_winner_acceleration_126d(revenue: pd.Series) -> pd.Series:
    """wtas_094_winner_acceleration_126d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(126)

def wtas_095_winner_acceleration_252d(revenue: pd.Series) -> pd.Series:
    """wtas_095_winner_acceleration_252d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(252)

def wtas_096_scale_efficiency_5d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """wtas_096_scale_efficiency_5d"""
    return (_safe_div(revenue, sga + rnd)).shift(5)

def wtas_097_scale_efficiency_21d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """wtas_097_scale_efficiency_21d"""
    return (_safe_div(revenue, sga + rnd)).shift(21)

def wtas_098_scale_efficiency_63d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """wtas_098_scale_efficiency_63d"""
    return (_safe_div(revenue, sga + rnd)).shift(63)

def wtas_099_scale_efficiency_126d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """wtas_099_scale_efficiency_126d"""
    return (_safe_div(revenue, sga + rnd)).shift(126)

def wtas_100_scale_efficiency_252d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """wtas_100_scale_efficiency_252d"""
    return (_safe_div(revenue, sga + rnd)).shift(252)

def wtas_101_market_capture_rate_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_101_market_capture_rate_5d"""
    return _safe_div(revenue.diff(252), assets.shift(252))

def wtas_102_market_capture_rate_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_102_market_capture_rate_21d"""
    return _safe_div(revenue.diff(252), assets.shift(252))

def wtas_103_market_capture_rate_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_103_market_capture_rate_63d"""
    return _safe_div(revenue.diff(252), assets.shift(252))

def wtas_104_market_capture_rate_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_104_market_capture_rate_126d"""
    return _safe_div(revenue.diff(252), assets.shift(252))

def wtas_105_market_capture_rate_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_105_market_capture_rate_252d"""
    return _safe_div(revenue.diff(252), assets.shift(252))

def wtas_106_valuation_premium_5d(ps: pd.Series) -> pd.Series:
    """wtas_106_valuation_premium_5d"""
    return (ps / ps.rolling(1260).mean()).shift(5)

def wtas_107_valuation_premium_21d(ps: pd.Series) -> pd.Series:
    """wtas_107_valuation_premium_21d"""
    return (ps / ps.rolling(1260).mean()).shift(21)

def wtas_108_valuation_premium_63d(ps: pd.Series) -> pd.Series:
    """wtas_108_valuation_premium_63d"""
    return (ps / ps.rolling(1260).mean()).shift(63)

def wtas_109_valuation_premium_126d(ps: pd.Series) -> pd.Series:
    """wtas_109_valuation_premium_126d"""
    return (ps / ps.rolling(1260).mean()).shift(126)

def wtas_110_valuation_premium_252d(ps: pd.Series) -> pd.Series:
    """wtas_110_valuation_premium_252d"""
    return (ps / ps.rolling(1260).mean()).shift(252)

def wtas_111_growth_premium_5d(revenue: pd.Series) -> pd.Series:
    """wtas_111_growth_premium_5d"""
    return (revenue.pct_change(252) / revenue.pct_change(252).rolling(1260).mean()).shift(5)

def wtas_112_growth_premium_21d(revenue: pd.Series) -> pd.Series:
    """wtas_112_growth_premium_21d"""
    return (revenue.pct_change(252) / revenue.pct_change(252).rolling(1260).mean()).shift(21)

def wtas_113_growth_premium_63d(revenue: pd.Series) -> pd.Series:
    """wtas_113_growth_premium_63d"""
    return (revenue.pct_change(252) / revenue.pct_change(252).rolling(1260).mean()).shift(63)

def wtas_114_growth_premium_126d(revenue: pd.Series) -> pd.Series:
    """wtas_114_growth_premium_126d"""
    return (revenue.pct_change(252) / revenue.pct_change(252).rolling(1260).mean()).shift(126)

def wtas_115_growth_premium_252d(revenue: pd.Series) -> pd.Series:
    """wtas_115_growth_premium_252d"""
    return (revenue.pct_change(252) / revenue.pct_change(252).rolling(1260).mean()).shift(252)

def wtas_116_moat_expansion_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """wtas_116_moat_expansion_5d"""
    return ((_safe_div(ebit, revenue)).diff(252)).shift(5)

def wtas_117_moat_expansion_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """wtas_117_moat_expansion_21d"""
    return ((_safe_div(ebit, revenue)).diff(252)).shift(21)

def wtas_118_moat_expansion_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """wtas_118_moat_expansion_63d"""
    return ((_safe_div(ebit, revenue)).diff(252)).shift(63)

def wtas_119_moat_expansion_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """wtas_119_moat_expansion_126d"""
    return ((_safe_div(ebit, revenue)).diff(252)).shift(126)

def wtas_120_moat_expansion_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """wtas_120_moat_expansion_252d"""
    return ((_safe_div(ebit, revenue)).diff(252)).shift(252)

def wtas_121_network_value_g_5d(marketcap: pd.Series) -> pd.Series:
    """wtas_121_network_value_g_5d"""
    return (marketcap.pct_change(252)).shift(5)

def wtas_122_network_value_g_21d(marketcap: pd.Series) -> pd.Series:
    """wtas_122_network_value_g_21d"""
    return (marketcap.pct_change(252)).shift(21)

def wtas_123_network_value_g_63d(marketcap: pd.Series) -> pd.Series:
    """wtas_123_network_value_g_63d"""
    return (marketcap.pct_change(252)).shift(63)

def wtas_124_network_value_g_126d(marketcap: pd.Series) -> pd.Series:
    """wtas_124_network_value_g_126d"""
    return (marketcap.pct_change(252)).shift(126)

def wtas_125_network_value_g_252d(marketcap: pd.Series) -> pd.Series:
    """wtas_125_network_value_g_252d"""
    return (marketcap.pct_change(252)).shift(252)

def wtas_126_user_scale_proxy_5d(revenue: pd.Series) -> pd.Series:
    """wtas_126_user_scale_proxy_5d"""
    return (np.log1p(revenue)).shift(5)

def wtas_127_user_scale_proxy_21d(revenue: pd.Series) -> pd.Series:
    """wtas_127_user_scale_proxy_21d"""
    return (np.log1p(revenue)).shift(21)

def wtas_128_user_scale_proxy_63d(revenue: pd.Series) -> pd.Series:
    """wtas_128_user_scale_proxy_63d"""
    return (np.log1p(revenue)).shift(63)

def wtas_129_user_scale_proxy_126d(revenue: pd.Series) -> pd.Series:
    """wtas_129_user_scale_proxy_126d"""
    return (np.log1p(revenue)).shift(126)

def wtas_130_user_scale_proxy_252d(revenue: pd.Series) -> pd.Series:
    """wtas_130_user_scale_proxy_252d"""
    return (np.log1p(revenue)).shift(252)

def wtas_131_dominance_momentum_5d(revenue: pd.Series) -> pd.Series:
    """wtas_131_dominance_momentum_5d"""
    return (revenue.pct_change(63)).shift(5)

def wtas_132_dominance_momentum_21d(revenue: pd.Series) -> pd.Series:
    """wtas_132_dominance_momentum_21d"""
    return (revenue.pct_change(63)).shift(21)

def wtas_133_dominance_momentum_63d(revenue: pd.Series) -> pd.Series:
    """wtas_133_dominance_momentum_63d"""
    return (revenue.pct_change(63)).shift(63)

def wtas_134_dominance_momentum_126d(revenue: pd.Series) -> pd.Series:
    """wtas_134_dominance_momentum_126d"""
    return (revenue.pct_change(63)).shift(126)

def wtas_135_dominance_momentum_252d(revenue: pd.Series) -> pd.Series:
    """wtas_135_dominance_momentum_252d"""
    return (revenue.pct_change(63)).shift(252)

def wtas_136_relative_strength_fundamental_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_136_relative_strength_fundamental_5d"""
    return (_safe_div(revenue.pct_change(252), assets.pct_change(252))).shift(5)

def wtas_137_relative_strength_fundamental_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_137_relative_strength_fundamental_21d"""
    return (_safe_div(revenue.pct_change(252), assets.pct_change(252))).shift(21)

def wtas_138_relative_strength_fundamental_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_138_relative_strength_fundamental_63d"""
    return (_safe_div(revenue.pct_change(252), assets.pct_change(252))).shift(63)

def wtas_139_relative_strength_fundamental_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_139_relative_strength_fundamental_126d"""
    return (_safe_div(revenue.pct_change(252), assets.pct_change(252))).shift(126)

def wtas_140_relative_strength_fundamental_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """wtas_140_relative_strength_fundamental_252d"""
    return (_safe_div(revenue.pct_change(252), assets.pct_change(252))).shift(252)

def wtas_141_winner_gap_5d(revenue: pd.Series) -> pd.Series:
    """wtas_141_winner_gap_5d"""
    return (revenue - _rolling_mean(revenue, 1260)).shift(5)

def wtas_142_winner_gap_21d(revenue: pd.Series) -> pd.Series:
    """wtas_142_winner_gap_21d"""
    return (revenue - _rolling_mean(revenue, 1260)).shift(21)

def wtas_143_winner_gap_63d(revenue: pd.Series) -> pd.Series:
    """wtas_143_winner_gap_63d"""
    return (revenue - _rolling_mean(revenue, 1260)).shift(63)

def wtas_144_winner_gap_126d(revenue: pd.Series) -> pd.Series:
    """wtas_144_winner_gap_126d"""
    return (revenue - _rolling_mean(revenue, 1260)).shift(126)

def wtas_145_winner_gap_252d(revenue: pd.Series) -> pd.Series:
    """wtas_145_winner_gap_252d"""
    return (revenue - _rolling_mean(revenue, 1260)).shift(252)

def wtas_146_winner_ratio_5d(revenue: pd.Series) -> pd.Series:
    """wtas_146_winner_ratio_5d"""
    return (_safe_div(revenue, _rolling_max(revenue, 1260))).shift(5)

def wtas_147_winner_ratio_21d(revenue: pd.Series) -> pd.Series:
    """wtas_147_winner_ratio_21d"""
    return (_safe_div(revenue, _rolling_max(revenue, 1260))).shift(21)

def wtas_148_winner_ratio_63d(revenue: pd.Series) -> pd.Series:
    """wtas_148_winner_ratio_63d"""
    return (_safe_div(revenue, _rolling_max(revenue, 1260))).shift(63)

def wtas_149_winner_ratio_126d(revenue: pd.Series) -> pd.Series:
    """wtas_149_winner_ratio_126d"""
    return (_safe_div(revenue, _rolling_max(revenue, 1260))).shift(126)

def wtas_150_winner_ratio_252d(revenue: pd.Series) -> pd.Series:
    """wtas_150_winner_ratio_252d"""
    return (_safe_div(revenue, _rolling_max(revenue, 1260))).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V68_REGISTRY = {
    "wtas_076_rev_rank_1y_5d": {"inputs": ['revenue'], "func": wtas_076_rev_rank_1y_5d},
    "wtas_077_rev_rank_1y_21d": {"inputs": ['revenue'], "func": wtas_077_rev_rank_1y_21d},
    "wtas_078_rev_rank_1y_63d": {"inputs": ['revenue'], "func": wtas_078_rev_rank_1y_63d},
    "wtas_079_rev_rank_1y_126d": {"inputs": ['revenue'], "func": wtas_079_rev_rank_1y_126d},
    "wtas_080_rev_rank_1y_252d": {"inputs": ['revenue'], "func": wtas_080_rev_rank_1y_252d},
    "wtas_081_mc_rank_1y_5d": {"inputs": ['marketcap'], "func": wtas_081_mc_rank_1y_5d},
    "wtas_082_mc_rank_1y_21d": {"inputs": ['marketcap'], "func": wtas_082_mc_rank_1y_21d},
    "wtas_083_mc_rank_1y_63d": {"inputs": ['marketcap'], "func": wtas_083_mc_rank_1y_63d},
    "wtas_084_mc_rank_1y_126d": {"inputs": ['marketcap'], "func": wtas_084_mc_rank_1y_126d},
    "wtas_085_mc_rank_1y_252d": {"inputs": ['marketcap'], "func": wtas_085_mc_rank_1y_252d},
    "wtas_086_winner_velocity_5d": {"inputs": ['revenue'], "func": wtas_086_winner_velocity_5d},
    "wtas_087_winner_velocity_21d": {"inputs": ['revenue'], "func": wtas_087_winner_velocity_21d},
    "wtas_088_winner_velocity_63d": {"inputs": ['revenue'], "func": wtas_088_winner_velocity_63d},
    "wtas_089_winner_velocity_126d": {"inputs": ['revenue'], "func": wtas_089_winner_velocity_126d},
    "wtas_090_winner_velocity_252d": {"inputs": ['revenue'], "func": wtas_090_winner_velocity_252d},
    "wtas_091_winner_acceleration_5d": {"inputs": ['revenue'], "func": wtas_091_winner_acceleration_5d},
    "wtas_092_winner_acceleration_21d": {"inputs": ['revenue'], "func": wtas_092_winner_acceleration_21d},
    "wtas_093_winner_acceleration_63d": {"inputs": ['revenue'], "func": wtas_093_winner_acceleration_63d},
    "wtas_094_winner_acceleration_126d": {"inputs": ['revenue'], "func": wtas_094_winner_acceleration_126d},
    "wtas_095_winner_acceleration_252d": {"inputs": ['revenue'], "func": wtas_095_winner_acceleration_252d},
    "wtas_096_scale_efficiency_5d": {"inputs": ['revenue', 'sga', 'rnd'], "func": wtas_096_scale_efficiency_5d},
    "wtas_097_scale_efficiency_21d": {"inputs": ['revenue', 'sga', 'rnd'], "func": wtas_097_scale_efficiency_21d},
    "wtas_098_scale_efficiency_63d": {"inputs": ['revenue', 'sga', 'rnd'], "func": wtas_098_scale_efficiency_63d},
    "wtas_099_scale_efficiency_126d": {"inputs": ['revenue', 'sga', 'rnd'], "func": wtas_099_scale_efficiency_126d},
    "wtas_100_scale_efficiency_252d": {"inputs": ['revenue', 'sga', 'rnd'], "func": wtas_100_scale_efficiency_252d},
    "wtas_101_market_capture_rate_5d": {"inputs": ['revenue', 'assets'], "func": wtas_101_market_capture_rate_5d},
    "wtas_102_market_capture_rate_21d": {"inputs": ['revenue', 'assets'], "func": wtas_102_market_capture_rate_21d},
    "wtas_103_market_capture_rate_63d": {"inputs": ['revenue', 'assets'], "func": wtas_103_market_capture_rate_63d},
    "wtas_104_market_capture_rate_126d": {"inputs": ['revenue', 'assets'], "func": wtas_104_market_capture_rate_126d},
    "wtas_105_market_capture_rate_252d": {"inputs": ['revenue', 'assets'], "func": wtas_105_market_capture_rate_252d},
    "wtas_106_valuation_premium_5d": {"inputs": ['ps'], "func": wtas_106_valuation_premium_5d},
    "wtas_107_valuation_premium_21d": {"inputs": ['ps'], "func": wtas_107_valuation_premium_21d},
    "wtas_108_valuation_premium_63d": {"inputs": ['ps'], "func": wtas_108_valuation_premium_63d},
    "wtas_109_valuation_premium_126d": {"inputs": ['ps'], "func": wtas_109_valuation_premium_126d},
    "wtas_110_valuation_premium_252d": {"inputs": ['ps'], "func": wtas_110_valuation_premium_252d},
    "wtas_111_growth_premium_5d": {"inputs": ['revenue'], "func": wtas_111_growth_premium_5d},
    "wtas_112_growth_premium_21d": {"inputs": ['revenue'], "func": wtas_112_growth_premium_21d},
    "wtas_113_growth_premium_63d": {"inputs": ['revenue'], "func": wtas_113_growth_premium_63d},
    "wtas_114_growth_premium_126d": {"inputs": ['revenue'], "func": wtas_114_growth_premium_126d},
    "wtas_115_growth_premium_252d": {"inputs": ['revenue'], "func": wtas_115_growth_premium_252d},
    "wtas_116_moat_expansion_5d": {"inputs": ['revenue', 'ebit'], "func": wtas_116_moat_expansion_5d},
    "wtas_117_moat_expansion_21d": {"inputs": ['revenue', 'ebit'], "func": wtas_117_moat_expansion_21d},
    "wtas_118_moat_expansion_63d": {"inputs": ['revenue', 'ebit'], "func": wtas_118_moat_expansion_63d},
    "wtas_119_moat_expansion_126d": {"inputs": ['revenue', 'ebit'], "func": wtas_119_moat_expansion_126d},
    "wtas_120_moat_expansion_252d": {"inputs": ['revenue', 'ebit'], "func": wtas_120_moat_expansion_252d},
    "wtas_121_network_value_g_5d": {"inputs": ['marketcap'], "func": wtas_121_network_value_g_5d},
    "wtas_122_network_value_g_21d": {"inputs": ['marketcap'], "func": wtas_122_network_value_g_21d},
    "wtas_123_network_value_g_63d": {"inputs": ['marketcap'], "func": wtas_123_network_value_g_63d},
    "wtas_124_network_value_g_126d": {"inputs": ['marketcap'], "func": wtas_124_network_value_g_126d},
    "wtas_125_network_value_g_252d": {"inputs": ['marketcap'], "func": wtas_125_network_value_g_252d},
    "wtas_126_user_scale_proxy_5d": {"inputs": ['revenue'], "func": wtas_126_user_scale_proxy_5d},
    "wtas_127_user_scale_proxy_21d": {"inputs": ['revenue'], "func": wtas_127_user_scale_proxy_21d},
    "wtas_128_user_scale_proxy_63d": {"inputs": ['revenue'], "func": wtas_128_user_scale_proxy_63d},
    "wtas_129_user_scale_proxy_126d": {"inputs": ['revenue'], "func": wtas_129_user_scale_proxy_126d},
    "wtas_130_user_scale_proxy_252d": {"inputs": ['revenue'], "func": wtas_130_user_scale_proxy_252d},
    "wtas_131_dominance_momentum_5d": {"inputs": ['revenue'], "func": wtas_131_dominance_momentum_5d},
    "wtas_132_dominance_momentum_21d": {"inputs": ['revenue'], "func": wtas_132_dominance_momentum_21d},
    "wtas_133_dominance_momentum_63d": {"inputs": ['revenue'], "func": wtas_133_dominance_momentum_63d},
    "wtas_134_dominance_momentum_126d": {"inputs": ['revenue'], "func": wtas_134_dominance_momentum_126d},
    "wtas_135_dominance_momentum_252d": {"inputs": ['revenue'], "func": wtas_135_dominance_momentum_252d},
    "wtas_136_relative_strength_fundamental_5d": {"inputs": ['revenue', 'assets'], "func": wtas_136_relative_strength_fundamental_5d},
    "wtas_137_relative_strength_fundamental_21d": {"inputs": ['revenue', 'assets'], "func": wtas_137_relative_strength_fundamental_21d},
    "wtas_138_relative_strength_fundamental_63d": {"inputs": ['revenue', 'assets'], "func": wtas_138_relative_strength_fundamental_63d},
    "wtas_139_relative_strength_fundamental_126d": {"inputs": ['revenue', 'assets'], "func": wtas_139_relative_strength_fundamental_126d},
    "wtas_140_relative_strength_fundamental_252d": {"inputs": ['revenue', 'assets'], "func": wtas_140_relative_strength_fundamental_252d},
    "wtas_141_winner_gap_5d": {"inputs": ['revenue'], "func": wtas_141_winner_gap_5d},
    "wtas_142_winner_gap_21d": {"inputs": ['revenue'], "func": wtas_142_winner_gap_21d},
    "wtas_143_winner_gap_63d": {"inputs": ['revenue'], "func": wtas_143_winner_gap_63d},
    "wtas_144_winner_gap_126d": {"inputs": ['revenue'], "func": wtas_144_winner_gap_126d},
    "wtas_145_winner_gap_252d": {"inputs": ['revenue'], "func": wtas_145_winner_gap_252d},
    "wtas_146_winner_ratio_5d": {"inputs": ['revenue'], "func": wtas_146_winner_ratio_5d},
    "wtas_147_winner_ratio_21d": {"inputs": ['revenue'], "func": wtas_147_winner_ratio_21d},
    "wtas_148_winner_ratio_63d": {"inputs": ['revenue'], "func": wtas_148_winner_ratio_63d},
    "wtas_149_winner_ratio_126d": {"inputs": ['revenue'], "func": wtas_149_winner_ratio_126d},
    "wtas_150_winner_ratio_252d": {"inputs": ['revenue'], "func": wtas_150_winner_ratio_252d},
}
